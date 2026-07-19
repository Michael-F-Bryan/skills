---
name: adaptive-decision-interviews
description: Use when the user wants the agent to conduct a structured interview that elicits and preserves their judgement before a decision artefact is drafted. Do not use for ordinary chat, job-interview practice, brainstorming, advice, one-off clarification, fact gathering, or execution after direction is already clear.
---

# Adaptive Decision Interviews

## Core principle

The human directs the decision. The agent reduces the effort required to express judgement, preserves the reasoning trail, and asks only questions whose answers could change the authorised artefact.

Research may inform the choices offered. It does not authorise the agent to settle the decision.

## When to use this skill

Use this skill when at least one of these is true:

- the user explicitly asks for an interview;
- the user asks to be questioned iteratively before a decision artefact, proposal, experiment, brief, or recommendation is drafted;
- an approved workflow requires a structured, durable record of human judgement.

Do **not** use it for:

- ordinary conversation, advice, or exploratory brainstorming;
- a single clarification before otherwise authorised work;
- questions answerable from tickets, documents, source code, telemetry, or other available evidence;
- requirements gathering that does not need a preserved reasoning trail;
- work where the user has already made the decision and asked for drafting or execution.

If the trigger is doubtful, communicate normally. Do not invent a lightweight interview mode.

## Interview contract

A proper adaptive decision interview has one workflow:

1. Read available evidence before asking the human to supply context.
2. Establish the decision horizon and current phase boundary.
3. Create the interview record and its cumulative registers.
4. Ask one high-leverage question.
5. Record the answer verbatim before interpreting it.
6. Update the current decision state.
7. Let that answer determine the next question.
8. Stop when further answers would not materially change the authorised artefact.
9. Produce only the interview outcome the user authorised.

## Before the first question

### Read sources first

Inspect the available source pack: tickets, research, prior decisions, code, logs, and existing artefacts. Ask the human for judgement that sources cannot reliably provide:

- desired outcomes and acceptable failure;
- tacit priorities and trade-offs;
- ownership, authority, and organisational boundaries;
- acceptable manual work or existing-tool fallbacks;
- practical behaviour under pressure;
- confidence, disagreement, and who must validate an assumption.

Do not make the interviewee repeat facts the agent can recover directly.

### Confirm the phase boundary

State internally what the user has authorised: interview only, interview plus calibrated summary, or interview followed by a named artefact. Research, interviewing, drafting, planning, and execution are separate phases.

An interview request does not authorise a proposal. A request for research does not authorise an interview. A completed interview does not authorise implementation.

### Establish the decision horizon

Distinguish the ultimate decision from any concrete orientation target.

For example, a named MVP may make an investigation tangible while the real decision is whether to adopt a technology for the foreseeable future. Questions and stopping criteria must serve the confirmed decision horizon rather than accidentally shrinking it to the example.

### Start the record

Use the user-provided location. Otherwise, place the record near the work it governs—normally a repository working folder—without committing it unless requested. If no writable workspace exists, keep the structure in the conversation and say plainly that it is not a durable file.

Seed the record with:

- status and timezone;
- source basis: paths, URLs, or evidence reviewed before the interview, plus the relevant facts relied on;
- interview purpose and decision horizon;
- authorised output and phase boundary;
- current calibrated direction, initially empty—a compact statement of what the interview has established, never a recommendation or downstream draft;
- cumulative assumptions, constraints, unknowns, learnings, and deferred decisions;
- the first pending question and why it matters.

## Select the next question

Choose the unresolved judgement with the highest **decision value**.

A high-value answer could change one or more of:

- the outcome or decision rule;
- required, optional, deferred, or excluded scope;
- ownership or allocation boundaries;
- authority to request, approve, execute, cancel, or override;
- acceptable manual work and fallback paths;
- failure thresholds and recovery behaviour;
- lifecycle, persistence, or reset boundaries;
- trusted data sources, semantics, or provenance;
- validation evidence or the person who must supply it;
- whether the interview should stop.

Prefer questions that are:

1. **Material** — different answers lead to meaningfully different artefacts.
2. **Human-only** — the answer is judgement, not recoverable information.
3. **Low burden** — the interviewee can answer without preparing a report.
4. **Timely** — the answer resolves the current decision frontier rather than a later implementation detail.

### Advance past the stated decision surface

