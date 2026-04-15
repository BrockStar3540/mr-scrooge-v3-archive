"""Overhead-to-Range ratio feature calculator."""

from __future__ import annotations

import logging
from datetime import datetime

from scrooge_v3.core.types import FeatureResult, MarketSnapshot

log = logging.getLogger("scrooge_v3.features.otr")


class OverheadRatioCalculator:
    """
    Computes the overhead-to-range ratio.

    OTR = total_round_trip_spread / range_half

    Requires zone_detector feature to have run first (for session_range).
    The caller must pass total_overhead in state["total_overhead"] and
    range_half in state["range_half"] (or this module reads from
    previously computed zone_detector results in state).

    Returns FeatureResult with values:
        otr_ratio      — overhead as fraction of range_half
        total_overhead — total round-trip spread cost
        range_half     — half the session range
    """

    name: str = "otr"

    def compute(
        self, symbol: str, snapshot: MarketSnapshot, state: dict
    ) -> FeatureResult:
        total_overhead = state.get("total_overhead", snapshot.spread * 2)
        range_half = state.get("range_half", 0.0)

        if range_half <= 0:
            log.warning(f"{symbol}: range_half is zero or negative, OTR undefined")
            return FeatureResult(
                name=self.name,
                values={"otr_ratio": float("inf"), "total_overhead": total_overhead, "range_half": range_half},
                computed_at=datetime.now(),
            )

        otr_ratio = total_overhead / range_half

        return FeatureResult(
            name=self.name,
            values={
                "otr_ratio": otr_ratio,
                "total_overhead": total_overhead,
                "range_half": range_half,
            },
            computed_at=datetime.now(),
        )
