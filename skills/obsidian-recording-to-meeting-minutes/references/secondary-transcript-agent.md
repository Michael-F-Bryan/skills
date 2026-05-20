# Secondary transcript cross-check subagent

Use when a meeting has both local `scribe` output and an independent transcript source such as Google Meet/Gemini.

## Purpose

Find high-confidence corrections without replacing the polished transcript wholesale.

## Values

- Secondary transcript is evidence, not authority.
- Prefer conservative corrections.
- Output machine-applicable JSON plus short notes.
- Leave weak differences unchanged.

## Goals

- Find high-confidence ASR, speaker, terminology, and punctuation corrections.
- Return corrections in a machine-applicable JSON format.
- Preserve the polished transcript unless evidence clearly supports a change.

## Inputs

- `manifest.json`
- one polished chunk file
- matching secondary transcript time range
- known terminology/names
- speaker-attribution caveats

## Required output

Write `agent-outputs/secondary-corrections-NN.json`:

```json
{
  "chunk_id": "chunk-001",
  "corrections": [
    {
      "timestamp": "00:42:10",
      "type": "asr_term|speaker|punctuation|leave_unchanged",
      "old": "boil and gas",
      "new": "oil and gas",
      "confidence": "high",
      "reason": "Secondary transcript and meeting context both support oil and gas."
    }
  ],
  "notes": ["Several differences were left unchanged because evidence was weak."]
}
```

## Method

1. Compare only the assigned time range.
2. Focus on domain terms, names, places, products, numbers, and speaker errors.
3. Do not treat every wording difference as a correction.
4. Use `confidence: high` only when source/context clearly supports the change.
5. Return `leave_unchanged` notes for tempting but weak corrections.

## Good output

- `DPERD` → `DPIRD` when the meeting context is Western Australian primary industries.
- Speaker correction with timestamp and dialogue-flow reason.

## Bad output

- Replacing the whole chunk with Google/Gemini text.
- Applying stylistic rewrites as corrections.
- Returning prose only, with no JSON corrections.
