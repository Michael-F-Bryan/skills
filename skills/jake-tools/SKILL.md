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
jake-tools ai-watch        Low-noise AI developments radar.
jake-tools clockify        Clockify helpers, including Jira-backed naming.
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

### `ai-watch`

Runs the AI article discovery and curation pipeline.

```bash
jake-tools ai-watch run --date today --max-candidates 80 --surface-limit 2 --max-article-age-days 90 --json
jake-tools ai-watch tune --date YYYY-MM-DD --surface-limit 2 --max-article-age-days 90
jake-tools ai-watch tune --date YYYY-MM-DD --surface-limit 2 --max-article-age-days 90 --remove-unsurfaced-notes
```

Key behaviour:

- `run` performs collect → fetch → scout → curate → Obsidian sync → digest → delivery.
- Default `--surface-limit 2` caps the main digest; extra surfaced curator decisions are demoted to `speculative.md`.
- Default `--max-article-age-days 90` demotes stale surfaced articles so AI Watch favours recent AI tools, techniques, and releases.
- Xcode-specific AI/dev-tooling articles are treated as low value unless they contain explicit non-Xcode transfer value.
- `tune` reapplies the cap and recency/platform filters to an existing dated run and regenerates `digest.md`, `speculative.md`, `manifest.json`, and `delivery-payload.txt` without rerunning LLM stages.
- `--remove-unsurfaced-notes` deletes generated Obsidian notes for demoted items only when the note contains matching `Candidate ID` and `Run ID` markers.

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

Pitfall/stall handling: long group recordings can appear stalled while `scribe`/`parakeet-mlx` or LLM polish is still running. First check the process tree, CPU activity, and artefact timestamps before intervening. If the host was asleep/offline or the process is still making progress, let the proper `jake-tools transcript recipe obsidian-recording` pipeline continue or rerun it with an explicit `--workdir` and `--manifest` so artefacts are traceable. Do not switch to a manual fallback just because a run went quiet; manual rendering from `transcript.artifact.json` requires explicit user approval or a confirmed hard failure. If fallback is approved, it must still follow the normal transcript contract: chapter headings keep timestamps; individual speaker turns do not. Apply user-confirmed speaker mappings when available. Do not apply low-confidence automatic speaker mappings to group walkthroughs; keep generic speaker labels only when neither the transcript nor the user gives clear evidence.

For Michael's DUM-C/Obsidian meeting notes, keep a short `[!summary]` callout, then put the meeting-minutes bullets under `## Discussion Notes`. Post-process generated minutes into his handwritten ops-log style before writing back: terse top-level bullets with tab-indented nested bullets, minimal headings, and enough structure to scan. Good style references: `2026-04-28_18-54 Training Handover from Lucas`, `2026-04-29_20-00 CSU Special General Meeting & Elections`, `2026-04-29_20-56 Chatting with Richard about Welfare`, and `2026-07-01_18-41 Awards Night Heaters`. Do not create task checkboxes or tell Michael what to do; notes may record next steps discussed, but should not assign actions. Omit explicit `Action:` labels. If the polished transcript is embedded in the note, do not copy/link the raw source transcript into the vault unless the user explicitly asks for provenance.

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

### `clockify`

Clockify API helpers for time-tracking hygiene.

```bash
jake-tools clockify whoami
jake-tools clockify jira-name SF-353 "Vehicle Control Logic - Preliminary Architecture" --json
jake-tools clockify jira-sync --dry-run --json
jake-tools clockify jira-sync --issue SF-304 --dry-run --json
jake-tools clockify jira-sync --issue SF-304 --apply --json
```

`jira-sync` defaults to active Jira work assigned to `currentUser()`. Repeat `--issue KEY` to reconcile exact work items regardless of assignee. Dry-run is the default. Apply can create, rename, reactivate, or complete Clockify records; every changed object is fetched again for verification. An empty default plan is not evidence about a specifically named issue outside the current-user scope.

For Sunfish Jira-backed Clockify records, `jira-name` encodes the current naming rule:

- Clockify project names use the Jira summary only, without the `SF-123` prefix.
- Clockify tasks keep the Jira key prefix.
- The Jira key belongs in the project note, e.g. `Jira: SF-131`.

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
