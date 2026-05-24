"""Textbook scalper probes — 6 high-value strategy families from the v1.12 corpus.

Maps textbook strategy IDs found in the unified 6-month rebuild routing table
into live probe candidates. Each probe emits a TradeCandidate with family
'direct' (breakout-style) or 'reversal' (fade-style) and a strategy_id that
matches the textbook name exactly.

Strategies covered (12 probes total — long + short for each):
  TF2_pullback_EMA20         → family='direct'   trend-follow pullback to EMA20
  BR2_vcb                    → family='direct'   VCB (volume-compression breakout)
  CP3_vol_coil_fade          → family='reversal' vol-coil extension fade
  MR5_williams_extreme       → family='reversal' Williams %R extreme reversal
  RG1_range_bound_scalp      → family='reversal' range-rail fade scalp
  BR5_opening_range_breakout → family='direct'   opening-range 20-bar breakout

All probes default DISABLED.
Enable via: strategies.probes_v2.<strategy_id>.enabled = true
  e.g. strategies.probes_v2.TF2_pullback_EMA20_long.enabled = true

Registers into the shared PROBE_REGISTRY from probes_v2 at import time.
"""
from __future__ import annotations

import logging

from scrooge_v3.strategies.probes_v2 import (
    PROBE_REGISTRY,
    ProbeContext,
    ProbeStrategy,
    _build_candidate_multi,
    _is_bull_bar,
    pip_size,
)

log = logging.getLogger("scrooge_v3.strategy.textbook_scalper")


def _parabolic_sar(highs, lows, step: float = 0.02, max_af: float = 0.2):
    """Return latest Wilder PSAR value, trend side, and bars since flip."""
    if len(highs) < 5 or len(lows) < 5:
        return None, None, None
    bull = (highs[1] + lows[1]) >= (highs[0] + lows[0])
    sar = lows[0] if bull else highs[0]
    ep = highs[0] if bull else lows[0]
    af = step
    bars_since_flip = 0
    for i in range(1, len(highs)):
        sar = sar + af * (ep - sar)
        if bull:
            sar = min(sar, lows[i - 1], lows[i - 2] if i >= 2 else lows[i - 1])
            if lows[i] < sar:
                bull = False
                sar = ep
                ep = lows[i]
                af = step
                bars_since_flip = 0
            else:
                bars_since_flip += 1
                if highs[i] > ep:
                    ep = highs[i]
                    af = min(af + step, max_af)
        else:
            sar = max(sar, highs[i - 1], highs[i - 2] if i >= 2 else highs[i - 1])
            if highs[i] > sar:
                bull = True
                sar = ep
                ep = highs[i]
                af = step
                bars_since_flip = 0
            else:
                bars_since_flip += 1
                if lows[i] < ep:
                    ep = lows[i]
                    af = min(af + step, max_af)
    return sar, bull, bars_since_flip


# ---------------------------------------------------------------------------
# TF2: trend-follow pullback to EMA20
# family='direct' — price tags EMA20 from trend side with mild RSI, resumes
# ---------------------------------------------------------------------------

def probe_TF2_pullback_EMA20_long(ctx: ProbeContext):
    f = ctx.features
    ema20, atr_pips, rsi = f.get("ema20"), f.get("atr_pips"), f.get("rsi")
    if None in (ema20, atr_pips, rsi):
        return None
    pip  = pip_size(ctx.symbol)
    close = ctx.m5_close[-1]
    # Price must be above EMA20 (uptrend side) and within 0.4 ATR of it
    if close <= ema20:
        return None
    if (close - ema20) / pip > 0.4 * atr_pips:
        return None
    # Moderate RSI (pulled back from overbought, not yet neutral)
    if rsi < 40 or rsi > 65:
        return None
    # Resumption: bullish bar
    if not _is_bull_bar(ctx):
        return None
    struct_ref = min(ctx.m5_low[-5:])
    return _build_candidate_multi(
        "long", close, struct_ref, ctx, "TF2_pullback_EMA20_long", {"rsi": rsi},
    )


