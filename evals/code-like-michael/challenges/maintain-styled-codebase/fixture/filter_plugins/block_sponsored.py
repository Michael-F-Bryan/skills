from __future__ import annotations

from datetime import datetime, timezone

from newsletter.types import Article


def filter_article(article: Article) -> bool:
    """Drop articles whose titles look like sponsored content."""
    blocked = ("sponsored", "advertisement", "paid post")
    title = article.title.lower()
    return not any(token in title for token in blocked)
