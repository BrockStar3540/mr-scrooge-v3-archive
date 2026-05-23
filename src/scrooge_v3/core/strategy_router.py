"""Strategy router — decides which strategies are eligible for the current context.

No strategy should self-activate outside router permission.
The router reads classifications and returns allowed strategy names.
"""

from __future__ import annotations

import logging
from typing import Any

from .types import SymbolContext

log = logging.getLogger("scrooge_v3.core.strategy_router")

# Default routing rules — BB state to strategy mapping
_DEFAULT_ROUTES: dict[str, list[str]] = {
    # Exhaustion states → reversal + direct + box_master_theory
    # (MTB Pitchfork fits exhaustion: sucker move into PDH/PDL → snap-back candle)
    "EXTREME_UP": ["reversal", "direct", "box_master_theory"],
    "EXTREME_DOWN": ["reversal", "direct", "box_master_theory"],
    "REJECTION_SHORT": ["reversal", "direct", "box_master_theory"],
    "REJECTION_LONG": ["reversal", "direct", "box_master_theory"],
    # STRETCH_UP previously 0% WR on V1 — direct/reversal still blocked. MTB
    # allowed because Pitchfork is PDH/PDL-anchored, not BB-anchored, and the
    # historic V1 STRETCH_UP block reflects direct/reversal failure modes that
    # don't apply to MTB's distinct entry mechanic. Routing-table gate is the
    # real safeguard — MTB only fires at routed cells (3 in v1.10).
    "STRETCH_UP": ["box_master_theory"],
    # STRETCH_DOWN = -2 pts in V3 scorer; dbb_trend + direct + MTB allowed
    "STRETCH_DOWN": ["dbb_trend", "direct", "box_master_theory"],
    # Breakout → dbb_trend + direct (MTB excluded: breakouts are continuation,
    # opposite of MTB's reversal-at-edge thesis)
    "BREAKOUT_UP": ["dbb_trend", "direct"],
    "BREAKOUT_DOWN": ["dbb_trend", "direct"],
    # Normal/range → direct + MTB (MTB can fire when PDH/PDL is wider than 2σ BB,
    # making price-at-edge possible while still inside Band A → bb_state=NORMAL)
    "NORMAL": ["direct", "box_master_theory"],
    # Compression → direct + MTB (compressed BB with wide PDH/PDL is exactly
    # the setup MTB targets: range-bound day with clean edges)
    "COMPRESSION": ["direct", "box_master_theory"],
}


class StrategyRouter:
    """Routes market context to eligible strategies.

    Reads BB state classification and returns which strategy names are allowed.
    Can be extended with custom routing rules.
    """

    def __init__(self, routes: dict[str, list[str]] | None = None):
        self.routes = routes or _DEFAULT_ROUTES

    def get_allowed(self, ctx: SymbolContext) -> list[str]:
        """Return list of allowed strategy names for the current context."""
        bb = ctx.classifications.get("bb_state")
        if bb is None:
            log.debug("[ROUTER] No BB classification for %s — no strategies", ctx.symbol)
            return []

        allowed = self.routes.get(bb.label, [])

        # Opening state can override — gap engine when available
        opening = ctx.classifications.get("opening_state")
        if opening and opening.label in ("GAP_UP", "GAP_DOWN"):
            if "gap" not in allowed:
                allowed = allowed + ["gap"]

        if allowed:
            log.debug(
                "[ROUTER] symbol=%s bb=%s → allowed=%s",
                ctx.symbol, bb.label, allowed,
            )

        # --- Routing-table observe-mode telemetry (Brock 2026-05-14) ---
        # Compute the table's decision for (regime53, pair, session) and log
        # the delta vs the BB-state-based allowed list. Behavior unchanged in
        # observe mode; flip to 'hard' to let the table actually drive routes.
        table = getattr(self, "routing_table", None)
        mode = getattr(self, "routing_table_mode", "observe")
        if table is not None:
            r53_feat = ctx.features.get("technical_regime_53")
            r53 = None
            if r53_feat is not None:
                vals = getattr(r53_feat, "values", {}) or {}
                r53 = vals.get("technical_regime_53")
            sess_cl = ctx.classifications.get("session_bucket")
            sess = getattr(sess_cl, "label", None) if sess_cl is not None else None
            if r53 and sess:
                decisions = table.lookup(r53, ctx.symbol, sess)
                table_names = [d.strategy for d in decisions]
                table_families = sorted({d.family for d in decisions})
                telemetry = getattr(self, "routing_telemetry", None)
                if telemetry is not None and telemetry.enabled:
                    telemetry.record(
                        symbol=ctx.symbol, regime53=r53, session_bucket=sess,
                        bb_allowed=list(allowed), table_strategies=table_names,
                        table_families=table_families,
                    )
                    log.debug(
                        "[ROUTING_TABLE] symbol=%s r53=%s session=%s bb_allowed=%s table_strategies=%s mode=%s",
                        ctx.symbol, r53, sess, allowed, table_names, mode,
                    )
                else:
                    log.info(
                        "[ROUTING_TABLE] symbol=%s r53=%s session=%s bb_allowed=%s table_strategies=%s table_families=%s mode=%s",
                        ctx.symbol, r53, sess, allowed, table_names, table_families, mode,
                    )
                if mode == "hard":
                    # Hard mode: table is the source of truth.
                    table_allowed = sorted(set(table_names + table_families))
                    if table_allowed:
                        ctx.metadata["router_fallback"] = False
                        return table_allowed
                    # Fallback (Brock 2026-05-19, Option B): when the table
                    # has no cell for (regime, pair, session), don't silently
                    # kill — emit the BB-allowed candidates with a fallback
                    # flag so downstream gates (entry_filter still hard) can
                    # block them while telemetry records the would-fire
                    # event. Without this, shadow can't observe what the
                    # router silently killed.
                    ctx.metadata["router_fallback"] = True
                    log.info(
                        "[ROUTER] hard_mode_fallback symbol=%s r53=%s session=%s bb_allowed=%s reason=table_empty",
                        ctx.symbol, r53, sess, allowed,
                    )
                    return allowed
                ctx.metadata["router_fallback"] = False

        return allowed
