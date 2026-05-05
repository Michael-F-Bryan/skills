# Code Style Dimensions v1 (File-Level Labels, Multi-Scale Coverage)

This framework is designed for **file-level labeling with repo rollups** while preserving signals from:

- **Micro scale**: expression-level and function-level coding choices
- **Meso scale**: module and package boundaries
- **Macro scale**: repository architecture and operational shape

## Recommended Structure

Use a **three-band taxonomy** with 20 total dimensions:

- **Band A (Micro, 8 dims)**: local code construction style
- **Band B (Meso, 6 dims)**: module/package boundary style
- **Band C (Macro, 6 dims)**: repository and operational architecture style

This avoids overfitting to only function internals while keeping file-level annotation practical.

## Alternative Structures Considered

1. **All dimensions at one flat level**
   - Pros: simpler first pass
   - Cons: tends to over-represent micro signals because files expose those most directly

2. **Hierarchical dimensions with hard dependencies**
   - Pros: mirrors architecture decomposition
   - Cons: harder to label consistently and can collapse orthogonality

3. **Three-band independent dimensions (recommended)**
   - Pros: explicit multi-scale coverage, easier to keep orthogonal, supports file-level labeling with robust rollups
   - Cons: requires a little more guidance for macro inference from files

## Scoring Model

Per file, score each dimension on a **1-5 anchored ordinal scale**:

- `1`: strongly opposite preference
- `2`: weak opposite preference
- `3`: neutral/mixed/insufficient evidence
- `4`: weakly aligned preference
- `5`: strongly aligned preference

Also track:

- `confidence` (`low`, `medium`, `high`)
- `evidence` (short snippets, symbol names, config entries, folder conventions)

Rollups:

- File -> package/module: weighted mean by file complexity (e.g., LOC or function count)
- Package/module -> repo: weighted mean with architecture files (e.g., CLI entrypoints, config, build files) given explicit macro weight

---

## The 20 Orthogonal Dimensions

Each dimension has: **what it measures**, **high-end signal**, and **why orthogonal**.

### Band A — Micro (Inside Functions and Types)

1. **Transformation Style**
   - Measures: preference for declarative transformation pipelines vs imperative mutation loops.
   - High signal: iterator chains/combinators for map/filter/reduce-like work.
   - Orthogonal to abstraction depth: you can be declarative in either flat or layered code.

2. **Control Flow Shape**
   - Measures: straight-line early-return flow vs deep nesting/branch pyramids.
   - High signal: guard clauses and short-circuit exits.
   - Orthogonal to error policy: both strict and loose error styles can use early returns.

3. **Mutation Budget**
   - Measures: tolerance for mutable state and reassignment in local scopes.
   - High signal: immutable-by-default locals, narrow mutable windows.
   - Orthogonal to performance posture: low mutation can still be performance-focused.

4. **Error Semantics Explicitness**
   - Measures: explicit typed/contextual error propagation vs opaque/generalized handling.
   - High signal: context-rich errors, typed/result-driven handling.
   - Orthogonal to control flow shape: explicit errors can coexist with varied branching style.

5. **Contract Strictness at Boundaries**
   - Measures: level of input/output validation and invariant checking.
   - High signal: explicit preconditions/postconditions and edge-case handling.
   - Orthogonal to naming style: strict contracts are independent of naming preferences.

6. **Naming Semantics Density**
   - Measures: degree to which identifiers encode intent and domain meaning.
   - High signal: precise, role-bearing names over short generic labels.
   - Orthogonal to documentation style: good names can exist with sparse comments.

7. **Local Abstraction Threshold**
   - Measures: tendency to extract helpers early vs keep logic inline until pressure appears.
   - High signal: consistent extraction policy based on complexity/reuse signals.
   - Orthogonal to module boundaries: local extraction is intra-file behavior.

