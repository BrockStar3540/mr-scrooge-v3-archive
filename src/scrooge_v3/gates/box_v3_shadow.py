"""Box mean-reversion v3 shadow gate (observe-only).

Implements the frozen v3 gate tree from the trainer repo:
  docs/box_gate_tree.md + data/regimes/box_gate_v3.yaml @ 19ada0e

Runs in OBSERVE mode. Never rejects a trade. Emits, per candidate:
  - would_allow (bool): would v3 have accepted this?
  - failed_gate: first hard gate that would have rejected (or None)
  - tier: A | B | C (based on ranking score)
  - ranking_score: 0-7
  - per-gate pass flags
  - input values used

These flow into `report["gates"]` and are auto-captured by ml-observer.
After a week of shadow logging, compare would_allow outcomes against
actual V3 trade outcomes to decide if v3 should graduate to a live gate.

Notes:
- Layer D6 (regime_type exclusion) can't be evaluated live — the live
  classifier is binary NORMAL/CAUTION, while v3 uses the annotation
  taxonomy. D6 is logged as "not_evaluated".
- Strategy family restriction to box branch (direct/reversal) is applied
  first — the gate is a no-op for trend candidates.
"""
from __future__ import annotations

from typing import Any

from scrooge_v3.core.types import (
    GateMode,
    GateResult,
    SymbolContext,
    TradeCandidate,
)

from .base import BaseGate


# Tuning constants (from frozen v3 spec)
WALL_MIN = 0.30
EMA20_DEAD_LO = 18.0
EMA20_DEAD_HI = 40.0
VOLUME_RATIO_MAX = 1.50
STOP_MIN_PIPS = 15.0
STOP_BOOST_PIPS = 25.0
BOX_AGE_MAX_HOURS = 6.0
BB_TAIL_UPPER = 0.80
BB_TAIL_LOWER = 0.20
ADR_A_TIER_MIN = 1.25
WALL_SWEET_LO = 0.30
WALL_SWEET_HI = 0.50
VOL_SWEET_LO = 0.60
VOL_SWEET_HI = 0.90

# Layer E ranking point weights
POINTS_ADR = 3
POINTS_WALL_SWEET = 2
POINTS_VOL_SWEET = 1
POINTS_STOP_WIDE = 1
POINTS_SHORT_GAP_DOWN = 1
A_TIER_THRESHOLD = 5
B_TIER_THRESHOLD = 2


def _pip_size(symbol: str) -> float:
    return 0.01 if symbol.split("_")[-1] == "JPY" else 0.0001


