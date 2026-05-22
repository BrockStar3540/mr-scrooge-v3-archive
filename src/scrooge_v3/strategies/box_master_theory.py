"""Box Master Theory — Scrooge-internal liquidity-sweep reversal strategy.

Sourced directly from `docs/MASTER_THEORY.md` (Part I — Source Theory): the Pitchfork
candle pattern at PDH/PDL edges. Implements MTB1 (strict) + MTB2 (strict + John Wick).

This is NOT a Darvas Box implementation. Darvas is a separate, trend-continuation
strategy and is not implemented in this module. See `wiki/systems/scrooge-strategy-naming-disambiguation.md`.

Entry mechanic (long; short is symmetric):
  1. Edge proximity   — low of last 5 bars within 0.5 * ATR14 of PDL
  2. Sucker move      — >=3 of last 5 bars red (emotional bearish pressure into the level)
  3. Sweep            — low of last 5 bars at or below PDL + 0.2 * ATR14 (liquidity grab)
  4. Middle filter    — current close <= PDL + 0.3 * (PDH - PDL)  (not in the middle of the box)
  5. Signal candle    — current bar is green AND prior bar was red (Pitchfork)
  6. (MTB2 only)      — lower wick of signal candle >= 30% of candle range  (John Wick)

  Stop  = signal candle's low - 2 pip buffer
  Entry = signal candle's close (modelled as next-bar open in live; limit order at signal-high + 1 pip works too)
  TP    = PDH  (opposite box edge; canonical "I'm trying to catch one swing")

10/12/ratchet execution clamp from V3 execution truth overrides the strategy's emitted
SL/TP at execution time (same as all current V3 strategies).

Routed family only: rule-pass on full corpus is permissive; only routing-table cells
get approval. See routing_table_v10_fast_v1_10.parquet for live-allowed cells.
"""
from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any

from scrooge_v3.core.types import (
    SymbolContext,
    TradeCandidate,
    TradeDirection,
)

log = logging.getLogger("scrooge_v3.strategy.box_master_theory")

# Tuning constants from MASTER_THEORY.md + canonical_rules.md offline backtest
SUCKER_WINDOW = 5            # bars before current to evaluate
SUCKER_MIN_SAME_COLOR = 3    # >=3 of last SUCKER_WINDOW must be same-direction
EDGE_PROXIMITY_ATR_FRAC = 0.5
SWEEP_PROXIMITY_ATR_FRAC = 0.2
MIDDLE_BOX_FRAC = 0.3        # entry must be within 30% of the edge (outer band)
WICK_FRAC_MIN = 0.30         # lower (or upper) wick must be >= 30% of candle range for MTB2
STOP_BUFFER_PIPS = 2
FIXED_SCORE = 30             # below dbb_trend (32) and v3 floor; routing-table is the real gate
MIN_BARS_REQUIRED = 25


