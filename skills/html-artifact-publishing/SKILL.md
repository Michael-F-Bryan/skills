---
name: html-artifact-publishing
description: Use when a locally valid HTML artefact has a blank, stale, or incompatible GistPreview rendering after publication.
---

# HTML Artefact Publishing Troubleshooting

Normal secret-Gist delivery belongs to `rich-html-artifact-delivery`. Load this skill only when the hosted rendering differs from the verified local file.

Check, in order:

1. The raw gist contains the expected title or hero text.
2. Gist visibility is secret (`public: false`).
3. The preview is using the intended filename and latest gist revision.
4. Inline module scripts are not relying on document-load events that already fired.
5. Runtime dependencies are not blocked by the host.

Prefer repairing the published file to adding another runtime layer. A stale preview may require a fresh secret gist; delete the stale gist after verifying the replacement. Do not turn every successful publication into a hosted browser QA pass.
