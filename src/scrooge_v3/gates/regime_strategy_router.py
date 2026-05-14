"""Regime → strategy router gate.

Implements Brock's 2026-05-14 architecture:

  - Regime is the FIRST gate, not the LAST filter.
  - Each (regime × strategy_family × dir_vs_hint) cell either has an attached
    strategy or it doesn't.
  - Attached → allow. Not attached → VETO (do not trade).
  - Adding a new strategy = adding an allow-list entry in config. Modular.

Initial allow-list (evidence-based; conservative):

  NORMAL  × reversal  × aligned   ALLOW  mean reversion in clean market
  NORMAL  × reversal  × counter   ALLOW  classic counter-trend reversal
  NORMAL  × dbb_trend × aligned   ALLOW  DBB trend continuation
  NORMAL  × direct    × aligned   ALLOW  direct entry with the prevailing trend
  CAUTION × reversal  × aligned   ALLOW  mean reversion still works in caution
  CAUTION × reversal  × counter   ALLOW  counter-trend reversal in caution
  CAUTION × direct    × aligned   ALLOW  +1.08R historic (regime_compat matrix)

Everything else: VETO. Documented loser cells (e.g. CAUTION × trend × counter
at -0.78R) are vetoed by being absent from the allow-list.

When new strategies arrive (from the seed factory, from research), they plug
in by adding their (regime, family, dir) cell to the allow-list. No code
change required.

Override via config.gates.regime_strategy_router:
  enabled: true|false           (default true)
  mode: "hard" | "observe"      (default hard)
  allow_list: list of "REGIME × family × dir_vs_hint" strings
"""

from __future__ import annotations

from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


DEFAULT_ALLOW_LIST = {
    ("NORMAL",  "reversal",  "aligned"),
    ("NORMAL",  "reversal",  "counter"),
    ("NORMAL",  "dbb_trend", "aligned"),
    ("NORMAL",  "direct",    "aligned"),
    ("CAUTION", "reversal",  "aligned"),
    ("CAUTION", "reversal",  "counter"),
    ("CAUTION", "direct",    "aligned"),
}

# Documented winners + losers from existing regime_compat matrix. For audit
# annotation; not behavioral.
_BASIS_NOTES = {
    ("CAUTION", "direct", "aligned"):
        "regime_compat matrix: n=165 win=0.61 meanR=+1.08",
    ("CAUTION", "trend", "counter"):
        "regime_compat matrix: n=215 win=0.07 meanR=-0.78 — DENIED",
    ("CAUTION", "direct", "counter"):
        "regime_compat matrix: n=455 win=0.17 meanR=-0.31 — DENIED",
    ("NORMAL", "trend", "aligned"):
        "regime_compat matrix: n=24 win=0.21 meanR=-0.46 (thin) — currently DENIED",
}


def _family(strategy: str) -> str:
    if strategy in ("dbb_trend", "trend"):
        return "trend" if strategy == "trend" else "dbb_trend"
    if strategy == "reversal":
        return "reversal"
    return "direct"


def _parse_allow_list(items: list[str]) -> set[tuple[str, str, str]]:
    """Parse 'REGIME × family × dir' strings to tuples. Tolerates * × and x."""
    out = set()
    if not items:
        return out
    for it in items:
        parts = [p.strip() for p in it.replace("×", "x").split("x")]
        if len(parts) == 3:
            out.add((parts[0].upper(), parts[1].lower(), parts[2].lower()))
    return out


class RegimeStrategyRouterGate(BaseGate):
    """Allow-list gate routing regime → strategy."""

    name = "regime_strategy_router"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)
        cfg = config or {}
        # config.allow_list overrides DEFAULT_ALLOW_LIST when provided
        list_strs = cfg.get("allow_list") or []
        parsed = _parse_allow_list(list_strs)
        self._allow: set[tuple[str, str, str]] = parsed if parsed else set(DEFAULT_ALLOW_LIST)

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        reg = ctx.classifications.get("regime")
        ema = ctx.features.get("ema")

        # If we don't know the regime or direction context, fail OPEN: pass with
        # a flag so we don't accidentally block valid trades. Real-life live
        # trading should pretty much always have these populated.
        if reg is None or ema is None:
            return GateResult(
                gate_name=self.name, passed=True,
                reason="insufficient inputs (regime or ema missing) — pass-through",
                metrics={"decision": "pass_through_missing_inputs"},
            )

        regime_label = str(getattr(reg, "label", "") or "").upper()
        ema_vals = getattr(ema, "values", {}) or {}
        ema20 = ema_vals.get("ema20")
        ema50 = ema_vals.get("ema50")
        if ema20 is None or ema50 is None:
            return GateResult(
                gate_name=self.name, passed=True,
                reason="ema values unavailable — pass-through",
                metrics={"decision": "pass_through_missing_ema"},
            )

        dir_hint = "long" if ema20 > ema50 else "short"
        cand_dir = candidate.direction.value
        dir_vs_hint = "aligned" if cand_dir == dir_hint else "counter"
        family = _family(candidate.strategy)

        key = (regime_label, family, dir_vs_hint)
        allowed = key in self._allow
        basis = _BASIS_NOTES.get(key, "")

        passed = allowed if self.mode == GateMode.HARD else True
        if allowed:
            reason = f"{regime_label} × {family} × {dir_vs_hint}: ALLOW (in allow-list)"
        else:
            reason = (
                f"{regime_label} × {family} × {dir_vs_hint}: VETO "
                f"(no strategy attached to this regime cell)"
            )

        return GateResult(
            gate_name=self.name,
            passed=passed,
            reason=reason,
            metrics={
                "regime_label": regime_label,
                "strategy_family": family,
                "direction": cand_dir,
                "direction_hint": dir_hint,
                "dir_vs_hint": dir_vs_hint,
                "in_allow_list": allowed,
                "allow_list_size": len(self._allow),
                "matrix_basis": basis,
                "mode": self.mode.value if hasattr(self.mode, "value") else str(self.mode),
            },
        )