def probe_TF2_pullback_EMA20_short(ctx: ProbeContext):
    f = ctx.features
    ema20, atr_pips, rsi = f.get("ema20"), f.get("atr_pips"), f.get("rsi")
    if None in (ema20, atr_pips, rsi):
        return None
    pip   = pip_size(ctx.symbol)
    close = ctx.m5_close[-1]
    if close >= ema20:
        return None
    if (ema20 - close) / pip > 0.4 * atr_pips:
        return None
    if rsi < 35 or rsi > 60:
        return None
    if _is_bull_bar(ctx):
        return None
    struct_ref = max(ctx.m5_high[-5:])
    return _build_candidate_multi(
        "short", close, struct_ref, ctx, "TF2_pullback_EMA20_short", {"rsi": rsi},
    )


def probe_TF4_sar_long(ctx: ProbeContext):
    f = ctx.features
    ema20, rsi, atr_pips = f.get("ema20"), f.get("rsi"), f.get("atr_pips")
    adx14 = f.get("ADX14")
    close_pos = f.get("close_pos")
    if None in (ema20, rsi, atr_pips):
        return None
    if len(ctx.m5_close) < 12:
        return None
    sar, bull, bars_since_flip = _parabolic_sar(ctx.m5_high[-12:], ctx.m5_low[-12:])
    if sar is None or not bull:
        return None
    close = ctx.m5_close[-1]
    pip = pip_size(ctx.symbol)
    if close <= sar or close <= ema20:
        return None
    if rsi < 54 or rsi > 76:
        return None
    if adx14 is not None and adx14 < 17:
        return None
    if close_pos is not None and close_pos < 0.55:
        return None
    if bars_since_flip is not None and bars_since_flip > 8:
        return None
    prior_hi = max(ctx.m5_high[-6:-1])
    if close <= prior_hi:
        return None
    if ctx.m5_close[-1] <= ctx.m5_close[-2]:
        return None
    if (close - sar) / pip > max(atr_pips * 1.35, 10.0):
        return None
    if not _is_bull_bar(ctx):
        return None
    struct_ref = float(min(ctx.m5_low[-5:]))
    return _build_candidate_multi(
        "long", close, struct_ref, ctx, "TF4_sar_long",
        {
            "rsi": rsi,
            "ADX14": adx14,
            "close_pos": close_pos,
            "psar": sar,
            "bars_since_flip": bars_since_flip,
            "prior_high": prior_hi,
        },
    )


# ---------------------------------------------------------------------------
# BR2: VCB (volume-compression breakout) — price breaks to new close extreme
# family='direct' — momentum breakout after compression
# ---------------------------------------------------------------------------

def probe_BR2_vcb_long(ctx: ProbeContext):
    f = ctx.features
    bb_pos, atr_pips, rsi = f.get("bb_position"), f.get("atr_pips"), f.get("rsi")
    if None in (bb_pos, atr_pips, rsi):
        return None
    if len(ctx.m5_close) < 6:
        return None
    # Price pushing into upper half of bands (expansion phase)
    if bb_pos < 0.80:
        return None
    # Momentum RSI — strong but not at extreme
    if rsi < 50 or rsi > 78:
        return None
    # Breakout bar: closes above prior 5-bar high close
    if ctx.m5_close[-1] <= max(ctx.m5_close[-6:-1]):
        return None
    if not _is_bull_bar(ctx):
        return None
    close = ctx.m5_close[-1]
    struct_ref = min(ctx.m5_low[-5:])
    return _build_candidate_multi(
        "long", close, struct_ref, ctx, "BR2_vcb_long",
        {"rsi": rsi, "bb_position": bb_pos},
    )


