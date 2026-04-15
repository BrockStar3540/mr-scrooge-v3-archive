"""Hierarchical, hot-reloadable configuration system.

Features:
  - Dot-path access (e.g. 'gates.rr.reversal_min_rr')
  - Schema validation on boot
  - File watcher for hot reload
  - Environment variable overrides (SCROOGE_SECTION_KEY=value)
  - ConfigChanged event emission on reload
  - Config change history tracking
"""

from __future__ import annotations

import json
import logging
import os
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Schema definitions — valid types and ranges per config field
# ---------------------------------------------------------------------------

# Format: dotpath -> (type, min, max, required)
# None for min/max means no constraint
_SCHEMA: dict[str, tuple[type, Any, Any, bool]] = {
    # Runtime
    "runtime.scan_interval_seconds": (int, 10, 3600, True),
    "runtime.dry_run": (bool, None, None, True),
    "runtime.log_level": (str, None, None, False),
    # Risk
    "risk.max_open_positions": (int, 1, 20, True),
    "risk.max_daily_loss_pct": (float, 0.1, 10.0, True),
    "risk.margin_utilization": (float, 0.01, 1.0, True),
    # Gates
    "gates.spread.max_spread_jpy": (float, 0.5, 20.0, False),
    "gates.spread.max_spread_default": (float, 0.1, 10.0, False),
    "gates.spread.spread_pct_of_half": (float, 0.01, 0.50, False),
    "gates.rr.reversal_min_rr": (float, 0.5, 5.0, False),
    "gates.rr.trend_min_rr": (float, 0.5, 5.0, False),
    "gates.regime_floor.min_score": (float, -10, 5, False),
    # Strategies
    "strategies.trend.size_full": (float, 0.1, 1.0, False),
    "strategies.trend.size_stretch": (float, 0.1, 1.0, False),
    # Features
    "features.atr.period": (int, 5, 50, False),
    "features.bollinger.period": (int, 5, 50, False),
    "features.bollinger.std_dev": (float, 1.0, 5.0, False),
    # Dashboard
    "dashboard.port": (int, 1024, 65535, False),
}

# Required top-level sections
_REQUIRED_SECTIONS = ["runtime", "risk", "features", "gates", "strategies"]


class ConfigValidationError(Exception):
    """Raised when config fails validation."""


