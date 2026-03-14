# Container Manifest Standard

Important containers should include a `_manifest.md`.

The manifest is a cheap routing aid.

The agent should inspect manifests before deeper searching.

## Recommended structure

```md
# <container name>

## Purpose
What this container is for.

## Includes
- kinds of notes that belong here

## Excludes
- kinds of notes that do not belong here

## Likely queries
- examples of what someone might search here for

## Related
- related containers
- related indexes
```

## Example

```md
# para

## Purpose
Reference material about the PARA system used in this repository.

## Includes
- classification rules
- project vs area vs resource distinctions
- practical PARA heuristics
- shallow-structure guidance

## Excludes
- active migration work
- current project execution artefacts
- repo-specific governance rules unless distilled

## Likely queries
- where should this file live
- para classification rule
- projects vs resources
- avoid bucket folders

## Related
- 2-areas/workspace-governance
- 3-resources/atomic-notes
```

## Retrieval rule

If a manifest strongly excludes the query, deprioritise the container even if the name looks plausible.

If a manifest strongly includes the query, prioritise the container even if title similarity is weak.
