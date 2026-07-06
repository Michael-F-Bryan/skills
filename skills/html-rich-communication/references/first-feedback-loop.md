# First-feedback loop

The first-feedback artefact exists to make the framing cheap to correct before visual polish makes it feel finished.

Use it for ambiguous, high-stakes, mixed-audience, design-review, executive, or source-heavy artefacts. Skip only for low-risk throwaways or when the user explicitly asks for final-only. Speed requests still need calibration when the reader's question, confidence, or document boundary is unclear.

Senior design review, unvalidated safety-relevant defaults, or open-loop control are first-feedback triggers even when the user asks for a same-day polished page.

## Shape

Use `templates/first-feedback.md` or a rough static HTML equivalent.

For sub-hour requests, use a compressed 5–10 minute first-feedback draft: BLUF, reader/action, confidence, top evidence, top uncertainty, proposed next move, and what is being cut. Do not skip calibration because the user asked for polish quickly.

Minimum sections:

1. BLUF / thesis.
2. Reader model.
3. Assumptions ledger: terms, setup, domain knowledge, validation state.
4. Anticipated hard questions.
5. Critique of the proposed outline.
6. Proposed section order.
7. Content disposition table.
8. Design-decision skeleton.
9. Metric provenance table for prominent numbers.
10. Reviewer prompts.

## Reviewer prompts

- What question did you expect this artefact to answer first?
- What section feels like it belongs in another document?
- What important non-goal/risk did you want earlier?
- Which heading did not tell you what you would get?
- Which number or claim felt stronger than the evidence supports?
- What would you ask in the review meeting after reading this?

## Calibration ledger

Capture feedback in `templates/feedback-ledger.md`:

| Feedback | Type | Action | Rationale |
|---|---|---|---|
| UI section useful but belongs in user guide | wrong-document | move/appendix | design-review reader needs architecture first |

Actions: fix, clarify, move, cut, append, link-out, reject-with-reason.
