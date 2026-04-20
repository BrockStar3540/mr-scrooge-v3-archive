"""Ratchet manager — locks percentage of peak unrealized gains.

Engineering extension from Part II Section 32.
Phase 3 (fix/mgmt-r-unified) changes:
  - Trigger is R-relative with a pip floor (same pattern as BE).
  - Lock anchors on peak_price (MFE), not current_price, so retracement
    from a spike-high can't unlock already-protected gains.
"""

from __future__ import annotations

import logging

from scrooge_v3.core.types import StopPlan, TradeDirection

log = logging.getLogger("scrooge_v3.management.ratchet")


class RatchetManager:
    """Locks a percentage of unrealized gains at periodic intervals."""

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.lock_pct = float(config.get("ratchet_lock_pct", 0.50))

        # Legacy fixed-pip key (deprecated).
        legacy = config.get("ratchet_min_profit_pips")
        if legacy is not None:
            log.warning(
                "[RATCHET] DEPRECATED config key ratchet_min_profit_pips detected "
                "— migrate to ratchet_trigger_r / ratchet_trigger_min_pips."
            )

        self.trigger_r = float(config.get("ratchet_trigger_r", 1.0))
        self.trigger_min_pips = float(
            config.get("ratchet_trigger_min_pips", legacy if legacy is not None else 3.0)
        )

    def compute_ratchet_stop(
        self,
        direction: TradeDirection,
        entry_price: float,
        current_price: float,
        current_stop: float,
        pip_size: float = 0.0001,
        initial_risk_distance: float = 0.0,
        peak_price: float = 0.0,
    ) -> StopPlan | None:
        """Compute ratcheted stop that locks a fraction of unrealized profit.

        Only activates when profit exceeds the R-relative trigger (with
        pip floor). Never loosens the stop — only tightens.

        If `peak_price` is provided and more favorable than `current_price`,
        the lock anchors on peak (MFE), protecting gains against retracement.
        """
        if direction == TradeDirection.LONG:
            profit_dist = current_price - entry_price
        else:
            profit_dist = entry_price - current_price

        if initial_risk_distance > 0:
            trigger_dist = max(
                self.trigger_r * initial_risk_distance,
                self.trigger_min_pips * pip_size,
            )
        else:
            trigger_dist = self.trigger_min_pips * pip_size

        if profit_dist < trigger_dist:
            return None

        # Anchor on peak (MFE) if provided and more favorable.
        if peak_price and peak_price > 0:
            if direction == TradeDirection.LONG:
                anchor = max(peak_price, current_price)
            else:
                anchor = min(peak_price, current_price)
        else:
            anchor = current_price

        locked_distance = abs(anchor - entry_price) * self.lock_pct

        if direction == TradeDirection.LONG:
            new_stop = entry_price + locked_distance
            if new_stop <= current_stop:
                return None
        else:
            new_stop = entry_price - locked_distance
            if new_stop >= current_stop:
                return None

        profit_pips = profit_dist / pip_size if pip_size > 0 else 0.0
        return StopPlan(
            position_id="",
            new_stop=new_stop,
            reason=f"ratchet lock {self.lock_pct:.0%} of {profit_pips:.1f} pips (anchor={anchor:.5f})",
        )
