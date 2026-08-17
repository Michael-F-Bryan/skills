---
name: adaptive-decision-interviews
description: Use when the user wants the agent to conduct a structured interview that elicits and preserves their judgement before a decision artefact is drafted. Do not use for ordinary chat, job-interview practice, advice, brainstorming, fact gathering, one-off clarification, or execution after direction is already clear.
---

# Adaptive Decision Interviews

## Purpose and boundary

Use this skill to elicit and preserve human judgement before an authorised decision artefact is drafted. The human owns the decision; the agent reduces expression cost, exposes consequences, and keeps evidence separate from interpretation.

An interview is not research, drafting, planning, or implementation. It does not authorise a proposal or downstream artefact unless the user explicitly names that output. If the trigger is doubtful, communicate normally.

## Before Q1: source-first decision contract

Read the available source pack first: tickets, research, prior decisions, code, logs, and existing artefacts. Recover facts yourself. Ask the human only for judgement sources cannot establish: outcomes, trade-offs, ownership, authority, acceptable manual work, practical failure behaviour, confidence, disagreement, or validation responsibility.

Before asking the first substantive question, state one compact contract and invite correction:

- **Decision horizon:** the ultimate adoption, investment, product, or policy decision the work must support—not merely the example or first milestone.
- **Orientation target:** value-leading use case, first shared capability, and validation context, kept as separate axes from the horizon.
- **Authorised output:** interview record, calibrated summary, or a named decision artefact; also name the intended reader.
- **Current phase and stopping gate:** what this interview may decide, and what would make further questions no longer decision-useful.
- **Evidence boundary:** sources reviewed, facts relied upon, and judgements that remain human-owned.

Record the contract and its provenance before classification. If an axis remains unclear, make it Q1 rather than asking for ceremonial approval and then starting the real interview. Do not proceed to domain questions until the contract is accepted or corrected. If acceptance is only assent to an assistant-framed contract, treat that framing as `assistant-proposed`, not as load-bearing human evidence; use the next substantive question to obtain a consequence, episode, criterion, or independent source. Do not ask consecutive confirmation questions.

Do not collapse the decision horizon, value-leading use case, first shared capability, and validation context into one exclusive choice. A concrete example may orient the interview without shrinking its horizon. If the true horizon emerges later, record the correction, update the contract, and re-evaluate the frontier rather than defending the old line.

If the user asks what the interview, ticket, or exercise is actually trying to achieve, treat that as a contract-control signal: pause the pending question, preserve the challenge, state the current purpose as agent interpretation, and wait for correction or renewed authorisation.

## Phase state and record layers

Create or use the user-specified record location. If no writable location exists, keep the structure in chat and say it is not durable. Seed it with status/timezone, phase, source basis, contract, authorised output, current projection, unresolved/deferred decisions, and the next-question marker.

The record has two logical layers:

1. **Chronological evidence:** additive, immutable entries containing questions, complete verbatim answers, amendments, provenance, interpretation, effects, and phase changes.
2. **Current projection:** a concise living view of the active contract, calibrated direction, scope/ownership/authority boundaries, open judgements, deferred questions, and next evidence gate.

The projection is not a replacement for evidence and must point to the entries or source refs supporting consequential claims. Trigger `productivity:evidence-log-curation` when the record exceeds about 20 substantive entries or 300 lines, reaches a phase boundary, adds external review, or becomes difficult to scan. Preserve evidence before compressing it; keep archive/JSONL/hash mechanics in that skill, not here.

Use these states exactly:

- **Active:** a named phase is authorised, unresolved human judgement remains, and one next question is selected.
- **Paused:** the user has stopped questioning; no pending question exists; unresolved decisions are preserved; do not continue until explicit resume.
- **Complete enough for <artefact>:** the named artefact can be produced without another interview question, while other decisions may remain open or deferred.
- **Complete:** the authorised interview phase is closed, its projection is current, no pending question remains, no unresolved human judgement remains inside that phase, and deferred items have an owner, trigger, or evidence gate.

