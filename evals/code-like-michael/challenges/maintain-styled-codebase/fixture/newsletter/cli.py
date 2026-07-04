from __future__ import annotations

import json
import sys
from pathlib import Path

import click

from newsletter.config import load_config
from newsletter.mail import build_digest_body, send_digest
from newsletter.plugins import apply_filters, load_filters
from newsletter.rss import fetch_feed_entries
from newsletter.store import article_count, init_schema, insert_if_new, mark_digested, undigested_above
from newsletter.types import AppConfig, ConfigError, FeedFetchError, MailDeliveryError, passes_threshold, score_article


@click.group()
@click.option(
    "--config",
    "config_path",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    required=True,
    help="JSON config with feeds, keywords, db_path, optional mail and plugin_dir.",
)
@click.pass_context
def cli(ctx: click.Context, config_path: Path) -> None:
    """Monitor RSS feeds, score relevance, store history, send digest email."""
    try:
        ctx.obj = load_config(config_path)
    except ConfigError as exc:
        raise click.ClickException(str(exc)) from exc


@cli.command("init-db")
@click.pass_obj
def init_db(config: AppConfig) -> None:
    """Create the SQLite schema if it does not exist."""
    db_path = Path(config.db_path)
    init_schema(db_path)
    click.echo(f"Initialized database at {db_path}")


@cli.command()
@click.option("--json", "as_json", is_flag=True, help="Emit machine-readable summary on stdout.")
@click.pass_obj
def poll(config: AppConfig, as_json: bool) -> None:
    """Fetch configured feeds, score articles, persist new matches."""
    db_path = Path(config.db_path)
    init_schema(db_path)
    filters = load_filters(Path(config.plugin_dir) if config.plugin_dir else None)

    inserted = skipped_low_score = skipped_filter = 0
    errors: list[str] = []

    for feed in config.feeds:
        try:
            entries = fetch_feed_entries(feed)
        except FeedFetchError as exc:
            errors.append(str(exc))
            continue

        for entry in entries:
            if filters and not apply_filters(entry, filters):
                skipped_filter += 1
                continue
            scored = score_article(entry, config.keywords)
            if not passes_threshold(scored, config.score_threshold):
                skipped_low_score += 1
                continue
            if insert_if_new(db_path, scored):
                inserted += 1

    summary = {
        "inserted": inserted,
        "skipped_low_score": skipped_low_score,
        "skipped_filter": skipped_filter,
        "errors": errors,
        "total_stored": article_count(db_path),
    }
    if as_json:
        click.echo(json.dumps(summary))
    else:
        click.echo(
            f"Poll complete: inserted={inserted}, skipped_low_score={skipped_low_score}, "
            f"skipped_filter={skipped_filter}, total_stored={summary['total_stored']}"
        )
        for error in errors:
            click.echo(error, err=True)
    if errors:
        sys.exit(1)


@cli.command()
@click.option("--dry-run", is_flag=True, help="Print digest body without sending mail.")
@click.option("--json", "as_json", is_flag=True, help="Emit machine-readable summary on stdout.")
@click.pass_obj
def digest(config: AppConfig, dry_run: bool, as_json: bool) -> None:
    """Email undigested articles above the score threshold."""
    db_path = Path(config.db_path)
    init_schema(db_path)
    pending = undigested_above(db_path, config.score_threshold)

    if not pending:
        payload = {"sent": 0, "marked_digested": 0, "article_ids": []}
        click.echo(json.dumps(payload) if as_json else "No undigested articles above threshold.")
        return

    if dry_run:
        click.echo(build_digest_body(pending))
        return

    if config.mail is None:
        raise click.ClickException("mail section required in config to send digest")
    try:
        send_digest(config.mail, pending)
    except MailDeliveryError as exc:
        raise click.ClickException(str(exc)) from exc

    marked = mark_digested(db_path, [article.id for article in pending])
    payload = {"sent": len(pending), "marked_digested": marked, "article_ids": [a.id for a in pending]}
    click.echo(json.dumps(payload) if as_json else f"Sent digest with {len(pending)} articles; marked {marked} digested.")


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