def probe_BR2_vcb_short(ctx: ProbeContext):
    f = ctx.features
    bb_pos, atr_pips, rsi = f.get("bb_position"), f.get("atr_pips"), f.get("rsi")
    if None in (bb_pos, atr_pips, rsi):
        return None
    if len(ctx.m5_close) < 6:
        return None
    if bb_pos > 0.20:
        return None
    if rsi < 22 or rsi > 50:
        return None
    if ctx.m5_close[-1] >= min(ctx.m5_close[-6:-1]):
        return None
    if _is_bull_bar(ctx):
        return None
    close = ctx.m5_close[-1]
    struct_ref = max(ctx.m5_high[-5:])
    return _build_candidate_multi(
        "short", close, struct_ref, ctx, "BR2_vcb_short",
        {"rsi": rsi, "bb_position": bb_pos},
    )


# ---------------------------------------------------------------------------
# CP3: vol-coil fade — fade the extension spike at BB extreme after compression
# family='reversal'
# ---------------------------------------------------------------------------

def probe_CP3_vol_coil_fade_long(ctx: ProbeContext):
    f = ctx.features
    bb_pos, rsi = f.get("bb_position"), f.get("rsi")
    if None in (bb_pos, rsi):
        return None
    if len(ctx.m5_close) < 5:
        return None
    # Extreme lower band tag (oversold spike to fade long)
    if bb_pos > 0.12:
        return None
    if rsi > 35:
        return None
    # Reversal: current close higher than previous (turn off lows) + bullish bar
    if ctx.m5_close[-1] <= ctx.m5_close[-2]:
        return None
    if not _is_bull_bar(ctx):
        return None
    close = ctx.m5_close[-1]
    struct_ref = min(ctx.m5_low[-3:])
    return _build_candidate_multi(
        "long", close, struct_ref, ctx, "CP3_vol_coil_fade_long",
        {"rsi": rsi, "bb_position": bb_pos},
    )


def probe_CP3_vol_coil_fade_short(ctx: ProbeContext):
    f = ctx.features
    bb_pos, rsi = f.get("bb_position"), f.get("rsi")
    if None in (bb_pos, rsi):
        return None
    if len(ctx.m5_close) < 5:
        return None
    # Extreme upper band tag (overbought spike to fade short)
    if bb_pos < 0.88:
        return None
    if rsi < 65:
        return None
    # Reversal: current close lower than previous (turn off highs) + bearish bar
    if ctx.m5_close[-1] >= ctx.m5_close[-2]:
        return None
    if _is_bull_bar(ctx):
        return None
    close = ctx.m5_close[-1]
    struct_ref = max(ctx.m5_high[-3:])
    return _build_candidate_multi(
        "short", close, struct_ref, ctx, "CP3_vol_coil_fade_short",
        {"rsi": rsi, "bb_position": bb_pos},
    )


# ---------------------------------------------------------------------------
# MR5: Williams %R extreme reversal (RSI14 used as proxy)
# family='reversal'
# ---------------------------------------------------------------------------

def probe_MR5_williams_extreme_long(ctx: ProbeContext):
    f = ctx.features
    rsi = f.get("rsi")
    if rsi is None:
        return None
    # Williams %R extreme low equivalent: RSI < 22
    if rsi > 22:
        return None
    # Reversal bar from extreme low
    if ctx.m5_close[-1] <= ctx.m5_close[-2]:
        return None
    if not _is_bull_bar(ctx):
        return None
    close = ctx.m5_close[-1]
    struct_ref = min(ctx.m5_low[-3:])
    return _build_candidate_multi(
        "long", close, struct_ref, ctx, "MR5_williams_extreme_long", {"rsi": rsi},
    )


def probe_MR5_williams_extreme_short(ctx: ProbeContext):
    f = ctx.features
    rsi = f.get("rsi")
    if rsi is None:
        return None
    # Williams %R extreme high equivalent: RSI > 78
    if rsi < 78:
        return None
    if ctx.m5_close[-1] >= ctx.m5_close[-2]:
        return None
    if _is_bull_bar(ctx):
        return None
    close = ctx.m5_close[-1]
    struct_ref = max(ctx.m5_high[-3:])
    return _build_candidate_multi(
        "short", close, struct_ref, ctx, "MR5_williams_extreme_short", {"rsi": rsi},
    )


