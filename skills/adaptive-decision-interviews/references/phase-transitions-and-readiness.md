# Phase transitions and readiness

Use these patterns when an interview is corrected, paused, resumed, or deliberately continued into another decision phase.

## Continue into a new phase

When the user continues a completed interview into architecture, implementation, operations, or another decision class:

1. Preserve the earlier phase’s completion state, timestamp, purpose, and verbatim record.
2. Record the user’s new authorisation as a distinct phase; do not silently broaden the old boundary.
3. Mark the overall interview active again while keeping the earlier phase complete.
4. Continue question numbering and cumulative registers unless the user requests a separate record.
5. State what the new phase may produce and what remains unauthorised.

A new implementation phase may authorise architecture decisions without authorising a specification, implementation plan, or code.

Treat superseded designs and old implementations as evidence about the problem, prior choices, and failure modes—not as approved direction.

## Pause and resume

When the user pauses an active interview:

1. Record any answer in the same message before changing state.
2. Append the pause direction verbatim with its timestamp.
3. Mark the current phase **Paused**, not complete.
4. Remove the pending-question marker so the record does not imply that questioning is continuing.
5. Preserve unresolved and deferred decisions.
6. Do not select or ask another question until the user explicitly resumes.

On resume, record the new authorisation, mark the phase active, recalculate the decision frontier from the current registers, and only then choose the next question.

## Amendments that also answer the current question

One reply may both correct an earlier answer and answer the pending question. Record two atomic items:

1. a timestamped amendment attached to the earlier question, preserving the original answer; and
2. the current answer under its own question number.

Update the calibrated direction and affected registers to cite the amendment. Do not merge both acts into one paraphrase or rewrite the earlier record.

## Assess whether there is enough direction to start

When the user pauses and asks whether implementation can begin, assess two different thresholds:

- **Product or decision sufficiency:** the outcome, first useful behaviour, trust-breaking failures, evidence and authority boundaries, success gate, and explicit exclusions are clear enough to authorise a first vertical slice.
- **Implementation discovery:** exact libraries, schemas, provider details, benchmark results, and operational limits may still be resolved through planning, spikes, and implementation.

Answer “enough to start” plainly. Say no only when unresolved human judgement could materially redirect the outcome, trust model, authority boundary, architecture boundary, or acceptance criterion. Do not call ordinary implementation discovery a decision blocker.

A readiness answer is still a synthesis, not permission to draft a specification, plan, or code.

## Reader-facing interview records

If the user authorises a publishable record, make the first reading path concise while retaining auditability:

1. background and decision horizon;
2. what the interview established;
3. scope, allocation, and unresolved boundaries;
4. chronological questions and verbatim answers, with interpretation visibly separate;
5. cumulative registers; and
6. source trail.

Do not let the readable synthesis replace or drift from the verbatim record.