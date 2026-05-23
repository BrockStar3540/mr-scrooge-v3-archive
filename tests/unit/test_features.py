"""Unit tests for feature modules — EMA, Volume, RSI, enriched Bollinger/ATR."""

from datetime import datetime, timezone

import numpy as np
import pandas as pd

from scrooge_v3.core.types import MarketSnapshot


def _snapshot(symbol="EUR_USD", mid=1.085, spread=0.00014, candles=None):
    return MarketSnapshot(
        symbol=symbol, bid=mid - spread / 2, ask=mid + spread / 2,
        mid=mid, spread=spread, timestamp=datetime.now(timezone.utc),
        candles=candles or {},
    )


def _hourly_bars(n=60, base_close=1.085, vol=1000):
    """Generate fake hourly bars with slight randomness."""
    np.random.seed(42)
    closes = base_close + np.cumsum(np.random.randn(n) * 0.0005)
    opens = closes - np.random.randn(n) * 0.0003
    highs = np.maximum(opens, closes) + abs(np.random.randn(n) * 0.0002)
    lows = np.minimum(opens, closes) - abs(np.random.randn(n) * 0.0002)
    volumes = np.full(n, vol) + np.random.randint(-100, 100, n)
    idx = pd.date_range(end=datetime.now(), periods=n, freq="h")
    return pd.DataFrame({
        "open": opens, "high": highs, "low": lows,
        "close": closes, "volume": volumes,
    }, index=idx)


def _daily_bars(n=20, base_close=1.085):
    np.random.seed(99)
    closes = base_close + np.cumsum(np.random.randn(n) * 0.002)
    opens = closes - np.random.randn(n) * 0.001
    highs = np.maximum(opens, closes) + abs(np.random.randn(n) * 0.003)
    lows = np.minimum(opens, closes) - abs(np.random.randn(n) * 0.003)
    idx = pd.date_range(end=datetime.now(), periods=n, freq="D")
    return pd.DataFrame({
        "open": opens, "high": highs, "low": lows,
        "close": closes, "volume": np.full(n, 50000),
    }, index=idx)


# =====================================================================
# EMA Calculator
# =====================================================================

class TestEMACalculator:
    def test_computes_ema20_and_ema50(self):
        from scrooge_v3.features.ema import EMACalculator
        calc = EMACalculator()
        bars = _hourly_bars(60)
        snap = _snapshot(candles={"1H": bars})
        result = calc.compute("EUR_USD", snap, {})

        assert "ema20" in result.values
        assert "ema50" in result.values
        assert result.values["ema20"] > 0
        assert result.values["ema50"] > 0

    def test_distance_pct_computed(self):
        from scrooge_v3.features.ema import EMACalculator
        calc = EMACalculator()
        bars = _hourly_bars(60)
        snap = _snapshot(candles={"1H": bars})
        result = calc.compute("EUR_USD", snap, {"box_range": 0.01})

        assert "ema20_dist_pct" in result.values
        assert "ema50_dist_pct" in result.values
        assert isinstance(result.values["ema20_dist_pct"], float)

    def test_insufficient_bars_returns_zeros(self):
        from scrooge_v3.features.ema import EMACalculator
        calc = EMACalculator()
        bars = _hourly_bars(10)
        snap = _snapshot(candles={"1H": bars})
        result = calc.compute("EUR_USD", snap, {})

        assert result.values["ema20"] == 0.0
        assert result.values["ema50"] == 0.0


# =====================================================================
# Volume Calculator
# =====================================================================

class TestVolumeCalculator:
    def test_computes_ratio(self):
        from scrooge_v3.features.volume import VolumeCalculator
        calc = VolumeCalculator()
        bars = _hourly_bars(30, vol=1000)
        snap = _snapshot(candles={"1H": bars})
        result = calc.compute("EUR_USD", snap, {})

        assert "volume_ratio" in result.values
        ratio = result.values["volume_ratio"]
        assert 0.5 < ratio < 2.0  # should be near 1.0

    def test_no_volume_column_returns_default(self):
        from scrooge_v3.features.volume import VolumeCalculator
        calc = VolumeCalculator()
        bars = _hourly_bars(30).drop(columns=["volume"])
        snap = _snapshot(candles={"1H": bars})
        result = calc.compute("EUR_USD", snap, {})

        assert result.values["volume_ratio"] == 1.0


# =====================================================================
# RSI Calculator
# =====================================================================

