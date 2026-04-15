"""Directional pressure gate -- detects explosive directional push into zone."""

from __future__ import annotations

from typing import Any

import pandas as pd

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


class DirectionalPressureGate(BaseGate):
    """Gate 4 -- Directional pressure detection.

    Requires fast directional move into zone AND termination at zone.
    Formerly known as "sucker move" detection.
    """

    name = "directional_pressure"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)
        self.min_candles: int = self.config.get("pressure_min_candles", 3)
        self.max_candles: int = self.config.get("pressure_max_candles", 5)
        self.zone_tolerance: float = self.config.get(
            "pressure_zone_tolerance", 0.005
        )
        self.atr_valid_pct: float = self.config.get("atr_valid_pct", 0.60)
        self.atr_strong_pct: float = self.config.get(
            "atr_high_confidence_pct", 0.80
        )

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        direction = candidate.direction.value
        bars: pd.DataFrame = ctx.metadata.get("bars_5m", pd.DataFrame())
        target_zone = ctx.metadata.get("target_zone")
        session_range = ctx.metadata.get("session_range")
        atr = session_range.ATR if session_range else 0

        search_window = self.max_candles + 2

        if len(bars) < search_window:
            return GateResult(
                gate_name=self.name,
                passed=False,
                reason="Insufficient bars to evaluate directional pressure",
                metrics={"score": 0.0},
            )

        closes = bars["close"].values
        opens = bars["open"].values
        best_count, best_start = 0, -1
        lookback = min(len(bars) - 1, 25)

        for start in range(
            len(bars) - lookback, len(bars) - self.min_candles
        ):
            end = min(start + search_window, len(bars) - 1)
            directional = sum(
                1
                for i in range(start, end)
                if (direction == "short" and closes[i] > opens[i])
                or (direction == "long" and closes[i] < opens[i])
            )
            if direction == "short":
                net_ok = closes[end - 1] > opens[start]
            else:
                net_ok = closes[end - 1] < opens[start]

            if (
                directional >= self.min_candles
                and net_ok
                and directional > best_count
            ):
                best_count, best_start = directional, start

        if best_count < self.min_candles:
            candle_color = "green" if direction == "short" else "red"
            reason = (
                f"Need {self.min_candles}+ {candle_color} candles"
                f" -- found {best_count}"
            )
            self._log.debug(
                "[GATE:%s] FAILED symbol=%s reason=%s",
                self.name, candidate.symbol, reason,
            )
            return GateResult(
                gate_name=self.name,
                passed=False,
                reason=reason,
                metrics={"score": 0.0},
            )

        search_end = min(best_start + search_window, len(bars))
        if direction == "short":
            move_start = float(bars["low"].iloc[best_start])
            move_end = float(
                bars["high"].iloc[best_start:search_end].max()
            )
        else:
            move_start = float(bars["high"].iloc[best_start])
            move_end = float(
                bars["low"].iloc[best_start:search_end].min()
            )

        move_size = abs(move_end - move_start)
        atr_consumed = move_size / atr if atr > 0 else 0
        strength = (
            "strong"
            if atr_consumed >= self.atr_strong_pct
            else "valid"
            if atr_consumed >= self.atr_valid_pct
            else "weak"
        )

        # Did move terminate at zone?
        terminating = False
        if target_zone is not None:
            end_price = move_end
            zone_price = (
                target_zone.price
                if hasattr(target_zone, "price")
                else target_zone
            )
            if (
                abs(end_price - zone_price) / max(zone_price, 1e-9)
                < self.zone_tolerance
            ):
                terminating = True

        if not terminating:
            reason = "Directional pressure not terminating at zone"
            self._log.debug(
                "[GATE:%s] FAILED symbol=%s reason=%s",
                self.name, candidate.symbol, reason,
            )
            return GateResult(
                gate_name=self.name,
                passed=False,
                reason=reason,
                metrics={
                    "score": 0.0,
                    "candle_count": best_count,
                    "atr_consumed": atr_consumed,
                    "strength": strength,
                },
            )

        score = 1.0 if strength == "strong" else 0.7 if strength == "valid" else 0.4

        self._log.debug(
            "[GATE:%s] PASSED symbol=%s reason=%d directional candles (%s)",
            self.name, candidate.symbol, best_count, strength,
        )
        return GateResult(
            gate_name=self.name,
            passed=True,
            reason=(
                f"{best_count} directional candles ({strength})"
                " terminating at zone"
            ),
            metrics={
                "score": score,
                "candle_count": best_count,
                "atr_consumed": atr_consumed,
                "strength": strength,
                "move_size": move_size,
            },
        )
