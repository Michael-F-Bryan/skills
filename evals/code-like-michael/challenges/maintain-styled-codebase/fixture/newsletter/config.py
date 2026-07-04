from __future__ import annotations

import json
from pathlib import Path

from newsletter.types import AppConfig, ConfigError, FeedConfig, MailConfig


def load_config(path: Path) -> AppConfig:
    if not path.is_file():
        raise ConfigError(str(path), "file not found")
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ConfigError(str(path), f"invalid JSON: {exc.msg}") from exc
    if not isinstance(raw, dict):
        raise ConfigError(str(path), "root must be a JSON object")

    feeds: list[FeedConfig] = []
    feeds_raw = raw.get("feeds")
    if not isinstance(feeds_raw, list) or not feeds_raw:
        raise ConfigError(str(path), "feeds must be a non-empty list")
    for index, item in enumerate(feeds_raw):
        if not isinstance(item, dict):
            raise ConfigError(str(path), f"feeds[{index}] must be an object")
        feeds.append(
            FeedConfig(
                name=_require_str(item, "name", str(path), f"feeds[{index}]"),
                url=_require_str(item, "url", str(path), f"feeds[{index}]"),
            )
        )

    keywords_raw = raw.get("keywords") or []
    if not isinstance(keywords_raw, list):
        raise ConfigError(str(path), "keywords must be a list")
    keywords = tuple(str(k).strip().lower() for k in keywords_raw if str(k).strip())

    plugin_dir = raw.get("plugin_dir")
    if plugin_dir is not None and not isinstance(plugin_dir, str):
        raise ConfigError(str(path), "plugin_dir must be a string path")

    mail_raw = raw.get("mail")
    mail = _parse_mail(mail_raw, str(path)) if mail_raw is not None else None

    return AppConfig(
        db_path=_require_str(raw, "db_path", str(path)),
        feeds=tuple(feeds),
        keywords=keywords,
        score_threshold=float(raw.get("score_threshold", 0.5)),
        plugin_dir=plugin_dir,
        mail=mail,
    )


def _parse_mail(raw: object, path: str) -> MailConfig:
    if not isinstance(raw, dict):
        raise ConfigError(path, "mail must be an object")
    to_raw = raw.get("to")
    if not isinstance(to_raw, list) or not to_raw:
        raise ConfigError(path, "mail.to must be a non-empty list")
    return MailConfig(
        smtp_host=_require_str(raw, "smtp_host", path, "mail"),
        smtp_port=int(raw.get("smtp_port", 587)),
        username=_require_str(raw, "username", path, "mail"),
        password=_require_str(raw, "password", path, "mail"),
        from_addr=_require_str(raw, "from", path, "mail"),
        to_addrs=tuple(str(a) for a in to_raw),
        use_tls=bool(raw.get("use_tls", True)),
    )


def _require_str(raw: dict[str, object], key: str, path: str, scope: str = "root") -> str:
    value = raw.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ConfigError(path if scope == "root" else scope, f"{key} must be a non-empty string")
    return value.strip()
