# Manifest and chunking

Use this when preparing subagent inputs after `scribe` completes.

## Purpose

Create bounded, file-based work packets so subagents can operate without loading the whole meeting.
This file is the canonical reference for chunking and multi-recording handling.

## Manifest schema

Write `/tmp/<slug>/manifest.json`:

```json
{
  "slug": "meeting-slug",
  "vault_path": "/absolute/path/to/Vault",
  "note_path": "/absolute/path/to/Vault/0 Inbox/Note.md",
  "vault_rules_summary": "Australian English; preserve frontmatter; use wikilinks",
  "attendees": ["[[Michael Bryan]]"],
  "recordings": [
    {
      "id": "rec01",
      "embed": "![[Recording 20260520105435.m4a]]",
      "audio_path": "/absolute/path/to/Vault/Attachments/Recording 20260520105435.m4a",
      "scribe_json": "/tmp/slug/scribe/merged.json",
      "filename_timestamp": "2026-05-20T10:54:35",
      "duration_seconds": 4915.76,
      "offset_seconds": 0,
      "boundary_notes": "Concatenated into merged stream in note order"
    }
  ],
  "chunks": [
    {
      "chunk_id": "chunk-001",
      "recording_id": "rec01",
      "start_seconds": 0,
      "end_seconds": 1800,
      "continuous_start_seconds": 0,
      "json_excerpt": "/tmp/slug/chunks/chunk-001.json",
      "text_excerpt": "/tmp/slug/chunks/chunk-001.txt",
      "polished_output": "/tmp/slug/agent-outputs/polished-chunk-001.md"
    }
  ],
  "speaker_mapping_policy": {
    "base_assumption": "merged_diarisation_global_labels",
    "notes": "Treat speaker IDs as globally consistent by default because diarisation ran once on merged audio; add caveats only when evidence is mixed."
  },
  "secondary_transcripts": [],
  "agent_outputs": {
    "speaker_attribution": "/tmp/slug/agent-outputs/speaker-attribution.md",
    "minutes": "/tmp/slug/agent-outputs/minutes.md",
    "qa": "/tmp/slug/agent-outputs/qa-audit.md"
  }
}
```

## Chunking rules

- Concatenate all embedded recordings into one scratch file and run one transcription pass before chunking.
- Default 20–45 minutes.
- Prefer natural recording boundaries and topic breaks.
- Split smaller when speaker attribution is difficult, density is high, or secondary comparison is needed.
- Preserve 10–30 seconds of overlap text between adjacent text excerpts for continuity, but avoid duplicating overlap in final output.
- Record continuous offsets separately from per-file timestamps.
- Transcribe sequentially, not in parallel. `scribe` is memory-heavy and parallel workers can destabilise laptops.

## Multi-recording handling

When the note embeds multiple recordings:

1. Extract all audio embeds from the note.
2. Resolve each file path under the vault.
3. Concatenate files in note order into `/tmp/<slug>/audio/merged.*`.
4. Transcribe the merged stream once.
5. Keep the original per-recording metadata in `recordings[]` for traceability.

## Extracting chunk files

Use a small script to filter `scribe` segments by `start`/`end`, then write both JSON and text excerpts. Text excerpts should include timestamp, speaker label, and utterance only.

Good text excerpt:

```text
[00:12:04] SPEAKER_01: We need to choose the first beachhead market...
[00:12:18] SPEAKER_02: I reckon seagrass is still the clearest...
```

Bad excerpt:

- Entire 3-hour transcript.
- Segments without timestamps.
- Speaker-normalised text before attribution has run.
