# Decision separation and implementation semantics

Use these patterns when a broad capability set, an architecture choice, or a derived product makes several decisions look like one.

## Separate orthogonal decision axes

Do not collapse these into one multiple-choice answer:

- **Decision horizon:** the broader adoption, investment, or product decision the evidence must support.
- **Value-leading use case:** which users or workflow may benefit first.
- **First shared capability:** the smallest end-to-end behaviour worth building or testing.
- **Validation context:** where and with whom that capability will be tested first.

One user group can benefit sooner while a shared foundation remains the first milestone. A concrete scenario can orient the work without becoming the full acceptance criterion. If an answer mixes these axes, reflect the distinctions and ask one orthogonal follow-up before declaring the milestone resolved.

## Allocate outcomes before interfaces

When research has produced many plausible functions, adapt this funnel rather than running it as a questionnaire:

1. Define success without naming software.
2. Offer the inferred end-to-end chain for correction.
3. Separate mandatory product behaviour from acceptable manual work, scripts, and existing tools.
4. Walk through a concrete operating episode to expose actors, timing, hand-offs, and failure consequences.
5. Convert the episode into an explicit scope cut: required, useful if cheap, later, excluded, or unknown.
6. Remove a key dependency and establish the acceptable fallback and terminal boundary.
7. When several reliability risks compete, ask which omission, error, delay, or false certainty would destroy trust fastest.
8. Only then allocate behaviour to an interface, component, external tool, or human process.

The episode discovers decisions; it does not automatically define requirements. The trust-breaking failure usually gives a more useful reliability priority than a generic quality target.

## Establish semantics before mechanisms

When the user is considering a queue, worker, workflow engine, service split, or favourite framework, decompose the choice in this order:

1. **Durable hand-off:** what must be persisted before the producer may consider its work accepted?
2. **Failure guarantee:** who owns retries, and what must survive restarts or downstream outages?
3. **Processing granularity:** is work one idempotent job, several independently retryable stages, or a versioned workflow expected to fan out?
4. **Deployment boundary:** which responsibilities genuinely need independent scaling, release, security, or failure isolation?
5. **Mechanism:** only now compare database-backed jobs, queues, workflow engines, service boundaries, or specific frameworks.

A modular monolith does not require unreliable work inside an HTTP request. A separate worker does not by itself justify a workflow engine. Treat exact models, providers, and machine sizes as empirical choices when benchmarks can decide them more honestly than interview preference.

## Unpack required derived products

A required map, dashboard, score, recommendation, or other derived view is not yet a usable requirement. Resolve its dependency chain one decision at a time:

1. trusted raw observation or external authority;
2. correction rules and provenance;
3. minimum fidelity and confidence representation;
4. exact semantics of the derived claim;
5. hidden acquisition, alignment, calibration, retention, or processing that becomes mandatory;
6. accumulation, edit, restart, and reset boundaries; and
7. validation owner and evidence.

Scope acquisition separately from display. An optional visualisation may consume data that another required outcome makes mandatory.

## Preserve source evidence across reprocessing

When source material may be processed repeatedly:

- separate immutable source evidence from derived interpretations;
- record whether runs append, replace, or selectively preserve prior results;
- retain versions, parameters, timestamps, status, outputs, and selection provenance when runs are append-only;
- treat “current” as a projection or explicit selection rather than silent destruction of history; and
- decide how reviewed human corrections interact with later machine results.

Do not let a newer machine result silently displace reviewed human judgement unless the user explicitly chooses that authority model.