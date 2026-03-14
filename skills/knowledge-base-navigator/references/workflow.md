# Knowledge Base Retrieval Workflow

This document defines the orchestrated workflow for querying the repository knowledge base.

The retrieval workflow is designed for:

- high precision
- bounded token use
- progressive disclosure
- human-like recognition-based navigation

## High-level workflow

1. Query Intent
2. Container Routing
3. Candidate Shortlisting
4. Deep Read
5. Retrieval Synthesis

Each step runs in a dedicated specialised sub-agent.

## 1. Query Intent Agent

Inputs

- user task or question
- current working context
- repository ontology

Outputs

```json
intent-report.json
```

Contains:

- query type
- likely knowledge class
- likely time orientation
- likely note kind
- likely PARA roots

Reference:

```text
references/agents/query-intent.md
```

## 2. Container Routing Agent

Inputs

```json
intent-report.json
```

and:

- repository tree
- container manifests
- optional global index

Outputs

```json
routing-report.json
```

Contains:

- ranked candidate containers
- routing rationale
- related containers
- fallback containers

Reference:

```text
references/agents/container-routing.md
```

## 3. Candidate Shortlist Agent

Inputs

```json
intent-report.json
routing-report.json
```

and:

- topic indexes
- note metadata
- note titles
- note summaries
- optional `kb-index.json`

Outputs

```json
shortlist-report.json
```

Contains:

- ranked candidate notes
- match signals
- shortlist confidence
- deferred candidates

Reference:

```text
references/agents/candidate-shortlist.md
```

## 4. Deep Read Agent

Inputs

```json
shortlist-report.json
```

Outputs

```json
deep-read-report.json
```

Contains:

- deeply read candidates
- extracted evidence
- rejected candidates
- ambiguities

Reference:

```text
references/agents/deep-read.md
```

## 5. Retrieval Synthesiser Agent

Inputs

```json
intent-report.json
routing-report.json
shortlist-report.json
deep-read-report.json
```

Outputs

```md
retrieval-result.md
```

Contains:

- best match or bounded uncertainty
- supporting notes
- rationale
- next widening step if unresolved

Reference:

```text
references/agents/retrieval-synthesiser.md
```

## Search widening policy

Widen the search only in this order:

1. related containers
2. additional indexes and manifests
3. broader metadata/title search
4. bounded full-text search
5. archives

Do not jump straight to repo-wide grep.

## Read budgets

Retrieval must stay bounded.

Default maximums:

- manifests inspected: 8
- indexes inspected: 6
- note candidates shortlisted: 12
- deep reads: 5
- archive candidates: 3

If the query remains unresolved after the budget is exhausted:

- return the best shortlist
- explain uncertainty
- suggest the next retrieval step

Do not silently expand into unbounded scanning.

## Adaptation rule

If the repository lacks one or more expected retrieval aids:

- fall back from `kb-index.json` to topic indexes
- fall back from topic indexes to manifests
- fall back from manifests to container names
- fall back from structured retrieval to bounded title and text search

The workflow should degrade gracefully rather than fail.
