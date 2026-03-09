# Coding Fingerprint Analysis Worksheet

Use this file as the contract between the coordinator and sub-agents.

## Working Directory

All artefacts live under:

```text
_working/coding-fingerprint/
```

Create the directory before starting analysis.

## Phase 0 Artefact

### `sample-inventory.md`

Required sections:

```markdown
# Sample Inventory

## Scope
- fingerprint subject:
- target output name:
- date:

## Samples
### `<sample-slug>`
- location:
- primary language:
- stack:
- authorship confidence: high | medium | low
- included because:
- available evidence:
- caveats:

## Coverage Gaps
- missing evidence:
- distorted samples:
- follow-up:
```

## Phase 1 Artefacts

Create one file per project:

```text
project-profile-<slug>.md
```

Required sections:

```markdown
# Project Profile: <name>

## Context
- sample slug:
- project type:
- language and stack:
- evidence inspected:
- confidence:

## Signature Decisions
- 3-7 high-signal decisions with concrete evidence

## Dimension Notes
### Naming And Vocabulary
### Function And Module Shape
### Abstractions And Boundaries
### Data Modelling
### Error Handling And Validation
### Tests And Verification
### Comments And Documentation
### Refactor Habits
### Architecture And Dependencies
### Review Heuristics And Avoidances

## Strongest Evidence
- short quoted snippets or concise references to code structures

## Weak Signals To Ignore
- framework defaults, generated code, or one-off anomalies

## Provisional Principles
- inferred principles, each tagged with confidence

## Open Questions
- contradictions or missing evidence
```

### Phase 1 sub-agent rules

- Analyse one project or one lens only
- Cite evidence, do not just describe impressions
- Prefer behaviour and trade-offs over formatting details
- Mark low-confidence inferences explicitly

## Phase 2 Artefacts

### `cross-project-patterns.md`

Required sections:

```markdown
# Cross-Project Patterns

## Repeated Across Samples
- pattern:
  evidence:
  confidence:

## Context-Specific Only
- pattern:
  tied to:
  reason:

## Contradictions
- tension:
  explanation:
  follow-up:
```

### `coding-principles.md`

Required sections:

```markdown
# Coding Principles

## Core Principles
- principle:
  because:
  evidence:

## Boundary Rules
- what the author centralises
- what the author localises
- what the author refuses to abstract

## Review Instincts
- likely objections this person would raise in review
```

### `fingerprint-spectrum.md`

Use axes that predict implementation behaviour.

Required sections:

```markdown
# Fingerprint Spectrum

- Local Pragmatism / Global Consistency: [1-5]
- Duplication Tolerance / Abstraction Bias: [1-5]
- Explicitness / Compression: [1-5]
- Early Validation / Late Validation: [1-5]
- Test-First Bias / Implementation-First Bias: [1-5]
- Domain Purity / Framework Affinity: [1-5]

## Notes
- why each rating exists
```

## Phase 3 Artefacts

### `drift-risks.md`

```markdown
# Drift Risks

- risk:
  why it is tempting:
  evidence against it:
```

### `counterexamples.md`

```markdown
# Counterexamples

- supposed pattern:
  counterexample:
  interpretation:
```

### `validation-notes.md`

```markdown
# Validation Notes

## Independent Re-derivation
- what a second analyser agreed on
- what they disagreed on

## Predictive Checks
- small task:
- predicted choices:
- matched source evidence:
- mismatches:

## Refinements
- updates required before final delivery
```

## Handoff Rule

Do not begin Phase 4 until these are true:

- every sample has a `project-profile-<slug>.md`
- synthesis artefacts exist and cite evidence
- challenge artefacts identify at least one drift risk
- unresolved contradictions are either explained or left visible

## Sub-agent Prompt Skeleton

Use this structure when spawning an analysis sub-agent:

```text
Task: Analyse sample <slug> for coding fingerprint extraction.
Read: sample inventory and the assigned project only.
Write: _working/coding-fingerprint/project-profile-<slug>.md
Focus: high-signal coding decisions, principles, and avoidances.
Do not: generate the final fingerprint or collapse across other samples.
```