class BoxV3ShadowGate(BaseGate):
    """Observe-only shadow of the frozen box v3 gate tree."""

    name = "box_v3_shadow"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.OBSERVE,
    ) -> None:
        super().__init__(config, mode)

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        # Restrict to box branch (direct / reversal). No-op for trend.
        strat = (candidate.strategy or "").lower()
        if strat not in ("direct", "reversal"):
            return GateResult(
                gate_name=self.name, passed=True,
                reason=f"not_box_branch(strategy={strat})",
                metrics={"applicable": False, "score": 1.0},
            )

        # Pull feature values defensively. Missing inputs → log as "skipped".
        zone = (ctx.features.get("zone_detector").values
                if ctx.features.get("zone_detector") else {}) or {}
        ema = (ctx.features.get("ema").values
               if ctx.features.get("ema") else {}) or {}
        vol = (ctx.features.get("volume").values
               if ctx.features.get("volume") else {}) or {}
        bb = (ctx.features.get("bollinger").values
              if ctx.features.get("bollinger") else {}) or {}
        atr_f = (ctx.features.get("atr").values
                 if ctx.features.get("atr") else {}) or {}

        opening_label = None
        if ctx.classifications.get("opening_state"):
            opening_label = ctx.classifications["opening_state"].label

        # Inputs
        wall_proximity = zone.get("wall_proximity")
        box_age = zone.get("box_age_hours")
        ema20_dist = ema.get("ema20_dist_pct")
        ema50_dist = ema.get("ema50_dist_pct")
        volume_ratio = vol.get("volume_ratio")
        bb_position = bb.get("bb_position")
        adr_consumed = atr_f.get("adr_consumed")

        # Natural stop in pips
        pip = _pip_size(candidate.symbol)
        natural_stop_pips = None
        try:
            natural_stop_pips = abs(float(candidate.entry_price)
                                     - float(candidate.stop_price)) / pip
        except Exception:
            natural_stop_pips = None

        # --- Layer A (envelope / hard) ---
        gate_results: dict[str, Any] = {}
        failed = None

        def check(name: str, ok: bool | None, skip_reason: str = "missing_input"):
            nonlocal failed
            if ok is None:
                gate_results[name] = "skipped"
            elif ok:
                gate_results[name] = "pass"
            else:
                gate_results[name] = "fail"
                if failed is None:
                    failed = name

        # LOOSE envelope checks (v2/v3 preserve these)
        check("loose_wall",
              (wall_proximity is not None) and (wall_proximity >= 0.20))
        check("loose_box_age",
              (box_age is not None) and (box_age <= BOX_AGE_MAX_HOURS))
        check("loose_bb_tail",
              (bb_position is not None) and
              ((bb_position <= BB_TAIL_LOWER) or (bb_position >= BB_TAIL_UPPER)))

        # Hard gates
        check("A1_wall_strict",
              (wall_proximity is not None) and (wall_proximity >= WALL_MIN))
        check("A2_ema20_not_dead",
              (ema20_dist is not None) and
              (ema20_dist < EMA20_DEAD_LO or ema20_dist >= EMA20_DEAD_HI))
        check("A3_not_expansion",
              (volume_ratio is not None) and (volume_ratio < VOLUME_RATIO_MAX))
        check("C1_min_stop",
              (natural_stop_pips is not None) and
              (natural_stop_pips >= STOP_MIN_PIPS))

        would_allow = (failed is None) and all(
            v == "pass" for v in gate_results.values())

        # --- Layer E ranking (computed regardless of gate pass) ---
        score = 0
        reasons = []
        if (adr_consumed is not None) and (adr_consumed >= ADR_A_TIER_MIN):
            score += POINTS_ADR; reasons.append("adr>=1.25(+3)")
        if (wall_proximity is not None) and (WALL_SWEET_LO <= wall_proximity <= WALL_SWEET_HI):
            score += POINTS_WALL_SWEET; reasons.append("wall0.30-0.50(+2)")
        if (volume_ratio is not None) and (VOL_SWEET_LO <= volume_ratio < VOL_SWEET_HI):
            score += POINTS_VOL_SWEET; reasons.append("vol0.60-0.90(+1)")
        if (natural_stop_pips is not None) and (natural_stop_pips >= STOP_BOOST_PIPS):
            score += POINTS_STOP_WIDE; reasons.append("stop>=25(+1)")
        # Short + GAP_DOWN opening
        direction = (candidate.direction.value
                     if hasattr(candidate.direction, "value")
                     else str(candidate.direction))
        if direction == "short" and opening_label == "GAP_DOWN":
            score += POINTS_SHORT_GAP_DOWN; reasons.append("short+GAP_DOWN(+1)")

        if score >= A_TIER_THRESHOLD:
            tier = "A"
        elif score >= B_TIER_THRESHOLD:
            tier = "B"
        else:
            tier = "C"

        return GateResult(
            gate_name=self.name,
            passed=True,  # observe-only: always passes
            reason=(f"would_{'allow' if would_allow else 'reject'}"
                    + (f" (failed={failed})" if failed else "")
                    + f" tier={tier} score={score}"),
            metrics={
                "would_allow": would_allow,
                "failed_gate": failed,
                "ranking_score": score,
                "tier": tier,
                "ranking_reasons": ";".join(reasons) if reasons else "",
                "gate_results": gate_results,
                "inputs": {
                    "wall_proximity": wall_proximity,
                    "box_age_hours": box_age,
                    "ema20_dist_pct": ema20_dist,
                    "ema50_dist_pct": ema50_dist,
                    "volume_ratio": volume_ratio,
                    "bb_position": bb_position,
                    "adr_consumed": adr_consumed,
                    "natural_stop_pips": (round(natural_stop_pips, 2)
                                          if natural_stop_pips is not None else None),
                    "direction": direction,
                    "opening_state": opening_label,
                    "strategy": strat,
                },
                "applicable": True,
                "score": 1.0,
            },
        )
