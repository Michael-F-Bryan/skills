# Decision separation and implementation semantics

Use these distinctions when one example, capability, or mechanism makes several decisions look like one.

## Keep decision axes separate

Distinguish:

- **Decision horizon:** the broader adoption, investment, product, or policy decision.
- **Value-leading use case:** who or what may benefit first.
- **First shared capability:** the smallest end-to-end behaviour worth testing or building.
- **Validation context:** where and with whom it will be tested.

A use case can lead value while a shared foundation is the first milestone. A scenario can orient work without becoming the full acceptance criterion. If an answer mixes axes, reflect the separation and ask one orthogonal, decision-useful follow-up.

## Allocate outcomes before mechanisms

Define success without naming software. Separate required behaviour from acceptable manual work, existing tools, later scope, exclusions, and unknowns. Use a concrete episode to expose actors, hand-offs, timing, and trust-breaking consequences; then allocate the outcome to a product, another tool, or a human process. The episode reveals decisions, not automatic requirements.

## Establish semantics before mechanisms

Before comparing a queue, worker, workflow engine, service split, model, provider, or framework, establish:

1. durable hand-off: what must persist before work is accepted;
2. failure semantics: who owns retry, recovery, and restart survival;
3. processing granularity: one idempotent job, independently retryable stages, or a versioned workflow; and
4. genuine boundary: what needs independent scaling, release, security, or failure isolation.

Mechanism is a later empirical choice unless it changes one of those semantics.

## Unpack derived products

For a required map, dashboard, score, recommendation, or other derived view, establish the trusted source, correction and provenance rules, minimum fidelity/confidence, exact claim semantics, hidden acquisition or alignment, lifecycle/reset boundary, and validation owner. Scope acquisition separately from display. A newer machine result must not silently displace reviewed human judgement.
