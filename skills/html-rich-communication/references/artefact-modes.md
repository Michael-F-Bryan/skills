# Artefact modes

Pick the mode by reader job. A single deliverable may have secondary layers, but one mode must own the first screen.

## Decision brief

Use when the reader must approve, choose, fund, defer, or stop.

Required: takeaway title, recommendation, decision requested, options/trade-offs, evidence confidence, risks/mitigations, owner, review gate, guardrails, and kill/revisit condition.

For approval/funding decisions, the first screen must state the recommendation, approval requested, cost/scope, owner, review gate, guardrails, and kill/revisit condition.

## Design review

Use when the reader must critique architecture or design.

Required: context and scope, goals and plausible non-goals, system shape/boundaries, interface contracts, design decisions with alternatives and accepted risks, validation state, and open questions.

Move user-guide steps, UI best-practice notes, and reference tables out of the core unless they directly support the review.

Normal authentication, generic form-label guidance, and operator how-to steps belong in appendix, linked user guide, or cut unless the design decision under review is security, authorisation, or UI interaction.

## Technical explainer

Use when the reader must understand how something works.

Required: mental model, path/flow diagram, annotated code/config snippets, gotchas, FAQ or glossary.

## User guide / operator doc

Use when the reader must perform a task.

Required: prerequisites, steps, expected results, safety/rollback, troubleshooting, and doc test or walkthrough evidence where possible.

## Reference / pathfinder

Use when lookup or navigation is the job.

Required: strong labels and information scent, grouped tables/cards, examples near the fields they explain, links to explanations or guides rather than mixing modes.

## Report / status / incident

Use when the reader must absorb state and next action.

Required: current read, confidence/evidence strength, timeline or status summary, impact, owners and follow-ups, next move, evidence on demand.

## Code review / PR aid

Use when the reader must review code safely.

Required: what changed and why, risk map, file/module tour, annotated diffs or snippets with comments next to relevant code, test plan, rollout/fallback, and where to focus review.

## Exploration fan-out

Use when the reader is choosing a direction.

Required: 3–6 materially different options, side-by-side comparison, trade-off label per option, recommendation or explicit selection prompt, and what to do after choosing.

## Prototype / design sandbox

Use when the reader must feel or tune an interaction.

Required: live example, controls for variables that matter, caveat that fidelity is limited, copy/export of selected parameters when useful.

## Custom editing interface

Use when the reader manipulates data and returns the result to the agent or repo.

Required: task-specific UI, constraints/warnings in the interface, visible counts/estimates/validation, copy/export button, and verification that exported output is correct.

## Deck

Use for meeting narrative.

Required: first slide answers the meeting question, keyboard navigation, concise slide titles with takeaways, appendix/on-demand detail.

## Dashboard / tool

Use when ongoing monitoring or exploration is the job.

Required: key metrics and state, filters/drilldowns, annotations and units near visuals, export/share if decisions are made from it.

If the user asks for a dashboard but needs approval, do not lead with dashboard language; make a decision brief and push dashboard views to appendix only.
