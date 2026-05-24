"""Box Master Theory — Scrooge-internal liquidity-sweep reversal strategy.

Sourced directly from `docs/MASTER_THEORY.md` (Part I — Source Theory): the Pitchfork
candle pattern at PDH/PDL edges.

Implements parameter-variant iteration: each variant runs the same Pitchfork mechanic
with different thresholds (sucker_count, wick_pct, middle_pct, sweep_proximity).
Variants are iterated strictest-first; the first variant that fires emits the candidate.

This is NOT a Darvas Box implementation. Darvas is a separate, trend-continuation
strategy and is not implemented in this module. See `wiki/systems/scrooge-strategy-naming-disambiguation.md`.

Entry mechanic (long; short is symmetric):
  1. Edge proximity   — low of last 5 bars within 0.5 * ATR14 of PDL
  2. Sucker move      — >=N of last 5 bars red (per-variant N)
  3. Sweep            — low of last 5 bars at or below PDL + sweep_pct * ATR14
  4. Middle filter    — current close <= PDL + middle_pct * (PDH - PDL)
  5. Signal candle    — current bar is green AND prior bar was red
  6. Wick filter      — lower wick of signal candle >= wick_pct of candle range (per-variant)

  Stop  = signal candle's low - 2 pip buffer
  Entry = signal candle's close
  TP    = PDH

10/12/ratchet execution clamp from V3 execution truth overrides at execution time.

Routed family only: rule-pass is permissive; routing_table_v10_fast_v1_XX.parquet gates approval.

VARIANT MATCHING NOTE: candidate.strategy = the exact MTB variant name. This keeps
live routing exact the same way DBB and textbook probes are exact. Each bank row should
therefore use the exact variant name the strategy emits, not a family alias.
"""
from __future__ import annotations
import logging
from datetime import datetime, timezone

from scrooge_v3.core.types import SymbolContext, TradeCandidate, TradeDirection

log = logging.getLogger("scrooge_v3.strategy.box_master_theory")

# Defaults shared across all variants (parameterized only when explicitly listed in variant dict)
SUCKER_WINDOW = 5
EDGE_PROXIMITY_ATR_FRAC = 0.5
STOP_BUFFER_PIPS = 2
FIXED_SCORE = 30
MIN_BARS_REQUIRED = 25

