---
name: html-rich-communication
description: Use when creating a rich HTML artefact, visual brief, explainer, report, review aid, decision memo, dashboard-like page, or interactive document for a human to inspect, understand, compare, or share complex information.
---

# HTML Rich Communication

## Core principle

Use HTML when the reader's understanding depends on layout, hierarchy, diagrams, interaction, comparison, or progressive disclosure. The goal is not a prettier wall of text; the goal is to help a specific reader make sense of something complex and act on it.

Default to Markdown when a short, linear answer is clearer. Reach for HTML when the artefact must be scanned, navigated, compared, reviewed on mobile, shared, or interacted with.

## Workflow

```text
1. Lock the communication job
2. Collate source material
3. Refine the argument
4. Plan the visual/interaction surface
5. Build the HTML artefact
6. Verify as the reader, not as the author
7. Share privately unless public sharing is explicit
```

Keep the stages separate. Do not let the HTML implementation start until the audience, reader job, source material, and visual plan are explicit.

## 1. Lock the communication job

Write a short artefact brief before creating the page:

- **Audience:** who will read it, what they know, and what they care about.
- **Reader job:** decide, understand, verify, compare, operate, learn, or edit/export.
- **Primary question:** the one question the first screen must answer.
- **Reading context:** mobile/desktop, time pressure, meeting use, offline/private/public.
- **Action:** the concrete next decision, review action, or exported result.
- **Privacy posture:** local-only, secret-link, internal, or public.

Use `references/audience-patterns.md` when the audience matters or is mixed.

## 2. Collate source material

Create a working folder near the source repo or in the user's requested location. Save:

```text
_working/<topic>/
  README.md                  # brief, constraints, status
  source-notes.md             # facts, excerpts, links, file paths
  prompts/                    # prompts given to sub-agents
  agents/                     # sub-agent outputs
  visual-plan.md              # layout, elements, interactions
  final/<name>.html            # final artefact
```

Read files and sources directly; do not rely on chat memory. If sub-agents are used, require named output files and read them back before trusting their summaries.

## 3. Refine before designing

Produce a simplified content brief before visual planning:

- lead with the answer/recommendation, not context archaeology;
- cut material that does not help the reader's job;
- separate facts, assumptions, judgement, risks, and open questions;
- decide which details should be visible by default and which belong behind `<details>`;
- make mobile-first structure explicit if the page may be read on a phone.

For decision support, prefer: **problem → judgement → options → evidence → risks → staged next move**.

For technical review, prefer: **system shape → change surface → evidence → failure paths → tests → open risks**.

## 4. Plan the visual surface

Create `visual-plan.md` before writing HTML. Choose elements because they clarify the reader's task.

Start with the default stack:

1. Hero thesis / reader decision.
2. Question-based navigation or sticky section nav.
3. 3–7 stacked cards for the main argument.
4. One structure diagram or map.
5. One staged path, decision gate, comparison, or risk/evidence visual.
6. Progressive disclosure for evidence and caveats.
7. One next-action block.

Mobile navigation needs deliberate design. A sticky horizontal chip nav is not automatically mobile-friendly: it can hide off-screen links, consume vertical space, and land anchors awkwardly under the sticky bar. Prefer wrapped question cards, a compact jump menu, bottom “next decision” links, or a visibly scrollable nav with tested anchor offsets.

For decision artefacts, separate evidence types visibly: **source fact**, **assumption**, **judgement**, and **unknown**. This helps readers trust the recommendation without mistaking confident presentation for certainty.

Use `references/visual-elements.md` for the element palette and `references/chart-routing.md` when numbers or relationships need visualisation.

## 5. Build native-first HTML

Prefer a single self-contained `.html` file:

- inline CSS;
- semantic HTML (`main`, `section`, headings, lists, tables when appropriate);
- native `<details>/<summary>` for progressive disclosure;
- inline SVG only for simple, controlled visuals;
- responsive CSS with a 375px mobile sanity check;
- print styles when the artefact may be saved as PDF;
- no external fonts, images, scripts, or CDNs unless explicitly justified.

### Image generation

Use image generation when a static image communicates better than LLM-authored SVG: hero scenes, physical-world metaphors, field-style sketches, domain illustrations, or visual anchors.

When using generated images, save beside the artefact and record:

- target path;
- prompt;
- aspect ratio;
- caption/alt text;
- role in the document;
- fallback if generation fails.

### CDN dependencies

Only use a CDN dependency when it unlocks high-value capability that would be difficult or fragile natively, such as Mermaid for complex flow/sequence/state diagrams, Chart.js for responsive charts, D3/Observable Plot for bespoke data visualisation, or Leaflet/MapLibre for real maps.

If a CDN is used, pin the version and document why in the working README. Avoid CDNs for private/offline artefacts unless the user accepts the trade-off.

## 6. Verify as the reader

Before claiming completion, run a reader-style verification:

- open the HTML in a browser, not just as text;
- inspect at mobile width around 375px and a desktop width;
- check that the first screen answers the primary reader question;
- click every nav link and record whether each target lands cleanly below any sticky header;
- open every `<details>` disclosure at mobile width and desktop width;
- check no critical meaning is carried only by colour, hover, animation, or tiny labels;
- check links, copy/export controls, and interactive widgets;
- check the file is self-contained unless dependencies were approved;
- check executive decision artefacts state exactly what approval authorises: scope, owner/next owner, review gate, and kill condition;
- check privacy: no accidental public upload, sensitive paths, or wrong audience framing.

For generated files, list the directory and read back key artefacts before reporting paths.

## Common failure modes

| Failure | Correction |
|---|---|
| Beautiful but wrong audience | Re-lock audience/job and regenerate the brief before touching CSS. |
| Markdown thinking inside HTML | Use layout, hierarchy, comparison, disclosure, and diagrams deliberately. |
| Visual garnish | Remove elements that do not answer a reader question. |
| SVG spaghetti | Use simpler diagrams, Mermaid if justified, or generated/static images. |
| Mobile added last | Carry mobile-first constraints through brief, visual plan, and implementation. |
| Hidden uncertainty | Use assumption ledgers, evidence chips, and known/unknown panels. |
| Public-by-accident sharing | Default to local files or secret links for work/project artefacts. |
| Sub-agent stalls before producing artefact | Constrain prompts: read named inputs, write the main output first, cap tool calls, then write notes and verify. |
| Mobile nav technically works but feels hidden | Prefer wrapped navigation, question-card TOCs, or next-links; if using horizontal sticky nav, verify link visibility and anchor landing. |
| Executive recommendation lacks authority shape | State what approval authorises: scope, owner, review gate, guardrails, and kill condition. |

## Prompt pattern for sub-agents

Use file-backed handoffs when quality matters:

1. **Collation agent:** read sources, extract facts, save `source-notes.md`.
2. **Refinement agent:** turn source notes into a concise audience-specific brief.
3. **Visual planning agent:** choose layout, elements, disclosure, and dependency policy.
4. **HTML agent:** implement exactly from the brief and visual plan.
5. **Review agent:** open in browser, interact with the page, and critique from the audience's perspective.

See `templates/subagent-prompts.md` for copyable prompts.
