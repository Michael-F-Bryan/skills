# Examples

This document shows how the retrieval workflow should behave.

## Example 1 — Conceptual rule, vague wording

Query:

```text
what was that thing about not using document categories
```

Intent classification:

- durable reference knowledge
- likely atomic note or topic note
- likely root: `3-resources/`

Likely containers:

- `3-resources/para/`
- `3-resources/atomic-notes/`
- `2-areas/workspace-governance/`

Rewritten queries:

- avoid document-category folders
- classification by purpose not file type
- avoid bucket folders

Expected behaviour:

- inspect manifests for `para`, `atomic-notes`, and `workspace-governance`
- inspect PARA index and atomic notes index
- shortlist note titles such as:
  - `avoid-catch-all-category-folders`
  - `active-outcome-beats-document-type`
- deep-read only those
- return best match with any close alternatives

## Example 2 — Current rule

Query:

```text
what is the current policy for big maintenance changes
```

Intent classification:

- operational/governance
- likely root: `2-areas/`

Likely containers:

- `2-areas/workspace-governance/`
- `2-areas/agent-operations/`

Expected behaviour:

- inspect manifests
- inspect relevant indexes or policy notes
- prefer current governance notes over resources
- search archives only if current areas do not answer the question

## Example 3 — Half-remembered project knowledge

Query:

```text
did we already work out how to split broad containers without adding nesting
```

Intent classification:

- durable principle, possibly first emerged in project work
- likely roots:
  - `3-resources/`
  - `1-projects/` as fallback if not yet distilled

Likely containers:

- `3-resources/para/`
- `3-resources/atomic-notes/`
- `1-projects/openclaw-maintenance/`

Expected behaviour:

- search resources first
- if not found, inspect current maintenance project notes
- if found only in project material, return that and suggest distillation if appropriate
