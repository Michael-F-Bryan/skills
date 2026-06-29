# Audience Patterns

Use this file when the artefact's audience changes the structure, level of detail, or interaction model.

## Routing table

| Audience | Primary job | Surface | Detail | Good elements | Avoid |
|---|---|---|---|---|---|
| C-suite / board | Decide quickly | Recommendation-first decision memo | Collapsed | Hero recommendation, KPI cards, risk/impact, decision options, appendices in `<details>` | Row-level data, implementation diagrams, unresolved jargon |
| Data scientist / analyst | Investigate and validate | Analytical report/notebook hybrid | Exposed/filterable | Provenance, assumptions, distributions, small multiples, filters, uncertainty, source links | KPI theatre, hidden transformations, decorative charts |
| Engineer / technical reviewer | Verify structure and risk | Architecture/review explainer | Path-anchored | Module map, call flow, state machine, annotated diffs, contracts, test matrix | Marketing framing, vague boxes, unverified claims |
| Founder / PM / strategy reader | Choose investment path | Decision-support brief | Evidence gates | Problem/wedge/options, staged path, kill/pivot signals, cheap-vs-expensive grid | Customer-sales CTA when reader is investor/founder, implementation trivia |
| Operator / responder | Act now | Field card/runbook/status console | Minimal | Status banner, checklist, escalation, event timeline, do/do-not panels | Long narrative, subtle cues, hover-only information |
| Public / non-expert | Understand and act | Guided explainer | Plain-language layers | One main message, annotated simple chart, glossary chips, FAQ, captions/alt text | Acronyms, unexplained scales, technical caveats first |
| Designer / creative stakeholder | Compare directions | Gallery/moodboard/options | Rationale per option | Small multiples, palette/type tokens, image prompt slots, what-to-react-to prompts | One final design too early, buried rationale |

## Audience lock questions

Ask or infer these before writing:

1. What decision/action is the reader being asked to take?
2. What do they already know, and what jargon will lose them?
3. What detail do they need visible by default?
4. What evidence would make them trust the artefact?
5. What would make the artefact feel like it was written for the wrong person?
6. Will they read on mobile, in a meeting, at a desk, or in the field?

## Mixed audiences

Do not flatten mixed audiences into an average reader. Pick a primary reader and use progressive disclosure or separated sections for secondary readers.

Useful pattern:

```text
Executive surface: recommendation, decision, risks, next action.
Technical layer: collapsed evidence, methods, source paths, implementation notes.
Appendix: raw detail, definitions, provenance.
```
