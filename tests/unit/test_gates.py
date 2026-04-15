"""Unit tests for gate modules — verify pass/fail logic with fake context."""

from scrooge_v3.core.types import (
    GateMode, GateResult, MarketSnapshot, SymbolContext,
    TradeCandidate, TradeDirection,
)
from datetime import datetime, timezone


def _ctx(symbol="EUR_USD", mid=1.085, spread=0.00014, **metadata):
    snap = MarketSnapshot(
        symbol=symbol, bid=mid - spread / 2, ask=mid + spread / 2,
        mid=mid, spread=spread, timestamp=datetime.now(timezone.utc),
    )
    return SymbolContext(symbol=symbol, snapshot=snap, metadata=metadata)


def _candidate(symbol="EUR_USD", direction="short", rr=1.5, strategy="reversal",
               entry=1.085, sl=1.087, tp=1.080, score=35):
    return TradeCandidate(
        symbol=symbol, direction=TradeDirection(direction), strategy=strategy,
        entry_price=entry, stop_price=sl, take_profit=tp,
        risk_reward=rr, score=score,
    )


# =====================================================================
# Spread Gate
# =====================================================================

class TestSpreadGate:
    def test_passes_within_threshold(self):
        from scrooge_v3.gates.spread import SpreadGate
        gate = SpreadGate()
        ctx = _ctx(spread=0.00012)
        result = gate.evaluate(_candidate(), ctx)
        assert result.passed

    def test_fails_above_threshold(self):
        from scrooge_v3.gates.spread import SpreadGate
        gate = SpreadGate({"max_spread_default": 2.0})
        ctx = _ctx(spread=3.0)
        result = gate.evaluate(_candidate(), ctx)
        assert not result.passed

    def test_jpy_uses_wider_threshold(self):
        from scrooge_v3.gates.spread import SpreadGate
        gate = SpreadGate({"max_spread_jpy": 5.0})
        ctx = _ctx(symbol="USD_JPY", mid=150.0, spread=4.0)
        result = gate.evaluate(_candidate(symbol="USD_JPY"), ctx)
        assert result.passed

    def test_fails_spread_pct_of_half(self):
        from scrooge_v3.gates.spread import SpreadGate
        gate = SpreadGate({"spread_pct_of_half": 0.10})
        ctx = _ctx(spread=0.0015, range_half=0.010)
        result = gate.evaluate(_candidate(), ctx)
        assert not result.passed  # 15% > 10%

    def test_fails_spread_exceeds_natural_stop(self):
        from scrooge_v3.gates.spread import SpreadGate
        gate = SpreadGate()
        ctx = _ctx(spread=0.0006, natural_stop_pips=0.0005)
        result = gate.evaluate(_candidate(), ctx)
        assert not result.passed


# =====================================================================
# Overhead Ratio Gate (OTR Inverted)
# =====================================================================

class TestOverheadRatioGate:
    def test_sweet_spot_passes(self):
        """OTR 8-18% = sweet spot (63-68% WR)."""
        from scrooge_v3.gates.overhead_ratio import OverheadRatioGate
        gate = OverheadRatioGate()
        ctx = _ctx(total_overhead=0.001, range_half=0.008)  # OTR = 12.5%
        result = gate.evaluate(_candidate(), ctx)
        assert result.passed
        assert result.metrics.get("otr_category") == "sweet_spot"

    def test_too_low_otr_fails(self):
        """OTR < 8% = wide unfocused box, 17% WR."""
        from scrooge_v3.gates.overhead_ratio import OverheadRatioGate
        gate = OverheadRatioGate()
        ctx = _ctx(total_overhead=0.0003, range_half=0.01)  # OTR = 3%
        result = gate.evaluate(_candidate(), ctx)
        assert not result.passed
        assert result.metrics.get("otr_category") == "too_low"

    def test_zero_range_fails(self):
        from scrooge_v3.gates.overhead_ratio import OverheadRatioGate
        gate = OverheadRatioGate()
        ctx = _ctx(total_overhead=0.001, range_half=0.0)
        result = gate.evaluate(_candidate(), ctx)
        assert not result.passed


# =====================================================================
# Risk Reward Gate
# =====================================================================

