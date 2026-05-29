---
name: obsidian-recording-to-meeting-minutes
description: Use when an Obsidian meeting note includes audio recording embeds and needs source-grounded minutes, chapters, and a polished diarised transcript written back into the note.
---

# Obsidian Recording to Meeting Minutes

## Overview

Convert a sparse or partial Obsidian meeting note into a complete, evidence-grounded note with:

- summary and key details
- chapter list
- polished diarised transcript

This workflow is coordinator-led and specialist-executed:

1. coordinator resolves note + recordings, merges audio, transcribes once, and builds manifest
2. specialists handle speaker attribution, transcript polishing, optional secondary cross-check, minutes extraction, and final QA
3. coordinator merges outputs and writes the vault note

Use `references/coordinator-workflow.md` as the canonical execution order.

## Prerequisites

- Know the vault absolute path and read `<vault>/AGENTS.md` before writing.
- Keep frontmatter, prep notes, and original `![[...audio]]` embeds unless asked otherwise.
- Have `ffmpeg` and `scribe` available.

Install `scribe` if needed:

```bash
uv tool install git+https://github.com/trailofbits/scribe.git
```

If the environment cannot run `scribe`, stop and report the blocker. Do not fabricate transcript content.

## Data handling

Treat `/tmp/<slug>/` working files as sensitive:

- merged audio
- diarised JSON
- chunk excerpts
- specialist outputs

Do not paste full transcripts into unrelated chats or tools.

## Non-negotiable architecture

1. **Single transcription pass:** resolve all audio embeds, concatenate into one scratch file, run `scribe` once.
2. **Manifest-first orchestration:** create `/tmp/<slug>/manifest.json` and bounded chunk files before specialist prompts.
3. **Speaker attribution before polishing:** produce a global speaker map from the merged diarisation, then apply per-chapter caveats only when needed.
4. **Transcript polishing must use `/transcript-polisher`:** polishing sub-agents follow that skill in strict Obsidian mode (faithful cleanup, not summarisation).
5. **QA is a separate sub-agent gate:** do not rely on a local verification script as the final check.

## Workflow

1. **Read rules and source note**
   - Read `<vault>/AGENTS.md`.
   - Read the target note and preserve the existing human-written notes + embeds.
2. **Resolve recordings and concatenate**
   - Parse all `![[...m4a]]`, `![[...mp3]]`, `![[...wav]]`.
   - Concatenate in note order with `ffmpeg` into `/tmp/<slug>/audio/merged.*`.
   - See `references/merged-audio-scribe-workflow.md` for the exact merged-audio pattern.
3. **Transcribe once**
   - Run `scribe --format json -o /tmp/<slug>/scribe/merged.json` on the merged file, not each embed separately.
4. **Build manifest and chunks**
   - Write `/tmp/<slug>/manifest.json` and chapter/chunk excerpt files.
5. **Run specialist phases**
   - Speaker attribution (`references/speaker-attribution-agent.md` + `references/speaker-attribution-from-prior-notes.md`).
   - Transcript polishing (`references/transcript-polishing-agent.md`, explicitly invoking `/transcript-polisher`).
   - Optional secondary transcript comparison (`references/secondary-transcript-agent.md`).
   - Minutes extraction (`references/minutes-extraction-agent.md`).
6. **Merge and draft final note**
   - Merge specialist outputs using `references/final-note-template.md`.
   - Keep the original audio embeds and the prep notes unless the user asks for a rewrite.
7. **Run QA sub-agent gate**
   - Spawn the QA specialist with explicit pass/fix/block criteria from `references/qa-audit-agent.md`.
   - Apply blockers before writing to vault.
8. **Write note + manual skim**
   - Write the final note, then re-read the first chapter and one later chapter for fidelity and readability.
   - Fix obvious ASR noise, but keep uncertain speaker labels uncertain.

## Speaker attribution rules

- Because diarisation comes from one merged transcription pass, treat speaker IDs as globally consistent by default.
- Validate mappings with:
  - attendee list in frontmatter
  - human-written notes already in the note body
  - explicit transcript anchors and role/context evidence
- Preserve uncertainty explicitly when evidence is weak.

## Quick reference

| Need                   | Default                                                                |
| ---------------------- | ---------------------------------------------------------------------- |
| Transcription strategy | Merge all embedded recordings, then one `scribe` pass                  |
| Chunking strategy      | Build chapter/chunk files after transcription; polish per chapter      |
| Speaker mapping        | Global map first (merged diarisation), caveats where needed            |
| Transcript polishing   | Separate sub-agent, must apply `/transcript-polisher`                  |
| Verification           | Separate QA sub-agent gate + manual skim                               |
| Raw transcript storage | Keep scratch artifacts in `/tmp/<slug>/`, not in vault note by default |

## Pitfalls

- Skipping `<vault>/AGENTS.md` rules.
- Transcribing each embed separately when merged transcription is available.
- Running polishing without a prior speaker-attribution pass.
- Polishing by rewriting/summarising instead of faithful cleanup.
- Converting speculative discussion into decisions without timestamp evidence.
- Treating QA as optional or replacing it with only a script check.
