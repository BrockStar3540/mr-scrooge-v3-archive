"""Mr Scrooge V3 — Factor Catalog (Brock 2026-05-26).

Each factor is a numbered EXCLUSION rule. When active in a formula, trades
matching the predicate are REMOVED from the set. The goal is to find the
factor subset per cluster that maximizes filtered expectancy.

Conventions:
  - Factor IDs F01..F99
  - Each predicate is a function (row: pd.Series -> bool)
  - "True" = exclude this trade

Categories:
  F01-F19  Single-factor continuous thresholds
  F20-F29  Multi-band exclusions (out of comfort zone)
  F30-F39  Categorical exclusions
  F40-F49  Direction-bias mismatches
  F50-F59  Cost / liquidity guards
  F60-F69  Structure / proximity guards
  F70-F79  Composite / interaction rules
"""
from __future__ import annotations
import pandas as pd
import numpy as np

# Helper for safe-comparison (returns False if value is NaN/None)
def _gt(row, col, t):
    v = row.get(col)
    return v is not None and not pd.isna(v) and float(v) > t

def _lt(row, col, t):
    v = row.get(col)
    return v is not None and not pd.isna(v) and float(v) < t

def _in(row, col, s):
    v = row.get(col)
    return v in s

def _eq(row, col, v):
    return row.get(col) == v

# ------------------------------------------------------------
# FACTOR DEFINITIONS
# ------------------------------------------------------------

