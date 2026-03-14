# Agent Contracts

This document summarises what each retrieval sub-agent must do.

## General rules

All agents must:

- stay within bounded read budgets
- prefer structured navigation over body scanning
- annotate uncertainty rather than failing
- produce outputs that downstream agents can consume cheaply

## Query Intent Agent

Input

- user query
- ontology

Output

- `intent-report.json`

Pass criteria

- narrows search space
- generates useful rewritten forms

## Container Routing Agent

Input

- `intent-report.json`
- manifests
- repo tree

Output

- `routing-report.json`

Pass criteria

- small plausible set of containers
- clear routing reasons

## Candidate Shortlist Agent

Input

- `intent-report.json`
- `routing-report.json`
- indexes and metadata

Output

- `shortlist-report.json`

Pass criteria

- bounded candidate set
- title/metadata-driven ranking

## Deep Read Agent

Input

- `shortlist-report.json`

Output

- `deep-read-report.json`

Pass criteria

- confirms best candidates with minimal reading
- extracts concrete evidence

## Retrieval Synthesiser Agent

Input

- all prior reports

Output

- `retrieval-result.md`

Pass criteria

- direct answer
- honest uncertainty
- recommended widening step if unresolved
