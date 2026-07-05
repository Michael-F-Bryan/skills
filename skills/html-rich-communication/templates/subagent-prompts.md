# Sub-agent Prompt Templates

## Collation agent

```text
You are preparing source material for a rich HTML communication artefact.

Audience/job: <audience and reader action>
Working folder: <absolute path>
Inputs: <paths, URLs, notes>

Tasks:
1. Read the inputs directly.
2. Extract facts, claims, evidence, assumptions, open questions, and useful quotes.
3. Save to <working-folder>/agents/source-notes.md.
4. Include source paths/URLs beside claims.
5. Do not design the page yet.
```

## Refinement agent

```text
Use <working-folder>/agents/source-notes.md to create a concise audience-specific brief.

Save <working-folder>/agents/refined-brief.md with:
- audience/job lock;
- one-sentence thesis;
- top 3-5 points;
- facts vs assumptions;
- risks/caveats;
- recommended next action;
- what to hide behind progressive disclosure.
```

## Visual planning agent

```text
Use <working-folder>/agents/refined-brief.md and plan the React artefact.

Save <working-folder>/agents/visual-plan.md with:
- page sections in order;
- visual elements and why each helps the reader;
- shadcn/ui or other React component choices;
- mobile-first layout notes;
- progressive disclosure plan;
- image-generation slots, if any, including prompts and target paths under app/src/assets/ or app/public/;
- chart/diagram library choices (npm packages to bundle, not CDN);
- project styling skill from AGENTS.md, if any.
Do not scaffold or implement yet.
```

## React implementation agent

```text
Build the React artefact from the refined brief and visual plan, then bundle it.

Inputs:
- <working-folder>/agents/refined-brief.md
- <working-folder>/agents/visual-plan.md
- Skill scripts at <skill-root>/scripts/

Steps:
1. If <working-folder>/app/ does not exist, run:
   cd <working-folder> && bash <skill-root>/scripts/init-artifact.sh app
2. Implement in <working-folder>/app/src/ (App.tsx and components).
3. Bundle from app root:
   cd <working-folder>/app && bash <skill-root>/scripts/bundle-artifact.sh
4. Copy deliverable:
   cp <working-folder>/app/bundle.html <working-folder>/final/bundle.html
5. If a shareable link is needed, create a secret gist and give the user the GistPreview URL (see <skill-root>/references/secret-gist-publishing.md).

Hard constraints:
- read the named inputs first;
- write React source and bundle.html before commentary, notes, screenshots, or extra files;
- keep tool use narrow and avoid broad searches;
- after bundling, write brief creator notes and verify final/bundle.html exists.

Requirements:
- React + TypeScript + Tailwind + shadcn/ui;
- if AGENTS.md names a project styling skill, read and follow it for visual design;
- mobile-first responsive design;
- progressive disclosure via Accordion/Collapsible/Tabs;
- accessible labels/captions;
- no runtime CDN dependencies — npm packages bundled at build time only.
```

## Browser review agent

```text
Open <working-folder>/final/bundle.html in a browser and interact with it as <audience>.

Do not only inspect source. You must:
- open the file in a browser;
- test mobile and desktop-ish viewport sizes;
- click nav links and record target landing behaviour;
- open every disclosure control at mobile and desktop widths;
- evaluate whether the first screen answers the reader's question;
- identify audience-fit issues, comprehension gaps, visual problems, accessibility problems, and implementation bugs;
- write the review files before spending time on optional screenshots or extra probes.

Save feedback to <working-folder>/reviews/browser-review.md.
```
