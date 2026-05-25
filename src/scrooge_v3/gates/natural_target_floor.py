"""Market-state projection floor — block any candidate when live market
conditions don't support the minimum scalp.

Brock 2026-05-25: this is a UNIVERSAL filter, recomputed per scan cycle
from live M5 bar data. It does NOT read strategy-specific metadata. The
question it answers: "given what the market is doing right now, can this
symbol realistically produce a `min_pips` move within a scalper holding
window?" If no, no strategy fires on this symbol this cycle. If the
calculation changes 5 min later (volatility expands, BB widens), the
same symbol can pass.

Projection composite:
  proj_atr = atr_m5_pips * horizon_bars   (expected cumulative motion)
  proj_bb  = bb_width_pips / 2            (room from BB midline to band)
  projection_pips = MIN(proj_atr, proj_bb)  -- conservative; both
                                              dimensions must support the move

Live tick freshness:
  - atr_m5 computed from snapshot.candles["M5"] true range over last
    `atr_bars` (default 14)
  - bb_width read from existing bollinger feature (upper_a - lower_a)
  - both recomputed every scan cycle by the feature pipeline

Failure handling:
  - insufficient M5 bars -> PASS (don't blanket-block on startup gaps)
  - missing bollinger feature -> PASS
"""
from __future__ import annotations

from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


def _pip_size(symbol: str) -> float:
    return 0.01 if any(j in symbol for j in ("JPY", "MXN")) else 0.0001


def _true_range(bar, prev_close: float) -> float:
    h = float(bar["high"]); l = float(bar["low"])
    return max(h - l, abs(h - prev_close), abs(l - prev_close))


class NaturalTargetFloorGate(BaseGate):
    """Block when live market projection is below the configured minimum."""

    name = "natural_target_floor"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)
        self.min_pips: float = float(self.config.get("min_pips", 7.0))
        self.atr_bars: int = int(self.config.get("atr_bars", 14))
        self.horizon_bars: float = float(self.config.get("horizon_bars", 3.0))

    def _m5_atr_pips(self, ctx: SymbolContext) -> float | None:
        m5 = ctx.snapshot.candles.get("M5")
        if m5 is None:
            return None
        try:
            # Support both list-of-dicts and DataFrame
            if hasattr(m5, "iloc"):
                rows = m5.tail(self.atr_bars + 1)
                if len(rows) < self.atr_bars + 1:
                    return None
                trs = []
                prev_c = float(rows.iloc[0]["close"])
                for i in range(1, len(rows)):
                    bar = rows.iloc[i]
                    trs.append(_true_range(bar, prev_c))
                    prev_c = float(bar["close"])
            else:
                if len(m5) < self.atr_bars + 1:
                    return None
                rows = m5[-(self.atr_bars + 1):]
                trs = []
                prev_c = float(rows[0]["close"])
                for bar in rows[1:]:
                    trs.append(_true_range(bar, prev_c))
                    prev_c = float(bar["close"])
            if not trs:
                return None
            atr = sum(trs) / len(trs)
            return atr / _pip_size(ctx.symbol)
        except Exception as e:
            self._log.debug("[GATE:%s] M5 ATR calc failed: %s", self.name, e)
            return None

    def _bb_width_pips(self, ctx: SymbolContext) -> float | None:
        bb = ctx.features.get("bollinger")
        if bb is None:
            return None
        vals = getattr(bb, "values", None) or {}
        upper = vals.get("upper_a"); lower = vals.get("lower_a")
        if upper is None or lower is None:
            return None
        return (float(upper) - float(lower)) / _pip_size(ctx.symbol)

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        atr_pips = self._m5_atr_pips(ctx)
        bb_pips  = self._bb_width_pips(ctx)

        # Insufficient data — pass (do not blanket-block during startup or
        # when feature pipeline is still warming up).
        if atr_pips is None and bb_pips is None:
            return GateResult(
                gate_name=self.name,
                passed=True,
                reason="insufficient_market_data",
                metrics={"min_pips": self.min_pips},
            )

        proj_atr = (atr_pips * self.horizon_bars) if atr_pips is not None else float("inf")
        proj_bb  = (bb_pips / 2.0) if bb_pips is not None else float("inf")
        projection = min(proj_atr, proj_bb)

        if projection < self.min_pips:
            reason = (
                f"market_projection_{projection:.1f}p_below_floor_{self.min_pips:.1f}p"
                f" (atr_m5={atr_pips:.1f}p*{self.horizon_bars:g}={proj_atr:.1f}p, "
                f"bb_width={bb_pips:.1f}p/2={proj_bb:.1f}p)"
                if atr_pips is not None and bb_pips is not None
                else f"market_projection_{projection:.1f}p_below_floor_{self.min_pips:.1f}p"
            )
            self._log.info(
                "[GATE:%s] FAILED symbol=%s strategy=%s %s",
                self.name, candidate.symbol, candidate.strategy, reason,
            )
            return GateResult(
                gate_name=self.name,
                passed=False,
                reason=reason,
                metrics={
                    "min_pips": self.min_pips,
                    "projection_pips": projection,
                    "atr_m5_pips": atr_pips or -1.0,
                    "bb_width_pips": bb_pips or -1.0,
                    "horizon_bars": self.horizon_bars,
                },
            )

        return GateResult(
            gate_name=self.name,
            passed=True,
            reason=f"market_projection_{projection:.1f}p_above_floor_{self.min_pips:.1f}p",
            metrics={
                "score": min(1.0, projection / 24.0),
                "min_pips": self.min_pips,
                "projection_pips": projection,
                "atr_m5_pips": atr_pips or -1.0,
                "bb_width_pips": bb_pips or -1.0,
                "horizon_bars": self.horizon_bars,
            },
        )
