# Retrieval Order

This document defines the standard retrieval order.

The agent should follow this order unless there is a strong reason not to.

## Standard retrieval order

### 1. Classify the query

Determine:

- what kind of knowledge is being requested
- whether it is likely current or historical
- whether it is likely a rule, a concept, a template, or active work

### 2. Predict likely containers

Use repository ontology plus container names to produce a small set of likely locations.

Do not search the full repository yet.

### 3. Inspect manifests

Open `_manifest.md` files for the most likely containers.

Use them to decide:

- what the container includes
- what it excludes
- whether the query belongs there

### 4. Inspect topic indexes

Open `index.md` for the best candidate topics.

Use them to recognise likely note titles and related concepts.

### 5. Search titles and metadata

Search candidate containers by:

- note title
- aliases
- `kind`
- `topics`
- `query-patterns`
- `related`

### 6. Inspect note summaries

Use the first summary lines of shortlisted notes for recognition-based filtering.

### 7. Deep-read only top candidates

Read a bounded shortlist deeply.

### 8. Widen carefully

If unresolved:

- inspect related containers
- inspect more indexes
- perform bounded full-text search
- inspect archives last

## Anti-pattern

Do not start with:

- blind repo-wide grep
- opening many full note bodies
- archive scanning before active roots
- title-agnostic text search across the entire repository

## Recognition over recall

Humans often retrieve notes by recognising a shortlist, not by recalling exact wording.

The agent should do the same.

That means:

- build a shortlist
- inspect titles and summaries
- choose the most plausible candidate
- widen only if needed
