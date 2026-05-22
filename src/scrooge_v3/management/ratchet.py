"""Ratchet manager — explicit stepwise scalper ratchet (Brock 2026-05-21).

Schedule:
  At MFE >= +6 pips:  SL -> entry - 6 pips  (cap loss at 6)
  At MFE >= +8 pips:  SL -> entry - 3 pips  (cap loss at 3)
  At MFE >= +10 pips: SL -> entry (BE)

Anchors on MFE (peak), not current price -- once a step triggers, the
stop ratchets and never loosens.

Old behavior (lock_pct of unrealized profit) is replaced. The lock_pct
config key is now read but logged-only; the explicit schedule wins.
"""

from __future__ import annotations

import logging
from typing import List, Tuple

from scrooge_v3.core.types import StopPlan, TradeDirection

log = logging.getLogger("scrooge_v3.management.ratchet")

# Default stepwise schedule (Brock 2026-05-21).
DEFAULT_STEPS: List[Tuple[float, float]] = [
    # (trigger_mfe_pips, new_sl_pips_from_entry  -- negative = below entry for long)
    (6.0,  -6.0),   # at +6 MFE, cap loss at -6 from entry
    (8.0,  -3.0),   # at +8 MFE, cap loss at -3 from entry
    (10.0,  0.0),   # at +10 MFE, breakeven
]


class RatchetManager:
    """Explicit stepwise scalper ratchet.

    Each step: (trigger_mfe_pips, new_sl_pips_from_entry).
    sl_pips_from_entry is the signed distance from entry (negative = on
    losing side for a long, positive = on losing side for a short via
    sign flip). Steps are evaluated in order; the highest triggered
    step's SL wins.
    """

    def __init__(self, config: dict | None = None):
        config = config or {}
        steps = config.get("scalper_steps", DEFAULT_STEPS)
        self.steps: List[Tuple[float, float]] = sorted(steps, key=lambda s: s[0])
        if "ratchet_lock_pct" in config or "ratchet_trigger_r" in config:
            log.info(
                "[RATCHET] legacy config keys (ratchet_lock_pct / ratchet_trigger_r) "
                "ignored under Brock 2026-05-21 stepwise scalper schedule"
            )

    def compute_ratchet_stop(
        self,
        direction: TradeDirection,
        entry_price: float,
        current_price: float,
        current_stop: float,
        pip_size: float = 0.0001,
        initial_risk_distance: float = 0.0,  # unused; kept for interface compat
        peak_price: float = 0.0,
    ) -> StopPlan | None:
        """Stepwise scalper ratchet. Anchors on MFE (peak_price).

        Returns a StopPlan if the ratchet would tighten the stop, else None.
        """
        # Compute MFE in pips (peak gain since entry)
        if peak_price and peak_price > 0:
            if direction == TradeDirection.LONG:
                mfe_pips = (peak_price - entry_price) / pip_size
            else:
                mfe_pips = (entry_price - peak_price) / pip_size
        else:
            if direction == TradeDirection.LONG:
                mfe_pips = (current_price - entry_price) / pip_size
            else:
                mfe_pips = (entry_price - current_price) / pip_size

        # Find highest step triggered
        triggered_sl_pips = None
        for trigger_mfe, sl_pips_from_entry in self.steps:
            if mfe_pips >= trigger_mfe:
                triggered_sl_pips = sl_pips_from_entry

        if triggered_sl_pips is None:
            return None  # haven't reached first trigger yet

        # Compute absolute new stop price
        # sl_pips_from_entry is signed in the convention "negative = on loss side for long"
        if direction == TradeDirection.LONG:
            # SL on loss side = below entry for long; so new_stop = entry + sl_pips (sl_pips negative)
            new_stop = entry_price + (triggered_sl_pips * pip_size)
            if new_stop <= current_stop:
                return None  # already tighter; don't loosen
        else:
            # For short, "loss side" = above entry; flip sign
            new_stop = entry_price - (triggered_sl_pips * pip_size)
            if new_stop >= current_stop:
                return None

        return StopPlan(
            position_id="",
            new_stop=new_stop,
            reason=(
                f"scalper_ratchet mfe={mfe_pips:.1f}pips "
                f"-> SL @ entry{triggered_sl_pips:+.1f}pips ({new_stop:.5f})"
            ),
        )
