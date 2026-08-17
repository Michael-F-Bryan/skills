# Evidence and elicitation provenance

Use this reference whenever an interview answer, candidate, confirmation, or source-derived claim may be mistaken for human-owned judgement.

## Provenance classes

Classify a candidate or answer **before** interpreting or accepting it:

| Class | Meaning | What it can establish |
| --- | --- | --- |
| `human-originated` | The user supplies an unprompted judgement, concrete episode, criterion, consequence, boundary, or correction in their own terms. | Human-owned evidence, subject to confidence and corroboration. |
| `source-explicit` | The source directly states or shows the claim. | A source fact; not human judgement unless the user independently adopts it. |
| `source-inferred` | The agent derives a plausible claim from one or more sources. | A hypothesis to verify, never a settled decision. |
| `assistant-proposed` | The agent supplies a candidate, menu, synthesis, wording, or interpretation. | A prompt for recognition/correction only. |
| `reviewer-proposed` | An external reviewer supplies a candidate or finding. | Review evidence or a proposal; it needs disposition by the authorised decision owner. |
| `historical-only` | A superseded answer, design, implementation, or prior decision retained for traceability. | Context and explanation of change, not current direction. |

A candidate’s origin does not change because the user selects it from a menu. Record the menu or framing that preceded the selection.

## Prompted evidence and assent

Prompting can elicit human-originated evidence when the user adds a concrete episode, personal observation, criterion, consequence, or correction that was not contained in the prompt. Record that added material, not merely the option letter.

A bare confirmation of an assistant-framed statement—“yes”, “that sounds right”, or an option selected without independent detail—is **assistant-framed assent**. It may provisionally close a low-stakes row when the consequence is reversible and does not set a load-bearing boundary. It cannot establish a load-bearing decision without at least one independent consequence, episode, criterion, or source.

Do not manufacture independence by asking repeated “are you sure?” questions. After assent, ask one substantive question that can supply the missing discriminator, then move on or stop based on its decision value.

When presenting recognition choices:

- preserve the candidate wording and its provenance;
- show consequences without implying a preferred answer;
- allow combinations, qualification, rejection, and the user’s own wording;
- treat rejection, correction, and “none” as evidence about the framing.

## Confidence and corroboration

Confidence describes the evidence state, not the assistant’s fluency. Record a concise level such as `high`, `medium`, `low`, or `unknown`, plus why. Keep the user’s uncertainty visible (`likely`, `I think`, `not sure`, `I don’t know`) at the point of use.

Corroboration means independent support, not repetition of the same assistant framing. Suitable corroboration includes:

- a separate concrete episode or consequence from the user;
- a distinct source that explicitly supports the claim;
- an independently authored reviewer finding, with its disposition recorded; or
- a later answer that supplies a non-derivative criterion or boundary.

Repeated assistant summaries, option letters, paraphrases, or confirmations are not corroboration. If support conflicts, preserve both claims, name the conflict, lower confidence, and ask only if resolving it could change the authorised output.

## Entry minimum

For each consequential answer or candidate, keep:

- question and decision consequence;
- source basis or `human judgement only`;
- verbatim answer or exact candidate wording;
- provenance class and any preceding prompt/framing;
- confidence and corroboration state;
- interpretation, clearly labelled as interpretation; and
- effect on scope, ownership, authority, output, or next question.

An interpretation can guide the next question, but it cannot upgrade `assistant-proposed`, `source-inferred`, or `assistant-framed assent` into human-owned evidence. The current projection should cite the evidence entries supporting every load-bearing boundary.
