# Repository Ontology

This document teaches the agent how to think about the repository.

Retrieval quality depends on understanding **what kinds of knowledge exist** and **where they usually live**.

## PARA roots

### `1-projects/`

Meaning

- active, outcome-driven work
- work with a finish line
- current execution artefacts

Typical contents

- plans
- active reports
- triage notes
- reply drafts
- working analyses
- project-local artefacts

Use when searching for

- current work
- active decisions
- not-yet-distilled knowledge
- current project context

Avoid when searching for

- evergreen principles
- stable governance rules
- mature conceptual knowledge

### `2-areas/`

Meaning

- ongoing responsibilities
- operating contracts
- governance
- rules the system actively follows

Typical contents

- operating principles
- workspace governance
- behavioural rules
- maintenance policies
- active process documents

Use when searching for

- current rules
- long-lived operational guidance
- workspace policies
- system behaviour expectations

Avoid when searching for

- old completed work
- one-off project plans
- generic conceptual reference material unless it governs current behaviour

### `3-resources/`

Meaning

- reusable reference knowledge
- durable concepts
- distilled notes
- templates
- examples

Typical contents

- topic notes
- atomic notes
- templates
- concept indexes
- durable heuristics
- summaries of reusable patterns

Use when searching for

- principles
- conceptual distinctions
- patterns
- atomic notes
- reusable knowledge
- templates and examples

Avoid when searching for

- live project execution state
- current triage artefacts

### `4-archives/`

Meaning

- inactive, historical, or superseded material

Typical contents

- completed projects
- old reports
- retired guidance
- historical notes

Use when searching for

- older decisions
- superseded context
- historical material
- inactive project knowledge

Avoid when the query is clearly about current or active knowledge.

## Note classes

## Topic note

A broader reference note about a domain or concept.

Examples:

- PARA
- workspace governance
- open-source maintenance
- engineering style

## Atomic note

A single durable idea, short and reusable.

Examples:

- active-outcome-beats-document-type
- avoid-catch-all-category-folders

## Template

A reusable structure for future output.

## Index

A navigation note that points to related notes in a topic area.

## Manifest

A container-level routing aid that defines what belongs in a container.

## Retrieval implications

When the agent needs:

- **an active status or current draft** → bias toward `1-projects/`
- **an operating rule** → bias toward `2-areas/`
- **a durable concept or pattern** → bias toward `3-resources/`
- **historical context** → bias toward `4-archives/`

When uncertain between `2-areas/` and `3-resources/`:

- ask whether the note is primarily a **governing rule currently in force**
- if yes, prefer `2-areas/`
- otherwise prefer `3-resources/`
