---
name: dumc-email-to-obsidian-notes
description: Use when turning CSU/DUM-C emails, Microsoft Graph mailbox pulls, or email thread summaries into durable Obsidian notes for Michael's Deputy Unit Manager - Capability area.
---

# DUM-C Email to Obsidian Notes

## Overview

Use this skill to convert CSU email threads into durable DUM-C operational notes without turning the vault into an inbox clone.

Core principle: preserve events, decisions, and source evidence — not every email.

Temporary working directories are ephemeral. Anything referenced from a saved note must either be copied into the vault's `Attachments/` tree or quoted/summarised sufficiently that losing the temp directory does not break the note.

## Trigger contract

Use this skill when the source material is any of:

- CSU or DUM-C mailbox messages, including `michael.bryan@csu-ses.com.au` and role accounts such as `deputycapability@csu-ses.com.au`.
- Microsoft Graph mail pulls, Outlook exports, Gmail/Himalaya exports, or `.eml` files.
- A summary of CSU emails that may need notes under `~/Documents/Vault/2 Areas/DUM-C`.

Do not use it for meeting transcripts. Use the meeting/transcript workflow for those.

## Prerequisites

1. Read `~/Documents/Vault/AGENTS.md` before writing into the vault.
2. Confirm the destination folder is `~/Documents/Vault/2 Areas/DUM-C` unless the user says otherwise.
3. Inspect nearby DUM-C notes to match naming, frontmatter, tags, and prose style.
4. Treat any `/tmp`, `_working`, download, or email-export directory as disposable.

## Noteworthiness threshold

Create or update a DUM-C note when the thread records at least one durable fact future DUM-C work may need.

| Create/update a note when... | Examples |
| --- | --- |
| Personnel or status changed | member stepping back, joining, changing availability, returning kit, losing account access |
| An action or decision happened | approved, declined, escalated, delegated, requested, or waiting on follow-up |
| Training/capability planning changed | training calendar, trainer availability, session design, resources, handover context |
| Operational/admin state matters | MOVAT, M365, Teams, newsletter access, contact lists, duty numbers, role mailbox state |
| It answers a future audit question | when it happened, who said it, why a decision was made, what source supports it |

Do not create standalone notes for:

- routine newsletter repetition with no new calendar/admin state;
- vendor/system noise;
- threads where the only durable value is FYI;
- raw announcements already captured better elsewhere;
- every email in a thread.

When uncertain, prefer a short entry in an existing running note over a new standalone note.

## One note versus many

Use one note per real-world event or coherent thread, not one note per email.

Create separate notes when events have different owners, timelines, or future retrieval questions. Merge emails when they are replies in the same thread or multiple notifications for the same action.

Examples:

- One note for a member stepping back, including the full reply chain.
- One note for a newsletter/M365 access issue, including the request, reply, and diagnosis.
- One note for a cluster of training-planning emails if they all update the same plan.
- A separate note for a trainer's availability if it is a distinct input to planning.
- No standalone note for a newsletter unless it changes an event, contact list, or operational state worth preserving.

## Source preservation rule

Never save an Obsidian note that points only to `/tmp`, `_working`, a transient download directory, or an email client's cache.

If the exact source file matters:

1. Copy the `.eml`, attachment, PDF, spreadsheet, or image into the vault, usually under `~/Documents/Vault/Attachments/DUM-C/`.
2. Use a stable, kebab-case or date-prefixed filename that identifies the thread.
3. Link the attachment from the note using Obsidian embed/link syntax.
4. Keep the email `Message-ID` in frontmatter or a source section.
5. Verify the copied attachment exists before reporting completion.

If the exact source file does not matter:

- include short direct excerpts where wording matters;
- record sender, recipients, timestamp, subject, and `Message-ID`;
- omit transient paths from the final note.

## Note shape

Use an ops-log/source-note hybrid.

```markdown
---
Timestamp: 2026-06-12T14:21
Date: [[June 12, 2026]]
Time: 14:21
Attendees:
  - [[Mark Newton]]
  - [[Matt Lavender]]
  - [[Michael Bryan]]
Organisation: [[Communications Support Unit]]
tags:
  - ops-log
  - note/email
message-id:
  - "<message-id@example>"
source:
  - "[[Attachments/DUM-C/2026-06-12-mark-newton-stepping-back.eml]]"
---

> [!summary]
> [[Mark Newton]] advised that work commitments mean he is unlikely to return to CSU before Christmas, and he intends to return his kit. [[Matt Lavender]] accepted the decision and thanked him for his contributions.

## Context

Why this matters to the DUM-C area.

## Key points

- What changed.
- Who is affected.
- What source says it.

## Follow-up

- [ ] Only add tasks that are implied by the email or explicitly requested.

## Source excerpts

> Short direct quotes where exact wording matters.

## Source emails

- 2026-06-12 14:21 — [[Mark Newton]] — `Not coming back`
- 2026-06-12 21:10 — [[Matt Lavender]] — `RE: Not coming back`
```

