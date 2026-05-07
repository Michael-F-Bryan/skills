# Harness principles (short)

Source: [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps) (Anthropic Engineering).

Load this file when **designing** or **changing** the loop itself — not for every implementation iteration.

| Principle                               | In this skill                                                                                                                                                                                         |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Separate generation from evaluation** | Implementor vs Reviewer; never merge in one sub-agent run.                                                                                                                                            |
| **Structured artefacts across steps**   | `_working/{TOPIC}/iter{N}.1-planner.md` (and `.2` / `.3`) only; coordinator updates index.                                                                                                            |
| **Self-evaluation is optimistic**       | Reviewer must be **sceptical**; Implementor self-check does not replace Reviewer.                                                                                                                     |
| **Contracts before deep work**          | Sprint contract in planner = pre-agreed “done” + evidence type.                                                                                                                                       |
| **Context resets vs compaction**        | Each sub-agent spawn is a **fresh** context; handoff files carry state (like a reset with a good bundle).                                                                                             |
| **Stress-test the harness**             | [workflow.md](workflow.md) tiering — remove Planner or shrink to solo when safe; re-add if quality drops.                                                                                             |
| **Evaluator cost tracks difficulty**    | Full trio at the capability edge; pair/solo when inside comfort zone.                                                                                                                                 |
| **Real-world dev shape**                | [discovery.md](discovery.md): vague customer → Q&A → **goals artefact**; then **sprints**; loop per sprint. [implementor.md](implementor.md): **normal Git workflow** — branch, **commit as you go**. |
