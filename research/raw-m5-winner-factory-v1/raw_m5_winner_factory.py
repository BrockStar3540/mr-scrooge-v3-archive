"""Raw-M5 Winner Factory v1.

Per 2026-05-13 Option A: generate raw-chart candidate events (no probe filter),
forward-walk every candidate, cluster winners.

Pair scope (v1): 8 USD-base pairs.
  EUR_USD GBP_USD AUD_USD NZD_USD USD_JPY USD_CHF USD_CAD USD_MXN

Period: dukascopy M5 2019-07-01 → 2026-04-22 per pair.
Discovery: entry_ts < 2025-01-01    Holdout: >= 2025-01-01

Triggers (6 implemented in v1, more queued for v2):
  T1_bb_lower_reclaim   (long)  prev low <= bb_lower; current close > bb_lower
  T2_bb_upper_reject    (short) prev high >= bb_upper; current close < bb_upper
  T3_band_reentry_long  (long)  prev close < bb_lower; current close > bb_lower
  T4_band_reentry_short (short) prev close > bb_upper; current close < bb_upper
  T5_ema20_reclaim_long (long)  prev close < ema20 - delta; current close > ema20
  T6_ema20_reject_short (short) prev close > ema20 + delta; current close < ema20

Forward-walk: 1×ATR stop, multi-target (1R, 1.5R, 2R), max 300 bars (25h).
Outcome record per candidate: realized_r at each target, mfe_r, mae_r,
gave_back_green flag, clean_stop flag.
"""
import pandas as pd
import numpy as np
import json
from pathlib import Path
from datetime import datetime, timezone

DUKA = Path("/data/oanda-bot-trainer-cache/dukascopy")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/raw-m5-winner-factory-v1")
OUT.mkdir(parents=True, exist_ok=True)

USD_BASE = ["EUR_USD","GBP_USD","AUD_USD","NZD_USD","USD_JPY","USD_CHF","USD_CAD","USD_MXN"]
DISCOVERY_END = pd.Timestamp("2025-01-01", tz="UTC")
MAX_HOLD_BARS = 300  # 25 hours


def pip_size(pair):
    return 0.01 if pair.endswith("JPY") else 0.0001


def load_pair_m5(pair):
    bars = []
    for f in sorted(Path(DUKA / pair).glob(f"{pair}_M5_*.jsonl")):
        for line in open(f):
            try:
                d = json.loads(line)
                bars.append({
                    "time": d["time"],
                    "open": (d["open_bid"] + d["open_ask"]) / 2,
                    "high": (d["high_bid"] + d["high_ask"]) / 2,
                    "low":  (d["low_bid"]  + d["low_ask"])  / 2,
                    "close":(d["close_bid"]+ d["close_ask"])/ 2,
                })
            except: pass
    df = pd.DataFrame(bars)
    df["ts"] = pd.to_datetime(df["time"], utc=True)
    return df.sort_values("ts").reset_index(drop=True)


def compute_indicators(df):
    c = df["close"]
    h = df["high"]
    l = df["low"]
    # BB
    sma = c.rolling(20).mean()
    std = c.rolling(20).std(ddof=0)
    df["bb_upper"] = sma + 2 * std
    df["bb_lower"] = sma - 2 * std
    df["sma_20"] = sma
    band_width = df["bb_upper"] - df["bb_lower"]
    df["bb_position"] = (c - df["bb_lower"]) / band_width
    df["bbw_a_bps"] = (band_width / sma) * 10000.0
    # RSI
    delta = c.diff()
    gain = delta.clip(lower=0).ewm(alpha=1/14, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1/14, adjust=False).mean()
    df["rsi"] = 100 - 100/(1 + gain/loss)
    # EMAs
    df["ema20"] = c.ewm(span=20, adjust=False).mean()
    df["ema50"] = c.ewm(span=50, adjust=False).mean()
    df["ema20_dist_bps"] = (c - df["ema20"]) / df["ema20"] * 10000.0
    df["ema50_dist_bps"] = (c - df["ema50"]) / df["ema50"] * 10000.0
    # ATR
    tr = pd.concat([h-l, (h-c.shift(1)).abs(), (l-c.shift(1)).abs()], axis=1).max(axis=1)
    df["atr14"] = tr.ewm(span=14, adjust=False).mean()
    # echo
    rng = h - l
    df["echo_range_ratio"] = rng / rng.shift(1).rolling(20).mean()
    # prior bars for trigger detection
    df["prev_high"] = h.shift(1)
    df["prev_low"] = l.shift(1)
    df["prev_close"] = c.shift(1)
    return df