# ---------------------------------------------------------------------------
# MR4: z-score extreme reversion — fade statistically stretched upper-band spikes
# family='reversal'
# ---------------------------------------------------------------------------

def probe_MR4_zscore_extreme_short(ctx: ProbeContext):
    f = ctx.features
    z_score, bb_pos, rsi = f.get("z_score"), f.get("bb_position"), f.get("rsi")
    if None in (z_score, bb_pos, rsi):
        return None
    if len(ctx.m5_close) < 5:
        return None
    if z_score < 1.8:
        return None
    if bb_pos < 0.88:
        return None
    if rsi < 64:
        return None
    if ctx.m5_close[-1] >= ctx.m5_close[-2]:
        return None
    if _is_bull_bar(ctx):
        return None
    close = ctx.m5_close[-1]
    struct_ref = max(ctx.m5_high[-4:])
    return _build_candidate_multi(
        "short", close, struct_ref, ctx, "MR4_zscore_extreme_short",
        {"rsi": rsi, "bb_position": bb_pos, "z_score": z_score},
    )


def probe_MR4_zscore_extreme_long(ctx: ProbeContext):
    f = ctx.features
    z_score, bb_pos, rsi = f.get("z_score"), f.get("bb_position"), f.get("rsi")
    if None in (z_score, bb_pos, rsi):
        return None
    if len(ctx.m5_close) < 5:
        return None
    if z_score > -1.8:
        return None
    if bb_pos > 0.12:
        return None
    if rsi > 36:
        return None
    if ctx.m5_close[-1] <= ctx.m5_close[-2]:
        return None
    if not _is_bull_bar(ctx):
        return None
    close = ctx.m5_close[-1]
    struct_ref = min(ctx.m5_low[-4:])
    return _build_candidate_multi(
        "long", close, struct_ref, ctx, "MR4_zscore_extreme_long",
        {"rsi": rsi, "bb_position": bb_pos, "z_score": z_score},
    )


def probe_MR2_bb_reversion_short(ctx: ProbeContext):
    f = ctx.features
    z_score, bb_pos, rsi = f.get("z_score"), f.get("bb_position"), f.get("rsi")
    bb_compress = f.get("BB_compress")
    if None in (bb_pos, rsi):
        return None
    if len(ctx.m5_close) < 5:
        return None
    if z_score is not None:
        if z_score < 1.2:
            return None
    elif bb_pos < 0.82:
        return None
    if bb_pos < 0.78:
        return None
    if rsi < 58:
        return None
    if bb_compress is not None and bb_compress > 1.15:
        return None
    if ctx.m5_close[-1] >= ctx.m5_close[-2]:
        return None
    if _is_bull_bar(ctx):
        return None
    close = ctx.m5_close[-1]
    struct_ref = max(ctx.m5_high[-4:])
    return _build_candidate_multi(
        "short", close, struct_ref, ctx, "MR2_bb_reversion_short",
        {"rsi": rsi, "bb_position": bb_pos, "z_score": z_score, "BB_compress": bb_compress},
    )


# ---------------------------------------------------------------------------
# RG1: range-bound scalp — fade band rails within a compression/range regime
# family='reversal'
# ---------------------------------------------------------------------------

def probe_RG1_range_bound_scalp_long(ctx: ProbeContext):
    f = ctx.features
    bb_pos, rsi = f.get("bb_position"), f.get("rsi")
    if None in (bb_pos, rsi):
        return None
    # Near lower rail of bands
    if bb_pos > 0.22:
        return None
    # RSI in mild-oversold zone (not extreme reversal territory — that's MR5)
    if rsi < 20 or rsi > 38:
        return None
    if not _is_bull_bar(ctx):
        return None
    close = ctx.m5_close[-1]
    struct_ref = min(ctx.m5_low[-3:])
    return _build_candidate_multi(
        "long", close, struct_ref, ctx, "RG1_range_bound_scalp_long",
        {"rsi": rsi, "bb_position": bb_pos},
    )


