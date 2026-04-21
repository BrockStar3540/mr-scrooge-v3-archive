"""Regime compatibility gate (observe-only).

Classifies each candidate into a (regime_label × strategy_family × dir_vs_hint)
cell and attaches the historically-fit recommendation (veto / boost / penalize /
neutral) without blocking the trade. One week of live log data informs promotion
to an active gate.

Matrix fit from 6 regime windows, 1,918 trades. See
`Oanda-Bot-Trainer/data/replay/compat_summary.md` for derivation.

Recommendations (observe-only):
  CAUTION × trend  × counter  → WOULD_VETO     (n=215, 7% win, -0.78R, 92% SL)
  CAUTION × direct × aligned  → WOULD_BOOST    (n=165, 61% win, +1.08R)
  CAUTION × direct × counter  → WOULD_PENALIZE (n=455, 17% win, -0.31R)
  NORMAL  × trend  × aligned  → WOULD_PENALIZE (n=24,  21% win, -0.46R; thin sample)

All other cells: NEUTRAL. Direction hint is sign(ema20 - ema50).
"""

from __future__ import annotations

from typing import Any

from scrooge_v3.core.types import (
    GateMode,
    GateResult,
    SymbolContext,
    TradeCandidate,
)

from .base import BaseGate


_MATRIX: dict[tuple[str, str, str], tuple[str, str]] = {
    ("CAUTION", "trend",  "counter"): ("would_veto",     "n=215 win=0.07 meanR=-0.78 SL=0.92 across 6 windows"),
    ("CAUTION", "direct", "aligned"): ("would_boost",    "n=165 win=0.61 meanR=+1.08"),
    ("CAUTION", "direct", "counter"): ("would_penalize", "n=455 win=0.17 meanR=-0.31"),
    ("NORMAL",  "trend",  "aligned"): ("would_penalize", "n=24  win=0.21 meanR=-0.46 (thin)"),
}


def _family(strategy: str) -> str:
    if strategy in ("dbb_trend", "trend"):
        return "trend"
    if strategy == "reversal":
        return "reversal"
    return "direct"


class RegimeCompatGate(BaseGate):
    """Observe-only compat classifier. Always passes — logs recommendation only."""

    name = "regime_compat"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.OBSERVE,
    ) -> None:
        super().__init__(config, mode)

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        reg = ctx.classifications.get("regime")
        ema = ctx.features.get("ema")

        if reg is None or ema is None:
            return GateResult(
                gate_name=self.name, passed=True,
                reason="insufficient inputs (regime or ema missing)",
                metrics={"recommendation": "unknown", "reason_code": "missing_inputs"},
            )

        regime_label = str(getattr(reg, "label", "") or "").upper()
        ema_vals = getattr(ema, "values", {}) or {}
        ema20 = ema_vals.get("ema20")
        ema50 = ema_vals.get("ema50")
        if ema20 is None or ema50 is None:
            return GateResult(
                gate_name=self.name, passed=True,
                reason="ema values unavailable",
                metrics={"recommendation": "unknown", "reason_code": "missing_ema"},
            )

        dir_hint = "long" if ema20 > ema50 else "short"
        cand_dir = candidate.direction.value
        dir_vs_hint = "aligned" if cand_dir == dir_hint else "counter"
        family = _family(candidate.strategy)

        key = (regime_label, family, dir_vs_hint)
        rec, detail = _MATRIX.get(key, ("neutral", "no matrix entry"))

        return GateResult(
            gate_name=self.name,
            passed=True,  # observe-only: always passes
            reason=f"{regime_label} × {family} × {dir_vs_hint} → {rec}",
            metrics={
                "regime_label": regime_label,
                "strategy_family": family,
                "direction": cand_dir,
                "direction_hint": dir_hint,
                "dir_vs_hint": dir_vs_hint,
                "ema20": float(ema20),
                "ema50": float(ema50),
                "recommendation": rec,
                "matrix_detail": detail,
                "pre_compat_score": float(candidate.score),
                "score": 1.0,
            },
        )
