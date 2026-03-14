# Deep Read Agent

Purpose

Read only the strongest candidate notes deeply enough to confirm or reject them.

## Inputs

```json
shortlist-report.json
```

## Tasks

Deep-read the top candidates.

Default maximum:

- 5 deep reads

For each candidate:

- confirm whether it answers the query
- extract the key evidence
- identify related notes if the candidate is close but incomplete
- reject clearly wrong candidates quickly

Prefer precision.

Do not drift into reading entire folders.

## Output

```json
{
  "confirmed_matches": [
    {
      "path": "",
      "evidence": [],
      "confidence": ""
    }
  ],
  "partial_matches": [],
  "rejected_candidates": [],
  "suggested_related_notes": []
}
```

## Evaluation criteria

A good result:

- confirms the best match with concrete evidence
- identifies close alternatives
- keeps reads bounded
- stops once the answer is adequately supported

If no match is confirmed:

- return the strongest partials
- recommend the next widening step
