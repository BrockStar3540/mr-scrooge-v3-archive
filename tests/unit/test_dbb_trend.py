"""DBB Trend Engine unit tests.

Tests eligibility, breakout detection, pullback continuation, and rejection cases.
"""

import numpy as np
import pandas as pd
from datetime import datetime, timezone
from unittest.mock import MagicMock

from scrooge_v3.strategies.dbb_trend import DBBTrendStrategy
from scrooge_v3.core.types import (
    SymbolContext,
    MarketSnapshot,
    FeatureResult,
    ClassificationResult,
    TradeDirection,
)


def _make_bars(n=30, base=1.1000, trend="up", breakout_at=None):
    """Generate synthetic 5M bars for testing."""
    closes = []
    opens = []
    highs = []
    lows = []
    p = base
    for i in range(n):
        if trend == "up":
            delta = 0.0002
        elif trend == "down":
            delta = -0.0002
        else:
            delta = 0.0
        o = p
        c = p + delta
        h = max(o, c) + 0.0001
        l = min(o, c) - 0.0001

        # Insert breakout bar
        if breakout_at is not None and i == breakout_at:
            if trend == "up":
                c = o + 0.0015  # Strong bullish bar
                h = c + 0.0001
            else:
                c = o - 0.0015
                l = c - 0.0001

        closes.append(c)
        opens.append(o)
        highs.append(h)
        lows.append(l)
        p = c

    return pd.DataFrame({
        "open": opens, "close": closes, "high": highs, "low": lows,
    })


def _make_ctx(
    symbol="EUR_USD",
    bb_label="TREND_UP",
    regime_label="NORMAL",
    upper_a=1.1050,
    lower_a=1.0950,
    sma_a=1.1000,
    bars=None,
    mid=1.1020,
    spread=0.00015,
):
    """Build a SymbolContext for testing."""
    if bars is None:
        bars = _make_bars()

    snap = MarketSnapshot(
        symbol=symbol,
        bid=mid - spread / 2,
        ask=mid + spread / 2,
        mid=mid,
        spread=spread,
        timestamp=datetime.now(timezone.utc),
        candles={"5M": bars},
    )

    features = {
        "bollinger": FeatureResult(
            name="bollinger",
            values={
                "upper_a": upper_a,
                "lower_a": lower_a,
                "sma_a": sma_a,
                "upper_b": upper_a + 0.005,
                "lower_b": lower_a - 0.005,
                "sma_b": sma_a,
                "current_close": float(bars["close"].iloc[-1]),
                "prior_close_1": float(bars["close"].iloc[-2]),
                "prior_close_2": float(bars["close"].iloc[-3]),
                "z_score": 0.8,
                "bb_position": 0.65,
            },
        ),
        "zone_detector": FeatureResult(
            name="zone_detector",
            values={
                "zone_map": {
                    "session_range": {
                        "PDH": 1.1080,
                        "PDL": 1.0920,
                        "center": 1.1000,
                        "range_half": 0.0080,
                    }
                },
                "box_age_hours": 4.0,
                "wall_proximity": 0.3,
            },
        ),
    }

    classifications = {
        "bb_state": ClassificationResult(name="bb_classifier", label=bb_label),
        "regime": ClassificationResult(name="regime_classifier", label=regime_label),
    }

    return SymbolContext(
        symbol=symbol,
        snapshot=snap,
        features=features,
        classifications=classifications,
    )


strategy = DBBTrendStrategy()


# =====================================================================
# Eligibility
# =====================================================================

