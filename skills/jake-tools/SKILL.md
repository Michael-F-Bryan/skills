---
name: jake-tools
description: Use the jake-tools CLI as a swiss-army knife for agent tasks. Load when you need to run a daily report, transcribe Obsidian recordings, polish transcripts, or manage CSU Weekly Newsletter items. Also load when deciding whether a recurring pattern warrants a new jake-tools command.
---

# jake-tools

`jake-tools` is an internal Python CLI built for agent-driven workflows. It is
installed globally via `uv tool install` from a checkout of
`https://github.com/Michael-F-Bryan/jake-tools` and is on `$PATH`. The install
is editable, so source changes take effect immediately without reinstalling.

## Golden rule

When in doubt, run `jake-tools --help` or `jake-tools <command> --help`. The
CLI's own help is always more current than this skill.

## Available commands

```
jake-tools daily-report    Run the deterministic daily-report coordinator.
jake-tools newsletter      Read and update the CSU Weekly Newsletter list.
jake-tools transcribe      Tools for transcribing audio files.
jake-tools transcript      Transcript primitive toolbox (schema discovery and inspection).
```

---

### `daily-report`

Runs a deterministic, multi-lane daily report for a target date.

```bash
jake-tools daily-report --date YYYY-MM-DD
jake-tools daily-report --date YYYY-MM-DD --json
```

Key flags:

| Flag | Default | Purpose |
|---|---|---|
| `--date YYYY-MM-DD` | **required** | Target local date |
| `--provider TEXT` | `openrouter` | LLM provider for lane workers |
| `--judgement-model TEXT` | `openrouter/auto` | Model for judgement-heavy lanes |
| `--evidence-model TEXT` | `openrouter/auto` | Model for evidence-fed lanes |
| `--json` | off | Emit machine-readable summary only |

**Behaviour:**

- All six lanes always run: session hindsight, memory candidates, skill review,
  failure patterns, transcripts/DUM-C, and inbox triage.
- Inbox triage is envelope-only (no message bodies, no mail mutation).
- Read-only outside `_working/daily-report-YYYY-MM-DD/` in the working directory.
- Exits `1` when any lane fails.
- Key artefacts: `report.md`, `summary.json`, `manifest.json`,
  `lane-events.jsonl`, plus `evidence/`, `subtasks/`, `prompts/`, `logs/`.

---

### `transcribe`

Audio-to-polished-note pipeline for Obsidian recordings.

#### `transcribe obsidian-recording`

```bash
jake-tools transcribe obsidian-recording NOTE.md
jake-tools transcribe obsidian-recording --dry-run --json NOTE.md
```

Rewrites the Obsidian note in-place (unless `--dry-run`). Output sections:
`## Meeting Notes`, `## Chapters`, `## Transcript`.

| Flag | Purpose |
|---|---|
| `--dry-run` | Run without writing back to disk |
| `--json` | Emit machine-readable JSON summary |
| `--default-model TEXT` | Override LLM model |
| `--provider TEXT` | Override LLM provider |

#### `transcribe polish`

```bash
jake-tools transcribe polish TRANSCRIPT.txt
```

Polishes a raw transcript and writes the result to stdout. Accepts
`--default-model` and `--provider`.

---

### `newsletter`

Read and mutate the CSU Weekly Newsletter SharePoint list via Microsoft Graph.
Requires `az login` to the CSU tenant first.

#### `newsletter list`

```bash
jake-tools newsletter list
jake-tools newsletter list --limit 25 --body --json
```

Read-only. Returns recent newsletter items (default: 10).

#### `newsletter add`

```bash
jake-tools newsletter add "Training night update" < /tmp/body.txt
jake-tools newsletter add "Title" --attach /tmp/image.png < /tmp/body.txt
```

Body is read from stdin (required). `--attach` can be supplied multiple times.

#### `newsletter edit`

```bash
jake-tools newsletter edit ITEM_ID --title "New title" < /tmp/new-body.txt
jake-tools newsletter edit ITEM_ID --attach /tmp/extra.png
```

Body from stdin is optional. `--attach` adds attachments without replacing
existing ones. `--title` replaces the title.

---

## External dependencies

| Tool | Required by |
|---|---|
| `uv` | Dependency management and runner |
| `hermes-agent` | LLM calls (editable path dep) |
| `himalaya` | `daily-report` inbox lane |
| `ffmpeg`, `scribe` | `transcribe obsidian-recording` audio pipeline |
| `az` (Azure CLI) | `newsletter` commands (Graph token) |

If a required tool is missing, report the blocker. Do not skip preflight
checks silently.

---

## Boundaries

- `daily-report` is read-only outside its dated work directory. Other commands
  may write to Obsidian notes or SharePoint by design.
- Do not commit secrets, tokens, or credentials.
- Do not assume the entire repo is read-only because `daily-report` is.

---

## Adding new commands

If you notice you are doing the same multi-step task repeatedly — pulling data
from an API, transforming files, triggering a pipeline — ask the user whether
it is worth integrating that pattern into the `jake-tools` CLI.

The repo convention is:
- Keep CLI commands thin (in `src/jake_tools/cli/`).
- Put orchestration and domain logic in package modules.
- Use typed Pydantic models; avoid ad hoc dicts.
- Run `uv run pre-commit run --all-files` before finishing (covers ruff, pyright, pytest, uv lock).
