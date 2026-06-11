"""Gate pipeline -- ordered gate runner."""

from __future__ import annotations

import logging
from typing import Any

from scrooge_v3.core.types import (
    GateMode,
    GateResult,
    HealthColor,
    SymbolContext,
    TradeCandidate,
)

from .base import BaseGate, GatePipelineResult


logger = logging.getLogger("scrooge_v3.gate.pipeline")


class GatePipeline:
    """Ordered gate runner.

    Iterates registered gates in order, handling disabled / observe /
    hard / soft modes per gate.  A crashed or missing gate is marked
    gray and does not block the pipeline.

    Returns a ``GatePipelineResult`` with all individual gate results.
    """

    def __init__(self, gates: list[BaseGate] | None = None) -> None:
        self._gates: list[BaseGate] = list(gates) if gates else []

    # -- Registration -------------------------------------------------------

    def register(self, gate: BaseGate) -> None:
        """Append a gate to the pipeline.

        Recommended gate order:
          1. spread
          2. otr (overhead_ratio)
          3. rr (risk_reward)
          4. nat_stop_validity  -- TODO: add gate (blocks if natural stop is invalid/missing)
          5. spread_vs_stop     -- TODO: add gate (blocks if spread >= natural stop distance)
          6. exhaustion_filter
          7. debounce
          8. cap
          9. regime_floor
        """
        self._gates.append(gate)

    def register_many(self, gates: list[BaseGate]) -> None:
        """Append multiple gates in order."""
        self._gates.extend(gates)

    @property
    def gates(self) -> list[BaseGate]:
        return list(self._gates)

    # -- Execution ----------------------------------------------------------

    def run(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GatePipelineResult:
        """Evaluate all gates in order.

        * **HARD** gate fails -> marks pipeline as failed, continues
          evaluating remaining gates for observability.
        * **SOFT** gate fails -> recorded but does not block.
        * **OBSERVE** gate -> always recorded, never blocks.
        * Crashed gate -> logged as gray, does not block.
        """
        result = GatePipelineResult(symbol=candidate.symbol)

        for gate in self._gates:
            gate_result = self._run_one(gate, candidate, ctx)
            result.append(gate_result)

            # Emit structured log for every gate
            status = "PASSED" if gate_result.passed else "FAILED"
            logger.info(
                "[GATE:%s] %s symbol=%s reason=%s",
                gate_result.gate_name,
                status,
                candidate.symbol,
                gate_result.reason,
            )

        # Aggregate decision — load-bearing for execution control. Before this
        # log existed, an OBSERVE-mode "FAILED" was indistinguishable from a
        # real HARD veto, and the 2026-05-18 bleed went unnoticed until orders
        # placed. Now any caller (or operator tailing logs) can see whether the
        # pipeline as a whole APPROVED or BLOCKED the candidate.
        if result.all_passed:
            logger.info(
                "[PIPELINE] APPROVED symbol=%s strategy=%s direction=%s",
                candidate.symbol, candidate.strategy,
                candidate.direction.value if hasattr(candidate.direction, "value") else candidate.direction,
            )
        else:
            logger.info(
                "[PIPELINE] BLOCKED symbol=%s rejection=%s",
                candidate.symbol, result.rejection_reason,
            )

        self._ledger(candidate, ctx, result)
        return result

    def _run_one(
        self, gate: BaseGate, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        """Run a single gate with crash protection."""
        try:
            return gate.safe_evaluate(candidate, ctx)
        except Exception as exc:
            # This should not happen (safe_evaluate catches exceptions)
            # but we defend against truly catastrophic failures.
            reason = f"Gate crashed: {exc}"
            logger.exception(
                "[GATE:%s] CRASHED symbol=%s error=%s",
                gate.name, candidate.symbol, exc,
            )
            return GateResult(
                gate_name=gate.name,
                passed=False,
                mode=GateMode.OBSERVE,  # Crashed gates don't block
                reason=reason,
                metrics={"crashed": True},
            )

    # -- Candidate ledger (Brock 2026-06-10) ---------------------------------
    # Append EVERY evaluated candidate (approved or refused) to
    # data/candidate-ledger.jsonl: the live counterfactual stream. The bot
    # previously only recorded picks; refusals are the training signal the
    # lab needs (forward-labeled daily on the Mini). Must never raise.
    def _ledger(self, candidate, ctx, result) -> None:
        try:
            import json as _json
            from datetime import datetime as _dt, timezone as _tz
            meta = getattr(candidate, "metadata", None) or {}
            sig = meta.get("exit_sig") or {}
            pw = None
            try:
                from scrooge_v3.advisors import lightgbm_shadow as _lgs
                pw = _lgs.predict_p_win(candidate.symbol, ctx, candidate)
            except Exception:
                pass
            rec = {
                "ts": _dt.now(_tz.utc).isoformat(timespec="seconds"),
                "symbol": candidate.symbol,
                "strategy": getattr(candidate, "strategy", ""),
                "direction": getattr(getattr(candidate, "direction", None), "value", ""),
                "entry": getattr(candidate, "entry_price", None),
                "stop": getattr(candidate, "stop_price", None),
                "align": meta.get("align_score"),
                "cell_hits": meta.get("cell_hits"),
                "buckets": {k: sig.get(k) for k in ("BB","BBP","A5","A1","RSI","E20","E50","ZS","SPR","ADR","H20","H60","T1","T4")} if sig else None,
                "session": sig.get("session") if sig else None,
                "p_win": round(pw, 4) if isinstance(pw, float) else None,
                "passed": bool(result.all_passed),
                "rejection": result.rejection_reason or None,
            }
            with open("data/candidate-ledger.jsonl", "a") as f:
                f.write(_json.dumps(rec) + "\n")
        except Exception:
            logger.debug("[LEDGER] write failed", exc_info=True)
