# Obsidian CLI Command Reference

Use this file as a command cheat sheet. Verify current syntax with `obsidian help`, `obsidian help <command>`, or `obsidian <command> --help` before relying on memory.

## Start here

- Need to discover capabilities: `obsidian help`
- Need the version: `obsidian version`
- Need vault information: `obsidian vault`, `obsidian vaults`, `obsidian vault:open`

## Vault discovery

1. If the target vault is unclear, run `obsidian vaults`.
2. If there is exactly one open vault, use it.
3. Otherwise choose from the listed vaults before running note commands.
4. If the CLI supports explicit vault targeting for the command you need, confirm the exact syntax with help and pass it explicitly.

## Read and search

- Read a note: `read`
- List or inspect files: `file`, `files`, `folder`, `folders`
- Search note content: `search`
- Search with surrounding context: `search:context`
- Open a search result in Obsidian: `search:open`
- Read a random note: `random:read`

Suggested sequence:

1. Confirm the vault target.
2. Use `search` or `search:context` to find the first promising note.
3. Use `read` once you know the target.
4. Use `links` and `backlinks` on that note to discover adjacent context.

## Create and edit

- Create a note: `create`
- Add content to the end: `append`
- Add content to the start: `prepend`
- Move a note: `move`
- Rename a note: `rename`
- Delete a note: `delete`

## Write verification checklist

1. Resolve the target vault and note.
2. Read the current content first.
3. Prefer `append` or `prepend` for local edits.
4. Re-read the note after writing when placement or content matters.
5. Ask before `move`, `rename`, `delete`, or restore-style operations.

## Daily notes

- Discover today's note path: `daily:path`
- Read today's daily note: `daily:read`
- Append to today's daily note: `daily:append`
- Prepend to today's daily note: `daily:prepend`

Suggested sequence:

1. Use `daily:path` or `daily:read` first.
2. Then write with `daily:append` or `daily:prepend`.
3. Re-read if you need to confirm placement.

## Links and structure

- Notes linking to a target: `backlinks`
- Links from a note: `links`
- Unresolved links: `unresolved`
- Orphan notes: `orphans`
- Dead-end notes: `deadends`
- Note outline: `outline`

Use these when the task is about note organisation rather than note text.

## Properties, tags, and tasks

- Aliases: `aliases`
- All properties or note properties: `properties`
- Read one property: `property:read`
- Set one property: `property:set`
- Remove one property: `property:remove`
- Tags: `tags`, `tag`
- Tasks: `tasks`, `task`
- Word counts: `wordcount`

## Templates

- List or inspect templates: `templates`
- Read a template: `template:read`
- Insert a template: `template:insert`

## History and recovery

- File history overview: `history`, `history:list`
- Read a historical version: `history:read`
- Restore a historical version: `history:restore`
- Open history in Obsidian: `history:open`
- Diff versions: `diff`

Treat restore-style commands as destructive until confirmed.

## Other useful areas

- Bookmarks: `bookmarks`, `bookmark`
- Commands and hotkeys: `commands`, `command`, `hotkeys`, `hotkey`
- Publish: `publish:site`, `publish:list`, `publish:status`, `publish:add`, `publish:remove`, `publish:open`
- Sync: `sync`, `sync:status`, `sync:history`, `sync:read`, `sync:restore`, `sync:open`, `sync:deleted`
- Workspace and tabs: `workspace`, `workspaces`, `workspace:save`, `workspace:load`, `workspace:delete`, `tabs`, `tab:open`, `recents`
- Plugins, themes, and snippets: `plugins`, `plugin:enable`, `plugin:disable`, `plugin:install`, `plugin:uninstall`, `themes`, `theme:set`, `snippets`, `snippet:enable`, `snippet:disable`

## Help patterns

- General help: `obsidian help`
- Command help: `obsidian help search`
- Subcommand help: `obsidian help daily:append`
- Alternate form: `obsidian search --help`

If help output does not show the operation you want, assume the CLI may not support it directly and fall back to a different workflow instead of inventing syntax.
