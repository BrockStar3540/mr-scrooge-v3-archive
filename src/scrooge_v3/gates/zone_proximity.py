"""Zone proximity gate -- checks if price is near a liquidity zone."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate


class ZoneProximityGate(BaseGate):
    """Gate 1 -- Zone proximity check.

    Passes if current price is within ``zone_proximity_pct`` of a known
    liquidity zone (formerly "magic line").
    """

    name = "zone_proximity"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)
        self.zone_proximity_pct: float = self.config.get(
            "zone_proximity_pct", 0.0025
        )

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        symbol = candidate.symbol
        zone_map = ctx.metadata.get("zone_map")
        if zone_map is None:
            return GateResult(
                gate_name=self.name,
                passed=False,
                reason="No zone_map in context",
            )

        current_price = zone_map.current_price

        # JPY pairs: 2x proximity (~0.2% ~= 31 pips at USD/JPY 158)
        proximity = (
            self.zone_proximity_pct * 2
            if "JPY" in symbol
            else self.zone_proximity_pct
        )

        best_zone = None
        best_tier = 99
        now_str = datetime.now().isoformat()

        # Check all liquidity zones
        for zone in zone_map.sell_zones + zone_map.buy_zones:
            dist_pct = abs(current_price - zone.price) / current_price
            if dist_pct <= proximity and zone.tier < best_tier:
                best_tier = zone.tier
                best_zone = zone

        # PDH/PDL -- always Tier 1
        session_range = zone_map.daily_box
        for level, label in [
            (session_range.PDH, "PDH"),
            (session_range.PDL, "PDL"),
        ]:
            if abs(current_price - level) / current_price <= proximity:
                if best_zone is None or best_tier > 1:
                    best_tier = 1
                    # Create a lightweight zone-like object
                    best_zone = _make_zone(
                        level, label, tier=1, strength=100,
                        source_tf="D", symbol=symbol, now_str=now_str,
                    )

        # Prior hour high/low -- Tier 2
        for level, label in [
            (zone_map.prior_hour_high, "PHH"),
            (zone_map.prior_hour_low, "PHL"),
        ]:
            if abs(current_price - level) / current_price <= proximity:
                if best_zone is None or best_tier > 2:
                    best_tier = 2
                    best_zone = _make_zone(
                        level, label, tier=2, strength=80,
                        source_tf="1H", symbol=symbol, now_str=now_str,
                    )

        if best_zone is None:
            self._log.debug(
                "[GATE:%s] FAILED symbol=%s reason=not near any liquidity zone",
                self.name, symbol,
            )
            return GateResult(
                gate_name=self.name,
                passed=False,
                reason=(
                    f"Price {current_price:.5f} not near any liquidity zone"
                ),
            )

        # Infer direction from zone type
        direction = (
            "short"
            if best_zone.zone_type
            in ("resistance", "PDH", "PHH", "sell_zone")
            else "long"
        )
        if zone_map.current_zone in ("sell_zone", "above_box"):
            direction = "short"

        # Score: Tier 1=1.0, Tier 2=0.7, Tier 3=0.4
        score = max(0.0, 1.0 - (best_tier - 1) * 0.3)

        self._log.debug(
            "[GATE:%s] PASSED symbol=%s reason=Tier %d %s @ %.5f",
            self.name, symbol, best_tier, best_zone.zone_type,
            best_zone.price,
        )
        return GateResult(
            gate_name=self.name,
            passed=True,
            reason=(
                f"Tier {best_tier} {best_zone.zone_type}"
                f" @ {best_zone.price:.5f}"
            ),
            metrics={
                "score": score,
                "zone_tier": best_tier,
                "zone_price": best_zone.price,
                "zone_type": best_zone.zone_type,
                "zone_strength": best_zone.strength_score,
                "direction": direction,
                "active_zone": best_zone,
            },
        )


def _make_zone(
    price: float,
    zone_type: str,
    *,
    tier: int,
    strength: int,
    source_tf: str,
    symbol: str,
    now_str: str,
) -> Any:
    """Build a lightweight zone object matching MagicLine / LiquidityZone shape."""
    from types import SimpleNamespace

    return SimpleNamespace(
        price=price,
        zone_type=zone_type,
        tier=tier,
        test_count=0,
        strength_score=strength,
        last_tested=now_str,
        daily_aligned=(tier == 1),
        is_breakout_flip=False,
        source_timeframe=source_tf,
        symbol=symbol,
        created_at=now_str,
    )