class TestRiskRewardGate:
    def test_passes_above_min(self):
        from scrooge_v3.gates.risk_reward import RiskRewardGate
        gate = RiskRewardGate({"reversal_min_rr": 1.0})
        result = gate.evaluate(_candidate(rr=1.5), _ctx())
        assert result.passed

    def test_fails_below_min(self):
        from scrooge_v3.gates.risk_reward import RiskRewardGate
        gate = RiskRewardGate({"reversal_min_rr": 1.0})
        result = gate.evaluate(_candidate(rr=0.8), _ctx())
        assert not result.passed

    def test_trend_uses_trend_min(self):
        from scrooge_v3.gates.risk_reward import RiskRewardGate
        gate = RiskRewardGate({"trend_min_rr": 1.0, "reversal_min_rr": 2.0})
        cand = _candidate(strategy="trend_full", rr=1.2)
        result = gate.evaluate(cand, _ctx())
        assert result.passed


# =====================================================================
# Exhaustion Filter Gate
# =====================================================================

class TestExhaustionFilterGate:
    def test_stretch_up_hard_blocked(self):
        from scrooge_v3.gates.exhaustion_filter import ExhaustionFilterGate
        from scrooge_v3.core.types import ClassificationResult
        gate = ExhaustionFilterGate()
        ctx = _ctx()
        ctx.classifications["bollinger_band"] = ClassificationResult(
            name="bollinger_band", label="STRETCH_UP")
        result = gate.evaluate(_candidate(), ctx)
        assert not result.passed

    def test_trend_bypasses(self):
        from scrooge_v3.gates.exhaustion_filter import ExhaustionFilterGate
        gate = ExhaustionFilterGate()
        cand = _candidate(strategy="trend_full")
        result = gate.evaluate(cand, _ctx())
        assert result.passed


# =====================================================================
# Regime Floor Gate
# =====================================================================

class TestRegimeFloorGate:
    def test_passes_above_min_score(self):
        from scrooge_v3.gates.regime_floor import RegimeFloorGate
        from scrooge_v3.core.types import ClassificationResult
        gate = RegimeFloorGate({"min_score": -1})
        ctx = _ctx()
        ctx.classifications["regime"] = ClassificationResult(
            name="regime", label="NORMAL", metadata={"score": 0})
        result = gate.evaluate(_candidate(), ctx)
        assert result.passed

    def test_fails_below_min_score(self):
        from scrooge_v3.gates.regime_floor import RegimeFloorGate
        from scrooge_v3.core.types import ClassificationResult
        gate = RegimeFloorGate({"min_score": -1})
        ctx = _ctx()
        ctx.classifications["regime"] = ClassificationResult(
            name="regime", label="BLOCKED", metadata={"score": -5})
        result = gate.evaluate(_candidate(), ctx)
        assert not result.passed


# =====================================================================
# Stop Planner
# =====================================================================

class TestStopPlanner:
    def test_trigger_side_short_validation(self):
        """Short SL must be above ASK + buffer."""
        from scrooge_v3.execution.stop_planner import StopPlanner
        planner = StopPlanner()
        adjusted, reason = planner.validate_stop(
            TradeDirection.SHORT,
            proposed_stop=1.08510,
            bid=1.08500, ask=1.08514,
            spread=0.00014,
        )
        # Proposed is below ask, should be adjusted up
        assert adjusted > 1.08514

    def test_trigger_side_long_validation(self):
        """Long SL must be below BID - buffer."""
        from scrooge_v3.execution.stop_planner import StopPlanner
        planner = StopPlanner()
        adjusted, reason = planner.validate_stop(
            TradeDirection.LONG,
            proposed_stop=1.08499,
            bid=1.08500, ask=1.08514,
            spread=0.00014,
        )
        assert adjusted < 1.08500

    def test_valid_stop_passes(self):
        from scrooge_v3.execution.stop_planner import StopPlanner
        planner = StopPlanner()
        adjusted, reason = planner.validate_stop(
            TradeDirection.SHORT,
            proposed_stop=1.09000,
            bid=1.08500, ask=1.08514,
            spread=0.00014,
        )
        assert reason == "valid"
        assert adjusted == 1.09000

    def test_hostile_spread_blocks_trail(self):
        from scrooge_v3.execution.stop_planner import StopPlanner
        planner = StopPlanner({"fast_market_multiplier": 2.5})
        ok, reason = planner.should_trail(
            TradeDirection.LONG,
            current_stop=1.08400, new_stop=1.08450,
            spread=0.0010, mean_spread=0.00014,
        )
        assert not ok
        assert "hostile_spread" in reason
