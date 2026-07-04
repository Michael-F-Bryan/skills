from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class FeedConfig:
    name: str
    url: str


@dataclass(frozen=True)
class Article:
    """Normalized RSS entry before persistence."""

    feed_name: str
    guid: str
    title: str
    link: str
    summary: str
    published_at: datetime | None


@dataclass(frozen=True)
class ScoredArticle:
    article: Article
    score: float


@dataclass(frozen=True)
class StoredArticle:
    id: int
    feed_name: str
    guid: str
    title: str
    link: str
    summary: str
    published_at: datetime | None
    score: float
    digested: bool


@dataclass(frozen=True)
class MailConfig:
    smtp_host: str
    smtp_port: int
    username: str
    password: str
    from_addr: str
    to_addrs: tuple[str, ...]
    use_tls: bool = True


@dataclass(frozen=True)
class AppConfig:
    db_path: str
    feeds: tuple[FeedConfig, ...]
    keywords: tuple[str, ...]
    score_threshold: float
    plugin_dir: str | None
    mail: MailConfig | None


class ConfigError(Exception):
    """Raised when configuration is missing or invalid."""

    def __init__(self, path: str, reason: str) -> None:
        self.path = path
        self.reason = reason
        super().__init__(f"Invalid config {path}: {reason}")


class FeedFetchError(Exception):
    """Raised when an RSS feed cannot be retrieved or parsed."""

    def __init__(self, feed_name: str, url: str, reason: str) -> None:
        self.feed_name = feed_name
        self.url = url
        self.reason = reason
        super().__init__(f"Feed {feed_name!r} ({url}): {reason}")


class MailDeliveryError(Exception):
    """Raised when digest email cannot be sent."""

    def __init__(self, recipient: str, reason: str) -> None:
        self.recipient = recipient
        self.reason = reason
        super().__init__(f"Mail to {recipient!r} failed: {reason}")


def score_article(article: Article, keywords: tuple[str, ...]) -> ScoredArticle:
    if not keywords:
        return ScoredArticle(article=article, score=0.0)
    haystack = f"{article.title}\n{article.summary}".lower()
    hits = sum(1 for keyword in keywords if keyword in haystack)
    return ScoredArticle(article=article, score=hits / len(keywords))


def passes_threshold(scored: ScoredArticle, threshold: float) -> bool:
    return scored.score >= threshold
