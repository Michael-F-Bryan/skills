---
name: jake-tools
description: Use when operating or extending the jake-tools CLI for deterministic personal automation such as daily reports, AI monitoring, Clockify reconciliation, newsletters, or command discovery.
---

# jake-tools

`jake-tools` is Michael's internal Python CLI for agent-driven workflows. It is installed globally from `https://github.com/Michael-F-Bryan/jake-tools` and is available on `PATH`.

## Golden rule

The live CLI help is authoritative:

```bash
unset PYTHONPATH
jake-tools --help
jake-tools <command> --help
```

Do not copy internal pipeline logic into skills or ad hoc scripts merely because a command lacks a required seam. Report the product gap.

## Commands

```text
jake-tools ai-watch      Low-noise AI developments radar.
jake-tools clockify      Clockify helpers and Jira reconciliation.
jake-tools daily-report  Deterministic daily-report coordinator.
jake-tools newsletter    CSU Weekly Newsletter operations.
jake-tools transcribe    Audio transcription tasks.
jake-tools transcript    Structured transcript workflows and primitives.
```

For any transcript acquisition, diarisation, polishing, chaptering, minutes, or meeting-note task, **REQUIRED SKILL:** `transcript-workflows`. This skill deliberately does not duplicate transcript policy.

## `daily-report`

```bash
jake-tools daily-report --date YYYY-MM-DD
jake-tools daily-report --date YYYY-MM-DD --json
```

Key behaviour:

- all configured lanes run;
- inbox triage is envelope-only unless separately authorised;
- output stays under `_working/daily-report-YYYY-MM-DD/`;
- a failed lane produces a non-zero exit;
- key artefacts include `report.md`, `summary.json`, `manifest.json`, and lane evidence.

Use live help for provider/model options.

## `ai-watch`

```bash
jake-tools ai-watch run --date today --json
jake-tools ai-watch tune --date YYYY-MM-DD
```

`run` performs collection, fetch, judgement, Obsidian sync, digest generation, and delivery. `tune` reapplies deterministic display and recency rules to an existing run without repeating model stages. Use live help for current limits and filters.

## `clockify`

```bash
jake-tools clockify whoami
jake-tools clockify jira-name SF-353 "Vehicle Control Logic - Preliminary Architecture" --json
jake-tools clockify jira-sync --dry-run --json
jake-tools clockify jira-sync --issue SF-304 --dry-run --json
jake-tools clockify jira-sync --issue SF-304 --apply --json
```

`jira-sync` is dry-run by default. An apply may create, rename, reactivate, or complete records and must verify each changed object by re-reading Clockify.

Sunfish naming:

- project name: Jira summary only;
- task name: Jira key plus summary;
- project note: `Jira: SF-123`.

## `newsletter`

Requires CSU Microsoft Graph authentication.

```bash
jake-tools newsletter list --limit 25 --body --json
jake-tools newsletter add "Title" < /tmp/body.txt
jake-tools newsletter edit ITEM_ID --title "New title" < /tmp/body.txt
```

Inspect recent items before mutation and re-fetch created or edited items for verification. Use live help for attachments and current options.

## External dependencies

| Tool | Used by |
|---|---|
| `uv` | dependency management and development runner |
| `hermes-agent` | bounded model stages |
| `himalaya` | daily-report inbox lane |
| `ffmpeg`, `scribe` | local audio workflows |
| `az` or the configured device-code client | Microsoft Graph operations |

If a required tool or command is absent, report the blocker rather than silently selecting another implementation.

## Development

When a repeated deterministic workflow belongs in `jake-tools`:

- keep Click handlers thin;
- put orchestration and domain logic in package modules;
- use typed boundaries;
- preserve immutable source evidence and version derived runs;
- test behaviour at meaningful seams;
- run `uv run pre-commit run --all-files` before completion.
