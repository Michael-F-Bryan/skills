# Example Coding Fingerprint

This is what a finished coding fingerprint can look like after running the wizard.

```markdown
---
name: coding-fingerprint-boundary-first-pragmatist
description: Apply a boundary-first, explicit coding fingerprint when planning, implementing, reviewing, or refactoring code. This style favours domain-owned names, early validation, narrow interfaces, behaviour-first tests, and incremental refactors over speculative abstraction.
---

# Coding Fingerprint: Boundary-First Pragmatist

This coding fingerprint is pragmatic, explicit, and boundary-aware. It pushes validation to the edges, keeps core logic small and readable, and prefers domain-owned names over generic helpers. Abstractions are introduced reluctantly, usually after duplication reveals a stable seam. Tests focus on observable behaviour through realistic inputs rather than mocked internals. The overall effect is code that feels deliberate, reviewable, and hard to misunderstand.

## Calibration Axes

- Local Pragmatism / Global Consistency: 4
- Duplication Tolerance / Abstraction Bias: 2
- Explicitness / Compression: 5
- Early Validation / Late Validation: 5
- Test-First Bias / Implementation-First Bias: 4
- Domain Purity / Framework Affinity: 4

## Core Behaviours

### Naming And Vocabulary

Names are concrete and domain-owned. Generic names like `utils`, `data`, or `manager` are avoided unless the domain genuinely uses them. Function names usually describe intent and side effects plainly.

### Function And Module Shape

Functions are narrow and usually do one visible thing. Orchestration sits near the edge, while business rules are pulled into smaller helpers or domain modules. Modules are split by ownership and responsibility rather than by technical layer alone.

### Abstractions And Boundaries

Abstractions appear late. The default move is to keep code concrete until two or three call sites prove the seam. Boundary code is allowed to be imperative; the core is kept predictable and testable.

### Data Modelling

Invalid states are pushed out of the happy path. Input is parsed and validated into narrower types early. Primitive obsession is tolerated briefly at edges but not in the core domain.

### Error Handling And Validation

Validation happens at boundaries. Errors are wrapped with useful context at system transitions. Error strings are stable and matter-of-fact rather than chatty. Panics or assertions are reserved for invariants, not user input.

### Tests And Verification

Tests aim at behaviour, not implementation detail. Preferred seams are real inputs with fakes or spies instead of mock-heavy unit tests. A good first test demonstrates the intended external behaviour and fails for the right reason.

### Comments And Documentation

Comments are sparse. They explain a non-obvious constraint, trade-off, or invariant, not line-by-line mechanics. Structure and names should carry most of the load.

## Architectural Tendencies

- preferred layering: functional core with imperative shell
- dependency direction: infrastructure depends on domain, not the reverse
- integration style: thin adapters around external systems
- migration/refactor posture: incremental, reversible steps with proof after each step

## Signature Patterns

- Pattern: Validate and normalise inputs at the edge before invoking core logic
  Why it matters: Keeps invalid state and transport concerns out of domain code
  Evidence: Repeated boundary parsing, typed constructors, and smaller core functions

- Pattern: Duplicate once before extracting a shared abstraction
  Why it matters: Optimises for clarity and correct seams rather than premature reuse
  Evidence: Similar flows stay separate until the common shape is proven

- Pattern: Test through public behaviour with controlled collaborators
  Why it matters: Preserves refactor freedom and checks what users of the code actually observe
  Evidence: Tests assert outputs, state transitions, or emitted diagnostics rather than private calls

## Avoidances

- avoids: broad helper modules
  because: they blur ownership and become gravity wells for unrelated logic

- avoids: opaque abstractions introduced for elegance alone
  because: they hide the real workflow and make debugging harder

- avoids: comments that restate the code
  because: they signal naming or structure problems rather than solving them

## Review Instincts

If a change feels wrong in this style, check for:

- validation buried deep in business logic
- a new abstraction with only one weak caller
- names that describe mechanism instead of domain meaning
- tests coupled to private helpers or call counts
- retries or logging added without a clear boundary reason

## Pre-Flight Checklist

Before returning code in this fingerprint, ask:

- [ ] Are the names precise and domain-owned?
- [ ] Did I validate input at the boundary instead of deeper in the flow?
- [ ] Did I keep the core logic smaller and cleaner than the outer orchestration?
- [ ] Did I avoid extracting an abstraction before the seam was obvious?
- [ ] Do the tests verify behaviour through realistic inputs?
- [ ] Did I avoid generic helper gravity wells?

## Anti-Patterns

If you see these, the output has drifted:

1. A new `utils` module appears without strong domain ownership
2. Validation is mixed throughout the core path instead of concentrated at boundaries
3. Tests assert on internal call order when public behaviour would do
4. Framework types leak into domain-facing interfaces
5. A generic abstraction replaces two slightly different flows too early
6. Comments narrate obvious code instead of clarifying constraints
7. Error messages are vague, title-cased, or inconsistent
8. Refactors combine behavioural change and structural cleanup without separation
```

## Why This Example Works

- It encodes choices an agent can act on
- It separates durable traits from style-guide fluff
- The anti-patterns are concrete enough to reject bad output
- The checklist is short enough to use during actual coding
