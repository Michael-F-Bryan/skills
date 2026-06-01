# Subagent contracts

Use these prompts/contracts as copy-ready templates. Outputs must be machine-checkable.

## Global specialist rules

- Mission is narrow; do not broaden scope.
- Write only declared output artifacts.
- No user-facing narrative; return structured output only.
- On uncertainty, escalate instead of guessing.
- On schema violation, return `status: "failed_contract"` with reasons.

## 1) Intake and provenance specialist

Mission:
- Validate inputs and produce a provenance snapshot.

Allowed tools:
- Read-only file inspection tools.

Required output artifact:
- `provenance.json`

Done criteria:
- Source note exists.
- Recording sources exist and are discoverable.
- Segment count, max end time, and unattributed segments captured.

Failure behavior:
- Return missing paths and stop pipeline.

## 2) Recording concatenation specialist

Mission:
- Concatenate all recordings in file creation order into a single merged audio file.

Allowed tools:
- Filesystem listing and deterministic shell utilities for ordering and concatenation.

Required output artifacts:
- `concat-plan.json`
- merged audio file (for example `merged.m4a`)

`concat-plan.json` shape:

```json
{
  "inputs_in_creation_order": [
    "/tmp/session/audio/0001.m4a",
    "/tmp/session/audio/0002.m4a"
  ],
  "output_merged_audio": "/tmp/session/audio/merged.m4a"
}
```

Done criteria:
- Input recordings are sorted oldest to newest by creation time.
- Merged file exists and has non-zero size.

Failure behavior:
- If timestamps are unavailable or ambiguous, escalate instead of guessing order.

## 3) Scribe transcription specialist

Mission:
- Generate diarized transcript JSON from merged audio using `scribe`.

Allowed tools:
- Shell execution of `scribe`.

Required output artifacts:
- `merged.json`
- `scribe-run-report.json`

`scribe-run-report.json` shape:

```json
{
  "input_audio": "/tmp/session/audio/merged.m4a",
  "output_json": "/tmp/session/audio/merged.json",
  "format": "json",
  "warnings": [],
  "segment_count": 2163
}
```

Done criteria:
- `scribe` command succeeds.
- Output JSON is valid and contains transcript segments.

Failure behavior:
- On command failure or invalid JSON, return `status: "failed_contract"` with stderr summary.

## 4) Speaker mapping specialist

Mission:
- Map diarized speakers to attendee names with confidence.

Allowed tools:
- Read transcript + note frontmatter + note hints.

Required output artifact:
- `speaker-mapping.json`

Required shape:

```json
{
  "mapping": {
    "SPEAKER_01": { "name": "Taylor Example", "confidence": 0.84, "reason": "Matches self-reference and attendee list" }
  },
  "unresolved": ["SPEAKER_07"],
  "notes": "Short caveats"
}
```

Done criteria:
- Every speaker label has object form.
- Names come from attendees list when resolved.
- `confidence < 0.65` speakers are listed unresolved unless strong evidence exists.

Failure behavior:
- Never emit flat string mapping.
- If confidence is low and unresolved is not acceptable, escalate with ambiguity notes.

## 5) Chaptering specialist

Mission:
- Segment conversation into semantic chapters.

Allowed tools:
- Read transcript and context note only.

Required output artifact:
- `chapters.json`

Required shape:

```json
[
  { "title": "Kickoff", "start": 0, "end": 123.16, "summary": "..." }
]
```

Done criteria:
- Starts at `0`.
- Ends at transcript max end.
- No gaps/overlaps.
- Boundaries are semantic (topic, mood, viewpoint change), not fixed windows.

Failure behavior:
- If semantic boundaries are unclear, return best attempt plus `needs_review: true`.

## 6) Chapter polishing specialists (parallel fan-out)

Mission:
- Polish assigned chapter files without summarizing or collapsing dialogue.

Allowed tools:
- Read/write chapter files and chapter-local artifact folder only.

Required output artifacts per chapter:
- `chapter-N-polished.md`
- `chapter-N-polish-ledger.json`
- `chapter-N-turn-manifest.json`
- `turn-artifacts/chapter-N/turn-XXXX.json` (at least one artifact per input turn)

Ledger shape:

```json
{
  "chapter": 7,
  "input_turns": 123,
  "output_turns": 123,
  "dropped_turns": [{ "index": 44, "reason": "filler_only" }],
  "merged_turns": [],
  "rewritten_turns": [{ "index": 18, "reason": "punctuation_only" }],
  "uncertain_terms": ["Asker?"]
}
```

Turn manifest shape:

```json
{
  "chapter": 7,
  "expected_turn_artifacts": 123,
  "produced_turn_artifacts": 123,
  "artifact_root": "turn-artifacts/chapter-7",
  "missing_turn_indices": []
}
```

Done criteria:
- `output_turns + dropped_turns == input_turns`
- `merged_turns == 0`
- no reordering
- no semantic compression

Allowed drop reasons:
- `filler_only`
- `empty_asr_fragment`
- `duplicate_fragment_immediate`

Failure behavior:
- On unresolved ambiguity, keep original wording with `[unclear]`.
- If turn parity fails, return `status: "failed_contract"` with failing indices.

## 7) Fidelity auditor specialist

Mission:
- Evaluate all chapter outputs against gate file and produce binary report.

Allowed tools:
- Read artifacts and ledgers only.

Required output artifact:
- `fidelity-report.json`

Done criteria:
- Every gate emits explicit `pass`/`fail`.
- Every failure includes chapter IDs and evidence.

Failure behavior:
- Never auto-fix. Return failed gates and rework list only.

## 8) Merge specialist

Mission:
- Merge validated chapter outputs into final note structure while preserving original authored sections.

Allowed tools:
- Deterministic merge script or structured file editing.

Required output artifact:
- Updated note file + `merge-report.json`

Done criteria:
- `## Chapters` count matches transcript chapter section count.
- Links resolve to matching headings.
- Original non-transcript content preserved.

Failure behavior:
- If mismatch detected, stop and report without partial merge.

## 9) Proper-noun correction specialist

Mission:
- Fix obvious names/acronyms with evidence-backed changes.

Allowed tools:
- Local corpus reads and web evidence lookup when needed.

Required output artifact:
- `corrections-ledger.json`

Ledger row shape:

```json
{
  "before": "AUCA",
  "after": "AUKUS",
  "evidence": "https://example.com",
  "confidence": 0.97,
  "chapter": 15,
  "turn_index": 84,
  "local_context_before": "...",
  "local_context_after": "..."
}
```

Done criteria:
- Every correction has evidence and local context.
- No bulk wildcard replacements.

Failure behavior:
- If uncertain, keep original and log unresolved.

## 10) Final signoff auditor

Mission:
- Confirm all mandatory artifacts exist and every blocking gate passed.

Allowed tools:
- Read-only verification across outputs.

Required output artifact:
- `signoff-report.json`

Done criteria:
- All required artifacts present.
- No blocking failures open.

Failure behavior:
- Return `status: "blocked"` with unresolved blockers.
