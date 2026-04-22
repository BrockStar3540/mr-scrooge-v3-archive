"""Unit tests for BoxV3ShadowGate (observe-only)."""
from datetime import datetime, timezone
from scrooge_v3.core.types import (
    ClassificationResult, FeatureResult, GateMode, MarketSnapshot,
    SymbolContext, TradeCandidate, TradeDirection,
)
from scrooge_v3.gates.box_v3_shadow import BoxV3ShadowGate


def _ctx(*, wall=0.35, box_age=4.0, bb_pos=0.85, ema20=15.0, ema50=40.0,
         volume_ratio=0.75, adr=1.30, opening="NORMAL_OPEN"):
    ctx = SymbolContext(
        symbol="USD_CHF",
        snapshot=MarketSnapshot(
            symbol="USD_CHF", bid=0.85, ask=0.8502, mid=0.8501,
            spread=0.0002, timestamp=datetime.now(timezone.utc),
        ),
    )
    ctx.features["zone_detector"] = FeatureResult(
        name="zone_detector",
        values={"wall_proximity": wall, "box_age_hours": box_age},
    )
    ctx.features["ema"] = FeatureResult(
        name="ema",
        values={"ema20_dist_pct": ema20, "ema50_dist_pct": ema50,
                "ema20": 0.85, "ema50": 0.84},
    )
    ctx.features["volume"] = FeatureResult(
        name="volume",
        values={"volume_ratio": volume_ratio, "current_volume": 1000, "avg_volume": 1333},
    )
    ctx.features["bollinger"] = FeatureResult(
        name="bollinger", values={"bb_position": bb_pos},
    )
    ctx.features["atr"] = FeatureResult(
        name="atr", values={"adr_consumed": adr},
    )
    ctx.classifications["opening_state"] = ClassificationResult(
        name="opening_state", label=opening, confidence=1.0,
    )
    return ctx


def _cand(direction=TradeDirection.SHORT, strategy="direct",
          entry=0.8510, stop=0.8530):
    return TradeCandidate(
        symbol="USD_CHF", direction=direction, strategy=strategy,
        entry_price=entry, stop_price=stop, take_profit=0.8480, score=55.0,
    )


def test_not_box_branch_noop():
    """Trend strategy → gate marks not_box_branch, always passes."""
    gate = BoxV3ShadowGate(mode=GateMode.OBSERVE)
    ctx = _ctx()
    cand = _cand(strategy="dbb_trend")
    r = gate.safe_evaluate(cand, ctx)
    assert r.passed is True
    assert r.metrics["applicable"] is False


def test_observe_passes_on_reject():
    """All-good box setup except fails wall strict → logs would_reject, passes."""
    gate = BoxV3ShadowGate(mode=GateMode.OBSERVE)
    # wall=0.25 passes LOOSE (>=0.20) but fails A1 (>=0.30)
    ctx = _ctx(wall=0.25)
    cand = _cand()  # stop 20 pips (above 15 floor)
    r = gate.safe_evaluate(cand, ctx)
    assert r.passed is True  # always passes in observe mode
    assert r.metrics["would_allow"] is False
    assert r.metrics["failed_gate"] == "A1_wall_strict"


def test_clean_box_setup_would_allow():
    """Clean box setup passes all gates; would_allow=True."""
    gate = BoxV3ShadowGate(mode=GateMode.OBSERVE)
    ctx = _ctx(wall=0.35, bb_pos=0.85, ema20=15.0, volume_ratio=0.75, adr=1.30)
    # stop = |0.8510 - 0.8530| = 0.002 = 20 pips (passes >=15)
    cand = _cand(entry=0.8510, stop=0.8530)
    r = gate.safe_evaluate(cand, ctx)
    assert r.passed is True
    assert r.metrics["would_allow"] is True
    assert r.metrics["failed_gate"] is None


def test_a_tier_scoring():
    """adr_consumed >= 1.25 (+3), wall 0.30-0.50 (+2), vol 0.60-0.90 (+1) = 6 = A-tier."""
    gate = BoxV3ShadowGate(mode=GateMode.OBSERVE)
    ctx = _ctx(wall=0.40, bb_pos=0.85, ema20=15.0, volume_ratio=0.75, adr=1.50)
    cand = _cand(entry=0.8510, stop=0.8540)  # 30 pips → +1 stop wide
    r = gate.safe_evaluate(cand, ctx)
    assert r.metrics["tier"] == "A"
    assert r.metrics["ranking_score"] >= 5


def test_b_tier_scoring():
    """Some points, below A threshold → B-tier."""
    gate = BoxV3ShadowGate(mode=GateMode.OBSERVE)
    ctx = _ctx(wall=0.35, bb_pos=0.85, ema20=15.0, volume_ratio=1.10, adr=0.80)
    # wall +2, volume outside sweet zone, no adr boost → 2 = B
    cand = _cand(entry=0.8510, stop=0.8530)  # 20 pips, no >=25 boost
    r = gate.safe_evaluate(cand, ctx)
    assert r.metrics["tier"] == "B"


def test_stop_min_fail():
    """Stop < 15 pips → C1 fails."""
    gate = BoxV3ShadowGate(mode=GateMode.OBSERVE)
    ctx = _ctx()
    cand = _cand(entry=0.8510, stop=0.8520)  # 10 pips
    r = gate.safe_evaluate(cand, ctx)
    assert r.metrics["would_allow"] is False
    assert r.metrics["failed_gate"] == "C1_min_stop"


def test_ema20_dead_zone_fail():
    """ema20 in [18,40] dead zone → A2 fails."""
    gate = BoxV3ShadowGate(mode=GateMode.OBSERVE)
    ctx = _ctx(ema20=25.0)
    cand = _cand(entry=0.8510, stop=0.8530)
    r = gate.safe_evaluate(cand, ctx)
    assert r.metrics["would_allow"] is False
    assert r.metrics["failed_gate"] == "A2_ema20_not_dead"


def test_expansion_volume_fail():
    """volume_ratio >= 1.50 → A3 fails."""
    gate = BoxV3ShadowGate(mode=GateMode.OBSERVE)
    ctx = _ctx(volume_ratio=1.60)
    cand = _cand(entry=0.8510, stop=0.8530)
    r = gate.safe_evaluate(cand, ctx)
    assert r.metrics["would_allow"] is False
    assert r.metrics["failed_gate"] == "A3_not_expansion"


def test_short_gap_down_boost():
    """Short + GAP_DOWN opening → +1 ranking point."""
    gate = BoxV3ShadowGate(mode=GateMode.OBSERVE)
    ctx_gap = _ctx(opening="GAP_DOWN")
    ctx_normal = _ctx(opening="NORMAL_OPEN")
    cand = _cand(direction=TradeDirection.SHORT, entry=0.8510, stop=0.8530)
    r_gap = gate.safe_evaluate(cand, ctx_gap)
    r_normal = gate.safe_evaluate(cand, ctx_normal)
    assert r_gap.metrics["ranking_score"] == r_normal.metrics["ranking_score"] + 1


def test_missing_inputs_never_blocks():
    """Missing features → gates marked skipped, gate still passes."""
    gate = BoxV3ShadowGate(mode=GateMode.OBSERVE)
    ctx = SymbolContext(
        symbol="USD_CHF",
        snapshot=MarketSnapshot(symbol="USD_CHF", bid=0.85, ask=0.85, mid=0.85,
                                 spread=0.0, timestamp=datetime.now(timezone.utc)),
    )
    cand = _cand()
    r = gate.safe_evaluate(cand, ctx)
    assert r.passed is True  # always passes
    # Most gates should be 'skipped' due to missing features
