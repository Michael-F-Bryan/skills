# Output schemas

Use these deterministic schemas for all stage boundaries.

## 1) provenance.json

```json
{
  "source_note": "/Users/work/Documents/Vault/0 Inbox/Meeting.md",
  "recording_paths": [
    "/tmp/session/audio/part-1.m4a",
    "/tmp/session/audio/part-2.m4a"
  ],
  "recording_count": 2
}
```

## 2) concat-plan.json

```json
{
  "inputs_in_creation_order": [
    "/tmp/session/audio/part-1.m4a",
    "/tmp/session/audio/part-2.m4a"
  ],
  "output_merged_audio": "/tmp/session/audio/merged.m4a"
}
```

## 3) scribe-run-report.json

```json
{
  "input_audio": "/tmp/session/audio/merged.m4a",
  "output_json": "/tmp/session/audio/merged.json",
  "format": "json",
  "warnings": ["8 segments could not be attributed to a speaker"],
  "segment_count": 2163
}
```

## 4) speaker-mapping.json

```json
{
  "mapping": {
    "SPEAKER_01": {
      "name": "Taylor Odishoo",
      "confidence": 0.82,
      "reason": "Matches attendee and self-reference in transcript"
    }
  },
  "unresolved": ["SPEAKER_07", "SPEAKER_08"],
  "notes": "Two labels remain unresolved due sparse turns"
}
```

## 5) chapters.json

```json
[
  {
    "title": "Kickoff and Card Review Plan",
    "start": 0,
    "end": 123.16,
    "summary": "Team aligns on the card-based debrief approach."
  }
]
```

## 6) chapter-N-polish-ledger.json

```json
{
  "chapter": 1,
  "input_turns": 98,
  "output_turns": 98,
  "dropped_turns": [],
  "merged_turns": [],
  "rewritten_turns": [
    { "index": 14, "reason": "punctuation_only" }
  ],
  "uncertain_terms": ["ASCA?"]
}
```

## 7) chapter-N-turn-manifest.json

```json
{
  "chapter": 1,
  "expected_turn_artifacts": 98,
  "produced_turn_artifacts": 98,
  "artifact_root": "turn-artifacts/chapter-1",
  "missing_turn_indices": []
}
```

## 8) turn-artifacts/chapter-N/turn-XXXX.json

```json
{
  "turn_index": 14,
  "speaker": "SPEAKER_03",
  "input_text": "uh should we start with cards",
  "action": "kept",
  "output_text": "Should we start with cards?",
  "reason_code": "punctuation_only"
}
```

## 9) fidelity-report.json

```json
{
  "status": "pass",
  "gates": {
    "A": { "result": "pass", "details": "Coverage 0 to 8519.8 with no gaps" },
    "B": { "result": "pass", "details": "Turn parity maintained for all chapters" },
    "C": { "result": "pass", "details": "Per-turn artifacts complete" },
    "D": { "result": "pass", "details": "Unresolved term rate under thresholds" },
    "E": { "result": "pass", "details": "Index, headings, and anchors aligned" },
    "F": { "result": "pass", "details": "All corrections evidence-backed" },
    "G": { "result": "pass", "details": "Completion guard satisfied" }
  },
  "failed_chapters": []
}
```

## 10) corrections-ledger.json

```json
[
  {
    "before": "AUCA",
    "after": "AUKUS",
    "evidence": "https://www.defence.gov.au",
    "confidence": 0.97,
    "chapter": 15,
    "turn_index": 84,
    "local_context_before": "talking about AUCA alignment",
    "local_context_after": "talking about AUKUS alignment"
  }
]
```

## 11) merge-report.json

```json
{
  "status": "pass",
  "chapters_index_count": 27,
  "transcript_heading_count": 27,
  "anchor_mismatches": [],
  "original_content_preserved": true
}
```

## 12) signoff-report.json

```json
{
  "status": "done",
  "required_artifacts_present": true,
  "blocking_failures": [],
  "manual_skim": {
    "early_chapter_checked": true,
    "mid_chapter_checked": true,
    "late_chapter_checked": true
  }
}
```