Do not ask the interviewee to repeat alternatives or uncertainty they have already stated. Once the decision surface is clear, ask for the consequence, criterion, or operational episode that would discriminate between the options.

For example, if the user has already said the choice is between platform-owned releases and application-owned paved roads, asking “which model are you choosing?” merely restates the unresolved decision. A higher-value question asks who must be accountable for diagnosis, rollback, and incident response when a release harms production. That answer supplies evidence for the choice.

## Design low-friction questions

### Ask one substantive question per turn

A short preface may explain why the question matters, but it must not smuggle in several additional questions. If an answer would require addressing unrelated dimensions, split the question.

### Prefer recognition and correction

When evidence supports plausible alternatives, offer a short inferred workflow or two to four bounded choices. Make the consequences of each choice clear.

Always leave room to:

- select several choices;
- qualify an answer;
- reject the framing; or
- answer in the interviewee's own words.

Do not use multiple choice when the options would create false certainty or anchor an answer that needs a concrete story.

### Ask for episodes when abstractions conceal the work

A concrete episode often reveals actors, timing, hand-offs, tools, and failure consequences better than an abstract feature list:

> The preferred network has just disappeared during an operation. Who notices first, what do they try, and where must recovery stop if that fails?

Use the episode to discover decisions. Do not silently turn every detail in the story into a requirement.

### Keep the answer small

Explicitly permit rough bullets, option letters, examples, “none”, and “I don't know”. The logged interpretation may be detailed; the human's required response should not be.

### Use the conversational channel

Ask in ordinary chat unless the user requests a form or specialised question interface. Single-select controls often prevent combinations and contextual corrections—the parts of the answer that carry the most judgement.

## Useful interview lenses

Pick one lens by default: the one that best resolves the current frontier.

| Lens | What it reveals |
| --- | --- |
| Outcome | What must become true, and what decision the artefact must enable |
| Concrete episode | Actual actors, sequence, timing, tools, and hand-offs |
| Scope cut | Required, useful if cheap, later, excluded, or unknown |
| Boundary | What belongs in the product, another tool, a manual process, or a later phase |
| Authority | Who may request, approve, execute, cancel, or override behaviour |
| Bad day | Offline, stale, rebooting, busy-operator, conflicting-state, and recovery behaviour |
| Lifecycle | What persists, accumulates, may be edited, resets, or survives restarts |
| Data authority | Trusted source, exact semantics, corrections, provenance, and minimum fidelity |
| Validation | Direct experience, team agreement, assumption, field evidence, or another owner |

## Record each answer atomically

Before asking the next question:

1. Timestamp receipt, including timezone.
2. Preserve the complete answer verbatim as a block quote.
3. Redact credentials and secrets as `[REDACTED]`; note that a redaction occurred.
4. Write the interpretation separately.
5. Record how the answer changes the artefact or follow-up path.
6. Update assumptions, constraints, unknowns, learnings, and deferred decisions.
7. Resolve or narrow superseded entries rather than leaving stale registers.
8. Choose and record the next question and its purpose.
9. Only then ask it in chat.

Use this entry shape:

```markdown
### QN — Short topic

**Asked:** YYYY-MM-DDTHH:MM:SS+ZZZZ (TZ)

**Question:** <exact question>

**What this is trying to decide:** <material consequence of the answer>

**Evidence basis:** <source paths, register IDs, or known facts that shaped the question; “human judgement only” if none>

**Answer received:** YYYY-MM-DDTHH:MM:SS+ZZZZ (TZ)

**Answer:**

> <complete verbatim answer>

**Interpretation:** <inference, kept separate from evidence>

**Effect:** <change to scope, ownership, direction, artefact, or next question>

**Register updates:** <IDs added, changed, resolved, or deferred>
```

The quote is evidence. Do not tidy it, complete it, or replace it with a polished paraphrase.

## Maintain cumulative decision state

Keep concise registers near the top of the record so the current state can be understood without rereading the full transcript.

### Assumptions

Record the claim, source, confidence, validation owner or method, and status. Do not promote a plausible inference into a constraint.

### Constraints

Record the boundary, its source, and its consequence for the authorised artefact.

### Unknowns

Record why the unknown matters, who or what can resolve it, and whether it is open, narrowed, deferred, or resolved.

### Learnings

