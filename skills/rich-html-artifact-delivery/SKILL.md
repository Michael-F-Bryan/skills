---
name: rich-html-artifact-delivery
description: Use when a locally complete HTML communication artefact must be packaged or delivered through a secret GitHub Gist and GistPreview.
---

# Rich HTML Artefact Delivery

`html-rich-communication` owns creation and local verification. This overlay owns only the final delivery boundary.

1. Require a locally rendered `index.html` with no material desktop/mobile defect.
2. Create a secret gist with `gh gist create`; do not pass `--public`.
3. Read the gist back with `gh api` and require `public: false`.
4. Return `https://gistpreview.github.io/?<gist-id>`.
5. Stop. Do not reopen the hosted preview unless the user reports a delivery defect or the page depends on host-specific script execution.

Prefer a genuinely self-contained file, but do not inline multi-megabyte runtimes. Render diagrams to static SVG. If packaging requires installing a browser framework or writing a custom bundler, the artefact is not in the default delivery lane.

If the hosted preview is blank, stale, or incompatible, stop this overlay and use `html-artifact-publishing`.
