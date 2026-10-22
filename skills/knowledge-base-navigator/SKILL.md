---
name: knowledge-base-navigator
description: Find and ground answers in a structured knowledge base.
---

# Knowledge Base Navigator

Retrieve directly; a routine question does not need five specialised agents or staged handoff files. Use for finding prior knowledge in a repository/vault, not a known-path read.

## Structure → shortlist → read → counterevidence → answer

1. **Inspect structure.** Read the actual layout and useful README, manifests or topic indexes. Use PARA if present; do not require it or reorganise the repository. A known filename/identifier can go straight to targeted search.
2. **Shortlist.** Use titles, aliases, summaries and metadata to select a small set of likely sources. An existing machine index is a routing aid, not truth. Do not generate an index merely to answer one question.
3. **Read.** Open the actual candidates, following relevant links. Preserve qualifications, ownership and applicability. Broaden weak results with synonyms, adjacent containers or targeted full-text search; empty results do not establish absence.
4. **Seek counterevidence.** Look for corrections, superseding decisions, conflicting notes and stale assumptions. Archives may matter immediately for historical questions. Prefer authoritative, current evidence; explain unresolved disagreement rather than averaging it away.
5. **Answer.** Cite source paths/sections for material claims. Separate source facts from inference, explain gaps and stop when support is adequate. Do not create or update notes unless requested.

## Optional aids

An existing PARA layout may offer projects, areas, resources and archives. Adapt to actual names. For an already maintained PARA index see [machine-readable index](references/optional-kb-index.md); its [builder](scripts/build_kb_index.py) is maintenance tooling, not a retrieval prerequisite. It requires PyYAML and indexes one container level only.

## Check

Did you read actual sources rather than index summaries? Did you look for contrary evidence or corrections? Are conclusions and gaps traceable? A confident retrieval report without supporting content is not evidence.
