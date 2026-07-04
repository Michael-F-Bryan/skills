from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import pytest

from newsletter.config import load_config
from newsletter.mail import build_digest_body, send_digest
from newsletter.plugins import apply_filters, load_filters
from newsletter.rss import fetch_feed_entries
from newsletter.types import passes_threshold, score_article
from newsletter.store import article_count, init_schema, insert_if_new, mark_digested, undigested_above
from newsletter.types import Article, FeedConfig, MailConfig, ScoredArticle


SAMPLE_RSS = b"""<?xml version="1.0"?>
<rss version="2.0"><channel>
<title>Test</title>
<item>
  <title>Python SQLite patterns</title>
  <link>https://example.com/a</link>
  <guid>a1</guid>
  <description>RSS and sqlite notes</description>
  <pubDate>Mon, 01 Jan 2024 12:00:00 GMT</pubDate>
</item>
<item>
  <title>Sponsored: buy widgets</title>
  <link>https://example.com/b</link>
  <guid>b1</guid>
  <description>advertisement</description>
</item>
</rss>"""


def test_score_article_counts_keyword_hits() -> None:
    article = Article(
        feed_name="test",
        guid="1",
        title="Python tooling",
        link="https://example.com",
        summary="sqlite and rss",
        published_at=None,
    )
    scored = score_article(article, ("python", "sqlite", "rss"))
    assert scored.score == pytest.approx(1.0)
    assert passes_threshold(scored, 0.5)


def test_store_insert_and_dedupe(tmp_path: Path) -> None:
    db_path = tmp_path / "news.db"
    init_schema(db_path)
    article = Article(
        feed_name="test",
        guid="g1",
        title="Title",
        link="https://example.com",
        summary="Body",
        published_at=datetime(2024, 1, 1, tzinfo=timezone.utc),
    )
    scored = ScoredArticle(article=article, score=0.8)

    assert insert_if_new(db_path, scored) is True
    assert insert_if_new(db_path, scored) is False
    assert article_count(db_path) == 1

    pending = undigested_above(db_path, 0.5)
    assert len(pending) == 1
    assert mark_digested(db_path, [pending[0].id]) == 1
    assert undigested_above(db_path, 0.5) == []


def test_fetch_feed_entries_with_injected_payload() -> None:
    feed = FeedConfig(name="test", url="https://example.com/feed.xml")
    entries = fetch_feed_entries(
        feed,
        urlopen_fn=lambda url, timeout: SAMPLE_RSS,
    )
    assert len(entries) == 2
    assert entries[0].title.startswith("Python")


def test_plugin_blocks_sponsored(tmp_path: Path) -> None:
    plugin_dir = tmp_path / "plugins"
    plugin_dir.mkdir()
    plugin_dir.joinpath("block.py").write_text(
        "from newsletter.types import Article\n"
        "def filter_article(article: Article) -> bool:\n"
        "    return 'sponsored' not in article.title.lower()\n",
        encoding="utf-8",
    )
    filters = load_filters(plugin_dir)
    assert len(filters) == 1

    blocked = Article("f", "1", "Sponsored deal", "", "", None)
    allowed = Article("f", "2", "Real news", "", "", None)
    assert apply_filters(blocked, filters) is False
    assert apply_filters(allowed, filters) is True


def test_load_config_validates_feeds(tmp_path: Path) -> None:
    path = tmp_path / "config.json"
    path.write_text(json.dumps({"db_path": "x.db", "feeds": []}), encoding="utf-8")
    with pytest.raises(Exception, match="non-empty"):
        load_config(path)


def test_send_digest_uses_injected_sender() -> None:
    captured: list[str] = []

    def fake_sender(mail: MailConfig, message) -> None:
        captured.append(message.get_content())

    mail = MailConfig(
        smtp_host="smtp.test",
        smtp_port=587,
        username="u",
        password="p",
        from_addr="from@test",
        to_addrs=("to@test",),
    )
    from newsletter.types import StoredArticle

    stored_article = StoredArticle(
        id=1,
        feed_name="f",
        guid="1",
        title="Python news",
        link="https://x",
        summary="sqlite",
        published_at=None,
        score=0.9,
        digested=False,
    )
    send_digest(mail, [stored_article], sender=fake_sender)
    assert "Python news" in captured[0]


def test_build_digest_body_empty() -> None:
    assert "No new articles" in build_digest_body([])


def test_cli_poll_end_to_end(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    from click.testing import CliRunner

    from newsletter.cli import cli

    config_path = tmp_path / "config.json"
    db_path = tmp_path / "news.db"
    plugin_dir = tmp_path / "plugins"
    plugin_dir.mkdir()
    plugin_dir.joinpath("block.py").write_text(
        "from newsletter.types import Article\n"
        "def filter_article(article: Article) -> bool:\n"
        "    return 'sponsored' not in article.title.lower()\n",
        encoding="utf-8",
    )

    config_path.write_text(
        json.dumps(
            {
                "db_path": str(db_path),
                "score_threshold": 0.3,
                "plugin_dir": str(plugin_dir),
                "keywords": ["python", "sqlite", "rss"],
                "feeds": [{"name": "test", "url": "https://example.com/feed.xml"}],
            }
        ),
        encoding="utf-8",
    )

    def fake_fetch(feed: FeedConfig):
        return fetch_feed_entries(
            feed,
            urlopen_fn=lambda url, timeout: SAMPLE_RSS,
        )

    monkeypatch.setattr("newsletter.cli.fetch_feed_entries", fake_fetch)

    runner = CliRunner()
    result = runner.invoke(cli, ["--config", str(config_path), "poll", "--json"])
    assert result.exit_code == 0, result.output
    payload = json.loads(result.output)
    assert payload["inserted"] == 1
    assert payload["skipped_filter"] == 1

    assert article_count(db_path) == 1
