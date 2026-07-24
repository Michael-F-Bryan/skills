# Fidelity, polishing, and verification

## Evidence contract

A private meeting transcript records what was said; it is not a publication summary.

Preserve:

- claims, examples, qualifications, objections, alternatives, uncertainty, humour, and interpersonal context;
- names, numbers, dates, technical terms, and decisions;
- speaker order and complete meeting-span coverage;
- immutable source artefacts and human corrections.

Structural checks do not prove fidelity. Word retention is a warning signal, not an acceptance criterion.

## Speaker mapping

1. Compare known attendee count with recurring machine-speaker count.
2. Review the normalised, unmerged transcript when diarisation is under-clustered.
3. Use bounded, numbered transcript passages for Michael's review by default; provide audio clips when he asks.
4. Record corrections at timestamp, segment, or quoted-phrase granularity.
5. Propagate human anchors only with adequate similarity and separation evidence.
6. Preserve per-turn assignment method and confidence.
7. Use `Unclear speaker` when evidence is insufficient.
8. Never use a mixed machine cluster as a named-speaker fallback or assign a silent attendee by elimination.
9. Split confirmed hand-offs into separate turns; do not invent composite speaker names.

A corrected speaker map invalidates dependent chapter inputs, polished chapters, minutes, and renders that embed the old map.

## Chapters

Fixed windows may bound model input but are not automatically semantic chapters.

- Propose topic transitions from transcript content.
- Snap final boundaries to actual turn edges.
- Require monotonic, non-overlapping boundaries.
- Account for every source turn exactly once with no gaps or duplication.
- Preserve chapter timestamps even when per-turn timestamps are removed for readability.

## Polish calibration

Before fan-out, polish representative early, middle, and late chapters. Read the changed passages, not merely metrics.

Reject a method that:

- mainly adjusts punctuation;
- leaves obvious fillers, duplicated fragments, false starts, or mangled sentences;
- collapses substantive turns into summary prose;
- changes attribution;
- weakens a claim, objection, caution, number, name, or uncertainty;
- cannot account for source turns.

Scale only after all representative pilots pass readability and substantive-coverage review.

## Worker and ledger contract

The deterministic coordinator owns splitting, serialisation, validation, promotion, and shared state. A judgement worker edits only its assigned immutable chapter input and writes a unique proposal.

Every source-turn index must occur exactly once in either:

- an output turn's `source_turn_indices`; or
- a logged `dropped_source_turn_indices` entry with an allowed reason.

Allowed drops are filler-only backchannels, immediate duplicate ASR fragments, or unintelligible fragments with no recoverable substance. Merge only adjacent same-speaker fragments inside one chapter. Never merge across speakers or chapter boundaries.

A timed-out worker may have written a complete proposal. Inspect and validate its output before retrying. A failed chapter must not invalidate successful siblings.

## Readability

For chaptered private-meeting output:

- render `**Speaker Name:** text`;
- remove per-turn timestamps unless requested;
- retain chapter timestamps;
- repair grammar and clear ASR damage conservatively;
- remove filler-only turns and false starts where meaning is unaffected;
- preserve meaningful hesitation, emotional tone, natural idiom, and uncertainty;
- mark unresolved wording rather than inventing a plausible repair.

A roughly 20% or greater cut from the parsed transcript deserves scrutiny, but neither high nor low retention decides acceptance. A 97–100% result may be punctuation-only; an 80% result may be valid if every substantive source turn is accounted for.

## Minutes

Minutes must distinguish:

- proposals;
- objections and alternatives;
- agreements;
- actual decisions;
- unresolved questions;
- risks;
- discussed owners and next steps.

Do not convert the dominant or longest-spoken proposal into consensus. Generate minutes from a stable high-fidelity transcript and recheck them after final transcript promotion.

## Corrections

Proper-noun and ASR corrections require evidence and a ledger. Human corrections outrank machine inference. A post-render correction invalidates the render; regenerate and reverify rather than patching scattered prose globally.

## Final verification

Before writing the canonical note, verify:

- ordered source provenance and expected duration;
- non-empty, monotonic transcript turns and final spoken content;
- explicit speaker uncertainty and confirmed mapping evidence;
- exact chapter and source-turn coverage;
- no unlogged drops or cross-speaker merges;
- early, middle, and late readability samples;
- minutes preserve disagreement and decision status;
- source embeds, frontmatter, wikilinks, and protected sections remain;
- required profile headings and note shape;
- proposed and written generated sections match;
- the final note has been re-read from disk.

Report partial state honestly. Missing canonical outputs or a failed gate means the workflow is blocked, not complete.
