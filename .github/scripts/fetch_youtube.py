#!/usr/bin/env python3
"""Fetch Marvin Builds videos into _data/youtube.json for Jekyll.

YouTube retired the public RSS endpoint used by the original version of this
script.  The channel pages still expose the public video metadata needed here,
so this script reads the ``/videos`` and ``/shorts`` pages and hydrates each
listed video from its watch page.

Stdlib only so it runs on a bare GitHub Actions runner.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path
from urllib.error import HTTPError, URLError

CHANNEL_HANDLE = "@MarvinBuildsAI"
CHANNEL_PAGES = {
    "videos": f"https://www.youtube.com/{CHANNEL_HANDLE}/videos",
    "shorts": f"https://www.youtube.com/{CHANNEL_HANDLE}/shorts",
}
MAX_ITEMS = int(os.environ.get("MAX_ITEMS", "50"))
DESC_LIMIT = 200
OUT = Path(__file__).resolve().parents[2] / "_data" / "youtube.json"

USER_AGENT = "Mozilla/5.0 (compatible; marvinswift.com feed updater)"
RETRYABLE_HTTP_STATUS = {408, 425, 429, 500, 502, 503, 504}


def http_get(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    last_error = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                return response.read()
        except HTTPError as error:
            last_error = error
            if error.code not in RETRYABLE_HTTP_STATUS:
                raise
        except URLError as error:
            last_error = error
        if attempt < 2:
            time.sleep(2**attempt)
    raise last_error


def clip(text):
    text = (text or "").strip()
    return text[:DESC_LIMIT] + ("…" if len(text) > DESC_LIMIT else "")


def normalize_timestamp(value):
    value = (value or "").strip()
    if not value:
        return ""
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc).isoformat()
    except ValueError:
        return value


def extract_json_assignment(text, variable):
    """Decode a JSON object assigned to a variable in a YouTube HTML page."""
    marker = f"var {variable} = "
    start = text.find(marker)
    if start < 0:
        marker = f"{variable} = "
        start = text.find(marker)
    if start < 0:
        raise ValueError(f"YouTube page did not contain {variable}")
    payload = text[start + len(marker):]
    return json.JSONDecoder().raw_decode(payload)[0]


def extract_published_from_html(html):
    """Read the publish date from alternate public metadata representations."""
    for tag in re.findall(r"<meta\b[^>]*>", html, flags=re.IGNORECASE):
        attributes = dict(
            re.findall(r'''([:\w-]+)\s*=\s*["']([^"']*)["']''', tag)
        )
        if attributes.get("itemprop") in {"datePublished", "uploadDate", "publishDate"}:
            if attributes.get("content"):
                return attributes["content"]

    for field in ("publishDate", "uploadDate", "datePublished"):
        match = re.search(rf'"{field}"\s*:\s*"([^"]+)"', html)
        if match:
            return match.group(1)
    return ""


def iter_dicts(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from iter_dicts(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_dicts(child)


def text_content(value):
    if not isinstance(value, dict):
        return ""
    if value.get("content"):
        return value["content"]
    if value.get("simpleText"):
        return value["simpleText"]
    return "".join(run.get("text", "") for run in value.get("runs", []))


def thumbnail_url(video_id):
    return f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"


def fetch_channel_items(section):
    html = http_get(CHANNEL_PAGES[section]).decode("utf-8", errors="replace")
    data = extract_json_assignment(html, "ytInitialData")
    items = []
    seen = set()

    for node in iter_dicts(data):
        item = node.get("lockupViewModel")
        if section == "videos" and isinstance(item, dict):
            if item.get("contentType") != "LOCKUP_CONTENT_TYPE_VIDEO":
                continue
            video_id = item.get("contentId", "")
            title = text_content(
                item.get("metadata", {})
                .get("lockupMetadataViewModel", {})
                .get("title", {})
            )
        elif section == "shorts" and isinstance(node.get("shortsLockupViewModel"), dict):
            item = node["shortsLockupViewModel"]
            endpoint = (
                item.get("onTap", {})
                .get("innertubeCommand", {})
                .get("reelWatchEndpoint", {})
            )
            video_id = endpoint.get("videoId", "")
            overlay = item.get("overlayMetadata", {})
            title = text_content(overlay.get("primaryText", {}))
            if not title:
                title = item.get("accessibilityText", "").split(",")[0]
        else:
            continue

        if not video_id or video_id in seen:
            continue
        seen.add(video_id)
        items.append({
            "id": video_id,
            "title": title,
            "published": "",
            "thumbnail": thumbnail_url(video_id),
            "description": "",
        })
        if len(items) >= MAX_ITEMS:
            break
    return items


def fetch_video_details(video_id):
    html = http_get(
        f"https://www.youtube.com/watch?v={video_id}"
    ).decode("utf-8", errors="replace")
    data = extract_json_assignment(html, "ytInitialPlayerResponse")
    details = data.get("videoDetails", {})
    microformat = data.get("microformat", {}).get("playerMicroformatRenderer", {})
    title = details.get("title") or text_content(microformat.get("title", {}))
    description = details.get("shortDescription") or text_content(
        microformat.get("description", {})
    )
    published = (
        microformat.get("publishDate")
        or microformat.get("uploadDate")
        or extract_published_from_html(html)
    )
    return {
        "id": video_id,
        "title": title,
        "published": normalize_timestamp(published),
        "thumbnail": thumbnail_url(video_id),
        "description": clip(description),
    }


def hydrate_item(item, previous):
    try:
        details = fetch_video_details(item["id"])
        old = previous.get(item["id"], {})
        if not details.get("title"):
            details["title"] = item["title"]
        if not details.get("published") and old.get("published"):
            details["published"] = old["published"]
        if not details.get("description") and old.get("description"):
            details["description"] = old["description"]
        if old.get("thumbnail"):
            details["thumbnail"] = old["thumbnail"]
        return details
    except Exception as error:  # Keep the update useful if one video is transiently unavailable.
        old = previous.get(item["id"], {})
        print(f"warning: could not hydrate {item['id']}: {error}", file=sys.stderr)
        return {
            **item,
            "published": old.get("published", ""),
            "thumbnail": old.get("thumbnail", item["thumbnail"]),
            "description": old.get("description", ""),
        }


def main():
    previous = {}
    if OUT.exists():
        old_data = json.loads(OUT.read_text(encoding="utf-8"))
        previous = {
            item.get("id"): item
            for section in ("videos", "shorts")
            for item in old_data.get(section, [])
            if item.get("id")
        }

    result = {}
    for section in ("videos", "shorts"):
        items = fetch_channel_items(section)
        if not items:
            print(f"error: no items found for {section}", file=sys.stderr)
            sys.exit(1)

        with ThreadPoolExecutor(max_workers=6) as executor:
            result[section] = list(
                executor.map(lambda item: hydrate_item(item, previous), items)
            )
        if any(not item.get("published") for item in result[section]):
            print(f"error: missing publish date for {section}", file=sys.stderr)
            sys.exit(1)
        print(f"{section}: {len(result[section])} items from channel page")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
