---
name: working-docs
description: Use when handling multi-step tasks, investigations, or long sessions where working notes, interim findings, and scratch planning are needed to keep context and handoffs clear.
---

The `_working/` directory is a scratch space purely for your use.

## When to use

- Multi-step implementation, debugging, or investigation work.
- Tasks likely to span a long session or multiple handoffs.
- Cases where interim findings should be captured before final output.

## When not to use

- One-shot requests that can be completed directly with no intermediate reasoning artifact.
- Final user-facing docs that belong in the repository outside `_working/`.

## Working notes convention

Use a stable path so notes are easy to find and continue:

- `_working/<topic>/notes.md` for running notes and decisions
- `_working/<topic>/scratch.md` for temporary drafts/experiments

As you work through a problem, always write notes to `_working/`. Capture observations and the reasoning that connects those observations to the task or broader project. Keep notes structured so another agent (or a future session) can resume quickly.

You may delete files in the scratch space when you are done with them.
