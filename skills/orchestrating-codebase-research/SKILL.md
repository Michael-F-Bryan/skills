---
name: orchestrating-codebase-research
description: Use when research must fan out across a corpus too large to read in one context — a large codebase, document set, or mixed source pack — and findings must be aggregated into a cited synthesis, architecture map, seam analysis, or decision report. Also use when coordinating research sub-agents/workers over source code, or when the user says "build intuition for how X is structured", "map the architecture", or "find seams for moving Y".
---

# Orchestrating Codebase Research

## Core principle

Coordinator context is for judgement — decomposition, gap analysis, dispositions, promotion. Source reading belongs to bounded workers. The filesystem is the evidence chain; chat is a receipt. **Synthesis is continuous, not a final phase**: a research effort that has produced verified reports but an empty synthesis is behind, no matter how full its task ledger is.

## When to use

Use when delegated research will span multiple workers or waves and the output must be a cited aggregate. Do not use for questions one agent can answer by reading the relevant files directly — fan-out below ~3 lanes is ordinary delegation; use `dispatching-parallel-agents`.

**REQUIRED SUB-SKILL:** `working-docs` owns the substrate rules (placement, git-ignore handling, write-as-you-go). This skill adds the orchestration layout and contracts.

## Calibrate first

Before creating the substrate, ask the user one brief round of calibration questions — only questions whose answers change the plan or the deliverable:

- **Purpose**: what decision or next step will the research inform?
- **Audience and genre**: who reads the final deliverable, in what setting — standalone decision brief, working reference, or both? Two audiences means planning two artefacts from the same synthesis now, not a late rewrite.
- **Research questions**: numbered, and what "answered" looks like — this becomes the definition of done.
- **Scope**: the representative sub-corpus or variant to trace, comparisons or baselines wanted, explicit exclusions.
- **Constraints**: time/cost budget, source boundary, version to pin.

Record the answers in README.md's framing. A mid-flight change to any of these is a contract change: JOURNAL entry plus README update, never a silent pivot. In the observed session, both a comparison requirement and the true meeting-room audience were available at the start but surfaced mid-flight — one cost an extra research lane, the other a full report rewrite at the end.

**RELATED SKILL:** `adaptive-decision-interviews` when the user wants deep elicitation with a preserved reasoning trail; the round above is deliberately one pass, not an interview mode.

## Substrate

```text
_working/<topic>/
  README.md      # stable framing ONLY: underlying need, research questions,
                 # source boundary, pinned commit, definition of done. No status.
  LEDGER.md      # sole status authority: task table (id, scope, status, artefact,
                 # review verdict, promoted?) + next gate. Update every wave.
  JOURNAL.md     # append-only: decisions, failures, contract changes, recoveries.
  SOURCE-MAP.md  # corpus orientation from wave 1; cited in every later brief.
  SYNTHESIS.md   # the living aggregate. Exists from wave 1, grows every wave.
  tasks/Txxx-<slug>/{BRIEF.md, REPORT.md}      # retries get new dirs: Txxx-A2-<slug>
  reviews/Rxxx-Txxx/{BRIEF.md, REVIEW.md}      # disposition appended to REVIEW.md
```

Do **not** pre-create topic/aggregation stub files: they carry no information and go stale — README status sections and empty "notes" skeletons were the first artefacts to rot in practice. Create a file when its first real content exists. Retire a ledger only with a final entry naming its successor.

State stays truthful only in files the loop forces you to touch: LEDGER.md stays current because reading the next gate means updating it; a README annotation is consulted by no step, so no step ever corrects it. So: outside LEDGER.md, describe **role, not state** — no "not yet written", "in progress", "pending", counts, or verification verdicts. An artefact index needs no state column; the directory listing is the state. In the observed session the handoff README told the next agent the final report was "not yet written" long after it had shipped and been reviewed — a sync instruction cannot fix this; placement can.

## Coordinator boundary

The coordinator never reads the corpus — only `_working/` artefacts and user-supplied framing documents (requests, meeting notes, prior decisions; their content is judgement/framing, never source fact). Source confirmation, contradiction checks, and citation validation are worker tasks. Repo metadata (`git rev-parse` for the commit pin, `git status` for cleanliness) is not corpus reading. Sitreps come from LEDGER.md plus reports, not from re-inspection. This boundary is what lets on-disk state outrank anyone's impression of progress — including the user's ("I think it's complete" is answered from the artefacts, and the artefacts win).

## Lane design

