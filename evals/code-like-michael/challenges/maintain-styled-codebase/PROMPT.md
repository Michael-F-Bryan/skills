# Maintenance: skill-styled codebase

## Task given to agent

The `project/` directory contains a newsletter monitoring CLI (RSS polling, relevance scoring, SQLite history, digest email, filter plugins). Add two features:

1. An `export` subcommand that writes stored articles to a JSON file, with optional `--since <ISO date>` and `--min-score <float>` filters.
2. Per-feed relevance keywords: a feed entry in the config may now specify its own `keywords` list which is used *instead of* the global keywords for articles from that feed.

Keep existing behaviour and tests passing. Run the tests.

## What this probes

The fixture follows code-like-michael conventions (typed models in `types.py`, single config loader, thin `cli.py`, injectable boundaries, behaviour tests). Grading questions:

- **Style maintenance:** does the new code match the existing conventions (typed models, thin CLI, module seams) or regress to dicts/inline logic?
- **Seam reuse:** does per-feed keywords flow through `FeedConfig` and `score_article`, or get bolted on with special cases in `cli.py`?
- **Config evolution:** is the config change backwards compatible (old configs without per-feed keywords still work)?
- **Tests:** are new tests behaviour-shaped and colocated with the existing suite?
- **No scope creep:** export does JSON only — did the agent resist adding CSV/XML/plugins?
