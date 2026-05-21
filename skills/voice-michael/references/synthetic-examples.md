# Synthetic examples (Michael)

Use these examples as calibration fixtures. They are not quotes; they are plausible Michael-shaped examples and counterexamples.

The counterexamples should be *near misses*, not straw men. A useful "too generic" example is something a competent assistant, engineer, or manager might actually write; the point is to expose the missing constraint, evidence standard, or operational judgement, not to dunk on obviously bad prose.

## Agent prompts

### Memory inspection

Good:

> I want to test whether the long-term memory is useful rather than just extensive.
>
> Don't ask clarifying questions first. Tell me what you know, mark each item as durable fact, likely stale, or guess, and call out anything that would be risky to rely on.

Near miss:

> Please summarise what you remember about me, including relevant preferences, background, and any caveats about uncertainty.

Why it misses:

> A typical person might write this because it is polite and clear enough. It still leaves the agent to choose the evaluation frame. Michael-style asks usually name the failure mode being tested — useful memory versus flattering memory, durable fact versus stale guess, safe-to-rely-on versus risky assumption.

### Repo investigation

Good:

> Check the repo state first, then trace where this value is set.
>
> I don't want a fix yet. Give me the shortest explanation that accounts for the behaviour, plus the command output or file references that support it.

Near miss:

> Investigate where this value is being set and report back with the likely cause and any options for fixing it.

Why it misses:

> This is a reasonable engineering request, but it quietly invites solution-shopping before the path is traced. Michael's version constrains sequence, evidence, and scope: check state, trace the value, do not fix yet, and cite the command output or file references.

### Implementation request

Good:

> Implement the boring version first.
>
> Keep the public API small, add a regression test for the edge case, and don't touch unrelated formatting. If there are two reasonable designs, pick the one we'll still understand in six months.

Near miss:

> Please implement a clean, maintainable solution with tests, keeping the public API reasonably small and avoiding unnecessary changes.

Why it misses:

> This is not bad engineering prose. The problem is that the important constraints are still abstract. "Clean" and "maintainable" give the agent room to invent architecture; Michael's version makes the design pressure explicit: boring first, specific regression test, no unrelated formatting, optimise for future comprehension.

## Feedback

### On assistant output

Good:

> That has the right facts, but the shape is wrong.
>
> Drop the ceremony, lead with the sitrep, and separate verified output from inference. I don't need a tutorial here.

Near miss:

> This has the right information, but it would be more useful if it were shorter, more direct, and clearer about what was verified.

Why it misses:

> A typical reviewer could write this and be understood. It is still softer and less operational than Michael's feedback. The Michael-shaped version tells the agent exactly what to change in the output structure — sitrep first, ceremony removed, verified output separated from inference, no tutorial.

### On writing style

Good:

> This reads like generic AI technical prose.
>
> Use the concrete example first, then unpack the principle. Also kill the "not just X but Y" construction; it's doing too much work and still saying very little.

Near miss:

> This is technically accurate, but it feels a bit generic. Can you make it sound more like me and less like AI-generated technical writing?

Why it misses:

> The diagnosis is plausible, but it gives the agent almost no mechanical handle. Michael-style feedback names the structural fix and the specific anti-pattern: concrete example first, principle second, remove the overworked construction.

## Obsidian / future-self notes

Good:

> Future me mostly needs the context here: what changed, why I cared, and which assumption turned out to be wrong.
>
> Keep it plain, add useful wikilinks, and don't turn it into a productivity-blog reflection.

Near miss:

> Write this up as a concise note for future reference, including the main change, why it mattered, and any lessons learned.

Why it misses:

> This is a normal note-taking request, but "lessons learned" often pushes agents into polished reflection. Michael's note style is more preservation than performance: context, changed assumption, useful wikilinks, no productivity-blog gloss.

## Company-facing updates

Good:

> Keep this very high-signal.
>
> No "Action:" labels, no emoji unless something is genuinely on fire, and don't make it sound like a release note. The whole company will see this, so optimise for "useful in ten seconds".

Near miss:

> Draft a concise company update covering what changed, why it matters, and any follow-up actions. Keep it short and easy to scan.

Why it misses:

> This is a perfectly normal workplace instruction. It still tends to produce labelled status-report prose. Michael's version calls out the audience and failure modes: whole company, ten-second usefulness, no release-note shape, no decorative labels, rare emoji.

## Engineering notes

Good:

> Current read: the failure is probably in the transcript lookup step, not the note writer.
>
> Evidence: the calendar event resolves, but the online meeting lookup returns nothing for two meetings with transcripts. Assumption: Teams is using a different meeting ID than the calendar event exposes.
>
> Smallest next step: log both IDs before changing the import flow.

Near miss:

> The failure appears to be in transcript lookup rather than note writing. The next step is to compare the meeting identifiers and adjust the import flow if needed.

Why it misses:

> This is close enough that an agent may think it passes. It does not. It collapses evidence, assumption, and recommendation into one paragraph, and it moves too quickly to changing the flow. Michael-shaped engineering notes keep the current read, evidence, assumption, and smallest next step distinct.

## Public technical prose

Good:

> The simplest version is a plain enum.
>
> That sounds boring, but boring is doing useful work here: the compiler can check every case, the caller can see the full state space, and we don't need to invent a plugin system before we've found the second implementation.

Near miss:

> A plain enum is often the most maintainable choice here because it gives compile-time guarantees and keeps the state space explicit.

Why it misses:

> The content is right, but the voice is flattened into generic technical prose. Michael's version keeps the concrete recommendation, acknowledges the boringness, explains the work that boringness is doing, and names the premature-abstraction failure mode.

## Quick calibration

A Michael-shaped example usually has at least one of these properties:

- It names the real constraint.
- It gives the evidence standard.
- It avoids ceremonial politeness.
- It treats the reader as competent.
- It chooses boring clarity over cleverness.
- It includes the failure mode the writer is trying to prevent.
