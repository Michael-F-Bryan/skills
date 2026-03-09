# Coding Fingerprint Artefact Contracts

Use this file as the source of truth for `_working/coding-fingerprint/` artefacts.

Use it when you need:

- the required files for a phase
- the required sections for an artefact
- the handoff rule between discovery, synthesis, challenge, and delivery
- the default prompt skeleton for analysis workers

Do not duplicate these contracts in `SKILL.md`. Read `SKILL.md` for workflow and quality bar, then use this file for the exact output shape.

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
- repo shape:
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
- repo shape:
- evidence inspected:
- confidence:

## Signature Decisions
- 3-7 high-signal decisions with concrete evidence

## Dimension Notes
### Naming And Vocabulary
### Function And Module Shape
### Repo Shape And Delivery Posture
### Abstractions And Boundaries
### Data Modelling
### Error Handling And Validation
### Tests And Verification
### Comments And Documentation
### CI/CD And Operational Hygiene
### Refactor Habits
### Architecture, Dependencies, And DI
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

### `portfolio-preferences.md`

Use this artefact to capture repo-shaping behaviour that survives across projects.

Required sections:

```markdown
# Portfolio Preferences

## Evidence Weighting
- primary signal:
- calibration signal:
- operational reading rule:

## Repo Size And Shape
- default:
- avoid:
- evidence:
- confidence:

## Utility Project Vs Workspace Vs Monorepo Preference
- utility project:
- workspace:
- monorepo:
- practical default:
- confidence:

## Experiments Vs Toy Vs Production-Leaning Posture
- default posture:
- meaning:
- avoid:
- evidence:
- confidence:

## CI/CD Values
- default CI shape:
- CD posture:
- avoid:
- evidence:
- confidence:

## Documentation Values
- preferred docs:
- practical default:
- evidence:
- confidence:

## Language And Paradigm Preferences
- strongest modern signal:
- paradigm bias:
- framework stance:
- confidence:

## Dependency And DI Posture
- dependency posture:
- DI posture:
- good seams:
- avoid:
- evidence:
- confidence:

## Typing Strictness
- core preference:
- common patterns:
- context sensitivity:
- avoid:
- evidence:
- confidence:

## When Abstractions Are Introduced
- introduce when:
- prefer generation when:
- practical default:
- evidence:
- confidence:

## Strictness Vs Context Sensitivity
- default rule:
- be strict about:
- be tolerant when:
- practical default:
- evidence:
- confidence:

## Default Repo-Shaping Moves
- repeated defaults another agent should apply
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
- `portfolio-preferences.md` exists and answers repo-shaping questions
- challenge artefacts identify at least one drift risk
- unresolved contradictions are either explained or left visible

### Phase 2 synthesis rules

- Synthesis workers may read all project profiles and the sample inventory.
- Promote only patterns that recur across samples or have unusually strong supporting evidence.
- Keep durable traits, context-specific choices, contradictions, and open questions separate.
- Treat repo-shaping and dependency posture as first-class output, not supporting colour.

### Phase 3 challenge rules

- Challenge workers should try to break the draft fingerprint, not defend it.
- Test for overfitting, avoidances, reproducibility, and predictive power.
- Leave visible disagreements in `validation-notes.md` rather than smoothing them over.
- If a supposed trait fails under challenge, demote it or qualify it explicitly.

## Phase 4 Handoff Package

Once the handoff rule passes, delivery can begin.

Delivery reads:

- the synthesis artefacts from this file
- the challenge artefacts from this file
- `references/fingerprint-template.md`

Use `references/example-coding-fingerprint.md` only if the target output shape is still unclear or you are performing final calibration.

## Sub-agent Prompt Skeleton

Use this structure when spawning an analysis sub-agent:

```text
Task: Analyse sample <slug> for coding fingerprint extraction.
Read: sample inventory and the assigned project only.
Write: _working/coding-fingerprint/project-profile-<slug>.md
Focus: high-signal coding decisions, repo-shaping preferences, principles, and avoidances.
Do not: generate the final fingerprint or collapse across other samples.
```
