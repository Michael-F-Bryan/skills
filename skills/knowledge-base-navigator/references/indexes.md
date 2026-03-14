# Topic Index Standard

Major topics should include an `index.md`.

Indexes support recognition-based retrieval.

They let the agent do what humans do:

- start from a known area
- scan likely note titles
- follow related links

## Recommended structure

```md
# <topic> Index

## Core Notes
- [[...]]
- [[...]]

## Atomic Notes
- [[...]]
- [[...]]

## Templates or Examples
- [[...]]
- [[...]]

## Related Topics
- [[...]]
- [[...]]
```

## Example

```md
# PARA Index

## Core Notes
- [[PARA-summary]]
- [[PARA-projects]]
- [[PARA-areas]]
- [[PARA-resources]]
- [[PARA-archives]]

## Atomic Notes
- [[active-outcome-beats-document-type]]
- [[avoid-catch-all-category-folders]]
- [[prefer-splitting-containers-over-adding-nesting]]

## Related Topics
- [[workspace-governance]]
- [[knowledge-base-navigation]]
```

## Retrieval rule

When a likely topic container exists and has an index, inspect the index before broad searching inside the container.
