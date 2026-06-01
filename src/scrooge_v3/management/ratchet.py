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

# Cheese-slicer schedule (Brock 2026-05-27, replaces 2026-05-21 schedule).
# With 7p entry SL the old -6/-3/0 steps were unreachable or weakly useful.
# This single positive step locks 5 pips of profit once MFE hits 5.5p,
# so we slice cheese off the table at every meaningful favorable move.
DEFAULT_STEPS: List[Tuple[float, float]] = [
    # (trigger_mfe_pips, new_sl_pips_from_entry  -- POSITIVE = above entry = profit lock for long)
    (5.5,  5.0),   # at +5.5 MFE, lock SL at entry+5 (5p profit guaranteed)
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
        stamped_sl: float = 0.0,  # Brock 2026-06-01 Fix A: persistent step-stamp
        spread: float = 0.0,  # Brock 2026-06-01: NET-green adjustment (price units)
    ) -> StopPlan | None:
        """Stepwise scalper ratchet. Anchors on MFE (peak_price).

        Returns a StopPlan if the ratchet would tighten the stop, else None.
        """
        # Compute MFE in pips (peak gain since entry).
        # NET-GREEN (Brock 2026-06-01): entry_price is the FILL (ask for long /
        # bid for short, since entries are now market orders) while peak/current
        # come from the MID. The TRUE net unrealized you'd realize on close is
        # measured at the close side (bid for long, ask for short), which sits a
        # half-spread away from the mid. Subtract spread/2 so a step trigger of
        # "5.5p" means the position is genuinely +5.5p net (spread fully paid) —
        # only THEN do we lock. The lock target (entry+sl_pips) already realizes
        # net sl_pips because a long stop fills at the bid / a short at the ask.
        half_spread_pips = (spread / pip_size) / 2.0 if (spread and pip_size) else 0.0
        if half_spread_pips > 15.0:  # implausible -> spread passed in wrong units; fail safe
            half_spread_pips = 0.0
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
        mfe_pips -= half_spread_pips  # mid-peak -> net (close-side) green

        # Find highest step triggered THIS cycle (based on current MFE)
        triggered_sl_pips = None
        for trigger_mfe, sl_pips_from_entry in self.steps:
            if mfe_pips >= trigger_mfe:
                triggered_sl_pips = sl_pips_from_entry

        # Brock 2026-06-01 Fix A: STAMP semantics.
        # 1) If a step is triggered this cycle, compute its target SL.
        # 2) If a prior stamp exists, only UPDATE the stamp if the new step
        #    is TIGHTER (closer to/past entry) than the previous stamp.
        # 3) If NO step is triggered this cycle but a prior stamp exists,
        #    enforce the prior stamp — don't unstamp.
        # 4) Reason includes whether this was a fresh stamp, an upgrade,
        #    or persistent enforcement of an older stamp.

        target_sl = 0.0
        reason_tag = ""

        if triggered_sl_pips is not None:
            # A step triggered this cycle — compute its target SL
            if direction == TradeDirection.LONG:
                step_target = entry_price + (triggered_sl_pips * pip_size)
            else:
                step_target = entry_price - (triggered_sl_pips * pip_size)

            # Is this tighter than any prior stamp?
            if stamped_sl > 0:
                tighter = (
                    (direction == TradeDirection.LONG and step_target > stamped_sl) or
                    (direction == TradeDirection.SHORT and step_target < stamped_sl)
                )
                if tighter:
                    target_sl = step_target
                    reason_tag = f"stamp_upgrade mfe={mfe_pips:.1f}p step={triggered_sl_pips:+.1f}p"
                else:
                    target_sl = stamped_sl
                    reason_tag = f"stamp_persist mfe={mfe_pips:.1f}p stamp@{stamped_sl:.5f}"
            else:
                target_sl = step_target
                reason_tag = f"stamp_new mfe={mfe_pips:.1f}p step={triggered_sl_pips:+.1f}p"
        elif stamped_sl > 0:
            # No new step but stamp exists — enforce
            target_sl = stamped_sl
            reason_tag = f"stamp_persist mfe={mfe_pips:.1f}p stamp@{stamped_sl:.5f}"
        else:
            # No step triggered, no prior stamp
            return None

        # Tightening check vs current SL
        if direction == TradeDirection.LONG:
            if target_sl <= current_stop:
                return None
        else:
            if target_sl >= current_stop:
                return None

        return StopPlan(
            position_id="",
            new_stop=target_sl,
            reason=f"scalper_ratchet {reason_tag} -> SL @ {target_sl:.5f}",
        )
