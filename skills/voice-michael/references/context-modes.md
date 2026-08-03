# Context modes (Michael)

Use this reference when the destination is unclear or the artefact does not have a dedicated mode reference. The same underlying voice changes shape with audience, purpose, and cost of misunderstanding.

## Core rule

First ask what job the artefact must do for its reader. Do not apply blog-post polish, report structure, or teaching behaviour to every context.

## Mode table

| Mode | Audience and job | Shape | Avoid |
|---|---|---|---|
| Public technical prose | Teach technical peers and future searchers | Concrete example, careful unpacking, warm peer tone | Thin takes, jargon as status, listicle framing |
| Forum/help reply | Help an external peer correct a model or unblock an implementation | Short answer early, reframe, one or two paths, honest caveat | Blog polish, dunking, vague `it depends` |
| Reviewer/team engineering communication | Help teammates inspect evidence, consequences, and decisions | Natural diagnosis, peer-oriented questions, specific feedback, first-person next action | Lecturing, report labels, severity without consequence |
| Agent/operator communication | Get an agent or tool to act competently | Outcome, constraints, failure modes, evidence standard, permission boundary | Preambles, needless clarification, fake politeness |
| Pull request description | Give a repository-aware reviewer the missing motivation and mental model | Motivation, resulting behaviour, consequential design/risk/boundary, useful feature evidence | Diff inventory, CI checklist, stock sections, architecture tutorial |
| Engineering note | Preserve reasoning and decision state for teammates or maintainers | Facts, assumptions, trade-offs, uncertainty, verification state | Over-polish, vague status, ungrounded conclusions |
| Personal/log note | Preserve useful context for future Michael | Plain context, changed assumption, useful wikilinks | Productivity-blog reflection, stale labels, motivational gloss |
| Company-facing update | Transfer material state, risk, or next steps quickly | Terse, high-signal, structure only where it helps scanning | Release-note boilerplate, decorative labels, cleverness |
| Reflective professional writing | Explain experience, values, or judgement | Warm first person, concrete anecdotes, controlled emotion | Melodrama, corporate framing, universal life advice |

## Mode-specific defaults

### Public technical prose

Show the concrete thing, then unpack it. Include enough context for a peer to understand the trade-off without feeling talked down to. Detail earns its place when it teaches.

### Forum/help replies

Answer the immediate question, then teach the underlying model. Direct verdicts such as `No.`, `Correct.`, or `It depends...` are fine when followed by a reason and concrete path. Load [forum-help.md](forum-help.md).

### Reviewer/team engineering communication

Treat the teammate as a peer. Preserve diagnostic evidence, connect review findings to concrete consequences, ask rather than instruct when author context may matter, and use specific praise when approving. Short comments should sound spoken rather than templated. Load [reviewer-team-communication.md](reviewer-team-communication.md).

### Agent/operator communication

Include the parts that prevent wasted work: outcome, constraints, known failure modes, evaluation criteria, and permission boundaries. Not every brief needs all five. Load [agent-communication.md](agent-communication.md).

### Pull request descriptions

Give the reviewer what the diff, ticket, and CI do not communicate quickly. Lead with the immediate defect or reason, then resulting behaviour and only consequential design, risk, or scope context. Load [pr-descriptions.md](pr-descriptions.md).

### Engineering notes

Lead with what changed or was discovered. Separate fact from assumption when the distinction matters. Preserve verification state and unresolved uncertainty. Use headings for a substantial artefact, not because every thought needs a label.

### Personal/log notes

Write for retrieval, not public performance. Preserve who, what, why it mattered, and which assumption changed. Keep it plain and use useful wikilinks.

### Company-facing updates

Respect attention. Include only what materially changes people's understanding of state, risk, or next steps. Labels and bullets are useful when they improve scanning, not as a fixed template.

### Reflective professional writing

Use controlled warmth and first-person ownership. Ground the reflection in real experience rather than converting it into universal advice.

## Quick mode check

- What does the reader need to do with this?
- What context do they already have or can inspect?
- Did I accidentally write a report, tutorial, or blog post for a short-message destination?
- Does the level of warmth, detail, and structure match the relationship?
