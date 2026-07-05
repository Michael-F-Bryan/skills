# Michael Brand Pack

**Operator Notes** is a professional artefact system for Michael F. Bryan / Michael-F-Bryan. It is designed for HTML artefacts, technical reports, project write-ups, decision briefs, architecture notes, incident reviews, and rich communication outputs.

## Brand concept

> **Operator-grade communication:** field notes refined into decision briefs.

## Core rule

> **Make the work legible. Make the next move obvious.**

## What this folder contains

```text
michael-brand-pack/
├── SKILL.md
├── README.md
├── docs/
│   ├── brand-guide.md
│   ├── voice-and-tone.md
│   ├── accessibility.md
│   └── component-patterns.md
├── css/
│   ├── tokens.css
│   └── operator-notes.css
├── templates/
│   ├── briefing.html
│   ├── decision-record.html
│   └── technical-report.html
├── examples/
│   ├── system-handoff.html
│   └── decision-brief.html
├── components/
│   ├── status-strip.html
│   ├── current-read.html
│   ├── recommendation.html
│   ├── risk-block.html
│   ├── trade-off-table.html
│   └── next-actions.html
└── diagrams/
    └── diagram-style.md
```

## Intended feel

The reader should feel:

- “This person understands the system.”
- “The important parts are visible.”
- “The recommendation is clear.”
- “The artefact is useful enough to forward.”
- “I can act on this.”

## Quick start

Use `templates/briefing.html` for most artefacts.

Use `templates/decision-record.html` for decisions, ADRs, technical recommendations, and trade-off analysis.

Use `templates/technical-report.html` for deeper reports, investigations, system handoffs, or postmortems.

The CSS files are split into:

- `css/tokens.css` — colours, spacing, typography, radius, and status tokens.
- `css/operator-notes.css` — complete layout and component styling.

For standalone artefacts, either link both CSS files or paste them into a single `<style>` block.

## Default identity

Preferred public identity:

```text
Michael F. Bryan · Michael-F-Bryan
```

Optional system label:

```text
Operator Notes
Field notes refined into decision briefs.
```
