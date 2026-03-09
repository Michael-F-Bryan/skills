# Coding Workflows For Obsidian CLI

Use this file when the task is not just "edit a note", but "use the vault to support coding work with the right note in the right way".

## Core principle

Treat the vault as external working memory. The goal is to preserve continuity, decisions, and next steps without creating documentation overhead.

Treat note discovery as graph traversal, not just keyword lookup. Find one good note, then use its `[[wikilinks]]`, `links`, and `backlinks` to uncover related context.

## Choose the right note

### Quick decision aid

- Need session progress, blocker state, or today's next step: use the daily note.
- Need durable project state, implementation status, or handover context: use the project note.
- Need explicit analysis, assumptions, or trade-off thinking during the work: use a working note.
- Need a reusable lesson that should survive beyond the task: use a synthesis note.
- If an existing note already fits, update it instead of creating a new one.

### Daily note

Use when the update is mainly about today.

Best for:

- Session progress
- Current blockers
- Waiting state
- The next action for later today or tomorrow

Do not use it for:

- Long-lived project state that will matter next week
- Detailed design rationale that belongs with the project

### Project note

Use when the update changes the durable state of active work.

Best for:

- Current scope
- Implementation status
- Key risks
- Decisions with consequences
- Handover context for later re-entry

Do not use it for:

- Every tiny implementation detail
- Throwaway session chatter

### Working note

Use when the task needs explicit analysis before or during execution.

Best for:

- Assumptions and constraints
- Evidence gathering
- Planning phases
- Acceptance criteria
- Trade-off analysis

Do not use it for:

- Finished synthesis that should be easier to skim later

### Synthesis note

Use when the result is worth keeping beyond the immediate task.

Best for:

- Tricky bug diagnoses
- Migration lessons
- Reusable implementation patterns
- Short post-task summaries with future value

Do not use it for:

- Routine progress logging

## Default workflows

### Resume non-trivial coding work

1. Confirm the vault.
2. Search for the project, subsystem, or ticket identifier.
3. Read the most relevant project or working note.
4. Follow nearby links and backlinks to build out the surrounding context.
5. Only then decide whether the vault needs an update.

### Record session progress

1. Read today's daily note.
2. Append a short update with progress, blocker, and next step.
3. Keep it concise enough that later scanning still works.

### Capture a design or implementation decision

1. Search for the project note or existing decision note.
2. Prefer updating the existing project note.
3. Record context, chosen approach, and consequences.
4. Create a separate note only if the decision will be reused independently.

### Leave a handover after substantial work

1. Update the project note with current state and follow-up work.
2. Add a daily-note entry if the timing or blocker matters today.
3. Create a synthesis note only if the lesson is broadly reusable.

## Practical heuristics

- Search before write.
- Once you find a promising note, prefer `links` and `backlinks` over repeated blind searching.
- Read before append.
- Prefer existing notes over new notes.
- Prefer local edits over full rewrites.
- Re-read after writing when the update is important.
- Keep capture separate from synthesis.
- Preserve wikilinks, headings, and light metadata already in the note.
- Add natural inline `[[wikilinks]]` to related notes, concepts, people, or projects where they improve future retrieval.
- Do not collect links in a trailing references section; place them where they matter in the prose.

## Good update shape

Use short, practical sections or bullets such as:

- Current state
- Decision
- Risk
- Blocker
- Next step

## Avoid

- Changelog-style dumps with no retrieval value
- Generic "worked on X" updates that say little
- Rewriting a structured note when an append would do
- Creating new notes for work that belongs in an existing project stream
