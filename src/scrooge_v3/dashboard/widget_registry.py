"""Dashboard widget registry — auto-discovery of module-registered panels.

Each module can register a DashboardWidget that provides data for its
section of the dashboard. Widgets are grouped by category and rendered
in the order they're registered.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any, Protocol

log = logging.getLogger("scrooge_v3.dashboard.widget_registry")


class DashboardWidget(Protocol):
    """Protocol for dashboard widgets. Any module can implement this."""

    @property
    def widget_name(self) -> str: ...

    @property
    def widget_category(self) -> str: ...

    def render_data(self) -> dict[str, Any]: ...


@dataclass
class WidgetEntry:
    name: str
    category: str
    instance: Any  # implements DashboardWidget


class WidgetRegistry:
    """Collects and serves dashboard widgets by category."""

    def __init__(self) -> None:
        self._widgets: list[WidgetEntry] = []

    def register(self, widget: Any) -> None:
        entry = WidgetEntry(
            name=widget.widget_name,
            category=widget.widget_category,
            instance=widget,
        )
        self._widgets.append(entry)
        log.debug("[WIDGETS] Registered: %s (%s)", entry.name, entry.category)

    def get_all(self) -> list[WidgetEntry]:
        return list(self._widgets)

    def get_by_category(self, category: str) -> list[WidgetEntry]:
        return [w for w in self._widgets if w.category == category]

    def categories(self) -> list[str]:
        seen: dict[str, None] = {}
        for w in self._widgets:
            seen[w.category] = None
        return list(seen.keys())

    def render_all(self) -> dict[str, list[dict[str, Any]]]:
        """Render all widgets grouped by category."""
        result: dict[str, list[dict[str, Any]]] = {}
        for entry in self._widgets:
            cat = entry.category
            if cat not in result:
                result[cat] = []
            try:
                data = entry.instance.render_data()
                result[cat].append({"name": entry.name, "data": data})
            except Exception as e:
                log.error("[WIDGETS] %s.render_data() failed: %s", entry.name, e)
                result[cat].append({"name": entry.name, "data": {"error": str(e)}})
        return result
