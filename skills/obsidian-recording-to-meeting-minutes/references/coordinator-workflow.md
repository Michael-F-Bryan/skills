# Coordinator workflow

This file defines routing, bounded loops, and escalation for the supervisor/coordinator.

## Ownership

- Coordinator is the single owner of user-facing updates and final status.
- Specialists produce artifacts only; they do not declare end-to-end completion.

## Stage order

1. intake and provenance
2. recording concatenation (creation order)
3. `scribe` JSON transcription
4. speaker mapping
5. chaptering
6. deterministic chapter split
7. parallel chapter polishing
8. fidelity audit
9. merge
10. proper-noun correction (if needed)
11. final signoff audit

No stage skipping.

## Routing rules

- Run concatenation only after intake has resolved recording sources.
- Recording order must be oldest creation time to newest creation time.
- Run `scribe` only after merged audio exists.
- Require JSON transcript output from `scribe` before downstream stages.
- Run speaker mapping only after `merged.json` is present and parseable.
- Run chaptering only after transcript max end is known.
- Run polishing only after chapter coverage passes.
- Run merge only after fidelity audit passes.
- Run correction pass only when unresolved proper nouns exceed threshold or user explicitly asks.
- Run final signoff after merge and any correction pass.

## Retry and timeout budgets

Default budgets:

- recording concatenation: max 2 attempts, 8 minutes each
- `scribe` transcription: max 2 attempts, 20 minutes each
- speaker mapping: max 2 attempts, 8 minutes each
- chaptering: max 2 attempts, 10 minutes each
- polishing batch: max 2 attempts per failed chapter, 15 minutes each
- fidelity audit: max 2 attempts, 6 minutes each
- correction pass: max 2 attempts, 12 minutes each
- merge: max 2 attempts, 8 minutes each

Escalation trigger:
- any stage exceeds retry budget,
- same gate fails twice for same chapter,
- required artifact missing after retry.

Escalation behavior:
- return `status: "blocked"` with failing stage, failed gates, and required manual decision.

## Parallel fan-out policy

- Parallelization allowed only for independent chapter polishing.
- Coordinator assigns disjoint chapter ranges.
- Coordinator waits for all child outputs before running fidelity audit.
- Failed chapters are re-polished in targeted fan-out; successful chapters are not reworked.

## Failure handling matrix

- Contract/schema failure: reject output and rerun same stage once.
- Gate failure (chapter-level): rerun only impacted chapters.
- Gate failure (global merge/correction): halt and escalate with remediation checklist.
- Tool/runtime failure: retry once with same prompt, then escalate.

## Status payloads

In-flight stage update:

```json
{
  "status": "in_progress",
  "stage": "scribe_transcription",
  "merged_audio_path": "/tmp/session/audio/merged.m4a",
  "output_json_path": "/tmp/session/audio/merged.json"
}
```

Blocked payload:

```json
{
  "status": "blocked",
  "stage": "fidelity_audit",
  "failed_gates": ["B", "C"],
  "affected_chapters": [5, 6],
  "next_action": "Re-polish affected chapters and regenerate manifests"
}
```

Done payload:

```json
{
  "status": "done",
  "artifacts": [
    "speaker-mapping.json",
    "chapters.json",
    "fidelity-report.json",
    "updated-note.md"
  ],
  "gates_passed": ["A", "B", "C", "E", "G"]
}
```
