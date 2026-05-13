"""MS-001 v3: try loosened BBW to confirm the strict version is unfireable on raw M5.

If we allow BBW in [5, 30) instead of [5, 15), do we get fires?
This tests whether MS-001 strict bins are achievable from raw chart data
or whether they're inherited from probe-fired conjunction.
"""
import pandas as pd
import numpy as np
import json
from pathlib import Path
from datetime import timedelta

DUKA = Path("/data/oanda-bot-trainer-cache/dukascopy")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/microbot-raw-m5-replay-ms001")
OUT.mkdir(parents=True, exist_ok=True)
USD_BASE = ["EUR_USD","GBP_USD","AUD_USD","NZD_USD","USD_JPY","USD_CHF","USD_CAD","USD_MXN"]
DISCOVERY_END = pd.Timestamp("2025-01-01", tz="UTC")


def pip_size(pair):
    return 0.01 if pair.endswith("JPY") else 0.0001

def load_pair_m5(pair):
    bars = []
    for f in sorted(Path(DUKA / pair).glob(f"{pair}_M5_*.jsonl")):
        for line in open(f):
            try:
                d = json.loads(line)
                bars.append({"time": d["time"], "open": (d["open_bid"]+d["open_ask"])/2,
                             "high": (d["high_bid"]+d["high_ask"])/2,
                             "low":  (d["low_bid"]+d["low_ask"])/2,
                             "close":(d["close_bid"]+d["close_ask"])/2})
            except: pass
    df = pd.DataFrame(bars)
    df["ts"] = pd.to_datetime(df["time"], utc=True)
    return df.sort_values("ts").reset_index(drop=True)

def compute_indicators(df):
    c = df["close"]
    sma = c.rolling(20).mean()
    std = c.rolling(20).std(ddof=0)
    df["bb_upper"] = sma + 2*std
    df["bb_lower"] = sma - 2*std
    band_width = df["bb_upper"] - df["bb_lower"]
    df["bb_position"] = (c - df["bb_lower"]) / band_width
    df["bbw_a_bps"] = (band_width / sma) * 10000.0
    delta = c.diff()
    gain = delta.clip(lower=0).ewm(alpha=1/14, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1/14, adjust=False).mean()
    df["rsi"] = 100 - 100/(1 + gain/loss)
    df["ema20"] = c.ewm(span=20, adjust=False).mean()
    df["ema20_dist_pct"] = (c - df["ema20"]) / df["ema20"] * 10000.0
    tr = pd.concat([df["high"]-df["low"], (df["high"]-c.shift(1)).abs(), (df["low"]-c.shift(1)).abs()], axis=1).max(axis=1)
    df["atr14"] = tr.ewm(span=14, adjust=False).mean()
    rng = df["high"] - df["low"]
    df["echo_range_ratio"] = rng / rng.shift(1).rolling(20).mean()
    return df


def forward_walk_short(df, ei, ep, sd, target_R=2.0, be_threshold=None, max_hold=300):
    sl = ep + sd
    tp = ep - target_R * sd
    mfe = mae = 0.0
    be_active = False
    eff_sl = sl
    end = min(ei + max_hold, len(df) - 1)
    for i in range(ei + 1, end + 1):
        bar = df.iloc[i]
        adv = bar["high"] - ep
        fav = ep - bar["low"]
        if fav > mfe: mfe = fav
        if adv > mae: mae = adv
        if be_threshold and not be_active and mfe >= be_threshold * sd:
            be_active = True; eff_sl = ep
        if bar["high"] >= eff_sl:
            if be_active and eff_sl == ep:
                return 0.0, mfe/sd, mae/sd, i-ei, "be_stop"
            return -1.0, mfe/sd, mae/sd, i-ei, "stop"
        if bar["low"] <= tp:
            return target_R, mfe/sd, mae/sd, i-ei, "tp"
    return 0.0, mfe/sd, mae/sd, end-ei, "time"


