# Architecture review sources

The architecture-review procedure adapts ideas from Matt Pocock’s `mattpocock/skills` repository, under the MIT licence. The core code-like-michael skill governs engineering judgement and testing policy; this adaptation does not endorse every upstream rule.

Pinned source revision: `49dd158d1076134a641b33efb035946536778336`.

- [Improve Codebase Architecture](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/improve-codebase-architecture/SKILL.md): scoped exploration, architectural friction, evidence-backed candidates and progressive design exploration.
- [Codebase Design](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/codebase-design/SKILL.md): depth as caller leverage, interface obligations, locality and the deletion thought experiment.
- [Deepening](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/codebase-design/DEEPENING.md): dependency-aware testing and moving coverage to useful interfaces.
- [Design It Twice](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/codebase-design/DESIGN-IT-TWICE.md): contrasting interface designs against the same constraints.

Copyright (c) 2026 Matt Pocock. See the [complete upstream MIT licence](licenses/mattpocock-skills-MIT.txt). Adapted with Hermes and Claude Fable for Michael F. Bryan.

The skills.sh preview is not the complete source. At this revision the upstream workflow uses an HTML candidate report followed by an interactive decision loop; its marketplace summary still mentions GitHub issue RFCs. Neither output mechanism is an automatic requirement of this adaptation.

## Deliberate differences from upstream

- **No mandatory HTML report with CDN assets.** Conversation or plain text is the default; richer artefacts are conditional on usefulness and scope.
- **No exact-vocabulary mandate or ban on "boundary".** The project's language and the core skill's existing terminology remain valid.
- **No adapter-count threshold for seams.** Ownership, lifetime control, actual variation and meaningful encapsulation govern the decision.
- **No automatic deletion of old unit tests.** Retirement requires demonstrated coverage of the protected behaviour and remains a visible part of the change.
- **No mandatory secondary skills, sub-agents, glossary or ADR writes.** Existing project knowledge informs a review; creating working artefacts or publishing changes requires appropriate scope and authority.
- **Deepening is a lens, not the whole architecture review.** Material system risks determine the review's focus, and small authorised changes do not require an interactive design ceremony.
