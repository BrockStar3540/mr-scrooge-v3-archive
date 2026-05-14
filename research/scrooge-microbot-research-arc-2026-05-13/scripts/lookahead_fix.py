"""Look-ahead-corrected M15 trend + H1 regime labels.

The bug: original v2 code did
    m15 = d.resample("15min").agg(...)           # bars labeled by START time
    pd.merge_asof(df, m15, on='ts', direction='backward')
At M5 ts=09:05, this finds the m15 bar labeled '09:00' whose close is 09:14:59 —
using future data.

The fix: shift m15/h1 timestamps to bar END times. At M5 ts=09:05, merge_asof
backward finds the most recent CLOSED bar (the m15 bar ending at 09:00, which
covered 08:45-09:00:00).

This script:
  1. Reloads M5 bars for the 5 pairs in the 15-cell shortlist.
  2. Computes corrected m15_trend and h1_regime aligned to bar-end times.
  3. Joins corrected labels onto the existing v2 parquet rows for those pairs.
  4. Compares label flip rate (how often original label is wrong).
  5. Re-derives the 15-cell shortlist under corrected labels.
"""
import pandas as pd
import numpy as np
import json
from pathlib import Path

ROOT = Path("/tmp/scrooge-research")
PARQUET = ROOT / "raw-m5-v2" / "raw_m5_v2_candidate_events.parquet"
DUKA = ROOT / "dukascopy"
OUT = ROOT / "reports"

PAIRS = ["USD_JPY","USD_MXN","EUR_USD","GBP_USD","USD_CHF"]


def load_m5(pair):
    bars = []
    for f in sorted(DUKA.glob(f"{pair}_M5_*.jsonl")):
        for line in open(f):
            try:
                d = json.loads(line)
                bars.append({
                    "time": d["time"],
                    "open": (d["open_bid"]+d["open_ask"])/2,
                    "high": (d["high_bid"]+d["high_ask"])/2,
                    "low":  (d["low_bid"]+d["low_ask"])/2,
                    "close":(d["close_bid"]+d["close_ask"])/2,
                })
            except: pass
    df = pd.DataFrame(bars)
    df["ts"] = pd.to_datetime(df["time"], utc=True)
    return df.sort_values("ts").reset_index(drop=True)


def corrected_context(df_m5):
    """Compute m15_trend + h1_regime aligned to bar-END times (no look-ahead)."""
    d = df_m5.set_index("ts")[["open","high","low","close"]]

    # M15 — bars labeled by START, then we'll shift to END
    m15 = d.resample("15min").agg({"open":"first","high":"max","low":"min","close":"last"}).dropna()
    m15["ema20"] = m15["close"].ewm(span=20, adjust=False).mean()
    m15["trend"] = np.where(m15["close"] > m15["ema20"]*1.0005, "up",
                    np.where(m15["close"] < m15["ema20"]*0.9995, "down", "flat"))
    # Shift index to bar END (start + 15min). Now ts=09:00 represents the bar
    # that ran from 08:45 to 09:00 and whose close was observed at 09:00.
    m15.index = m15.index + pd.Timedelta("15min")
    m15 = m15[["trend"]].rename(columns={"trend":"m15_trend_fixed"}).reset_index()

    # H1
    h1 = d.resample("1h").agg({"open":"first","high":"max","low":"min","close":"last"}).dropna()
    h1_range = h1["high"] - h1["low"]
    h1["rank"] = h1_range.rolling(48).rank(pct=True)
    h1["regime"] = np.where(h1["rank"] < 0.25, "consolidation",
                    np.where(h1["rank"] > 0.75, "breakout", "in_range"))
    # Shift to bar END
    h1.index = h1.index + pd.Timedelta("1h")
    h1 = h1[["regime"]].rename(columns={"regime":"h1_regime_fixed"}).reset_index()

    # merge_asof backward: at M5 ts, find most recent bar where END <= ts
    df = df_m5[["ts"]].sort_values("ts")
    df = pd.merge_asof(df, m15.sort_values("ts"), on="ts", direction="backward")
    df = pd.merge_asof(df, h1.sort_values("ts"),  on="ts", direction="backward")
    return df


# Compute corrected labels per pair
print("Computing corrected M15/H1 labels for 5 pairs ...")
fixed = {}
for p in PAIRS:
    print(f"  [{p}] loading bars ...")
    m5 = load_m5(p)
    fix = corrected_context(m5)
    fix["pair"] = p
    fixed[p] = fix
    print(f"    {len(fix)} bars, m15 nulls={fix['m15_trend_fixed'].isna().sum()}, h1 nulls={fix['h1_regime_fixed'].isna().sum()}")
fix_all = pd.concat([fixed[p] for p in PAIRS], ignore_index=True)
print(f"\ntotal corrected-label rows: {len(fix_all):,}")

# Load v2 parquet, filter to 5 pairs, join corrected labels
print("\nloading v2 parquet ...")
v2 = pd.read_parquet(PARQUET)
v2["entry_ts"] = pd.to_datetime(v2["entry_ts"], utc=True)
v2_5 = v2[v2["pair"].isin(PAIRS)].copy()
del v2
print(f"v2 candidates for 5 pairs: {len(v2_5):,}")

