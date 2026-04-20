"""Runtime — thin orchestrator for the V3 trading platform.

Wires together: bootstrap, scan pipeline, execution, position management.
The runtime is the conductor — it calls into specialized modules
rather than implementing their logic directly.

Phase 1 extraction (2026-04-16):
  - boot logic → bootstrap.py
  - typed dependencies → runtime_context.py
  - dashboard updates → services/dashboard_bridge.py
"""

from __future__ import annotations

import logging
import signal
import time
from datetime import datetime, timedelta, timezone
from typing import Any

from .config import ConfigStore
from .bootstrap import build_runtime, BootFailure
from .runtime_context import RuntimeContext
from .types import MarketSnapshot, TradeDirection

log = logging.getLogger("scrooge_v3.core.runtime")


class Runtime:
    """Main runtime — boots the system and runs the trading loop.

    Responsibilities:
      - Boot via bootstrap.build_runtime()
      - Run scan cycle
      - Delegate execution and position management
      - Publish state via DashboardBridge
      - Handle shutdown gracefully
    """

    def __init__(self, config: ConfigStore, live_state: Any = None):
        self.config = config
        self.live_state = live_state
        self.ctx: RuntimeContext | None = None
        self._shutdown_requested = False
        self.dashboard: Any = None

    @property
    def event_bus(self):
        """Access event_bus — delegates to ctx after boot, temporary before."""
        if self.ctx:
            return self.ctx.event_bus
        if not hasattr(self, '_pre_boot_event_bus'):
            from .events import EventBus
            self._pre_boot_event_bus = EventBus()
        return self._pre_boot_event_bus

    def boot(self) -> bool:
        """Initialize all engines via bootstrap."""
        log.info("[RUNTIME] Booting V3...")

        signal.signal(signal.SIGTERM, self._handle_signal)
        signal.signal(signal.SIGINT, self._handle_signal)

        try:
            self.ctx = build_runtime(self.config, self.live_state)
        except BootFailure as e:
            log.error("[RUNTIME] Boot failed: %s", e)
            return False
        except Exception:
            log.exception("[RUNTIME] Boot failed with unexpected error")
            return False

        # Wire config hot reload
        self.config.on_change(self._handle_config_change)

        # Create dashboard bridge
        if self.live_state:
            from scrooge_v3.services.dashboard_bridge import DashboardBridge
            self.dashboard = DashboardBridge(self.live_state)

        # Transfer pre-boot event subscribers (e.g. EventRecorder from __main__)
        if hasattr(self, '_pre_boot_event_bus'):
            for h in self._pre_boot_event_bus._global_handlers:
                self.ctx.event_bus.subscribe_all(h)

        # Create services
        from scrooge_v3.services.config_watcher import ConfigWatcher
        from scrooge_v3.services.state_recovery import StateRecovery
        from scrooge_v3.core.scan_coordinator import ScanCoordinator
        from scrooge_v3.core.execution_coordinator import ExecutionCoordinator
        from scrooge_v3.core.position_coordinator import PositionCoordinator
        self.config_watcher = ConfigWatcher(self.ctx)
        self.recovery = StateRecovery(self.ctx)
        self.scanner = ScanCoordinator(self.ctx)
        self.executor = ExecutionCoordinator(self.ctx, self.recovery)
        self.positions = PositionCoordinator(self.ctx, self.recovery, self.config)

        log.info("[RUNTIME] Boot complete")
        return True

    @staticmethod
    def is_weekend() -> bool:
        """True during OANDA weekend close (Sat 00:00 - Sun 22:00 UTC)."""
        now = datetime.now(timezone.utc)
        wd = now.weekday()
        if wd == 5:
            return True
        if wd == 6 and now.hour < 22:
            return True
        return False

    def run(self) -> None:
        """Main trading loop."""
        if not self.boot():
            log.error("[RUNTIME] Boot failed — not starting")
            return

        ctx = self.ctx
        log.info("[RUNTIME] Starting main loop (interval=%ds)", ctx.scan_interval)

        while not self._shutdown_requested:
            cycle_start = time.monotonic()
            ctx.state.cycle_count += 1

            try:
                self._run_cycle()
            except Exception:
                log.exception("[RUNTIME] Cycle %d failed", ctx.state.cycle_count)

            ctx.state.persist()

            elapsed = time.monotonic() - cycle_start
            sleep_time = max(0, ctx.scan_interval - elapsed)
            if sleep_time > 0 and not self._shutdown_requested:
                self._interruptible_sleep(sleep_time)

        log.info("[RUNTIME] Shutdown complete after %d cycles", ctx.state.cycle_count)

    def _run_cycle(self) -> None:
        """Execute one scan cycle."""
        ctx = self.ctx
        now = datetime.now(timezone.utc)

        # Weekend detection
        if self.is_weekend():
            log.debug("[RUNTIME] Weekend — market closed, skipping cycle")
            return

        # Daily reset at date boundary
        if ctx.state.session_start.date() != now.date():
            ctx.state.daily_reset()
            ctx.state.session_start = now
            acct = ctx.broker.get_account()
            if acct:
                ctx.state.equity_start = acct.equity
                log.info("[RUNTIME] New day — equity baseline: $%.2f", acct.equity)

        # Daily loss limit
        if ctx.state.is_daily_loss_exceeded():
            log.warning("[RUNTIME] Daily loss limit reached — skipping cycle")
            return

        # --- Reconcile broker state FIRST (Bug E: state-truth before decisions) ---
        # Order matters: vanished detection -> tracker reconcile -> pending order
        # reconcile. This must all complete before the scanner reads tracker
        # state (held_symbols / pending_symbols / correlation filter) or the
        # management pipeline makes decisions on stale data.
        self.recovery.detect_vanished_trades()
        self.recovery.reconcile_tracker()
        self.recovery.reconcile_pending_orders()

        # --- Scan cycle ---
        scan = self.scanner.scan_cycle(now)
        reports = scan.reports
        candidates = scan.candidates

        if scan.spread_skip and self.live_state:
            self.live_state.update(
                spread_skips=self.live_state.spread_skips + 1,
                last_spread_skip=f"{scan.spread_skip_symbol} ({scan.spread_skip_ratio:.1f}x)",
            )

        # --- Entry logic ---
        if scan.best_candidate:
            self.executor.try_execute(scan.best_candidate)

        # --- Manage open positions ---
        self.positions.manage_all()

        # --- Publish to dashboard ---
        if self.dashboard:
            self.dashboard.publish_cycle(
                broker=ctx.broker,
                state=ctx.state,
                tracker=ctx.tracker,
                execution_audit=ctx.execution_audit,
                dbb_audit=ctx.dbb_audit,
                reports=reports,
                now=now,
            )

        log.debug("[RUNTIME] Cycle %d complete — positions=%d, candidates=%d",
                  ctx.state.cycle_count, ctx.state.position_count, len(candidates))

    # ------------------------------------------------------------------
    # Entry execution
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def shutdown(self) -> None:
        """Graceful shutdown."""
        log.info("[RUNTIME] Shutdown requested")
        self._shutdown_requested = True
        self.config.stop_watcher()
        if self.ctx:
            self.ctx.state.persist()

    def _handle_signal(self, signum: int, frame: Any) -> None:
        log.info("[RUNTIME] Received signal %d", signum)
        self.shutdown()

    def _handle_config_change(self, change: dict) -> None:
        """Delegate config changes to ConfigWatcher service."""
        if hasattr(self, 'config_watcher'):
            self.config_watcher.handle_change(change)

    def _interruptible_sleep(self, seconds: float) -> None:
        """Sleep that can be interrupted by shutdown."""
        end = time.monotonic() + seconds
        while time.monotonic() < end and not self._shutdown_requested:
            time.sleep(min(1.0, end - time.monotonic()))
