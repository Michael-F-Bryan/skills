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
3. Refine the argument → content-brief.md
4. Plan the visual/interaction surface → visual-plan.md
5. Scaffold React app in _working/
6. Implement the artefact (match the plan, or document why not)
7. Bundle to a single HTML file
8. Verify as the reader → reviews/browser-review.md
9. Share (local file; secret gist + GistPreview when a link is needed)
```

Keep the stages separate. Do not scaffold or implement until the audience, reader job, source material, content brief, and visual plan are explicit. Do not mark the task complete until `final/bundle.html` exists **and** `reviews/browser-review.md` records real browser checks.

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
  README.md                  # brief, status, plan-fidelity notes, share URLs
  content-brief.md           # refined argument (step 3)
  source-notes.md            # facts, excerpts, links, file paths
  visual-plan.md             # layout, elements, interactions (step 4)
  reviews/
    browser-review.md        # reader verification evidence (step 8; required)
  prompts/                   # optional: sub-agent prompts
  agents/                    # optional: sub-agent outputs
  app/                       # React project (scaffolded in step 5)
  final/
    bundle.html              # bundled self-contained artefact
```

Read files and sources directly; do not rely on chat memory. If sub-agents are used, require named output files and read them back before trusting their summaries.

Confirm `_working/` is gitignored before writing (`git check-ignore -v _working/<topic>/README.md`).

## 3. Refine before designing

Save the output as `content-brief.md` before writing `visual-plan.md`. Produce a simplified brief:

- lead with the answer/recommendation, not context archaeology;
- cut material that does not help the reader's job — record major cuts and why;
- separate facts, assumptions, judgement, risks, and open questions (tag each claim);
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

**Typography:** if the plan names fonts, specify bundled woff2 files under `app/public/fonts/` — not runtime CDN links (Google Fonts, etc.). System font stacks are fine when named explicitly in the plan.

**Evidence typing:** when the artefact mixes facts, assumptions, and judgement, plan Badge (or equivalent) usage up front — e.g. **source fact**, **assumption**, **judgement**, **unknown**, **hard rule**, **anti-pattern**, **example** — and place them where readers need trust cues.

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

The init script creates `app/` with path aliases (`@/`), Radix/shadcn theming, scroll-padding defaults for anchor nav, and Node 18+ compatibility. Requires Node 18+ and pnpm (installed automatically if missing).

If the script fails, fix the script or report the error — do not silently hand-scaffold a partial project and continue. A broken pipeline hides skill regressions.

## 6. Implement the artefact

Edit the generated React app to match `content-brief.md` and `visual-plan.md`. Primary entry: `app/src/App.tsx` and supporting components under `app/src/`.

### Plan fidelity

Before bundling, walk the visual plan section by section. Each planned element should exist for a reader reason. When you deviate — simpler diagram, dropped section, system fonts instead of named faces — add a **Plan fidelity** subsection to `README.md` listing each delta and why. Unexplained drift is a common failure mode.

Use `references/implementation-checklist.md` (plan fidelity + React source sections).

### Design guidelines

**Project styling takes precedence.** Before choosing colours, typography, spacing, or component styling, read the repo's `AGENTS.md` (or equivalent agent instructions). If it names a default styling or design skill — e.g. brand guidelines, theme factory, frontend-design — read and follow that skill for the visual language. The shadcn/Tailwind scaffold from `init-artifact.sh` is a technical baseline only; do not treat its default theme as the design system when the project specifies otherwise.

If no project styling skill is stipulated, avoid “AI slop”: excessive centered layouts, purple gradients, uniform rounded corners everywhere, and Inter as the default font. Match typography, spacing, and hierarchy to the audience and reading context.

### Implementation conventions

- **Layout:** semantic structure via components; responsive Tailwind with a 375px mobile sanity check.
- **Progressive disclosure:** shadcn Accordion, Collapsible, or Tabs — not hover-only reveals.
- **Navigation:** pair `scroll-padding-top` on `html` with matching `scroll-mt-*` on section targets; test every nav link (see step 8). Sticky header height and scroll padding must match.
- **Charts/diagrams:** prefer npm packages (e.g. recharts, mermaid) bundled into the artefact — not runtime CDN loads.
- **Print/PDF:** add print styles when the artefact may be saved as PDF.
- **Images:** put assets in `app/src/assets/` or `app/public/`; they are inlined at bundle time.
- **Fonts:** `@font-face` from bundled files only; never `<link>` to external font CDNs in `index.html`.

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

This produces `app/bundle.html` — a self-contained file with all JavaScript, CSS, and assets inlined via Parcel + html-inline. The script configures Parcel's native dependencies for pnpm 10+.

