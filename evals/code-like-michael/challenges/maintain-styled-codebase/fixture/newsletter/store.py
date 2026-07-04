from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from newsletter.types import ScoredArticle, StoredArticle


def init_schema(db_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with _connect(db_path) as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                feed_name TEXT NOT NULL,
                guid TEXT NOT NULL,
                title TEXT NOT NULL,
                link TEXT NOT NULL,
                summary TEXT NOT NULL,
                published_at TEXT,
                score REAL NOT NULL,
                digested INTEGER NOT NULL DEFAULT 0,
                inserted_at TEXT NOT NULL,
                UNIQUE(feed_name, guid)
            );
            """
        )


def insert_if_new(db_path: Path, scored: ScoredArticle) -> bool:
    article = scored.article
    published = article.published_at.isoformat() if article.published_at else None
    with _connect(db_path) as conn:
        cursor = conn.execute(
            """
            INSERT OR IGNORE INTO articles
                (feed_name, guid, title, link, summary, published_at, score, digested, inserted_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, 0, ?)
            """,
            (
                article.feed_name,
                article.guid,
                article.title,
                article.link,
                article.summary,
                published,
                scored.score,
                datetime.now(timezone.utc).isoformat(),
            ),
        )
        return cursor.rowcount == 1


def undigested_above(db_path: Path, threshold: float) -> list[StoredArticle]:
    with _connect(db_path) as conn:
        rows = conn.execute(
            """
            SELECT id, feed_name, guid, title, link, summary, published_at, score, digested
            FROM articles
            WHERE digested = 0 AND score >= ?
            ORDER BY score DESC, id ASC
            """,
            (threshold,),
        ).fetchall()
    return [_row_to_stored(row) for row in rows]


def mark_digested(db_path: Path, article_ids: list[int]) -> int:
    if not article_ids:
        return 0
    placeholders = ",".join("?" for _ in article_ids)
    with _connect(db_path) as conn:
        cursor = conn.execute(
            f"UPDATE articles SET digested = 1 WHERE id IN ({placeholders})",
            article_ids,
        )
        return cursor.rowcount


def article_count(db_path: Path) -> int:
    with _connect(db_path) as conn:
        row = conn.execute("SELECT COUNT(*) FROM articles").fetchone()
    return int(row[0]) if row else 0


def _connect(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def _row_to_stored(row: sqlite3.Row) -> StoredArticle:
    published_raw = row["published_at"]
    published_at = datetime.fromisoformat(published_raw) if published_raw else None
    return StoredArticle(
        id=int(row["id"]),
        feed_name=str(row["feed_name"]),
        guid=str(row["guid"]),
        title=str(row["title"]),
        link=str(row["link"]),
        summary=str(row["summary"]),
        published_at=published_at,
        score=float(row["score"]),
        digested=bool(row["digested"]),
    )
