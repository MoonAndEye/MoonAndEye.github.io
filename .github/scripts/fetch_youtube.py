#!/usr/bin/env python3
"""Fetch Marvin Builds videos into _data/youtube.json for Jekyll.

YouTube retired the public RSS endpoint used by the original version of this
script.  The channel pages still expose the public video metadata needed here,
so this script reads the ``/videos`` and ``/shorts`` pages and hydrates each
listed video from its watch page.

From GitHub's datacenter IPs YouTube answers a long video's watch page with a
"Sign in to confirm you're not a bot" check: the player data is empty, but the
page's ``ytInitialData`` still carries the title and the publish *day*.  Shorts
pages are not checked and give the exact timestamp.  To stay within that:

* only new videos and the newest few are fetched; everything else is reused
  from the previous ``_data/youtube.json``;
* a video with no publish date at all is left out of this run (with a workflow
  warning) instead of failing the whole update.

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
# Newest videos per section that are re-read on every run (title / description edits).
REFRESH_RECENT = int(os.environ.get("REFRESH_RECENT", "3"))
DESC_LIMIT = 200
OUT = Path(__file__).resolve().parents[2] / "_data" / "youtube.json"

USER_AGENT = "Mozilla/5.0 (compatible; marvinswift.com feed updater)"
RETRYABLE_HTTP_STATUS = {408, 425, 429, 500, 502, 503, 504}


def http_get(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    last_error = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                return response.read()
        except HTTPError as error:
            last_error = error
            if error.code not in RETRYABLE_HTTP_STATUS:
                raise
        except URLError as error:
            last_error = error
        if attempt < 3:
            # A 429 means "slow down": wait longer than for a dropped connection.
            rate_limited = isinstance(last_error, HTTPError) and last_error.code == 429
            time.sleep(2**attempt * (5 if rate_limited else 1))
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
    markers = (
        f"var {variable} = ",
        f"window.{variable} = ",
        f'window["{variable}"] = ',
        f"window['{variable}'] = ",
        f"{variable} = ",
    )
    for marker in markers:
        start = text.find(marker)
        if start >= 0:
            payload = text[start + len(marker):]
            return json.JSONDecoder().raw_decode(payload)[0]
    raise ValueError(f"YouTube page did not contain {variable}")


def fetch_page_data(url, variable):
    """Retry successful HTTP responses that are not usable YouTube pages."""
    last_error = None
    for attempt in range(3):
        html = http_get(url).decode("utf-8", errors="replace")
        try:
            return html, extract_json_assignment(html, variable)
        except ValueError as error:
            last_error = error
            if attempt == 2:
                break
            delay = 2**attempt
            print(
                f"warning: YouTube response lacked usable {variable}; "
                f"retrying in {delay}s ({attempt + 1}/3)",
                file=sys.stderr,
            )
            time.sleep(delay)

    raise ValueError(
        f"YouTube did not return usable {variable} from {url} after 3 attempts"
    ) from last_error


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
    _, data = fetch_page_data(CHANNEL_PAGES[section], "ytInitialData")
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


MONTHS = {
    name: number
    for number, name in enumerate(
        ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"),
        start=1,
    )
}
DAY_TEXT_RE = re.compile(r"\b(" + "|".join(MONTHS) + r")[a-z]*\.? (\d{1,2}), (\d{4})\b")


def parse_day_text(text):
    """'Oct 29, 2026' (also 'Premiered Oct 29, 2026') -> '2026-10-29', or ''."""
    match = DAY_TEXT_RE.search(text or "")
    if not match:
        return ""
    month, day, year = match.groups()
    return f"{int(year):04d}-{MONTHS[month]:02d}-{int(day):02d}"


def details_from_initial_data(data):
    """Title, description and publish day from a watch page's ytInitialData.

    This survives the bot check that empties ytInitialPlayerResponse.
    """
    primary = secondary = None
    for node in iter_dicts(data):
        primary = primary or node.get("videoPrimaryInfoRenderer")
        secondary = secondary or node.get("videoSecondaryInfoRenderer")
        if primary and secondary:
            break
    primary, secondary = primary or {}, secondary or {}
    return {
        "title": text_content(primary.get("title", {})),
        "published": parse_day_text(text_content(primary.get("dateText", {}))),
        "description": text_content(secondary.get("attributedDescription", {})),
    }


def fetch_watch_page(url):
    """Return the page HTML once it embeds YouTube's JSON, retrying otherwise."""
    for attempt in range(3):
        html = http_get(url).decode("utf-8", errors="replace")
        if "ytInitialPlayerResponse" in html or "ytInitialData" in html:
            return html
        if attempt < 2:
            delay = 2**attempt
            print(f"warning: {url} lacked page data; retrying in {delay}s ({attempt + 1}/3)", file=sys.stderr)
            time.sleep(delay)
    raise ValueError(f"YouTube did not return usable page data from {url} after 3 attempts")


