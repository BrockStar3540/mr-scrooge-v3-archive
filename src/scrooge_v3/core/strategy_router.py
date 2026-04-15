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
    # Trend states → trend + direct
    "TREND_UP": ["trend", "direct"],
    "TREND_DOWN": ["trend", "direct"],
    # STRETCH_UP = 0% WR on V1 live data — hard block, no strategies allowed
    "STRETCH_UP": [],
    # STRETCH_DOWN = -3 pts in V3 scorer, allow trend but scorer penalizes
    "STRETCH_DOWN": ["trend", "direct"],
    # Breakout → trend + direct
    "BREAKOUT_UP": ["trend", "direct"],
    "BREAKOUT_DOWN": ["trend", "direct"],
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
        return allowed
