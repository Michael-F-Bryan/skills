---
name: code-like-michael
description: Write, refactor, and review code in Michael's style; explicit contracts, thin entrypoints, practical boundaries, anti-ceremony abstractions, deterministic tooling, and architecture that scales from function internals to repository shape.
---

# Code Like Michael

This skill is an execution policy for agents. It converts labeled examples in `references/examples/` into concrete coding decisions.

If you are writing code, changing architecture, reviewing PRs, or proposing refactors in this repo, apply this skill.

## Ground Truth

Treat these files as source-of-truth calibration:

- `references/examples/` (labeled examples; highest authority)
- `references/dimensions.md` (20 dimensions)
- `references/annotations-rubric.md` (anchor definitions)

When uncertain, prefer consistency with labeled examples over generic best practices.

## Style North Star

Write code that is:

1. **Concrete first, abstract second**: extract only when an abstraction clearly earns its keep.
2. **Boundary strict**: parse into typed/domain models early; avoid "stringly" and loose dictionary contracts.
3. **Thin at the edges**: entrypoints orchestrate, domain modules decide, adapters perform IO.
4. **Operationally explicit**: deterministic tooling, obvious command paths, documented and typed configuration.
5. **Easy to reason about**: guard clauses, meaningful names, comments that explain intent and constraints.

## Non-Negotiables (Default)

Unless the user explicitly asks otherwise, treat these as MUST-level defaults:

1. **No runtime env reads in random application code.**
   - Load config once near startup, parse into a typed config object, inject downstream.
2. **No placeholder abstractions.**
   - "Class with one pass-through method" and speculative repository interfaces are usually rejected.
3. **No broad leaky surfaces by default.**
   - Keep exports narrow, enforce invariants with constructors/factories and domain types.
4. **No deeply nested control flow unless unavoidable.**
   - Prefer early returns and branch flattening.
5. **No generic/opaque error handling when domain context matters.**
   - Keep cause + context; prefer typed or structured error paths.

## Language-Specific Defaults

The same philosophy applies across languages, but tactics differ.

### Rust

- Prefer iterator pipelines for straightforward transformations.
- Prefer typed errors over `String` errors for domain flows.
- Keep `main` thin; use `clap` derive-based CLI modeling.
- Prefer domain newtypes/enums over raw primitives for constrained values.
- Avoid excess `let mut`; mutate only where it pays for clarity/perf.

### Go

- Prefer simple, concrete code over heavyweight repository layering.
- Validate boundary values explicitly (zero values are common failure mode).
- Avoid `flag` for complex CLIs; use explicit command parsers like `kong` and subcommands.
- Prefer explicit dependency injection for testability, but avoid interface explosion.
- Handle errors with context; avoid ambiguous `errors.New("failed")`.

### Python

- Prefer typed models (for example Pydantic/dataclasses at boundaries) over `Dict[str, Any]` contracts.
- Keep side effects at edges; pure core transformations in dedicated functions.
- Use straightforward control flow and explicit invariants.
- Prefer meaningful exceptions with context over vague `ValueError("bad input")`.

### TypeScript

- Centralize config in one typed loader; avoid distributed `process.env` reads.
- Prefer explicit domain types/unions at boundaries.
- Avoid throwing raw strings.
- Keep CLIs and handlers as orchestration shells, not business-logic dumps.
- Create seams for external IO/time/randomness where tests benefit.

## Dimension Application Rules

Use this as a quick execution map while coding.

1. **Transformation Style**: favor declarative transforms when linear and clear.
2. **Control Flow Shape**: guard clauses first; flatten branch trees.
3. **Mutation Budget**: immutable by default, mutation only where local and useful.
4. **Error Semantics**: preserve cause + context; avoid generic failure labels.
5. **Boundary Contracts**: parse, then operate; avoid loosely typed pass-through payloads.
6. **Naming**: identifiers should encode domain intent, not implementation trivia.
7. **Abstraction Threshold**: extract when complexity/reuse justifies it, not preemptively.
8. **Commenting**: explain "why/constraint/tradeoff", never narrate obvious mechanics.
9. **Module Cohesion**: one module, one reason to change.
10. **Dependency Directionality**: avoid layering theater and direction violations.
11. **Boundary Surface Area**: minimal public API; rich internal domain modeling.
12. **Cross-Cutting Placement**: keep logs/metrics/auth at deliberate seams.
13. **Testability**: inject unstable dependencies (clock, network, random, env).
14. **Concurrency Discipline**: prefer well-known primitives/libraries over bespoke concurrency scaffolding.
15. **Entry-Point Architecture**: thin CLI/service entrypoints that delegate.
16. **Repo Topology**: organize by feature/responsibility, not generic buckets.
17. **Config Strategy**: one typed config load path near startup.
18. **IO Isolation**: separate pure domain logic from transport/storage.
19. **Tooling Contract**: explicit, reproducible scripts and pinned toolchain versions.
20. **Evolution Posture**: migrations and deprecations where compatibility matters.

## Anti-Patterns to Reject by Default

Flag these unless a clear task-specific reason exists:

- `util`/`helpers` dumping grounds with unrelated concerns
- Deeply nested `if/else` trees where early returns would simplify
- Generic names (`x`, `data`, `thing`, `doStuff`) in domain code
- Runtime env access from request handlers/domain functions
- "Stringly typed" domain fields when constrained types are known
- Entry-point files containing domain/business logic
- Comments that duplicate the code line-by-line
- Hard-coded network/time dependencies in logic that should be testable

## Implementation Workflow (Agent)

When this skill is active, follow this sequence:

1. **Classify the change** across micro/meso/macro dimensions.
2. **Design boundaries first**: identify domain types, seams, and entrypoint responsibilities.
3. **Implement concretely** with minimal necessary abstraction.
4. **Run a style self-audit** using the checklist below before presenting.

Prefer surgical changes. Do not reformat, rename, repartition modules, or introduce new architecture unless it directly supports the requested change.

## Pre-Response Self-Audit Checklist

Before returning code, verify:

- Are boundaries typed and explicit?
- Is config loaded centrally and injected?
- Are entrypoints thin?
- Is control flow flattened where possible?
- Are names domain-meaningful?
- Are comments high-signal (why/constraints) rather than narration?
- Are abstractions justified by real complexity/reuse?
- Are IO/time/env dependencies isolated enough for testing?
- Are errors specific and context-bearing?
- Is the repo/module shape moving toward cohesive responsibility boundaries?

If two style goals conflict, choose the option that:

1. strengthens boundary correctness,
2. keeps execution model explicit,
3. reduces accidental complexity.

## Review Mode Guidance

When reviewing code, prioritize findings in this order:

1. Broken/weak boundaries (contracts, validation, domain typing)
2. Architecture drift (fat entrypoints, mixed responsibilities, leaky surfaces)
3. Testability regressions (hard-coded side effects, missing seams)
4. Error/context quality
5. Readability and naming quality

Keep feedback concrete and propose specific reshaping steps, not abstract style advice.