# Join on (pair, ts)
fix_all = fix_all.rename(columns={"ts":"entry_ts"})
joined = v2_5.merge(fix_all, on=["pair","entry_ts"], how="left")
n_unmatched = joined["m15_trend_fixed"].isna().sum()
print(f"  joined with corrected labels: {len(joined):,}  (unmatched: {n_unmatched})")

# Label-flip rate
def flip_rate(col_old, col_new):
    mask = joined[col_new].notna()
    return (joined.loc[mask, col_old] != joined.loc[mask, col_new]).mean()

print(f"\n=== LABEL FLIP RATE (original vs corrected) ===")
print(f"  m15_trend flip rate: {flip_rate('m15_trend','m15_trend_fixed'):.1%}")
print(f"  h1_regime flip rate: {flip_rate('h1_regime','h1_regime_fixed'):.1%}")

# Cross-tab
print("\nm15_trend transition matrix (rows=original, cols=corrected):")
print(pd.crosstab(joined["m15_trend"], joined["m15_trend_fixed"], normalize="index").round(3))
print("\nh1_regime transition matrix (rows=original, cols=corrected):")
print(pd.crosstab(joined["h1_regime"], joined["h1_regime_fixed"], normalize="index").round(3))

# === Re-derive shortlist under corrected labels ===
print("\n=== RE-DERIVING shortlist under CORRECTED labels ===")
# Build corrected cell key
joined["_cell_fixed"] = (joined["trigger_type"]+"|"+joined["pair"]+"|"+joined["direction"]
                         +"|"+joined["session_quarter"]+"|"+joined["m15_trend_fixed"].fillna("nan")
                         +"|"+joined["h1_regime_fixed"].fillna("nan"))

# What were the 15 strict cells (under original labels)?
strict15 = pd.read_csv(OUT / "triple_gate_strict.csv")
print(f"\nOriginal 15 strict cells: {len(strict15)}")

# Per original cell, look at the corrected-label distribution of its candidates
# This tells us how the look-ahead bias was MAKING the original cell appear positive.
print("\n--- For each original-15 cell, the corrected-label breakdown of its trades ---")
strict15["_cell_orig"] = (strict15["trigger_type"]+"|"+strict15["pair"]+"|"+strict15["direction"]
                          +"|"+strict15["session_quarter"]+"|"+strict15["m15_trend"]
                          +"|"+strict15["h1_regime"])
joined["_cell_orig"] = (joined["trigger_type"]+"|"+joined["pair"]+"|"+joined["direction"]
                        +"|"+joined["session_quarter"]+"|"+joined["m15_trend"]
                        +"|"+joined["h1_regime"])
for _, c in strict15.iterrows():
    sub = joined[joined["_cell_orig"] == c["_cell_orig"]]
    if len(sub) == 0: continue
    n_total = len(sub)
    mean_r_orig = sub["realized_at_2R_net"].mean()
    # When labels match corrected, mean R there?
    same_m15 = sub[sub["m15_trend"] == sub["m15_trend_fixed"]]
    same_both = sub[(sub["m15_trend"] == sub["m15_trend_fixed"]) & (sub["h1_regime"] == sub["h1_regime_fixed"])]
    pct_same_both = len(same_both)/n_total if n_total else 0
    mean_r_same_both = same_both["realized_at_2R_net"].mean() if len(same_both) else np.nan
    print(f"\n{c['trigger_type']} | {c['pair']} | {c['direction']} | {c['session_quarter']} | M15={c['m15_trend']} | H1={c['h1_regime']}")
    print(f"  orig n={n_total}  meanR={mean_r_orig:.3f}")
    print(f"  same-labels-after-fix n={len(same_both)} ({pct_same_both:.0%})  meanR_those={mean_r_same_both:.3f}")
    # Mean R for trades that don't match the original gate after fix
    diff = sub[(sub["m15_trend"] != sub["m15_trend_fixed"]) | (sub["h1_regime"] != sub["h1_regime_fixed"])]
    if len(diff):
        print(f"  labels-changed n={len(diff)}  meanR={diff['realized_at_2R_net'].mean():.3f}")

# Now: cluster under CORRECTED labels and see which cells survive
print("\n=== CLUSTERS UNDER CORRECTED LABELS (5 pairs only) ===")
joined["era"] = np.where(joined["entry_ts"] < pd.Timestamp("2025-01-01", tz="UTC"), "discovery", "holdout")
CELL_FIXED = ["trigger_type","pair","direction","session_quarter","m15_trend_fixed","h1_regime_fixed"]
gp = joined.groupby(CELL_FIXED + ["era"]).agg(
    n=("realized_at_2R_net","size"),
    mean_R=("realized_at_2R_net","mean"),
    win_rate=("realized_at_2R_net", lambda x: (x>0).mean()),
).reset_index()
# Pivot to disc/hold
piv = gp.pivot_table(index=CELL_FIXED, columns="era", values=["n","mean_R","win_rate"]).reset_index()
piv.columns = [(f"{a}_{b}" if b else a) for a,b in piv.columns]
piv = piv.rename(columns={"n_discovery":"n_d","n_holdout":"n_h",
                          "mean_R_discovery":"mean_R_d","mean_R_holdout":"mean_R_h",
                          "win_rate_discovery":"wr_d","win_rate_holdout":"wr_h"})
