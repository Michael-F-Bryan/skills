# Larger greenfield: site audit CLI

## Task given to agent

Build a site audit CLI tool in Python in this directory. It should: crawl a website starting from a URL (same-domain only, configurable max pages), check each page for broken internal links, missing alt attributes on images, and missing/duplicate title tags, then produce a report as human-readable text or JSON (`--format` flag). Include a `crawl` subcommand for the full audit and a `check-page` subcommand for auditing a single page without crawling. Use pytest for tests. This will be maintained by our team long-term.

## What this probes

Medium-complexity greenfield with a real temptation to over-architect (crawler + checkers + reporters invites plugin registries and strategy patterns).

Grading questions:

- Size: 5–8 production files / 250–500 LOC is reasonable; 12+ files or 800+ LOC is slop.
- Injectable HTTP seam rather than hard-wired requests in domain logic?
- Do tests use the injection seam, or monkeypatch module globals (e.g. `httpx.Client`)?
- All tests passing, and verification status reported honestly?
- Reference run (2026-07-04, Composer): 8 files / 544 LOC, good architecture, but one failing test that monkeypatched `httpx.Client` despite an injectable fetcher seam existing — this motivated the module-global-monkeypatch self-audit line.
