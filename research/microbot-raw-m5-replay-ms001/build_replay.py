"""MS-001 standalone raw-M5 replay.

Per 2026-05-13 directive: build winning microbots from raw chart data.
NO inheritance from corpus probe rows. Generate candidates from M5 bars
directly using the MS-001 entry rule.

MS-001 entry rule:
  pair_family = usd_base
  direction   = short
  session     = overlap_q2 (UTC hour 13:00-13:59)
  bb_pos_bin     = lower_band   (bb_position in [0.10, 0.35))
  rsi_bin        = low          (RSI in [30, 45))
  ema20_dist_bin = ema_mid      (|ema20_dist_pct| in [10, 30))
  bbw_bin        = bbw_mid      (BB width bps in [5, 15))
  echo_ratio_bin = echo_expanded (echo_range_ratio in [1.00, 1.40))

Management variants tested:
  V0: TP=2R, stop=1×ATR (the corpus baseline; matches MS-001 promotion data)
  V1: TP=1.5R, stop=1×ATR (tighter target)
  V2: TP=2R, stop=1×ATR, BE@0.5R (early BE for shorts)
  V3: TP=2R, stop=1×ATR, BE@1.0R

Period: 2019-07 → 2026-04-22 (dukascopy coverage)
Discovery: <2025-01-01    Holdout: >=2025-01-01
"""
import pandas as pd
import numpy as np
import json
import glob
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict


DUKA = Path("/data/oanda-bot-trainer-cache/dukascopy")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/microbot-raw-m5-replay-ms001")
OUT.mkdir(parents=True, exist_ok=True)

USD_BASE = ["EUR_USD","GBP_USD","AUD_USD","NZD_USD","USD_JPY","USD_CHF","USD_CAD","USD_MXN"]

# === Bin functions — IDENTICAL to winner factory ===
def bb_bin(x):
    if pd.isna(x): return "bb_unknown"
    if x < -0.05: return "below_band"
    if x < 0.10:  return "lower_rail"
    if x < 0.35:  return "lower_band"
    if x <= 0.65: return "middle"
    if x <= 0.90: return "upper_band"
    if x <= 1.05: return "upper_rail"
    return "above_band"

def rsi_bin(x):
    if pd.isna(x): return "rsi_unknown"
    if x < 30:   return "oversold"
    if x < 45:   return "low"
    if x <= 55:  return "mid"
    if x <= 70:  return "high"
    return "overbought"

def ema_bin(x):
    if pd.isna(x): return "ema_unknown"
    ax = abs(float(x))
    if ax < 10: return "ema_near"
    if ax < 30: return "ema_mid"
    if ax < 60: return "ema_far"
    return "ema_stretched"

def bbw_bin(x):
    if pd.isna(x): return "bbw_unknown"
    if x < 5:  return "bbw_tight"
    if x < 15: return "bbw_mid"
    if x < 30: return "bbw_wide"
    return "bbw_explosive"

def echo_bin(x):
    if pd.isna(x): return "echo_unknown"
    if x < 0.70: return "echo_compressed"
    if x < 1.00: return "echo_mid"
    if x < 1.40: return "echo_expanded"
    return "echo_explosive"