Copy the deliverable to the working folder output:

```bash
cp bundle.html ../final/bundle.html
```

Run step 8 before reporting completion. If bundling fails, fix `bundle-artifact.sh` or the project config — manual Parcel invocations are a last resort, not the normal path. The React source in `app/` is the editable working copy; `final/bundle.html` is the deliverable.

## 8. Verify as the reader

Verification is a **required deliverable**, not an optional polish pass. Serve `final/bundle.html` over a local HTTP server (`python3 -m http.server` in `final/`) — do not rely on `file://` alone or source inspection.

Write `_working/<topic>/reviews/browser-review.md` using `references/browser-review-template.md`. The review must include:

- viewports tested (mobile ~375px and desktop);
- whether the first screen answers the primary reader question;
- a **nav anchor table** — every in-page link clicked, pass/fail on landing below the sticky header (target: heading within ~24px of `scroll-padding-top`);
- every accordion, tab, and filter exercised at both widths;
- audience-fit issues separated from implementation bugs;
- a ship / caveats / do-not-ship verdict.

Also check: no colour-only meaning; copy/export controls work; no runtime CDN fetches; privacy posture matches README; executive artefacts (when applicable) state scope, owner, review gate, and kill condition.

Update `README.md` status checkboxes **only after** `browser-review.md` exists with evidence. List the working folder, read back `README.md`, `browser-review.md`, and confirm `final/bundle.html` before reporting completion.

Use `references/implementation-checklist.md` (browser verification section).

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
| Visual plan drift                              | Walk plan vs built before bundling; record deltas in README **Plan fidelity** or implement what was planned.                             |
| Verification theatre                           | Write `reviews/browser-review.md` with nav/disclosure evidence; do not claim browser verification from one or two clicks.                |
| Anchor nav lands mid-viewport                  | Match `scroll-padding-top` on `html` to sticky header height; use matching `scroll-mt-*` on targets; re-test all links.                  |
| Hand-authored HTML instead of React pipeline   | Scaffold with `init-artifact.sh`, implement in React, bundle with `bundle-artifact.sh`.                                                  |
| Script failure → silent manual workaround      | Fix `init-artifact.sh` / `bundle-artifact.sh` or stop and report; partial hand-scaffolding hides pipeline regressions.                   |
| Shipping source without bundle                 | Deliver `final/bundle.html`; keep `app/` as working source only.                                                                         |
| SVG spaghetti                                  | Use simpler diagrams, Mermaid via npm if justified, or generated/static images.                                                          |
| Mobile added last                              | Carry mobile-first constraints through brief, visual plan, and implementation.                                                           |
| Hidden uncertainty                             | Use assumption ledgers, evidence chips, and known/unknown panels.                                                                        |
| External font CDN                              | Bundle woff2 under `app/public/fonts/`; keep the artefact self-contained.                                                                |
| Public-by-accident sharing                     | Default to local files or secret gists; use GistPreview for rendered links. See `references/secret-gist-publishing.md`.                  |
| Ignoring project styling skill                 | Read `AGENTS.md`; follow the named styling/design skill before applying shadcn defaults.                                                 |
| Sub-agent stalls before producing artefact     | Constrain prompts: read named inputs, write the main output first, cap tool calls, then bundle and verify.                               |
| Mobile nav technically works but feels hidden  | Prefer wrapped navigation, question-card TOCs, or next-links; if using horizontal sticky nav, verify link visibility and anchor landing. |
| Executive recommendation lacks authority shape | State what approval authorises: scope, owner, review gate, guardrails, and kill condition.                                               |
| Bundle step skipped                            | Run `bundle-artifact.sh` from `app/` and copy to `final/bundle.html`.                                                                    |

## Prompt pattern for sub-agents

Use file-backed handoffs when quality matters:

1. **Collation agent:** read sources, extract facts, save `source-notes.md`.
2. **Refinement agent:** turn source notes into `content-brief.md`.
3. **Visual planning agent:** choose layout, elements, disclosure, and component/chart choices → `visual-plan.md`.
4. **React implementation agent:** scaffold if needed, implement from brief and visual plan, record plan fidelity, bundle to `final/bundle.html`.
5. **Review agent:** browser-verify `final/bundle.html`, save `reviews/browser-review.md` before any completion summary.

See `templates/subagent-prompts.md` for copyable prompts.

## Reference

- **shadcn/ui components:** https://ui.shadcn.com/docs/components
- **Implementation checklist:** `references/implementation-checklist.md`
- **Browser review template:** `references/browser-review-template.md`
- **Secret gist sharing:** `references/secret-gist-publishing.md`
- **Rendered preview:** https://gistpreview.github.io/
