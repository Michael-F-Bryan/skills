---
name: transcript-workflows
description: Use when acquiring or cleaning speech-to-text, ASR, captions, diarisation/diarization, transcripts, chapters, meeting minutes, or Obsidian source notes from local recordings, Teams, Gemini, YouTube, podcasts, or existing transcript files.
---

# Transcript Workflows

## Core rule

`jake-tools` is the only transcript workflow executor. This skill supplies routing and acceptance policy; it does not reimplement the pipeline.

## Start here

```bash
unset PYTHONPATH
jake-tools --help
jake-tools transcript --help
jake-tools transcribe --help
```

Use the narrowest task-oriented command exposed by the live help. Prefer a composite recipe over public primitives. Give long runs an explicit work directory and manifest when supported, and use dry-run/proposed output before mutating an Obsidian note.

Do not:

- import `jake_tools` internals from an ad hoc script;
- revive skill-local transcript fetchers, renderers, or verifiers;
- chain `source`, `parse`, `transform`, `stage`, `render`, and `note` primitives to emulate a missing outcome recipe;
- construct a parallel coordinator from model workers;
- guess undocumented CLI options;
- silently fall back to manual transcription when the requested route is absent.

If the live CLI cannot honour an explicit phase boundary, source, profile, or resume point, stop with the last valid artefact and report the precise `jake-tools` capability gap. Michael requesting the phase boundary or desired output is not approval to improvise a bridge. A narrow deterministic bridge is allowed only after the gap and concrete bridge have been presented and Michael separately approves that workaround.

## Source and profile routing

**REQUIRED REFERENCE:** Read `references/source-routing.md` for local recordings, Teams/Graph, Gemini, timed media, existing transcripts, vault destinations, and DUM-C note shape.

The source adapter ends at canonical transcript JSON. Raw VTT, captions, PDFs, recordings, and emails remain provenance artefacts; they do not define downstream workflow structure.

## Fidelity and readability

**REQUIRED REFERENCE:** Read `references/fidelity-and-polishing.md` for private meetings, speaker mapping, chapter coverage, polishing, minutes, corrections, and final verification.

Transcript text is evidence. Structural validity is necessary but does not prove fidelity or readability. Human speaker corrections outrank machine inference, and corrected upstream artefacts invalidate affected downstream output.

`present-validated` is mechanical capability proof only. It does not establish that the transcript is readable or that minutes preserve commitment modality. Before canonical apply, render a candidate, export its exact product-review pack with `transcript review product export`, inspect it, and record the accepted or rejected decision with `transcript review product decide`. `transcript apply` must remain blocked until that exact revision, transcript, minutes, render, and policy have accepted product review.

Use supported repair seams rather than bundle surgery:

- `transcript transform utterances export/apply` for reviewed exact-partition semantic reflow;
- `transcript transform correction-pack export/apply` for evidence-backed one-turn text repairs;
- regenerate chapters, minutes, and render after either changes canonical turns.

If command JSON claims success but the process returns non-zero, stop and diagnose the command/runtime boundary. Neither signal may be discarded to force progression.

## Human checkpoints

Honour explicit checkpoints before downstream work. For under-clustered diarisation, preserve the normalised unmerged transcript, collect bounded speaker evidence, and leave uncertain turns unresolved rather than manufacturing complete-looking names.

## Evaluation fixture clipping

When deriving bounded local audio fixtures, record the source hash, source-local offset, duration, and any combined-timeline mapping. Probe the actual codec and container rather than trusting the extension.

A valid vault `.m4a` may contain Opus in an MP4 container. `ffmpeg -c copy output.m4a` can select the `ipod` muxer and fail with `Could not find tag for codec opus`. Preserve the source codec by selecting MP4 explicitly:

```bash
ffmpeg -ss START -t DURATION -i source.m4a \
  -map 0:a:0 -c copy -avoid_negative_ts make_zero -f mp4 output.m4a
```

After clipping, decode the complete output, probe its duration/codec, confirm it is not silent, and record the derived hash. If stream copy is impossible, document any re-encoding rather than treating the derivative as source-equivalent evidence.

## Claude session-limit failures

If `jake-tools` reports `Claude Code returned an error result: success`, do not treat it as a prompt, transcript, or validator failure. Inspect the newest Claude session JSONL for the repository working directory under `~/.claude/projects/`. A synthetic assistant message with `isApiErrorMessage: true`, `apiErrorStatus: 429`, or text such as `You've hit your session limit` establishes a provider/session limit even when the SDK's outer exception says `success`.

Record the stated reset time, preserve the last validated bundle head, and resume only the missing stage after reset. Do not change the prompt or loop retries while the limit remains active.

## Completion

Report:

- command and profile used;
- source and destination paths;
- manifest or run directory;
- speaker uncertainty;
- chapter and turn coverage status;
- representative readability result;
- final note verification;
- exact blocked stage and resumption action when incomplete.

No canonical note write is complete until the written file has been re-read and compared with the verified proposed artefact.