8. **Commenting Philosophy**
   - Measures: explanatory strategy (why-focused comments vs mostly self-documenting code).
   - High signal: comments for intent/constraints, not narrating obvious mechanics.
   - Orthogonal to naming density: both can be high or low independently.

### Band B — Meso (Modules, Packages, Internal APIs)

9. **Module Cohesion**
   - Measures: whether files group around one responsibility vs mixed concerns.
   - High signal: focused modules with clear thematic purpose.
   - Orthogonal to public API width: cohesive modules can expose narrow or wide APIs.

10. **Dependency Directionality Discipline**
   - Measures: consistency of dependency flow (e.g., domain inward, adapters outward).
   - High signal: clear one-way dependency gradients, minimal cycles.
   - Orthogonal to repo topology: directionality can be enforced in many layouts.

11. **Boundary Surface Area**
   - Measures: preference for narrow interfaces/contracts vs broad direct coupling.
   - High signal: minimal exported surface, intentional API seams.
   - Orthogonal to cohesion: cohesive modules may still overexpose symbols.

12. **Cross-Cutting Concern Placement**
   - Measures: where logging/metrics/auth/retries live (infrastructure edge vs scattered inline).
   - High signal: consistent placement policy with limited leakage into pure domain code.
   - Orthogonal to error semantics: explicit errors can coexist with either placement style.

13. **Testability by Construction**
   - Measures: ease of isolating modules via injected dependencies and deterministic contracts.
   - High signal: seams that support fast unit-level and integration-level tests.
   - Orthogonal to test quantity: this measures design-for-test, not number of tests.

14. **Concurrency Model Discipline**
   - Measures: consistency in concurrency primitives and ownership/cancellation patterns.
   - High signal: explicit concurrency boundaries and predictable synchronization style.
   - Orthogonal to performance posture: disciplined concurrency may or may not be aggressive.

### Band C — Macro (Repository, Entry Points, Operations)

15. **Entry-Point Architecture**
   - Measures: how execution is organized through CLI/services/workers.
   - High signal: explicit command/subcommand shells that delegate to domain modules.
   - Orthogonal to folder topology: similar entry strategy can use different directories.

16. **Repository Topology Style**
   - Measures: structural organization pattern (modular monolith, service-split, package-centric).
   - High signal: repeatable, principle-driven folder/package conventions.
   - Orthogonal to dependency directionality: topology and dependency rules are distinct axes.

17. **Configuration and Environment Strategy**
   - Measures: typed explicit config handling vs ad-hoc environment reads.
   - High signal: centralized config schema, validated startup, explicit defaults.
   - Orthogonal to entry-point architecture: any entry model can have good or poor config discipline.

18. **Data Boundary and IO Isolation**
   - Measures: separation between pure domain logic and external IO/persistence/integration code.
   - High signal: adapter layers and minimal leakage of transport/storage details.
   - Orthogonal to module cohesion: cohesive modules can still mix IO and domain inadvertently.

19. **Build/Tooling Contract**
   - Measures: reproducibility and explicitness of build/test/lint/dev workflows.
   - High signal: deterministic commands, pinned tooling policy, clear task entrypoints.
   - Orthogonal to code style inside files: operational discipline is separate from syntax choices.

20. **Evolution Posture**
   - Measures: bias toward stable long-lived contracts vs rapid internal churn tolerance.
   - High signal: migration discipline, deprecation strategy, compatibility intent.
   - Orthogonal to abstraction threshold: either stable or fast-changing systems can be abstract or concrete.

---

## How This Captures Your Example Span

- Micro example ("prefer iterator chains over for-loops in Rust transformations") maps strongly to **Dimension 1 (Transformation Style)** and secondarily **Dimension 3 (Mutation Budget)**.
- Macro example ("modular monolith exposed through CLI subcommands delegating to domain modules/internal packages") maps strongly to **Dimensions 15, 16, 10, and 11**.

The design intentionally preserves both without forcing one to dominate.