def probe_RG1_range_bound_scalp_short(ctx: ProbeContext):
    f = ctx.features
    bb_pos, rsi = f.get("bb_position"), f.get("rsi")
    if None in (bb_pos, rsi):
        return None
    # Near upper rail of bands
    if bb_pos < 0.78:
        return None
    if rsi < 62 or rsi > 80:
        return None
    if _is_bull_bar(ctx):
        return None
    close = ctx.m5_close[-1]
    struct_ref = max(ctx.m5_high[-3:])
    return _build_candidate_multi(
        "short", close, struct_ref, ctx, "RG1_range_bound_scalp_short",
        {"rsi": rsi, "bb_position": bb_pos},
    )


def probe_RG2_range_support_bounce_long(ctx: ProbeContext):
    f = ctx.features
    pdh, pdl = f.get("pdh"), f.get("pdl")
    if pdh is None or pdl is None:
        return None
    if ctx.bb_state not in ("REJECTION_LONG", "EXTREME_DOWN"):
        return None
    pip = pip_size(ctx.symbol)
    current_price = ctx.m5_close[-1]
    if current_price > pdh or current_price < pdl:
        return None
    box_range = max(pdh - pdl, pip)
    proximity = box_range * 0.0025
    curr_open, curr_close = ctx.m5_open[-1], ctx.m5_close[-1]
    prev_open, prev_high, prev_low, prev_close = ctx.m5_open[-2], ctx.m5_high[-2], ctx.m5_low[-2], ctx.m5_close[-2]
    c_close = float(curr_close)
    body = max(abs(prev_close - prev_open), pip * 0.5)
    if c_close > pdl + proximity:
        return None
    lower_wick = min(prev_open, prev_close) - prev_low
    upper_wick = prev_high - max(prev_open, prev_close)
    if lower_wick < body * 1.5 or lower_wick <= upper_wick:
        return None
    if c_close <= prev_high:
        return None
    return _build_candidate_multi(
        "long", c_close, float(prev_low), ctx, "RG2_range_support_bounce_long",
        {"pdh": pdh, "pdl": pdl, "bb_state": ctx.bb_state},
    )


def probe_BR3_inside_bar_long(ctx: ProbeContext):
    f = ctx.features
    ema20, rsi = f.get("ema20"), f.get("rsi")
    if None in (ema20, rsi):
        return None
    if len(ctx.m5_close) < 4:
        return None
    mother_hi, mother_lo = ctx.m5_high[-3], ctx.m5_low[-3]
    inside_hi, inside_lo = ctx.m5_high[-2], ctx.m5_low[-2]
    if not (inside_hi <= mother_hi and inside_lo >= mother_lo):
        return None
    close = ctx.m5_close[-1]
    if close <= mother_hi:
        return None
    if close <= ema20:
        return None
    if rsi < 52:
        return None
    if not _is_bull_bar(ctx):
        return None
    return _build_candidate_multi(
        "long", close, float(min(mother_lo, inside_lo)), ctx, "BR3_inside_bar_long",
        {"rsi": rsi, "mother_high": mother_hi, "mother_low": mother_lo},
    )


