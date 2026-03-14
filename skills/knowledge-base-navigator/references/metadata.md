# Durable Note Metadata

This document defines optional metadata that improves retrieval quality.

Use it especially for durable notes in `3-resources/`.

## Recommended frontmatter

```yaml
title: Avoid Catch-All Category Folders
aliases:
  - avoid bucket folders
  - no misc folders
kind: atomic-note
topics:
  - para
  - classification
query-patterns:
  - where should notes live
  - avoid notes folders
  - document categories are bad
related:
  - active-outcome-beats-document-type
  - use-topic-containers-not-document-buckets
```

## Field meanings

### `aliases`

Alternative names or likely remembered phrasings.

### `kind`

Useful values:

- atomic-note
- topic-note
- template
- index
- manifest
- governance-note
- project-artefact

### `topics`

Major conceptual domains for routing and ranking.

### `query-patterns`

Likely user phrasings or search intents.

### `related`

Nearby notes likely to be relevant during retrieval.

## Retrieval rule

Prefer metadata-based shortlisting over body-content searching.

If metadata is missing:

- rely on title and summary
- do not invent metadata on the fly
