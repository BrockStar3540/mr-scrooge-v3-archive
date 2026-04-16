"""Config watcher — handles hot-reload changes to live config.

Extracted from Runtime._handle_config_change() to keep config mutation
logic separate from the trading loop.
"""

from __future__ import annotations

import logging
from typing import Any

log = logging.getLogger("scrooge_v3.services.config_watcher")


class ConfigWatcher:
    """Processes validated config changes and applies them to live modules."""

    def __init__(self, ctx: Any):
        self.ctx = ctx

    def handle_change(self, change: dict) -> None:
        """Handle a config hot-reload change.

        Applies safe live-updatable changes:
          - Module mode switching (features, classifiers, strategies, gates)
          - Scan interval updates
        Emits CONFIG_CHANGED event for other listeners.
        """
        from scrooge_v3.core.events import CONFIG_CHANGED, Event

        path = change.get("path", "")
        new_val = change.get("new")
        ctx = self.ctx

        if ctx is None:
            return

        # Module mode switching: e.g. features.atr.mode = "disabled"
        parts = path.split(".")
        if len(parts) >= 3 and parts[2] == "mode":
            category = parts[0]
            module_name = parts[1]
            new_mode = str(new_val)
            log.info("[CONFIG] Mode change: %s.%s → %s", category, module_name, new_mode)
            ctx.registry.set_mode(category, module_name, new_mode)

        # Scan interval change
        if path == "runtime.scan_interval_seconds" and isinstance(new_val, (int, float)):
            ctx.scan_interval = int(new_val)
            log.info("[CONFIG] Scan interval changed to %ds", ctx.scan_interval)

        # Emit event for other listeners
        ctx.event_bus.emit(Event(type=CONFIG_CHANGED, payload=change))