class BoxMasterTheoryStrategy:
    """Pitchfork-pattern liquidity-sweep reversal at PDH/PDL edges.

    Implements StrategyModule Protocol.
    """

    name = "box_master_theory"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.enabled = config.get("enabled", True)
        self.sucker_window = config.get("sucker_window", SUCKER_WINDOW)
        self.sucker_min_same = config.get("sucker_min_same_color", SUCKER_MIN_SAME_COLOR)
        self.edge_atr_frac = config.get("edge_proximity_atr_frac", EDGE_PROXIMITY_ATR_FRAC)
        self.sweep_atr_frac = config.get("sweep_proximity_atr_frac", SWEEP_PROXIMITY_ATR_FRAC)
        self.middle_frac = config.get("middle_box_frac", MIDDLE_BOX_FRAC)
        self.wick_frac_min = config.get("wick_frac_min", WICK_FRAC_MIN)
        self.stop_buffer_pips = config.get("stop_buffer_pips", STOP_BUFFER_PIPS)
        self.fixed_score = config.get("fixed_score", FIXED_SCORE)
        # If False, only MTB1 (no-wick) rules are checked. If True, MTB2 wick filter is
        # tried first; if it passes the variant is tagged MTB2. If MTB1 passes only,
        # variant is MTB1. The routing-table cell's strategy_id captures which variant
        # was prescribed by the offline corpus.
        self.try_wick_variant = config.get("try_wick_variant", True)

    # ------------------------------------------------------------------
    # Protocol
    # ------------------------------------------------------------------

    def eligible(self, ctx: SymbolContext) -> bool:
        if not self.enabled:
            return False
        # Need PDH/PDL from zone_detector (existing V3 feature)
        zone = ctx.features.get("zone_detector")
        if zone is None:
            return False
        # Need ATR from atr feature
        atr_feat = ctx.features.get("atr")
        if atr_feat is None:
            return False
        # Need 5M bars for the sucker move + signal candle
        bars = ctx.snapshot.candles.get("5M")
        if bars is None or len(bars) < MIN_BARS_REQUIRED:
            return False
        # Need PDH/PDL specifically
        pdh, pdl = self._extract_pdh_pdl(zone)
        if pdh is None or pdl is None or pdh <= pdl:
            return False
        return True

    def evaluate(self, ctx: SymbolContext) -> TradeCandidate | None:
        zone = ctx.features.get("zone_detector")
        atr_feat = ctx.features.get("atr")
        bars = ctx.snapshot.candles.get("5M")

        if zone is None or atr_feat is None or bars is None or len(bars) < MIN_BARS_REQUIRED:
            return None

        pdh, pdl = self._extract_pdh_pdl(zone)
        if pdh is None or pdl is None or pdh <= pdl:
            return None

        atr14 = self._extract_atr14(atr_feat)
        if atr14 is None or atr14 <= 0:
            return None

        pip = 0.01 if "JPY" in ctx.symbol else 0.0001
        buffer = self.stop_buffer_pips * pip

        # Try long pitchfork first (sucker move into PDL → first green close)
        candidate = self._try_long_pitchfork(ctx, bars, pdh, pdl, atr14, pip, buffer)
        if candidate is not None:
            return candidate

        # Try short pitchfork (sucker move into PDH → first red close)
        candidate = self._try_short_pitchfork(ctx, bars, pdh, pdl, atr14, pip, buffer)
        return candidate

    # ------------------------------------------------------------------
    # Long Pitchfork
    # ------------------------------------------------------------------

    def _try_long_pitchfork(
        self, ctx: SymbolContext, bars,
        pdh: float, pdl: float, atr14: float, pip: float, buffer: float,
    ) -> TradeCandidate | None:
        # Use last (sucker_window + 1) bars: i-window..i-1 are the sucker move, i is the signal
        n = len(bars)
        if n < self.sucker_window + 2:
            return None

        opens = bars["open"].astype(float).values
        highs = bars["high"].astype(float).values
        lows  = bars["low"].astype(float).values
        closes = bars["close"].astype(float).values

        i = n - 1  # current bar (signal)
        w = self.sucker_window

        # Sucker move: count red bars in [i-w, i-1]
        red_count = sum(1 for k in range(i - w, i) if closes[k] < opens[k])
        if red_count < self.sucker_min_same:
            return None

        # Edge proximity: low of last w bars within edge_atr_frac * atr of PDL
        prior_min_low = min(lows[i - w:i])
        if prior_min_low > pdl + self.edge_atr_frac * atr14:
            return None

        # Sweep: low of last w bars at or below PDL + sweep_atr_frac * atr
        if prior_min_low > pdl + self.sweep_atr_frac * atr14:
            return None

        # Middle filter: current close not in middle of box
        box_height = pdh - pdl
        if box_height <= 0:
            return None
        if closes[i] > pdl + self.middle_frac * box_height:
            return None

        # Signal candle: current bar is green, prior bar was red
        if closes[i] <= opens[i]:
            return None
        if closes[i - 1] >= opens[i - 1]:
            return None

        # Compute candle quality (for variant tagging)
        candle_range = highs[i] - lows[i]
        if candle_range <= 0:
            return None
        lower_wick_pct = (min(opens[i], closes[i]) - lows[i]) / candle_range
        variant_id = "MTB1_pitchfork_long_strict"
        if self.try_wick_variant and lower_wick_pct >= self.wick_frac_min:
            variant_id = "MTB2_pitchfork_long_with_wick"

        # Entry / stop / tp
        entry_price = ctx.snapshot.close_ask if hasattr(ctx.snapshot, 'close_ask') else closes[i]
        stop_price = lows[i] - buffer
        tp_price = pdh
        risk = entry_price - stop_price
        reward = tp_price - entry_price
        if risk <= 0 or reward <= 0:
            return None
        rr = reward / risk

        log.info(
            "[STRATEGY:box_master_theory] LONG_PITCHFORK symbol=%s variant=%s "
            "close=%.5f pdl=%.5f pdh=%.5f sucker_red=%d lower_wick_pct=%.2f rr=%.2f",
            ctx.symbol, variant_id, closes[i], pdl, pdh,
            red_count, lower_wick_pct, rr,
        )

        return TradeCandidate(
            symbol=ctx.symbol,
            direction=TradeDirection.LONG,
            strategy=self.name,
            entry_price=entry_price,
            stop_price=stop_price,
            take_profit=tp_price,
            size=0.0,
            risk_reward=rr,
            score=self.fixed_score,
            metadata={
                "entry_type": "MTB_PITCHFORK_LONG",
                "variant": variant_id,
                "strategy_family": "box_master_theory",
                "management_profile": "reversal_core",
                "pdh": pdh,
                "pdl": pdl,
                "sucker_red_count": int(red_count),
                "lower_wick_pct": float(round(lower_wick_pct, 3)),
                "signal_candle_low": float(lows[i]),
                "signal_candle_high": float(highs[i]),
                "box_height": float(box_height),
                "atr14": float(atr14),
            },
            created_at=datetime.now(timezone.utc),
        )

    # ------------------------------------------------------------------
    # Short Pitchfork
    # ------------------------------------------------------------------

    def _try_short_pitchfork(
        self, ctx: SymbolContext, bars,
        pdh: float, pdl: float, atr14: float, pip: float, buffer: float,
    ) -> TradeCandidate | None:
        n = len(bars)
        if n < self.sucker_window + 2:
            return None

        opens = bars["open"].astype(float).values
        highs = bars["high"].astype(float).values
        lows  = bars["low"].astype(float).values
        closes = bars["close"].astype(float).values

        i = n - 1
        w = self.sucker_window

        # Sucker move: count green bars
        green_count = sum(1 for k in range(i - w, i) if closes[k] > opens[k])
        if green_count < self.sucker_min_same:
            return None

        # Edge proximity (upper)
        prior_max_high = max(highs[i - w:i])
        if prior_max_high < pdh - self.edge_atr_frac * atr14:
            return None

        # Sweep
        if prior_max_high < pdh - self.sweep_atr_frac * atr14:
            return None

        # Middle filter (current close not in middle)
        box_height = pdh - pdl
        if box_height <= 0:
            return None
        if closes[i] < pdh - self.middle_frac * box_height:
            return None

        # Signal candle: current red, prior green
        if closes[i] >= opens[i]:
            return None
        if closes[i - 1] <= opens[i - 1]:
            return None

        candle_range = highs[i] - lows[i]
        if candle_range <= 0:
            return None
        upper_wick_pct = (highs[i] - max(opens[i], closes[i])) / candle_range
        variant_id = "MTB1_pitchfork_short_strict"
        if self.try_wick_variant and upper_wick_pct >= self.wick_frac_min:
            variant_id = "MTB2_pitchfork_short_with_wick"

        entry_price = ctx.snapshot.close_bid if hasattr(ctx.snapshot, 'close_bid') else closes[i]
        stop_price = highs[i] + buffer
        tp_price = pdl
        risk = stop_price - entry_price
        reward = entry_price - tp_price
        if risk <= 0 or reward <= 0:
            return None
        rr = reward / risk

        log.info(
            "[STRATEGY:box_master_theory] SHORT_PITCHFORK symbol=%s variant=%s "
            "close=%.5f pdh=%.5f pdl=%.5f sucker_green=%d upper_wick_pct=%.2f rr=%.2f",
            ctx.symbol, variant_id, closes[i], pdh, pdl,
            green_count, upper_wick_pct, rr,
        )

        return TradeCandidate(
            symbol=ctx.symbol,
            direction=TradeDirection.SHORT,
            strategy=self.name,
            entry_price=entry_price,
            stop_price=stop_price,
            take_profit=tp_price,
            size=0.0,
            risk_reward=rr,
            score=self.fixed_score,
            metadata={
                "entry_type": "MTB_PITCHFORK_SHORT",
                "variant": variant_id,
                "strategy_family": "box_master_theory",
                "management_profile": "reversal_core",
                "pdh": pdh,
                "pdl": pdl,
                "sucker_green_count": int(green_count),
                "upper_wick_pct": float(round(upper_wick_pct, 3)),
                "signal_candle_low": float(lows[i]),
                "signal_candle_high": float(highs[i]),
                "box_height": float(box_height),
                "atr14": float(atr14),
            },
            created_at=datetime.now(timezone.utc),
        )

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _extract_pdh_pdl(self, zone_feat) -> tuple[float | None, float | None]:
        """Pull PDH/PDL from zone_detector feature. Tolerant to nested shapes."""
        v = getattr(zone_feat, "values", None) or {}
        # zone_detector exposes zone_map.session_range.PDH/PDL based on V3's existing code
        zm = v.get("zone_map")
        if zm is None:
            return None, None
        sr = getattr(zm, "session_range", None) or (zm.get("session_range") if isinstance(zm, dict) else None)
        if sr is None:
            return None, None
        pdh = getattr(sr, "PDH", None) or (sr.get("PDH") if isinstance(sr, dict) else None)
        pdl = getattr(sr, "PDL", None) or (sr.get("PDL") if isinstance(sr, dict) else None)
        return (float(pdh) if pdh is not None else None,
                float(pdl) if pdl is not None else None)

    def _extract_atr14(self, atr_feat) -> float | None:
        v = getattr(atr_feat, "values", None) or {}
        # Try canonical name then fallbacks
        for k in ("atr", "atr14", "ATR14", "atr_14", "value"):
            if k in v and v[k] is not None:
                try:
                    return float(v[k])
                except (TypeError, ValueError):
                    pass
        return None
