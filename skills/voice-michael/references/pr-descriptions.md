# Pull request descriptions (Michael)

**Scope:** drafting or evaluating a pull request description. For review comments on someone else's PR, use [team-communication.md](team-communication.md).

## Cognitive job

Help a technically capable, repository-aware reviewer build the right mental model before reading the diff. Supply what the ticket, code, commits, and CI do not communicate quickly.

A PR description is not a changelog, implementation inventory, test report, or self-contained architecture document.

Treat every supplied fact as candidate context, not mandatory prose. Standard tests, schema validation, and ordinary CI results stay out unless an unusual failure, manual verification result, or review risk makes them material.

## Positive recipe

Use the parts that earn their place; this is a sequence, not a section template.

1. **Motivation** — Name the immediate defect, constraint, or reason and its consequence. Stop when the reviewer can infer the need.
2. **Resulting behaviour** — Say what becomes true for the user, operator, or system.
3. **Decision ownership** — Identify the layer that owns consequential behaviour when this tells the reviewer where to inspect the logic. Do not narrate every transport hop.
4. **Consequential design or risk** — Give a substantial internal architecture change one compact sentence. Describe the changed design model, not diff size.
5. **Feature evidence** — For substantial functionality, show one real command, output, screenshot, or focused demonstration when it helps a skimming reviewer understand the product.
6. **Material boundary** — State a migration, deployment, rollback, or excluded scope boundary when omission could create a footgun or materially overstate where the feature applies.
7. **Provenance** — Link the originating ticket when available.

Most PRs need only the first two items and the ticket link.

## Inclusion decisions

| If a detail... | Then... |
|---|---|
| names the defect and consequence | include it early |
| merely restates a need already implied by that consequence | omit it |
| locates consequential logic in the owning layer | include it compactly |
| lists components the data passes through | leave it to the diff |
| materially changes the internal architecture or risk model | give it one compact sentence |
| reports routine plumbing, generated code, or file count | leave it to the diff |
| shows what a significant new feature actually looks like | include the real artefact |
| explains standard test commands or duplicates CI | omit it |
| prevents a misleading deployment or scope assumption | include it |
| records a stock non-goal with no reviewer consequence | omit it |

A large change set is not itself noteworthy. A coherent vertical may cross firmware, services, contracts, and UI without needing a defence of its file count.

## Formatting

Compact prose is the default. Use bullets for genuinely parallel points, inline code for identifiers and commands, and links or images when they reduce explanation cost. Add headings only when the description is long enough to need navigation.

Structure should help a reviewer skim; it should not make every detail look equally important.

## Calibrated examples

### Behaviour and ownership

> Operators keep seeing the last leak-sensor value after CAN updates stop, which makes stale data look current.
>
> The operator UI now displays the leak sensor as unavailable after five seconds without an update, while the vehicle service continues yielding readings as they arrive.
>
> The event path now uses reusable sources and broadcast primitives instead of event-specific plumbing.
>
> Closes [SF-355](https://example.invalid/browse/SF-355).

Why it works:

- the opening states the defect and consequence without restating the inferred operator need;
- the second paragraph locates the staleness decision in the UI without narrating the transport path;
- the architecture change earns one sentence because it materially changes the internal design; and
- routine files, generated contracts, and CI remain in their proper places.

### Feature evidence and deployment boundary

> Vehicle endpoints are repeated across `buttctl` invocations, which makes routine commands error-prone.
>
> This adds named TOML profiles selected with `--profile`. Explicit flags still override profile values, and invalid profiles fail before opening a network connection.
>
> Profiles are only consumed by `buttctl`; long-running services keep their existing environment-based configuration.
>
> ```console
> $ buttctl --profile zoda status
> Using profile "zoda" (10.9.3.4)
> ```
>
> Closes [SF-197](https://example.invalid/browse/SF-197).

The command shows the feature to a skimming reviewer. The service-configuration sentence prevents a deployment footgun. A `Testing` section explaining familiar commands would add noise instead.

## Common misses

- Opening with a feature inventory instead of the problem.
- Repeating the same motivation as defect, user need, and value statement.
- Attributing behaviour to the wrong layer.
- Narrating every subsystem in the vertical.
- Treating file count as architecture context.
- Giving routine cleanup the same weight as a consequential redesign.
- Adding stock `Summary`, `Scope`, `Non-goals`, `Migration`, `Rollback`, or `Verification` sections for completeness.
- Manufacturing screenshots, output, or manual test theatre.
- Generic claims such as `improves maintainability` without a reviewer-relevant consequence.

## Final check

- Can the reviewer see why the change exists and what becomes true?
- Did I trust them to infer what the stated consequence already implies?
- Did I locate consequential logic without narrating the diff?
- Does each supporting detail change their understanding of design, risk, product, or deployment?
- Would a real example materially help a skimming reviewer?
- Did standard tests and CI stay out of the prose?
- Is the ticket linked?
