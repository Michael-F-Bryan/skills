---
name: obsidian-cli
description: Operate an Obsidian vault through its actual CLI.
---

# Obsidian CLI

## When to apply

- The user asks to work with an Obsidian vault from the terminal.
- The requested operation needs Obsidian CLI commands or application-managed vault state. Mere mention of notes, Markdown, or coding is not a trigger.
- The task is about using the Obsidian CLI rather than editing files directly.
- Do not activate for ordinary code changes, filesystem note edits, or generic working memory. Access the vault only when the task calls for it.

## Core workflow

1. Confirm the target vault before running note commands. If it is unclear, run `obsidian vaults`.
2. If `obsidian vaults` shows exactly one open vault, use that vault by default.
3. If the command or syntax is uncertain, check help first with `obsidian help`, `obsidian help <command>`, or `obsidian <command> --help`.
4. Prefer read-only discovery first: search or read, then expand with `links` and `backlinks` once you find a relevant note.
5. Prefer updating an existing note with `append` or `prepend` over rewriting a whole note or creating a new one.
6. Re-read afterwards when the write matters operationally.

## Safe defaults

- Target a specific vault explicitly whenever the CLI supports it.
- Return or summarise CLI output directly. Do not open the GUI unless the user asks for it.
- Ask before destructive operations such as `delete`, `move`, `rename`, `history:restore`, or sync/history restore operations.
- Preserve existing frontmatter, headings, wikilinks, and note structure unless the user asks for a rewrite.
- For daily-note work, resolve the note first with `daily:path` or inspect it with `daily:read` before writing.
- If help output does not show the operation you want, assume the CLI may not support it directly and use a different workflow instead of inventing syntax.

## Coding use

- Only for an explicitly requested vault update during coding, use the vault as the chosen destination; do not create an automatic coding log.
- Prefer updating an existing project, daily, or working note before creating a fresh note.
- Read `references/coding-workflows.md` when the task is about note choice, coding context, or what kind of update to record.
- Read `references/voice.md` only when you need help drafting the note text itself.

## Portability

- This skill may be installed into another project. Do not assume any repo-local layout.
- Always ask for or discover the vault path or vault target from the runtime environment.
- On WSL, `obsidian` may not be available on `$PATH`. If so, invoke the Windows CLI entrypoint directly, for example `"/mnt/c/Program Files/Obsidian/Obsidian.com" vaults`.

## Additional resources

- Start with [references/REFERENCE.md](references/REFERENCE.md) to choose the right supporting file.
