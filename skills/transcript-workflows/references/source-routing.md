# Source routing and note profiles

## Route by source

Always inspect live help before selecting a route. Command names below describe the current shape, not a promise that every checkout exposes every adapter.

| Source or request | Canonical route | Source boundary |
|---|---|---|
| Obsidian note with local recordings | `jake-tools transcript recipe obsidian-recording` | Resolve all embeds, order recordings by creation time, concatenate, and require local Scribe JSON before downstream work. Do not select the older direct-write `transcribe obsidian-recording` path for meeting-note jobs. |
| Microsoft Teams meeting | `jake-tools transcript recipe teams-meeting` | Outlook calendar event → organiser and join URL → `onlineMeeting` → transcript metadata → VTT content → canonical JSON. |
| Gemini text or PDF | A live `jake-tools transcript source gemini-*` route followed by the supported workflow | Preserve source message/doc/PDF metadata. A notes-only document is not a transcript. |
| Existing transcript | The live `jake-tools transcribe polish` or supported transcript-stage route | Preserve the original transcript as immutable evidence. |
| YouTube, podcast, or recorded talk | A task-oriented `jake-tools` route when live help exposes one | Prefer authored captions, then appropriate automatic captions, before expensive local ASR. Preserve timing and source URL. |

If the source route is absent, report it as a `jake-tools` product gap. Do not recreate the old skill-local workflow.

## Local recordings

- Preserve every source embed and record ordered input paths.
- Use local `scribe` JSON for the canonical ASR artefact.
- A host that slept or lost network may make a healthy long run look stalled. Check process activity and artefact timestamps before intervening.
- Do not switch to a manual renderer merely because a run is quiet.
- For attendee count greater than recurring machine-speaker count, stop for speaker review before destructive adjacent-speaker merging or downstream note mutation.

## Teams and CSU

Use the established `csu-teams` delegated device-code path. Do not ask Michael for Graph environment credentials or a client secret for one-off delegated retrieval.

- Outlook calendar is the durable index, including when Michael was an attendee rather than organiser.
- Graph transcript metadata is JSON; speaker-attributed transcript content is VTT. Convert VTT immediately at the ingestion boundary and retain raw VTT only as working provenance.
- Inspect token scopes when endpoints return 403. Successful `/me` access does not prove `Calendars.Read`, `OnlineMeetings.Read`, or `OnlineMeetingTranscript.Read.All`.
- Use direct Graph probes only to diagnose a failing canonical route, not as a second production pipeline.

## Gemini

- Preserve exact message/document identity for deduplication; use the source message ID as the ledger when available.
- If Gemini provides notes without a transcript, keep them as notes and state that no transcript was available. Never fabricate dialogue.
- If a linked recording is available and the live canonical route supports it, transcribe that recording and retain the Gemini source link.
- Do not revive `record-gemini-transcripts` helper scripts after consolidation.

## Timed media

- Prefer captions to ASR when available.
- For YouTube, JSON3 is preferable to rolling-window VTT when the canonical adapter supports it.
- Preserve title, channel/publisher, source URL, selected caption track, language, and timing provenance.
- Do not infer a speaker from the channel or title.

## Vault rules

Read the vault's current instructions before writing. Michael's vault root is `~/Documents/Vault`.

### DUM-C

Destination: `~/Documents/Vault/2 Areas/DUM-C`.

- Use AWST (`UTC+8`).
- Preserve source embeds and authored frontmatter/content.
- Keep a short `[!summary]` callout.
- Put terse, nested operational minutes under `## Discussion Notes`.
- Keep `## Chapters` before `## Transcript` when a chaptered transcript is requested.
- Record discussed next steps without assigning Michael tasks.
- Do not add task checkboxes or `Action:` labels.
- Keep attendees in frontmatter when that is the established note convention.

### Sunfish and general private meetings

Use the requested area and existing note conventions. Keep meeting minutes distinct from the evidence transcript. Do not copy raw source transcripts into the vault when the polished transcript is already embedded unless Michael explicitly requests provenance there.

## Mutation rule

Generate and verify a proposed note first. Replace only generated sections unless the user explicitly asks to rebuild the whole note. Preserve frontmatter, embeds, wikilinks, authored notes, and unrelated top-level sections byte-for-byte where practical.
