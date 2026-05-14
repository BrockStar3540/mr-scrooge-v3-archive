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
    # Exhaustion states → reversal + direct
    "EXTREME_UP": ["reversal", "direct"],
    "EXTREME_DOWN": ["reversal", "direct"],
    "REJECTION_SHORT": ["reversal", "direct"],
    "REJECTION_LONG": ["reversal", "direct"],
    # STRETCH_UP = 0% WR on V1 live data — hard block, no strategies allowed
    "STRETCH_UP": [],
    # STRETCH_DOWN = -2 pts in V3 scorer, allow dbb_trend continuation
    "STRETCH_DOWN": ["dbb_trend", "direct"],
    # Breakout → dbb_trend + direct
    "BREAKOUT_UP": ["dbb_trend", "direct"],
    "BREAKOUT_DOWN": ["dbb_trend", "direct"],
    # Normal/range → direct entry only (V3 scorer decides quality)
    "NORMAL": ["direct"],
    # Compression → direct only
    "COMPRESSION": ["direct"],
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
                log.info(
                    "[ROUTING_TABLE] symbol=%s r53=%s session=%s bb_allowed=%s table_strategies=%s table_families=%s mode=%s",
                    ctx.symbol, r53, sess, allowed, table_names, table_families, mode,
                )
                if mode == "hard":
                    # Hard mode: table is the source of truth. Empty list = death.
                    # Return both family names and probe names (registry holds both).
                    return sorted(set(table_names + table_families))

        return allowed
