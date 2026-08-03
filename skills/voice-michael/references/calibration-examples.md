# Calibration examples (Michael)

**Scope:** synthetic fixtures for calibrating any mode. These are not quotes; they are plausible Michael-shaped examples and near-miss counterexamples. A useful near miss is something a competent assistant, engineer, or manager might actually write — the point is to expose the missing constraint, evidence standard, or operational judgement, not to dunk on obviously bad prose.

## Agent prompts

### Memory inspection

Good:

> I want to sanity-check what you think you know about me.
>
> Don't search the web, and don't ask clarifying questions first. Use memory and recent session context, then separate durable facts from things that are probably stale, and call out anything that would be risky to rely on.
>
> I'm mostly interested in whether your model is useful, not whether it's flattering.

Near miss:

> Please give me a concise overview of what you know about me from memory, including preferences, background, and any caveats where you might be uncertain.

Why it misses: it optimises for a summary. Michael's version optimises for model inspection — it restricts lookup, prevents clarifying-question theatre, separates durable facts from stale ones, and names the evaluation criterion (useful, not flattering).

### Repo investigation

Good:

> Check the repo state first, then trace where this value is set.
>
> I don't want a fix yet. Give me the shortest explanation that accounts for the behaviour, plus the command output or file references that support it. If there are two plausible causes, say what evidence would distinguish them.

Near miss:

> Please investigate the bug, identify the likely root cause, and suggest possible fixes once you understand what's going on.

Why it misses: it quietly invites solution-shopping before the path is traced. Michael's version constrains sequence, evidence, and scope: check state, trace the value, no fix yet, cite the supporting output, and handle ambiguity by naming discriminating evidence.

### Implementation request

Good:

> Implement the boring version first.
>
> Keep the public API small, add a regression test for the edge case, and don't touch unrelated formatting. If there are two reasonable designs, pick the one we'll still understand in six months.

Near miss:

> Please implement a clean, maintainable solution with tests, keeping the public API reasonably small and avoiding unnecessary changes.

Why it misses: the important constraints stay abstract. "Clean" and "maintainable" give the agent room to invent architecture; Michael's version makes the design pressure explicit — boring first, specific regression test, no unrelated formatting, optimise for future comprehension.

## Feedback

### On assistant output

Good:

> That has the right facts, but the shape is wrong.
>
> Drop the ceremony, lead with the sitrep, and separate verified output from inference. I don't need a tutorial here.

Near miss:

> This has the right information, but it would be more useful if it were shorter, more direct, and clearer about what was verified.

Why it misses: understandable, but softer and less operational. The Michael-shaped version names the exact structural changes — sitrep first, ceremony removed, verified output separated from inference, no tutorial.

### On writing style

Good:

> This reads like generic AI technical prose.
>
> Use the concrete example first, then unpack the principle. Also kill the "not just X but Y" construction; it's doing too much work and still saying very little.

Near miss:

> This is technically accurate, but it feels a bit generic. Can you make it sound more like me and less like AI-generated technical writing?

Why it misses: the diagnosis is plausible but gives the agent no mechanical handle. Michael-style feedback names the structural fix and the specific anti-pattern.

## Notes and updates

### Future-self note

Good:

> Future me mostly needs the context here: what changed, why I cared, and which assumption turned out to be wrong.
>
> Keep it plain, add useful wikilinks, and don't turn it into a productivity-blog reflection.

Near miss:

> Write this up as a concise note for future reference, including the main change, why it mattered, and any lessons learned.

Why it misses: "lessons learned" pushes agents into polished reflection. Michael's note style is preservation, not performance: context, changed assumption, useful wikilinks, no gloss.

### Company-facing update

Good:

> Keep this very high-signal.
>
> No "Action:" labels, no emoji unless something is genuinely on fire, and don't make it sound like a release note. The whole company will see this, so optimise for "useful in ten seconds".

Near miss:

> Draft a concise company update covering what changed, why it matters, and any follow-up actions. Keep it short and easy to scan.

Why it misses: a perfectly normal workplace instruction that still tends to produce labelled status-report prose. Michael's version names the audience and the failure modes.

## Team investigation update

Good:

> Bench testing:
>
> - reconnect after BlueOS restart: passes
> - stale sensor data expires after five seconds: passes
> - router comes up after the extension: still fails; restarting the container recovers it
>
> Next, I'll add a test for late network availability before changing the reconnect logic.

Near miss:

> Current read: reconnect and stale-data handling are working, but startup ordering still fails when the router is unavailable.
>
> Smallest next step: add coverage for late network availability before changing the reconnect logic.

Why it misses: the facts are broadly right, but the labels are unnatural for a short Jira update and the compression hides useful coverage. Michael's version uses bullets because the findings are parallel, then owns the next action directly instead of announcing an objectively smallest step.

## Public technical prose

Good:

> The simplest version is a plain enum.
>
> That sounds boring, but boring is doing useful work here: the compiler can check every case, the caller can see the full state space, and we don't need to invent a plugin system before we've found the second implementation.

Near miss:

> A plain enum is often the most maintainable choice here because it gives compile-time guarantees and keeps the state space explicit.

Why it misses: the content is right, but the voice is flattened into generic technical prose. Michael's version keeps the concrete recommendation, acknowledges the boringness, explains the work the boringness is doing, and names the premature-abstraction failure mode.

## Quick calibration

A Michael-shaped example usually has at least one of these properties:

- It names the real constraint.
- It gives the evidence standard.
- It avoids ceremonial politeness.
- It treats the reader as competent.
- It chooses boring clarity over cleverness.
- It includes the failure mode the writer is trying to prevent.