def detect_triggers(df):
    """Vectorized trigger detection. Returns DataFrame of (idx, trigger_type, direction)."""
    triggers = []
    # T1: BB lower band reclaim (long)
    m = (df["prev_low"] <= df["bb_lower"].shift(1)) & (df["close"] > df["bb_lower"])
    for i in df.index[m]:
        triggers.append((i, "T1_bb_lower_reclaim", "long"))
    # T2: BB upper band reject (short)
    m = (df["prev_high"] >= df["bb_upper"].shift(1)) & (df["close"] < df["bb_upper"])
    for i in df.index[m]:
        triggers.append((i, "T2_bb_upper_reject", "short"))
    # T3: prev close was outside lower band, current close back inside
    m = (df["prev_close"] < df["bb_lower"].shift(1)) & (df["close"] > df["bb_lower"])
    for i in df.index[m]:
        triggers.append((i, "T3_band_reentry_long", "long"))
    # T4: prev close was outside upper band, current close back inside
    m = (df["prev_close"] > df["bb_upper"].shift(1)) & (df["close"] < df["bb_upper"])
    for i in df.index[m]:
        triggers.append((i, "T4_band_reentry_short", "short"))
    # T5: EMA20 reclaim — prev close below EMA20 - 5bps, current close above EMA20
    delta = df["ema20"] * 0.0005  # 5bps
    m = (df["prev_close"] < (df["ema20"].shift(1) - delta.shift(1))) & (df["close"] > df["ema20"])
    for i in df.index[m]:
        triggers.append((i, "T5_ema20_reclaim_long", "long"))
    # T6: EMA20 reject — prev close above EMA20 + 5bps, current close below EMA20
    m = (df["prev_close"] > (df["ema20"].shift(1) + delta.shift(1))) & (df["close"] < df["ema20"])
    for i in df.index[m]:
        triggers.append((i, "T6_ema20_reject_short", "short"))
    return triggers


