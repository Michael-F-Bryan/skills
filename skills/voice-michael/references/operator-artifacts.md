# Operator artefacts (Michael)

**Scope:** substantial decision briefs, technical reports, handoffs, architecture notes, incident reviews, and structured HTML artefacts. Short review comments, Jira updates, and Discord messages use natural sentences instead — load [team-communication.md](team-communication.md) for those. For visual styling of HTML artefacts, attach a brand/design-system skill (e.g. michael-brand-pack) and html-rich-communication for the build workflow.

## Framing

Operator-grade writing is direct, grounded, technically competent, and low-drama: an operator sharing working notes with enough clarity for executive scrutiny.

Core rule for decision-oriented artefacts:

> Make the work legible. Make the next move obvious.

For teaching explainers, soften the second half: legibility first; next move only when the reader's job is to decide or operate.

## Core rules

1. Lead with the read (decide) or thesis (learn).
2. Separate facts, judgement, assumptions, and uncertainty.
3. Be blunt about systems, not people.
4. Prefer specific nouns and active recommendations.
5. Use tables for trade-offs. (Blog prose prefers lists; this mode is the exception — see [public-writing.md](public-writing.md).)
6. Use diagrams for relationships.
7. Label uncertainty instead of hiding it.
8. Avoid cleverness that makes the reader decode the structure.

## Recommendation pattern

Use often on decide/operate artefacts:

```text
Recommendation: Keep the first version deliberately simple.
Why: The predictable failure mode is easier to explain and debug.
Trade-off: Users may need to retry manually during the prototype phase.
Next move: Add visible handoff state and document the expected failure mode.
```

## Known / Judgement / Uncertainty

Use when the distinction matters:

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

Good: "This is brittle." / "The current design hides the important state." / "I would not ship this as-is." / "This is a coordination problem, not a tooling problem."

Avoid: "This is terrible." / "Obviously bad." / "Whoever wrote this did not think it through." / "This is over-engineered nonsense."

Be direct about the system. Do not grandstand at people.

## Heading vocabulary

These labels are for substantial artefacts long enough to need navigation; in short communication they read as ceremony.

Prefer: Current read · Recommendation · What changed · Why it matters · Trade-off · Known constraints · Open questions · Next move · Decision required · Failure mode · Operational impact

Occasional punch is fine when it clarifies: "The risk is state, not syntax", "The happy path is not the system". Avoid cute headings that make the reader decode the structure.

## Tone by artefact type

| Context | Tone |
|---|---|
| Decision brief | concise, directive, trade-off aware |
| Technical report | analytical, structured, evidence-led |
| Incident review | factual, blameless, operationally clear |
| Architecture note | precise, option-aware, recommendation-first |
| Public write-up | polished, readable, lightly personal |
| CSU/mixed audience | plain English, explain acronyms, keep structure visible |
| Sunfish engineering | technical, pragmatic, implementation-aware |
| Mentoring explainer | thesis-first, patient, example-led |

## Progressive disclosure (content)

Use accordion or `<details>` only when the panel carries enough substance: 2–3 sentences of context, 3+ substantive bullets, or a bad/good code pair with brief explanation. If content fits a bullet list, keep it visible — do not hide a single sentence behind disclosure.

Each code example has one canonical section. Other sections link or deepen — do not repeat the same snippet in tabs, accordions, and compare blocks.
