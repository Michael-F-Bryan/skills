# Session email review workflow

Use this as the practical workflow when asked to review recent CSU/DUM-C emails and decide what belongs in Obsidian.

## Source-selection rule

For CSU email reviews, start from the CSU Microsoft Graph mailbox path, not Michael's personal Gmail/Himalaya mailbox.

Primary target:

- `/me` via the `csu-teams` Microsoft Graph token, which resolves to `michael.bryan@csu-ses.com.au`.
- Token file: `~/.hermes/csu-teams-graph-token.json`.
- Required mail scopes include `Mail.Read`, `Mail.Read.Shared`, and `Mail.ReadBasic`.

Probe likely role/shared mailboxes explicitly, for example:

- `deputycapability@csu-ses.com.au`
- `training@csu-ses.com.au`
- `recruitment@csu-ses.com.au`
- `administration@csu-ses.com.au`
- `admin@csu-ses.com.au`
- `manager@csu-ses.com.au`
- `welfareteam@csu-ses.com.au`

If Graph returns `403 Authorization_RequestDenied` for a role mailbox, record that scope limit in the summary and final report. Do not imply those role mailboxes were reviewed. Messages from those roles that land in Michael's mailbox are still in scope.

Use Himalaya/Gmail only when the user explicitly asks for the personal mailbox, when Graph is unavailable and you label the fallback clearly, or when a known DUM-C source only exists in that mailbox.

## Working-directory stance

Treat the pull directory as scratch only. It is useful for grouping and summarising, but it must not become a provenance dependency for any saved note.

Recommended scratch artefacts:

- `download-index.json` or `deduped-messages.json` — mailbox/folder, provider ID, subject, sender, recipients, dates, message-id, attachment names, and local scratch paths.
- `text/<mailbox>__<folder>__<slug>.txt` — extracted readable body for quick review.
- `raw-eml/` — exported raw MIME sources.
- `attachments/` — temporary attachment downloads before promotion into the vault.
- `probe-log.json` — which mailboxes/folders were readable, blocked, empty, or errored.

## Review sequence

1. Pull the requested time window into a timestamped scratch directory.
2. Build a small index before summarising so later claims can be traced to specific messages.
3. Include both received and sent mail for the readable CSU mailbox unless the user narrows the scope.
4. Probe role/shared mailboxes and record access failures separately from true zero results.
5. Group messages by real-world event/thread, not by individual email.
6. Summarise the grouped events for Michael before writing notes unless he has already asked for note creation.
7. For each group, decide: ignore, summarise only, update existing note, or create new note.
8. Before any Obsidian note links source material, copy the relevant `.eml` or attachment into `Attachments/DUM-C/` and link that stable copy.
9. Re-read saved notes and check no `/tmp`, `_working`, cache, or scratch path remains.

## Microsoft Graph pull pattern

Use the existing Graph token and refresh it with device-code auth when expired. A durable helper script is better than a long inline one-liner; long background Python snippets can be truncated or mangled.

Minimum implementation requirements:

1. Resolve `/me` and confirm the identity is `michael.bryan@csu-ses.com.au`.
2. Query at least `Inbox` and `SentItems` for the requested window.
3. Probe each role/shared mailbox with the same folders and capture `403` responses in `probe-log.json`.
4. Download raw MIME (`/$value`) for selected messages into `raw-eml/`.
5. Extract readable text into `text/`.
6. Deduplicate by `internetMessageId`, not by subject alone.
7. Preserve Graph metadata: `id`, `internetMessageId`, `receivedDateTime`, `sentDateTime`, `from`, `toRecipients`, `ccRecipients`, `hasAttachments`, `_mailbox`, `_folder`, `_raw_path`, and `_text_path`.
8. Filter vendor/system noise only after indexing, so the summary can report scan counts honestly.

## Recent-email pull pattern with Himalaya

Use this only for personal Gmail/Himalaya mailbox checks or clearly labelled fallback work.

When the available source is Michael's configured Himalaya mailbox, use a broad-but-controlled pass rather than only checking one visible folder:

1. Get the local date/time first so "last week" has a concrete boundary and timezone.
2. List accounts and folders, then search at least:
   - the likely SES label/folder, e.g. `Personal/SES`;
   - `INBOX`, because some SES mail may still be there;
   - `[Gmail]/All Mail`, because Gmail labels and inbox state can hide relevant messages from narrow folder searches;
   - `[Gmail]/Sent Mail`, if replies or approvals may have been sent.
3. Use separate simple queries when Himalaya's query parser returns blank output for complex boolean expressions. Prefer several narrow calls such as `from dfes`, `to csu-ses`, `subject MOVAT`, `subject eAcademy`, and `body CSU` over one parenthesised query.
4. Export any messages that become sources with `himalaya message export --folder '[Gmail]/All Mail' --full --destination <scratch>.eml <id>`, then promote the selected `.eml` files into `Attachments/DUM-C/` before linking them.
5. Parse the exported `.eml` headers for `Message-ID`, `Date`, `From`, `To`, `Cc`, and `Subject` so frontmatter is based on the raw source rather than the rendered body.
6. If the configured account is only Michael's personal mailbox, explicitly state the scope limitation in the final report. Do not imply that shared or role mailboxes such as `deputycapability@csu-ses.com.au` were covered unless they were actually queried.

Duplicate-looking automated notifications should be grouped into one event note when they refer to the same real-world action. Preserve all distinct `Message-ID` values and source `.eml` links in that one note.

## What to preserve from email metadata

Preserve enough metadata that the original can be found again without relying on the scratch directory:

- subject;
- sender and recipients;
- sent/received timestamp with timezone when known;
- `Message-ID` / `internetMessageId`;
- source mailbox/folder when useful;
- attachment filenames and stable vault copies if used.

## Pitfalls captured from the June 2026 sessions

1. A good temporary review directory is not a durable source archive. If a future note needs to cite source evidence, promote the evidence into the vault first. If the source does not need to be retained, quote or summarise the relevant facts directly in the note and omit scratch paths entirely.
2. Checking `Personal/SES`, Gmail `INBOX`, and Gmail `Sent Mail` can produce plausible-looking DUM-C notes while missing the actual CSU mailbox. For requests about "my CSU emails", use the Graph CSU mailbox first.
3. Treat role-mailbox `403` as a scope limitation, not as an empty mailbox.
4. Do not let automated-notification notes crowd out higher-signal CSU threads. The role-context threshold should surface personnel/status changes, training planning, admin-state changes, and audit-worthy decisions from the CSU mailbox.
