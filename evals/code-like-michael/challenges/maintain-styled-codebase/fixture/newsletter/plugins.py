from __future__ import annotations

import importlib.util
import sys
from collections.abc import Callable
from pathlib import Path

from newsletter.types import Article

ArticleFilter = Callable[[Article], bool]


def load_filters(plugin_dir: Path | None) -> list[ArticleFilter]:
    if plugin_dir is None or not plugin_dir.is_dir():
        return []

    filters: list[ArticleFilter] = []
    for path in sorted(plugin_dir.glob("*.py")):
        if path.name.startswith("_"):
            continue
        fn = _load_filter_function(path)
        if fn is not None:
            filters.append(fn)
    return filters


def apply_filters(article: Article, filters: list[ArticleFilter]) -> bool:
    for filter_fn in filters:
        if not filter_fn(article):
            return False
    return True


def _load_filter_function(path: Path) -> ArticleFilter | None:
    module_name = f"newsletter_plugin_{path.stem}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        return None

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    candidate = getattr(module, "filter_article", None)
    if candidate is None or not callable(candidate):
        return None
    return candidate