- A lane must fit **comfortably inside one worker run** (well under the worker's call/time budget). When in doubt, split before dispatch: an oversized lane observed in practice burned three worker runs to deliver what two half-sized lanes then produced in one run each.
- Splitting beats retrying. If a lane fails on budget, do not re-run it with sterner instructions — cut its scope in half.
- Batch only related lanes (same subsystem, same source family). Never combine unrelated work to fill capacity.
- Stage the first wave as orientation: it produces SOURCE-MAP.md (directory roles, key entry points, where each subsystem lives) alongside its findings. Every later brief cites SOURCE-MAP.md and the specific prior reports it builds on — workers re-deriving repo layout from scratch cost millions of input tokens per worker before this rule.

## Dispatch

Worker invariants live **once**, in the brief template (`references/worker-contract.md`) — never restated ad hoc per dispatch, which drifts. A dispatch message is only: role, the exact brief path, and the return contract.

Before every dispatch, read the brief back from disk and paste that exact path into the dispatch — never retype it. A hand-retyped path, mangled in 2 of 3 first-wave dispatches in practice, made one worker reconstruct its task from ambient files and silently drop a research question. The worker-side rule is the mirror: read the brief first; if the path is unreadable, return `BLOCKED` with the attempted path — never reconstruct the task from nearby files.

Every brief carries the persistence-first contract from wave 1 — not as a recovery measure after a loss: skeleton REPORT.md within the first three calls, checkpoint after each section, calls reserved for read-back. A worker that dies mid-run must leave salvageable sections, not nothing.

## Verify

Every first-order research report gets an independent adversarial review — a worker with source access, briefed to refute: locate each cited path/line, check the wording is supported, separate fact from inference, hunt omissions. In practice this caught real errors in **every single report** (wrong file citations, subsystem-specific evidence generalised corpus-wide); skipping it is how plausible-but-wrong claims reach the synthesis.

The reviewer's verdict is not authoritative. The coordinator appends a per-finding disposition (accept / narrow / resolve) to REVIEW.md — no separate validation file. Disputed consequential claims go to a fresh, narrow resolution lane.

Cap the loop: resolutions are reviewed only if they introduce new consequential claims. Wording-level corrections are applied directly and never re-reviewed.

## Promote — continuous synthesis

After each disposition, immediately merge that report's corrected **"claims safe for synthesis"** into SYNTHESIS.md, each with provenance (`Txxx`/`Rxxx` + `path:line`). Rules:

- Promote from the disk artefact **re-read in the same turn** — never from memory of it. Context compaction silently replaces artefacts with summaries of them.
- After promoting, gap-check SYNTHESIS.md against README's research questions and dispatch narrow gap lanes for what's missing.
- The wave loop is: dispatch → review → disposition → **promote** → gap-check → next wave. A wave is not done at "review complete"; it is done at "promoted".

## Finish

The final report is **assembly** from SYNTHESIS.md — ordering, framing, and an honest unknowns/not-inspected section — not fresh writing. Then:

1. **The final deliverable passes its own adversarial review before "done".** The same gate every worker artefact passed applies to the coordinator's writing; the observed failure was a coordinator that reviewed everything except itself, declared completion, and was immediately handed a REVISE when the user forced a review.
2. **Verification is semantic**: each research question is answered, each consequential claim traces to a promoted SYNTHESIS.md entry. Headings-exist and paths-resolve checks are necessary but prove nothing about content. Close with a **staleness sweep**: re-read every `_working/` file that describes another artefact and correct any sentence the work since has falsified — "not yet written" annotations, superseded verdicts, counts describing an earlier version.
3. **Never overwrite a verified deliverable.** Revisions produce `FINAL-REPORT-v2.md` (or an archived copy first). `_working/` is typically untracked — an overwrite there destroys the only copy. Ledger verification claims describe a specific file; re-run them against the file actually shipped.
4. **Every source-fact sentence keeps its anchor** (`path:line` or a SYNTHESIS/index row ID) through every revision. "Make it standalone" means inline the evidence, not strip it.
5. **Audience reframing is a contract change.** Restructuring for a meeting, an exec, a different reader: either update README's definition of done first, or ship a second artefact derived from the same synthesis. Never silently mutate the research deliverable into a different genre. Content imported from outside the evidence pipeline (meeting notes, user assertions) is labelled as judgement, never presented as source fact.
6. **Post-review edits beyond pure wording trigger a diff-scoped re-review.** Promote only the reviewed bytes.
7. **Cap finishing ceremony**: at most two render-verify iterations on cosmetics (diagrams, formatting); delegate cosmetic QA rather than looping on it. In the observed session, diagram polishing consumed more coordinator traffic than all endgame research combined.

## Failure handling

- Inspect the task directory before retrying — completion summaries and artefacts can disagree in both directions; non-empty expected files plus a coherent report outrank any chat summary, and a detailed chat summary with a missing report is an **incomplete task**, never evidence.
- Retries get a fresh `Txxx-A2-*` directory; preserve the failed attempt; re-dispatch only the missing scope, halved.
- Record every failure, recovery, and contract change in JOURNAL.md — the observed recovery that worked was designed directly from the journal entry describing the failure.

## Pitfalls

| Observed failure | Rule that prevents it |
|---|---|
| 53 min of verified reports, zero synthesis | Promote after every disposition; wave ends at "promoted" |
| Lane 2× worker budget → 3 failed runs | Size to comfortable single-run fit; split, don't retry harder |
| Mangled brief path → silently dropped question | Read brief back; paste exact path; worker BLOCKED rule |
| Same invariants reworded in 13 dispatches | Invariants live once in the template |
| Workers re-derive repo layout (1–5M tokens each) | SOURCE-MAP.md cited in every brief |
| Stub note files + README status rot | No pre-created stubs; status only in LEDGER.md |
| Reviews of reviews converge, add nothing | Review first-order reports; cap the loop |
| "Done" declared on unreviewed final report | Final deliverable passes the same review gate |
| Verified report overwritten by revision | Version revisions; re-verify the shipped file |
| "Standalone" rewrite strips all citations | Anchors survive revision; reframing = new contract or new artefact |
| Handoff README says report "not yet written" after it shipped | Role-not-state outside LEDGER.md; staleness sweep at finish |