FACTORS: dict[str, dict] = {

    # F01-F19: single-factor continuous thresholds
    "F01": {"name": "rsi14_below_30", "predicate": lambda r: _lt(r, "rsi14", 30)},
    "F02": {"name": "rsi14_above_70", "predicate": lambda r: _gt(r, "rsi14", 70)},
    "F03": {"name": "bb_position_above_0.85", "predicate": lambda r: _gt(r, "bb_position", 0.85)},
    "F04": {"name": "bb_position_below_0.15", "predicate": lambda r: _lt(r, "bb_position", 0.15)},
    "F05": {"name": "spread_pips_above_1.5", "predicate": lambda r: _gt(r, "spread_pips", 1.5)},
    "F06": {"name": "atr_5m_below_2pips",   "predicate": lambda r: _lt(r, "atr_5m_pips", 2.0)},
    "F07": {"name": "atr_5m_above_15pips",  "predicate": lambda r: _gt(r, "atr_5m_pips", 15.0)},
    "F08": {"name": "atr_1h_below_8pips",   "predicate": lambda r: _lt(r, "atr_1h_pips", 8.0)},
    "F09": {"name": "atr_1h_above_50pips",  "predicate": lambda r: _gt(r, "atr_1h_pips", 50.0)},
    "F10": {"name": "bb_width_below_5pips", "predicate": lambda r: _lt(r, "bb_width_pips", 5.0)},
    "F11": {"name": "bb_width_above_30pips","predicate": lambda r: _gt(r, "bb_width_pips", 30.0)},
    "F12": {"name": "zscore_above_2",       "predicate": lambda r: _gt(r, "zscore", 2.0)},
    "F13": {"name": "zscore_below_neg2",    "predicate": lambda r: _lt(r, "zscore", -2.0)},
    "F14": {"name": "realized_vol_top_decile", "predicate": lambda r: _gt(r, "realized_vol", 0.0015)},
    "F15": {"name": "realized_vol_bottom_decile", "predicate": lambda r: _lt(r, "realized_vol", 0.0002)},
    "F16": {"name": "adr_consumed_above_1.0", "predicate": lambda r: _gt(r, "adr_consumed", 1.0)},
    "F17": {"name": "adr_consumed_above_0.85", "predicate": lambda r: _gt(r, "adr_consumed", 0.85)},
    "F18": {"name": "ema20_slope_flat",    "predicate": lambda r: abs(r.get("ema20_slope") or 0) < 1.0},
    "F19": {"name": "ema50_slope_flat",    "predicate": lambda r: abs(r.get("ema50_slope") or 0) < 0.5},

    # F20-F29: multi-band "out of comfort" rules (combination wrappers)
    "F20": {"name": "rsi14_extreme_either", "predicate": lambda r: _lt(r,"rsi14",30) or _gt(r,"rsi14",70)},
    "F21": {"name": "rsi14_neutral_45_55",  "predicate": lambda r: r.get("rsi14") is not None and 45 <= float(r["rsi14"]) <= 55},
    "F22": {"name": "bb_position_extreme",  "predicate": lambda r: _lt(r,"bb_position",0.1) or _gt(r,"bb_position",0.9)},
    "F23": {"name": "bb_position_middle_4060","predicate": lambda r: r.get("bb_position") is not None and 0.40 <= float(r["bb_position"]) <= 0.60},
    "F24": {"name": "atr_5m_extreme",       "predicate": lambda r: _lt(r,"atr_5m_pips",1.5) or _gt(r,"atr_5m_pips",20)},
    "F25": {"name": "spread_to_atr_high",   "predicate": lambda r: (r.get("spread_pips") and r.get("atr_5m_pips") and float(r["atr_5m_pips"]) > 0 and float(r["spread_pips"]) / float(r["atr_5m_pips"]) > 0.30)},
    "F26": {"name": "bb_width_compressed",  "predicate": lambda r: _lt(r,"bb_width_pips",6.0)},
    "F27": {"name": "range_top_decile",     "predicate": lambda r: _gt(r,"range_percentile",0.9)},
    "F28": {"name": "range_bottom_decile",  "predicate": lambda r: _lt(r,"range_percentile",0.1)},
    "F29": {"name": "pullback_too_deep",    "predicate": lambda r: _gt(r,"pullback_depth_pct",0.70)},

    # F30-F39: categorical exclusions
    "F30": {"name": "session_asia",       "predicate": lambda r: _eq(r,"session_bucket","asia")},
    "F31": {"name": "session_asia_late",  "predicate": lambda r: _eq(r,"session_bucket","asia_late")},
    "F32": {"name": "session_off_hours",  "predicate": lambda r: _eq(r,"session_bucket","off_hours")},
    "F33": {"name": "session_low_liq",    "predicate": lambda r: _in(r,"session_bucket",{"asia","asia_late","off_hours"})},
    "F34": {"name": "bb_state_extreme",   "predicate": lambda r: _in(r,"bb_state",{"EXTREME_UP","EXTREME_DOWN"})},
    "F35": {"name": "bb_state_breakout",  "predicate": lambda r: _in(r,"bb_state",{"BREAKOUT_UP","BREAKOUT_DOWN"})},
    "F36": {"name": "bb_state_stretch",   "predicate": lambda r: _in(r,"bb_state",{"STRETCH_UP","STRETCH_DOWN"})},
    "F37": {"name": "regime_blocked",     "predicate": lambda r: _eq(r,"regime_label","BLOCKED")},
    "F38": {"name": "regime_score_low",   "predicate": lambda r: _lt(r,"regime_score",-2)},
    "F39": {"name": "hour_weekend_seam",  "predicate": lambda r: _in(r,"hour_utc",{20,21,22})},

    # F40-F49: direction-bias mismatch (counter-trend filters)
    "F40": {"name": "cand_vs_htf20_mismatch",  "predicate": lambda r: r.get("direction_exec") and r.get("htf_bias_20") and r["direction_exec"] != r["htf_bias_20"]},
    "F41": {"name": "cand_vs_htf60_mismatch",  "predicate": lambda r: r.get("direction_exec") and r.get("htf_bias_60") and r["direction_exec"] != r["htf_bias_60"]},
    "F42": {"name": "cand_vs_htf120_mismatch", "predicate": lambda r: r.get("direction_exec") and r.get("htf_bias_120") and r["direction_exec"] != r["htf_bias_120"]},
    "F43": {"name": "cand_vs_trend1h_mismatch","predicate": lambda r: r.get("direction_exec") and r.get("trend_1h") and r["direction_exec"] != r["trend_1h"]},
    "F44": {"name": "cand_vs_trend4h_mismatch","predicate": lambda r: r.get("direction_exec") and r.get("trend_4h") and r["direction_exec"] != r["trend_4h"]},
    "F45": {"name": "htf_neutral_5",           "predicate": lambda r: _eq(r,"htf_bias_5","neutral")},
    "F46": {"name": "htf_neutral_20",          "predicate": lambda r: _eq(r,"htf_bias_20","neutral")},

    # F50-F59: cost / liquidity guards
    "F50": {"name": "spread_above_2pips",      "predicate": lambda r: _gt(r,"spread_pips",2.0)},
    "F51": {"name": "slice_below_7_with_buf",  "predicate": lambda r: (r.get("slice_available_pips") is not None and float(r["slice_available_pips"]) < 7.0)},
    "F52": {"name": "slice_below_10_with_buf", "predicate": lambda r: (r.get("slice_available_pips") is not None and float(r["slice_available_pips"]) < 10.0)},
    "F53": {"name": "slice_below_5_with_buf",  "predicate": lambda r: (r.get("slice_available_pips") is not None and float(r["slice_available_pips"]) < 5.0)},

    # F60-F69: structure / proximity guards
    "F60": {"name": "dist_struct_above_30",    "predicate": lambda r: _gt(r,"distance_to_structure_pips",30)},
    "F61": {"name": "dist_struct_below_5",     "predicate": lambda r: _lt(r,"distance_to_structure_pips",5)},
    "F62": {"name": "swing_high_close",        "predicate": lambda r: _lt(r,"dist_to_swing_high_pips",5)},
    "F63": {"name": "swing_low_close",         "predicate": lambda r: _lt(r,"dist_to_swing_low_pips",5)},
    "F64": {"name": "otr_above_0.5",           "predicate": lambda r: _gt(r,"otr_ratio",0.5)},

    # F70-F79: composite / interaction
    "F70": {"name": "extended_AND_neutral_htf", "predicate": lambda r: (_gt(r,"bb_position",0.85) or _lt(r,"bb_position",0.15)) and _eq(r,"htf_bias_20","neutral")},
    "F71": {"name": "compressed_AND_no_trend",  "predicate": lambda r: _lt(r,"bb_width_pips",5) and abs(r.get("ema20_slope") or 0) < 0.5},
    "F72": {"name": "high_spread_low_atr",      "predicate": lambda r: _gt(r,"spread_pips",1.5) and _lt(r,"atr_5m_pips",3)},
    "F73": {"name": "adr_used_near_end",        "predicate": lambda r: _gt(r,"adr_consumed",0.85) and _in(r,"session_bucket",{"ny_close","off_hours"})},
}

