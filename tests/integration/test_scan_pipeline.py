"""Integration test — ScanPipeline with mock market data produces candidates."""

from datetime import datetime, timezone

import numpy as np
import pandas as pd

from scrooge_v3.core.events import EventBus
from scrooge_v3.core.registry import ModuleRegistry
from scrooge_v3.core.scan_pipeline import ScanPipeline
from scrooge_v3.core.strategy_router import StrategyRouter
from scrooge_v3.core.types import MarketSnapshot
from scrooge_v3.features.atr import ATRCalculator
from scrooge_v3.features.bollinger import BollingerCalculator
from scrooge_v3.features.ema import EMACalculator
from scrooge_v3.features.rsi import RSICalculator
from scrooge_v3.features.volume import VolumeCalculator
from scrooge_v3.strategies.v3_scorer import V3HybridScorer


def _make_bars(n, base, tf_minutes=5):
    """Generate plausible OHLCV bars."""
    np.random.seed(42)
    closes = base + np.cumsum(np.random.randn(n) * 0.0003)
    opens = closes - np.random.randn(n) * 0.0002
    highs = np.maximum(opens, closes) + abs(np.random.randn(n) * 0.0002)
    lows = np.minimum(opens, closes) - abs(np.random.randn(n) * 0.0002)
    freq = f"{tf_minutes}min" if tf_minutes < 60 else f"{tf_minutes // 60}h"
    if tf_minutes >= 1440:
        freq = "D"
    idx = pd.date_range(end=datetime.now(), periods=n, freq=freq)
    return pd.DataFrame({
        "open": opens, "high": highs, "low": lows,
        "close": closes, "volume": np.full(n, 1000),
    }, index=idx)


def _snapshot(symbol="EUR_USD", mid=1.085):
    """Create a MarketSnapshot with all required candle timeframes."""
    spread = 0.00014
    return MarketSnapshot(
        symbol=symbol, bid=mid - spread / 2, ask=mid + spread / 2,
        mid=mid, spread=spread, timestamp=datetime.now(timezone.utc),
        candles={
            "D": _make_bars(20, mid, 1440),
            "1H": _make_bars(60, mid, 60),
            "5M": _make_bars(50, mid, 5),
        },
    )


def _build_pipeline():
    """Wire up a minimal pipeline with features and scorer (no gates)."""
    registry = ModuleRegistry()

    # Register features
    registry.register("features", "atr", ATRCalculator())
    registry.register("features", "bollinger", BollingerCalculator({"timeframe": "1H"}))
    registry.register("features", "ema", EMACalculator())
    registry.register("features", "rsi", RSICalculator())
    registry.register("features", "volume", VolumeCalculator())

    # No classifiers, strategies, or gates — just test feature pipeline
    scorer = V3HybridScorer()

    return ScanPipeline(
        registry=registry,
        router=StrategyRouter(),
        event_bus=EventBus(),
        scorer=scorer,
    )


class TestScanPipelineFeatures:
    def test_features_compute_without_crash(self):
        """All features run on mock data without exceptions."""
        pipeline = _build_pipeline()
        snap = _snapshot()
        # scan_symbol won't produce candidates (no strategies registered)
        # but features should compute cleanly
        result = pipeline.scan_symbol("EUR_USD", snap)
        # No candidate (no strategies), but no crash
        assert result is None

    def test_scan_universe_returns_tuple(self):
        pipeline = _build_pipeline()
        snaps = {"EUR_USD": _snapshot(), "USD_JPY": _snapshot("USD_JPY", 150.5)}
        candidates, reports = pipeline.scan_universe(["EUR_USD", "USD_JPY"], snaps)
        assert isinstance(candidates, list)
        assert isinstance(reports, list)
        assert len(reports) == 2


class TestScanPipelineEvents:
    def test_emits_features_computed_event(self):
        from scrooge_v3.core.events import FEATURES_COMPUTED
        pipeline = _build_pipeline()
        events = []
        pipeline.event_bus.subscribe(FEATURES_COMPUTED, lambda e: events.append(e))
        pipeline.scan_symbol("EUR_USD", _snapshot())
        assert len(events) == 1
        assert "features" in events[0].payload