def session_quarter_of(hour, minute):
    minute_of_day = int(hour) * 60 + int(minute)
    h = int(hour) % 24
    if 22 <= h or h < 6:
        bucket = "asia"
        shifted = minute_of_day + (24*60 if h < 6 else 0)
        start, end = 22*60, 30*60
    elif 6 <= h < 12:
        bucket = "london"; shifted = minute_of_day
        start, end = 6*60, 12*60
    elif 12 <= h < 16:
        bucket = "overlap"; shifted = minute_of_day
        start, end = 12*60, 16*60
    elif 16 <= h < 21:
        bucket = "ny_pm"; shifted = minute_of_day
        start, end = 16*60, 21*60
    else:
        bucket = "rollover"; shifted = minute_of_day
        start, end = 21*60, 22*60
    q = min(4, max(1, int((shifted - start) // ((end - start) / 4.0)) + 1))
    return bucket, f"{bucket}_q{q}"


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


def forward_walk(df, ei, ep, sd, direction, max_hold=MAX_HOLD_BARS):
    """Return (realized_at_1R, realized_at_1_5R, realized_at_2R, mfe_r, mae_r, exit_reason, exit_bars)."""
    end = min(ei + max_hold, len(df) - 1)
    mfe = mae = 0.0
    for i in range(ei + 1, end + 1):
        bar_h = df["high"].iloc[i]
        bar_l = df["low"].iloc[i]
        if direction == "long":
            adv = ep - bar_l
            fav = bar_h - ep
            sl = ep - sd
            adverse_hit = bar_l <= sl
            tp_2r_hit = bar_h >= ep + 2*sd
        else:
            adv = bar_h - ep
            fav = ep - bar_l
            sl = ep + sd
            adverse_hit = bar_h >= sl
            tp_2r_hit = bar_l <= ep - 2*sd
        if fav > mfe: mfe = fav
        if adv > mae: mae = adv
        if adverse_hit:
            mfe_r = mfe / sd
            mae_r = mae / sd
            # outcomes at each target
            r_1r = 1.0 if mfe_r >= 1.0 else -1.0
            r_15r = 1.5 if mfe_r >= 1.5 else -1.0
            r_2r = 2.0 if mfe_r >= 2.0 else -1.0
            return r_1r, r_15r, r_2r, mfe_r, mae_r, "stop", i - ei
        if tp_2r_hit:
            return 1.0, 1.5, 2.0, 2.0, mae/sd, "tp_2r", i - ei
    mfe_r = mfe / sd if sd > 0 else 0
    mae_r = mae / sd if sd > 0 else 0
    r_1r = 1.0 if mfe_r >= 1.0 else 0.0
    r_15r = 1.5 if mfe_r >= 1.5 else 0.0
    r_2r = 2.0 if mfe_r >= 2.0 else 0.0
    return r_1r, r_15r, r_2r, mfe_r, mae_r, "time", end - ei


PAIR_FAMILY = {p: "usd_base" for p in USD_BASE}


print("Raw-M5 Winner Factory v1 starting ...")
print(f"Pair scope: {USD_BASE}")
all_candidates = []

for pair in USD_BASE:
    print(f"\n[{pair}] loading + computing ...")
    df = load_pair_m5(pair)
    if df is None or len(df) < 100:
        print(f"  skip (no data)")
        continue
    df = compute_indicators(df)
    triggers = detect_triggers(df)
    print(f"  total trigger candidates: {len(triggers)}")
    if not triggers:
        continue

    rows = []
    for ei, trigger_type, direction in triggers:
        row = df.iloc[ei]
        ep = row["close"]
        sd = row["atr14"]
        if pd.isna(sd) or sd <= 0: continue
        ts = row["ts"]
        bucket, sq = session_quarter_of(ts.hour, ts.minute)
        r_1r, r_15r, r_2r, mfe_r, mae_r, exit_reason, exit_bars = forward_walk(df, ei, ep, sd, direction)
        rows.append({
            "pair": pair, "pair_family": PAIR_FAMILY[pair],
            "entry_ts": ts, "direction": direction,
            "trigger_type": trigger_type,
            "session_bucket": bucket, "session_quarter": sq,
            "entry_price": ep, "atr14": sd,
            "stop_pips": sd / pip_size(pair),
            "bb_position": row["bb_position"], "bb_pos_bin": bb_bin(row["bb_position"]),
            "rsi": row["rsi"], "rsi_bin": rsi_bin(row["rsi"]),
            "ema20_dist_bps": row["ema20_dist_bps"], "ema20_dist_bin": ema_bin(row["ema20_dist_bps"]),
            "ema50_dist_bps": row["ema50_dist_bps"],
            "bbw_a_bps": row["bbw_a_bps"], "bbw_bin": bbw_bin(row["bbw_a_bps"]),
            "echo_range_ratio": row["echo_range_ratio"], "echo_ratio_bin": echo_bin(row["echo_range_ratio"]),
            "realized_at_1R": r_1r, "realized_at_1_5R": r_15r, "realized_at_2R": r_2r,
            "mfe_r": mfe_r, "mae_r": mae_r,
            "exit_reason": exit_reason, "exit_bars": exit_bars,
            "gave_back_green": (mfe_r > 0.5) and (r_2r <= 0),
            "clean_stop": (mae_r >= 0.95) and (mfe_r < 0.25),
            "clean_2r": (mfe_r >= 2.0) and (mae_r <= 0.75),
        })
    pair_df = pd.DataFrame(rows)
    print(f"  candidates with outcomes: {len(pair_df)}")
    if len(pair_df):
        print(f"  clean_2r rate: {pair_df['clean_2r'].mean()*100:.1f}%, mean_R@2: {pair_df['realized_at_2R'].mean():+.3f}")
    all_candidates.append(pair_df)


if not all_candidates:
    print("\nNO candidates generated")
else:
    full = pd.concat(all_candidates, ignore_index=True)
    full["era"] = np.where(full["entry_ts"] < DISCOVERY_END, "discovery", "holdout")
    full.to_parquet(OUT / "raw_m5_candidate_events.parquet", index=False)
    print(f"\n=== TOTAL CANDIDATES: {len(full):,} ===")
    print(f"by era: {full['era'].value_counts().to_dict()}")
    print(f"by trigger:")
    print(full["trigger_type"].value_counts().to_string())
    print(f"by direction: {full['direction'].value_counts().to_dict()}")

    # === CLUSTER WINNERS ===
    print("\nclustering winners...")
    CELL = ["trigger_type", "pair_family", "direction", "session_quarter",
            "bb_pos_bin", "rsi_bin", "ema20_dist_bin", "bbw_bin", "echo_ratio_bin"]

    cells = full.groupby(CELL).agg(
        n=("entry_ts", "size"),
        clean_2r_rate=("clean_2r", "mean"),
        mfe_r_median=("mfe_r", "median"),
        mae_r_median=("mae_r", "median"),
        gave_back_rate=("gave_back_green", "mean"),
        clean_stop_rate=("clean_stop", "mean"),
        winner_rate_1r=("realized_at_1R", lambda x: (x > 0).mean()),
        winner_rate_2r=("realized_at_2R", lambda x: (x > 0).mean()),
        total_R_2r=("realized_at_2R", "sum"),
        mean_R_2r=("realized_at_2R", "mean"),
    ).reset_index()

    # Discovery-only cells
    disc_cells = full[full["era"] == "discovery"].groupby(CELL).agg(
        n_discovery=("entry_ts", "size"),
        clean_2r_rate_discovery=("clean_2r", "mean"),
        winner_rate_2r_discovery=("realized_at_2R", lambda x: (x > 0).mean()),
        mean_R_2r_discovery=("realized_at_2R", "mean"),
    ).reset_index()

    hold_cells = full[full["era"] == "holdout"].groupby(CELL).agg(
        n_holdout=("entry_ts", "size"),
        clean_2r_rate_holdout=("clean_2r", "mean"),
        winner_rate_2r_holdout=("realized_at_2R", lambda x: (x > 0).mean()),
        mean_R_2r_holdout=("realized_at_2R", "mean"),
    ).reset_index()

    cells_full = cells.merge(disc_cells, on=CELL, how="left").merge(hold_cells, on=CELL, how="left")
    cells_full.to_csv(OUT / "raw_m5_winner_clusters.csv", index=False)
    print(f"  cells: {len(cells_full)}")

    # Filter to PROMISING cells: discovery n >= 50, clean_2r >= 0.40, holdout n >= 20
    promising = cells_full[
        (cells_full["n_discovery"] >= 50) &
        (cells_full["clean_2r_rate_discovery"] >= 0.40) &
        (cells_full["n_holdout"] >= 20) &
        (cells_full["clean_2r_rate_holdout"] >= 0.30)
    ].sort_values("mean_R_2r_discovery", ascending=False)
    print(f"\n  promising cells (disc n>=50 + clean_2r>=40% + hold n>=20 + hold clean_2r>=30%): {len(promising)}")
    promising.to_csv(OUT / "raw_m5_microstrategy_candidates.csv", index=False)

    if len(promising):
        print("\n=== TOP 15 PROMISING CELLS ===")
        cols_view = ["trigger_type","pair_family","direction","session_quarter",
                     "bb_pos_bin","rsi_bin","ema20_dist_bin","bbw_bin","echo_ratio_bin",
                     "n_discovery","clean_2r_rate_discovery","mean_R_2r_discovery",
                     "n_holdout","clean_2r_rate_holdout","mean_R_2r_holdout"]
        print(promising[cols_view].head(15).to_string(index=False))

    print(f"\nsaved {OUT}")
