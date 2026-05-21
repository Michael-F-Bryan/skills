# Agent communication (Michael)

Use this reference when drafting prompts, instructions, feedback, handoffs, Discord asks, or automation briefs in Michael's voice.

## Overall pattern

Michael communicates with agents as capable operators, not conversational companions. He gives intent, constraints, and evaluation criteria, then expects the agent to infer obvious safe defaults, use tools, verify results, and avoid performative clarification.

The tone is direct, peer-like, and low ceremony.

## Common shape

A Michael-shaped instruction often contains:

1. **Intent** - what problem is being solved or what question is being answered.
2. **Scope** - what to touch, inspect, or avoid.
3. **Failure modes** - what kind of bad output to prevent.
4. **Evidence standard** - what counts as grounded or verified.
5. **Output shape** - sections, examples, terse sitrep, note format, etc.

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

Use these sparingly. The behaviour matters more than the phrase.

## Avoid in assistant-facing output

- "I'd be happy to help..."
- "Thanks for the detailed context..."
- "To ensure I understand fully..." when the default action is obvious.
- Decorative labels like "Action:" / "Why this matters:" unless requested or genuinely useful.
- Fake enthusiasm, influencer framing, or a motivational tone.
- Generic summaries that do not change what the user can decide or do.
- Turning practical notes into blog-post prose.
- Replacing judgement with format.

## Synthetic examples

### Memory/model inspection

Good:

> I want to sanity-check what you think you know about me.
>
> Don't search the web, and don't ask clarifying questions first. Use memory and recent session context, then separate durable facts from things that are probably stale.
>
> I'm mostly interested in whether your model is useful, not whether it's flattering.

Too assistant-shaped:

> Please provide a comprehensive overview of my known preferences and background, including any caveats that may apply.

### Engineering investigation

Good:

> Have a look at the repo and tell me where this behaviour is coming from.
>
> I don't want a fix yet. First, trace the path properly and give me the smallest explanation that accounts for the symptoms. If there are two plausible causes, say what evidence would distinguish them.

Too vague:

> Investigate the bug and let me know what you find.

### Feedback to an agent

Good:

> That's close, but it's too assistant-shaped.
>
> Drop the "why this matters" framing, keep the actual signal, and assume the reader is already technical enough to understand the context. The useful part was the second paragraph.

Too softened:

> This is a good start, but perhaps you could make it slightly more concise and technical.

## Quick check

Before finalising agent-facing text, ask:

- Did I state the outcome before the process?
- Did I include constraints that prevent known bad outputs?
- Did I avoid asking for clarification that a competent operator would not need?
- Is the requested evidence or verification standard clear?
- Would this waste less time than a generic assistant prompt?
