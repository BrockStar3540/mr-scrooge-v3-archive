"""Regression test for the 2026-05-18 Sunday-open bleed.

The bleed root cause: `gates.entry_filter` was registered in OBSERVE mode
because the config block was `{"min_tier": "Pro"}` with no `mode` key.
The gate logged `[GATE:entry_filter] FAILED` on every candidate, but
`GatePipelineResult.all_passed` only flips False for HARD-mode failures,
so the scorer + executor kept running and orders fired.

These tests pin the load-bearing behavior:
  * HARD gate that fails  -> result.all_passed = False
  * OBSERVE gate that fails -> result.all_passed = True
  * mixed HARD+OBSERVE failures -> rejection_reason names the HARD gate
"""

from __future__ import annotations

from datetime import datetime, timezone

from scrooge_v3.core.types import (
    GateMode, GateResult, MarketSnapshot, SymbolContext,
    TradeCandidate, TradeDirection,
)
from scrooge_v3.gates.base import BaseGate
from scrooge_v3.gates.pipeline import GatePipeline


def _ctx(symbol: str = "EUR_USD") -> SymbolContext:
    snap = MarketSnapshot(
        symbol=symbol, bid=1.0849, ask=1.0851,
        mid=1.085, spread=0.00014,
        timestamp=datetime.now(timezone.utc),
    )
    return SymbolContext(symbol=symbol, snapshot=snap)


def _candidate(symbol: str = "EUR_USD") -> TradeCandidate:
    return TradeCandidate(
        symbol=symbol, direction=TradeDirection.LONG, strategy="direct",
        entry_price=1.085, stop_price=1.083, take_profit=1.090,
        risk_reward=2.5, score=35,
    )


class _StubGate(BaseGate):
    """Configurable gate that returns a preset result."""

    def __init__(self, name: str, passed: bool, reason: str, mode: GateMode):
        super().__init__(config={}, mode=mode)
        self.name = name
        self._passed = passed
        self._reason = reason

    def evaluate(self, candidate, ctx) -> GateResult:
        return GateResult(
            gate_name=self.name, passed=self._passed,
            mode=self.mode, reason=self._reason,
        )


class TestPipelineHardVetoEnforced:
    def test_hard_fail_blocks_pipeline(self):
        """A HARD-mode failure must flip all_passed to False."""
        gate = _StubGate("entry_filter", passed=False,
                         reason="no_routing_match_tier_gated", mode=GateMode.HARD)
        pipeline = GatePipeline([gate])
        result = pipeline.run(_candidate(), _ctx())
        assert not result.all_passed
        assert "entry_filter" in result.rejection_reason
        assert "no_routing_match_tier_gated" in result.rejection_reason

    def test_observe_fail_does_not_block(self):
        """An OBSERVE-mode failure must NOT flip all_passed — this is the
        2026-05-18 bleed mechanism. The "FAILED" log line is intentional
        telemetry; only HARD failures should stop a trade."""
        gate = _StubGate("entry_filter", passed=False,
                         reason="below_min_tier:Standard_rank1<2",
                         mode=GateMode.OBSERVE)
        pipeline = GatePipeline([gate])
        result = pipeline.run(_candidate(), _ctx())
        assert result.all_passed
        assert result.rejection_reason == ""

    def test_hard_pass_allows_pipeline(self):
        gate = _StubGate("entry_filter", passed=True,
                         reason="shave_rule_satisfied", mode=GateMode.HARD)
        pipeline = GatePipeline([gate])
        result = pipeline.run(_candidate(), _ctx())
        assert result.all_passed

    def test_observe_fail_then_hard_fail_names_hard_gate(self):
        """When both an OBSERVE and a HARD gate fail, the rejection_reason
        must name the first HARD failure — the OBSERVE one is just noise."""
        observe = _StubGate("sub_regime_filter", passed=False,
                            reason="sub_regime_unmatched:C01",
                            mode=GateMode.OBSERVE)
        hard = _StubGate("entry_filter", passed=False,
                         reason="below_min_tier:Probationary_rank0<2",
                         mode=GateMode.HARD)
        pipeline = GatePipeline([observe, hard])
        result = pipeline.run(_candidate(), _ctx())
        assert not result.all_passed
        assert "entry_filter" in result.rejection_reason
        assert "sub_regime_filter" not in result.rejection_reason

    def test_pipeline_decision_log_present(self, caplog):
        """The [PIPELINE] BLOCKED / APPROVED log line is the operator's
        canonical signal that the pipeline as a whole stopped a trade.
        Without it, the 2026-05-18 bleed presented as per-gate FAILED lines
        with no aggregate marker — and orders kept firing."""
        import logging
        with caplog.at_level(logging.INFO, logger="scrooge_v3.gate.pipeline"):
            hard = _StubGate("entry_filter", passed=False,
                             reason="no_routing_match_tier_gated",
                             mode=GateMode.HARD)
            GatePipeline([hard]).run(_candidate(), _ctx())
        messages = [r.getMessage() for r in caplog.records]
        assert any("[PIPELINE] BLOCKED" in m for m in messages), messages

        caplog.clear()
        with caplog.at_level(logging.INFO, logger="scrooge_v3.gate.pipeline"):
            ok = _StubGate("entry_filter", passed=True,
                           reason="shave_rule_satisfied", mode=GateMode.HARD)
            GatePipeline([ok]).run(_candidate(), _ctx())
        messages = [r.getMessage() for r in caplog.records]
        assert any("[PIPELINE] APPROVED" in m for m in messages), messages
