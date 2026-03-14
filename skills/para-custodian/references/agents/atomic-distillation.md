# Atomic Distillation Agent

Purpose

Extract reusable atomic notes from recent work.

Implements the **Distil** stage of the [[CODE]] system.

## Inputs

```
survey-report.json
activity-report.json
```

## Tasks

Review recently changed files.

Identify durable ideas.

Examples:

- classification rules
- recurring design patterns
- operational heuristics
- failure modes

Create atomic notes when appropriate.

Atomic notes must be:

- self-contained
- reusable
- concise
- concept-focused

## Output

```
atomic-notes-report.json
```

Example

```
{
  "created_notes": [],
  "proposed_notes": []
}
```

## Storage

Atomic notes belong under:

```
3-resources/atomic-notes/
```

## Evaluation criteria

A good atomic note:

- expresses a single idea
- improves future reasoning
- is grounded in recent work

Avoid extracting:

- status updates
- ephemeral logs
- trivial observations

## Retrieval alignment

Created atomic notes must be retrieval-friendly so the knowledge-base-navigator skill can find them.

- Follow note-writing and metadata expectations in `knowledge-base-navigator/references/note-writing.md` and `knowledge-base-navigator/references/metadata.md`.
- Notes without titles, summaries, or metadata still work but are harder to shortlist and rank during retrieval.

## Atomic note checklist

When creating or proposing an atomic note, ensure:

- **Title:** Concept-shaped, stable, specific (e.g. `avoid-catch-all-category-folders`).
- **Summary:** Short summary near the top (e.g. blockquote or first line after the title).
- **Frontmatter (when possible):** `kind: atomic-note`, `topics`, `aliases`, `related` per knowledge-base-navigator metadata standard.