FACTOR_IDS = sorted(FACTORS.keys())   # F01, F02, ...

def factor_name(fid: str) -> str:
    return FACTORS.get(fid, {}).get("name", fid)

def factor_predicate(fid: str):
    return FACTORS.get(fid, {}).get("predicate", lambda r: False)

def applies(row, fid: str) -> bool:
    """Returns True if this factor would EXCLUDE this row."""
    try:
        return bool(factor_predicate(fid)(row))
    except Exception:
        return False

# ============================================================
# Formula serial encoding/decoding
# ============================================================
import re
_PAIR_RE = re.compile(r"[A-Z]{3}_[A-Z]{3}")

def make_serial(pair: str, regime: str, strategy: str,
                 direction: str, factor_ids: list[str],
                 session: str | None = None) -> str:
    """Build a deterministic formula serial.
       Example without session: USD_JPY-RNA-Sdbb_trend-Dlong-F03-F09-F40
       Example with session:    USD_JPY-RNA-Sdbb_trend-Dlong-Bny_open-F03-F09-F40
       Session is prefixed with 'B' (for session-Bucket)."""
    parts = [pair, f"R{regime or 'NA'}", f"S{strategy}", f"D{direction}"]
    if session is not None:
        parts.append(f"B{session or 'NA'}")
    for fid in sorted(set(factor_ids)):
        parts.append(fid)
    return "-".join(parts)

def parse_serial(serial: str) -> dict:
    parts = serial.split("-")
    pair = parts[0]
    out = {"pair": pair, "factors": [], "session": None}
    for p in parts[1:]:
        if p.startswith("R"): out["regime"] = p[1:]
        elif p.startswith("S") and not p.startswith("Sb") and len(p) > 1 and not p[1].isupper(): out["strategy"] = p[1:]
        elif p.startswith("S"): out["strategy"] = p[1:]
        elif p.startswith("D"): out["direction"] = p[1:]
        elif p.startswith("B"): out["session"] = p[1:]
        elif p.startswith("F"): out["factors"].append(p)
    return out


# ============================================================
# Filter application
# ============================================================
def apply_formula(trades_df, factor_ids: list[str]):
    """Return mask of rows to KEEP (where no factor excludes them)."""
    if not factor_ids:
        return pd.Series([True]*len(trades_df), index=trades_df.index)
    mask = pd.Series([True]*len(trades_df), index=trades_df.index)
    for fid in factor_ids:
        pred = factor_predicate(fid)
        def _safe(r):
            try:
                v = pred(r)
                return bool(v) if v is not None else False
            except Exception:
                return False
        excluded = trades_df.apply(_safe, axis=1).astype(bool)
        mask = mask & ~excluded
    return mask

def cluster_stats(trades_df, factor_ids: list[str] | None = None) -> dict:
    """Compute cluster-level metrics, optionally after applying factor exclusions."""
    if factor_ids:
        keep = apply_formula(trades_df, factor_ids)
        df = trades_df[keep]
    else:
        df = trades_df
    n = len(df)
    if n == 0:
        return {"n": 0, "wr": None, "mean_pnl_pips": None, "sum_pnl_pips": None,
                "expectancy_pips": None, "kept_pct": 0.0}
    wins = int(df["win"].sum())
    sum_pnl = float(df["pnl_pips"].sum())
    return {
        "n": n,
        "wr": wins / n,
        "mean_pnl_pips": sum_pnl / n,
        "sum_pnl_pips": sum_pnl,
        "expectancy_pips": sum_pnl / n,
        "wins": wins,
        "losses": n - wins,
        "kept_pct": n / len(trades_df) if len(trades_df) > 0 else 0.0,
    }