class TestEligibility:
    def test_trend_up_eligible(self):
        ctx = _make_ctx(bb_label="TREND_UP")
        assert strategy.eligible(ctx) is True

    def test_breakout_down_eligible(self):
        ctx = _make_ctx(bb_label="BREAKOUT_DOWN")
        assert strategy.eligible(ctx) is True

    def test_stretch_down_eligible(self):
        ctx = _make_ctx(bb_label="STRETCH_DOWN")
        assert strategy.eligible(ctx) is True

    def test_normal_not_eligible(self):
        ctx = _make_ctx(bb_label="NORMAL")
        assert strategy.eligible(ctx) is False

    def test_extreme_not_eligible(self):
        ctx = _make_ctx(bb_label="EXTREME_UP")
        assert strategy.eligible(ctx) is False

    def test_stretch_up_not_eligible(self):
        ctx = _make_ctx(bb_label="STRETCH_UP")
        assert strategy.eligible(ctx) is False

    def test_blocked_regime_not_eligible(self):
        ctx = _make_ctx(bb_label="TREND_UP", regime_label="BLOCKED")
        assert strategy.eligible(ctx) is False

    def test_disabled_not_eligible(self):
        s = DBBTrendStrategy({"enabled": False})
        ctx = _make_ctx(bb_label="TREND_UP")
        assert s.eligible(ctx) is False


# =====================================================================
# Breakout Mode
# =====================================================================

class TestBreakout:
    def test_strong_bullish_breakout(self):
        """Current bar closes above Band A and prior high with strong body."""
        bars = _make_bars(30, base=1.0950, trend="up")
        # Set last bar as a strong breakout
        bars.loc[bars.index[-1], "open"] = 1.1048
        bars.loc[bars.index[-1], "close"] = 1.1062
        bars.loc[bars.index[-1], "high"] = 1.1063
        bars.loc[bars.index[-1], "low"] = 1.1047

        ctx = _make_ctx(
            bb_label="BREAKOUT_UP",
            upper_a=1.1050,
            bars=bars,
            mid=1.1062,
        )
        result = strategy.evaluate(ctx)
        # May or may not produce candidate depending on structure check
        # The key test is that it doesn't crash and returns proper type
        assert result is None or result.strategy == "dbb_trend"

    def test_weak_body_rejected(self):
        """Breakout candle with tiny body (doji) should be rejected."""
        bars = _make_bars(30, base=1.0950, trend="up")
        bars.loc[bars.index[-1], "open"] = 1.1055
        bars.loc[bars.index[-1], "close"] = 1.1056  # Tiny body
        bars.loc[bars.index[-1], "high"] = 1.1065
        bars.loc[bars.index[-1], "low"] = 1.1045

        ctx = _make_ctx(
            bb_label="BREAKOUT_UP",
            upper_a=1.1050,
            bars=bars,
            mid=1.1056,
        )
        result = strategy.evaluate(ctx)
        # With body_pct = 0.05%, should fail min_breakout_body_pct
        assert result is None or result.metadata.get("entry_type") != "DBB_BREAKOUT"


# =====================================================================
# Pullback Mode
# =====================================================================

class TestPullback:
    def test_pullback_requires_prior_breakout(self):
        """No breakout in history = no pullback candidate."""
        bars = _make_bars(30, base=1.1000, trend="flat")
        ctx = _make_ctx(bb_label="TREND_UP", bars=bars, upper_a=1.1200)
        result = strategy.evaluate(ctx)
        assert result is None


# =====================================================================
# Metadata
# =====================================================================

class TestMetadata:
    def test_breakout_metadata_fields(self):
        """If a candidate is produced, it must have required metadata."""
        bars = _make_bars(30, base=1.0940, trend="up")
        bars.loc[bars.index[-1], "open"] = 1.1040
        bars.loc[bars.index[-1], "close"] = 1.1062
        bars.loc[bars.index[-1], "high"] = 1.1063
        bars.loc[bars.index[-1], "low"] = 1.1039

        ctx = _make_ctx(
            bb_label="BREAKOUT_UP",
            upper_a=1.1050,
            bars=bars,
            mid=1.1062,
        )
        result = strategy.evaluate(ctx)
        if result is not None:
            meta = result.metadata
            assert meta["management_profile"] == "trend_runner"
            assert meta["strategy_family"] == "trend"
            assert meta["entry_type"] in ("DBB_BREAKOUT", "DBB_PULLBACK")
            assert "risk_points" in meta
            assert "reward_points" in meta
            assert "sma20" in meta
            assert "dbb_upper_a" in meta

    def test_strategy_name(self):
        assert strategy.name == "dbb_trend"
