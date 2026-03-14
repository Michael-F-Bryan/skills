---
name: knowledge-base-navigator
description: Query a structured repository knowledge base intelligently using ontology-aware routing, manifests, indexes, metadata, shortlist-based retrieval, and bounded deep reads. Prefer navigation and recognition over blind grep.
entrypoint: references/workflow.md
---

# Knowledge Base Navigator

This skill teaches an agent to query a repository as a **designed memory system**, not a pile of text files.

It is intended for repositories organised around shallow numbered PARA roots:

- `1-projects/`
- `2-areas/`
- `3-resources/`
- `4-archives/`

Both skills assume the same PARA layout (four roots, one level of containers); retrieval aids (manifests, indexes, note metadata) are described in this skill's references.

The skill helps the agent retrieve knowledge the way a human would:

- by knowing the system
- by predicting where something should live
- by recognising likely titles
- by using manifests, indexes, and summaries
- by reading a small shortlist deeply
- by using raw text search only as a fallback

## When to use

Use this skill when the agent needs to:

- find an existing note, rule, pattern, or principle
- answer a question using repository knowledge
- locate a half-remembered concept
- retrieve relevant prior work with bounded context use
- search intelligently during maintenance, planning, writing, or execution
- decide whether knowledge has already been captured before creating new notes
- suggest or trigger para-custodian maintenance when retrieval repeatedly fails due to missing manifests, indexes, or stale structure (e.g. many unclassified or misplaced files)

Do **not** use this skill as the first choice for:

- exact known-path reads
- one-off direct file access when the location is already known
- exhaustive repo-wide full-text searching with no routing attempt

## Core principle

Treat retrieval as a **routing problem**, not a keyword-matching problem.

The agent should not ask:

> What file contains these words?

It should ask:

> What kind of knowledge am I looking for, where should that kind of thing live, and which few candidates are most likely?

## Retrieval posture

Always search in this order:

1. classify the query intent
2. predict likely PARA roots and containers
3. inspect container manifests
4. inspect topic indexes
5. shortlist notes by title, aliases, metadata, and summaries
6. deeply read only top candidates
7. widen carefully if needed
8. use broad full-text search only as a fallback
9. search archives last unless the query is explicitly historical

Never begin with blind `grep` unless targeted retrieval has already failed.

## Required repository conventions

This skill works best when the repository contains:

- strong second-level container names
- `_manifest.md` files for important containers
- `index.md` files for major topics
- durable notes with good titles
- short summary lines near the top of notes
- optional frontmatter such as:
  - `aliases`
  - `kind`
  - `topics`
  - `query-patterns`
  - `related`
- optional generated index files such as:
  - `kb-index.json`

The agent should exploit these layers for progressive disclosure.

## Progressive disclosure

Load information in the cheapest useful order:

1. repository ontology
2. container manifests
3. topic indexes
4. note metadata
5. note summaries
6. full note bodies

Do not deep-read large numbers of files unless prior layers fail.

## Sub-agent architecture

This skill uses specialised sub-agents with strict inputs and outputs.

Agents:

- Query Intent Agent
- Container Routing Agent
- Candidate Shortlist Agent
- Deep Read Agent
- Retrieval Synthesiser Agent

Agents should **adapt rather than fail**.

If uncertain they should:

- make a best-effort shortlist
- annotate uncertainty
- continue the workflow

Only fail if the repository cannot be accessed at all.

## Success criteria

This skill is working when:

- the agent usually finds the right note from a small shortlist
- token use stays bounded as the repo grows
- retrieval relies more on structure than brute-force text search
- the agent can find knowledge even when the exact wording is unknown
- the agent avoids creating duplicate notes when equivalent knowledge already exists
