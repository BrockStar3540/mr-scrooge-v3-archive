"""Dashboard bridge — publishes runtime state to the dashboard.

Extracted from Runtime._run_cycle() to keep trading logic
separate from UI/reporting concerns. Dashboard failures
cannot affect live trading decisions.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any

log = logging.getLogger("scrooge_v3.services.dashboard_bridge")


class DashboardBridge:
    """Pushes internal state to the dashboard LiveState."""

    def __init__(self, live_state: Any):
        self.live_state = live_state

    def publish_cycle(
        self,
        broker: Any,
        state: Any,
        tracker: Any,
        execution_audit: Any,
        dbb_audit: Any,
        reports: list[dict],
        now: datetime,
    ) -> None:
        """Push all cycle data to dashboard. Safe — catches all exceptions."""
        if not self.live_state:
            return

        try:
            self._publish_execution_audit(execution_audit)
            self._publish_dbb_audit(dbb_audit)
            self._publish_daily_pnl(broker)
            self._publish_account_and_scan(broker, state, tracker, reports, now)
        except Exception:
            log.exception("[DASHBOARD] Publish failed — trading unaffected")

    def _publish_execution_audit(self, audit: Any) -> None:
        if audit:
            self.live_state.update(
                execution_summary=audit.summary(),
                execution_events=audit.recent_events(50),
            )

    def _publish_dbb_audit(self, dbb: Any) -> None:
        if dbb:
            self.live_state.update(
                dbb_summary=dbb.summary(),
                dbb_candidates=dbb.recent(30),
            )

    def _publish_daily_pnl(self, broker: Any) -> None:
        daily_pl = broker.get_realized_pl_today()
        self.live_state.update(daily_pnl=daily_pl)

    def _publish_account_and_scan(
        self,
        broker: Any,
        state: Any,
        tracker: Any,
        reports: list[dict],
        now: datetime,
    ) -> None:
        from scrooge_v3.market.screener import get_active_sessions

        acct = broker.get_account()
        sessions = get_active_sessions(now.hour)
        viable = [r for r in reports if r.get("verdict", "").startswith("TAKE")]

        self.live_state.update(
            cycle_count=state.cycle_count,
            equity=acct.equity if acct else 0,
            balance=acct.balance if acct else 0,
            unrealized_pl=acct.unrealized_pl if acct else 0,
            daily_pnl=broker.get_realized_pl_today() if acct else 0,
            position_count=state.position_count,
            pairs_scanned=len(reports),
            pairs_viable=len(viable),
            signals_evaluated=len(reports),
            active_sessions=[s["name"] for s in sessions],
            scan_reports=reports,
            valid_count=len(viable),
            rejected_count=len(reports) - len(viable),
            daily_loss_exceeded=state.is_daily_loss_exceeded(),
        )

        # Pending orders count
        self.live_state.update(
            pending_limit_orders=len(tracker.all_pending_entries()) + len(tracker.get_positions_with_harvest_orders()),
        )
