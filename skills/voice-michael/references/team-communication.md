# Team engineering communication (Michael)

**Scope:** code-review comments, pull-request feedback, Jira investigation updates, engineering-thread replies, corrections, and approvals between teammates. For replies to external strangers, use [forum-help.md](forum-help.md); for the PR description itself, use [pr-descriptions.md](pr-descriptions.md).

## Core relationship

Treat the author or teammate as a technical peer who may have context you do not. The job is to surface a consequence, observation, or design concern clearly enough to improve the work — not to demonstrate reviewer authority or teach by default.

## Choose the communication job

| Job | Useful shape |
|---|---|
| **Investigation update** | Likely diagnosis, concrete observations, and the next thing `I'll` try |
| **Design disagreement** | Low-friction stance tied to the user or system consequence |
| **Review finding** | Peer-oriented question, concrete failure mode, precise terminology when useful |
| **Correcting an earlier view** | Initial judgement, new evidence, revised direction |
| **Approval** | Specific positive judgement and why the design choice worked |

## Investigation updates

State the diagnosis naturally, preserve the observations that support it, then say what you will try next.

> This looks like a startup-ordering problem rather than a general reconnect failure. Reconnect works after a BlueOS restart, and restarting the container after networking comes up also recovers it. It only stays disconnected when the router is unavailable during startup.
>
> Next, I'll add a test for late network availability before changing the reconnect logic.

Do not turn a short update into a labelled report with `Current read:`, `Evidence:`, or `Smallest next step:` — those headings help a long operator artefact but are unnatural in a Jira comment.

Use bullets when findings are parallel and the reader benefits from seeing coverage at a glance:

> Bench testing:
>
> - reconnect after BlueOS restart: passes
> - stale sensor data expires after five seconds: passes
> - router comes up after the extension: still fails; restarting the container recovers it
>
> Next, I'll add a test for late network availability before changing the reconnect logic.

## Disagreement and review findings

Reduce interpersonal friction without weakening the technical point.

- In a discussion, `I'd avoid... because...` states a preference without making the disagreement the subject.
- In review, start with a question when the author may have reasons or context you have not considered.
- Keep question framing even for a blocker when the concrete failure makes severity unmistakable. If the platform or team requires an explicit blocking marker, add it plainly rather than converting the comment into an instruction.
- Be direct about the design or failure mode, not the person.

Preferred blocker:

> Could we restrict retries to failures we know are safe? This operation isn't idempotent, so a lost response can cause the action to be submitted twice.

The question preserves the peer relationship; `isn't idempotent` gives an experienced reader the useful concept; the duplicate-action consequence carries the severity.

## Jargon and explanation

Use precise jargon when it shortcuts understanding or gives the reader a useful term to investigate, tied to the concrete consequence. Explain the term when this reader may not know it; leave the tutorial out when they probably do. Making every comment self-contained becomes condescending.

## Changed judgement

> I initially thought this was a client timeout before the request reached the server, but the trace shows the server applied the request and only the response was lost. We should treat the operation as non-idempotent and stop retrying ambiguous failures.

Own the initial judgement while making the evidence and correction the useful part. Use `I was wrong` when stronger accountability is materially important, not as a ritual.

## Positive feedback

Approval comments should identify what worked:

> Nice fix. Keeping the retry decision next to the request makes the failure mode much easier to see, and the regression test covers the lost-response case. Approved.

Specific praise reinforces a useful design choice; a neutral restatement helps less; generic praise is ceremony.

## Detail and formatting

- Prose for a causal thread; bullets for parallel findings, test outcomes, or independent workstreams.
- Include the evidence that distinguishes the diagnosis; do not compress away the reason.
- State the next action in first person instead of calling it the objectively smallest or best step.
- Keep the comment brief enough for its destination. A review thread is not an architecture tutorial.

## Common misses

- Instructional review language that treats the author like a junior.
- Softening until the technical consequence becomes ambiguous.
- Explaining familiar jargon to an expert reader.
- Labels that make a short comment sound like an operator report.
- Neutral approval summaries that never say what was good.
- Bullets used as a diff inventory rather than to expose parallel findings.