def probe_BR3_inside_bar_short(ctx: ProbeContext):
    f = ctx.features
    ema20, rsi = f.get("ema20"), f.get("rsi")
    if None in (ema20, rsi):
        return None
    if len(ctx.m5_close) < 4:
        return None
    mother_hi, mother_lo = ctx.m5_high[-3], ctx.m5_low[-3]
    inside_hi, inside_lo = ctx.m5_high[-2], ctx.m5_low[-2]
    if not (inside_hi <= mother_hi and inside_lo >= mother_lo):
        return None
    close = ctx.m5_close[-1]
    if close >= mother_lo:
        return None
    if close >= ema20:
        return None
    if rsi > 48:
        return None
    if _is_bull_bar(ctx):
        return None
    return _build_candidate_multi(
        "short", close, float(max(mother_hi, inside_hi)), ctx, "BR3_inside_bar_short",
        {"rsi": rsi, "mother_high": mother_hi, "mother_low": mother_lo},
    )


# ---------------------------------------------------------------------------
# BR5: opening-range breakout — 20-bar high/low break with momentum confirm
# family='direct'
# ---------------------------------------------------------------------------

def probe_BR5_opening_range_breakout_long(ctx: ProbeContext):
    f = ctx.features
    rsi = f.get("rsi")
    if rsi is None:
        return None
    if len(ctx.m5_high) < 22:
        return None
    # Price breaks above the 20-bar high (excluding current and previous bar)
    prior_high = max(ctx.m5_high[-22:-2])
    if ctx.m5_high[-1] <= prior_high:
        return None
    if not _is_bull_bar(ctx):
        return None
    # Momentum: RSI above neutral
    if rsi < 50:
        return None
    close = ctx.m5_close[-1]
    struct_ref = min(ctx.m5_low[-5:])
    return _build_candidate_multi(
        "long", close, struct_ref, ctx, "BR5_opening_range_breakout_long",
        {"rsi": rsi, "prior_high": prior_high},
    )


def probe_BR5_opening_range_breakout_short(ctx: ProbeContext):
    f = ctx.features
    rsi = f.get("rsi")
    if rsi is None:
        return None
    if len(ctx.m5_low) < 22:
        return None
    prior_low = min(ctx.m5_low[-22:-2])
    if ctx.m5_low[-1] >= prior_low:
        return None
    if _is_bull_bar(ctx):
        return None
    if rsi > 50:
        return None
    close = ctx.m5_close[-1]
    struct_ref = max(ctx.m5_high[-5:])
    return _build_candidate_multi(
        "short", close, struct_ref, ctx, "BR5_opening_range_breakout_short",
        {"rsi": rsi, "prior_low": prior_low},
    )


def probe_CP1_coil_breakout_long(ctx: ProbeContext):
    f = ctx.features
    ema20, rsi, atr_pips = f.get("ema20"), f.get("rsi"), f.get("atr_pips")
    bb_compress = f.get("BB_compress")
    if None in (ema20, rsi, atr_pips):
        return None
    if len(ctx.m5_close) < 7:
        return None
    if bb_compress is not None and bb_compress > 0.95:
        return None
    coil_hi = max(ctx.m5_high[-6:-1])
    coil_lo = min(ctx.m5_low[-6:-1])
    if (coil_hi - coil_lo) / max(atr_pips * pip_size(ctx.symbol), pip_size(ctx.symbol)) > 1.25:
        return None
    close = ctx.m5_close[-1]
    if close <= coil_hi:
        return None
    if close <= ema20:
        return None
    if rsi < 53:
        return None
    if not _is_bull_bar(ctx):
        return None
    return _build_candidate_multi(
        "long", close, float(coil_lo), ctx, "CP1_coil_breakout_long",
        {"rsi": rsi, "BB_compress": bb_compress, "coil_high": coil_hi, "coil_low": coil_lo},
    )