# Filter — strict MS-001 except bbw_a_bps loosened to [5, 30)
def matches_loose(row):
    h = row["ts"].hour
    if h != 13: return False
    bb = row["bb_position"]
    if pd.isna(bb) or bb < 0.10 or bb >= 0.35: return False
    if pd.isna(row["rsi"]) or row["rsi"] < 30 or row["rsi"] >= 45: return False
    edp = abs(row["ema20_dist_pct"]) if not pd.isna(row["ema20_dist_pct"]) else None
    if edp is None or edp < 10 or edp >= 30: return False
    if pd.isna(row["bbw_a_bps"]) or row["bbw_a_bps"] < 5 or row["bbw_a_bps"] >= 30: return False  # LOOSENED
    if pd.isna(row["echo_range_ratio"]) or row["echo_range_ratio"] < 1.0 or row["echo_range_ratio"] >= 1.4: return False
    return True


print("MS-001 LOOSENED (BBW relaxed to 5-30) raw-M5 replay")
results = []
per_pair = {}
for pair in USD_BASE:
    df = load_pair_m5(pair)
    if df is None or len(df) < 100: continue
    df = compute_indicators(df)
    df["hour"] = df["ts"].dt.hour
    cand_idx = df.index[df.apply(matches_loose, axis=1)].tolist()
    print(f"[{pair}] {len(cand_idx)} candidate bars")
    per_pair[pair] = (df, cand_idx)


variants = {
    "V0_TP2R_no_BE":      (2.0, None),
    "V1_TP1.5R_no_BE":    (1.5, None),
    "V2_TP2R_BE_0.5R":    (2.0, 0.5),
    "V3_TP2R_BE_1.0R":    (2.0, 1.0),
}

print("\n=== RUNNING VARIANTS ===")
all_rows = []
for vname, (target_R, be) in variants.items():
    print(f"\n[{vname}]")
    for pair, (df, idx_list) in per_pair.items():
        for ei in idx_list:
            row = df.iloc[ei]
            ep = row["close"]
            sd = row["atr14"]
            if pd.isna(sd) or sd <= 0: continue
            r, mfe, mae, off, reason = forward_walk_short(df, ei, ep, sd, target_R, be)
            all_rows.append({
                "variant": vname, "pair": pair,
                "entry_ts": row["ts"], "entry_price": ep,
                "stop_dist_pips": sd / pip_size(pair),
                "bb_position": row["bb_position"], "rsi": row["rsi"],
                "ema20_dist_pct": row["ema20_dist_pct"],
                "bbw_a_bps": row["bbw_a_bps"],
                "echo_range_ratio": row["echo_range_ratio"],
                "realized_r": r, "mfe_r": mfe, "mae_r": mae,
                "exit_reason": reason,
            })

full = pd.DataFrame(all_rows)
if len(full):
    full["era"] = np.where(full["entry_ts"] < DISCOVERY_END, "discovery", "holdout")
    full.to_parquet(OUT / "ms001_loose_trades.parquet", index=False)
    print(f"\ntotal trades: {len(full)}")
    print(f"By variant × era:")
    summary = full.groupby(["variant", "era"]).agg(
        n=("realized_r", "size"),
        mean_r=("realized_r", "mean"),
        winner_rate=("realized_r", lambda x: (x > 0).mean()),
        clean_2r=("mfe_r", lambda x: ((x >= 2.0) & (full.loc[x.index, "mae_r"] <= 0.75)).mean()),
        full_tp_hit=("exit_reason", lambda x: (x == "tp").mean()),
        be_stop=("exit_reason", lambda x: (x == "be_stop").mean()),
        total_R=("realized_r", "sum"),
    ).reset_index()
    print(summary.to_string(index=False))
    summary.to_csv(OUT / "ms001_loose_summary.csv", index=False)
    # By pair
    print("\nBy pair × variant (V0 only):")
    bypair = full[full.variant == "V0_TP2R_no_BE"].groupby("pair").agg(
        n=("realized_r", "size"),
        clean_2r=("mfe_r", lambda x: ((x >= 2.0) & (full.loc[x.index, "mae_r"] <= 0.75)).mean()),
        mean_r=("realized_r", "mean"),
    )
    print(bypair.to_string())
else:
    print("\nNO trades — even loosened MS-001 generates nothing")
