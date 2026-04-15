"""Bollinger Band state classifier.

Uses precomputed bollinger feature results to classify into one of:
  NORMAL, STRETCH_UP, STRETCH_DOWN, EXTREME_UP, EXTREME_DOWN,
  BREAKOUT_UP, BREAKOUT_DOWN, REJECTION_SHORT, REJECTION_LONG

Regime signal deltas:
  BREAKOUT_UP / BREAKOUT_DOWN  -> -2  (directional momentum, bad for mean-reversion)
  EXTREME_UP / EXTREME_DOWN    ->  0  (outlier -- may reverse, may continue)
  REJECTION_SHORT              -> +1  (BB snap-back from top confirms PDH short)
  REJECTION_LONG               -> +1  (BB snap-back from bottom confirms PDL long)
  STRETCH / NORMAL             ->  0
"""

from __future__ import annotations

import logging
from enum import Enum

from scrooge_v3.core.types import ClassificationResult, SymbolContext

log = logging.getLogger("scrooge_v3.classifiers.bb_state")


class BBState(Enum):
    NORMAL = "NORMAL"
    STRETCH_UP = "STRETCH_UP"
    STRETCH_DOWN = "STRETCH_DOWN"
    EXTREME_UP = "EXTREME_UP"
    EXTREME_DOWN = "EXTREME_DOWN"
    BREAKOUT_UP = "BREAKOUT_UP"
    BREAKOUT_DOWN = "BREAKOUT_DOWN"
    REJECTION_SHORT = "REJECTION_SHORT"
    REJECTION_LONG = "REJECTION_LONG"


# Score delta each state contributes to regime score
BB_STATE_DELTA: dict[BBState, int] = {
    BBState.NORMAL: 0,
    BBState.STRETCH_UP: 0,
    BBState.STRETCH_DOWN: 0,
    BBState.EXTREME_UP: 0,
    BBState.EXTREME_DOWN: 0,
    BBState.BREAKOUT_UP: -2,
    BBState.BREAKOUT_DOWN: -2,
    BBState.REJECTION_SHORT: +1,
    BBState.REJECTION_LONG: +1,
}


class BollingerStateClassifier:
    """
    Classifies Bollinger Band state from precomputed band values.

    Reads ctx.features["bollinger"] for band levels and recent closes.
    Implements ClassifierModule protocol.
    """

    name: str = "bb_classifier"

    def classify(self, ctx: SymbolContext) -> ClassificationResult:
        bb = ctx.features.get("bollinger")
        if bb is None or not bb.values:
            return ClassificationResult(
                name=self.name,
                label=BBState.NORMAL.value,
                confidence=0.0,
                metadata={"detail": "No bollinger data available"},
            )

        v = bb.values
        upper_a = v["upper_a"]
        lower_a = v["lower_a"]
        upper_b = v["upper_b"]
        lower_b = v["lower_b"]
        c = v["current_close"]
        c1 = v["prior_close_1"]
        c2 = v["prior_close_2"]

        def _result(state: BBState, detail: str) -> ClassificationResult:
            return ClassificationResult(
                name=self.name,
                label=state.value,
                confidence=1.0,
                metadata={
                    "bb_state": state.value,
                    "score_delta": BB_STATE_DELTA[state],
                    "detail": detail,
                    "upper_a": upper_a,
                    "lower_a": lower_a,
                    "upper_b": upper_b,
                    "lower_b": lower_b,
                    "current_close": c,
                },
            )

        # -- Priority 1: Extreme (beyond Band B) --
        if c > upper_b and upper_b > upper_a:
            return _result(
                BBState.EXTREME_UP,
                f"Close {c:.5f} above Band B upper {upper_b:.5f} -- extreme extension",
            )
        if c < lower_b and lower_b < lower_a:
            return _result(
                BBState.EXTREME_DOWN,
                f"Close {c:.5f} below Band B lower {lower_b:.5f} -- extreme extension",
            )

        # -- Priority 2: Rejection (was outside Band A, now back inside) --
        if c <= upper_a and (c1 > upper_a or c2 > upper_a):
            return _result(
                BBState.REJECTION_SHORT,
                f"Close {c:.5f} re-entered Band A upper {upper_a:.5f} -- snap-back from top",
            )
        if c >= lower_a and (c1 < lower_a or c2 < lower_a):
            return _result(
                BBState.REJECTION_LONG,
                f"Close {c:.5f} re-entered Band A lower {lower_a:.5f} -- snap-back from bottom",
            )

        # -- Priority 3: Breakout (2+ consecutive closes outside Band A, advancing) --
        if c > upper_a and c1 > upper_a and c >= c1:
            return _result(
                BBState.BREAKOUT_UP,
                f"2+ consecutive closes above Band A upper {upper_a:.5f} -- trending breakout up",
            )
        if c < lower_a and c1 < lower_a and c <= c1:
            return _result(
                BBState.BREAKOUT_DOWN,
                f"2+ consecutive closes below Band A lower {lower_a:.5f} -- trending breakout down",
            )

        # -- Priority 4: Stretch (outside Band A, not yet breakout/rejection) --
        if c > upper_a:
            return _result(
                BBState.STRETCH_UP,
                f"Close {c:.5f} above Band A upper {upper_a:.5f} -- stretched, watching",
            )
        if c < lower_a:
            return _result(
                BBState.STRETCH_DOWN,
                f"Close {c:.5f} below Band A lower {lower_a:.5f} -- stretched, watching",
            )

        # -- Normal --
        return _result(
            BBState.NORMAL,
            f"Close {c:.5f} within Band A [{lower_a:.5f} -- {upper_a:.5f}]",
        )
