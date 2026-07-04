# Greenfield: RSS ingestion pipeline CLI (harder probe)

## Unprompted arm

Build a Python CLI tool for an agent workflow that:
- Fetches one or more RSS feed URLs
- Parses articles (title, link, published date, summary)
- Deduplicates by URL across feeds
- Filters articles matching optional keyword list (case-insensitive, any keyword matches)
- Writes matching articles as markdown files to an output directory (one file per article, slugified filename)
- Supports a `run` subcommand that does the full pipeline and prints JSON summary to stdout (counts fetched, deduped, matched, written)
- Human-readable progress on stderr

Use Click, pytest, pyproject.toml. Put under `output/`.

## Explicit arm

Same task, but **must** read and apply `code-like-michael` skill first.

## Grading notes

This task is designed to trigger architecture slop. Reasonable: 5-8 files, 250-500 LOC. Slop: 12+ files, service/repository/factory layers, 800+ LOC.