def fetch_video_details(video_id, section):
    # A Short's own page is not bot-checked and has the exact timestamp.  For a
    # long video /shorts/<id> just redirects to the (checked) watch page.
    path = "shorts/" + video_id if section == "shorts" else "watch?v=" + video_id
    html = fetch_watch_page(f"https://www.youtube.com/{path}")

    try:
        player = extract_json_assignment(html, "ytInitialPlayerResponse")
    except ValueError:
        player = {}
    details = player.get("videoDetails", {})
    microformat = player.get("microformat", {}).get("playerMicroformatRenderer", {})
    title = details.get("title") or text_content(microformat.get("title", {}))
    description = details.get("shortDescription") or text_content(
        microformat.get("description", {})
    )
    published = normalize_timestamp(
        microformat.get("publishDate")
        or microformat.get("uploadDate")
        or extract_published_from_html(html)
    )

    if not (title and published and description):
        try:
            fallback = details_from_initial_data(extract_json_assignment(html, "ytInitialData"))
        except ValueError:
            fallback = {}
        title = title or fallback.get("title", "")
        description = description or fallback.get("description", "")
        published = published or fallback.get("published", "")  # day only, e.g. 2026-10-29
    return {
        "id": video_id,
        "title": title,
        "published": published,
        "thumbnail": thumbnail_url(video_id),
        "description": clip(description),
    }


def needs_fetch(index, item, previous):
    """New or undated videos, and the newest few, are read from YouTube again."""
    old = previous.get(item["id"])
    return index < REFRESH_RECENT or not old or not old.get("published")


def hydrate_item(index, item, previous, section):
    old = previous.get(item["id"], {})
    details = {}
    if needs_fetch(index, item, previous):
        try:
            details = fetch_video_details(item["id"], section)
        except Exception as error:  # Keep the update useful if one video is transiently unavailable.
            print(f"warning: could not hydrate {item['id']}: {error}", file=sys.stderr)

    published = details.get("published", "")
    if old.get("published") and (not published or len(published) == 10):
        published = old["published"]  # a stored exact time beats a missing or day-only one
    return {
        "id": item["id"],
        "title": details.get("title") or item["title"] or old.get("title", ""),
        "published": published,
        "thumbnail": old.get("thumbnail", item["thumbnail"]),
        "description": details.get("description") or old.get("description", ""),
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

        # One at a time: only a handful of pages are read, and bursts get a 429.
        with ThreadPoolExecutor(max_workers=1) as executor:
            hydrated = list(
                executor.map(
                    lambda pair: hydrate_item(pair[0], pair[1], previous, section),
                    enumerate(items),
                )
            )
        # Never publish a video without a date (the site shows it and puts it in
        # structured data).  Leave it out; the next run tries again.
        for item in hydrated:
            if not item["published"]:
                print(
                    f"::warning title=YouTube {section}::no publish date for {item['id']} "
                    f"({item['title']}); left out until a later run can read it"
                )
        result[section] = [item for item in hydrated if item["published"]]
        if not result[section]:
            print(f"error: no dated items for {section}", file=sys.stderr)
            sys.exit(1)
        print(f"{section}: {len(result[section])} of {len(items)} items from channel page")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
