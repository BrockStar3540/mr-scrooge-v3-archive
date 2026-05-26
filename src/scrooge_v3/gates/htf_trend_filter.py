"""Higher-Timeframe Trend Filter — daily directional bias gate.

Computes bias as sign(close_now - close_N_periods_ago) on the daily
candles in snapshot.candles["D"]. If a candidate's direction does not
match the bias, the gate flags it. By default in OBSERVE mode the gate
only logs what it would have blocked — it does NOT block. Set
gates.htf_trend_filter.mode="hard" to enforce.

Brock 2026-05-26: replay lab confirmed +37%% to +57%% aggregate return
on 6 months when this filter is applied with 4-week lookback, vs
-17%% to -24%% with no filter. 6.8yr corpus validation pending.
"""
from __future__ import annotations

from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


class HTFTrendFilterGate(BaseGate):
    """Block (or observe) candidates that fight HTF directional bias."""

    name = "htf_trend_filter"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.OBSERVE,
    ) -> None:
        super().__init__(config, mode)
        self.lookback_periods: int = int(self.config.get("lookback_periods", 20))
        self.htf: str = str(self.config.get("htf", "D"))
        self.neutral_pct: float = float(self.config.get("neutral_pct", 0.0))

    def _compute_bias(self, ctx: SymbolContext) -> tuple[str | None, float | None]:
        bars = ctx.snapshot.candles.get(self.htf)
        if bars is None or len(bars) == 0:
            bars = ctx.snapshot.candles.get("D")
        if bars is None or len(bars) <= self.lookback_periods:
            return None, None
        try:
            close_now = float(bars["close"].iloc[-1])
            close_then = float(bars["close"].iloc[-1 - self.lookback_periods])
            if not close_then:
                return None, None
            pct_change = (close_now - close_then) / close_then
            if abs(pct_change) < self.neutral_pct:
                return "neutral", pct_change
            return ("long" if pct_change > 0 else "short"), pct_change
        except Exception:
            return None, None

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        bias, pct = self._compute_bias(ctx)
        if bias is None:
            return GateResult(
                gate_name=self.name,
                passed=True,
                reason="insufficient_htf_data",
                metrics={"lookback": self.lookback_periods, "htf": self.htf},
            )
        if bias == "neutral":
            # Pass through; neutral bias means we don\'t take a stand
            return GateResult(
                gate_name=self.name,
                passed=True,
                reason=f"htf_neutral:pct={pct:+.4f}",
                metrics={"htf_bias": "neutral", "htf_pct": pct,
                         "lookback": self.lookback_periods, "htf": self.htf},
            )
        cand_dir = candidate.direction.value
        if cand_dir == bias:
            return GateResult(
                gate_name=self.name,
                passed=True,
                reason=f"htf_aligned:bias={bias} pct={pct:+.4f}",
                metrics={"score": 1.0, "htf_bias": bias, "htf_pct": pct,
                         "lookback": self.lookback_periods, "htf": self.htf},
            )
        # Misaligned
        reason = f"htf_misaligned:cand={cand_dir} bias={bias} pct={pct:+.4f}"
        self._log.info(
            "[GATE:%s] %s symbol=%s strategy=%s %s",
            self.name, "OBSERVED" if self.mode == GateMode.OBSERVE else "FAILED",
            candidate.symbol, candidate.strategy, reason,
        )
        return GateResult(
            gate_name=self.name,
            passed=False,
            reason=reason,
            metrics={"htf_bias": bias, "htf_pct": pct, "cand_dir": cand_dir,
                     "lookback": self.lookback_periods, "htf": self.htf},
        )
