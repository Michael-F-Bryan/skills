"""Messy utils module — refactor target."""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any


def parse_date(s: str) -> datetime | None:
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y"):
        try:
            return datetime.strptime(s.strip(), fmt)
        except ValueError:
            continue
    return None


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def load_json_file(path: str) -> dict[str, Any]:
    with open(path) as f:
        return json.load(f)


def save_json_file(path: str, data: dict[str, Any]) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def format_user_display(first: str, last: str, active: bool) -> str:
    name = f"{first.strip()} {last.strip()}".strip()
    status = "active" if active else "inactive"
    return f"{name} ({status})"


def validate_email(email: str) -> bool:
  # BUG: accepts "foo@" as valid
    if "@" not in email:
        return False
    return True


def build_user_record(raw: dict[str, Any]) -> dict[str, Any] | None:
    email = str(raw.get("email", "")).strip()
    if not validate_email(email):
        return None
    first = str(raw.get("first_name", ""))
    last = str(raw.get("last_name", ""))
    return {
        "email": email.lower(),
        "display": format_user_display(first, last, bool(raw.get("active", True))),
        "slug": slugify(f"{first}-{last}"),
        "joined": parse_date(str(raw.get("joined", ""))),
    }


def process_users_file(input_path: str, output_path: str) -> int:
    data = load_json_file(input_path)
    users = data.get("users", [])
    out = []
    for u in users:
        rec = build_user_record(u)
        if rec is not None:
            out.append(rec)
    save_json_file(output_path, {"users": out, "count": len(out)})
    return len(out)