def session_quarter_of(hour, minute):
    """Mimic winner factory's session_quarter."""
    minute_of_day = int(hour) * 60 + int(minute)
    h = int(hour) % 24
    if 22 <= h or h < 6:
        bucket = "asia"
    elif 6 <= h < 12:
        bucket = "london"
    elif 12 <= h < 16:
        bucket = "overlap"
    elif 16 <= h < 21:
        bucket = "ny_pm"
    else:
        bucket = "rollover"
    ranges = {"asia": (22*60, 30*60), "london": (6*60, 12*60),
              "overlap": (12*60, 16*60), "ny_pm": (16*60, 21*60), "rollover": (21*60, 22*60)}
    start, end = ranges[bucket]
    shifted = minute_of_day if bucket != "asia" else (minute_of_day + 24*60 if h < 6 else minute_of_day)
    q = min(4, max(1, int((shifted - start) // ((end - start) / 4.0)) + 1))
    return bucket, f"{bucket}_q{q}"


def pip_size(pair):
    return 0.01 if pair.endswith("JPY") else 0.0001


def load_pair_m5(pair):
    """Load all M5 bars for a pair across all years. Returns sorted DataFrame."""
    pair_dir = DUKA / pair
    if not pair_dir.exists(): return None
    bars = []
    for f in sorted(pair_dir.glob(f"{pair}_M5_*.jsonl")):
        for line in open(f):
            try:
                d = json.loads(line)
                bars.append({
                    "time": d["time"],
                    "open": (d["open_bid"] + d["open_ask"]) / 2,
                    "high": (d["high_bid"] + d["high_ask"]) / 2,
                    "low":  (d["low_bid"]  + d["low_ask"])  / 2,
                    "close":(d["close_bid"]+ d["close_ask"])/ 2,
                    "volume_bid": d.get("volume_bid", 0),
                })
            except: pass
    if not bars: return None
    df = pd.DataFrame(bars)
    df["ts"] = pd.to_datetime(df["time"], utc=True)
    df = df.sort_values("ts").reset_index(drop=True)
    return df


def compute_indicators(df):
    """Compute the same indicators the corpus does on M5 close."""
    c = df["close"]
    # Bollinger Bands (20, 2)
    sma = c.rolling(20).mean()
    std = c.rolling(20).std(ddof=0)
    df["bb_upper"] = sma + 2 * std
    df["bb_lower"] = sma - 2 * std
    df["sma_20"] = sma
    band_width = df["bb_upper"] - df["bb_lower"]
    df["bb_position"] = (c - df["bb_lower"]) / band_width
    df["bbw_a_bps"] = (band_width / sma) * 10000.0
    # RSI(14)
    delta = c.diff()
    gain = delta.clip(lower=0).ewm(alpha=1/14, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1/14, adjust=False).mean()
    rs = gain / loss
    df["rsi"] = 100 - 100 / (1 + rs)
    # EMA20 and EMA50
    df["ema20"] = c.ewm(span=20, adjust=False).mean()
    df["ema50"] = c.ewm(span=50, adjust=False).mean()
    df["ema20_dist_pct"] = (c - df["ema20"]) / df["ema20"] * 10000.0  # in bps
    # ATR(14)
    tr = pd.concat([
        df["high"] - df["low"],
        (df["high"] - c.shift(1)).abs(),
        (df["low"]  - c.shift(1)).abs(),
    ], axis=1).max(axis=1)
    df["atr14"] = tr.ewm(span=14, adjust=False).mean()
    # echo_range_ratio (current M5 range / mean of prior 20 M5 ranges)
    rng = df["high"] - df["low"]
    df["echo_range_ratio"] = rng / rng.rolling(20).mean().shift(1)
    return df


def match_ms001(row, pair):
    """Check if a bar matches MS-001 entry conditions."""
    h = row["ts"].hour
    m = row["ts"].minute
    bucket, sq = session_quarter_of(h, m)
    if sq != "overlap_q2": return False
    if bb_bin(row["bb_position"]) != "lower_band": return False
    if rsi_bin(row["rsi"]) != "low": return False
    if ema_bin(row["ema20_dist_pct"]) != "ema_mid": return False
    if bbw_bin(row["bbw_a_bps"]) != "bbw_mid": return False
    if echo_bin(row["echo_range_ratio"]) != "echo_expanded": return False
    return True


def forward_walk_short(df_pair, entry_idx, entry_price, stop_dist, target_R=2.0,
                       be_threshold=None, max_hold_bars=300):
    """Walk forward bars from entry_idx. Short trade.
    Stop = entry + stop_dist. TP = entry - target_R * stop_dist.
    Optional BE rule: if MFE reaches be_threshold * stop_dist, move stop to entry.
    Returns (realized_r, mfe_r, mae_r, exit_bar_offset, exit_reason).
    """
    pip = pip_size(df_pair.iloc[0]["time"][:6] + "_USD")  # crude — overridden by caller
    sl = entry_price + stop_dist
    tp = entry_price - target_R * stop_dist
    mfe_dist = 0.0
    mae_dist = 0.0
    be_active = False
    effective_sl = sl

    end_idx = min(entry_idx + max_hold_bars, len(df_pair) - 1)
    for i in range(entry_idx + 1, end_idx + 1):
        bar = df_pair.iloc[i]
        # For short: high is the adverse direction, low is favorable
        adv = bar["high"] - entry_price
        fav = entry_price - bar["low"]
        if fav > mfe_dist: mfe_dist = fav
        if adv > mae_dist: mae_dist = adv
        # BE rule activation
        if be_threshold is not None and not be_active and mfe_dist >= be_threshold * stop_dist:
            be_active = True
            effective_sl = entry_price  # break-even
        # Check stop
        if bar["high"] >= effective_sl:
            # Hit stop — if BE active, this is BE close; else full stop loss
            if be_active and effective_sl == entry_price:
                return 0.0, mfe_dist / stop_dist, mae_dist / stop_dist, i - entry_idx, "be_stop"
            return -1.0, mfe_dist / stop_dist, mae_dist / stop_dist, i - entry_idx, "stop"
        # Check TP
        if bar["low"] <= tp:
            return target_R, mfe_dist / stop_dist, mae_dist / stop_dist, i - entry_idx, "tp"
    return 0.0, mfe_dist / stop_dist, mae_dist / stop_dist, end_idx - entry_idx, "time"


def variant_run(df_pair, entries_idx, target_R=2.0, be_threshold=None):
    """Run all entries through forward walk for one variant. Returns DataFrame."""
    results = []
    for ei in entries_idx:
        row = df_pair.iloc[ei]
        entry_price = row["close"]
        stop_dist = row["atr14"]
        if pd.isna(stop_dist) or stop_dist <= 0:
            continue
        r, mfe, mae, exit_off, exit_reason = forward_walk_short(
            df_pair, ei, entry_price, stop_dist, target_R, be_threshold
        )
        results.append({
            "entry_ts": row["ts"], "entry_idx": ei,
            "entry_price": entry_price, "stop_dist": stop_dist,
            "atr14": row["atr14"], "bb_position": row["bb_position"],
            "rsi": row["rsi"], "ema20_dist_pct": row["ema20_dist_pct"],
            "bbw_a_bps": row["bbw_a_bps"], "echo_range_ratio": row["echo_range_ratio"],
            "realized_r": r, "mfe_r": mfe, "mae_r": mae,
            "exit_offset_bars": exit_off, "exit_reason": exit_reason,
        })
    return pd.DataFrame(results)


# === MAIN ===
print("MS-001 raw-M5 replay starting ...")
print(f"USD-base pairs: {USD_BASE}")
DISCOVERY_END = pd.Timestamp("2025-01-01", tz="UTC")

all_entries_per_pair = {}
for pair in USD_BASE:
    print(f"\n[{pair}] loading M5 bars ...")
    df = load_pair_m5(pair)
    if df is None or len(df) < 100:
        print(f"  no data")
        continue
    print(f"  loaded {len(df):,} bars, range {df['ts'].min()} → {df['ts'].max()}")
    df = compute_indicators(df)
    # Only consider bars in overlap_q2 (UTC hour 13)
    df["hour"] = df["ts"].dt.hour
    overlap_q2 = df[(df["hour"] == 13)].copy()
    print(f"  bars in UTC hour 13 (overlap_q2): {len(overlap_q2):,}")
    # Apply full MS-001 filter
    overlap_q2["match"] = overlap_q2.apply(lambda r: match_ms001(r, pair), axis=1)
    matches = overlap_q2[overlap_q2["match"]].index.tolist()
    print(f"  MS-001 matches: {len(matches)}")
    all_entries_per_pair[pair] = (df, matches)


# Aggregate variants
print("\n=== RUNNING VARIANTS ===")
variants = {
    "V0_TP2R_no_BE":        {"target_R": 2.0, "be_threshold": None},
    "V1_TP1.5R_no_BE":      {"target_R": 1.5, "be_threshold": None},
    "V2_TP2R_BE_at_0.5R":   {"target_R": 2.0, "be_threshold": 0.5},
    "V3_TP2R_BE_at_1.0R":   {"target_R": 2.0, "be_threshold": 1.0},
}

all_results = []
for vname, vparams in variants.items():
    print(f"\n--- variant: {vname} ---")
    var_rows = []
    for pair, (df, idx_list) in all_entries_per_pair.items():
        if not idx_list: continue
        df_res = variant_run(df, idx_list, **vparams)
        df_res["pair"] = pair
        var_rows.append(df_res)
    if not var_rows:
        continue
    var_df = pd.concat(var_rows, ignore_index=True)
    var_df["variant"] = vname
    var_df["era"] = np.where(var_df["entry_ts"] < DISCOVERY_END, "discovery", "holdout")
    all_results.append(var_df)
    # Summary
    print(f"  total entries: {len(var_df)}")
    print(f"  by era:    {var_df['era'].value_counts().to_dict()}")
    print(f"  by pair:   {var_df['pair'].value_counts().to_dict()}")
    print(f"  total R: {var_df['realized_r'].sum():.2f}, mean: {var_df['realized_r'].mean():.3f}")
    for era in ["discovery", "holdout"]:
        sub = var_df[var_df["era"] == era]
        if len(sub) == 0: continue
        full_win = (sub["realized_r"] >= 1.9).sum()
        be = (sub["realized_r"] == 0).sum() if vparams["be_threshold"] else 0
        clean_2r = ((sub["mfe_r"] >= 2.0) & (sub["mae_r"] <= 0.75)).sum()
        print(f"  [{era}] n={len(sub)}, clean_2R_rate={clean_2r/len(sub)*100:.1f}%, full_TP_hits={full_win}, mean_R={sub['realized_r'].mean():+.3f}")


if all_results:
    full = pd.concat(all_results, ignore_index=True)
    full.to_parquet(OUT / "ms001_trades.parquet", index=False)
    full.to_csv(OUT / "ms001_trades.csv", index=False)
    print(f"\nsaved {OUT}/ms001_trades.parquet ({len(full)} rows)")

    # Per-variant per-era summary
    summary = full.groupby(["variant", "era"]).agg(
        n=("realized_r", "size"),
        total_R=("realized_r", "sum"),
        mean_R=("realized_r", "mean"),
        winner_rate=("realized_r", lambda x: (x > 0).mean()),
        full_2r_rate=("mfe_r", lambda x: (x >= 2.0).mean()),
        clean_2r_rate=("mfe_r", lambda x: ((x >= 2.0) & (full.loc[x.index, "mae_r"] <= 0.75)).mean()),
    ).reset_index()
    summary.to_csv(OUT / "variant_era_summary.csv", index=False)
    print("\n=== VARIANT × ERA SUMMARY ===")
    print(summary.to_string(index=False))
else:
    print("\nNO RESULTS — no matches in any pair")