class ConfigStore:
    """Hierarchical config store with validation, hot reload, and env overrides."""

    def __init__(self, config_path: Path | None = None) -> None:
        self._data: dict[str, Any] = {}
        self._path = config_path
        self._change_history: list[dict[str, Any]] = []
        self._on_change_callbacks: list[Callable[[dict[str, Any]], None]] = []
        self._watcher_thread: threading.Thread | None = None
        self._watcher_stop = threading.Event()
        self._last_mtime: float = 0.0

    def load(self, path: Path | None = None) -> None:
        p = path or self._path
        if p and p.exists():
            with open(p) as f:
                self._data = json.load(f)
            self._last_mtime = p.stat().st_mtime
            logger.info("Config loaded from %s", p)

    def save(self, path: Path | None = None) -> None:
        p = path or self._path
        if p:
            with open(p, "w") as f:
                json.dump(self._data, f, indent=2)

    def get(self, dotpath: str, default: Any = None) -> Any:
        """Get a value by dot-separated path, e.g. 'gates.rr.reversal_min_rr'."""
        keys = dotpath.split(".")
        node = self._data
        for key in keys:
            if isinstance(node, dict) and key in node:
                node = node[key]
            else:
                return default
        return node

    def set(self, dotpath: str, value: Any, persist: bool = False) -> None:
        """Set a value and optionally persist. Records change in history."""
        old_value = self.get(dotpath)
        keys = dotpath.split(".")
        node = self._data
        for key in keys[:-1]:
            if key not in node or not isinstance(node[key], dict):
                node[key] = {}
            node = node[key]
        node[keys[-1]] = value

        self._change_history.append({
            "path": dotpath,
            "old": old_value,
            "new": value,
            "time": datetime.now(timezone.utc).isoformat(),
        })
        # Keep last 100 changes
        if len(self._change_history) > 100:
            self._change_history = self._change_history[-100:]

        if persist and self._path:
            self.save()

        for cb in self._on_change_callbacks:
            try:
                cb({"path": dotpath, "old": old_value, "new": value})
            except Exception:
                logger.exception("Config change callback failed")

    def section(self, prefix: str) -> dict[str, Any]:
        """Return a whole config section as a dict."""
        result = self.get(prefix)
        return result if isinstance(result, dict) else {}

    def as_dict(self) -> dict[str, Any]:
        return self._data.copy()

    def change_history(self) -> list[dict[str, Any]]:
        return list(self._change_history)

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def validate(self) -> list[str]:
        """Validate config against schema. Returns list of errors (empty = valid)."""
        errors: list[str] = []

        # Check required sections
        for section in _REQUIRED_SECTIONS:
            if section not in self._data:
                errors.append(f"Missing required section: {section}")

        # Check each schema field
        for dotpath, (expected_type, min_val, max_val, required) in _SCHEMA.items():
            value = self.get(dotpath)

            if value is None:
                if required:
                    errors.append(f"Missing required field: {dotpath}")
                continue

            # Type check (allow int for float fields)
            if expected_type is float and isinstance(value, int):
                value = float(value)
            if not isinstance(value, expected_type):
                errors.append(
                    f"{dotpath}: expected {expected_type.__name__}, got {type(value).__name__}"
                )
                continue

            # Range check
            if min_val is not None and value < min_val:
                errors.append(f"{dotpath}: {value} below minimum {min_val}")
            if max_val is not None and value > max_val:
                errors.append(f"{dotpath}: {value} above maximum {max_val}")

        return errors

    def validate_or_raise(self) -> None:
        """Validate and raise ConfigValidationError if invalid."""
        errors = self.validate()
        if errors:
            raise ConfigValidationError(
                f"Config validation failed:\n  " + "\n  ".join(errors)
            )

    # ------------------------------------------------------------------
    # Environment variable overrides
    # ------------------------------------------------------------------

    def apply_env_overrides(self, prefix: str = "SCROOGE") -> int:
        """Apply environment variable overrides. Returns count of overrides applied.

        Format: SCROOGE_SECTION_KEY=value (dots become underscores, uppercase)
        Example: SCROOGE_GATES_RR_REVERSAL_MIN_RR=1.5
        """
        count = 0
        env_prefix = f"{prefix}_"
        for key, value in os.environ.items():
            if not key.startswith(env_prefix):
                continue
            # Convert SCROOGE_RUNTIME_DRY_RUN -> runtime.dry_run
            # Strategy: try all possible 1-dot and 2-dot splits, pick the one that
            # matches an existing config path.
            raw = key[len(env_prefix):].lower()
            dotpath = self._resolve_env_path(raw)
            if dotpath is None:
                logger.debug("No config path found for env var %s", key)
                continue

            # Type coercion
            schema_entry = _SCHEMA.get(dotpath)
            if schema_entry:
                expected_type = schema_entry[0]
                try:
                    if expected_type is bool:
                        typed_value = value.lower() in ("true", "1", "yes")
                    elif expected_type is int:
                        typed_value = int(value)
                    elif expected_type is float:
                        typed_value = float(value)
                    else:
                        typed_value = value
                except (ValueError, TypeError):
                    logger.warning("Cannot coerce %s=%s to %s", key, value, expected_type)
                    continue
            else:
                typed_value = value

            logger.info("ENV override: %s = %s", dotpath, typed_value)
            self.set(dotpath, typed_value)
            count += 1

        return count

    # ------------------------------------------------------------------
    # File watcher for hot reload
    # ------------------------------------------------------------------

    def _resolve_env_path(self, raw: str) -> str | None:
        """Resolve an underscore-separated env suffix to a dotpath.

        Tries all possible splits of underscores into dots, preferring
        paths that exist in the current config. E.g. 'runtime_dry_run'
        tries 'runtime.dry_run' (match!) before 'runtime.dry.run'.
        """
        parts = raw.split("_")
        # Try 2-level: section.rest (most common)
        for i in range(1, len(parts)):
            section = "_".join(parts[:i])
            rest = "_".join(parts[i:])
            path = f"{section}.{rest}"
            if self.get(path) is not None:
                return path
        # Try 3-level: section.subsection.rest
        for i in range(1, len(parts)):
            for j in range(i + 1, len(parts)):
                section = "_".join(parts[:i])
                subsection = "_".join(parts[i:j])
                rest = "_".join(parts[j:])
                path = f"{section}.{subsection}.{rest}"
                if self.get(path) is not None:
                    return path
        # Fallback: check schema for the dotpath
        for dotpath in _SCHEMA:
            if dotpath.replace(".", "_") == raw:
                return dotpath
        return None

    def on_change(self, callback: Callable[[dict[str, Any]], None]) -> None:
        """Register a callback for config changes."""
        self._on_change_callbacks.append(callback)

    def start_watcher(self, interval: float = 5.0) -> None:
        """Start background thread watching config file for changes."""
        if self._watcher_thread and self._watcher_thread.is_alive():
            return
        if not self._path:
            logger.warning("No config path set — cannot start watcher")
            return

        self._watcher_stop.clear()
        self._watcher_thread = threading.Thread(
            target=self._watch_loop, args=(interval,),
            daemon=True, name="config-watcher",
        )
        self._watcher_thread.start()
        logger.info("Config watcher started (interval=%.1fs)", interval)

    def stop_watcher(self) -> None:
        """Stop the config file watcher."""
        self._watcher_stop.set()
        if self._watcher_thread:
            self._watcher_thread.join(timeout=10)
            self._watcher_thread = None

    def _watch_loop(self, interval: float) -> None:
        while not self._watcher_stop.is_set():
            try:
                if self._path and self._path.exists():
                    mtime = self._path.stat().st_mtime
                    if mtime > self._last_mtime:
                        logger.info("Config file changed — reloading")
                        old_data = self._data.copy()
                        self.load()
                        errors = self.validate()
                        if errors:
                            logger.error("Reloaded config is invalid: %s", errors)
                            self._data = old_data  # rollback
                        else:
                            # Notify callbacks of all changed fields
                            changes = self._diff(old_data, self._data)
                            for path, (old_v, new_v) in changes.items():
                                for cb in self._on_change_callbacks:
                                    try:
                                        cb({"path": path, "old": old_v, "new": new_v})
                                    except Exception:
                                        logger.exception("Change callback failed for %s", path)
                            logger.info("Config reloaded: %d changes", len(changes))
            except Exception:
                logger.exception("Config watcher error")
            self._watcher_stop.wait(interval)

    @staticmethod
    def _diff(
        old: dict[str, Any], new: dict[str, Any], prefix: str = ""
    ) -> dict[str, tuple[Any, Any]]:
        """Find all changed leaf values between two config dicts."""
        changes: dict[str, tuple[Any, Any]] = {}
        all_keys = set(old.keys()) | set(new.keys())
        for key in all_keys:
            path = f"{prefix}.{key}" if prefix else key
            old_v = old.get(key)
            new_v = new.get(key)
            if isinstance(old_v, dict) and isinstance(new_v, dict):
                changes.update(ConfigStore._diff(old_v, new_v, path))
            elif old_v != new_v:
                changes[path] = (old_v, new_v)
        return changes
