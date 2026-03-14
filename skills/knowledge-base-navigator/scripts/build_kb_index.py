#!/usr/bin/env python3
"""
Build kb-index.json from markdown under PARA roots.

Scans .md files under 1-projects/, 2-areas/, 3-resources/, 4-archives/ (one level
of containers), parses YAML frontmatter and optional first-line summary, and
emits a JSON array matching the structure in references/optional-kb-index.md.

Run after maintenance (e.g. after para-custodian) to refresh kb-index.json.

Usage:
  python build_kb_index.py --repo /path/to/repo [--out path/to/kb-index.json] [--exclude-archives]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

PARA_ROOTS = ("1-projects", "2-areas", "3-resources", "4-archives")


def parse_frontmatter_and_body(content: str) -> tuple[dict, str]:
    """Split YAML frontmatter and body. Returns (frontmatter_dict, body)."""
    if not content.strip().startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    try:
        fm = yaml.safe_load(parts[1]) or {}
        return fm, parts[2]
    except Exception:
        return {}, content


def first_heading(line: str) -> str | None:
    """Extract text from a line like '# Title' or '## Title'."""
    m = re.match(r"^#+\s+(.+)$", line.strip())
    return m.group(1).strip() if m else None


def first_blockquote_or_line(body: str) -> str | None:
    """First blockquote line (e.g. '> summary') or first non-empty line."""
    for line in body.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith(">"):
            return s.lstrip("> ").strip()
        return s
    return None


def relative_path(path: Path, repo_root: Path) -> str:
    """Path as string relative to repo root, using forward slashes."""
    return path.relative_to(repo_root).as_posix()


def index_note(path: Path, repo_root: Path) -> dict | None:
    """Read one .md file and return an index entry dict, or None to skip."""
    text = path.read_text(encoding="utf-8", errors="replace")
    fm, body = parse_frontmatter_and_body(text)

    # Derive root and container from path: e.g. 3-resources/atomic-notes/foo.md
    rel = relative_path(path, repo_root)
    parts = rel.split("/")
    if len(parts) < 3:
        return None
    root = parts[0]
    container = parts[1]
    if root not in PARA_ROOTS:
        return None

    title = fm.get("title")
    if not title:
        for line in body.splitlines():
            t = first_heading(line)
            if t:
                title = t
                break
    if not title:
        title = path.stem.replace("-", " ").title()

    summary = fm.get("summary")
    if not summary:
        summary = first_blockquote_or_line(body)

    entry = {
        "path": rel,
        "title": title,
        "aliases": fm.get("aliases") or [],
        "kind": fm.get("kind") or "note",
        "root": root,
        "container": container,
        "topics": fm.get("topics") or [],
        "summary": summary or "",
        "related": fm.get("related") or [],
    }
    return entry


def collect_notes(repo_root: Path, exclude_archives: bool) -> list[dict]:
    """Walk PARA roots (one level of containers) and collect index entries."""
    repo_root = repo_root.resolve()
    entries = []
    roots = [r for r in PARA_ROOTS if r != "4-archives" or not exclude_archives]

    for root_name in roots:
        root_dir = repo_root / root_name
        if not root_dir.is_dir():
            continue
        for container_path in root_dir.iterdir():
            if not container_path.is_dir():
                continue
            for path in container_path.glob("*.md"):
                if path.name.startswith("."):
                    continue
                entry = index_note(path, repo_root)
                if entry:
                    entries.append(entry)

    return entries


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build kb-index.json from PARA markdown (frontmatter + paths)."
    )
    parser.add_argument(
        "--repo",
        type=Path,
        default=Path.cwd(),
        help="Repository root (default: current directory)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output path for kb-index.json (default: stdout)",
    )
    parser.add_argument(
        "--exclude-archives",
        action="store_true",
        help="Do not include notes under 4-archives/",
    )
    args = parser.parse_args()

    if not args.repo.is_dir():
        print(f"Not a directory: {args.repo}", file=sys.stderr)
        return 1

    entries = collect_notes(args.repo, args.exclude_archives)
    out = json.dumps(entries, indent=2, ensure_ascii=False)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(out, encoding="utf-8")
    else:
        print(out)

    return 0


if __name__ == "__main__":
    sys.exit(main())
