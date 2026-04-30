# Discovery — goals before the loop

Real product work rarely starts with a crisp spec. This phase mirrors what **dev teams do first**: vague customer intent → **questions** → shared understanding → **goals and principles** that later sprints and the planner–implementor–reviewer loop inherit.

## When to run it

- **Default** for new `{TOPIC}` work, multi-session effort, or “customer said something fuzzy” inputs.
- **Skip** (explicitly) for one-line typos, mechanical regenerates, or when the user hands you a finished sprint contract already.

## Who runs it

Usually the **coordinator** (main agent) with the **user** — not the Planner sub-agent. The output is a **durable artefact**, not chat scroll.

## Suggested artefact

Write under `_working/{TOPIC}/` (pick a stable name early):

```text
_working/{TOPIC}/GOALS.md
```

Sections (adapt to scope):

1. **Customer / user context** — who benefits, what “done” feels like for them.
2. **Problem framing** — what pain exists today (1–3 paragraphs).
3. **Goals** — numbered, **testable at a high level** (not LogQL yet).
4. **Principles** — e.g. “honest about Loki vs billing”, “no issue-tracker spam”, “prefer small PRs”.
5. **Non-goals / out of scope** — protects later Planners from scope creep.
6. **Open questions** — carry forward until answered; strike through when resolved.

Large programmes can add **`SPRINTS.md`** (ordered backlog of sprint themes) before iteration 1.

## Interaction pattern

- Ask **concrete** questions; prefer multiple-choice or “pick one of A/B” when the user is busy.
- Summarise back: “If I understood, we optimise for X, not Y — correct?”
- When stable, **commit GOALS.md** (or equivalent) so the Implementor’s git history shows the same story as the code.

## Hand-off to the loop

The **first Planner** (`iter1.1-planner.md`) should **reference** `GOALS.md` in its inputs and must not contradict it without calling that out explicitly.
