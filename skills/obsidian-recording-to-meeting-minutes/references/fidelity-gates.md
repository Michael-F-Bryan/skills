# Fidelity gates

Run these gates before merge and before final sign-off.

## Gate 0: ingestion integrity

- recording inputs are sorted by creation time (oldest to newest)
- merged audio artifact exists and is non-empty
- `scribe` ran against merged audio
- JSON transcript artifact exists and is parseable

Fail action:
- block all downstream stages and rerun ingestion pipeline.

## Gate A: chapter coverage

- first chapter starts at `0`
- last chapter ends at transcript max end
- each adjacent chapter touches exactly (`chapter[i].end == chapter[i+1].start`)
- no negative or reversed ranges

Fail action:
- block merge and rerun chaptering.

## Gate B: turn preservation per chapter

For each chapter:

- compute `input_turns`, `output_turns`, `dropped_turns`, `merged_turns`
- require `output_turns + dropped_turns == input_turns`
- require `merged_turns == 0`
- require stable turn order and index continuity

Allowed drop reasons only:
- `filler_only`
- `empty_asr_fragment`
- `duplicate_fragment_immediate`

Fail action:
- re-polish failed chapters only.

## Gate C: per-turn artifact completeness

For each chapter:

- `expected_turn_artifacts == input_turns`
- `produced_turn_artifacts == expected_turn_artifacts`
- no missing turn indices in manifest

Fail action:
- rerun polishing specialist for affected chapter set.

## Gate D: unresolved term safety

Track unresolved proper nouns/acronyms in polishing output:

- unresolved per 100 turns must be `<= 3`
- unresolved per 1,000 words must be `<= 5`

If either threshold fails:
- run targeted correction pass with evidence ledger.

## Gate E: merge integrity

After merge:

- `## Chapters` list item count equals chapter count
- `## Transcript` chapter heading count equals chapter count
- chapter titles and timestamps match between index and transcript headings
- internal anchors resolve
- original authored content remains present

Fail action:
- rollback generated section and rerun merge logic.

## Gate F: correction safety

For each correction:

- includes evidence URL or local citation
- includes chapter and turn index
- includes local context before/after
- confidence is recorded

Forbidden:
- whole-note wildcard replacements
- ambiguous-token global substitutions

Fail action:
- revert unsafe corrections and rerun targeted correction pass.

## Gate G: completion guard

Workflow can report `done` only when:

- Gates A-B-C-E pass
- Gate D is either under threshold or corrected with ledger
- Gate F passes if corrections were attempted

Otherwise return:

```json
{
  "status": "blocked",
  "failed_gates": ["B", "F"],
  "affected_chapters": [5, 6, 15],
  "next_action": "Re-polish chapters and regenerate correction ledger"
}
```
