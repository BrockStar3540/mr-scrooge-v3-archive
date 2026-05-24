"""Canonical Darvas Box — FX-adapted continuation breakout.

Implements the five variants documented in the Mini-side research:
  - DRV1_darvas_box_long_strict
  - DRV2_darvas_box_long_6bar
  - DRV3_darvas_box_long_no_trend_filter
  - DRV4_darvas_box_long_ghost
  - DRV5_darvas_box_mirrored_short_NONCANON

The strategy registers under name="canonical_darvas" so the router/scan path
can target it exactly the same way canonical_lien_dbb is targeted. Each fired
candidate emits candidate.strategy=<variant_name>, which lets the routing table
match exact DRV* rows.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime, timezone

import pandas as pd

from scrooge_v3.core.types import SymbolContext, TradeCandidate, TradeDirection

log = logging.getLogger("scrooge_v3.strategy.canonical_darvas")


DEFAULT_VARIANTS = [
    {"name": "DRV4_darvas_box_long_ghost", "direction": "long", "hold": 3, "trend_filter": True, "ghost": True},
    {"name": "DRV1_darvas_box_long_strict", "direction": "long", "hold": 3, "trend_filter": True, "ghost": False},
    {"name": "DRV3_darvas_box_long_no_trend_filter", "direction": "long", "hold": 3, "trend_filter": False, "ghost": False},
    {"name": "DRV2_darvas_box_long_6bar", "direction": "long", "hold": 6, "trend_filter": True, "ghost": False},
    {"name": "DRV5_darvas_box_mirrored_short_NONCANON", "direction": "short", "hold": 3, "trend_filter": True, "ghost": False},
]


@dataclass
class BoxSpec:
    top: float
    bottom: float
    set_idx: int
    top_idx: int
    bottom_idx: int


class CanonicalDarvasStrategy:
    name = "canonical_darvas"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.enabled = config.get("enabled", True)
        self.variants = config.get("variants", DEFAULT_VARIANTS)
        self.max_stale_bars = int(config.get("max_stale_bars", 30))
        self.min_box_pips = float(config.get("min_box_pips", 8.0))
        self.min_box_atr = float(config.get("min_box_atr", 0.6))
        self.entry_buffer_atr = float(config.get("entry_buffer_atr", 0.05))
        self.stop_buffer_pips = float(config.get("stop_buffer_pips", 2.0))
        self.fixed_score = int(config.get("fixed_score", 33))
        self.min_rr = float(config.get("min_rr", 1.2))
        log.info("[STRATEGY:canonical_darvas] init enabled=%s variants=%d", self.enabled, len(self.variants))

    def eligible(self, ctx: SymbolContext) -> bool:
        if not self.enabled:
            return False
        bars = ctx.snapshot.candles.get("5M")
        if bars is None or len(bars) < 40:
            return False
        if ctx.features.get("atr") is None or ctx.features.get("ema") is None:
            return False
        return True

    def evaluate(self, ctx: SymbolContext) -> TradeCandidate | None:
        bars = ctx.snapshot.candles.get("5M")
        atr_feat = ctx.features.get("atr")
        ema_feat = ctx.features.get("ema")
        if bars is None or atr_feat is None or ema_feat is None or len(bars) < 40:
            return None

        opens = bars["open"].astype(float).values
        highs = bars["high"].astype(float).values
        lows = bars["low"].astype(float).values
        closes = bars["close"].astype(float).values
        current_close = float(closes[-1])
        atr14 = self._extract_atr14(atr_feat)
        ema50 = self._extract_ema50(ema_feat)
        if atr14 is None or atr14 <= 0 or ema50 is None or ema50 <= 0:
            return None

        pip = 0.01 if "JPY" in ctx.symbol else 0.0001
        stop_buffer = self.stop_buffer_pips * pip
        entry_buffer = self.entry_buffer_atr * atr14

        for variant in self.variants:
            hold = int(variant["hold"])
            direction = variant["direction"]
            spec = self._find_latest_box(highs, lows, hold, direction)
            if spec is None:
                continue
            if (len(closes) - 1 - spec.set_idx) > self.max_stale_bars:
                continue
            box_height = spec.top - spec.bottom
            if box_height <= 0:
                continue
            if box_height < max(self.min_box_pips * pip, self.min_box_atr * atr14):
                continue

            if variant.get("trend_filter", True):
                if direction == "long" and current_close <= ema50:
                    continue
                if direction == "short" and current_close >= ema50:
                    continue

            prev_close = float(closes[-2])
            if direction == "long":
                breakout = current_close > spec.top + entry_buffer and prev_close <= spec.top + entry_buffer
                if not breakout:
                    continue
                entry_price = ctx.snapshot.close_ask if hasattr(ctx.snapshot, "close_ask") else current_close
                stop_price = spec.bottom - stop_buffer
                risk = entry_price - stop_price
                tp = entry_price + 2.0 * risk
                reward = tp - entry_price
                trade_dir = TradeDirection.LONG
            else:
                breakout = current_close < spec.bottom - entry_buffer and prev_close >= spec.bottom - entry_buffer
                if not breakout:
                    continue
                entry_price = ctx.snapshot.close_bid if hasattr(ctx.snapshot, "close_bid") else current_close
                stop_price = spec.top + stop_buffer
                risk = stop_price - entry_price
                tp = entry_price - 2.0 * risk
                reward = entry_price - tp
                trade_dir = TradeDirection.SHORT

            if risk <= 0 or reward <= 0:
                continue
            rr = reward / risk
            if rr < self.min_rr:
                continue

            variant_id = variant["name"]
            log.info(
                "[STRATEGY:canonical_darvas] %s symbol=%s close=%.5f top=%.5f bottom=%.5f hold=%d rr=%.2f",
                variant_id, ctx.symbol, current_close, spec.top, spec.bottom, hold, rr,
            )
            return TradeCandidate(
                symbol=ctx.symbol,
                direction=trade_dir,
                strategy=variant_id,
                entry_price=entry_price,
                stop_price=stop_price,
                take_profit=tp,
                size=0.0,
                risk_reward=rr,
                score=self.fixed_score,
                metadata={
                    "entry_type": "CANONICAL_DARVAS",
                    "strategy_family": "canonical_darvas",
                    "variant_name": variant_id,
                    "darvas_top": spec.top,
                    "darvas_bottom": spec.bottom,
                    "darvas_hold": hold,
                    "darvas_box_age_bars": int(len(closes) - 1 - spec.set_idx),
                    "darvas_top_idx": spec.top_idx,
                    "darvas_bottom_idx": spec.bottom_idx,
                    "box_height": float(box_height),
                    "atr14": float(atr14),
                    "ema50": float(ema50),
                    "ghost_mode": bool(variant.get("ghost", False)),
                },
                created_at=datetime.now(timezone.utc),
            )
        return None

    def _find_latest_box(self, highs, lows, hold: int, direction: str) -> BoxSpec | None:
        n = len(highs)
        if direction == "long":
            for top_idx in range(n - (2 * hold + 2), hold, -1):
                top = float(highs[top_idx])
                post_top = highs[top_idx + 1 : top_idx + hold + 1]
                if len(post_top) < hold or max(post_top) > top:
                    continue
                low_window_start = top_idx + 1
                low_window_end = min(n - hold, top_idx + hold + 4)
                if low_window_start >= low_window_end:
                    continue
                candidate_lows = lows[low_window_start:low_window_end]
                bottom_rel = int(candidate_lows.argmin())
                bottom_idx = low_window_start + bottom_rel
                bottom = float(lows[bottom_idx])
                hold_after_low = lows[bottom_idx + 1 : bottom_idx + hold + 1]
                if len(hold_after_low) < hold or min(hold_after_low) < bottom:
                    continue
                return BoxSpec(top=top, bottom=bottom, set_idx=bottom_idx + hold, top_idx=top_idx, bottom_idx=bottom_idx)
        else:
            for bottom_idx in range(n - (2 * hold + 2), hold, -1):
                bottom = float(lows[bottom_idx])
                post_bottom = lows[bottom_idx + 1 : bottom_idx + hold + 1]
                if len(post_bottom) < hold or min(post_bottom) < bottom:
                    continue
                high_window_start = bottom_idx + 1
                high_window_end = min(n - hold, bottom_idx + hold + 4)
                if high_window_start >= high_window_end:
                    continue
                candidate_highs = highs[high_window_start:high_window_end]
                top_rel = int(candidate_highs.argmax())
                top_idx = high_window_start + top_rel
                top = float(highs[top_idx])
                hold_after_high = highs[top_idx + 1 : top_idx + hold + 1]
                if len(hold_after_high) < hold or max(hold_after_high) > top:
                    continue
                return BoxSpec(top=top, bottom=bottom, set_idx=top_idx + hold, top_idx=top_idx, bottom_idx=bottom_idx)
        return None

    @staticmethod
    def _extract_atr14(atr_feat) -> float | None:
        v = getattr(atr_feat, "values", None) or {}
        for k in ("atr", "atr14", "ATR14", "atr_14", "value"):
            if k in v and v[k] is not None:
                try:
                    return float(v[k])
                except (TypeError, ValueError):
                    pass
        return None

    @staticmethod
    def _extract_ema50(ema_feat) -> float | None:
        v = getattr(ema_feat, "values", None) or {}
        try:
            return float(v.get("ema50"))
        except (TypeError, ValueError):
            return None


__all__ = ["CanonicalDarvasStrategy"]
