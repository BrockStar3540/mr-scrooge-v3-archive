"""RuntimeContext — typed dependency container for all live system components.

Created by bootstrap.build_runtime(), consumed by Runtime.
Keeps runtime.py thin by holding all wired dependencies in one place.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .config import ConfigStore
from .events import EventBus
from .registry import ModuleRegistry
from .scan_pipeline import ScanPipeline
from .state_controller import StateController
from .strategy_router import StrategyRouter


@dataclass
class RuntimeContext:
    """All wired dependencies for the live trading loop."""

    config: ConfigStore
    broker: Any
    event_bus: EventBus
    registry: ModuleRegistry
    state: StateController
    router: StrategyRouter
    scan_pipeline: ScanPipeline
    position_pipeline: Any
    tracker: Any
    spread_monitor: Any
    execution_audit: Any
    dbb_audit: Any
    live_state: Any
    screener: Any

    # Internal state
    known_trade_ids: set[str] = field(default_factory=set)
    pending_entry_meta: dict[str, dict] = field(default_factory=dict)
    scan_interval: int = 60
    dry_run: bool = True
