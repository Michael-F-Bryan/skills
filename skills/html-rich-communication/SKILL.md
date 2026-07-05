---
name: html-rich-communication
description: Use when creating a rich HTML artefact, visual brief, explainer, report, review aid, decision memo, dashboard-like page, or interactive document for a human to inspect, understand, compare, or share complex information.
---

# HTML Rich Communication

## Core principle

Use HTML when the reader's understanding depends on layout, hierarchy, diagrams, interaction, comparison, or progressive disclosure. The goal is not a prettier wall of text; the goal is to help a specific reader make sense of something complex and act on it.

Default to Markdown when a short, linear answer is clearer. Reach for this skill when the artefact must be scanned, navigated, compared, reviewed on mobile, shared, or interacted with.

## Workflow

```text
1. Lock the communication job
2. Collate source material
3. Refine the argument
4. Plan the visual/interaction surface
5. Scaffold React app in _working/
6. Implement the artefact
7. Bundle to a single HTML file
8. Verify as the reader, not as the author
9. Share (local file; secret gist + GistPreview when a link is needed)
```

Keep the stages separate. Do not scaffold or implement until the audience, reader job, source material, and visual plan are explicit.

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

Create a working folder per **RELATED SKILL:** `working-docs`. Save:

```text
_working/<topic>/
  README.md                  # brief, constraints, status
  source-notes.md            # facts, excerpts, links, file paths
  prompts/                   # prompts given to sub-agents
  agents/                    # sub-agent outputs
  visual-plan.md             # layout, elements, interactions
  app/                       # React project (scaffolded in step 5)
  final/
    bundle.html              # bundled self-contained artefact
```

Read files and sources directly; do not rely on chat memory. If sub-agents are used, require named output files and read them back before trusting their summaries.

Confirm `_working/` is gitignored before writing (`git check-ignore -v _working/<topic>/README.md`).

## 3. Refine before designing

Produce a simplified content brief before visual planning:

- lead with the answer/recommendation, not context archaeology;
- cut material that does not help the reader's job;
- separate facts, assumptions, judgement, risks, and open questions;
- decide which details should be visible by default and which belong behind progressive disclosure;
- make mobile-first structure explicit if the page may be read on a phone.

For decision support, prefer: **problem → judgement → options → evidence → risks → staged next move**.

For technical review, prefer: **system shape → change surface → evidence → failure paths → tests → open risks**.

## 4. Plan the visual surface

Create `visual-plan.md` before scaffolding. Choose elements because they clarify the reader's task.

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

Record component choices in the visual plan: shadcn/ui primitives (Card, Tabs, Accordion/Collapsible, Badge, etc.), chart library if needed, and any generated images with target paths under `app/src/assets/` or `app/public/`.

If the repo's `AGENTS.md` names a project styling skill, note it in the visual plan and plan to apply its typography, colours, and layout rules during implementation.

Use `references/visual-elements.md` for the element palette and `references/chart-routing.md` when numbers or relationships need visualisation.

## 5. Scaffold the React app

Do **not** hand-author a standalone `.html` file. Scaffold a React project inside the working folder, then bundle it in step 7.

From `_working/<topic>/`:

```bash
bash <skill-root>/scripts/init-artifact.sh app
cd app
```

`<skill-root>` is the directory containing this skill's `SKILL.md` (e.g. `skills/html-rich-communication` in this repo).

**Stack:** React 18 + TypeScript + Vite + Tailwind CSS + shadcn/ui (40+ components pre-installed)

The init script creates `app/` with path aliases (`@/`), Radix/shadcn theming, and Node 18+ compatibility. Requires Node 18+ and pnpm (installed automatically if missing).

## 6. Implement the artefact

Edit the generated React app to match the brief and visual plan. Primary entry: `app/src/App.tsx` and supporting components under `app/src/`.

### Design guidelines

**Project styling takes precedence.** Before choosing colours, typography, spacing, or component styling, read the repo's `AGENTS.md` (or equivalent agent instructions). If it names a default styling or design skill — e.g. brand guidelines, theme factory, frontend-design — read and follow that skill for the visual language. The shadcn/Tailwind scaffold from `init-artifact.sh` is a technical baseline only; do not treat its default theme as the design system when the project specifies otherwise.

If no project styling skill is stipulated, avoid “AI slop”: excessive centered layouts, purple gradients, uniform rounded corners everywhere, and Inter as the default font. Match typography, spacing, and hierarchy to the audience and reading context.

### Implementation conventions

- **Layout:** semantic structure via components; responsive Tailwind with a 375px mobile sanity check.
- **Progressive disclosure:** shadcn Accordion, Collapsible, or Tabs — not hover-only reveals.
- **Navigation:** test anchor offsets with any sticky header; verify mobile link visibility.
- **Charts/diagrams:** prefer npm packages (e.g. recharts, mermaid) bundled into the artefact — not runtime CDN loads.
- **Print/PDF:** add print styles when the artefact may be saved as PDF.
- **Images:** put assets in `app/src/assets/` or `app/public/`; they are inlined at bundle time.

### Image generation

Use image generation when a static image communicates better than code-authored SVG: hero scenes, physical-world metaphors, field-style sketches, domain illustrations, or visual anchors.

When using generated images, save under `app/src/assets/` or `app/public/` and record in the working README:

