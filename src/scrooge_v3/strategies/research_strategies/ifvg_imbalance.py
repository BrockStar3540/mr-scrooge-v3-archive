"""IFVG (Inverse Fair Value Gap) intraday strategy — research module.

A Fair Value Gap (FVG) is a 3-candle imbalance pattern:
  * Bullish FVG: candle[i-2].high < candle[i].low. The empty range
    (candle[i-2].high, candle[i].low) is an unfilled "gap" left below
    candle 3 / above candle 1.
  * Bearish FVG: candle[i-2].low > candle[i].high. Empty range
    (candle[i].high, candle[i-2].low).

An *Inverse* FVG (IFVG) forms when price later CLOSES THROUGH a previously
created FVG, invalidating it. The original zone now flips polarity and
acts as resistance/support in the OPPOSITE direction.

Entry logic:
  1. Walk last N M5 bars; detect every FVG creation.
  2. For each FVG, scan forward — was it closed through (invalidated)?
     If so, mark the zone as an IFVG with flipped direction.
  3. If the most recent few bars retest an active IFVG zone (price touches
     the zone again without invalidating the IFVG itself), emit a
     candidate in the IFVG direction (opposite of the original FVG).

Targets follow the project brief: 5R take-profit (lab geometry layer can
override). Stop placed beyond the IFVG zone with a small pip buffer.

Emits:
  strategy = "IFVG_v1_long" or "IFVG_v1_short"
  metadata["strategy_family"] = "ifvg"
  metadata["projected_tp_pips"] required by natural_target_floor gate.

This is a research module — register manually if/when promoted to live.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

from scrooge_v3.core.types import SymbolContext, TradeCandidate, TradeDirection

log = logging.getLogger("scrooge_v3.strategy.ifvg_imbalance")


# ---------------------------------------------------------------------------
# Internal zone bookkeeping
# ---------------------------------------------------------------------------

@dataclass
class _IFVGZone:
    """A FVG that was closed-through and flipped polarity.

    `direction` is the IFVG trade direction (opposite of the original FVG).
      original bull FVG closed-through DOWN  -> IFVG short zone (resistance)
      original bear FVG closed-through UP    -> IFVG long  zone (support)
    """
    direction: str           # "long" or "short"
    upper: float             # top of the zone
    lower: float             # bottom of the zone
    formed_idx: int          # bar index of original FVG candle 3
    inverted_idx: int        # bar index where the close-through happened


# ---------------------------------------------------------------------------
# Strategy class
# ---------------------------------------------------------------------------

class IFVGStrategy:
    """Inverse Fair Value Gap intraday scalper.

    Tracks FVGs over a rolling M5 lookback, flips them to IFVGs on close-
    through, then emits on retest of an active IFVG zone.

    Config keys (all optional):
      enabled              : bool   (default True)
      lookback_bars        : int    (default 80)   M5 bars to scan
      min_gap_pips         : float  (default 1.5)  ignore noise gaps
      retest_bars          : int    (default 3)    most-recent N bars must
                                                   touch the zone to count
                                                   as a retest
      stop_buffer_pips     : float  (default 2.0)  beyond the zone edge
      tp_r_multiple        : float  (default 5.0)  per project brief
      min_rr               : float  (default 1.0)  sanity floor
      fixed_score          : float  (default 30)   placeholder score
    """

    _family = "ifvg"  # routing-table family (matches lab matrix)
    name = "ifvg_imbalance"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.enabled = bool(config.get("enabled", True))
        self.lookback_bars = int(config.get("lookback_bars", 80))
        self.min_gap_pips = float(config.get("min_gap_pips", 1.5))
        self.retest_bars = int(config.get("retest_bars", 3))
        self.stop_buffer_pips = float(config.get("stop_buffer_pips", 2.0))
        self.tp_r_multiple = float(config.get("tp_r_multiple", 5.0))
        self.min_rr = float(config.get("min_rr", 1.0))
        self.fixed_score = float(config.get("fixed_score", 30))
        log.info(
            "[STRATEGY:ifvg_imbalance] init enabled=%s lookback=%d min_gap=%.2fp tp_r=%.1f",
            self.enabled, self.lookback_bars, self.min_gap_pips, self.tp_r_multiple,
        )

    # -----------------------------------------------------------------
    # Required interface
    # -----------------------------------------------------------------

    def eligible(self, ctx: SymbolContext) -> bool:
        if not self.enabled:
            return False
        try:
            bars = ctx.snapshot.candles.get("5M")
        except Exception:
            return False
        if bars is None:
            return False
        try:
            n = len(bars)
        except Exception:
            return False
        # Need at least a handful of bars to form + invalidate + retest
        return n >= 15

    def evaluate(self, ctx: SymbolContext) -> TradeCandidate | None:
        try:
            return self._evaluate_inner(ctx)
        except Exception as exc:  # never crash the scan loop
            log.warning(
                "[STRATEGY:ifvg_imbalance] evaluate crash symbol=%s err=%r",
                getattr(ctx, "symbol", "?"), exc,
            )
            return None

    # -----------------------------------------------------------------
    # Internals
    # -----------------------------------------------------------------

    def _evaluate_inner(self, ctx: SymbolContext) -> TradeCandidate | None:
        bars = ctx.snapshot.candles.get("5M")
        if bars is None:
            return None

        # DataFrame expected, but be defensive
        try:
            highs = bars["high"].astype(float).values
            lows = bars["low"].astype(float).values
            closes = bars["close"].astype(float).values
        except Exception:
            return None

        n = len(closes)
        if n < 15:
            return None

        # Trim to lookback window
        start = max(0, n - self.lookback_bars)
        h = highs[start:]
        l = lows[start:]
        c = closes[start:]
        m = len(c)
        if m < 10:
            return None

        pip = 0.01 if "JPY" in ctx.symbol else 0.0001
        min_gap = self.min_gap_pips * pip
        buf = self.stop_buffer_pips * pip

        # ---- Pass 1: detect every FVG in the window ---------------------
        # Bullish FVG at index i (>=2): h[i-2] < l[i]; gap zone is
        #   (h[i-2], l[i]).
        # Bearish FVG at index i (>=2): l[i-2] > h[i]; gap zone is
        #   (h[i], l[i-2]).
        fvgs: list[dict[str, Any]] = []
        for i in range(2, m):
            # Bullish
            if h[i - 2] < l[i]:
                gap = l[i] - h[i - 2]
                if gap >= min_gap:
                    fvgs.append({
                        "kind": "bull",
                        "lower": float(h[i - 2]),
                        "upper": float(l[i]),
                        "idx": i,
                    })
            # Bearish
            if l[i - 2] > h[i]:
                gap = l[i - 2] - h[i]
                if gap >= min_gap:
                    fvgs.append({
                        "kind": "bear",
                        "lower": float(h[i]),
                        "upper": float(l[i - 2]),
                        "idx": i,
                    })

        if not fvgs:
            return None

        # ---- Pass 2: for each FVG, find a close-through -> flip to IFVG --
        # Bullish FVG invalidated when a later candle CLOSES BELOW its lower
        # edge. Bearish FVG invalidated when a later candle CLOSES ABOVE
        # its upper edge. The bar that does this is the "inversion" bar.
        ifvgs: list[_IFVGZone] = []
        for fvg in fvgs:
            i0 = fvg["idx"]
            if fvg["kind"] == "bull":
                for j in range(i0 + 1, m):
                    if c[j] < fvg["lower"]:
                        ifvgs.append(_IFVGZone(
                            direction="short",
                            upper=fvg["upper"],
                            lower=fvg["lower"],
                            formed_idx=i0,
                            inverted_idx=j,
                        ))
                        break
            else:  # bear
                for j in range(i0 + 1, m):
                    if c[j] > fvg["upper"]:
                        ifvgs.append(_IFVGZone(
                            direction="long",
                            upper=fvg["upper"],
                            lower=fvg["lower"],
                            formed_idx=i0,
                            inverted_idx=j,
                        ))
                        break

        if not ifvgs:
            return None

        # ---- Pass 3: filter to IFVGs that are still "active" --------------
        # An IFVG is invalidated itself if, after inversion, price closed
        # back through it in the opposite direction (a SHORT IFVG dies if a
        # close prints above its upper edge; a LONG IFVG dies if a close
        # prints below its lower edge).
        active: list[_IFVGZone] = []
        for z in ifvgs:
            killed = False
            for j in range(z.inverted_idx + 1, m):
                if z.direction == "short" and c[j] > z.upper:
                    killed = True
                    break
                if z.direction == "long" and c[j] < z.lower:
                    killed = True
                    break
            if not killed:
                active.append(z)

        if not active:
            return None

        # ---- Pass 4: did the most recent `retest_bars` touch a zone? -----
        # Touch = bar's [low, high] intersects [zone.lower, zone.upper].
        last_close = float(c[-1])
        retest_lo = max(0, m - self.retest_bars)
        recent_highs = h[retest_lo:]
        recent_lows = l[retest_lo:]

        # Prefer the most recently inverted active zone (freshest signal)
        active.sort(key=lambda z: z.inverted_idx, reverse=True)

        chosen: _IFVGZone | None = None
        for z in active:
            touched = False
            for bar_h, bar_l in zip(recent_highs, recent_lows):
                if bar_l <= z.upper and bar_h >= z.lower:
                    touched = True
                    break
            if not touched:
                continue
            # For a long IFVG (support), we want price currently AT or
            # ABOVE the zone (rejection from support). For a short IFVG
            # (resistance), price AT or BELOW the zone.
            if z.direction == "long" and last_close < z.lower:
                continue
            if z.direction == "short" and last_close > z.upper:
                continue
            chosen = z
            break

        if chosen is None:
            return None

        # ---- Build the candidate -----------------------------------------
        if chosen.direction == "long":
            direction = TradeDirection.LONG
            entry_price = last_close
            stop_price = chosen.lower - buf
            risk = entry_price - stop_price
            if risk <= 0:
                return None
            take_profit = entry_price + self.tp_r_multiple * risk
            reward = take_profit - entry_price
            strategy_id = "IFVG_v1_long"
        else:
            direction = TradeDirection.SHORT
            entry_price = last_close
            stop_price = chosen.upper + buf
            risk = stop_price - entry_price
            if risk <= 0:
                return None
            take_profit = entry_price - self.tp_r_multiple * risk
            reward = entry_price - take_profit
            strategy_id = "IFVG_v1_short"

        if risk <= 0 or reward <= 0:
            return None
        rr = reward / risk
        if rr < self.min_rr:
            return None

        projected_tp_pips = abs(take_profit - entry_price) / pip

        log.info(
            "[STRATEGY:ifvg_imbalance] %s symbol=%s dir=%s entry=%.5f stop=%.5f tp=%.5f rr=%.2f "
            "zone=[%.5f, %.5f] inv_idx=%d",
            strategy_id, ctx.symbol, direction.value,
            entry_price, stop_price, take_profit, rr,
            chosen.lower, chosen.upper, chosen.inverted_idx,
        )

        return TradeCandidate(
            symbol=ctx.symbol,
            direction=direction,
            strategy=strategy_id,
            entry_price=entry_price,
            stop_price=stop_price,
            take_profit=take_profit,
            size=0.0,
            risk_reward=rr,
            score=self.fixed_score,
            metadata={
                "entry_type": "IFVG_RETEST",
                "strategy_family": "ifvg",
                "management_profile": "scalper_5r",
                "variant_name": strategy_id,
                "ifvg_direction": chosen.direction,
                "zone_upper": chosen.upper,
                "zone_lower": chosen.lower,
                "zone_height_pips": (chosen.upper - chosen.lower) / pip,
                "fvg_formed_offset": (m - 1) - chosen.formed_idx,
                "ifvg_inverted_offset": (m - 1) - chosen.inverted_idx,
                "tp_r_multiple": self.tp_r_multiple,
                "be_at_r": 3.0,
                "risk_pct": 0.25,
                "projected_tp_pips": projected_tp_pips,
                "risk_points": risk,
                "reward_points": reward,
            },
            created_at=datetime.now(timezone.utc),
        )


__all__ = ["IFVGStrategy"]
