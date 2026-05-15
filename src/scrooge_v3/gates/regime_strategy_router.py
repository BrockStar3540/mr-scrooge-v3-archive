"""Regime → strategy router gate (v3: LABEL-ONLY per Phase D, 2026-05-14).

Phase D (2026-05-14): Gate stops vetoing. Always passes. The routing table
at the leaf (data/routing_table_v*.parquet) is now the only enforcer. This
gate is retained for audit-trail continuity — it still emits the labels
and metrics that downstream telemetry expects, so dashboards/logs do not
break — but it does not kill trades anymore.

Rationale (ungated 26-pair replay 2026-05-14): per-trade economics are
identical in dead vs alive regimes (both −0.028 mean R). 8 (probe × regime)
winning cells totaling +366R live inside the "dead" regimes the previous
v2 gate vetoed. The veto layer was throwing winners out with losers.

v2 (2026-05-14, superseded): 53-cell allow-list veto.

Implements Brock's 2026-05-14 architecture:

  - Regime is the FIRST gate, not the LAST filter.
  - Each (regime × strategy_family × dir_vs_hint) cell either has an attached
    strategy or it doesn't.
  - Attached → allow. Not attached → VETO (do not trade).
  - Adding a new strategy = adding an allow-list entry in config. Modular.

v2 (2026-05-14): The router prefers `technical_regime_53` (bar-true 53-cell
classification) when the feature is available. The 53-cell allow-list is
derived from:
  - Moving-regime seed factory evidence (last 6mo, 6,779 winners across 92
    (strategy × regime) parent cells in non-dead regimes).
  - Dead regimes (R04 tight_range, T07 directional_drift_flat, Z01 catch_all):
    full VETO — R-math doesn't work, 96% of textbook fires land here as
    losers.
  - Trend regimes (T01-T06, B01-B08, X01,X02,X04): dbb_trend aligned + direct
    aligned. Extended trends (T01, T03) also open reversal counter (mean
    reversion at extreme).
  - Range/coil regimes (R01-R03, C01-C04): reversal both directions.
  - Overbought/oversold (O01-O06): reversal both directions (counter is the
    main play — mean reversion at extremes).
  - Stop-hunts / false-breaks (M01-M04, F01-F04): reversal both directions.
  - Sessions: S03/S06 (active) trade-permissive; S01/S05 (quiet) VETO.
  - Flat expansion (X03) and Z01 catch_all: VETO.

If `technical_regime_53` is missing for a tick (e.g. early bar warmup),
the gate falls back to the original binary NORMAL/CAUTION allow-list so
trading is not blocked by a missing feature.

Override via config.gates.regime_strategy_router:
  enabled: true|false              (default true)
  mode: "hard" | "observe"         (default hard)
  allow_list: list of "REGIME × family × dir_vs_hint" strings
                                   (overrides binary defaults)
  allow_list_53: list of strings   (overrides 53-cell defaults)
  prefer_regime_53: true|false     (default true)
"""

from __future__ import annotations

from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


# --- Binary fallback allow-list (NORMAL/CAUTION × family × dir) -----------

DEFAULT_ALLOW_LIST = {
    ("NORMAL",  "reversal",  "aligned"),
    ("NORMAL",  "reversal",  "counter"),
    ("NORMAL",  "dbb_trend", "aligned"),
    ("NORMAL",  "direct",    "aligned"),
    ("CAUTION", "reversal",  "aligned"),
    ("CAUTION", "reversal",  "counter"),
    ("CAUTION", "direct",    "aligned"),
}

# --- 53-regime allow-list -------------------------------------------------
# Encoded as set of (regime53_code, family, dir_vs_hint).
# Built from evidence: last 6mo / 47K textbook + 7K probe / 6,779 moving
# winners spread across O04-O06, T03/T05/T06, plus trend / range / breakout
# heuristics for cells we have less direct evidence on.

