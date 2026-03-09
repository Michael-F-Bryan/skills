# Coding Fingerprint Template

Use this template for the final generated skill.

```markdown
---
name: coding-fingerprint-[name]
description: Apply [Name]'s coding fingerprint when planning, implementing, reviewing, or refactoring code. This style favours [brief summary of principles and coding behaviour].
---

# Coding Fingerprint: [Name]

[One paragraph summary of the coding fingerprint. Focus on recognisable engineering choices, not biography.]

## Calibration Axes

- Local Pragmatism / Global Consistency: [1-5]
- Duplication Tolerance / Abstraction Bias: [1-5]
- Explicitness / Compression: [1-5]
- Early Validation / Late Validation: [1-5]
- Test-First Bias / Implementation-First Bias: [1-5]
- Domain Purity / Framework Affinity: [1-5]

## Core Behaviours

### Naming And Vocabulary
[How domain concepts are named, how precise the language is, and what gets avoided.]

### Function And Module Shape
[How code is split, typical function size, whether orchestration and logic are separated.]

### Abstractions And Boundaries
[What gets abstracted, what stays concrete, how seams are chosen.]

### Data Modelling
[How invalid states are handled, preferred data structures, boundary types.]

### Error Handling And Validation
[Where validation happens, how errors are wrapped, how failure is surfaced.]

### Tests And Verification
[Test style, preferred seams, what gets tested first, what is considered enough coverage.]

### Comments And Documentation
[When comments appear, what they explain, what is left implicit.]

## Architectural Tendencies

- preferred layering:
- dependency direction:
- integration style:
- migration/refactor posture:

## Signature Patterns

- Pattern:
  Why it matters:
  Evidence:

- Pattern:
  Why it matters:
  Evidence:

## Avoidances

- avoids:
  because:

- avoids:
  because:

## Review Instincts

If a change feels wrong in this style, check for:

- boundary validation in the wrong place
- abstraction introduced before duplication proves the need
- vague or non-domain naming
- tests that assert internals instead of behaviour
- framework concerns leaking into domain logic

## Pre-Flight Checklist

Before returning code in this fingerprint, ask:

- [ ] Are names domain-owned and specific?
- [ ] Are boundaries placed where this person usually places them?
- [ ] Is validation happening at the expected edge?
- [ ] Did I choose the same level of abstraction they usually choose?
- [ ] Do the tests express behaviour the way they would?
- [ ] Did I avoid patterns this fingerprint rejects?

## Anti-Patterns

If you see these, the output has drifted:

- [list 5-10 concrete violations of the fingerprint]
```

## Template Notes

- Keep the summary behavioural, not flattering
- Every section should help another agent make a code choice
- Anti-patterns should be specific enough to reject plausible bad output
- If a section cannot be grounded in evidence, omit or weaken it rather than bluffing
