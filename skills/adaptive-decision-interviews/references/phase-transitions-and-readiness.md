# Phase transitions and readiness

Use this reference for pause, resume, completion, pivots, readiness, and hand-off to a downstream artefact.

## State invariants

| State | Invariant |
| --- | --- |
| **Active** | A named phase is authorised; unresolved human judgement remains; exactly one next question is selected. |
| **Paused** | The user has stopped questioning; no pending question exists; unresolved and deferred decisions remain visible; no question is asked until explicit resume. |
| **Complete enough for <artefact>** | The named artefact can be produced without another interview question. Other decisions may remain open or deferred. |
| **Complete** | The authorised phase is closed; its projection and evidence references are current; no pending question exists; no unresolved human judgement remains inside that phase; deferred items have an owner, trigger, or evidence gate. |

Update status before every pivot into reflection, review, readiness, drafting, or another phase. A pivot is not evidence that unresolved judgement has been decided.

## Pause, resume, and amendments

On pause, record any answer in that message first, append the pause direction verbatim with timestamp, mark the current phase `Paused`, remove the pending-question marker, and preserve open/deferred decisions. Do not select a next question.

On explicit resume, record the new authorisation, mark the phase `Active`, recompute the frontier from the current projection, then select one question. Do not resume from a stale pending question.

If a reply both amends an earlier answer and answers the current question, record two atomic items: a timestamped amendment attached to the earlier item, then the current answer under its own number. Preserve the original; update the projection and registers to cite the amendment.

If the decision horizon or level changes, record the correction, close or defer the abandoned line, update the contract and status, and continue only at the corrected frontier. If a completed interview continues into architecture, implementation, operations, or another decision class, preserve the prior phase as `Complete`, record new authorisation as a distinct phase, and mark the overall record `Active` again. A new phase authorises only the named output.

## Readiness

When asked whether work can start, distinguish:

- **Decision sufficiency:** the outcome, first useful behaviour, trust-breaking failures, scope, ownership/authority, evidence boundary, success gate, and exclusions are clear enough for the named artefact.
- **Implementation discovery:** exact libraries, schemas, providers, benchmarks, and operational details can be resolved later unless they could redirect the outcome, trust model, authority boundary, architecture boundary, or acceptance criterion.

Report `Complete enough for <artefact>` only when another interview answer is not decision-useful for that artefact. A readiness synthesis is not permission to draft a different artefact or write code.

## Two different outputs

A **publishable interview record** keeps a concise reader path to the decision horizon, current projection, scope/authority boundaries, unresolved items, chronology, verbatim answers, and source trail. It remains an account of how judgement was elicited.

A **decision artefact informed by the interview** is authored for its reader and purpose. It uses the current projection and evidence references, preserving uncertainty and deferred decisions, but does not use interview chronology as its narrative spine. It requires separate authorisation and a separate phase boundary.
