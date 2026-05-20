---
name: obsidian-recording-to-meeting-minutes
description: Use when an Obsidian meeting note is mostly blank but contains or links to an audio recording that needs turning into complete meeting minutes, chapters, and a polished diarised transcript.
---

# Obsidian Recording to Meeting Minutes

## Overview

Turn sparse Obsidian meeting notes plus recordings into source-grounded minutes and a polished diarised, chapterised transcript. This is a **coordinator-led workflow**: the coordinator transcribes and orchestrates, while specialist phases (subagents when the platform supports them) handle speaker attribution, transcript polishing, minutes extraction, secondary transcript comparison, and QA. See `references/coordinator-workflow.md` for single-session mode.

## Prerequisites

- **Vault:** Know `<vault>` (absolute path). Read `<vault>/AGENTS.md` before writing. Recording embeds usually resolve under `<vault>/Attachments/` (adjust if your vault stores media elsewhere).
- **scribe:** Local diarised transcription via [trailofbits/scribe](https://github.com/trailofbits/scribe). If `scribe` is missing, install with [uv](https://docs.astral.sh/uv/)’s tool runner:

  ```bash
  uv tool install git+https://github.com/trailofbits/scribe.git
  ```

  Ensure the `scribe` executable is on `PATH` (uv prints the install location when the command finishes). **One-off without a permanent install:**

  ```bash
  uvx --from git+https://github.com/trailofbits/scribe.git scribe --format json -o /tmp/<slug>/scribe/<recording>.json '<vault>/Attachments/<recording>.m4a'
  ```

  Upstream also documents **clone + `uv sync`** in-repo; use that if `uv tool install` is unsuitable.

  Upstream requirements include **macOS with Apple Silicon**, **Python 3.13+**, and **ffmpeg** (e.g. `brew install ffmpeg`). If the environment cannot run scribe, stop and tell the user rather than faking a transcript.

## Data handling

Audio, diarised JSON, chunk excerpts, and drafts under `/tmp/<slug>/` are sensitive. Do not paste full transcripts into public tools or unrelated chats. Prefer deleting or leaving scratch to the user’s disk policy after a successful vault write.

## Non-negotiable architecture

Do **not** process a recording end-to-end in the coordinator context. Every recording import uses progressive disclosure:

1. Coordinator reads vault rules, finds the note, resolves recordings, runs `scribe`, writes a manifest, runs specialist phases (subagents or single-session mode), merges file outputs, writes the note, and verifies. See `references/coordinator-workflow.md`.
2. Split each recording into chunk windows before polishing. Default 20–45 minutes; shorter if dense or speaker attribution is hard. Chunks may run in parallel. See `references/manifest-and-chunking.md`.
3. Speaker attribution runs in its own subagent before transcript polishing. See `references/speaker-attribution-agent.md` and `references/speaker-attribution-from-prior-notes.md`.
4. Transcript polishing runs in chunk subagents. See `references/transcript-polishing-agent.md`.
5. Minutes/key takeaways are extracted by a separate subagent from chunk summaries and timestamp evidence. See `references/minutes-extraction-agent.md`.
6. If Google Meet/Gemini or another transcript exists, cross-check via separate chunk reviewers. See `references/secondary-transcript-agent.md` and `references/secondary-transcript-cross-check.md`.
7. A final QA/audit subagent reviews the merged note before the coordinator writes to the vault. See `references/qa-audit-agent.md`.

## Workflow

1. **Load note rules.** Read `<vault>/AGENTS.md` first and follow locale, tone, and linking rules stated there (e.g. Australian English, concise prose, useful wikilinks — only if the vault says so).
2. **Find and preserve the target note.** Use the supplied path if given; otherwise search by title. Preserve frontmatter, prep notes, and original recording embeds unless explicitly told otherwise.
3. **Resolve and transcribe every recording.** Parse all `![[...m4a]]`, `![[...mp3]]`, and `![[...wav]]` embeds. Resolve paths relative to the vault (commonly `Attachments/`). Run diarised JSON to scratch space:
   ```bash
   scribe --format json -o /tmp/<slug>/scribe/<recording>.json '<vault>/Attachments/<recording>.m4a'
   ```
   Keep JSON and scratch transcripts out of the vault by default.
4. **Create the manifest and chunk files.** Record note path, vault rules summary, attendees, recordings, durations, chunk windows, offsets, secondary transcript paths, and subagent output paths. Write bounded JSON/text excerpts for each chunk. Details: `references/manifest-and-chunking.md` and `references/multi-chunk-recordings.md`.
5. **Run specialists.** Prefer subagents with the manifest and file paths only; do not paste whole transcripts into the coordinator. If subagents are unavailable, use **single-session mode** in `references/coordinator-workflow.md`. Subagent outputs go under `/tmp/<slug>/agent-outputs/`.
6. **Merge conservatively.** The coordinator combines polished chunks, speaker mappings, minutes extraction, and QA findings. Keep uncertain speaker labels or claims marked uncertain instead of inventing confidence.
7. **Write the note.** Follow section order, transcript conventions, and the body template in `references/final-note-template.md`.
8. **Verify before claiming completion.** Re-read the note and run structure checks. Confirm frontmatter intact, summary after frontmatter, key details before chapters, chapters before transcript, every recording embed preserved, chunk timestamps continuous and overlap/gap-checked, speaker caveats reflected, decisions/actions timestamp-grounded, and no `## Raw transcript` section.
9. **Place the note correctly.** Move only when requested or when convention is clear (e.g. vault PARA rules or user instruction). Example maintainer convention: Sunfish notes under `2 Areas/Sunfish` when that area applies.

## Quick Reference

| Need | Default |
|---|---|
| Architecture | Coordinator + specialists each recording import (subagents or single-session mode) |
| Transcription | Coordinator runs `scribe --format json` to `/tmp/<slug>/` |
| Chunking | 20–45 min windows, natural file boundaries preferred, parallelisable |
| Working files | `/tmp/<slug>/manifest.json`, `/tmp/<slug>/agent-outputs/*.md/json` |
| Multi-file recordings | Resolve every embed; validate gaps/overlap before continuous offsets |
| Speaker attribution | Dedicated phase; subagent preferred; labels chunk-local and confidence-rated |
| Polishing | Dedicated per-chunk phase; subagent preferred; faithful, conservative ASR cleanup |
| Minutes | Dedicated extractor; decisions/actions require timestamp evidence |
| Secondary transcripts | Dedicated comparison phase; JSON corrections only |
| Final QA | Dedicated audit before vault write |
| Raw transcript | Scratch/evidence only; do not add to note by default |

## Pitfalls

- Do not skip vault-local instructions.
- Do not process the transcript, speaker mapping, polishing, and minutes in one coordinator context.
- Do not paste full transcripts into coordinator prompts when a scratch file plus chunk reference will do.
- Do not transcribe only the first recording embed.
- Do not assume `SPEAKER_01` is the same person across files or chunks.
- Do not trust diarisation blindly; clusters can contain stray turns. User corrections become anchors.
- Do not turn speculative discussion into decisions.
- Do not paste raw `scribe` or Google/Gemini output into the note.
- Do not write scratch artefacts into the vault by default.
- Do not move PARA folders unless requested or required by stable convention.

## Verification Snippet

Heuristic structural checks only; extend patterns if your embed filenames differ. See `references/final-note-template.md`.

```bash
python3 - <<'PY'
from pathlib import Path
p = Path('<note.md>')
s = p.read_text()
checks = {
    'frontmatter': s.startswith('---'),
    'summary': '\n> [!summary]' in s[:600],
    'key_before_chapters': '## Key details' in s and '## Chapters' in s and s.index('## Key details') < s.index('## Chapters'),
    'chapters_before_transcript': '## Chapters' in s and '## Transcript' in s and s.index('## Chapters') < s.index('## Transcript'),
    'recording_embed': '![[' in s and (']]' in s) and any(ext in s for ext in ('.m4a]]', '.mp3]]', '.wav]]')),
    'no_raw_transcript_section': '## Raw transcript' not in s,
}
for k, v in checks.items(): print(f'{k}: {v}')
PY
```

Only claim completion once structure checks, semantic QA, and a manual skim pass.