- target path;
- prompt;
- aspect ratio;
- caption/alt text;
- role in the document;
- fallback if generation fails.

### Local preview (optional)

During development, `pnpm dev` in `app/` is fine. Do not delay bundling and delivery while polishing in dev mode unless the user asks.

## 7. Bundle to single HTML

From `app/` (project root with `package.json` and `index.html`):

```bash
bash <skill-root>/scripts/bundle-artifact.sh
```

This produces `app/bundle.html` — a self-contained file with all JavaScript, CSS, and assets inlined via Parcel + html-inline.

Copy or move the deliverable to the working folder output:

```bash
cp bundle.html ../final/bundle.html
```

Verify (section 8), then share locally or via secret gist + GistPreview (section 9). The React source in `app/` is the editable working copy; `final/bundle.html` is the deliverable.

## 8. Verify as the reader

Before claiming completion, run a reader-style verification on `final/bundle.html`:

- open the HTML in a browser, not just as text;
- inspect at mobile width around 375px and a desktop width;
- check that the first screen answers the primary reader question;
- click every nav link and record whether each target lands cleanly below any sticky header;
- open every disclosure/tab/filter at mobile and desktop widths;
- check no critical meaning is carried only by colour, hover, animation, or tiny labels;
- check links, copy/export controls, and interactive widgets;
- check the file is self-contained (no runtime CDN dependencies);
- check executive decision artefacts state exactly what approval authorises: scope, owner/next owner, review gate, and kill condition;
- check privacy: no accidental public upload, sensitive paths, or wrong audience framing.

List `_working/<topic>/`, read back `README.md` and `final/bundle.html`, and confirm paths exist before reporting completion.

Defer heavy browser automation until after presenting the artefact unless the user requests upfront testing or something is clearly broken.

## 9. Share the artefact

Default delivery is the local `final/bundle.html` path. When the user needs a link they can open in a browser — especially on mobile or outside the agent session — publish via **secret gist + GistPreview**:

1. Create a secret gist with `gh gist create` (no `--public`).
2. Build the rendered preview URL: `https://gistpreview.github.io/?<gist_id>/<filename>` ([GistPreview](https://gistpreview.github.io/)).
3. Verify raw and preview URLs return `200` before reporting.
4. Record gist id and both URLs in `_working/<topic>/README.md`.

Renaming the upload to `index.html` simplifies the preview URL (filename can be omitted). See `references/secret-gist-publishing.md` for commands, verification curls, and what to do if a gist was created public by mistake.

Only use public gists when the user explicitly wants discoverable sharing.

## Common failure modes

| Failure                                        | Correction                                                                                                                               |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Beautiful but wrong audience                   | Re-lock audience/job and regenerate the brief before touching components.                                                                |
| Markdown thinking inside HTML                  | Use layout, hierarchy, comparison, disclosure, and diagrams deliberately.                                                                |
| Visual garnish                                 | Remove elements that do not answer a reader question.                                                                                    |
| Hand-authored HTML instead of React pipeline   | Scaffold with `init-artifact.sh`, implement in React, bundle with `bundle-artifact.sh`.                                                  |
| Shipping source without bundle                 | Deliver `final/bundle.html`; keep `app/` as working source only.                                                                         |
| SVG spaghetti                                  | Use simpler diagrams, Mermaid via npm if justified, or generated/static images.                                                          |
| Mobile added last                              | Carry mobile-first constraints through brief, visual plan, and implementation.                                                           |
| Hidden uncertainty                             | Use assumption ledgers, evidence chips, and known/unknown panels.                                                                        |
| Public-by-accident sharing                     | Default to local files or secret gists; use GistPreview for rendered links. See `references/secret-gist-publishing.md`.                  |
| Ignoring project styling skill                 | Read `AGENTS.md`; follow the named styling/design skill before applying shadcn defaults.                                                 |
| Sub-agent stalls before producing artefact     | Constrain prompts: read named inputs, write the main output first, cap tool calls, then bundle and verify.                               |
| Mobile nav technically works but feels hidden  | Prefer wrapped navigation, question-card TOCs, or next-links; if using horizontal sticky nav, verify link visibility and anchor landing. |
| Executive recommendation lacks authority shape | State what approval authorises: scope, owner, review gate, guardrails, and kill condition.                                               |
| Bundle step skipped                            | Run `bundle-artifact.sh` from `app/` and copy to `final/bundle.html`.                                                                    |

## Prompt pattern for sub-agents

Use file-backed handoffs when quality matters:

1. **Collation agent:** read sources, extract facts, save `source-notes.md`.
2. **Refinement agent:** turn source notes into a concise audience-specific brief.
3. **Visual planning agent:** choose layout, elements, disclosure, and component/chart choices.
4. **React implementation agent:** scaffold if needed, implement from brief and visual plan, bundle to `final/bundle.html`.
5. **Review agent:** open `final/bundle.html` in browser, interact with the page, and critique from the audience's perspective.

See `templates/subagent-prompts.md` for copyable prompts.

## Reference

- **shadcn/ui components:** https://ui.shadcn.com/docs/components
- **Implementation checklist:** `references/implementation-checklist.md`
- **Secret gist sharing:** `references/secret-gist-publishing.md`
- **Rendered preview:** https://gistpreview.github.io/
