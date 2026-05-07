---
name: handoff-iteration-loop
description: >-
  Use when coordinating multi-iteration work with explicit `_working/{TOPIC}/`
  handoffs, binary sprint contracts, and independent reviewer gating after
  implementation.
---

# Handoff iteration loop

Multi-agent pattern inspired by [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps) (Anthropic): **separate generation from evaluation**, **structured artefacts** across iterations, **sceptical external QA**, **contracts before heavy work**, **simplify the harness** when the task no longer needs every role — and **real dev-team shape**: **discovery / Q&A → goals → sprints → loop**, with **Git commits as the implementor goes**.

## Progressive disclosure — load only what you need

| If you are…                                                             | Read first                                                                  | Then if needed                                                                                                              |
| ----------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Spinning up the workflow**                                            | This file + [workflow.md](workflow.md)                                      | [discovery.md](discovery.md) if the ask is vague; then role files                                                           |
| **Discovery / customer goals**                                          | [discovery.md](discovery.md)                                                | [workflow.md](workflow.md) §Phases                                                                                          |
| **Redesigning the harness** (adding/removing roles, changing contracts) | [harness-principles.md](harness-principles.md) + [workflow.md](workflow.md) | Role files only if prompts change                                                                                           |
| **Coordinator** (main agent orchestrating `Task` / sub-agents)          | [coordinator.md](coordinator.md)                                            | [workflow.md](workflow.md) §Contracts, any single [planner.md](planner.md) / [reviewer.md](reviewer.md) for prompt patterns |
| **Planner sub-agent**                                                   | [planner.md](planner.md)                                                    | [workflow.md](workflow.md) §Handoff filenames + §Sprint contract                                                            |
| **Implementor sub-agent**                                               | [implementor.md](implementor.md)                                            | [workflow.md](workflow.md) §Contracts, [planner.md](planner.md) §Anti-patterns (mirror only outcomes)                       |
| **Reviewer sub-agent**                                                  | [reviewer.md](reviewer.md)                                                  | [workflow.md](workflow.md) §Sprint contract + §Evidence                                                                     |

Do **not** load all role files into one context unless the coordinator is authoring a full runbook in one shot.

## Minimal workflow (one screen)

```text
(Optional) Discovery → _working/{TOPIC}/GOALS.md  [see discovery.md]
       ↓
Coordinator → Planner writes _working/{TOPIC}/iter{N}.1-planner.md
           → Implementor (git commits as you go + iter{N}.2-implementor.md)
           → Reviewer (verification + iter{N}.3-reviewer.md)
           → Coordinator gates iter{N+1} or stops; updates project HANDOVER/STATE line
```

**Markdown handoffs** + **`GOALS.md`** carry intent; **git** carries implementation history. No chat-memory reliance.

## Hard rules (always)

1. **Tier decides required handoff files** under `_working/{TOPIC}/` (see [workflow.md](workflow.md) §Tiering):
   - **Full tier:** `iter{N}.1-planner.md`, `iter{N}.2-implementor.md`, `iter{N}.3-reviewer.md`
   - **Pair tier:** `iter{N}.2-implementor.md`, `iter{N}.3-reviewer.md` (+ reference the active planner contract)
   - **Solo tier:** `iter{N}.2-implementor.md` (+ explicit “risk accepted” line)
2. **Planner** embeds **`## Sprint contract (binary checks)`** — reviewer executes it mechanically ([workflow.md](workflow.md)).
3. **Reviewer defaults to FAIL** unless every contract line has independent evidence.
4. **Coordinator does not** plan, implement, or review the artefact **unless** the user explicitly collapses roles.

## Veritas reference templates

MUL-55 Grafana temp dashboard: `_working/mul55-dash/iter6.1-planner.md` (contract + protocol), `_working/mul55-dash/iter6.3-reviewer.md` (sceptical PASS table), `_working/HANDOVER-mul55-cost-dashboard.md` (index line pattern).
