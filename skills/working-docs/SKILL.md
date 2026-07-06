---
name: working-docs
description: Use when a task has multiple phases, evidence sources, handoff risk, interruption risk, or intermediate findings that must affect later work. Record what you did in `_working/<topic>/` before finishing so another agent can continue. Sometimes referred to as the "working folder" or `_working/<topic>/`.
---

# Working Docs

## Core principle

`_working/<topic>/` is the task's external memory: notes, evidence, and intermediate artefacts that must outlive a single context window.

A note earns its place only if **deleting it would change a later action**. If the task could finish identically with the folder erased, you are doing ceremony, not working memory. Capture what you will reuse; skip what you will not.

## When to use

Use when at least two of these hold:

- multiple phases, sources, files, or systems
- findings that may change the plan later
- interruption, compaction, handoff, or sub-agents are likely
- claims must be auditable later (investigations, benchmarks, source-grounded synthesis)

Do **not** use for one-shot answers, tiny edits, or work where no intermediate state matters after the next tool call.

## Where it goes

Put `_working/` as close to the files it refers to as possible — normally the **root of the git repository** you are working in. One stable folder per task, unless the user gives a path:

```text
<repo-root>/_working/<topic-slug>/
  README.md         # the entry point: what this is, where things stand
  <other files>     # evidence, drafts, sub-agent prompts, the final artefact, etc.
```

`README.md` is the entry point — the first thing you or another agent reads on resuming. Add further files only when they pull their weight.

Persist the **work products** you generate — plans, prompts you write for sub-agents, drafts, the final report — as files in this folder, not just as notes about them. If a later step or another agent must use an artefact, it belongs on disk, not only in your reply.

Keep `_working/` out of commits unless the user wants the artefacts tracked: confirm it is covered by `.gitignore` (add a `_working/` line if not) before creating files. If there is no enclosing repo, use the working directory root.

## What to capture

There is no required format. Write what this task actually needs, in whatever shape serves recall and handoff. Choose from the following as the work warrants — a short task may need only the first two:

- **The underlying need** — the real goal or problem behind the literal request, so later decisions serve the intent and not just the wording.
- **Principles and values to honour** — constraints, preferences, and trade-offs to keep in mind when you must use initiative or decide something the user didn't spell out.
- **Definition of done** and the current plan or phases.
- **Decisions and the evidence behind them** — and, for claims that must be auditable, the source path/URL/command, the relevant fact, and any caveat.
- **Failed attempts** and what they ruled out, so you don't repeat them.
- **Paths, IDs, versions, and exact inputs** that affect conclusions.
- **Open questions, blockers, and the next step**, plus any user corrections and how they changed the plan.

Avoid dumping raw output that isn't itself the evidence, duplicating the final answer, vague lines like "looked at files", and stale TODOs left unreconciled.

## The loop

- **Seed** `README.md` before deep work with the underlying need, principles to honour, and definition of done — these anchor every later judgement call.
- **Capture** evidence, decisions, and the artefacts you produce (plans, prompts, drafts, reports) as files, while you still know why they matter.
- **Read back** before each phase change (drafting, changing direction, after a failed command, after sub-agents return, before the final response). When a captured fact settles a decision, **cite it instead of re-deriving from memory** — that citation is the proof the note mattered.
- **Close out** before you finish — done, blocked, or paused. Update `_working/<topic>/` so another agent can step in and continue without re-discovering what you already learned. Do not rely on chat history for handoff; the working directory is the handoff surface.
- **Resume** from `README.md` after any pause. The next agent (or you, post-compaction) should be able to continue from the folder alone.

## Agent handoff

When you use `_working/`, treat every session as potentially your last. **Before your final response, record what you did in the working directory.**

At minimum, update `README.md` with:

- what you did this session
- current state — done, in progress, or blocked
- the exact next step
- which files to read first

Persist any artefact the next agent needs (drafts, reports, prompts, evidence) as files in the folder, not only in your reply. If you changed the plan, recorded a decision, or ruled out an approach, that belongs in the working directory too.

## Verifying and handing off

Working docs are a substrate, not a substitute for verification. Before claiming completion, **REQUIRED SUB-SKILL:** `verification-before-completion` — list the folder, read back `README.md` and the artefact, and confirm files exist at the stated paths.

When delegating, give sub-agents the `_working/<topic>/` path, require a named output file, and read that file back yourself before trusting any summary. **REQUIRED SUB-SKILL:** `subagent-driven-development`. A missing file means the result is unverified, regardless of what the sub-agent reports.

For multi-agent work where roles hand off across the same `_working/` substrate, **RELATED SKILL:** `handoff-iteration-loop`.
