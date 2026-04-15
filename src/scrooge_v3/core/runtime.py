"""Runtime — thin orchestrator replacing the V2 coordinator.

Wires together: ScanPipeline, PositionPipeline, StateController.
Runs the main 5-minute loop and the 3-second fast loop.

This file should stay under 200 lines. If it grows beyond that,
something that should be a module is being embedded here.
"""

from __future__ import annotations

import logging
import signal
import threading
import time
from datetime import datetime, timezone
from typing import Any

from .config import ConfigStore
from .events import EventBus
from .registry import ModuleRegistry
from .scan_pipeline import ScanPipeline
from .state_controller import StateController
from .strategy_router import StrategyRouter
from .types import MarketSnapshot

log = logging.getLogger("scrooge_v3.core.runtime")


class Runtime:
    """Main runtime — boots the system and runs the trading loop.

    Responsibilities:
      - Boot all engines and register modules
      - Run 5-minute scan cycle
      - Delegate position management to PositionPipeline
      - Handle shutdown gracefully
    """

    def __init__(self, config: ConfigStore):
        self.config = config
        self.event_bus = EventBus()
        self.registry = ModuleRegistry()
        self.state = StateController(
            config=config.section("risk") | config.section("runtime"),
        )
        self.router = StrategyRouter()
        self.scan_pipeline = ScanPipeline(
            registry=self.registry,
            router=self.router,
            event_bus=self.event_bus,
        )
        self._shutdown_requested = False
        self._scan_interval = config.get("runtime.scan_interval_seconds", 300)
        self._dry_run = config.get("runtime.dry_run", True)

    def boot(self) -> bool:
        """Initialize all engines and register modules.

        Returns True if boot succeeds, False if smoke test fails.
        """
        log.info("[RUNTIME] Booting V3...")

        # Register signal handlers
        signal.signal(signal.SIGTERM, self._handle_signal)
        signal.signal(signal.SIGINT, self._handle_signal)

        # TODO: Initialize broker adapter
        # TODO: Register feature modules
        # TODO: Register classifier modules
        # TODO: Register strategy modules
        # TODO: Register gate modules
        # TODO: Run smoke test (broker ping, dry scan cycle)

        log.info("[RUNTIME] Boot complete — dry_run=%s", self._dry_run)
        return True

    def run(self) -> None:
        """Main 5-minute trading loop."""
        if not self.boot():
            log.error("[RUNTIME] Boot failed — not starting")
            return

        log.info("[RUNTIME] Starting main loop (interval=%ds)", self._scan_interval)

        while not self._shutdown_requested:
            cycle_start = time.monotonic()
            self.state.cycle_count += 1

            try:
                self._run_cycle()
            except Exception:
                log.exception("[RUNTIME] Cycle %d failed", self.state.cycle_count)

            # Persist state after each cycle
            self.state.persist()

            # Sleep for remainder of interval
            elapsed = time.monotonic() - cycle_start
            sleep_time = max(0, self._scan_interval - elapsed)
            if sleep_time > 0 and not self._shutdown_requested:
                self._interruptible_sleep(sleep_time)

        log.info("[RUNTIME] Shutdown complete after %d cycles", self.state.cycle_count)

    def _run_cycle(self) -> None:
        """Execute one scan cycle."""
        now = datetime.now(timezone.utc)

        # Check for daily reset
        if self.state.session_start.date() != now.date():
            self.state.daily_reset()
            self.state.session_start = now

        # Check daily loss limit
        if self.state.is_daily_loss_exceeded():
            log.warning("[RUNTIME] Daily loss limit reached — skipping cycle")
            return

        # TODO: Get active pairs from screener
        # TODO: Fetch market snapshots from broker
        # TODO: Run scan_pipeline.scan_universe()
        # TODO: Fire best candidate if not at max positions
        # TODO: Run position_pipeline.manage_all()

        log.debug(
            "[RUNTIME] Cycle %d complete — positions=%d",
            self.state.cycle_count,
            self.state.position_count,
        )

    def shutdown(self) -> None:
        """Graceful shutdown."""
        log.info("[RUNTIME] Shutdown requested")
        self._shutdown_requested = True
        # TODO: Close all positions if configured
        # TODO: Persist final state

    def _handle_signal(self, signum: int, frame: Any) -> None:
        log.info("[RUNTIME] Received signal %d", signum)
        self.shutdown()

    def _interruptible_sleep(self, seconds: float) -> None:
        """Sleep that can be interrupted by shutdown."""
        end = time.monotonic() + seconds
        while time.monotonic() < end and not self._shutdown_requested:
            time.sleep(min(1.0, end - time.monotonic()))
