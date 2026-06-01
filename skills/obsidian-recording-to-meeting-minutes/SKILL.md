---
name: obsidian-recording-to-meeting-minutes
description: Use when turning Obsidian meeting recordings or diarized transcripts into meeting minutes where transcript fidelity, bounded specialist orchestration, and evidence-backed corrections are required.
---

# Obsidian Recording to Meeting Minutes

## Overview

This skill is a fidelity-first operating system for converting long Obsidian meeting recordings into structured minutes plus a traceable transcript.

Core rule: transcript text is evidence, not prose.

## Trigger contract

Use this skill when all of the following are true:

1. Source is an Obsidian note and local recording/transcript artifacts.
2. Output requires meeting minutes plus chaptered transcript content.
3. Stakeholders care about preserving the conversation rather than summarizing away detail.

Do not use this skill for publication-style transcript compression.

## Non-negotiables

1. Single explicit owner per turn: coordinator owns user-facing state and completion claims.
2. Specialists are narrow and contract-bound; no generic helper roles.
3. Ingestion must concatenate all recordings by creation order before transcription.
4. Ingestion transcript must be generated via `scribe` in JSON format.
5. Polishing cannot summarize, collapse, or silently drop substantive turns.
6. All loops are bounded with retry, timeout, and escalation.
7. Quality gates are binary pass/fail and block completion on failure.
8. Proper-noun corrections require evidence and a change ledger.
9. No whole-note global replacement passes.

## Ingestion contract

Before speaker mapping/chaptering:

1. Discover all source recordings from note links or configured recording directory.
2. Sort recordings by file creation time (oldest to newest).
3. Concatenate into a single merged audio artifact.
4. Run `scribe` on merged audio and require JSON output (`merged.json`).
5. Capture ingest provenance (ordered inputs, merged output path, scribe output path, scribe warnings/errors).

If any ingestion step fails, stop and return `blocked` with stage `ingestion`.

## Routing contract

Coordinator decides which specialist runs next and only passes minimal required context.

Specialist roster:
- intake-provenance
- speaker-mapping
- chaptering
- chapter-splitter (deterministic)
- chapter-polisher (parallel fan-out)
- fidelity-auditor
- merge-specialist
- proper-noun-correction
- final-signoff-auditor

Use `references/coordinator-workflow.md` for sequence, retries, and escalation.

## State contract

Coordinator is the sole writer for pipeline state keys:
- `provenance`
- `speaker_map`
- `chapters`
- `polish_ledgers`
- `turn_manifests`
- `fidelity_report`
- `corrections_ledger`
- `final_note_status`

Specialists may only write their designated artifacts and must never mutate prior artifacts in place.

## Termination contract

Stop with `blocked` status when any blocking gate fails and retries are exhausted.

Return partial-failure payload containing:
- failed gate IDs,
- affected chapters,
- last successful stage,
- next required action.

Never claim completion without a passing fidelity report.

## Verification contract

Run all gates in `references/fidelity-gates.md`:
- chapter coverage,
- turn preservation,
- per-turn artifact completeness,
- merge integrity,
- correction safety.

## Output contract

Required deliverables:
- updated Obsidian note,
- merged audio artifact path + ordered input list,
- `merged.json` transcript path,
- `speaker-mapping.json`,
- `chapters.json`,
- chapter polish ledgers and turn manifests,
- `fidelity-report.json`,
- `corrections-ledger.json` (if corrections were attempted).

If any required artifact is missing, workflow is not done.

## Reference map

- `references/coordinator-workflow.md`
- `references/subagent-contracts.md`
- `references/fidelity-gates.md`
- `references/output-schemas.md`
