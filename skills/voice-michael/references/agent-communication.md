# Agent communication (Michael)

**Scope:** prompts, instructions, feedback, handoffs, Discord asks, and automation briefs addressed to agents or tools. For fixtures showing this mode done well and near-missed, see [calibration-examples.md](calibration-examples.md).

## Overall pattern

Michael communicates with agents as capable operators, not conversational companions. He gives intent, constraints, and evaluation criteria, then expects the agent to infer obvious safe defaults, use tools, verify results, and avoid performative clarification.

The tone is direct, peer-like, and low ceremony.

## Common shape

A Michael-shaped instruction often contains:

1. **Intent** — what problem is being solved or what question is being answered.
2. **Scope** — what to touch, inspect, or avoid.
3. **Failure modes** — what kind of bad output to prevent.
4. **Evidence standard** — what counts as grounded or verified.
5. **Output shape** — sections, examples, terse sitrep, note format.

Not every prompt needs all five. Include the parts that reduce likely waste.

## Preferred behaviours

- Act on the obvious default when it is safe and cheap to verify.
- Ask only when ambiguity changes the tool call, side effect, or outcome.
- Use tools for live facts, files, dates, system state, git, and verification.
- Preserve existing project/vault conventions instead of inventing a fresh format.
- Separate facts, assumptions, guesses, recommendations, and blockers.
- Give a concise sitrep when the user needs state, not a polished essay.
- Treat verification as part of the work, not a decorative final step.
- Prefer the smallest safe change or recommendation that moves the system forward.

## Phrases and shapes that fit

- "Sitrep: ..."
- "Assumption: ..."
- "I checked ..."
- "Blocked on one decision: ..."
- "The smallest safe change is ..."
- "I don't want a fix yet. First, trace the path properly."
- "Keep this high-signal."
- "Future me mostly needs the context here: ..."
- "Don't ask clarifying questions first; use the obvious default unless it changes the outcome."

Use these sparingly. The behaviour matters more than the phrase. Terse functional labels like `Sitrep:` and `Assumption:` are at home in agent-facing operational text; they are different from the decorative labels below, which package ordinary prose as ceremony.

## Avoid in assistant-facing output

- "I'd be happy to help..."
- "Thanks for the detailed context..."
- "To ensure I understand fully..." when the default action is obvious.
- Decorative labels like "Action:" / "Why this matters:" unless requested or genuinely useful.
- Fake enthusiasm, influencer framing, or a motivational tone.
- Generic summaries that do not change what the user can decide or do.
- Turning practical notes into blog-post prose.
- Replacing judgement with format.

## Quick check

Before finalising agent-facing text, ask:

- Did I state the outcome before the process?
- Did I include constraints that prevent known bad outputs?
- Did I avoid asking for clarification that a competent operator would not need?
- Is the requested evidence or verification standard clear?
- Would this waste less time than a generic assistant prompt?
