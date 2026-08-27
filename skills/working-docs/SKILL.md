---
name: working-docs
description: Use when a task has multiple phases, evidence sources, handoff or interruption risk, or intermediate findings that must change later decisions. Also applies when the user asks for a working folder or `_working` directory.
---

# Working Docs

## Core principle

`_working/<topic>/` is external task memory: preserve only the notes, evidence, and intermediate artefacts that later work will actually use.

A file earns its place only if deleting it would change a later action, decision, handoff, or audit. If the task could finish identically without the folder, skip it.

Working docs serve the requested task. They do not enlarge its scope, create extra review or testing obligations, or turn a quick task into a documented project.

## Activation gate

Use working docs when the user explicitly asks for a working folder or when one strong persistence need exists:

- interruption, compaction, or handoff is likely;
- another agent or process needs named intermediate artefacts;
- conclusions must remain auditable after the session.

Otherwise, use them only when both the task spans multiple phases, sources, files, or systems **and** findings may change later decisions.

Without an explicit request or persistence need, do not use working docs for one-shot answers, tiny edits, or work where no intermediate state matters after the next tool call. Reassess this gate even when the skill was preloaded.

## Location

Put one stable folder close to the work, normally at the repository root unless the user gives another path:

```text
<repo-root>/_working/<topic-slug>/
  README.md         # current state and entry point
  <other files>     # only evidence, drafts, prompts, or outputs later work needs
```

`README.md` should let a fresh agent resume: the underlying need, material constraints, current state, decisions, blockers, next step, and which files to read.

Keep `_working/` out of commits unless the user wants it tracked. Check effective ignore rules from the repository root:

```bash
git check-ignore -q _working/
```

Ignoring the folder is optional local hygiene, not a prerequisite. If it is not ignored, add `_working/` to `.git/info/exclude` only when local repository housekeeping is within the task's authority and the untracked noise would hinder the work. Otherwise leave repository configuration unchanged. Change the tracked `.gitignore` only when the user explicitly wants repository-wide policy. Outside a repository, use the working directory without creating Git configuration.

## What to preserve

Capture only information with downstream value:

- decisions and the evidence or constraint behind them;
- failed approaches that should not be repeated;
- paths, IDs, versions, exact inputs, and source references that affect conclusions;
- user corrections and how they changed the plan;
- unresolved questions, blockers, recovery information, and the next step;
- plans, prompts, drafts, or reports that another phase, process, or person will consume.

Do not dump raw output that is not itself evidence, duplicate the final response, maintain vague activity logs, or write a file merely because a template suggests one.

## Working-memory loop

1. **Seed before deep work.** Create `README.md` with the need, material constraints, current state, and next step.
2. **Update on meaningful change.** Record a decision, reusable finding, changed direction, durable blocker, or produced artefact when it occurs—not after every tool call.
3. **Read when the record is authoritative.** Read `README.md` after interruption or compaction, before handoff, after agents return, or before a decision that depends on captured evidence. Do not repeatedly reread unchanged files as ceremony.
4. **Keep the entry point current.** When the plan or state changes materially, update `README.md` so it points to the authoritative artefacts.
5. **Stop when the substrate is sufficient.** Once later work can resume and all claimed artefacts are grounded, do not add recap files or polish that no downstream action needs.

## Delegation and handoff

When another agent or process needs the working folder:

- provide the exact `_working/<topic>/` path;
- name the input files it must read and the output file it must produce;
- require source paths or evidence for material claims;
- read the named output before relying on it.

A summary saying a file was written is not evidence that it exists. Read every named or required handoff artefact before relying on it. If an expected file is absent or unreadable, report the missing artefact rather than treating the delegated task as complete.

## Bounded verification

Verify claims about working docs with the smallest direct check:

1. list the relevant folder;
2. read back `README.md`, every named or required artefact, and anything else whose existence or contents you will claim;
3. confirm blockers and next steps are current enough for the handoff or final response.

This verifies the working substrate only. Product behaviour, code, deployment, or hardware claims require evidence from the owning task; working docs do not trigger unrelated tests, full suites, reviews, or live operations.
