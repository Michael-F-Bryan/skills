# Synthetic examples (Michael)

Use these examples as calibration fixtures. They are not quotes; they are plausible Michael-shaped examples and counterexamples.

## Agent prompts

### Memory inspection

Good:

> I want to test whether the long-term memory is useful rather than just extensive.
>
> Don't ask clarifying questions first. Tell me what you know, mark each item as durable fact, likely stale, or guess, and call out anything that would be risky to rely on.

Too generic:

> Please summarise what you remember about me and include any relevant caveats.

### Repo investigation

Good:

> Check the repo state first, then trace where this value is set.
>
> I don't want a fix yet. Give me the shortest explanation that accounts for the behaviour, plus the command output or file references that support it.

Too assistant-shaped:

> Could you investigate the repository and provide a comprehensive analysis of the root cause and potential solutions?

### Implementation request

Good:

> Implement the boring version first.
>
> Keep the public API small, add a regression test for the edge case, and don't touch unrelated formatting. If there are two reasonable designs, pick the one we'll still understand in six months.

Too polished:

> Please implement a robust and maintainable solution following best practices and ensuring sufficient test coverage.

## Feedback

### On assistant output

Good:

> That has the right facts, but the shape is wrong.
>
> Drop the ceremony, lead with the sitrep, and separate verified output from inference. I don't need a tutorial here.

Too soft:

> This is helpful, but could you maybe make it a little more concise and structured?

### On writing style

Good:

> This reads like generic AI technical prose.
>
> Use the concrete example first, then unpack the principle. Also kill the "not just X but Y" construction; it's doing too much work and still saying very little.

Too abstract:

> Make this sound more authentic and less AI-generated.

## Obsidian / future-self notes

Good:

> Future me mostly needs the context here: what changed, why I cared, and which assumption turned out to be wrong.
>
> Keep it plain, add useful wikilinks, and don't turn it into a productivity-blog reflection.

Too public-facing:

> Write a reflective note about today's progress and the lessons learned.

## Company-facing updates

Good:

> Keep this very high-signal.
>
> No "Action:" labels, no emoji unless something is genuinely on fire, and don't make it sound like a release note. The whole company will see this, so optimise for "useful in ten seconds".

Too noisy:

> Create a company update with sections for what happened, why it matters, action items, and next steps.

## Engineering notes

Good:

> Current read: the failure is probably in the transcript lookup step, not the note writer.
>
> Evidence: the calendar event resolves, but the online meeting lookup returns nothing for two meetings with transcripts. Assumption: Teams is using a different meeting ID than the calendar event exposes.
>
> Smallest next step: log both IDs before changing the import flow.

Too vague:

> The transcript pipeline appears to have an issue with meeting lookup. Further investigation is needed.

## Public technical prose

Good:

> The simplest version is a plain enum.
>
> That sounds boring, but boring is doing useful work here: the compiler can check every case, the caller can see the full state space, and we don't need to invent a plugin system before we've found the second implementation.

Too generic:

> A simple enum provides a robust and maintainable approach by leveraging compile-time guarantees.

## Quick calibration

A Michael-shaped example usually has at least one of these properties:

- It names the real constraint.
- It gives the evidence standard.
- It avoids ceremonial politeness.
- It treats the reader as competent.
- It chooses boring clarity over cleverness.
- It includes the failure mode the writer is trying to prevent.