def probe_CP1_coil_breakout_short(ctx: ProbeContext):
    f = ctx.features
    ema20, rsi, atr_pips = f.get("ema20"), f.get("rsi"), f.get("atr_pips")
    bb_compress = f.get("BB_compress")
    if None in (ema20, rsi, atr_pips):
        return None
    if len(ctx.m5_close) < 7:
        return None
    if bb_compress is not None and bb_compress > 0.95:
        return None
    coil_hi = max(ctx.m5_high[-6:-1])
    coil_lo = min(ctx.m5_low[-6:-1])
    if (coil_hi - coil_lo) / max(atr_pips * pip_size(ctx.symbol), pip_size(ctx.symbol)) > 1.25:
        return None
    close = ctx.m5_close[-1]
    if close >= coil_lo:
        return None
    if close >= ema20:
        return None
    if rsi > 47:
        return None
    if _is_bull_bar(ctx):
        return None
    return _build_candidate_multi(
        "short", close, float(coil_hi), ctx, "CP1_coil_breakout_short",
        {"rsi": rsi, "BB_compress": bb_compress, "coil_high": coil_hi, "coil_low": coil_lo},
    )


def probe_CP2_squeeze_momentum_long(ctx: ProbeContext):
    f = ctx.features
    ema20, rsi, atr_pips = f.get("ema20"), f.get("rsi"), f.get("atr_pips")
    bb_compress = f.get("BB_compress")
    adx14 = f.get("ADX14")
    close_pos = f.get("close_pos")
    if None in (ema20, rsi, atr_pips):
        return None
    if len(ctx.m5_close) < 9:
        return None
    # Squeeze context first: prefer compressed conditions before the break.
    if bb_compress is not None and bb_compress > 0.92:
        return None
    # Momentum continuation only when the broader tape is already carrying.
    if adx14 is not None and adx14 < 18:
        return None
    if close_pos is not None and close_pos < 0.58:
        return None
    close = ctx.m5_close[-1]
    pip = pip_size(ctx.symbol)
    coil_hi = max(ctx.m5_high[-8:-1])
    coil_lo = min(ctx.m5_low[-8:-1])
    coil_range_pips = (coil_hi - coil_lo) / max(pip, 1e-9)
    # Keep it a real squeeze, not just any breakout bar.
    if coil_range_pips > max(atr_pips * 1.05, 6.0):
        return None
    if close <= coil_hi:
        return None
    if close <= ema20:
        return None
    if rsi < 56 or rsi > 78:
        return None
    # Require expanding closes through the break, not a one-tick poke.
    if ctx.m5_close[-1] <= ctx.m5_close[-2] or ctx.m5_close[-2] <= ctx.m5_close[-3]:
        return None
    if not _is_bull_bar(ctx):
        return None
    return _build_candidate_multi(
        "long", close, float(coil_lo), ctx, "CP2_squeeze_momentum_long",
        {
            "rsi": rsi,
            "BB_compress": bb_compress,
            "ADX14": adx14,
            "close_pos": close_pos,
            "coil_high": coil_hi,
            "coil_low": coil_lo,
        },
    )


# ---------------------------------------------------------------------------
# Register into shared PROBE_REGISTRY (side-effectful at import time)
# ---------------------------------------------------------------------------

