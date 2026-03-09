---
name: code-like-michael
description: Write, refactor, or review code in Michael's style. Use when the user wants code to feel like Michael wrote it, wants to match Michael's coding fingerprint, or asks for boundary-first, explicit, pragmatically typed code with late abstraction, conditional validation, and seam-focused tests.
---

# Code Like Michael

Use this skill when writing new code, refactoring existing code, or reviewing changes that should feel like Michael wrote them.

## Core Stance

Optimise for explicit flow, domain-owned names, narrow boundary seams, and strong seam verification.

Do not optimise for:
- abstract symmetry
- framework purity
- mock-friendly indirection
- deduplicating two paths that are only superficially similar

## Quick Start

Before writing code:

1. Identify the boundary type.
2. Keep the main flow visible in one composition root.
3. Validate at the right edge for that boundary.
4. Add wrappers only where local semantics begin.
5. Keep semantically different paths separate.
6. Test the real seam, fixture, or generated surface.

## Boundary Rule

Apply this split deliberately:

- Fail early at integrity boundaries: config, auth, IDs, request shape, transport status, schema input.
- Continue with structure when downstream diagnostics are the product: parsers, analysis pipelines, compilers, validation/reporting flows.

Do not turn this into "always fail fast" or "always continue".

## Module Shape

Prefer:
- a thin `main`, `run`, `serve`, command, or router setup function
- explicit phase or boundary modules
- medium-sized orchestration that keeps execution order obvious
- smaller helpers for detailed rules

Avoid:
- deep indirection to recover the happy path
- broad `service`, `repository`, `manager`, or `utils` layers without a strong semantic reason
- shared helpers that erase policy differences between two flows

## Abstraction Threshold

Abstract only when one of these is true:

- the repeated shape is semantically identical
- the repeated code is mechanical and can be generated
- the concern is globally cross-cutting
- a third-party boundary would otherwise leak awkward semantics inward

Otherwise, keep the duplication local and explicit.

## Data And Errors

Prefer:
- explicit structs, enums, and named boundary types
- stable, lowercase error strings
- error wrapping at meaningful IO, parsing, or protocol boundaries
- assertions only for invariants, impossible states, or stale generated artefacts

Avoid:
- raw maps and flag soups in the core
- framework or protocol types leaking inward after local semantics begin
- reflection-heavy conversion that hides policy decisions

## Testing Rule

Prefer tests that prove the seam that can actually break:

- request-path tests
- fixture tests
- parser or snapshot tests
- DB/container/integration tests
- drift checks for generated code, docs, diagnostics, or schemas

Do not invent extra seams just to make mocking easier.

## Review Triggers

Something is probably off-style if:

- the main flow is hard to recover without tracing multiple abstractions
- validation is buried deep in domain logic
- a generic helper was extracted before the shared shape was stable
- framework purity caused a worse API than direct boundary use
- tests mostly assert mocked internals rather than observable behaviour
- generated or documented output can drift silently

## Delivery Checklist

Before returning code, check:

- [ ] Is the execution order obvious from one composition root?
- [ ] Are names domain-owned and specific?
- [ ] Is validation happening at the correct edge for this boundary?
- [ ] If bad input is tolerated, is that because better diagnostics are the product?
- [ ] Did I keep semantically different paths separate?
- [ ] Did I wrap only the boundaries that needed local semantics?
- [ ] Do the tests exercise a real seam or drift surface?

## Additional Resources

- For concrete "write this instead of that" examples, read [references/write-this-not-that.md](references/write-this-not-that.md)
- For the boundary and abstraction playbook, read [references/boundary-playbook.md](references/boundary-playbook.md)
