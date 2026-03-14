# Candidate Shortlist Agent

Purpose

Shortlist likely notes from the routed containers using cheap recognition signals.

## Inputs

```json
intent-report.json
routing-report.json
```

and:

- topic indexes
- note titles
- note metadata
- note summaries
- optional `kb-index.json`

## Tasks

Within the routed containers, rank note candidates by:

- title similarity
- alias match
- topic overlap
- `query-patterns` overlap
- summary match
- link proximity to known relevant notes
- canonical/index status
- recent use when relevant

Build a shortlist.

Default maximum:

- 12 candidates total
- ideally 5 to 8 strong candidates

Prefer recognition signals over body-content scanning.

## Output

```json
{
  "shortlist": [
    {
      "path": "",
      "score": 0,
      "signals": [],
      "summary": ""
    }
  ],
  "deferred_candidates": [],
  "confidence": ""
}
```

## Evaluation criteria

A good shortlist:

- contains plausible candidates
- is small enough for bounded deep reading
- uses titles, aliases, metadata, and summaries effectively
- avoids broad full-text search when cheap signals are sufficient

If the repo lacks metadata:

- rely on title and summary signals
- widen only if the shortlist is weak
