---
name: risk-calibrated-agent-reviews
description: Use when deciding whether agent implementation or correction work warrants independent review.
---

# Risk-Calibrated Agent Reviews

Use this skill only to decide whether independent review is worth another judgement seat. `code-like-michael` owns testing and verification: the changed claim, consumer boundary, evidence choice, reuse, and stopping point.

## Core rule

**Review load-bearing boundaries; verify ordinary corrections; exercise presentation directly.**

Independent review is a risk control, not ceremony after implementation, every correction, or every push. It does not replace direct evidence at the acceptance boundary.

## Review when independent judgement can change the outcome

A fresh review is normally worthwhile when a defect could corrupt downstream work, operator truth, safety, recovery, or a public contract, especially for:

- safety-sensitive device or control behaviour;
- cancellation, interruption, retry, recovery, concurrency, or lifecycle semantics;
- runtime trust boundaries;
- protocol, parser, serializer, or generated-contract design relied on by separate consumers;
- cross-package or cross-layer ownership that later work will build upon; or
- a correction that materially expands or changes the original risk surface.

A generated artefact is not an automatic review trigger. Review it when the change establishes or alters a load-bearing contract; otherwise structural generation checks and a real consumer or render exercise are direct verification, not a reason to add a reviewer.

## Do not review by default

Prefer verification without an independent review for:

- a narrow bug with a focused regression and owning package or suite;
- a small local correction whose material claim is directly exercised;
- presentation, interaction, responsive layout, focus behaviour, or operator copy that can be exercised in the browser or real runtime;
- mechanical integration with an observable real-consumer result; or
- work already supported by valid evidence while the relevant tree, artefact, and environment remain unchanged.

Do not reserve a final review merely because several commits or workers existed. Use one only when their integration creates a new load-bearing interaction that direct evidence does not adequately constrain.

## Re-review only when the correction renews the risk

A correction warrants a fresh delta review when it materially changes the same load-bearing boundary, introduces another consequential abstraction or dependency, spans ownership layers, or becomes too large for the original review judgement to remain useful.

A focused correction does not need re-review merely because it followed review. Validate the finding, apply the correction, and use the proportionate evidence selected under `code-like-michael`.

## Brief the review to falsify the boundary

Bind a reviewer to exact base and head revisions. Name the consequential boundary and ask concrete counterexample questions rather than saying only “be adversarial”. Examples:

- Can cancellation be mistaken for authoritative device state?
- Does stream chunking alter terminal behaviour?
- Can a discriminator-valid payload omit evidence required by the consumer?
- Can successful completion erase a warning already shown to the operator?

Ask for Critical, Important, and Minor findings with a verdict. Critical and Important findings block acceptance until the coordinator verifies or rejects them.

## Treat findings as leads

Check factual premises against the authoritative source and reproduce actionable behaviour. Accept a demonstrated defect even if part of the reviewer’s causal story is wrong; reject the bad premise without losing the valid finding. Use `delegated-review-validation` when detailed citation and revision validation is needed.

A review result is not authority for a push, merge, deployment, hardware action, or acceptance claim.

## Route the seat proportionately

Use a capable mid-tier model for bounded delta review, a stronger general model for substantive protocol, trust-boundary, or multi-package review, and exceptional effort only for unresolved novel safety semantics or contradictory architecture evidence. Do not compare models by rerunning accepted work.

## Stop

Once material review concerns have been dispositioned and the changed claims have adequate direct evidence, stop. Repeated clean reviews, re-reviews, full-suite runs, and routine CI waits do not become useful through accumulation.

## Pitfalls

- Reviewing every change because a workflow diagram says so.
- Treating generated output, frontend work, or a final commit as automatic review triggers.
- Re-reviewing a focused correction without renewed boundary risk.
- Using source review where browser, device, runtime, or real-consumer evidence owns acceptance.
- Trusting a confident report without checking its premises.
- Measuring assurance by reviewer count or report length.

## References

Historical observations live under [evaluation calibration](../../evals/risk-calibrated-agent-reviews/calibration/), not the normal review path.
- `references/model-routing-by-semantic-phase.md` — model routing after a review is warranted.
- `references/subtractive-prose-revision-reviews.md` — exact-revision probes for consequential prose review.
- `references/destructive-git-cli-review.md` — safety probes for destructive Git tooling.
- `references/observability-review-validation.md` — validating tracing and logging findings.
- `references/technical-ui-copy-humanisation.md` — direct rendered inspection of technical UI copy.
