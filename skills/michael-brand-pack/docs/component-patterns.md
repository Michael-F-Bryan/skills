# Component Patterns

Reusable components are the core of the Operator Notes system. They make artefacts recognisable through structure and judgement rather than decoration.

## Status strip

Use near the top of serious artefacts.

Fields:

- Status
- Owner
- Updated
- Confidence
- Scope

Example:

```text
Status: Recommended
Owner: Michael F. Bryan
Updated: 5 July 2026
Confidence: Medium
Scope: Sunfish / internal technical planning
```

## Current read

Purpose: give the reader the interpretation immediately.

Use when the artefact needs judgement, not just information.

Example:

```text
The system is conceptually sound, but the implementation hides important state. That is acceptable for the prototype. It becomes risky once multiple people need to debug it.
```

## Recommendation

Purpose: make the desired action explicit.

Pattern:

```text
Recommendation: Do X.
Why: Y.
Trade-off: Z.
Next move: A.
```

## Decision block

Purpose: record an accepted or proposed decision.

Include:

- decision
- rationale
- trade-offs accepted
- follow-up actions

## Evidence block

Purpose: distinguish observed facts from interpretation.

Use for:

- measurements
- logs
- dates
- user feedback
- system behaviour
- examples

## Trade-off table

Purpose: compare options without rambling.

Recommended columns:

| Option | Upside | Downside | Read |
|---|---|---|---|
| Simple | Easy to debug | Manual recovery | Best first version |
| Smart | Smoother UX | Hidden complexity | Later |

## Risk block

Purpose: make operational risk visible.

Fields:

- risk
- impact
- likelihood
- severity
- mitigation

Severity labels:

- Low
- Medium
- High
- Blocker

## Assumption block

Purpose: show what the conclusion rests on.

Example:

```text
Assumption: Users will tolerate manual retry during the prototype phase as long as the failure is clear and recoverable.
```

## Open questions

Purpose: show unresolved items without blocking the whole artefact.

Use when:

- the recommendation is provisional
- external input is required
- evidence is missing
- implementation details remain unclear

## Next actions / next move

Purpose: convert understanding into movement.

Good actions are concrete:

- “Add visible handoff state.”
- “Log the state transition that matters.”
- “Document the expected failure mode.”

Weak actions:

- “Improve robustness.”
- “Investigate options.”
- “Align stakeholders.”

## Appendix

Purpose: hold detail without burying the main read.

Use for:

- raw notes
- references
- code snippets
- extended tables
- discarded options
- detailed evidence