def _build_regime53_allow_list() -> set[tuple[str, str, str]]:
    out: set[tuple[str, str, str]] = set()

    # Trending regimes — DBB trend + direct go with the trend
    # Extended (T01, T03): open reversal counter for mean-reversion at extremes
    for code in ("T01", "T02", "T05"):  # uptrends
        out.add((code, "dbb_trend", "aligned"))
        out.add((code, "direct",    "aligned"))
    for code in ("T03", "T04", "T06"):  # downtrends
        out.add((code, "dbb_trend", "aligned"))
        out.add((code, "direct",    "aligned"))
    # Extended trends — let counter-reversal in (proven moving-regime seeds)
    for code in ("T01", "T03"):
        out.add((code, "reversal", "counter"))

    # Breakouts — direct + dbb_trend continuation
    for code in ("B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08"):
        out.add((code, "direct",    "aligned"))
        out.add((code, "dbb_trend", "aligned"))

    # Expansions — direction-anchored
    out.add(("X01", "direct", "aligned"));    out.add(("X01", "dbb_trend", "aligned"))
    out.add(("X02", "direct", "aligned"));    out.add(("X02", "dbb_trend", "aligned"))
    # X03 flat expansion: VETO (no direction)
    out.add(("X04", "direct", "aligned"));    out.add(("X04", "dbb_trend", "aligned"))
    # X05 no-trend expansion: chop — reversal both
    out.add(("X05", "reversal", "aligned"));  out.add(("X05", "reversal", "counter"))

    # Stop-hunts (M01-M04) — counter-reversal is the setup
    for code in ("M01", "M02", "M03", "M04"):
        out.add((code, "reversal", "aligned"))
        out.add((code, "reversal", "counter"))

    # False breaks (F01-F04) — counter-reversal
    for code in ("F01", "F02", "F03", "F04"):
        out.add((code, "reversal", "aligned"))
        out.add((code, "reversal", "counter"))

    # Coils (C01-C04) — pre-breakout, reversal both + direct aligned
    for code in ("C01", "C02", "C03", "C04"):
        out.add((code, "reversal", "aligned"))
        out.add((code, "reversal", "counter"))
        out.add((code, "direct",   "aligned"))

    # Overbought / oversold (O01-O06) — mean reversion play
    # Seed-factory evidence: O04/O05/O06 are top winning-cell regimes
    for code in ("O01", "O02", "O03", "O04", "O05", "O06"):
        out.add((code, "reversal", "aligned"))
        out.add((code, "reversal", "counter"))
    # O02 (overbought_trend_caution) and O04 (oversold_trend_caution) have
    # ADX>=25 — also allow direct aligned (trend still in effect)
    out.add(("O02", "direct",    "aligned"))
    out.add(("O02", "dbb_trend", "aligned"))
    out.add(("O04", "direct",    "aligned"))
    out.add(("O04", "dbb_trend", "aligned"))

    # Ranges — reversal both
    out.add(("R01", "reversal", "aligned")); out.add(("R01", "reversal", "counter"))
    out.add(("R01", "direct",   "aligned"))   # wide volatile — direct OK
    out.add(("R02", "reversal", "aligned")); out.add(("R02", "reversal", "counter"))
    out.add(("R03", "reversal", "aligned")); out.add(("R03", "reversal", "counter"))
    # R04 tight_range: VETO (dead — 96% loser bucket)

    # Sessions — permissive in active, VETO in quiet
    # S01 quiet_asia, S05 quiet_ny: VETO
    out.add(("S02", "reversal", "aligned")); out.add(("S02", "reversal", "counter"))
    out.add(("S03", "reversal", "aligned")); out.add(("S03", "reversal", "counter"))
    out.add(("S03", "direct",   "aligned")); out.add(("S03", "dbb_trend", "aligned"))
    out.add(("S04", "reversal", "aligned")); out.add(("S04", "reversal", "counter"))
    out.add(("S06", "reversal", "aligned")); out.add(("S06", "reversal", "counter"))
    out.add(("S06", "direct",   "aligned")); out.add(("S06", "dbb_trend", "aligned"))

    # T07 directional_drift_flat: VETO
    # Z01 catch_all: VETO

    return out


DEFAULT_REGIME53_ALLOW_LIST = _build_regime53_allow_list()

# Dead regimes (R-math doesn't work) — for explicit audit annotation
DEAD_REGIMES_53 = {"R04", "T07", "Z01", "S01", "S05", "X03"}


# --- Existing binary basis notes (kept for fallback path) -----------------

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
    """Parse 'REGIME × family × dir' strings to tuples. Tolerates × and x."""
    out: set[tuple[str, str, str]] = set()
    if not items:
        return out
    for it in items:
        parts = [p.strip() for p in it.replace("×", "x").split("x")]
        if len(parts) == 3:
            out.add((parts[0], parts[1].lower(), parts[2].lower()))
    return out