Adapt the headings to the event. Do not force empty sections.

## Summarising and interpretation

Keep three layers visibly separate:

1. **Summary** — factual and concise: what happened, who was involved, what changed.
2. **Context/significance** — light interpretation: why it matters to DUM-C, capability, training, or admin.
3. **Follow-up** — only actions implied by the email or requested by the user.

Do not turn email notes into essays. Do not add speculation. If a conclusion is inferred rather than stated, label it as an inference.

## Wikilinking policy

Inject wikilinks deliberately.

Link:

- people: `[[Mark Newton]]`, `[[Lilian Oh]]`, `[[Des Everingham]]`;
- organisations and units: `[[Communications Support Unit]]`, `[[DFES]]`, `[[Stirling SES]]`;
- systems and processes: `[[MOVAT]]`, `[[M365]]`, `[[FESMaps]]`, `[[Caltopo]]`, `[[AVL]]`;
- recurring responsibilities: `[[Training]]`, `[[Newsletter]]`, `[[Kit Return]]` when such notes exist or should exist.

Search the vault for existing pages before creating new target spellings. Use aliases when the canonical page name would read awkwardly in prose.

Do not link every noun. Link things a future reader would navigate to.

## Workflow

For the practical recent-email review pattern, including Graph mailbox selection, scratch index shape, and source promotion rules, see `references/session-email-review-workflow.md`.

For requests about Michael's CSU emails, use the CSU Microsoft Graph path first (`csu-teams` token for `michael.bryan@csu-ses.com.au`) and explicitly probe role/shared mailboxes such as `deputycapability@csu-ses.com.au`. Use Himalaya/Gmail only as a labelled fallback or when the user asks for the personal mailbox.

1. Group messages by thread/event.
2. Apply the noteworthiness threshold.
3. Search DUM-C for existing notes about the same event or person/date.
4. Choose create versus update:
   - update existing notes when the thread continues an already-captured event;
   - create a new note when it is a distinct future retrieval target.
5. Copy any durable source files into `Attachments/DUM-C/` before referencing them.
6. Draft the note in the ops-log/source-note hybrid shape.
7. Add only useful wikilinks.
8. Re-open the saved note and verify frontmatter, links, source files, and absence of transient paths.

## Common pitfalls

1. **Inbox mirroring.** Do not create one note per email. Preserve events and decisions.
2. **Broken provenance.** Do not reference `/tmp` or `_working` from final notes. Copy durable source files into the vault first.
3. **Over-summarising away evidence.** Keep source facts, timestamps, people, and Message-IDs.
4. **Invented actions.** Only create tasks that the email implies or the user asks for.
5. **Overlinking.** Wikilinks should aid navigation, not make every sentence noisy.
6. **Role-mailbox blind spots.** If Graph cannot read a shared mailbox directly, say so. Do not imply the pull was complete for role accounts.
7. **Wrong mailbox, plausible notes.** Personal Gmail/Himalaya `Personal/SES` can contain SES-looking messages, but it is not the CSU mailbox. A run that skips `michael.bryan@csu-ses.com.au` via Graph has not satisfied a CSU-email review.

## Verification checklist

Before reporting completion:

- [ ] Email source matches the request: CSU Graph first for CSU mail; any Gmail/Himalaya fallback is labelled.
- [ ] `~/Documents/Vault/AGENTS.md` was followed.
- [ ] Notes are in `~/Documents/Vault/2 Areas/DUM-C` unless directed otherwise.
- [ ] Each note maps to one event/thread, not one arbitrary email.
- [ ] Frontmatter includes `Timestamp`, `Date`, `Time`, `Organisation`, `tags`, and `message-id` where available.
- [ ] Any referenced `.eml` or attachment has been copied into the vault `Attachments/` tree.
- [ ] No final note references `/tmp`, `_working`, or other ephemeral paths.
- [ ] Wikilinks use existing canonical page names where practical.
- [ ] The saved notes were re-read from disk.
