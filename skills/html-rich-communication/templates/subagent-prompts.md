# Sub-agent Prompt Templates

Paths assume the working folder from **RELATED SKILL:** `working-docs`. Replace `<working-folder>`, `<skill-root>`, and `<audience>` before use.

## Collation agent

```text
You are preparing source material for a rich HTML communication artefact.

Audience/job: <audience and reader action>
Working folder: <absolute path>
Inputs: <paths, URLs, notes>

Tasks:
1. Read the inputs directly.
2. Extract facts, claims, evidence, assumptions, open questions, and useful quotes — tag each by type.
3. Save to <working-folder>/source-notes.md.
4. Include source paths/URLs beside claims.
5. Do not design the page yet.
```

## Refinement agent

```text
Use <working-folder>/source-notes.md to create the refined argument.

Save <working-folder>/content-brief.md with:
- audience/job lock;
- one-sentence thesis;
- top 3-5 points;
- facts vs assumptions vs judgement (tagged);
- material cut and why;
- risks/caveats;
- recommended next action;
- what to hide behind progressive disclosure.
```

## Visual planning agent

```text
Use <working-folder>/content-brief.md and plan the React artefact.

Save <working-folder>/visual-plan.md with:
- page sections in order;
- visual elements and why each helps the reader;
- shadcn/ui or other React component choices;
- mobile-first layout and nav pattern (with anchor strategy);
- evidence badge types where trust cues matter;
- typography/fonts — bundled woff2 paths if not system stacks;
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
- <working-folder>/content-brief.md
- <working-folder>/visual-plan.md
- Skill scripts at <skill-root>/scripts/

Steps:
1. If <working-folder>/app/ does not exist, run:
   cd <working-folder> && bash <skill-root>/scripts/init-artifact.sh app
   If the script fails, stop and report — do not hand-scaffold around it.
2. Implement in <working-folder>/app/src/ (App.tsx and components).
3. Compare built UI to visual-plan.md; record any deltas in <working-folder>/README.md under "Plan fidelity".
4. Bundle from app root:
   cd <working-folder>/app && bash <skill-root>/scripts/bundle-artifact.sh
5. Copy deliverable:
   cp <working-folder>/app/bundle.html <working-folder>/final/bundle.html
6. If a shareable link is needed, create a secret gist (see <skill-root>/references/secret-gist-publishing.md).

Hard constraints:
- read the named inputs first;
- write React source and bundle.html before commentary or optional files;
- keep tool use narrow and avoid broad searches;
- do not mark README verification complete — that is the review agent's job.

Requirements:
- React + TypeScript + Tailwind + shadcn/ui;
- scroll-padding-top on html matching sticky header; scroll-mt on section targets;
- if AGENTS.md names a project styling skill, read and follow it for visual design;
- mobile-first responsive design;
- progressive disclosure via Accordion/Collapsible/Tabs;
- accessible labels/captions;
- no runtime CDN dependencies — npm packages and bundled fonts only.
```

## Browser review agent

```text
Verify <working-folder>/final/bundle.html as <audience> and write the review before any completion summary.

Serve locally (python3 -m http.server in final/) — do not rely on file:// or source inspection alone.

You must:
- test mobile (~375px) and desktop viewports;
- click every in-page nav link and record anchor landing (pass/fail) in a table;
- open every accordion, tab, and filter at both widths;
- evaluate whether the first screen answers the reader's primary question;
- separate audience-fit issues from implementation bugs;
- check self-containment (no runtime CDN fetches) and privacy posture.

Use <skill-root>/references/browser-review-template.md for structure.
Save to <working-folder>/reviews/browser-review.md.
Update <working-folder>/README.md status checkboxes only after the review file is written.
```
