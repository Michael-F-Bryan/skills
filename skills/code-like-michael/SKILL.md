---
name: code-like-michael
description: "Default coding style for all implementation, refactoring, and code review unless the user specifies otherwise. Applies Michael's conventions: explicit contracts, thin entrypoints, practical boundaries, anti-ceremony abstractions, deterministic tooling, and operator-shaped CLIs. Use whenever writing or changing code, touching architecture, or reviewing PRs."
---

# Code Like Michael

This skill is an execution policy for agents. It converts labelled examples in `references/examples/` into concrete coding decisions.

If you are writing code, changing architecture, reviewing PRs, or proposing refactors in this repo, apply this skill.

## When to Use

Use this skill when the work needs to feel deliberately authored in Michael's style, not merely correct:

- new features or bug fixes where architecture choices matter
- refactors that touch boundaries, config, IO, module layout, or CLI shape
- review passes where you need to distinguish `works` from `fits this repo`
- internal tools and utility CLIs that should feel operator-friendly rather than script-like

Do not treat this as permission for decorative rewrites. Prefer narrow, task-shaped changes unless the request explicitly asks for broader restructuring.

## Ground Truth

Treat these files as source-of-truth calibration:

- `references/examples/` (labelled examples; highest authority)
- `references/dimensions.md` (20 dimensions)
- `references/annotations-rubric.md` (anchor definitions)

When uncertain, prefer consistency with labelled examples over generic best practices.

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
- Keep `main` thin; use `clap` derive-based CLI modelling.
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

- Centralise config in one typed loader; avoid distributed `process.env` reads.
- Prefer explicit domain types/unions at boundaries.
- Avoid throwing raw strings.
- Keep CLIs and handlers as orchestration shells, not business-logic dumps.
- Create seams for external IO/time/randomness where tests benefit.

## Internal CLI and Operator Tooling Defaults

When the code is a CLI or internal operator tool, apply these additional defaults. This is the main update from the `20260617_143450_10d6ab11` session.

See `references/internal-cli-philosophy.md` for the full rationale and examples.

1. **Treat the CLI as a serious operator boundary.**
   - It is not a thin wrapper around random functions.
   - Its job is to make a messy system operable.
2. **Shape commands around operator tasks, not the source tree.**
   - Command paths should be guessable from the job to be done.
   - Repeated snippets and tribal-knowledge workflows often want a first-class subcommand.
3. **Keep entrypoints and handlers thin.**
   - Process-wide setup, parse and validate arguments, assemble dependencies, dispatch, render result.
   - Do not hide the system's main understanding inside the CLI shell.
4. **Parse loose inputs early into typed objects.**
   - Paths, URLs, request payloads, config, and option combinations should be normalised and validated at the boundary.
5. **Teach through help text.**
   - `--help` is part of the interface contract.
   - Encode invariants, examples, caveats, and adjacent command hints where the operator will actually look.
6. **Civilise awkward backends and protocols.**
   - Normalise weird shapes, reject bad combinations up front, and expose a task-shaped command instead of leaking raw API ceremony.
7. **Tell the truth.**
   - No fake flags, no silent fallbacks, no misleading success, no accepting malformed input just to fail later.
8. **Serve humans, scripts, and agents at the same time.**
   - Human-readable defaults are good.
   - Stable JSON or machine-readable output should exist where automation wants it.
   - Keep progress and chatter off structured stdout.

## Dimension Application Rules

Use this as a quick execution map while coding.

1. **Transformation Style**: favour declarative transforms when linear and clear.
2. **Control Flow Shape**: guard clauses first; flatten branch trees.
3. **Mutation Budget**: immutable by default, mutation only where local and useful.
4. **Error Semantics**: preserve cause + context; avoid generic failure labels.
5. **Boundary Contracts**: parse, then operate; avoid loosely typed pass-through payloads.
6. **Naming**: identifiers should encode domain intent, not implementation trivia.
7. **Abstraction Threshold**: extract when complexity/reuse justifies it, not preemptively.
8. **Commenting**: explain "why/constraint/tradeoff", never narrate obvious mechanics.
9. **Module Cohesion**: one module, one reason to change.
10. **Dependency Directionality**: avoid layering theatre and direction violations.
11. **Boundary Surface Area**: minimal public API; rich internal domain modelling.
12. **Cross-Cutting Placement**: keep logs/metrics/auth at deliberate seams.
13. **Testability**: inject unstable dependencies (clock, network, random, env).
14. **Concurrency Discipline**: prefer well-known primitives/libraries over bespoke concurrency scaffolding.
15. **Entry-Point Architecture**: thin CLI/service entrypoints that delegate.
16. **Repo Topology**: organise by feature/responsibility, not generic buckets.
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
- CLI surfaces organised around package names instead of operator tasks
- Help text omitting invariants, examples, or dangerous constraints.
- Fake or placeholder flags that imply behaviour the tool does not implement
- Mixing machine-readable stdout with human progress noise
- Comments that duplicate the code line-by-line
- Hard-coded network/time dependencies in logic that should be testable
- Solving a generic nearby problem instead of the actual local problem
- Tests that assert mocked choreography rather than observable behaviour
- Speculative options, unused helpers, or "future-proofing" left behind
- Bypassing existing config/logging/tracing/auth/IO seams instead of using them

## Implementation Workflow (Agent)

When this skill is active, follow this sequence:

1. **Classify the change** across micro/meso/macro dimensions.
2. **Design boundaries first**: identify domain types, seams, and entrypoint responsibilities.
3. **Implement concretely** with minimal necessary abstraction.
4. **Reshape first-pass output as a draft**, not an artefact to preserve. Apply this default sequence until the code looks deliberately authored for this repository:
   1. delete excess structure
   2. recover local domain names
   3. move validation to the correct boundary
   4. preserve cause and context in errors
   5. test the real seam, not its scaffolding
   6. confirm every remaining file has a reason to exist
5. **Run a style self-audit** using the checklist below before presenting.

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

When reviewing code, prioritise findings in this order:

1. Broken/weak boundaries (contracts, validation, domain typing)
2. Architecture drift (fat entrypoints, mixed responsibilities, leaky surfaces)
3. Testability regressions (hard-coded side effects, missing seams)
4. Error/context quality
5. Readability and naming quality

Keep feedback concrete and propose specific reshaping steps, not abstract style advice.
