"""Smoke test — verify the system can import and construct without crash.

Does NOT connect to OANDA or make real API calls. Tests that all modules
load, wire together, and the configuration is valid.
"""

import json
from pathlib import Path


def test_all_imports():
    """Every module can be imported without error."""
    from scrooge_v3.core.runtime import Runtime
    from scrooge_v3.core.config import ConfigStore
    from scrooge_v3.core.events import EventBus
    from scrooge_v3.core.registry import ModuleRegistry
    from scrooge_v3.core.scan_pipeline import ScanPipeline
    from scrooge_v3.core.state_controller import StateController
    from scrooge_v3.core.strategy_router import StrategyRouter
    from scrooge_v3.features import (
        ATRCalculator, BollingerCalculator, EMACalculator,
        OverheadRatioCalculator, RSICalculator, VolumeCalculator, ZoneDetector,
    )
    from scrooge_v3.classifiers.bb_state import BollingerStateClassifier
    from scrooge_v3.classifiers.regime import RegimeClassifier
    from scrooge_v3.strategies import ReversalStrategy, TrendStrategy, V3HybridScorer
    from scrooge_v3.strategies.direct_entry import DirectEntryStrategy
    from scrooge_v3.gates import (
        SpreadGate, OverheadRatioGate, RiskRewardGate,
        EntryConfirmationGate, ExhaustionFilterGate, DebounceGate,
        ZoneEntryCapGate, RegimeFloorGate,
    )
    from scrooge_v3.market import OANDAAdapter, DryRunAdapter, FeeCalculator
    from scrooge_v3.dashboard import create_app, LiveState


def test_config_loads():
    """default.json is valid JSON and has required sections."""
    config_path = Path(__file__).parent.parent.parent / "config" / "default.json"
    assert config_path.exists(), f"Config file not found: {config_path}"

    with open(config_path) as f:
        cfg = json.load(f)

    assert "runtime" in cfg
    assert "risk" in cfg
    assert "features" in cfg
    assert "gates" in cfg
    assert "strategies" in cfg

    # Key values
    assert cfg["risk"]["max_daily_loss_pct"] > 0
    assert cfg["risk"]["max_open_positions"] > 0
    assert cfg["gates"]["rr"]["reversal_min_rr"] == 1.0
    assert cfg["gates"]["spread"]["spread_pct_of_half"] == 0.10


def test_scorer_deterministic():
    """Same inputs always produce same score."""
    from scrooge_v3.strategies.v3_scorer import V3HybridScorer
    scorer = V3HybridScorer()
    factors = {
        "hour": 3, "bage": 4, "ns": 5, "vr": 1.0, "mom": 2, "dc": 4,
        "zs": 0.8, "bbp": 0.72, "e50d": 65, "e20d": 22, "otr": 12,
        "adr": 0.6, "dur": 60, "wp": 0.08, "bp": 0.2, "bbs": "REJ_L", "rsi": 35,
    }
    r1 = scorer._compute_score(factors)
    r2 = scorer._compute_score(factors)
    assert r1.score == r2.score
    assert r1.tier == r2.tier
    assert r1.breakdown == r2.breakdown


def test_fee_calculator_otr_inversion():
    """Low OTR must be flagged as 'too_low', not 'excellent'."""
    from scrooge_v3.market.fee_calculator import FeeCalculator
    fc = FeeCalculator()

    # Very low OTR (wide box, small spread)
    result = fc.calculate("EUR_USD", 0.00014, half_box=0.05)
    assert result.otr_category == "too_low"
    assert not result.viable

    # Sweet spot OTR
    result2 = fc.calculate("EUR_USD", 0.00014, half_box=0.002)
    assert result2.otr_category == "sweet_spot"
    assert result2.viable


def test_live_state():
    """LiveState creates snapshots."""
    from scrooge_v3.dashboard.live_state import LiveState
    state = LiveState()
    state.update(cycle_count=5, equity=1500.0)
    snap = state.snapshot()
    assert snap["system"]["cycle_count"] == 5
    assert snap["account"]["equity"] == 1500.0
