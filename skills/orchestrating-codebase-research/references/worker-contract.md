# Worker contract — templates

The invariants live here, once. Dispatch messages carry only role, the exact
brief path, and the return contract. Adapt bracketed parts; keep the rest.

## Dispatch message (research or review)

```text
Read this brief first and follow it exactly:
<absolute path to BRIEF.md — pasted after reading the file back, never retyped>
If the brief is unreadable at that exact path, return BLOCKED with the path you
tried — do not reconstruct the task from other files.
Chat return: status (DONE / DONE_WITH_CONCERNS / BLOCKED), the absolute report
path, and a one-line concern. Findings go in the report, not the chat.
```

## BRIEF.md — research lane

```markdown
# T00x — <lane title>

## Goal
<One paragraph: the question this lane answers and why it matters to the
research questions in README.md. One lane = one worker run, comfortably.>

## Source boundary
- Corpus: <repo root> at commit <pinned sha>. Read-only.
- Orientation: read SOURCE-MAP.md first; build on <specific prior REPORT.md
  paths>, do not re-derive them.
- Do not run builds, tests, or external lookups.

## Questions
1. <numbered, concrete, answerable from source>
2. ...

## Output contract
Write everything to <absolute task dir>/REPORT.md:
- Create the REPORT.md skeleton (all section headings) within your first
  three calls. Checkpoint findings into it after each section — a run that
  dies mid-way must leave salvageable sections.
- Cite every consequential claim inline as `path/file.ext:start-end`.
- Separate sections: findings; **Facts vs inference**; **Limits of static
  analysis**; closing numbered **Claims safe for synthesis** (only claims a
  reader may reuse without re-checking source).
- Reserve calls to re-read the finished report before returning.
```

## BRIEF.md — adversarial review lane

```markdown
# R00x — review of T00x

## Goal
Independently refute <task REPORT.md path> against the corpus at commit
<sha>. You have source access; the report's author claims do not bind you.

## Checks
1. Locate every cited path:line; verify the lines support the exact wording.
2. Hunt overgeneralisation (evidence from one subsystem stated corpus-wide).
3. Separate fact from inference where the report blurs them.
4. Search for counterexamples and material omissions against the brief at
   <original BRIEF.md path>.

## Output contract
Write <review dir>/REVIEW.md: verdict (ACCEPT / ACCEPT WITH CORRECTIONS /
REVISE), then a finding table — ID | target claim | verdict (verified /
partly supported / unsupported / contradicted / material omission) | exact
source evidence | required correction — then lists: claims safe for
synthesis, disputed claims, missing questions by consequence.
Same persistence rules as research lanes: skeleton first, checkpoint per
finding group, read back before returning.
```

## Coordinator disposition (appended to REVIEW.md)

```markdown
## Disposition (coordinator)
| Finding | Disposition | Action |
|---|---|---|
| F1 | accept | wording applied to promoted claim |
| F2 | narrow | claim promoted in corrected form: "<exact wording>" |
| F3 | resolve | dispatched T00x-A2 (new consequential dispute) |
Promotion: claims <ids> promoted to SYNTHESIS.md with provenance.
```

## SYNTHESIS.md entry shape

```markdown
- <claim, in review-corrected wording> — `path/file.ext:120-145` (T003/R003)
```

One line per claim. Corrected wording only; provenance always; inference and
judgement labelled as such, never mixed into source facts.
