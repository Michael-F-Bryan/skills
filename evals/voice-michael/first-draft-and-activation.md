# First-draft and negative activation cases

Sanitised historical failure shapes; generic scenarios below are fixtures, not audit excerpts or quotations. Compare actual first drafts with source facts and reader needs. Do not score semantic success with string-presence checks.

## Peer update, first draft

Prompt: “Draft a short engineering-thread update: reconnect after a service restart passes, stale data expiry passes, late network startup still fails; the next action is a regression before changing retry logic.”

Useful shape: preserve the parallel evidence, then own the next action in ordinary prose. Near miss: a polished two-line `Current read` / `Smallest next step` summary that hides which cases were exercised. Judge the first output, not only a rewrite after correction.

## Reviewer context, first draft

Run [the existing PR scenario](pr-description.md). Compare motivation, resulting behaviour and the shared event-source rationale. A file inventory, CI checklist or architecture lesson is not evidence of a better description. No word-count target.

## Explanation, first draft

Prompt: “Explain why a small enum fits a tool with one implementation today. The reader is an experienced engineer.”

Useful shape: give the choice and concrete caller/compiler consequences, then stop when the trade-off has landed. Near miss: broad clean-architecture taxonomy or an over-complete conclusion.

## Negative activation

- “Fix a typo in this README.” No working folder, interview, independent reviewer, Obsidian CLI, brand styling or note callout policy is needed.
- “Add a regression in this Python package.” Engineering guidance applies; Temporal only if it actually uses that SDK. No automatic vault log.
- “Create a company HTML evidence brief.” HTML and voice may apply; personal branding does not unless requested. Publication remains with its owner.
- “Read this known note path from disk.” Direct read, not a retrieval-agent pipeline or Obsidian CLI requirement.
- “I’m unsure which option to pick; give me advice.” Do not turn ordinary advice into a recorded structured interview unless requested.

For each case record actual activation, output and reasoned judgement. Supplying a skill inline tests adherence, not discovery. Behavioural comparison remains unrun until an agent has generated and a person/agent has assessed the actual outputs.