ds_fixed = piv[(piv.n_d >= 50) & (piv.n_h >= 15) & (piv.mean_R_d > 0) & (piv.mean_R_h > 0)].copy()
print(f"  pair-grain double-survivors (corrected): {len(ds_fixed)}")
ds_fixed.to_csv(OUT / "corrected_pair_grain_survivors.csv", index=False)

# Top 20
print("\nTop 20 corrected cells by holdout mean R:")
cols_show = CELL_FIXED + ["n_d","mean_R_d","wr_d","n_h","mean_R_h","wr_h"]
print(ds_fixed.sort_values("mean_R_h", ascending=False)[cols_show].head(20).to_string(index=False, float_format="%.3f"))

# CI on corrected survivors
print("\ncomputing bootstrap 95% CI on corrected survivors...")
rng = np.random.default_rng(42)
def boot_ci(arr, B=500, alpha=0.05):
    n = len(arr)
    if n < 5: return np.nan, np.nan
    idx = rng.integers(0, n, size=(B, n))
    means = arr[idx].mean(axis=1)
    return float(np.quantile(means, alpha/2)), float(np.quantile(means, 1-alpha/2))

joined["_cell_fixed"] = joined[CELL_FIXED].astype(str).agg("|".join, axis=1)
ds_fixed["_cell_fixed"] = ds_fixed[CELL_FIXED].astype(str).agg("|".join, axis=1)
ci_rows = []
for cell, g in joined[joined["_cell_fixed"].isin(set(ds_fixed["_cell_fixed"]))].groupby("_cell_fixed"):
    g_d = g[g.era == "discovery"]["realized_at_2R_net"].values
    g_h = g[g.era == "holdout"]["realized_at_2R_net"].values
    if len(g_d) < 50 or len(g_h) < 15: continue
    ci_d_lo, _ = boot_ci(g_d)
    ci_h_lo, _ = boot_ci(g_h)
    ci_rows.append({"_cell_fixed": cell, "ci_d_lo": ci_d_lo, "ci_h_lo": ci_h_lo,
                    "n_d": len(g_d), "n_h": len(g_h),
                    "mean_R_d": float(g_d.mean()), "mean_R_h": float(g_h.mean()),
                    "wr_h": float((g_h>0).mean())})
ci_fixed = pd.DataFrame(ci_rows)
ci_fixed = ci_fixed.merge(ds_fixed[["_cell_fixed"] + CELL_FIXED], on="_cell_fixed")
ci_fixed_pass = ci_fixed[(ci_fixed["ci_d_lo"] > 0) & (ci_fixed["ci_h_lo"] > 0)].sort_values("ci_h_lo", ascending=False)
print(f"\n=== CORRECTED CI-PASS CELLS ===")
print(f"  pass: {len(ci_fixed_pass)} / {len(ci_fixed)}")
print("\nTop 20:")
print(ci_fixed_pass[CELL_FIXED + ["n_d","n_h","mean_R_d","ci_d_lo","mean_R_h","ci_h_lo","wr_h"]].head(20).to_string(index=False, float_format="%.3f"))
ci_fixed_pass.to_csv(OUT / "corrected_ci_pass.csv", index=False)

# Most-recent 6mo on corrected cells
hold_end = joined[joined.era=="holdout"]["entry_ts"].max()
recent_start = hold_end - pd.Timedelta(days=180)
print(f"\n=== CORRECTED + RECENT 6MO ({recent_start.date()} → {hold_end.date()}) ===")
recent_rows = []
for cell in ci_fixed_pass["_cell_fixed"]:
    g = joined[(joined["_cell_fixed"] == cell) & (joined.entry_ts >= recent_start)]
    if len(g) < 5: continue
    arr = g["realized_at_2R_net"].values
    ci_lo, _ = boot_ci(arr)
    recent_rows.append({"_cell_fixed": cell, "n_recent": len(g),
                        "mean_R_recent": float(arr.mean()),
                        "ci_lo_recent": ci_lo,
                        "wr_recent": float((arr>0).mean())})
recent_fixed = pd.DataFrame(recent_rows)
final = ci_fixed_pass.merge(recent_fixed, on="_cell_fixed")
final_strict = final[(final.mean_R_recent > 0) & (final.ci_lo_recent > 0)]
print(f"  pass corrected + recent CI > 0: {len(final_strict)}")
print(final_strict.sort_values("ci_lo_recent", ascending=False)[CELL_FIXED + ["n_h","mean_R_h","ci_h_lo","n_recent","mean_R_recent","ci_lo_recent","wr_recent"]].to_string(index=False, float_format="%.3f"))
final_strict.to_csv(OUT / "corrected_triple_gate_strict.csv", index=False)
print(f"\nsaved -> {OUT}")
