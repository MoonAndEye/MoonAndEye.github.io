#!/usr/bin/env python3
"""Fetch Marvin Builds playlist data into _data/youtube.json for Jekyll.

Data sources (per playlist):
- Default: YouTube RSS feed — no API key needed, returns the latest 15 items.
- If the env var YOUTUBE_API_KEY is set: YouTube Data API v3 playlistItems,
  50 items per page, paginated up to MAX_ITEMS.

Stdlib only so it runs on a bare GitHub Actions runner.
"""
import json
import os
import sys
import urllib.request
from pathlib import Path
from xml.etree import ElementTree as ET

CHANNEL_PLAYLISTS = {
    "videos": "UULFh3pnlNkGStSGikqGJG64Qw",   # long-form only
    "shorts": "UUSHh3pnlNkGStSGikqGJG64Qw",   # Shorts only
}
MAX_ITEMS = int(os.environ.get("MAX_ITEMS", "50"))
DESC_LIMIT = 200
OUT = Path(__file__).resolve().parents[2] / "_data" / "youtube.json"

ATOM_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "yt": "http://www.youtube.com/xml/schemas/2015",
    "media": "http://search.yahoo.com/mrss/",
}


def http_get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (marvinswift.com feed updater)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def clip(text):
    text = (text or "").strip()
    return text[:DESC_LIMIT] + ("…" if len(text) > DESC_LIMIT else "")


def fetch_rss(playlist_id):
    root = ET.fromstring(http_get(
        f"https://www.youtube.com/feeds/videos.xml?playlist_id={playlist_id}"))
    items = []
    for entry in root.findall("atom:entry", ATOM_NS):
        vid = entry.findtext("yt:videoId", default="", namespaces=ATOM_NS)
        if not vid:
            continue
        thumb = entry.find(".//media:thumbnail", ATOM_NS)
        items.append({
            "id": vid,
            "title": entry.findtext("atom:title", default="", namespaces=ATOM_NS),
            "published": (entry.findtext("atom:published", default="", namespaces=ATOM_NS))[:10],
            "thumbnail": thumb.get("url") if thumb is not None else f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",
            "description": clip(entry.findtext(".//media:description", default="", namespaces=ATOM_NS)),
        })
    return items


def fetch_api(playlist_id, key):
    items, page_token = [], None
    while len(items) < MAX_ITEMS:
        url = ("https://www.googleapis.com/youtube/v3/playlistItems"
               f"?part=snippet&maxResults=50&playlistId={playlist_id}&key={key}")
        if page_token:
            url += f"&pageToken={page_token}"
        data = json.loads(http_get(url))
        for item in data.get("items", []):
            sn = item["snippet"]
            vid = sn.get("resourceId", {}).get("videoId")
            if not vid:
                continue
            thumbs = sn.get("thumbnails", {})
            thumb = (thumbs.get("medium") or thumbs.get("high") or thumbs.get("default") or {}).get(
                "url", f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg")
            items.append({
                "id": vid,
                "title": sn.get("title", ""),
                "published": (sn.get("publishedAt") or "")[:10],
                "thumbnail": thumb,
                "description": clip(sn.get("description")),
            })
        page_token = data.get("nextPageToken")
        if not page_token:
            break
    return items[:MAX_ITEMS]


def main():
    api_key = os.environ.get("YOUTUBE_API_KEY", "").strip()
    source = "api" if api_key else "rss"
    result = {}
    for section, playlist_id in CHANNEL_PLAYLISTS.items():
        items = fetch_api(playlist_id, api_key) if api_key else fetch_rss(playlist_id)
        if not items:
            print(f"error: no items for {section} ({playlist_id}) — keeping old data", file=sys.stderr)
            sys.exit(1)
        result[section] = items
        print(f"{section}: {len(items)} items via {source}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
