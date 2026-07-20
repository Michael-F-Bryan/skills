---
name: rendered-artifact-verification
description: Use when a renderer, generator, build tool, or deployment system materially transforms source into effective configuration or runtime output; not for ordinary static HTML communication pages.
---

# Rendered Artefact Verification

Verify the effective output when source text is not the runtime contract—for example rendered Compose, Kubernetes, generated schemas, deployment manifests, or bundled application output.

1. Run the real renderer.
2. Inspect the emitted artefact or effective configuration.
3. Assert on runtime-relevant fields.
4. Probe the real boundary when practical.

Do not load or apply this workflow merely because a static HTML document is viewed in a browser. `html-rich-communication` owns proportionate HTML checks. A source-level string match is weak evidence only when a generator can change its meaning.
