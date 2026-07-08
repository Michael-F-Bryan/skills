# HTML effectiveness patterns

HTML earns its cost when it changes the reader's task from reading prose to inspecting, comparing, tuning, tracing, presenting, or exporting. If the page is just a nicer Markdown document, use Markdown or simplify the HTML.

Use these patterns as building blocks. A single artefact may combine several, but one reader job must own the first screen.

## Pattern catalogue

| Pattern | Reader job | Use when | Must include | Avoid |
|---|---|---|---|---|
| Side-by-side exploration | compare / choose | There are several plausible directions | 3–6 materially different options, visible trade-off per option, selection prompt, next step after choosing | Sequential prose that forces the reader to remember every option |
| Implementation plan surface | plan / hand off | A plan needs diagrams, risks, snippets, and verification context | milestone/timeline, data or control-flow diagram, risky code snippets, test/verification path, owner/sequence | A wall of tasks with no system shape |
| Annotated diff | review | Code changed and risk needs targeted review | file jump links, severity labels, margin/inline notes near relevant diff hunks, test evidence, review focus | Raw patch dump or decorative syntax highlighting |
| PR write-up | review / approve | Reviewers need motivation and safe focus areas | why, before/after, file/module tour, risks, rollout/fallback, tests, reviewer prompts | Repeating the commit log |
| Module map | understand / trace | A package or subsystem is unfamiliar | boxes/arrows, entry points, hot path, boundaries, failure path where relevant | Architecture art with unlabelled arrows |
| Design token sheet | inspect / copy | A visual system or component library is under review | swatches, type scale, spacing examples, copyable token values, accessibility notes | Screenshot-only design docs |
| Component contact sheet | inspect / compare | Variants, states, sizes, or themes matter | all meaningful states side-by-side, labels, disabled/error/focus states, notes on use | One polished happy-path component |
| Tuning sandbox | tune / feel | Motion, layout, prompt, colour, timing, or parameters need adjustment | live preview, controls for real variables, current value display, reset, copy/export selected parameters | Controls that do not affect the output |
| Clickable flow | feel / validate | A screen sequence or interaction needs rough validation | linked screens/states, obvious current state, caveat about fidelity, notes on what is being tested | Productising the throwaway prototype |
| SVG figure sheet | teach / publish | Diagrams or article figures need visual iteration | editable inline SVG, labels, copy/export path or clear embedding notes, consistent style | Raster-only images when vector structure matters |
| Annotated flowchart | trace / operate | A process, pipeline, or incident path has branches/failures | labelled steps, timings/owners where useful, failure paths, click/disclosure for details | Straight-line diagrams that hide errors |
| Deck HTML | present | The artefact will be walked through live | keyboard navigation, slide titles with takeaways, first slide answer, appendix/detail path | A long scrolling report pretending to be slides |
| Report surface | report / skim | Status, research, incident, or weekly work needs uptake | headline read, timeline or chart, confidence/evidence, owners, follow-ups, links to evidence | Colourful dashboard without a next move |
| Custom editor | edit-export | The reader must sort, tag, tune, rewrite, triage, or curate data | task-specific UI, constraints/warnings, counts/validation, copy/export output, inspected export sample | Generic CRUD UI or interaction with no export loop |

## First-screen rule

The hero is not automatically navigation. Use the first screen for the highest-value reader action:

| Hero pattern | Use when | Avoid |
|---|---|---|
| Mode recommender | The reader/agent needs to choose an artefact shape | Duplicating a table of contents |
| Live proof | The page argues HTML can do something Markdown cannot | Static marketing cards |
| Input capture | A short prompt/config can generate useful output | Asking for data that does nothing |
| Before/after | The value is best shown by contrast | Two fake examples with no decision |
| Diagnostic console | The reader must classify state or risk | Decorative dashboard chrome |
| Tiny editor/export | The loop closes by copying a result back | Interactions with no export |

If there is already a persistent table of contents, do not put another section-jump nav in the hero. Make the hero earn its space by producing orientation, choice, demonstration, or output.

## Export contract for interactive artefacts

Before building any stateful or manipulative page, write the export contract:

```markdown
- Task:
- User-manipulated fields/buckets:
- Export format: JSON / Markdown / prompt / diff / copied CSS tokens
- Export ordering:
- One sample exported item:
```

The exported output is part of the artefact. Verify it by exercising controls, copying/exporting, and inspecting the result.

## Multi-artefact workflows

For exploratory or implementation work, a web of small HTML files can be better than one giant page:

1. **Exploration board:** side-by-side options or experiments.
2. **Selected direction:** why this path won, what was rejected, assumptions.
3. **Implementation plan:** timeline, system/data flow, risky snippets, test path.
4. **Verification/review aid:** annotated diffs, module maps, evidence, reviewer prompts.
5. **Handoff index:** links to the above, current status, and what the next agent/human should read first.

Keep each artefact honest about its job. Do not merge everything into a dashboard-shaped junk drawer.

## Checks

- Can the reader do something useful before scrolling?
- Is there exactly one primary first-screen interaction or decision?
- Does the first screen avoid duplicating sticky/local navigation?
- Does every interaction have a visible state change and copy/export when appropriate?
- For custom editors, has exported output been copied and inspected?
- Does the page still read when JavaScript is unavailable?
- Is the HTML surface doing something Markdown could not do as clearly?

## Inspiration notes

Thariq Shihipar's HTML-effectiveness examples show the point: HTML artefacts work because they turn reading into spatial comparison, live tuning, annotated inspection, diagrams, decks, reports, and custom editors. The page should demonstrate that thesis rather than decorate it.