_TEXTBOOK_ENTRIES: dict = {
    "TF2_pullback_EMA20_long":          {"fn": probe_TF2_pullback_EMA20_long,          "family": "direct",   "sentinel": "Charlie",       "target": 1.5},
    "TF2_pullback_EMA20_short":         {"fn": probe_TF2_pullback_EMA20_short,         "family": "direct",   "sentinel": "Charlie",       "target": 1.5},
    "TF4_sar_long":                     {"fn": probe_TF4_sar_long,                     "family": "direct",   "sentinel": "Charlie",       "target": 1.5},
    "BR2_vcb_long":                     {"fn": probe_BR2_vcb_long,                     "family": "direct",   "sentinel": "Alpha-fresh",   "target": 1.5},
    "BR2_vcb_short":                    {"fn": probe_BR2_vcb_short,                    "family": "direct",   "sentinel": "Alpha-fresh",   "target": 1.5},
    "CP3_vol_coil_fade_long":           {"fn": probe_CP3_vol_coil_fade_long,           "family": "reversal", "sentinel": "Echo-tight",    "target": 2.0},
    "CP3_vol_coil_fade_short":          {"fn": probe_CP3_vol_coil_fade_short,          "family": "reversal", "sentinel": "Echo-tight",    "target": 2.0},
    "MR5_williams_extreme_long":        {"fn": probe_MR5_williams_extreme_long,        "family": "reversal", "sentinel": "Echo-explosive", "target": 2.0},
    "MR5_williams_extreme_short":       {"fn": probe_MR5_williams_extreme_short,       "family": "reversal", "sentinel": "Echo-explosive", "target": 2.0},
    "MR4_zscore_extreme_short":         {"fn": probe_MR4_zscore_extreme_short,         "family": "reversal", "sentinel": "Echo-explosive", "target": 2.0},
    "MR4_zscore_extreme_long":          {"fn": probe_MR4_zscore_extreme_long,          "family": "reversal", "sentinel": "Echo-explosive", "target": 2.0},
    "MR2_bb_reversion_short":           {"fn": probe_MR2_bb_reversion_short,           "family": "reversal", "sentinel": "Echo-explosive", "target": 2.0},
    "RG1_range_bound_scalp_long":       {"fn": probe_RG1_range_bound_scalp_long,       "family": "reversal", "sentinel": "Echo-tight",    "target": 1.5},
    "RG1_range_bound_scalp_short":      {"fn": probe_RG1_range_bound_scalp_short,      "family": "reversal", "sentinel": "Echo-tight",    "target": 1.5},
    "RG2_range_support_bounce_long":    {"fn": probe_RG2_range_support_bounce_long,    "family": "reversal", "sentinel": "Echo-tight",    "target": 1.5},
    "BR3_inside_bar_long":              {"fn": probe_BR3_inside_bar_long,              "family": "direct",   "sentinel": "Delta",         "target": 1.5},
    "BR3_inside_bar_short":             {"fn": probe_BR3_inside_bar_short,             "family": "direct",   "sentinel": "Delta",         "target": 1.5},
    "BR5_opening_range_breakout_long":  {"fn": probe_BR5_opening_range_breakout_long,  "family": "direct",   "sentinel": "Delta",         "target": 1.5},
    "BR5_opening_range_breakout_short": {"fn": probe_BR5_opening_range_breakout_short, "family": "direct",   "sentinel": "Delta",         "target": 1.5},
    "CP1_coil_breakout_long":           {"fn": probe_CP1_coil_breakout_long,           "family": "direct",   "sentinel": "Charlie",       "target": 1.5},
    "CP1_coil_breakout_short":          {"fn": probe_CP1_coil_breakout_short,          "family": "direct",   "sentinel": "Charlie",       "target": 1.5},
    "CP2_squeeze_momentum_long":        {"fn": probe_CP2_squeeze_momentum_long,        "family": "direct",   "sentinel": "Charlie",       "target": 1.5},
}

PROBE_REGISTRY.update(_TEXTBOOK_ENTRIES)

# ---------------------------------------------------------------------------
# Public exports
# ---------------------------------------------------------------------------

_TEXTBOOK_NAMES = list(_TEXTBOOK_ENTRIES.keys())

# Pre-built list (disabled by default) — used by boot test and bootstrap.
TEXTBOOK_PROBES: list[ProbeStrategy] = [
    ProbeStrategy(name, {}) for name in _TEXTBOOK_NAMES
]


def build_all_textbook_probes(config: dict | None = None) -> list[ProbeStrategy]:
    """Return ProbeStrategy instances for all 12 textbook scalper probes.

    config shape (same section as probes_v2):
      config["TF2_pullback_EMA20_long"] = {"enabled": bool, "r_target": float}
    Missing entries → disabled.
    """
    cfg = config or {}
    return [ProbeStrategy(name, cfg.get(name, {})) for name in _TEXTBOOK_NAMES]


__all__ = ["TEXTBOOK_PROBES", "build_all_textbook_probes"]
