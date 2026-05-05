---
name: code-like-michael
description: Apply Michael's coding fingerprint when planning, implementing, reviewing, refactoring, or shaping a repository. This style favors linear orchestration, explicit boundaries, typed contracts at hard edges, seam-driven abstraction, and drift-aware verification.
---

# Coding Fingerprint: Michael

Michael-style code optimizes for readability under change: top-level flow stays linear, key decisions are hoisted into explicit variants/types, and traversal mechanics are pushed downward into focused executors. Boundaries are typed and explicit, frameworks stay at hard edges, abstractions appear only under real seam pressure, and outcome semantics remain truthful so operations and failures are legible.

## Calibration Axes

- Local Pragmatism / Global Consistency: 4
- Duplication Tolerance / Abstraction Bias: 2
- Explicitness / Compression: 5
- Early Validation / Late Validation: 4
- Test-First Bias / Implementation-First Bias: 2
- Domain Purity / Framework Affinity: 2

## Core Behaviours

### Naming And Vocabulary

Use responsibility-shaped names that expose domain intent and boundary semantics. Prefer names like `StageResult`, `ClassifierActivity`, or `StoreDocument` over generic holders like `Manager`, `Processor`, or `Utils`.

Avoid vague mode strings and implicit lifecycle names. If a closed set exists, model it explicitly as enum/tagged variants.

### Function And Module Shape

Keep top-level orchestration linear and declarative:
- establish dependencies
- guard early
- call stage/executor functions in order
- return explicit result

Push mechanics downward: retries, batching, pagination, streaming, resume indexes, and loop bookkeeping belong in lower-level helpers/executors. Do not mix traversal mechanics with top-level business decisions.

Prefer early returns over deep nesting. Hoist major branching into explicit types/variants when that removes repeated `kind`/mode switching in orchestration.

Extraction triggers for splitting orchestration:
- repeated edits in the same orchestrator across unrelated concerns for 2+ PRs
- stage-branch growth where intent is no longer skimmable at a glance (for example, 4+ stage branches with inline mechanics)
- ownership spread where one orchestrator coordinates behavior owned by 3+ modules/teams
When these appear, split by stage/executor seams before adding new branches.

### Abstractions And Boundaries

Use explicit composition roots and manual parameter passing. Add interfaces/seams only where external variability or ownership demands them.

Abstraction threshold:
- tolerate first duplication
- inspect second repetition
- extract on third only if behavior is semantically identical

Do not add service/repository layering by default. Do not add wrappers that still require concrete-client reach-through.
If you define a wrapper seam, make it contract-complete for required operations; do not rely on `hasattr`/reflection/probing to access hidden concrete clients.

### Data Modelling

Use typed boundary models and domain types to keep invalid states out of the core. Avoid long-lived `dict[str, Any]` or stringly state-machine fields for known shapes.

Prefer type-directed dispatch over repeated `kind`/mode switching. If a branch is fundamental and recurring, represent it as variants/types.

Edge exception budget: dynamic shape handling is acceptable only at unavoidable protocol edges, must be localized, and must be followed by conversion into typed models before entering core orchestration.
Edge exceptions must carry an explicit promotion trigger (new consumer, recurring bug, or second conversion site) that forces promotion to a typed contract.

### Error Handling And Validation

Validate aggressively at integrity boundaries (config, IDs, request shape, auth, transport contracts). Keep transport/protocol error normalization at adapters.

Never swallow broad exceptions while returning success/completed status. Encode partial/degraded/failure outcomes explicitly when tolerance is required, and preserve truthful run status semantics.

### Tests And Verification

Prioritize behavior at real seams and regression risk over call choreography. Verify contract truth (status, errors, boundary payloads, generated/drift surfaces) rather than just invocation order.

Testing process preference is medium confidence from current corpus. Treat this as a practical guideline, not dogma: choose the lightest test that still proves boundary behavior and failure truth.

### Comments And Documentation

Keep comments for policy and boundary rationale, especially when handling edge exceptions or intentional compromises. Keep docs practical and decision-bearing; avoid narrative padding.

## Repo-Shaping Defaults

- preferred repo shape: modular monolith with explicit bounded modules and clear execution surfaces
- executable surfaces: one obvious composition root per app/CLI/worker/workflow surface
- when to split crates/packages/apps: split when execution mode, ownership, lifecycle, or operational boundaries diverge
- source-of-truth artefacts: typed contracts, schemas, generated interfaces, diagnostics surfaces
- default CI checks: build/test/lint plus regeneration or drift checks for contract artifacts
- documentation defaults: concise README plus boundary/architecture notes where decisions are durable

