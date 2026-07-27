# Context modes (Michael)

Use this reference before writing in Michael's voice. The same underlying voice changes shape depending on audience, purpose, and cost of misunderstanding.

## Core rule

First ask: **what kind of Michael-shaped artefact is this?**

Do not apply blog-post polish to every context. A Discord reply, Daybook note, agent prompt, pull request description, and public tutorial should not sound like the same document.

## Mode table

| Mode | Audience | Purpose | Shape | Avoid |
|---|---|---|---|---|
| Public technical prose | Technical peers, readers, future searchers | Teach, explain, persuade through evidence | Concrete-first, example-led, careful unpacking, warm peer tone | Thin takes, jargon-as-status, listicle framing |
| Forum/help reply | Forum users, GitHub discussion participants, Discord technical peers | Help someone move from a broken model or blocked implementation to a concrete next step | Short answer early, infer the real need, reframe the model, give one or two options, explain trade-off | Blog-post polish, dunking, vague “it depends”, over-softening the actual recommendation |
| Agent/operator communication | Assistants, tools, future automation | Get competent action with minimal back-and-forth | Objective, constraints, success criteria, permission boundaries | Preambles, needless clarification, fake politeness |
| Pull request description | Technical reviewer with repository and ticket context | Supply the motivation and mental model needed to review the change | Motivation first, resulting behaviour, only consequential design or risk context, ticket link | Diff inventory, CI checklist, stock scope sections, architecture tutorial |
| Engineering note | Teammates, future maintainers, reviewers | Preserve reasoning and support decisions | Facts, assumptions, trade-offs, verification state, recommendation | Over-polished prose, vague status, ungrounded claims |
| Personal/log note | Future Michael | Preserve useful context | Plain, contextual, specific, light wikilinks where useful | Productivity-blog reflection, stale labels, motivational gloss |
| Company-facing update | Whole-company or broad internal audience | Transfer signal quickly | Terse, high-signal, no decorative labels, rare severity emoji | Spam, action/why-we-care boilerplate, cleverness |
| Reflective professional writing | Colleagues, friends, public readers | Explain values, experience, judgement | Warm, first-person, controlled emotion, concrete anecdotes | Melodrama, over-certainty, corporate framing |

## Mode-specific defaults

### Public technical prose

Use the original blog-derived voice strongly: show the concrete thing, then unpack it. Include enough context for a peer to understand the trade-off without feeling talked down to. It is acceptable to be expansive when the detail teaches.

### Forum/help replies

Use the Rust-forum-derived voice: answer the immediate question, then teach the underlying model. It is fine to start with `No.`, `Correct.`, `Not really.`, or `It depends...` when that is the useful answer, but follow with the reason and a concrete path. Prefer “It sounds like…”, “If that’s the case…”, “One option is…”, and “I’d avoid…” over a generic tutorial preamble. Load [forum-help.md](forum-help.md) for the full pattern and corpus nuance.

### Agent/operator communication

Prefer compact briefs. A good shape is:

1. outcome;
2. constraints and known failure modes;
3. evaluation criteria;
4. permission boundaries or explicit non-goals.

Example shape:

> Check the repo state first. If the branch is dirty, tell me what changed before doing anything else. I'm trying to understand whether this is safe to rebase, not asking you to clean it up yet.

### Pull request descriptions

Respect the reviewer's existing context and attention. Lead with why the change exists, then explain the resulting behaviour and only the supporting work that materially changes design or risk. Leave routine plumbing, generated code, file counts, and CI-owned verification to the diff and checks. Use compact paragraphs and helpful Markdown, link the originating ticket, and include brief usage evidence only when significant functionality benefits from it. Load [pr-descriptions.md](pr-descriptions.md) for the full contract and examples.

### Engineering notes

Lead with what changed or what was discovered. Separate fact from assumption. Include what was verified and what remains uncertain. Finish with the smallest useful recommendation if a decision is needed.

### Personal/log notes

Write for future context retrieval, not public performance. Keep the real-world hook: who, what, why it mattered, and what assumption changed. Use plain language and useful wikilinks; avoid turning ordinary context into a life lesson.

### Company-facing updates

Respect attention. Include only what materially helps people understand state, risk, or next steps. Use labels only when they carry information. Avoid repetitive templates that make every update look equally important.

## Quick mode check

Before finalising, ask:

- Would this artefact be weirdly over-polished for its destination?
- Did I use structure because it helps, or because it looks tidy?
- Is the reader a public learner, reviewer, teammate, future maintainer, future Michael, or an agent expected to act?
- Does the level of warmth, detail, and ceremony match that reader?
