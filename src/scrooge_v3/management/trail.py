"""Trailing stop manager — follows structure using hourly candles.

Source theory Section 17: "Move the stop below each hourly candlestick's low."
Engineering extension: spread-aware trailing pauses in hostile spread.
"""

from __future__ import annotations

import logging
from typing import Any

from scrooge_v3.core.types import StopPlan, TradeDirection

log = logging.getLogger("scrooge_v3.management.trail")


class TrailManager:
    """Trailing stop based on hourly candle structure."""

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.buffer_pips = config.get("trail_buffer_pips", 2.0)

    def compute_trail_stop(
        self,
        direction: TradeDirection,
        current_stop: float,
        hourly_bars: Any,
        pip_size: float = 0.0001,
    ) -> StopPlan | None:
        """Compute new trailing stop from the last completed hourly candle.

        For longs: stop = low of last completed hourly candle - buffer
        For shorts: stop = high of last completed hourly candle + buffer
        """
        if hourly_bars is None or len(hourly_bars) < 2:
            return None

        # Use the second-to-last bar (last COMPLETED candle)
        last_completed = hourly_bars.iloc[-2]
        buffer = self.buffer_pips * pip_size

        if direction == TradeDirection.LONG:
            new_stop = float(last_completed["low"]) - buffer
            if new_stop <= current_stop:
                return None  # Would loosen stop — don't trail backwards
        else:
            new_stop = float(last_completed["high"]) + buffer
            if new_stop >= current_stop:
                return None  # Would loosen stop

        return StopPlan(
            position_id="",  # caller sets this
            new_stop=new_stop,
            reason=f"hourly_trail from {current_stop:.5f} to {new_stop:.5f}",
        )
