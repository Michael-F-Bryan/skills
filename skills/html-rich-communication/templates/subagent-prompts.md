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
Use <working-folder>/agents/refined-brief.md and plan the HTML artefact.

Save <working-folder>/agents/visual-plan.md with:
- page sections in order;
- visual elements and why each helps the reader;
- mobile-first layout notes;
- progressive disclosure plan;
- image-generation slots, if any, including prompts and target paths;
- dependency policy: native-only or justified CDN.
Do not write final HTML.
```

## HTML implementation agent

```text
Build the HTML artefact from the refined brief and visual plan.

Inputs:
- <working-folder>/agents/refined-brief.md
- <working-folder>/agents/visual-plan.md

Output:
- <working-folder>/outputs/<name>.html

Hard constraints:
- read the named inputs first;
- write the HTML output before commentary, notes, screenshots, or extra files;
- keep tool use narrow and avoid broad searches;
- after writing HTML, write brief creator notes and verify the file exists.

Requirements:
- single self-contained HTML file unless explicitly justified;
- mobile-first responsive design;
- semantic structure;
- progressive disclosure;
- accessible labels/captions;
- no external dependencies unless the visual plan justifies them.
```

## Browser review agent

```text
Open <html-path> in a browser and interact with it as <audience>.

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
