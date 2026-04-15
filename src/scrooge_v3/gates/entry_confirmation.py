"""Entry confirmation gate -- reversal candle detection."""

from __future__ import annotations

from typing import Any

import pandas as pd

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


class EntryConfirmationGate(BaseGate):
    """Gate 5 -- Reversal candle confirmation.

    Detects wick rejection, engulfing reversal, or standard reversal pattern.
    Returns trigger/stop prices in metrics for position sizing.

    Priority: wick_rejection -> engulfing_reversal -> standard_reversal.
    """

    name = "entry_confirmation"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)
        self.sl_floor_pct: float = self.config.get("sl_floor_pct", 0.0050)
        self.directional_min: int = self.config.get("directional_min", 3)
        self.directional_max: int = self.config.get("directional_max", 5)
        self.volatility_mult: float = self.config.get(
            "high_volatility_atr_mult", 99
        )

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        direction = candidate.direction.value
        bars_5m: pd.DataFrame = ctx.metadata.get("bars_5m", pd.DataFrame())
        bars_1h: pd.DataFrame = ctx.metadata.get("bars_1h", pd.DataFrame())
        session_range = ctx.metadata.get("session_range")
        zone_price: float | None = ctx.metadata.get("zone_price")
        box_stop: float | None = ctx.metadata.get("box_stop")

        # Select timeframe
        is_high_vol = self._is_high_volatility(bars_1h, session_range)
        bars = bars_1h if is_high_vol else bars_5m
        tf_lbl = "1H" if is_high_vol else "5M"

        if len(bars) < 4:
            return GateResult(
                gate_name=self.name,
                passed=False,
                reason="Insufficient bars",
                metrics={"score": 0.0},
            )

        # Priority: wick_rejection -> engulfing_reversal -> standard_reversal
        detectors = [
            (self._detect_wick_rejection, "wick_rejection", 1.0),
            (self._detect_engulfing_reversal, "engulfing_reversal", 1.0),
            (self._detect_standard_reversal, "standard_reversal", 0.7),
        ]

        for detect_fn, signal_type, score in detectors:
            result = detect_fn(
                bars, direction, tf_lbl, zone_price, box_stop
            )
            if result["detected"]:
                confidence_boost = (
                    0.1 if result.get("confidence") == "HIGH" else 0.0
                )
                final_score = min(1.0, score + confidence_boost)
                reason = f"{signal_type} ({tf_lbl}): {result['details']}"
                self._log.debug(
                    "[GATE:%s] PASSED symbol=%s reason=%s",
                    self.name, candidate.symbol, reason,
                )
                return GateResult(
                    gate_name=self.name,
                    passed=True,
                    reason=reason,
                    metrics={
                        "score": final_score,
                        **result,
                    },
                )

        reason = (
            f"No reversal candle (direction={direction}, tf={tf_lbl})"
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

    # -- Signal detectors ---------------------------------------------------

    def _detect_wick_rejection(
        self,
        bars: pd.DataFrame,
        direction: str,
        timeframe: str,
        zone_price: float | None,
        box_stop: float | None,
    ) -> dict[str, Any]:
        """Detect wick rejection pattern (formerly 'john_wick')."""
        for i in range(len(bars) - 4, len(bars) - 1):
            if i < 0:
                continue
            o = float(bars["open"].iloc[i])
            h = float(bars["high"].iloc[i])
            l = float(bars["low"].iloc[i])
            c = float(bars["close"].iloc[i])
            body = abs(c - o)
            total_range = h - l
            if total_range == 0:
                continue
            upper_wick = h - max(o, c)
            lower_wick = min(o, c) - l

            if direction == "long":
                wick_ratio = lower_wick / total_range
                if (
                    wick_ratio >= 0.60
                    and (body / total_range) <= 0.30
                    and lower_wick >= body * 2
                ):
                    confirmed = any(
                        float(bars["close"].iloc[j])
                        > float(bars["open"].iloc[j])
                        for j in range(i + 1, len(bars))
                    )
                    if confirmed:
                        trigger = h * 1.0001
                        stop = self._apply_sl_floor(
                            trigger,
                            l * (1 - self.sl_floor_pct),
                            direction,
                        )
                        return {
                            "detected": True,
                            "signal_type": "wick_rejection",
                            "confirmation_type": "wick_rejection",
                            "direction": direction,
                            "trigger_price": trigger,
                            "stop_price": stop,
                            "confidence": "HIGH",
                            "timeframe_used": timeframe,
                            "details": (
                                f"Hammer wick {wick_ratio:.0%}"
                                " + confirmation"
                            ),
                        }
            else:
                wick_ratio = upper_wick / total_range
                if (
                    wick_ratio >= 0.60
                    and (body / total_range) <= 0.30
                    and upper_wick >= body * 2
                ):
                    confirmed = any(
                        float(bars["close"].iloc[j])
                        < float(bars["open"].iloc[j])
                        for j in range(i + 1, len(bars))
                    )
                    if confirmed:
                        trigger = l * 0.9999
                        stop = self._apply_sl_floor(
                            trigger,
                            h * (1 + self.sl_floor_pct),
                            direction,
                        )
                        return {
                            "detected": True,
                            "signal_type": "wick_rejection",
                            "confirmation_type": "wick_rejection",
                            "direction": direction,
                            "trigger_price": trigger,
                            "stop_price": stop,
                            "confidence": "HIGH",
                            "timeframe_used": timeframe,
                            "details": (
                                f"Inv hammer wick {wick_ratio:.0%}"
                                " + confirmation"
                            ),
                        }
        return {"detected": False}

    def _detect_engulfing_reversal(
        self,
        bars: pd.DataFrame,
        direction: str,
        timeframe: str,
        zone_price: float | None,
        box_stop: float | None,
    ) -> dict[str, Any]:
        """Detect engulfing reversal pattern (formerly 'power_of_towers')."""
        for i in range(len(bars) - 2, 0, -1):
            ph = float(bars["high"].iloc[i - 1])
            pl = float(bars["low"].iloc[i - 1])
            po = float(bars["open"].iloc[i - 1])
            pc = float(bars["close"].iloc[i - 1])
            ch = float(bars["high"].iloc[i])
            cl = float(bars["low"].iloc[i])
            co = float(bars["open"].iloc[i])
            cc = float(bars["close"].iloc[i])
            if direction == "long":
                if pc < po and cc > co and cl < pl and ch > ph:
                    trigger = ch * 1.0001
                    stop = self._apply_sl_floor(
                        trigger,
                        cl * (1 - self.sl_floor_pct),
                        direction,
                    )
                    return {
                        "detected": True,
                        "signal_type": "engulfing_reversal",
                        "confirmation_type": "engulfing_reversal",
                        "direction": direction,
                        "trigger_price": trigger,
                        "stop_price": stop,
                        "confidence": "HIGH",
                        "timeframe_used": timeframe,
                        "details": (
                            "Green engulfs full range of prior red"
                        ),
                    }
            else:
                if pc > po and cc < co and ch > ph and cl < pl:
                    trigger = cl * 0.9999
                    stop = self._apply_sl_floor(
                        trigger,
                        ch * (1 + self.sl_floor_pct),
                        direction,
                    )
                    return {
                        "detected": True,
                        "signal_type": "engulfing_reversal",
                        "confirmation_type": "engulfing_reversal",
                        "direction": direction,
                        "trigger_price": trigger,
                        "stop_price": stop,
                        "confidence": "HIGH",
                        "timeframe_used": timeframe,
                        "details": (
                            "Red engulfs full range of prior green"
                        ),
                    }
        return {"detected": False}

    def _detect_standard_reversal(
        self,
        bars: pd.DataFrame,
        direction: str,
        timeframe: str,
        zone_price: float | None,
        box_stop: float | None,
    ) -> dict[str, Any]:
        """Detect standard reversal pattern (formerly 'standard_pitchfork')."""
        closes = bars["close"].values
        opens = bars["open"].values
        highs = bars["high"].values
        lows = bars["low"].values

        for end_idx in range(
            len(bars) - 2, self.directional_min, -1
        ):
            if direction == "long":
                is_reversal = closes[end_idx] > opens[end_idx]
            else:
                is_reversal = closes[end_idx] < opens[end_idx]
            if not is_reversal:
                continue

            count = 0
            for k in range(
                end_idx - 1,
                max(end_idx - self.directional_max - 1, -1),
                -1,
            ):
                if direction == "long":
                    if closes[k] < opens[k]:
                        count += 1
                    else:
                        break
                else:
                    if closes[k] > opens[k]:
                        count += 1
                    else:
                        break

            if count >= self.directional_min:
                if direction == "long":
                    trigger = highs[end_idx] * 1.0001
                    stop = self._apply_sl_floor(
                        trigger,
                        lows[end_idx] * (1 - self.sl_floor_pct),
                        direction,
                    )
                else:
                    trigger = lows[end_idx] * 0.9999
                    stop = self._apply_sl_floor(
                        trigger,
                        highs[end_idx] * (1 + self.sl_floor_pct),
                        direction,
                    )
                conf = "HIGH" if count >= 4 else "MODERATE"
                return {
                    "detected": True,
                    "signal_type": "standard_reversal",
                    "confirmation_type": "standard_reversal",
                    "direction": direction,
                    "trigger_price": trigger,
                    "stop_price": stop,
                    "confidence": conf,
                    "timeframe_used": timeframe,
                    "directional_candles": count,
                    "details": (
                        f"{count} directional candles -> reversal"
                    ),
                }

        return {
            "detected": False,
            "details": (
                f"Need {self.directional_min}-{self.directional_max}"
                " directional candles + reversal"
            ),
        }

    # -- Helpers ------------------------------------------------------------

    def _is_high_volatility(
        self, bars_1h: pd.DataFrame, session_range: Any
    ) -> bool:
        if session_range is None or len(bars_1h) < 2:
            return False
        last_range = (
            float(bars_1h["high"].iloc[-2])
            - float(bars_1h["low"].iloc[-2])
        )
        hourly_atr_equiv = session_range.ATR / 6.5
        return last_range > hourly_atr_equiv * self.volatility_mult

    def _apply_sl_floor(
        self, trigger: float, stop: float, direction: str
    ) -> float:
        if direction == "short":
            return max(stop, trigger * (1 + self.sl_floor_pct))
        return min(stop, trigger * (1 - self.sl_floor_pct))
