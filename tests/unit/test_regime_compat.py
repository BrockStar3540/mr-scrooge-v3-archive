"""Unit test for RegimeCompatGate (observe-only)."""
from datetime import datetime, timezone

import pytest

from scrooge_v3.core.types import (
    ClassificationResult, FeatureResult, GateMode, MarketSnapshot,
    SymbolContext, TradeCandidate, TradeDirection,
)
from scrooge_v3.gates.regime_compat import RegimeCompatGate


def _ctx(regime_label: str, ema20: float, ema50: float) -> SymbolContext:
    ctx = SymbolContext(
        symbol="USD_JPY",
        snapshot=MarketSnapshot(
            symbol="USD_JPY", bid=150.0, ask=150.02, mid=150.01,
            spread=0.02, timestamp=datetime.now(timezone.utc),
        ),
    )
    ctx.classifications["regime"] = ClassificationResult(
        name="regime", label=regime_label, confidence=1.0,
    )
    ctx.features["ema"] = FeatureResult(
        name="ema", values={"ema20": ema20, "ema50": ema50},
    )
    return ctx


def _cand(direction: TradeDirection, strategy: str) -> TradeCandidate:
    return TradeCandidate(
        symbol="USD_JPY", direction=direction, strategy=strategy,
        entry_price=150.0, stop_price=149.8, take_profit=150.4, score=55.0,
    )


def test_veto_cell_caution_trend_counter():
    """CAUTION × trend × counter — the primary VETO cell."""
    gate = RegimeCompatGate(mode=GateMode.OBSERVE)
    # EMA20 < EMA50 → dir_hint=short. Candidate=long → counter.
    ctx = _ctx("CAUTION", ema20=149.5, ema50=150.0)
    cand = _cand(TradeDirection.LONG, "dbb_trend")
    res = gate.safe_evaluate(cand, ctx)
    assert res.passed is True  # observe-only always passes
    assert res.metrics["recommendation"] == "would_veto"
    assert res.metrics["strategy_family"] == "trend"
    assert res.metrics["dir_vs_hint"] == "counter"


def test_boost_cell_caution_direct_aligned():
    """CAUTION × direct × aligned — the BOOST cell."""
    gate = RegimeCompatGate(mode=GateMode.OBSERVE)
    ctx = _ctx("CAUTION", ema20=150.5, ema50=150.0)  # dir_hint=long
    cand = _cand(TradeDirection.LONG, "direct")
    res = gate.safe_evaluate(cand, ctx)
    assert res.metrics["recommendation"] == "would_boost"
    assert res.metrics["dir_vs_hint"] == "aligned"


def test_penalize_cell_caution_direct_counter():
    gate = RegimeCompatGate(mode=GateMode.OBSERVE)
    ctx = _ctx("CAUTION", ema20=149.5, ema50=150.0)  # hint=short
    cand = _cand(TradeDirection.LONG, "direct")
    res = gate.safe_evaluate(cand, ctx)
    assert res.metrics["recommendation"] == "would_penalize"


def test_neutral_cell_normal_direct_aligned():
    """NORMAL × direct × aligned — matrix has no entry → neutral."""
    gate = RegimeCompatGate(mode=GateMode.OBSERVE)
    ctx = _ctx("NORMAL", ema20=150.5, ema50=150.0)
    cand = _cand(TradeDirection.LONG, "direct")
    res = gate.safe_evaluate(cand, ctx)
    assert res.metrics["recommendation"] == "neutral"


def test_reversal_family_mapping():
    gate = RegimeCompatGate(mode=GateMode.OBSERVE)
    ctx = _ctx("CAUTION", ema20=150.5, ema50=150.0)
    cand = _cand(TradeDirection.LONG, "reversal")
    res = gate.safe_evaluate(cand, ctx)
    assert res.metrics["strategy_family"] == "reversal"


def test_missing_inputs_never_blocks():
    gate = RegimeCompatGate(mode=GateMode.OBSERVE)
    ctx = SymbolContext(
        symbol="USD_JPY",
        snapshot=MarketSnapshot(
            symbol="USD_JPY", bid=150.0, ask=150.02, mid=150.01,
            spread=0.02, timestamp=datetime.now(timezone.utc),
        ),
    )
    cand = _cand(TradeDirection.LONG, "direct")
    res = gate.safe_evaluate(cand, ctx)
    assert res.passed is True
    assert res.metrics["recommendation"] == "unknown"


def test_always_passes_even_on_veto():
    """Observe-only guarantee: would_veto still passes the gate."""
    gate = RegimeCompatGate(mode=GateMode.OBSERVE)
    ctx = _ctx("CAUTION", ema20=149.5, ema50=150.0)
    cand = _cand(TradeDirection.LONG, "dbb_trend")
    res = gate.safe_evaluate(cand, ctx)
    assert res.passed is True
    assert res.mode == GateMode.OBSERVE
