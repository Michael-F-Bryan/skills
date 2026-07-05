# Publishing bundled artefacts as secret gists

Use this reference when sharing `final/bundle.html` (or a renamed copy) through GitHub Gist and [GistPreview](https://gistpreview.github.io/).

## Default visibility

Use **secret gists by default** unless the user explicitly asks for public visibility. Secret gists are accessible to anyone with the link, but they do not appear in public gist listings or search the same way public gists do.

## Create and verify a secret gist

Upload the bundled artefact. Renaming to `index.html` before upload makes GistPreview work without specifying a filename.

```bash
FILE=/path/to/_working/<topic>/final/bundle.html
# Optional: cp "$FILE" /tmp/index.html && FILE=/tmp/index.html
DESC="Short private description"
URL=$(gh gist create "$FILE" --desc "$DESC")
GIST_ID=${URL##*/}
FILENAME=$(basename "$FILE")

gh api "gists/$GIST_ID" --jq '{id, public}'
gh api "gists/$GIST_ID" --jq '.files[] | {filename, raw_url}'
```

Do not pass `--public` unless public discoverability is explicitly desired.

## GistPreview URL

Rendered preview link:

```text
https://gistpreview.github.io/?<gist_id>/<filename>
```

Examples:

- `https://gistpreview.github.io/?abc123def456/bundle.html`
- `https://gistpreview.github.io/?abc123def456/index.html`
- `https://gistpreview.github.io/?abc123def456` — previews `index.html` or the first file if no filename is given

Verify before reporting:

```bash
curl -Ls -o /dev/null -w '%{http_code} %{url_effective}\n' "https://gist.github.com/<owner>/<gist_id>"
curl -Ls -o /dev/null -w '%{http_code} %{size_download} %{url_effective}\n' "<raw_url>"
curl -Ls -o /dev/null -w '%{http_code} %{url_effective}\n' "https://gistpreview.github.io/?<gist_id>/<filename>"
```

Give the user the **GistPreview URL** for rendered viewing, not only the raw gist URL.

Record gist id, raw URL, and preview URL in `_working/<topic>/README.md`.

## If a gist was accidentally created public

GitHub/`gh` does not provide a reliable in-place toggle from public to secret. Use replacement workflow:

1. Recreate the same file as a new secret gist.
2. Verify the new gist reports `public: false` and raw/preview URLs return `200`.
3. Delete the public original:
   ```bash
   gh gist delete <old_public_gist_id> --yes
   ```
4. Verify the old gist no longer resolves through the API:
   ```bash
   gh api "gists/<old_public_gist_id>" || true
   ```
5. Update working README and any shared links with the replacement URLs.

## Pitfall

`gh gist create --public` is sticky in practice: do not use it for work/project artefacts just because the content is not a credential. Strategy, customer context, and internal docs should start link-only.