## Architectural Tendencies

- preferred layering: thin composition root, stage/domain modules, edge adapters
- dependency direction: edges depend inward; inner flow stays framework-light
- integration style: direct at hard boundaries, wrapped only when local semantics begin
- migration/refactor posture: small, reviewable steps with behavior changes separated from broad reshaping where possible

## Dependency And DI Posture

- dependency posture: explicit constructor/builder args with focused dependencies
- dependency red flags: deep dependency graphs, omnivore facades, and wrappers that leak concrete implementation
- preferred DI style: manual wiring at composition roots
- avoid: container-heavy DI and interface proliferation not tied to a real seam

## Contracts, Docs, And CI

- contracts treated as product surfaces: APIs, schemas, generated contracts, diagnostics/status surfaces
- docs posture: concise, practical, and tied to real boundaries or operations
- CI/CD posture: fast feedback first; include drift checks where regeneration is expected
- drift-check expectations: if humans can forget to regenerate or update contract surfaces, CI should fail loudly

## Signature Patterns

- Pattern: Linear orchestration with downward delegation of mechanics.
  Why it matters: Keeps review and operations centered on intent, not loop bookkeeping.
  Evidence: Solarbutt entrypoints are short/explicit; Lyric anti-sample marks mechanic-heavy mega-orchestrators as major drift.

- Pattern: Boundary-typed modeling with edge-local conversion.
  Why it matters: Prevents runtime repair logic from spreading through the core.
  Evidence: Solarbutt keeps protocol shaping in adapters; Lyric anti-sample flags `Union[Typed, dict]` coercion and stringly workflow states.

- Pattern: Seam-driven abstraction with explicit composition roots.
  Why it matters: Reduces fake layers while still isolating real IO/auth/runtime boundaries.
  Evidence: Narrow auth/client seams in solarbutt; anti-sample rejects god facades and concrete reach-through.

- Pattern: Truthful outcome semantics and explicit failure signaling.
  Why it matters: Operational correctness depends on status contracts matching reality.
  Evidence: Anti-sample classifies swallowed errors plus success status as critical drift.

## Avoidances

- avoids: orchestration that interleaves business decisions with retries, batching, pagination, or resume loops.
  because: it obscures intent and increases drift risk in high-churn execution paths.

- avoids: weak boundary contracts (`dict` unions, stringly state machines, ad-hoc reflection probes).
  because: they force hidden runtime patching and erode model guarantees.

- avoids: framework-shaped facades owning unrelated concerns.
  because: they collapse boundaries and create brittle change hotspots.

## Review Instincts

If a change feels wrong in this style, check for:

- top-level flow doing mechanics instead of intent
- repeated mode/kind switching that should be type- or variant-directed
- boundary validation or conversion happening too deep
- abstraction introduced before seam pressure exists
- wrapper seams leaking concrete client details
- status contracts that claim success while errors are suppressed
- tests proving mocked choreography rather than boundary behavior

## Pre-Flight Checklist

Before returning code in this fingerprint, ask:

- [ ] Is top-level flow linear with early returns and declarative stage calls?
- [ ] Did I hoist important branching into explicit variants/types where it clarifies intent?
- [ ] Are traversal mechanics delegated downward instead of mixed into orchestration?
- [ ] Are boundary contracts typed with conversion localized at edges?
- [ ] Are outcome semantics truthful for success/partial/failure paths?
- [ ] Did I avoid adding abstraction layers without proven seam pressure?
- [ ] Is framework and generated glue confined to hard edges?
- [ ] Do tests verify behavior and contract truth at real seams?
- [ ] Can contract/docs/generated outputs drift without a failing check?

## Anti-Patterns

If you see these, the output has drifted:

- top-level orchestration with nested branch + loop bookkeeping mixed with domain decisions
- repeated switching on free-form `kind`/mode strings in orchestration code
- `Union[TypedModel, dict]` and runtime coercion as standard internal API shape
- comment-enforced allowed values instead of enums/variants for closed states
- broad exception catch that logs and still returns success/completed
- broad facades owning unrelated responsibilities across boundary layers
- dependency wrappers that require concrete-client reach-through (`hasattr`, reflection probing)
- tests that rely on prints or weak shape checks without asserting contract outcomes
