---
name: coding-fingerprint-wizard
description: Analyse several example projects to synthesise a reusable coding fingerprint. Use when the user wants to capture a person's coding style, engineering principles, architectural tendencies, or implementation habits so agents can reproduce them consistently.
---

# Coding Fingerprint Wizard

Create a reusable coding fingerprint from example projects.

The goal is not to infer formatter trivia or generic "clean code" advice. The goal is to identify the decisions that make a person's code recognisable: how they shape modules, where they validate, what they test, what they refuse to abstract, and which trade-offs they make repeatedly.

## What This Produces

The output is a `coding-fingerprint-[name]/SKILL.md` file that another agent can apply when planning, writing, reviewing, or refactoring code.

## Core Model: Double Diamond

This skill uses a diverge-converge workflow:

1. **Discover**: spread out, gather evidence, inspect multiple projects and lenses in parallel
2. **Define**: converge on the durable patterns that actually survive across contexts
3. **Develop**: diverge again by stress-testing the draft fingerprint against counterexamples and edge cases
4. **Deliver**: converge into a final, reusable coding fingerprint skill

Treat this as a strict operating model, not a metaphor.

## Coordinator Rules

The top-level agent is a coordinator.

- Spawn sub-agents for the detailed analysis
- Run parallel sub-agents where the work is independent
- Enforce the artefact contracts in `references/analysis-worksheet.md`
- Decide when the evidence is broad enough to converge
- Resolve conflicts between sub-agent outputs

Do not let the coordinator do the full analysis itself unless it is reconciling disagreements or repairing a failed handoff.

## Before You Begin

Use samples that reflect the person's real engineering style.

**Good samples:**
- 2-5 projects with meaningful authorship signal
- Code with tests, docs, commit history, or review context when available
- Projects from roughly the same era and responsibility level
- Code the person would still endorse

**Avoid:**
- Heavily templated or generated repositories
- One-off experiments with little behavioural signal
- Team code where authorship is unclear
- Samples dominated by a framework's generated structure

If the sample set mixes very different contexts, note that explicitly and treat context-specific patterns as weaker evidence.

## Workspace

Use `_working/coding-fingerprint/` for all intermediate artefacts.

Required files:
- `sample-inventory.md`
- `cross-project-patterns.md`
- `coding-principles.md`
- `fingerprint-spectrum.md`
- `drift-risks.md`
- `counterexamples.md`
- `validation-notes.md`

Per-project files:
- `project-profile-<slug>.md`

Read `references/analysis-worksheet.md` before starting Phase 1.

## Workflow

### Phase 0: Prepare Inputs

Create `sample-inventory.md`.

For each sample project, record:
- path or identifier
- primary language and stack
- why it belongs in the set
- known authorship confidence
- available evidence: code, tests, commits, docs, PRs, issues
- important context that may distort the fingerprint

Do not start synthesis until the inventory exists.

### Phase 1: Discover

Run sub-agents in parallel.

Default pattern:
- One sub-agent per project for a project profile
- Optional extra sub-agents by lens if the projects are large: testing, architecture, review style, or error handling

Each discovery sub-agent must produce a structured artefact, not loose notes. Use `project-profile-<slug>.md` and follow the worksheet exactly.

Focus on signals such as:
- naming and vocabulary
- function and module shape
- abstractions and boundaries
- data modelling
- error handling and validation
- tests and verification
- comments and documentation
- refactor habits
- architecture and dependency choices
- review heuristics and avoidances

The goal of this phase is breadth. Prefer collecting too much evidence over collapsing to conclusions early.

### Phase 2: Define

Run a synthesis sub-agent after the project profiles exist.

It must create:
- `cross-project-patterns.md`
- `coding-principles.md`
- `fingerprint-spectrum.md`

This is the first convergence point. Separate:
- durable fingerprint traits
- context-specific project choices
- contradictory signals
- open questions that need more evidence

Do not promote a pattern into the fingerprint unless it appears across projects or is supported by strong surrounding evidence.

### Phase 3: Develop

Run challenge sub-agents to stress-test the draft fingerprint.

At minimum, cover:
- overfitting: which traits only appear in one project
- avoidances: what the author consistently does not do
- reproducibility: whether independent agents infer similar rules
- predictive power: whether the fingerprint implies plausible implementation choices

Outputs:
- `drift-risks.md`
- `counterexamples.md`
- `validation-notes.md`

This is the second divergence. The aim is to break a weak fingerprint before it becomes canonical.

### Phase 4: Deliver

Generate the final skill using `references/fingerprint-template.md`.

Save it as:

```text
coding-fingerprint-[name]/
└── SKILL.md
```

The generated fingerprint must include:
- a one-paragraph summary
- calibration axes
- core coding behaviours
- architectural tendencies
- testing and error-handling preferences
- signature patterns
- anti-patterns and avoidances
- a pre-flight checklist

### Phase 5: Validate

Use a fresh sub-agent that has access only to:
- the generated fingerprint skill
- a small, representative coding task

Ask it to propose or critique a change in the inferred style, then compare that output back to the source projects.

Refine the fingerprint if any of these are true:
- it sounds like generic senior-engineer advice
- it contradicts the project evidence
- it overfits to one codebase
- it captures style but not principles
- another agent cannot reliably apply it

## Fingerprint Heuristics

Prefer high-signal patterns over surface polish.

**Strong signals:**
- where validation lives
- how boundaries are drawn
- how tests express intent
- what gets abstracted versus duplicated
- preferred error semantics
- naming choices that reveal domain modelling
- the shape of refactors and incremental changes

**Weak signals:**
- formatter output
- language defaults with no visible choice
- isolated clever code
- framework boilerplate

## Anti-Patterns

Avoid these failures:

- reducing the fingerprint to style-guide clichés
- treating one impressive project as the whole person
- confusing ecosystem constraints with personal preference
- inferring principles without citing evidence
- producing a fingerprint that another agent cannot operationalise
- skipping the challenge phase because the synthesis "looks right"

## Output Quality Bar

The final fingerprint is good only if it helps another agent answer questions like:

- How would this person split the module?
- Where would they validate input?
- What would they test first?
- Which abstraction would they reject as premature?
- What code smell would they flag immediately?

If the skill cannot answer those questions, the fingerprint is still too vague.

## Additional Resources

- Artefact contracts and sub-agent deliverables: [references/analysis-worksheet.md](references/analysis-worksheet.md)
- Final output template: [references/fingerprint-template.md](references/fingerprint-template.md)
- Worked example: [references/example-coding-fingerprint.md](references/example-coding-fingerprint.md)

## Related Skills

- Use `working-docs` when you need scratch notes outside this workflow
- Use `test-driven-development` when validating the generated fingerprint against an implementation task

