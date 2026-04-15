"""Module registry — modules are discovered, not hard-wired."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any

from .types import HealthColor, HealthStatus, ModuleMode

logger = logging.getLogger(__name__)


@dataclass
class ModuleEntry:
    """Registry entry for any pluggable module."""

    name: str
    version: str = "0.1.0"
    enabled: bool = True
    mode: str = "active"
    dependencies: list[str] = field(default_factory=list)
    config_namespace: str = ""
    instance: Any = None
    health: HealthStatus | None = None


class ModuleRegistry:
    """Central registry for all module types."""

    def __init__(self) -> None:
        self._registries: dict[str, dict[str, ModuleEntry]] = {}

    def register(
        self,
        registry_name: str,
        name: str,
        instance: Any,
        *,
        version: str = "0.1.0",
        enabled: bool = True,
        mode: str = "active",
        dependencies: list[str] | None = None,
        config_namespace: str = "",
    ) -> None:
        if registry_name not in self._registries:
            self._registries[registry_name] = {}

        entry = ModuleEntry(
            name=name,
            version=version,
            enabled=enabled,
            mode=mode,
            dependencies=dependencies or [],
            config_namespace=config_namespace or f"{registry_name}.{name}",
            instance=instance,
        )
        self._registries[registry_name][name] = entry
        logger.info("Registered %s/%s (mode=%s)", registry_name, name, mode)

    def get(self, registry_name: str, name: str) -> ModuleEntry | None:
        return self._registries.get(registry_name, {}).get(name)

    def get_active(self, registry_name: str) -> list[ModuleEntry]:
        """Return all enabled modules in a registry."""
        return [
            e
            for e in self._registries.get(registry_name, {}).values()
            if e.enabled
        ]

    def list_all(self, registry_name: str) -> list[ModuleEntry]:
        return list(self._registries.get(registry_name, {}).values())

    def registry_names(self) -> list[str]:
        return list(self._registries.keys())

    def set_mode(self, registry_name: str, name: str, mode: str) -> bool:
        entry = self.get(registry_name, name)
        if entry is None:
            return False
        entry.mode = mode
        entry.enabled = mode != ModuleMode.DISABLED
        return True

    def health_summary(self) -> dict[str, list[HealthStatus]]:
        """Return health for all modules, grouped by registry."""
        result: dict[str, list[HealthStatus]] = {}
        for reg_name, entries in self._registries.items():
            statuses = []
            for entry in entries.values():
                if entry.health:
                    statuses.append(entry.health)
                else:
                    color = HealthColor.GRAY if not entry.enabled else HealthColor.GREEN
                    statuses.append(HealthStatus(name=entry.name, color=color))
            result[reg_name] = statuses
        return result