# Default variant list: strictest-first ordering for first-match wins.
# Add NEW variants here as v1.11 / v1.12 candidates come online.
DEFAULT_VARIANTS = [
    # === v1.11 NEW VARIANTS (added 2026-05-23) ===
    # Most-restrictive: 4-of-5 same-color sucker + wick + loose middle
    {"name": "MTB_S4W30M35P20_long",  "direction": "long",  "sucker": 4, "wick": 0.30, "middle": 0.35, "sweep": 0.20},
    # === v1.10 EXISTING VARIANTS (preserve) ===
    {"name": "MTB2_pitchfork_long_with_wick",  "direction": "long",  "sucker": 3, "wick": 0.30, "middle": 0.30, "sweep": 0.20},
    {"name": "MTB2_pitchfork_short_with_wick", "direction": "short", "sucker": 3, "wick": 0.30, "middle": 0.30, "sweep": 0.20},
    # === v1.11 NEW VARIANTS (continued) ===
    {"name": "MTB_S3W0M35P20_long",   "direction": "long",  "sucker": 3, "wick": 0.0,  "middle": 0.35, "sweep": 0.20},
    {"name": "MTB_S3W0M30P30_short",  "direction": "short", "sucker": 3, "wick": 0.0,  "middle": 0.30, "sweep": 0.30},
    # === v1.10 EXISTING VARIANTS (continued) ===
    {"name": "MTB1_pitchfork_long_strict",     "direction": "long",  "sucker": 3, "wick": 0.0,  "middle": 0.30, "sweep": 0.20},
    {"name": "MTB1_pitchfork_short_strict",    "direction": "short", "sucker": 3, "wick": 0.0,  "middle": 0.30, "sweep": 0.20},
    # === v1.11 NEW VARIANTS (loosest sucker) ===
    {"name": "MTB_S2W0M30P20_long",   "direction": "long",  "sucker": 2, "wick": 0.0,  "middle": 0.30, "sweep": 0.20},
    {"name": "MTB_S2W0M30P20_short",  "direction": "short", "sucker": 2, "wick": 0.0,  "middle": 0.30, "sweep": 0.20},
    # === v1.12_FULL NEW VARIANTS (added 2026-05-24) — from unified 6m rebuild ===
    {"name": "MTB_S2W0M25P20_short",  "direction": "short", "sucker": 2, "wick": 0.0,  "middle": 0.25, "sweep": 0.20},
    {"name": "MTB_S3W0M30P30_long",   "direction": "long",  "sucker": 3, "wick": 0.0,  "middle": 0.30, "sweep": 0.30},
    {"name": "MTB_S2W20M35P20_short", "direction": "short", "sucker": 2, "wick": 0.20, "middle": 0.35, "sweep": 0.20},
    {"name": "MTB_S2W30M25P20_short", "direction": "short", "sucker": 2, "wick": 0.30, "middle": 0.25, "sweep": 0.20},
    {"name": "MTB_S3W30M35P20_long",  "direction": "long",  "sucker": 3, "wick": 0.30, "middle": 0.35, "sweep": 0.20},
    {"name": "MTB_S3W20M25P20_short", "direction": "short", "sucker": 3, "wick": 0.20, "middle": 0.25, "sweep": 0.20},
    {"name": "MTB_S3W20M30P20_long",  "direction": "long",  "sucker": 3, "wick": 0.20, "middle": 0.30, "sweep": 0.20},
    # === v1.12_EMERGENCY 2026-05-24 — extra raw-profitable tonight variants ===
    {"name": "MTB1S2_long",                  "direction": "long",  "sucker": 2, "wick": 0.0,  "middle": 0.30, "sweep": 0.20},
    {"name": "MTB1S2_short",                 "direction": "short", "sucker": 2, "wick": 0.0,  "middle": 0.30, "sweep": 0.20},
    {"name": "MTB2W20_long",                "direction": "long",  "sucker": 3, "wick": 0.20, "middle": 0.30, "sweep": 0.20},
    {"name": "MTB_S2W0M35P20_short",        "direction": "short", "sucker": 2, "wick": 0.0,  "middle": 0.35, "sweep": 0.20},
    {"name": "MTB_S2W20M25P20_short",       "direction": "short", "sucker": 2, "wick": 0.20, "middle": 0.25, "sweep": 0.20},
    {"name": "MTB_S2W20M30P20_short",       "direction": "short", "sucker": 2, "wick": 0.20, "middle": 0.30, "sweep": 0.20},
    {"name": "MTB_S4W20M30P20_short",       "direction": "short", "sucker": 4, "wick": 0.20, "middle": 0.30, "sweep": 0.20},
    {"name": "MTB_S3W0M25P20_long",         "direction": "long",  "sucker": 3, "wick": 0.0,  "middle": 0.25, "sweep": 0.20},
    {"name": "MTB_S3W0M30P15_long",         "direction": "long",  "sucker": 3, "wick": 0.0,  "middle": 0.30, "sweep": 0.15},
    {"name": "MTB3T1_75_short",             "direction": "short", "sucker": 3, "wick": 0.0,  "middle": 0.30, "sweep": 0.20, "travel_atr": 1.75},
    {"name": "MTB3T2_0_short",              "direction": "short", "sucker": 3, "wick": 0.0,  "middle": 0.30, "sweep": 0.20, "travel_atr": 2.0},
    # === v1.12_SIBLING_WAVE 2026-05-24 — deeper brother/sister pools in live hot pockets ===
    {"name": "MTB_S3W0M25P20_short",        "direction": "short", "sucker": 3, "wick": 0.0,  "middle": 0.25, "sweep": 0.20},
    {"name": "MTB_S3W0M30P15_short",        "direction": "short", "sucker": 3, "wick": 0.0,  "middle": 0.30, "sweep": 0.15},
    {"name": "MTB_S3W0M30P20_short",        "direction": "short", "sucker": 3, "wick": 0.0,  "middle": 0.30, "sweep": 0.20},
    {"name": "MTB_S3W0M35P20_short",        "direction": "short", "sucker": 3, "wick": 0.0,  "middle": 0.35, "sweep": 0.20},
    {"name": "MTB_S2W20M25P20_long",        "direction": "long",  "sucker": 2, "wick": 0.20, "middle": 0.25, "sweep": 0.20},
    {"name": "MTB_S2W20M30P20_long",        "direction": "long",  "sucker": 2, "wick": 0.20, "middle": 0.30, "sweep": 0.20},
    {"name": "MTB_S2W20M35P20_long",        "direction": "long",  "sucker": 2, "wick": 0.20, "middle": 0.35, "sweep": 0.20},
    {"name": "MTB_S2W40M25P20_long",        "direction": "long",  "sucker": 2, "wick": 0.40, "middle": 0.25, "sweep": 0.20},
    {"name": "MTB_S2W40M30P20_long",        "direction": "long",  "sucker": 2, "wick": 0.40, "middle": 0.30, "sweep": 0.20},
    {"name": "MTB_S2W40M35P20_long",        "direction": "long",  "sucker": 2, "wick": 0.40, "middle": 0.35, "sweep": 0.20},
    {"name": "MTB_S3W20M25P20_long",        "direction": "long",  "sucker": 3, "wick": 0.20, "middle": 0.25, "sweep": 0.20},
    {"name": "MTB_S3W30M25P20_long",        "direction": "long",  "sucker": 3, "wick": 0.30, "middle": 0.25, "sweep": 0.20},
    {"name": "MTB2W40_long",                "direction": "long",  "sucker": 3, "wick": 0.40, "middle": 0.30, "sweep": 0.20},
    {"name": "MTB2W50_long",                "direction": "long",  "sucker": 3, "wick": 0.50, "middle": 0.30, "sweep": 0.20},
    # === v1.12_FULL TIER1B — MTB3 emotional / travel-based variants (added 2026-05-24) ===
    # travel_atr: require move INTO sweep >= travel_atr * ATR14 (emotional / outsized move signature)
    {"name": "MTB3_pitchfork_long_emotional",  "direction": "long",  "sucker": 3, "wick": 0.0, "middle": 0.30, "sweep": 0.20, "travel_atr": 1.5},
    {"name": "MTB3_pitchfork_short_emotional", "direction": "short", "sucker": 3, "wick": 0.0, "middle": 0.30, "sweep": 0.20, "travel_atr": 1.5},
    {"name": "MTB3T1_0_long",                  "direction": "long",  "sucker": 3, "wick": 0.0, "middle": 0.30, "sweep": 0.20, "travel_atr": 1.0},
    {"name": "MTB3T1_25_short",                "direction": "short", "sucker": 3, "wick": 0.0, "middle": 0.30, "sweep": 0.20, "travel_atr": 1.25},
    {"name": "MTB3T1_5_long",                  "direction": "long",  "sucker": 3, "wick": 0.0, "middle": 0.30, "sweep": 0.20, "travel_atr": 1.5},
]