class TestRSICalculator:
    def test_computes_rsi(self):
        from scrooge_v3.features.rsi import RSICalculator
        calc = RSICalculator()
        bars = _hourly_bars(30)
        snap = _snapshot(candles={"1H": bars})
        result = calc.compute("EUR_USD", snap, {})

        rsi = result.values["rsi"]
        assert 0 <= rsi <= 100

    def test_insufficient_bars_returns_50(self):
        from scrooge_v3.features.rsi import RSICalculator
        calc = RSICalculator()
        bars = _hourly_bars(5)
        snap = _snapshot(candles={"1H": bars})
        result = calc.compute("EUR_USD", snap, {})

        assert result.values["rsi"] == 50.0


# =====================================================================
# Bollinger Enrichment (z_score, bb_position)
# =====================================================================

class TestBollingerEnrichment:
    def test_z_score_computed(self):
        from scrooge_v3.features.bollinger import BollingerCalculator
        calc = BollingerCalculator({"timeframe": "1H"})
        bars = _hourly_bars(30)
        snap = _snapshot(candles={"1H": bars})
        result = calc.compute("EUR_USD", snap, {})

        assert "z_score" in result.values
        z = result.values["z_score"]
        assert -5.0 < z < 5.0

    def test_bb_position_in_range(self):
        from scrooge_v3.features.bollinger import BollingerCalculator
        calc = BollingerCalculator({"timeframe": "1H"})
        bars = _hourly_bars(30)
        snap = _snapshot(candles={"1H": bars})
        result = calc.compute("EUR_USD", snap, {})

        bbp = result.values["bb_position"]
        assert -0.5 < bbp < 1.5  # can be slightly outside 0-1


# =====================================================================
# ATR Enrichment (adr_consumed)
# =====================================================================

class TestATREnrichment:
    def test_adr_consumed_computed(self):
        from scrooge_v3.features.atr import ATRCalculator
        calc = ATRCalculator()
        bars = _daily_bars(20)
        snap = _snapshot(candles={"D": bars})
        result = calc.compute("EUR_USD", snap, {})

        assert "adr_consumed" in result.values
        adr = result.values["adr_consumed"]
        assert adr >= 0  # today's range / ATR


# =====================================================================
# Strategy Router
# =====================================================================

class TestStrategyRouter:
    def test_stretch_up_blocks_reversal_and_direct(self):
        """STRETCH_UP = 0% WR for reversal/direct (V1 historic). Only box_master_theory
        is allowed under the 2026-05-23 router patch — MTB Pitchfork is PDH/PDL-anchored
        and the V1 STRETCH_UP block reflected direct/reversal failure modes, not MTB's
        distinct entry mechanic. Routing-table family_lock is the real safeguard."""
        from scrooge_v3.core.strategy_router import StrategyRouter
        from scrooge_v3.core.types import SymbolContext, ClassificationResult
        router = StrategyRouter()
        ctx = _snapshot()
        sym_ctx = SymbolContext(symbol="EUR_USD", snapshot=ctx, features={},
                               classifications={"bb_state": ClassificationResult(
                                   name="bb_state", label="STRETCH_UP")})
        allowed = router.get_allowed(sym_ctx)
        assert "reversal" not in allowed
        assert "direct" not in allowed
        assert "dbb_trend" not in allowed
        assert allowed == ["box_master_theory"]

    def test_extreme_down_allows_reversal(self):
        from scrooge_v3.core.strategy_router import StrategyRouter
        from scrooge_v3.core.types import SymbolContext, ClassificationResult
        router = StrategyRouter()
        ctx = _snapshot()
        sym_ctx = SymbolContext(symbol="EUR_USD", snapshot=ctx, features={},
                               classifications={"bb_state": ClassificationResult(
                                   name="bb_state", label="EXTREME_DOWN")})
        allowed = router.get_allowed(sym_ctx)
        assert "reversal" in allowed

    def test_normal_allows_direct(self):
        from scrooge_v3.core.strategy_router import StrategyRouter
        from scrooge_v3.core.types import SymbolContext, ClassificationResult
        router = StrategyRouter()
        ctx = _snapshot()
        sym_ctx = SymbolContext(symbol="EUR_USD", snapshot=ctx, features={},
                               classifications={"bb_state": ClassificationResult(
                                   name="bb_state", label="NORMAL")})
        allowed = router.get_allowed(sym_ctx)
        assert "direct" in allowed
