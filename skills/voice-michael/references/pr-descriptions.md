# Pull request descriptions (Michael)

Use this reference when drafting or evaluating a pull request description in Michael's voice.

## Core philosophy

A PR description should respect the reviewer's context and attention: explain why the change exists and give just enough behavioural and design context to understand it, while leaving routine implementation detail, the diff, and CI to speak for themselves.

The description is not a changelog, implementation inventory, test report, or self-contained architecture document. Its job is to help a technically capable reviewer build the right mental model before reading the diff.

## Reader and purpose

Assume the reviewer:

- knows the repository and has access to the surrounding project context;
- can inspect the diff and commits;
- can see CI results; and
- needs the motivation, resulting behaviour, and consequential design or risk context that those sources do not communicate quickly.

Optimise for that reviewer, not a hypothetical future reader arriving without context.

## Default shape

Prefer a few compact paragraphs:

1. **Motivation** — the problem, constraint, or reason the change exists.
2. **Behaviour** — what becomes true for the user, operator, or system.
3. **Consequential support** — non-obvious supporting work only where it materially changes the design or risk.
4. **Provenance** — link the original ticket being closed when one is available.

This is a writing sequence, not a required four-section template. Combine or reorder sentences when that reads more naturally, but motivation-first is the default.

## Inclusion test

Before adding a detail, ask:

> Does this materially change how the reviewer understands the motivation, resulting product, design, or risk?

If not, leave it to the diff.

A large change set is not itself noteworthy. A coherent vertical may cross firmware, services, generated contracts, and UI without needing a defence of its file count. Conceptual coherence matters more than diff size.

### Usually include

- the problem or motivation;
- the resulting user-, operator-, or system-visible behaviour;
- a supporting refactor or removal that materially changes design or risk;
- a major migration, rollback concern, or excluded boundary when omitting it would mislead the review; and
- a link to the originating ticket, when available.

### Usually omit

- routine plumbing and generated code;
- file-by-file or subsystem-by-subsystem inventories;
- drive-by refactors unless they materially affect the resulting product;
- diff statistics or prose justifying a large but coherent change;
- stock `Scope`, `Non-goals`, `Migration`, or `Rollback` sections;
- verification checklists that duplicate CI; and
- generic claims such as “improves maintainability” without a concrete reviewer-relevant consequence.

The bar for extra explanation is high. Several substantial design or risk decisions may justify more detail; ordinary implementation complexity does not.

## Significant functionality

When the PR adds a substantial capability, briefly show how a reviewer or user encounters it. Depending on the change, that may be:

- one short usage example;
- a representative command and output;
- an embedded UI screenshot; or
- a link to a focused demonstration.

Use evidence that already exists and helps review the product. Do not manufacture screenshots, output, or manual verification theatre merely to fill the description.

## Formatting

Compact prose is the default, not a prohibition on Markdown.

Use bullets for genuinely parallel points, inline code for identifiers and commands, and links or images where they reduce explanation cost. Add headings only when the description is long enough that they improve navigation. Structure earns its place by making the description easier to skim.

## Example

Good:

> Operators need a direct indication that the vehicle has taken on water without continuing to present stale CAN data as current.
>
> This threads the leak-sensor reading from its embedded CAN node through the vehicle service to an indicator in the operator UI. The service stops publishing the reading when the sensor becomes stale.
>
> The new stream also replaces the event hub's event-specific plumbing with reusable sources and broadcast primitives.
>
> Closes [ENG-355](https://example.invalid/browse/ENG-355).

Near miss:

> ## Summary
>
> Adds leak-sensor support across the embedded node, CAN transport, vehicle service, generated API contracts, event stream, and frontend.
>
> ## Supporting changes
>
> - refactors the event hub;
> - removes the old heartbeat path;
> - updates generated code; and
> - touches 53 files across four subsystems.
>
> ## Verification
>
> - [ ] run the unit tests;
> - [ ] run the linter; and
> - [ ] confirm the UI indicator updates.

Why it misses:

> It inventories the diff instead of explaining the motivation and resulting behaviour, treats file count as reviewer context, gives routine plumbing equal weight to design, and turns CI-owned verification into unchecked prose.

## Quick check

Before finalising:

- Does the opening explain why the change exists?
- Can the reviewer quickly understand the resulting behaviour?
- Is every supporting detail material to design, risk, or the resulting product?
- Did routine implementation detail stay in the diff?
- Is the originating ticket linked when available?
- Would Markdown, a usage example, command output, or screenshot genuinely reduce review effort?
- Did I avoid duplicating CI or adding stock sections for completeness?
