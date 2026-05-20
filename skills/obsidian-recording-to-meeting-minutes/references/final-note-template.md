# Final note template

Use this when merging specialist outputs into the vault-bound meeting note. Match vault `AGENTS.md` if it conflicts (wikilinks, locale, callouts).

## Section order

After any YAML frontmatter, the body should follow this order unless vault rules say otherwise:

1. `> [!summary]` callout (immediately after frontmatter)
2. `## Key details`
3. `## Chapters`
4. `## Transcript`

Include `## Transcript` at the bottom of the note, after chapters. Keep the polished, diarised transcript in the vault note. Keep any raw ASR or scratch-only evidence out of the note unless the user explicitly asks for it. Do **not** add `## Raw transcript`.

## Body template

```markdown
> [!summary]
> Concise meeting outcome summary.

## Key details
- **Meeting:** ...
- **Attendees:** [[...]], [[...]]
- **Recording:** ![[...m4a]]
- **Decisions:** ...
- **Actions / follow-ups:** ...
- **Open questions:** ...

## Chapters
- **00:00 — Topic:** One-sentence description.

## Transcript
### 00:00 — Topic
**Speaker (00:12):** Polished but faithful utterance.
```

### Transcript conventions

- Chapter headings under `## Transcript` mirror `## Chapters` timing and titles.
- Turn lines: `**Speaker Name (H:MM:SS):**` utterance — timestamps grounded in the polished/diarised source.
- Preserve uncertainty from speaker attribution (e.g. “Unknown (likely [[Name]])”) rather than forcing a clean label.

### Multiple recordings

Repeat **Recording** bullets under Key details (or list each embed clearly). Ensure every original `![[...]]` audio embed from the source note remains in the final note unless the user asked to remove one.

## Verification (structural)

Automated checks in the parent skill’s verification snippet are **heuristics** (e.g. recording embed detection may miss unusual embed spellings). Always combine with a manual skim and QA audit output.
