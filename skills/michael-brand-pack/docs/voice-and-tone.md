# Voice and Tone

Operator Notes writing should be direct, grounded, technically competent, and low-drama.

The voice should feel like an operator sharing working notes with enough clarity for executive scrutiny.

## Core voice rules

1. Lead with the read.
2. Separate facts, judgement, assumptions, and uncertainty.
3. Be blunt about systems, not people.
4. Prefer specific nouns and active recommendations.
5. Use tables for trade-offs.
6. Use diagrams for relationships.
7. Label uncertainty instead of hiding it.
8. Avoid cleverness that makes the reader decode the structure.

## Lead with the read

Good:

> The design is conceptually sound, but it hides important state. That is acceptable for the prototype. It becomes risky once multiple people need to debug it.

Weak:

> There are a few different considerations here, and some of them may become important later depending on how the system evolves.

## Recommendation pattern

Use this pattern often:

```text
Recommendation: Do X.
Why: Y.
Trade-off: Z.
Next move: A.
```

Example:

```text
Recommendation: Keep the first version deliberately simple.
Why: The predictable failure mode is easier to explain and debug.
Trade-off: Users may need to retry manually during the prototype phase.
Next move: Add visible handoff state and document the expected failure mode.
```

## Fact / judgement / uncertainty split

Use this when the distinction matters.

```text
Known:
- The current workflow handles the happy path.
- Failures require manual inspection.

Judgement:
- This is acceptable for the prototype.
- It is not acceptable once multiple users depend on it.

Uncertainty:
- We do not yet know the actual failure frequency under production load.
```

## Bluntness calibration

Good:

- “This is brittle.”
- “The current design hides the important state.”
- “This abstraction is probably too clever for the current maturity of the system.”
- “I would not ship this as-is.”
- “This is a coordination problem, not a tooling problem.”

Avoid:

- “This is terrible.”
- “Obviously bad.”
- “Whoever wrote this did not think it through.”
- “This is over-engineered nonsense.”

Be direct about the system. Do not grandstand at people.

## Heading style

Prefer useful headings:

- Current read
- Recommendation
- What changed
- Why it matters
- Trade-off
- Known constraints
- Open questions
- Next move
- Decision required
- Failure mode
- Operational impact

Occasional punch is fine when it clarifies:

- The risk is state, not syntax
- This is a coordination problem
- The happy path is not the system

Avoid cute headings that make the reader decode the structure.

## Tone by context

| Context | Tone |
|---|---|
| Decision brief | concise, directive, trade-off aware |
| Technical report | analytical, structured, evidence-led |
| Incident review | factual, blameless, operationally clear |
| Architecture note | precise, option-aware, recommendation-first |
| Public write-up | polished, readable, lightly personal |
| CSU/mixed audience | plain English, explain acronyms, keep structure visible |
| Sunfish engineering | technical, pragmatic, implementation-aware |

## Words to prefer

- recommendation
- decision
- trade-off
- risk
- assumption
- constraint
- evidence
- failure mode
- next move
- current read
- operational impact
- known / unknown

## Words to avoid or use carefully

- leverage
- unlock
- alignment
- enablement
- synergy
- transformative
- seamless
- cutting-edge
- revolutionary
- paradigm
- robust, unless explained
- scalable, unless scoped
- production-ready, unless tested

## Sentence shape

Prefer compact sentences with clear subjects.

Good:

> The handoff works, but only when every step succeeds. The failure state is not visible to the user.

Weak:

> In cases where the handoff process does not complete as expected, it may be difficult for users to determine what has occurred.

## Uncertainty language

Use:

- “Likely” when based on evidence but not confirmed.
- “Assumption” when the argument depends on something unverified.
- “Open question” when a decision needs more information.
- “Confidence: High/Medium/Low” sparingly, with an explanation.

Example:

```text
Confidence: Medium — the architecture is clear, but production traffic assumptions are still untested.
```
