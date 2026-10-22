# SF-511 review calibration

Observed on one coordinated contract/backend/transport/state workflow. These are calibration data, not a controlled benchmark; task scope differed.

## Seats and outcomes

| Seat | Model / effort | Wall time | Cost | Review value |
| --- | --- | ---: | ---: | --- |
| Cross-layer backend implementation | Opus / high | 31m 18s | US$15.21 | Successful, but mixed two natural slices and over-invested in reconnaissance. |
| Backend adversarial review | Fable / xhigh | 12m 13s | US$10.45 | Found two Important defects and two Minors; findings valuable, model/effort excessive. |
| Backend scoped fix review | Sonnet / high | 2m 40s | US$1.04 | Confirmed accepted fixes with no blockers. |
| Frontend transport/parser implementation | Sonnet / high | 8m 46s | US$2.13 | Focused commit and 24 behavioural tests, but “validated” meant discriminator-check plus cast. |
| Transport/parser substantive review | Opus / high | 5m 36s | US$1.67 | Found one Important runtime trust-boundary defect plus three local Minors. High value. |
| Parser corrections | Sonnet / high | 9m 00s | US$3.21 | Correct, but an exhaustive prompt caused +452 production and +570 test lines. |
| Parser correction re-review | Sonnet / high | 4m 41s | US$1.18 | Justified because the correction added over 1,000 lines and mirrored an OpenAPI graph. |
| Pure operation reducer implementation | Sonnet / high | 5m 13s | US$1.51 | One 264-line module and 17 representative tests; complexity checkpoint worked. |
| Reducer substantive review | Opus / high | 5m 24s | US$1.75 | Found one Important warning-evidence loss path and four Minors. Reproduction valid; claim that backend did not exist was false. |
| Reducer corrections | Sonnet / high | 4m 19s | US$1.45 | Preserved warning union, completion evidence, and cancellation clarity; direct controller verification used instead of another review seat. |

## Durable lessons

### Initial reviews paid for themselves

The first independent review at each trust boundary found real Important defects:

- generated enum contract violation and lost terminal server evidence;
- runtime casts that did not establish the consumer's trusted payload shape;
- terminal state dropping warnings already shown to an operator.

These defects would have contaminated later UI work or operator evidence.

### Re-review value depended on correction shape

The parser correction was larger than the original parser and duplicated the authoritative schema structure. A scoped re-review was justified.

The reducer correction was local, had direct RED→GREEN coverage, and left a focused diff. Exact diff inspection, the owning tests, production build, lint, formatting, and clean status were proportionate; another independent review would have added little.

### Reviewer findings and reviewer narratives are separable

The reducer reviewer reproduced warning loss correctly but asserted that the backend did not exist. Source inspection showed:

- the backend existed;
- warnings were appended to cumulative `FlashResult.Warnings` before stream emission;
- terminal outcomes serialised that cumulative list;
- no-warning Go outcomes used `omitempty` rather than emitting an empty list.

The frontend defect still mattered because the public OpenAPI contract defined no warning-retraction semantics. The correct disposition was: accept the preservation defect, reject the backend premise, and write the fix from the public contract.

### Review prompts should falsify boundaries

High-yield probes included:

- a discriminator-valid outcome missing required evidence;
- `text/event-streaming` passing prefix matching;
- post-terminal behaviour changing across TCP chunks;
- cancellation being mistaken for authoritative terminal board state;
- `warnings: []` erasing observed warning evidence; and
- `last_completed_stage` being ignored.

Generic “be adversarial” language was less important than these concrete counterexamples.

### Prompt constraints can manufacture entropy

Demanding full nested validation while forbidding dependencies, generated validators, and schema engines left handwritten duplication as the only legal solution. Future prompts should define the minimum consumer guarantee and require a stop/options report if satisfying it starts duplicating an authoritative contract.

### Final cadence correction: evidence ownership still matters

The initial cadence decision correctly removed automatic UI code-review/re-review, but it used the phrase “direct scenario verification” without preserving the explicit coordinator-only role. The coordinator then authored a mock SSE server and Playwright harness, debugged it, and ran browser scenarios. No tracked product code changed, and the owned test servers were stopped, but Michael correctly rejected this as a role-boundary violation: substantive validation belonged to delegated Claude workers just as implementation did.

The corrected cadence is:

- one implementation writer;
- one fresh delegated browser verifier for package selection, modal persistence, cancellation, evidence, and ambiguous-target recovery;
- coordinator inspection of receipts, reports, exact Git state, and owned process cleanup only;
- focused corrections delegated to the sole writer, with validation delegated again only when the correction risk warrants it; and
- a final fresh-context review only when the integrated workflow introduces a new load-bearing interaction that direct evidence does not adequately constrain.

A review seat can be removed without transferring its work to the coordinator. “Use direct runtime evidence” means commission the appropriate verifier when the user's role contract is coordinator-only.

This preserves independent judgement at load-bearing boundaries without turning review artefact count into progress or silently changing who owns execution.