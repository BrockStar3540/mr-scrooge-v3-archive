"""Opening state classifier -- gap/opening detection.

Reads the session range from ctx.features["zone_detector"] and determines
how the current session opened relative to the prior session range.

Labels:
  GAP_UP      -- today's open is significantly above prior PDH
  GAP_DOWN    -- today's open is significantly below prior PDL
  DEAD_CENTER -- opened very close to the midpoint (avoid)
  NORMAL_OPEN -- opened within the prior range, no special condition
"""

from __future__ import annotations

import logging

from scrooge_v3.core.types import ClassificationResult, SymbolContext

log = logging.getLogger("scrooge_v3.classifiers.opening")


class OpeningStateClassifier:
    """
    Classifies the current session's opening condition relative to the prior
    session range.

    Implements ClassifierModule protocol.
    """

    name: str = "opening"

    def __init__(self, config: dict | None = None):
        config = config or {}
        # Gap threshold as fraction of range (e.g., 0.5 = open must be > PDH + 50% of range)
        self.gap_threshold_pct = config.get("gap_threshold_pct", 0.005)  # 0.5% of price
        # Dead center band -- fraction of range around center considered "dead"
        self.dead_center_pct = config.get("dead_center_pct", 0.10)  # 10% of range

    def classify(self, ctx: SymbolContext) -> ClassificationResult:
        zd = ctx.features.get("zone_detector")
        if zd is None or not zd.values:
            return ClassificationResult(
                name=self.name,
                label="UNKNOWN",
                confidence=0.0,
                metadata={"detail": "No zone_detector data available"},
            )

        zone_map = zd.values.get("zone_map")
        if zone_map is None:
            return ClassificationResult(
                name=self.name,
                label="UNKNOWN",
                confidence=0.0,
                metadata={"detail": "No zone_map in zone_detector output"},
            )

        sr = zone_map.session_range

        # Use gap detection already computed by zone_detector
        if sr.gap_detected:
            label = "GAP_UP" if sr.gap_direction == "up" else "GAP_DOWN"
            return ClassificationResult(
                name=self.name,
                label=label,
                confidence=1.0,
                metadata={
                    "gap_direction": sr.gap_direction,
                    "PDH": sr.PDH,
                    "PDL": sr.PDL,
                    "detail": f"Gap {sr.gap_direction} detected by zone detector",
                },
            )

        # Check if current price is near center (dead center)
        current_price = ctx.snapshot.mid
        center = sr.center
        range_half = sr.range_half

        if range_half > 0:
            distance_from_center = abs(current_price - center)
            center_ratio = distance_from_center / range_half

            if center_ratio < self.dead_center_pct:
                return ClassificationResult(
                    name=self.name,
                    label="DEAD_CENTER",
                    confidence=1.0,
                    metadata={
                        "current_price": current_price,
                        "center": center,
                        "distance_pct": center_ratio,
                        "detail": (
                            f"Price {current_price:.5f} within {center_ratio:.1%} of center "
                            f"{center:.5f} -- avoid trading"
                        ),
                    },
                )

        # Normal open -- within range, no gap, not dead center
        return ClassificationResult(
            name=self.name,
            label="NORMAL_OPEN",
            confidence=1.0,
            metadata={
                "current_price": current_price,
                "PDH": sr.PDH,
                "PDL": sr.PDL,
                "center": sr.center,
                "detail": "Normal opening within prior session range",
            },
        )