class BoxMasterTheoryStrategy:
    """Pitchfork-pattern liquidity-sweep reversal at PDH/PDL edges.

    Implements StrategyModule Protocol.
    """

    name = "box_master_theory"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.enabled = config.get("enabled", True)
        self.sucker_window = config.get("sucker_window", SUCKER_WINDOW)
        self.edge_atr_frac = config.get("edge_proximity_atr_frac", EDGE_PROXIMITY_ATR_FRAC)
        self.stop_buffer_pips = config.get("stop_buffer_pips", STOP_BUFFER_PIPS)
        self.fixed_score = config.get("fixed_score", FIXED_SCORE)
        # Variants list. Each = {name, direction, sucker, wick, middle, sweep}. Strictest first.
        self.variants = config.get("variants", DEFAULT_VARIANTS)
        log.info("[STRATEGY:box_master_theory] init enabled=%s variants=%d", self.enabled, len(self.variants))

    def eligible(self, ctx: SymbolContext) -> bool:
        if not self.enabled:
            return False
        zone = ctx.features.get("zone_detector")
        if zone is None:
            return False
        atr_feat = ctx.features.get("atr")
        if atr_feat is None:
            return False
        bars = ctx.snapshot.candles.get("5M")
        if bars is None or len(bars) < MIN_BARS_REQUIRED:
            return False
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

        # Iterate variants strictest-first. First match wins.
        for v in self.variants:
            try:
                cand = self._try_variant(ctx, v, bars, pdh, pdl, atr14, pip, buffer)
                if cand is not None:
                    return cand
            except Exception:
                log.exception("[STRATEGY:box_master_theory] variant %s failed for %s", v.get("name"), ctx.symbol)
        return None

    def _try_variant(self, ctx, v, bars, pdh, pdl, atr14, pip, buffer) -> TradeCandidate | None:
        direction = v["direction"]
        if direction == "long":
            return self._try_long_pitchfork(ctx, bars, pdh, pdl, atr14, pip, buffer, v)
        return self._try_short_pitchfork(ctx, bars, pdh, pdl, atr14, pip, buffer, v)

    def _try_long_pitchfork(self, ctx, bars, pdh, pdl, atr14, pip, buffer, v) -> TradeCandidate | None:
        n = len(bars)
        if n < self.sucker_window + 2:
            return None
        opens = bars["open"].astype(float).values
        highs = bars["high"].astype(float).values
        lows  = bars["low"].astype(float).values
        closes = bars["close"].astype(float).values
        i = n - 1
        w = self.sucker_window
        sucker_min = v["sucker"]
        wick_min = v["wick"]
        middle_frac = v["middle"]
        sweep_frac = v["sweep"]

        red_count = sum(1 for k in range(i - w, i) if closes[k] < opens[k])
        if red_count < sucker_min:
            return None
        prior_min_low = min(lows[i - w:i])
        if prior_min_low > pdl + self.edge_atr_frac * atr14:
            return None
        if prior_min_low > pdl + sweep_frac * atr14:
            return None
        box_height = pdh - pdl
        if box_height <= 0:
            return None
        if closes[i] > pdl + middle_frac * box_height:
            return None
        if closes[i] <= opens[i]:
            return None
        if closes[i - 1] >= opens[i - 1]:
            return None
        candle_range = highs[i] - lows[i]
        if candle_range <= 0:
            return None
        lower_wick_pct = (min(opens[i], closes[i]) - lows[i]) / candle_range
        if wick_min > 0 and lower_wick_pct < wick_min:
            return None

        # MTB3 emotional / travel check: require move INTO sweep >= travel_atr * ATR14
        travel_atr = v.get("travel_atr")
        if travel_atr and travel_atr > 0:
            session_high = float(highs[i - w:i].max())
            travel_distance = (session_high - prior_min_low) / atr14 if atr14 > 0 else 0.0
            if travel_distance < travel_atr:
                return None

        entry_price = ctx.snapshot.close_ask if hasattr(ctx.snapshot, 'close_ask') else closes[i]
        stop_price = lows[i] - buffer
        tp_price = pdh
        risk = entry_price - stop_price
        reward = tp_price - entry_price
        if risk <= 0 or reward <= 0:
            return None
        rr = reward / risk

        variant_id = v["name"]
        log.info(
            "[STRATEGY:box_master_theory] LONG_PITCHFORK symbol=%s variant=%s "
            "close=%.5f pdl=%.5f pdh=%.5f sucker_red=%d wick_pct=%.2f middle=%.2f sweep=%.2f rr=%.2f",
            ctx.symbol, variant_id, closes[i], pdl, pdh,
            red_count, lower_wick_pct, middle_frac, sweep_frac, rr,
        )
        return TradeCandidate(
            symbol=ctx.symbol, direction=TradeDirection.LONG, strategy=variant_id,
            entry_price=entry_price, stop_price=stop_price, take_profit=tp_price,
            size=0.0, risk_reward=rr, score=self.fixed_score,
            metadata={
                "entry_type": "MTB_PITCHFORK_LONG", "variant_id": variant_id,
                "strategy_family": "box_master_theory", "management_profile": "reversal_core",
                "pdh": pdh, "pdl": pdl,
                "sucker_red_count": int(red_count), "lower_wick_pct": float(round(lower_wick_pct, 3)),
                "variant_sucker_min": sucker_min, "variant_wick_min": wick_min,
                "variant_middle_frac": middle_frac, "variant_sweep_frac": sweep_frac,
                "signal_candle_low": float(lows[i]), "signal_candle_high": float(highs[i]),
                "box_height": float(box_height), "atr14": float(atr14),
            },
            created_at=datetime.now(timezone.utc),
        )

    def _try_short_pitchfork(self, ctx, bars, pdh, pdl, atr14, pip, buffer, v) -> TradeCandidate | None:
        n = len(bars)
        if n < self.sucker_window + 2:
            return None
        opens = bars["open"].astype(float).values
        highs = bars["high"].astype(float).values
        lows  = bars["low"].astype(float).values
        closes = bars["close"].astype(float).values
        i = n - 1
        w = self.sucker_window
        sucker_min = v["sucker"]
        wick_min = v["wick"]
        middle_frac = v["middle"]
        sweep_frac = v["sweep"]

        green_count = sum(1 for k in range(i - w, i) if closes[k] > opens[k])
        if green_count < sucker_min:
            return None
        prior_max_high = max(highs[i - w:i])
        if prior_max_high < pdh - self.edge_atr_frac * atr14:
            return None
        if prior_max_high < pdh - sweep_frac * atr14:
            return None
        box_height = pdh - pdl
        if box_height <= 0:
            return None
        if closes[i] < pdh - middle_frac * box_height:
            return None
        if closes[i] >= opens[i]:
            return None
        if closes[i - 1] <= opens[i - 1]:
            return None
        candle_range = highs[i] - lows[i]
        if candle_range <= 0:
            return None
        upper_wick_pct = (highs[i] - max(opens[i], closes[i])) / candle_range
        if wick_min > 0 and upper_wick_pct < wick_min:
            return None

        # MTB3 emotional / travel check (SHORT): require move INTO sweep >= travel_atr * ATR14
        travel_atr = v.get("travel_atr")
        if travel_atr and travel_atr > 0:
            session_low = float(lows[i - w:i].min())
            travel_distance = (prior_max_high - session_low) / atr14 if atr14 > 0 else 0.0
            if travel_distance < travel_atr:
                return None

        entry_price = ctx.snapshot.close_bid if hasattr(ctx.snapshot, 'close_bid') else closes[i]
        stop_price = highs[i] + buffer
        tp_price = pdl
        risk = stop_price - entry_price
        reward = entry_price - tp_price
        if risk <= 0 or reward <= 0:
            return None
        rr = reward / risk

        variant_id = v["name"]
        log.info(
            "[STRATEGY:box_master_theory] SHORT_PITCHFORK symbol=%s variant=%s "
            "close=%.5f pdh=%.5f pdl=%.5f sucker_green=%d wick_pct=%.2f middle=%.2f sweep=%.2f rr=%.2f",
            ctx.symbol, variant_id, closes[i], pdh, pdl,
            green_count, upper_wick_pct, middle_frac, sweep_frac, rr,
        )
        return TradeCandidate(
            symbol=ctx.symbol, direction=TradeDirection.SHORT, strategy=variant_id,
            entry_price=entry_price, stop_price=stop_price, take_profit=tp_price,
            size=0.0, risk_reward=rr, score=self.fixed_score,
            metadata={
                "entry_type": "MTB_PITCHFORK_SHORT", "variant_id": variant_id,
                "strategy_family": "box_master_theory", "management_profile": "reversal_core",
                "pdh": pdh, "pdl": pdl,
                "sucker_green_count": int(green_count), "upper_wick_pct": float(round(upper_wick_pct, 3)),
                "variant_sucker_min": sucker_min, "variant_wick_min": wick_min,
                "variant_middle_frac": middle_frac, "variant_sweep_frac": sweep_frac,
                "signal_candle_low": float(lows[i]), "signal_candle_high": float(highs[i]),
                "box_height": float(box_height), "atr14": float(atr14),
            },
            created_at=datetime.now(timezone.utc),
        )

    def _extract_pdh_pdl(self, zone_feat) -> tuple:
        v = getattr(zone_feat, "values", None) or {}
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

    def _extract_atr14(self, atr_feat):
        v = getattr(atr_feat, "values", None) or {}
        for k in ("atr", "atr14", "ATR14", "atr_14", "value"):
            if k in v and v[k] is not None:
                try:
                    return float(v[k])
                except (TypeError, ValueError):
                    pass
        return None