Every pivot into reflection, review, readiness, or drafting updates the status first. A pivot pauses or closes scripted questioning; it does not silently resolve judgement.

## The adaptive loop

For each turn:

1. Recompute the current decision frontier from the projection and latest evidence.
2. Choose one unresolved judgement with the highest decision value.
3. Ask one substantive question in ordinary chat; permit rough bullets, examples, “none”, and “I don’t know”.
4. Record the answer verbatim before interpretation, with provenance and confidence.
5. Apply corrections or scope pivots immediately, update registers and status, then select the next question only while the phase remains **Active**.
6. Stop when no unresolved human judgement can materially change the authorised output.

A question passes the decision-value test only if it is **material** (different answers change the artefact or its authority), **human-only** (not recoverable from sources), **current** (not a later implementation detail), and **low burden**. Prefer questions that resolve outcome, scope, ownership, authority, fallback, failure threshold, persistence, data authority, validation, or stopping.

Do not ask a question whose answer is already present. Once alternatives are stated, ask for the consequence, criterion, or operational episode that would discriminate between them. Recognition is useful: offer two to four bounded interpretations with consequences and an escape hatch, then test the candidate against a concrete operational job before recording detailed semantics. A correction or rejection is evidence about the framing, not confirmation of it.

Use a concrete episode when abstractions hide actors, timing, hand-offs, or failure consequences. The episode discovers decisions; it does not turn every detail into scope. A bad-day question is allowed only when its answer can change the current artefact’s ownership, representation, persistence, or authority boundary. If the discussion requires combined-fault precedence, timeout matrices, regulator thresholds, qualification evidence, or a formal FMEA, preserve the invariant and defer the entire analysis family.

Establish required semantics before mechanisms. Resolve the durable hand-off, failure/retry responsibility, processing granularity, and genuine boundary before asking about a tool, provider, framework, or component. For a required derived product, resolve source authority, correction/provenance, minimum fidelity, claim semantics, hidden acquisition, lifecycle, and validation owner. See `references/decision-separation-and-implementation-semantics.md`.

## Evidence, corrections, and closure

Each entry keeps these separate: exact question and complete answer as block quotes; why the answer matters; source/evidence basis; provenance class; confidence; corroboration or missing corroboration; interpretation; effect on the authorised output; register updates; and next-question purpose. Redact secrets as `[REDACTED]` and note the redaction. The answer is evidence; the interpretation is not. Apply the rules in `references/evidence-and-elicitation-provenance.md`.

When the user corrects the topic, level, horizon, or prior answer:

1. preserve the correction verbatim with a timestamp;
2. record candidate provenance before classifying it;
3. mark the abandoned line deferred or out of scope;
4. update the contract, projection, frontier, and affected registers;
5. ask the next high-value question at the corrected level.

Never rewrite history. If one reply amends an earlier answer and answers the current question, record two atomic items. A statement such as “I want to direct this” is a control boundary: stop synthesising unapproved decisions.

Do not force uncertainty into a choice. Record what remains open, why it matters, who or what can resolve it, and the trigger. Once deferred to a named owner/evidence gate, remove it from the current frontier instead of asking the same question again.

Stop when the authorised output has enough direction about its decision horizon, material scope, ownership/authority, consequential failure or fallback behaviour, and validation or deliberate deferral. Not every category is required; the marginal-value test governs. On closure, remove the pending-question marker, update the state, write the concise projection, list unresolved/deferred items, and explain why questioning stopped.

A **publishable interview record** is an auditable account of the interview. A **decision artefact informed by the interview** is a separate downstream output: it uses the current projection and evidence references, not interview chronology as its narrative spine. Do not draft either one, or cross the phase boundary, without the user’s authorisation. For exact pause/resume, readiness, amendment, and phase rules, see `references/phase-transitions-and-readiness.md`.

## Quick self-check

Before each question: *Could different answers materially change the authorised output, and is this judgement unavailable in the sources?* If not, do not ask it. Before completion: *Is the state accurate, is the projection supported by evidence refs, and has the downstream author been explicitly authorised?*