class RegimeStrategyRouterGate(BaseGate):
    """Allow-list gate routing regime → strategy.

    Prefers 53-regime classification (technical_regime_53 feature) when
    available; falls back to binary NORMAL/CAUTION (regime classification).
    """

    name = "regime_strategy_router"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)
        cfg = config or {}

        # Binary allow-list (fallback path)
        bin_list = _parse_allow_list(cfg.get("allow_list") or [])
        self._allow_binary: set[tuple[str, str, str]] = (
            {(k[0].upper(), k[1], k[2]) for k in bin_list}
            if bin_list else set(DEFAULT_ALLOW_LIST)
        )

        # 53-regime allow-list (primary path)
        r53_list = _parse_allow_list(cfg.get("allow_list_53") or [])
        self._allow_53: set[tuple[str, str, str]] = (
            r53_list if r53_list else set(DEFAULT_REGIME53_ALLOW_LIST)
        )

        self._prefer_53: bool = bool(cfg.get("prefer_regime_53", True))

    def _get_regime53(self, ctx: SymbolContext) -> str | None:
        feat = ctx.features.get("technical_regime_53")
        if feat is None:
            return None
        vals = getattr(feat, "values", {}) or {}
        code = vals.get("technical_regime_53")
        if not code:
            return None
        return str(code).upper()

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        ema = ctx.features.get("ema")
        if ema is None:
            return GateResult(
                gate_name=self.name, passed=True,
                reason="ema missing — pass-through",
                metrics={"decision": "pass_through_missing_ema"},
            )
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

        regime53 = self._get_regime53(ctx) if self._prefer_53 else None

        if regime53:
            # 53-cell primary path
            key53 = (regime53, family, dir_vs_hint)
            allowed = key53 in self._allow_53
            in_dead = regime53 in DEAD_REGIMES_53
            passed = True  # Phase D: label-only, table enforces at leaf
            if allowed:
                reason = f"r53 {regime53} × {family} × {dir_vs_hint}: LABEL-ONLY pass"
            elif in_dead:
                reason = (
                    f"r53 {regime53} × {family} × {dir_vs_hint}: LABEL-ONLY pass "
                    f"(dead regime label retained — table is enforcer)"
                )
            else:
                reason = (
                    f"r53 {regime53} × {family} × {dir_vs_hint}: LABEL-ONLY pass "
                    f"(no allow-list match retained — table is enforcer)"
                )
            return GateResult(
                gate_name=self.name,
                passed=passed,
                reason=reason,
                metrics={
                    "path": "regime53",
                    "technical_regime_53": regime53,
                    "strategy_family": family,
                    "direction": cand_dir,
                    "direction_hint": dir_hint,
                    "dir_vs_hint": dir_vs_hint,
                    "in_allow_list_53": allowed,
                    "in_dead_regime_53": in_dead,
                    "allow_list_53_size": len(self._allow_53),
                    "mode": self.mode.value if hasattr(self.mode, "value") else str(self.mode),
                },
            )

        # Fallback: binary NORMAL/CAUTION
        reg = ctx.classifications.get("regime")
        if reg is None:
            return GateResult(
                gate_name=self.name, passed=True,
                reason="no regime53 and no binary regime — pass-through",
                metrics={"decision": "pass_through_missing_inputs", "path": "binary_missing"},
            )
        regime_label = str(getattr(reg, "label", "") or "").upper()
        key = (regime_label, family, dir_vs_hint)
        allowed = key in self._allow_binary
        basis = _BASIS_NOTES.get(key, "")
        passed = True  # Phase D: label-only, table enforces at leaf
        if allowed:
            reason = f"binary {regime_label} × {family} × {dir_vs_hint}: LABEL-ONLY pass (binary fallback)"
        else:
            reason = (
                f"binary {regime_label} × {family} × {dir_vs_hint}: LABEL-ONLY pass "
                f"(binary fallback, no allow-list match)"
            )
        return GateResult(
            gate_name=self.name,
            passed=passed,
            reason=reason,
            metrics={
                "path": "binary_fallback",
                "regime_label": regime_label,
                "strategy_family": family,
                "direction": cand_dir,
                "direction_hint": dir_hint,
                "dir_vs_hint": dir_vs_hint,
                "in_allow_list": allowed,
                "allow_list_size": len(self._allow_binary),
                "matrix_basis": basis,
                "mode": self.mode.value if hasattr(self.mode, "value") else str(self.mode),
            },
        )
