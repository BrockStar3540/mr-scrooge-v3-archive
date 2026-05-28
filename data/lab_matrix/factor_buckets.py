"""factor_buckets.py v3 — expanded RSI/BBP/ZS/ADR per Brock 2026-05-27.

v3 changes from v2:
- RSI: 6 -> 8 buckets (classical TA zones: <20, 20-30, 30-40, 40-50, 50-60, 60-70, 70-80, >80)
- BBP: 5 -> 7 buckets (adds "just-touched" zones around band edges)
- ZS:  5 -> 7 buckets (adds extreme statistical outlier zones at ±3)
- ADR: 4 -> 6 buckets (adds overshoot levels for shock-day moves)
Other factors unchanged.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Sequence


def _safe(v, default=None):
    try:
        if v is None: return default
        f = float(v)
        if f != f: return default
        return f
    except (TypeError, ValueError):
        return default


@dataclass
class Factor:
    code: str
    name: str
    description: str
    bucket_for: Callable[[dict, dict], str]
    phase: int = 1


# ============================================================================
# Phase-1 factors — v3 spec
# ============================================================================

def _bucket_BB(row, ctx):
    bb_w = _safe(row.get("bb_width_pips"))
    stop = _safe(ctx.get("stop_pips"), 7.0)
    if bb_w is None or stop is None or stop <= 0: return "BBx"
    r = bb_w / stop
    if r < 0.7:  return "BB0"
    if r < 2.0:  return "BB1"
    if r < 2.5:  return "BB2"
    return "BB3"

def _bucket_BBP(row, ctx):
    """v3: 7 buckets — split 'just outside' from 'deep outside'."""
    p = _safe(row.get("bb_position"))
    if p is None:
        upper = _safe(row.get("bb_upper_a")) or _safe(row.get("bb_upper_b"))
        lower = _safe(row.get("bb_lower_a")) or _safe(row.get("bb_lower_b"))
        price = _safe(row.get("entry_price")) or _safe(row.get("mid")) or _safe(row.get("close"))
        if upper and lower and price and upper > lower:
            p = (price - lower) / (upper - lower)
    if p is None: return "BBPx"
    if p < -0.1:   return "BBP0"   # deep below lower
    if p < 0.0:    return "BBP1"   # just touched lower
    if p < 0.33:   return "BBP2"   # lower third
    if p < 0.66:   return "BBP3"   # middle
    if p <= 1.0:   return "BBP4"   # upper third
    if p <= 1.1:   return "BBP5"   # just touched upper
    return "BBP6"                   # deep above upper

def _bucket_A5(row, ctx):
    atr = _safe(row.get("atr_5m_pips"))
    stop = _safe(ctx.get("stop_pips"), 7.0)
    if atr is None or stop is None or stop <= 0: return "A5_x"
    r = atr / stop
    if r < 0.33: return "A5_0"
    if r < 0.80: return "A5_1"
    if r < 1.20: return "A5_2"
    return "A5_3"

def _bucket_A1(row, ctx):
    atr = _safe(row.get("atr_1h_pips"))
    stop = _safe(ctx.get("stop_pips"), 7.0)
    if atr is None or stop is None or stop <= 0: return "A1_x"
    r = atr / stop
    if r < 2.0: return "A1_0"
    if r < 4.0: return "A1_1"
    if r < 8.0: return "A1_2"
    return "A1_3"

def _bucket_RSI(row, ctx):
    """v3: 8 buckets — classical TA zones.
    Accepts either lab key `rsi14` or live key `rsi` so the gate doesn't
    need to bridge naming explicitly."""
    rsi = _safe(row.get("rsi14"))
    if rsi is None:
        rsi = _safe(row.get("rsi"))
    if rsi is None: return "RSIx"
    if rsi < 20: return "RSI0"   # extreme oversold
    if rsi < 30: return "RSI1"   # oversold
    if rsi < 40: return "RSI2"   # weak
    if rsi < 50: return "RSI3"   # lower neutral
    if rsi < 60: return "RSI4"   # upper neutral
    if rsi < 70: return "RSI5"   # strong
    if rsi < 80: return "RSI6"   # overbought
    return "RSI7"                 # extreme overbought

def _bucket_E20(row, ctx):
    s = _safe(row.get("ema20_slope"))
    stop = _safe(ctx.get("stop_pips"), 7.0)
    if s is None or stop is None or stop <= 0: return "E20x"
    norm = s / stop
    if norm >= 0.50:  return "E20a"
    if norm >= 0.15:  return "E20b"
    if norm >= -0.15: return "E20c"
    if norm >= -0.50: return "E20d"
    return "E20e"

def _bucket_E50(row, ctx):
    s = _safe(row.get("ema50_slope"))
    stop = _safe(ctx.get("stop_pips"), 7.0)
    if s is None or stop is None or stop <= 0: return "E50x"
    norm = s / stop
    if norm >= 0.50:  return "E50a"
    if norm >= 0.15:  return "E50b"
    if norm >= -0.15: return "E50c"
    if norm >= -0.50: return "E50d"
    return "E50e"

def _bucket_ZS(row, ctx):
    """v3: 7 buckets — adds extreme outlier zones at ±3.
    Accepts either lab key `zscore` or live key `z_score`."""
    z = _safe(row.get("zscore"))
    if z is None:
        z = _safe(row.get("z_score"))
    if z is None: return "ZSx"
    if z < -3.0: return "ZS0"   # extreme oversold (statistical outlier)
    if z < -2.0: return "ZS1"   # deep oversold
    if z < -1.0: return "ZS2"   # oversold
    if z <= 1.0: return "ZS3"   # neutral
    if z <= 2.0: return "ZS4"   # overbought
    if z <= 3.0: return "ZS5"   # deep overbought
    return "ZS6"                 # extreme overbought

def _bucket_SPR(row, ctx):
    sp = _safe(row.get("spread_pips"))
    stop = _safe(ctx.get("stop_pips"), 7.0)
    if sp is None or stop is None or stop <= 0: return "SPRx"
    r = sp / stop
    if r < 0.10: return "SPR0"
    if r < 0.20: return "SPR1"
    if r < 0.30: return "SPR2"
    return "SPR3"

def _bucket_ADR(row, ctx):
    """v3: 6 buckets — adds overshoot levels for shock-day moves."""
    a = _safe(row.get("adr_consumed"))
    if a is None: return "ADRx"
    if a < 0.30: return "ADR0"   # fresh
    if a < 0.60: return "ADR1"   # mid
    if a < 0.90: return "ADR2"   # approaching full
    if a < 1.10: return "ADR3"   # at/near limit
    if a < 1.50: return "ADR4"   # overshooting
    return "ADR5"                 # shock day / far past normal

def _htf_align_score(row, ctx, pct_key, bias_key):
    pct = _safe(row.get(pct_key))
    direction = str(row.get("direction_exec") or row.get("direction") or ctx.get("direction", "")).lower()
    if pct is not None:
        return pct if direction == "long" else -pct
    bias = str(row.get(bias_key, "")).lower()
    bias_map = {"long": 1, "up": 1, "bull": 1, "short": -1, "down": -1, "bear": -1, "neutral": 0, "flat": 0}
    b = bias_map.get(bias)
    if b is None: return None
    return b if direction == "long" else -b

def _bucket_HTF(row, ctx, pct_key, bias_key, code):
    score = _htf_align_score(row, ctx, pct_key, bias_key)
    if score is None: return f"{code}x"
    if abs(score) >= 0.50: return f"{code}a" if score > 0 else f"{code}e"
    if score >= 0.005:  return f"{code}a"
    if score >= 0.0015: return f"{code}b"
    if score >= -0.0015: return f"{code}c"
    if score >= -0.005: return f"{code}d"
    return f"{code}e"

def _bucket_H20(row, ctx): return _bucket_HTF(row, ctx, "htf_pct_20", "htf_bias_20", "H20")
def _bucket_H60(row, ctx): return _bucket_HTF(row, ctx, "htf_pct_60", "htf_bias_60", "H60")

def _bucket_T1(row, ctx):
    # v3 fix 2026-05-28: str(None) was producing "none" which fell through
    # the alignment check and returned T1c (against-trend) on missing data.
    # Now explicit None / "none" / "" -> T1x (no-data sentinel).
    direction = str(row.get("direction_exec") or row.get("direction") or ctx.get("direction", "")).lower()
    raw = row.get("trend_1h")
    if raw is None:
        return "T1x"
    t = str(raw).lower()
    if not t or t == "none":
        return "T1x"
    if t in ("neutral", "flat"):
        return "T1b"
    aligned = (direction == "long" and t in ("long", "up", "bull")) or \
              (direction == "short" and t in ("short", "down", "bear"))
    return "T1a" if aligned else "T1c"

def _bucket_T4(row, ctx):
    # v3 fix 2026-05-28: same None->str("none") bug as T1.
    direction = str(row.get("direction_exec") or row.get("direction") or ctx.get("direction", "")).lower()
    raw = row.get("trend_4h")
    if raw is None:
        return "T4x"
    t = str(raw).lower()
    if not t or t == "none":
        return "T4x"
    if t in ("neutral", "flat"):
        return "T4b"
    aligned = (direction == "long" and t in ("long", "up", "bull")) or \
              (direction == "short" and t in ("short", "down", "bear"))
    return "T4a" if aligned else "T4c"


PHASE_1: list[Factor] = [
    Factor("BB",  "BB width / stop",                "Bollinger width relative to stop size", _bucket_BB,  1),
    Factor("BBP", "BB position",                    "Price position within Bollinger bands (7 bands)", _bucket_BBP, 1),
    Factor("A5",  "ATR 5m / stop",                  "5-minute ATR relative to stop",          _bucket_A5,  1),
    Factor("A1",  "ATR 1h / stop",                  "1-hour ATR relative to stop",            _bucket_A1,  1),
    Factor("RSI", "RSI14 (8 zones)",                "Relative Strength Index, classical TA zones", _bucket_RSI, 1),
    Factor("E20", "EMA20 slope / stop",             "EMA20 directional drift normalized",     _bucket_E20, 1),
    Factor("E50", "EMA50 slope / stop",             "EMA50 directional drift normalized",     _bucket_E50, 1),
    Factor("ZS",  "Price z-score (7 levels)",       "Standard deviations from mean incl extremes", _bucket_ZS,  1),
    Factor("SPR", "Spread / stop",                  "Spread cost relative to stop",           _bucket_SPR, 1),
    Factor("ADR", "ADR consumed (6 levels)",        "Daily range used incl overshoot",        _bucket_ADR, 1),
    Factor("H20", "HTF20 alignment",                "20-period HTF bias vs candidate dir",    _bucket_H20, 1),
    Factor("H60", "HTF60 alignment",                "60-period HTF bias vs candidate dir",    _bucket_H60, 1),
    Factor("T1",  "Trend 1h alignment",             "1h trend vs candidate direction",        _bucket_T1,  1),
    Factor("T4",  "Trend 4h alignment",             "4h trend vs candidate direction",        _bucket_T4,  1),
]

# Phase 2 unchanged from v2
def _bucket_PBD(row, ctx):
    p = _safe(row.get("pullback_depth_pct"))
    if p is None: return "PBDx"
    if p > 1.5: p = p / 100.0
    if p < 0.20: return "PBD0"
    if p < 0.40: return "PBD1"
    if p < 0.60: return "PBD2"
    if p < 0.80: return "PBD3"
    return "PBD4"

def _bucket_DST(row, ctx):
    d = _safe(row.get("distance_to_structure_pips"))
    stop = _safe(ctx.get("stop_pips"), 7.0)
    if d is None or stop is None or stop <= 0: return "DSTx"
    r = d / stop
    if r < 0.75: return "DST0"
    if r < 1.25: return "DST1"
    if r < 2.0:  return "DST2"
    if r < 3.0:  return "DST3"
    return "DST4"

def _bucket_RNG(row, ctx):
    p = _safe(row.get("range_percentile"))
    if p is None: return "RNGx"
    if p > 1.5: p = p / 100.0
    if p < 0.20: return "RNG0"
    if p < 0.40: return "RNG1"
    if p < 0.60: return "RNG2"
    if p < 0.80: return "RNG3"
    return "RNG4"

def _bucket_RVL(row, ctx):
    rv = _safe(row.get("realized_vol"))
    if rv is None: return "RVLx"
    base = _safe(ctx.get("rv_baseline"), 0.002)
    ratio = rv / base if base > 0 else None
    if ratio is None: return "RVLx"
    if ratio < 0.70: return "RVL0"
    if ratio < 0.95: return "RVL1"
    if ratio < 1.20: return "RVL2"
    if ratio < 1.60: return "RVL3"
    return "RVL4"

PHASE_2: list[Factor] = [
    Factor("PBD", "Pullback depth %",       "Retracement as fraction of prior impulse",  _bucket_PBD, 2),
    Factor("DST", "Distance to structure",  "Distance to next opposing level / stop",    _bucket_DST, 2),
    Factor("RNG", "Range percentile",       "Current range vs recent lookback rank",     _bucket_RNG, 2),
    Factor("RVL", "Realized vol normalized","Recent realized vol vs baseline",           _bucket_RVL, 2),
]

FACTORS: list[Factor] = list(PHASE_1)

def build_serial(identity, row, factors=None, stop_pips=7.0, pip_size=None, rv_baseline=0.002):
    if factors is None: factors = FACTORS
    pair = identity.get("pair", "?")
    if pip_size is None:
        pip_size = 0.01 if any(j in pair for j in ("JPY", "MXN")) else 0.0001
    ctx = {"stop_pips": stop_pips, "pip_size": pip_size, "rv_baseline": rv_baseline}
    parts = [pair, str(identity.get("strategy", "?")),
             str(identity.get("direction", "?")),
             str(identity.get("session_bucket", "?"))]
    for f in factors:
        try:
            parts.append(f.bucket_for(row, ctx))
        except Exception:
            parts.append(f"{f.code}x")
    return "|".join(parts)

def parse_serial(serial, factors=None):
    if factors is None: factors = FACTORS
    parts = serial.split("|")
    if len(parts) < 4 + len(factors):
        return {"raw": serial, "error": "too short"}
    return {
        "pair": parts[0], "strategy": parts[1], "direction": parts[2], "session_bucket": parts[3],
        "buckets": {f.code: parts[4 + i] for i, f in enumerate(factors)},
    }

__all__ = ["Factor", "PHASE_1", "PHASE_2", "FACTORS", "build_serial", "parse_serial"]
