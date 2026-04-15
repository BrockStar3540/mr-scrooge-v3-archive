"""Health widget — status lights from module registry and health monitor."""

from __future__ import annotations

from typing import Any


class HealthWidget:
    """Shows module health status: green/yellow/red/gray per module."""

    widget_name = "health"
    widget_category = "core"

    def __init__(self, registry: Any = None):
        self._registry = registry

    def render_data(self) -> dict[str, Any]:
        if self._registry is None:
            return {"modules": [], "summary": "no registry"}

        summary = self._registry.health_summary()
        modules = []
        for entry in self._registry.list_all():
            modules.append({
                "name": entry.name,
                "category": entry.category,
                "mode": entry.mode.value if hasattr(entry.mode, "value") else str(entry.mode),
                "health": summary.get(entry.name, {}).get("color", "gray"),
            })
        return {"modules": modules, "total": len(modules)}
