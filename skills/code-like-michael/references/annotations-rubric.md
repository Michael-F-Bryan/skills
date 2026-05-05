# Annotation Rubrics v1 (File-Level Labels + Repo Rollup)

This rubric operationalizes the 20 dimensions from `dimensions.md`.

## Labeling Contract

- Unit: one source file
- Output per dimension: `score` (1-5), `confidence` (`low|medium|high`), `evidence` (1-3 short notes)
- If evidence is genuinely absent, use `3` with `low` confidence and note "insufficient evidence"

## Global Scale Anchors (Apply to All Dimensions)

- `1`: strong opposite tendency
- `2`: mild opposite tendency
- `3`: mixed, neutral, or unknown
- `4`: mild alignment
- `5`: strong, repeated alignment

## Evidence Rules

- Prefer direct code evidence in the file: symbols, control flow, imports, tests, docs comments, config calls
- Avoid mind-reading intent; infer only from observable patterns
- When in doubt between adjacent scores, choose lower confidence instead of forcing certainty

## Rollup Rules

- File -> module/package: weighted average by LOC or function count
- Module/package -> repo: weighted average, but apply explicit macro weight uplift for:
  - CLI entrypoints
  - dependency/build config files
  - module boundary and wiring files

---

## Dimension Rubrics (1-5 Anchors)

### 1) Transformation Style
- `1`: mostly imperative loops and manual accumulation for transform-heavy logic
- `3`: mixed loops and declarative transforms
- `5`: predominantly declarative transformation pipelines/combinators where appropriate

### 2) Control Flow Shape
- `1`: deep nesting and branch pyramids are common
- `3`: mixed style, occasional nesting hotspots
- `5`: mostly linear flow with guard clauses/early exits

### 3) Mutation Budget
- `1`: frequent mutable state, wide mutation scope
- `3`: moderate mutation with some containment
- `5`: immutable-by-default with narrow, intentional mutation windows

### 4) Error Semantics Explicitness
- `1`: generic/opaque errors, limited context propagation
- `3`: some typed/contextual handling mixed with opaque paths
- `5`: explicit typed/context-rich errors and systematic propagation

### 5) Contract Strictness at Boundaries
- `1`: boundary assumptions mostly implicit
- `3`: partial validation/invariant checks
- `5`: explicit and consistent input/output validation plus invariants

### 6) Naming Semantics Density
- `1`: generic names dominate (`data`, `tmp`, `value`, `doThing`)
- `3`: mixed generic and domain-intent naming
- `5`: identifiers encode role, domain, and intent consistently

### 7) Local Abstraction Threshold
- `1`: extraction is erratic or too-late (large tangled local blocks)
- `3`: partially consistent extraction behavior
- `5`: consistent extraction policy based on complexity/reuse pressure

### 8) Commenting Philosophy
- `1`: comments mostly narrate obvious mechanics or are misleading/stale
- `3`: mixed quality comments
- `5`: comments focus on "why/constraints/tradeoffs", not obvious "what"

### 9) Module Cohesion
- `1`: file mixes unrelated responsibilities
- `3`: mostly cohesive with notable drift
- `5`: focused responsibility and clear thematic boundary

### 10) Dependency Directionality Discipline
- `1`: bidirectional/tangled dependency flow is common
- `3`: partial directional rules with exceptions
- `5`: clear directional dependency policy with minimal violations

### 11) Boundary Surface Area
- `1`: broad exposed APIs and leaky internals
- `3`: moderate boundary discipline
- `5`: intentionally narrow interfaces and minimal exports

### 12) Cross-Cutting Concern Placement
- `1`: logging/metrics/auth/retries scattered through domain logic
- `3`: partially centralized with leakage
- `5`: consistent placement at intended boundaries/adapters

### 13) Testability by Construction
- `1`: hard-wired dependencies and non-deterministic seams
- `3`: some injectable seams, partial determinism
- `5`: dependencies and contracts designed for isolation and deterministic tests

### 14) Concurrency Model Discipline
- `1`: ad hoc concurrency primitives and weak cancellation/ownership patterns
- `3`: some consistency, some drift
- `5`: explicit, consistent concurrency model and lifecycle handling

### 15) Entry-Point Architecture
- `1`: entrypoints contain business logic and orchestration is tangled
- `3`: partial delegation with some leakage
- `5`: entrypoints are thin shells delegating to domain/application modules

### 16) Repository Topology Style
- `1`: structure appears ad hoc and unstable
- `3`: some convention, some inconsistency
- `5`: coherent, repeated topology pattern aligned to architectural intent

### 17) Configuration and Environment Strategy
- `1`: ad hoc env/config reads across codebase, minimal validation
- `3`: some centralization, partial schema/defaults
- `5`: centralized typed config, validated at startup with explicit defaults

### 18) Data Boundary and IO Isolation
- `1`: IO/persistence concerns mixed directly into core domain paths
- `3`: partial separation
- `5`: clear adapters/boundaries with minimal leakage into domain logic

### 19) Build/Tooling Contract
- `1`: workflows implicit, non-reproducible, or undocumented
- `3`: partially reproducible with gaps
- `5`: deterministic and explicit build/test/lint/dev contracts

### 20) Evolution Posture
- `1`: contract changes are frequent and unmanaged
- `3`: some migration/deprecation handling
- `5`: stable compatibility posture with explicit migration/deprecation discipline

---

## Language-Specific Cues

Use these cues as supporting evidence, not strict requirements.

## Rust Cues

- Transformation Style: iterator chains (`map`, `filter`, `fold`, `collect`) favored for pure transforms
- Error Explicitness: `Result<T, E>`, `thiserror`/typed errors, `?` with context where useful
- Mutation Budget: `let` over `let mut` unless clear need
- Concurrency Discipline: explicit ownership, channel/task boundaries, cancellation strategy
- Build/Tooling Contract: `cargo` tasks and lint/test conventions are explicit

## Go Cues

- Control Flow Shape: early returns for errors and guard conditions
- Error Explicitness: wrapped errors (`fmt.Errorf("...: %w", err)`) and sentinel/type checks where needed
- Module Cohesion: package purpose stays tight; avoid god packages
- Testability by Construction: interface seams where valuable, constructor injection
- Entry-Point Architecture: thin `cmd/*` with domain logic in internal packages

## Python Cues

- Contract Strictness: explicit boundary validation (dataclasses/pydantic/manual checks)
- Naming Density: domain-meaningful function/variable names over generic script-like naming
- Data/IO Isolation: keep side effects at edges, pure core logic where practical
- Build/Tooling Contract: explicit `pytest`/lint/format command paths and pinned tooling
- Evolution Posture: migration notes and compatibility handling in public APIs

## TypeScript Cues

- Contract Strictness: runtime validation for untrusted input; strong type boundaries
- Boundary Surface Area: narrow exported types/functions; avoid accidental barrel bloat
- Error Explicitness: typed error contracts or discriminated-union style failure paths
- Testability by Construction: dependency seams and side-effect isolation
- Config Strategy: centralized typed env/config module with startup validation
