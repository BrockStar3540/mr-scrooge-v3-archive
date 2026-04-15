"""Hierarchical, hot-reloadable configuration system."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


class ConfigStore:
    """Hierarchical config store with dot-path access and file-backed persistence."""

    def __init__(self, config_path: Path | None = None) -> None:
        self._data: dict[str, Any] = {}
        self._path = config_path

    def load(self, path: Path | None = None) -> None:
        p = path or self._path
        if p and p.exists():
            with open(p) as f:
                self._data = json.load(f)
            logger.info("Config loaded from %s", p)

    def save(self, path: Path | None = None) -> None:
        p = path or self._path
        if p:
            with open(p, "w") as f:
                json.dump(self._data, f, indent=2)

    def get(self, dotpath: str, default: Any = None) -> Any:
        """Get a value by dot-separated path, e.g. 'strategies.trend_engine.enabled'."""
        keys = dotpath.split(".")
        node = self._data
        for key in keys:
            if isinstance(node, dict) and key in node:
                node = node[key]
            else:
                return default
        return node

    def set(self, dotpath: str, value: Any) -> None:
        keys = dotpath.split(".")
        node = self._data
        for key in keys[:-1]:
            if key not in node or not isinstance(node[key], dict):
                node[key] = {}
            node = node[key]
        node[keys[-1]] = value

    def section(self, prefix: str) -> dict[str, Any]:
        """Return a whole config section as a dict."""
        result = self.get(prefix)
        return result if isinstance(result, dict) else {}

    def as_dict(self) -> dict[str, Any]:
        return self._data.copy()
