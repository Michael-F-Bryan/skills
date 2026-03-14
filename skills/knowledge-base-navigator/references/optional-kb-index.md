# Optional Machine-Readable KB Index

A generated `kb-index.json` can improve retrieval performance and reduce token use.

This is optional, but useful for larger repositories.

## Suggested location

```text
2-areas/workspace-governance/kb-index.json
```

## Suggested structure

```json
[
  {
    "path": "3-resources/atomic-notes/avoid-catch-all-category-folders.md",
    "title": "Avoid Catch-All Category Folders",
    "aliases": [
      "avoid bucket folders",
      "no misc folders"
    ],
    "kind": "atomic-note",
    "root": "3-resources",
    "container": "atomic-notes",
    "topics": [
      "para",
      "classification"
    ],
    "summary": "Use concrete topic or outcome containers rather than generic buckets.",
    "related": [
      "active-outcome-beats-document-type"
    ]
  }
]
```

## Retrieval rule

If `kb-index.json` exists:

- consult it before reading many note files
- use it to shortlist candidate paths
- treat it as a routing and ranking aid, not as the source of truth

If a shortlist candidate looks promising, open the actual note to confirm.

## Maintenance implication

When the repository changes significantly, the index should be refreshed. Refresh is typically done after para-custodian runs (or manually) using a script that scans note frontmatter and paths; see example in this skill's `scripts/` directory.

A stale index is still often useful for shortlisting, but live note content remains authoritative.
