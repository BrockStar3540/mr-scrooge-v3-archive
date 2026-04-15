"""System widget — cycle count, uptime, equity, daily P&L, active sessions."""

from __future__ import annotations

import time
from datetime import datetime, timezone
from typing import Any


class SystemWidget:
    """Core system metrics — always present on dashboard."""

    widget_name = "system"
    widget_category = "core"

    def __init__(self, state: Any = None, broker: Any = None):
        self._state = state
        self._broker = broker
        self._boot_time = time.monotonic()

    def render_data(self) -> dict[str, Any]:
        uptime_s = time.monotonic() - self._boot_time

        data: dict[str, Any] = {
            "uptime_hours": round(uptime_s / 3600, 2),
            "cycle_count": 0,
            "position_count": 0,
            "daily_loss_exceeded": False,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        if self._state:
            data["cycle_count"] = self._state.cycle_count
            data["position_count"] = self._state.position_count
            data["daily_loss_exceeded"] = self._state.is_daily_loss_exceeded()

        if self._broker:
            acct = self._broker.get_account()
            if acct:
                data["equity"] = acct.equity
                data["balance"] = acct.balance
                data["margin_utilization"] = round(acct.margin_utilization * 100, 1)
                data["unrealized_pl"] = acct.unrealized_pl

            data["realized_pl_today"] = self._broker.get_realized_pl_today()

        return data
