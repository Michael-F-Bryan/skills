from __future__ import annotations

from collections.abc import Callable
from datetime import datetime, timezone
from typing import Any
from urllib.error import URLError
from urllib.request import Request, urlopen

import feedparser

from newsletter.types import Article, FeedConfig, FeedFetchError

UrlOpener = Callable[[str, float], bytes]


def default_urlopen(url: str, timeout: float) -> bytes:
    request = Request(url, headers={"User-Agent": "newsletter-monitor/0.1"})
    with urlopen(request, timeout=timeout) as response:
        return response.read()


def fetch_feed_entries(
    feed: FeedConfig,
    *,
    urlopen_fn: UrlOpener = default_urlopen,
    timeout: float = 15.0,
) -> list[Article]:
    try:
        payload = urlopen_fn(feed.url, timeout)
    except URLError as exc:
        raise FeedFetchError(feed.name, feed.url, str(exc.reason or exc)) from exc

    parsed = feedparser.parse(payload)
    if parsed.bozo and not parsed.entries:
        reason = str(parsed.bozo_exception) if parsed.bozo_exception else "parse failed"
        raise FeedFetchError(feed.name, feed.url, reason)

    articles: list[Article] = []
    for entry in parsed.entries:
        guid = _entry_guid(entry, feed)
        if not guid:
            continue
        articles.append(
            Article(
                feed_name=feed.name,
                guid=guid,
                title=_clean_text(entry.get("title"), fallback="(untitled)"),
                link=_clean_text(entry.get("link"), fallback=""),
                summary=_clean_text(entry.get("summary"), fallback=""),
                published_at=_entry_published_at(entry),
            )
        )
    return articles


def _entry_guid(entry: Any, feed: FeedConfig) -> str | None:
    guid = entry.get("id") or entry.get("link") or entry.get("title")
    if not guid:
        return None
    return str(guid)


def _entry_published_at(entry: Any) -> datetime | None:
    published = entry.get("published_parsed") or entry.get("updated_parsed")
    if not published:
        return None
    return datetime(*published[:6], tzinfo=timezone.utc)


def _clean_text(value: object, *, fallback: str) -> str:
    if value is None:
        return fallback
    text = str(value).strip()
    return text or fallback