Record the durable implication and its evidence. Keep this compact; the full answer remains in the chronological record.

### Deferred decisions

Record the trigger for revisiting the decision, the evidence needed, and the future owner. “Not sure yet” is a valid result, not an invitation to invent a fallback answer.

## Follow the answer

After each answer, briefly state what changed if that helps orientation; do not recap the entire interview. Follow any more consequential exception, ownership boundary, or unknown the answer exposes, and remove planned questions it already resolved.

When an answer represents somebody else's needs, distinguish:

- direct experience;
- established team agreement;
- the interviewee's informed judgement; and
- a best guess requiring validation.

This prevents confident prose from laundering an assumption into a decision.

## Honour pivots, corrections, and amendments

When the user says the interview is too deep, at the wrong level, or aimed at the wrong topic:

1. Record the correction verbatim.
2. Mark the abandoned line as deferred or out of scope.
3. Update the decision frontier.
4. Ask the next question at the requested level immediately.

Do not defend the old line, finish its questionnaire, or explain why the detail might eventually matter.

Treat corrections after an interview as timestamped amendments. Preserve the original answer, append the amendment verbatim, and update the calibrated direction and affected registers. Do not rewrite history to make the conversation appear consistent.

A statement such as “I want to direct this” is a control boundary. Stop synthesising unapproved decisions and return control through the next high-value question.

## Preserve uncertainty

Uncertainty is often the most useful finding in the interview. When the user is unsure:

- identify what decision remains open;
- record why it matters;
- name the evidence or event that would make the decision timely;
- identify the future decision owner where possible; and
- continue only if another current question could narrow the uncertainty honestly.

Do not force a speculative choice merely to complete a register or produce a tidy summary.

Once a decision has been deferred to a named owner, evidence source, and future trigger, remove it from the current interview frontier. Do not immediately ask the interviewee to decide the same uncertainty in different words. Move to another current judgement that can be answered honestly, or stop.

## Stop deliberately

After each answer, ask internally:

> Can any unresolved human judgement still materially change the authorised artefact?

If no, stop. Do not ask ceremonial questions to make the interview feel comprehensive.

The interview is normally complete when the current decision has enough clarity about:

- outcome and decision horizon;
- material scope boundaries;
- ownership or authority;
- fallback and consequential failure behaviour;
- validation owners or deliberately deferred unknowns.

Not every interview needs every category. The marginal-value test is authoritative.

At completion:

1. mark the record complete and remove any pending-question marker;
2. write a concise **Calibrated direction** above the chronological entries: the current state of the interview—established boundaries, material rationale, and open decisions—not a recommendation or downstream artefact;
3. list unresolved and deferred decisions without smoothing them away;
4. tell the user why the interview can stop; and
5. do not automatically draft a spec, recommendation, plan, or implementation.

Cross the next phase boundary only when the user asks.

## Worked first turn

User:

> I want an experiment that tells us whether this technology is mature enough for adoption. Interview me before writing the plan.

Poor responses either draft the experiment or ask a batch about architecture, metrics, schedule, UI, and testing.

A useful first turn identifies the decision horizon:

> At the end of this experiment, which decision must the evidence let you make?
>
> **A.** Adopt or reject the technology for the foreseeable future
>
> **B.** Choose among integration methods while adoption remains assumed
>
> **C.** Estimate migration effort and the largest unknowns
>
> **D.** A combination, or something else
>
> Multiple selections and context are welcome.

The next question depends on the answer. It is not selected in advance.

## Failure patterns

- **Premature authorship:** converting research or a vivid answer into an unapproved plan. Return to the authorised phase.
- **Questionnaire batches:** optimising for coverage rather than decision value. Ask one material question.
- **Leading recognition:** offering choices that encode the agent's preferred answer. Contrast consequences and keep an escape hatch.
- **Feature-list gravity:** treating every plausible capability or episode detail as required scope. Ask for an explicit scope cut.
- **Depth creep:** building a complete domain model after the decision boundary is already clear. Defer implementation detail.
- **False closure:** turning uncertainty into a decision because the document wants an answer. Record a deferred decision.
- **Deferred-decision loop:** naming a future owner and evidence, then asking the current interviewee to decide it anyway. Remove it from the current frontier.
- **History laundering:** silently rewriting an earlier answer after a correction. Append an amendment.
