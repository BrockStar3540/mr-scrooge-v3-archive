"""Scoring widget — V3 scorer breakdown per candidate."""

from __future__ import annotations

from typing import Any


class ScoringWidget:
    """Shows V3 scorer results: score breakdown, tier, pair bonuses."""

    widget_name = "scoring"
    widget_category = "strategies"

    def __init__(self):
        self._last_results: list[dict[str, Any]] = []

    def record_result(self, symbol: str, score: int, tier: str,
                      breakdown: dict, pairs_total: int) -> None:
        self._last_results.append({
            "symbol": symbol, "score": score, "tier": tier,
            "breakdown": breakdown, "pairs_total": pairs_total,
        })
        # Keep last 50 results
        if len(self._last_results) > 50:
            self._last_results = self._last_results[-50:]

    def render_data(self) -> dict[str, Any]:
        return {
            "recent_scores": self._last_results[-10:],
            "total_evaluated": len(self._last_results),
            "tiers": {
                "A": sum(1 for r in self._last_results if r["tier"] == "A"),
                "B": sum(1 for r in self._last_results if r["tier"] == "B"),
                "REJECT": sum(1 for r in self._last_results if r["tier"] == "REJECT"),
                "BLOCKED": sum(1 for r in self._last_results if r["tier"] == "BLOCKED"),
            },
        }
