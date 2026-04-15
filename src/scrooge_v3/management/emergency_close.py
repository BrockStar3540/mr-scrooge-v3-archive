"""Emergency close — hard circuit breaker for account-level risk events.

Triggers on: margin call risk, equity drawdown, broker disconnect,
or any condition that threatens account integrity.

This is the last line of defense — always deterministic, never optional.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass

log = logging.getLogger("scrooge_v3.management.emergency_close")


@dataclass
class EmergencyCloseAction:
    """Describes an emergency close action."""

    reason: str
    close_all: bool = True
    positions_to_close: list[str] | None = None  # None = all


class EmergencyCloseManager:
    """Account-level risk circuit breaker."""

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.max_drawdown_pct = config.get("emergency_max_drawdown_pct", 5.0)
        self.min_margin_pct = config.get("emergency_min_margin_pct", 50.0)

    def check(
        self,
        equity: float,
        equity_start: float,
        margin_used_pct: float,
        broker_connected: bool = True,
    ) -> EmergencyCloseAction | None:
        """Check if emergency close conditions are met.

        Returns EmergencyCloseAction if any circuit breaker triggers.
        """
        # Broker disconnect
        if not broker_connected:
            return EmergencyCloseAction(reason="broker_disconnected")

        # Equity drawdown
        if equity_start > 0:
            drawdown_pct = ((equity_start - equity) / equity_start) * 100
            if drawdown_pct >= self.max_drawdown_pct:
                return EmergencyCloseAction(
                    reason=f"equity_drawdown {drawdown_pct:.1f}% >= {self.max_drawdown_pct}%",
                )

        # Margin utilization too high
        if margin_used_pct >= self.min_margin_pct:
            return EmergencyCloseAction(
                reason=f"margin_critical {margin_used_pct:.1f}% >= {self.min_margin_pct}%",
            )

        return None
