"""Full 26-pair corrected re-derivation.

Same logic as lookahead_fix.py but extended to all 26 pairs. Final verdict on
whether ANY genuine edge survives look-ahead correction.
"""
import pandas as pd
import numpy as np
import json
from pathlib import Path

ROOT = Path("/tmp/scrooge-research")
PARQUET = ROOT / "raw-m5-v2" / "raw_m5_v2_candidate_events.parquet"
DUKA = ROOT / "dukascopy"
OUT = ROOT / "reports"

PAIRS = ["EUR_USD","GBP_USD","AUD_USD","NZD_USD","USD_JPY","USD_CHF","USD_CAD","USD_MXN",
         "EUR_GBP","EUR_AUD","EUR_NZD","EUR_CAD","EUR_CHF","EUR_JPY",
         "GBP_AUD","GBP_NZD","GBP_CAD","GBP_CHF","GBP_JPY",
         "AUD_CAD","AUD_CHF","AUD_JPY","AUD_NZD","CAD_JPY","CHF_JPY","NZD_JPY"]


def load_m5(pair):
    bars = []
    for f in sorted(DUKA.glob(f"{pair}_M5_*.jsonl")):
        for line in open(f):
            try:
                d = json.loads(line)
                bars.append({
                    "time": d["time"],
                    "high": (d["high_bid"]+d["high_ask"])/2,
                    "low":  (d["low_bid"]+d["low_ask"])/2,
                    "close":(d["close_bid"]+d["close_ask"])/2,
                })
            except: pass
    df = pd.DataFrame(bars)
    if df.empty: return df
    df["ts"] = pd.to_datetime(df["time"], utc=True)
    return df.sort_values("ts").reset_index(drop=True)


def corrected_context(df_m5):
    d = df_m5.set_index("ts")[["high","low","close"]]
    # M15: bars labeled by start time. close at end. Shift index to end (start+15min)
    m15 = d.resample("15min").agg({"high":"max","low":"min","close":"last"}).dropna()
    m15["ema20"] = m15["close"].ewm(span=20, adjust=False).mean()
    m15["trend"] = np.where(m15["close"] > m15["ema20"]*1.0005, "up",
                    np.where(m15["close"] < m15["ema20"]*0.9995, "down", "flat"))
    m15.index = m15.index + pd.Timedelta("15min")
    m15 = m15[["trend"]].rename(columns={"trend":"m15_trend_fixed"}).reset_index()
    h1 = d.resample("1h").agg({"high":"max","low":"min","close":"last"}).dropna()
    h1["rank"] = (h1["high"]-h1["low"]).rolling(48).rank(pct=True)
    h1["regime"] = np.where(h1["rank"] < 0.25, "consolidation",
                    np.where(h1["rank"] > 0.75, "breakout", "in_range"))
    h1.index = h1.index + pd.Timedelta("1h")
    h1 = h1[["regime"]].rename(columns={"regime":"h1_regime_fixed"}).reset_index()
    df = df_m5[["ts"]].sort_values("ts")
    df = pd.merge_asof(df, m15.sort_values("ts"), on="ts", direction="backward")
    df = pd.merge_asof(df, h1.sort_values("ts"),  on="ts", direction="backward")
    return df


print(f"Computing corrected M15/H1 labels for {len(PAIRS)} pairs ...")
fixed_parts = []
for p in PAIRS:
    print(f"  [{p}] ...", flush=True)
    m5 = load_m5(p)
    if len(m5) == 0:
        print(f"    no bars; skipping")
        continue
    fix = corrected_context(m5)
    fix["pair"] = p
    fixed_parts.append(fix)
fix_all = pd.concat(fixed_parts, ignore_index=True)
print(f"\ntotal corrected-label rows: {len(fix_all):,}")
del fixed_parts

print("\nloading v2 parquet ...")
v2 = pd.read_parquet(PARQUET)
v2["entry_ts"] = pd.to_datetime(v2["entry_ts"], utc=True)
print(f"  {len(v2):,} candidates")

fix_all = fix_all.rename(columns={"ts":"entry_ts"})
joined = v2.merge(fix_all, on=["pair","entry_ts"], how="left")
print(f"  joined: {len(joined):,}  unmatched: {joined['m15_trend_fixed'].isna().sum():,}")
del v2, fix_all

joined["era"] = np.where(joined["entry_ts"] < pd.Timestamp("2025-01-01", tz="UTC"), "discovery", "holdout")

# Label-flip stats global
print(f"\n=== LABEL FLIP RATES (all 26 pairs) ===")
mask_m15 = joined["m15_trend_fixed"].notna()
mask_h1 = joined["h1_regime_fixed"].notna()
flip_m15 = (joined.loc[mask_m15, "m15_trend"] != joined.loc[mask_m15, "m15_trend_fixed"]).mean()
flip_h1 = (joined.loc[mask_h1, "h1_regime"] != joined.loc[mask_h1, "h1_regime_fixed"]).mean()
print(f"  m15_trend flip rate: {flip_m15:.1%}")
print(f"  h1_regime flip rate: {flip_h1:.1%}")
print("\nh1_regime transition (rows orig, cols corrected, normalized by row):")
print(pd.crosstab(joined["h1_regime"], joined["h1_regime_fixed"], normalize="index").round(3))

# === Cluster under corrected labels ===
print("\n=== CLUSTERING under CORRECTED LABELS ===")
CELL = ["trigger_type","pair","direction","session_quarter","m15_trend_fixed","h1_regime_fixed"]
gp = joined.groupby(CELL + ["era"]).agg(
    n=("realized_at_2R_net","size"),
    mean_R=("realized_at_2R_net","mean"),
    win_rate=("realized_at_2R_net", lambda x: (x>0).mean()),
).reset_index()
piv = gp.pivot_table(index=CELL, columns="era", values=["n","mean_R","win_rate"]).reset_index()
piv.columns = [(f"{a}_{b}" if b else a) for a,b in piv.columns]
piv = piv.rename(columns={"n_discovery":"n_d","n_holdout":"n_h",
                          "mean_R_discovery":"mean_R_d","mean_R_holdout":"mean_R_h",
                          "win_rate_discovery":"wr_d","win_rate_holdout":"wr_h"})
print(f"  total cells: {len(piv)}")
ds = piv[(piv.n_d >= 50) & (piv.n_h >= 15) & (piv.mean_R_d > 0) & (piv.mean_R_h > 0)].copy()
print(f"  pair-grain double-survivors (n_d>=50, n_h>=15, both pos): {len(ds)}")
ds.to_csv(OUT / "corrected_26pair_survivors.csv", index=False)

# CI filter on survivors
rng = np.random.default_rng(42)
def boot_ci(arr, B=500, alpha=0.05):
    n = len(arr)
    if n < 5: return np.nan, np.nan
    idx = rng.integers(0, n, size=(B, n))
    means = arr[idx].mean(axis=1)
    return float(np.quantile(means, alpha/2)), float(np.quantile(means, 1-alpha/2))

print("\ncomputing 95% CI on corrected survivors ...")
joined["_cell"] = joined[CELL].astype(str).agg("|".join, axis=1)
ds["_cell"] = ds[CELL].astype(str).agg("|".join, axis=1)
ci_rows = []
sub_pool = joined[joined["_cell"].isin(set(ds["_cell"]))]
for cell, g in sub_pool.groupby("_cell"):
    g_d = g[g.era == "discovery"]["realized_at_2R_net"].values
    g_h = g[g.era == "holdout"]["realized_at_2R_net"].values
    if len(g_d) < 50 or len(g_h) < 15: continue
    ci_d_lo, _ = boot_ci(g_d)
    ci_h_lo, _ = boot_ci(g_h)
    ci_rows.append({"_cell": cell,
                    "n_d": len(g_d), "n_h": len(g_h),
                    "mean_R_d": float(g_d.mean()), "ci_d_lo": ci_d_lo,
                    "mean_R_h": float(g_h.mean()), "ci_h_lo": ci_h_lo,
                    "wr_h": float((g_h>0).mean())})
ci = pd.DataFrame(ci_rows).merge(ds[["_cell"] + CELL], on="_cell")
ci_pass = ci[(ci["ci_d_lo"] > 0) & (ci["ci_h_lo"] > 0)].sort_values("ci_h_lo", ascending=False)
print(f"  CI-pass (lower bound > 0 both eras): {len(ci_pass)}")
ci_pass.to_csv(OUT / "corrected_26pair_ci_pass.csv", index=False)

# Walk-forward
hold_start = pd.Timestamp("2025-01-01", tz="UTC")
hold_end = joined[joined.era == "holdout"]["entry_ts"].max()
edges = pd.date_range(hold_start, hold_end + pd.Timedelta("1d"), periods=5)
print(f"\nholdout windows: {[str(e.date()) for e in edges]}")
wf_rows = []
for cell in ci_pass["_cell"]:
    g = joined[joined["_cell"] == cell]
    means = []; ns = []
    for i in range(4):
        wg = g[(g.entry_ts >= edges[i]) & (g.entry_ts < edges[i+1])]
        means.append(float(wg["realized_at_2R_net"].mean()) if len(wg) > 0 else np.nan)
        ns.append(len(wg))
    pos = sum(1 for m in means if (not pd.isna(m)) and m > 0)
    enough = sum(1 for n in ns if n >= 5)
    wf_rows.append({"_cell": cell,
                    "w1_n": ns[0], "w1_mean": means[0],
                    "w2_n": ns[1], "w2_mean": means[1],
                    "w3_n": ns[2], "w3_mean": means[2],
                    "w4_n": ns[3], "w4_mean": means[3],
                    "windows_positive": pos, "windows_with_n5": enough})
wf = pd.DataFrame(wf_rows).merge(ci_pass[["_cell","mean_R_h","ci_h_lo","wr_h","n_h"] + CELL], on="_cell")
robust = wf[(wf["windows_positive"] >= 3) & (wf["windows_with_n5"] >= 3)].copy()
print(f"  walk-forward (>=3/4 positive): {len(robust)}")
wf.to_csv(OUT / "corrected_26pair_walk_forward.csv", index=False)

# Recent 6mo
recent_start = hold_end - pd.Timedelta(days=180)
print(f"\nrecent 6mo: {recent_start.date()} → {hold_end.date()}")
recent_rows = []
for cell in ci_pass["_cell"]:
    g = joined[(joined["_cell"] == cell) & (joined.entry_ts >= recent_start)]
    if len(g) < 5: continue
    arr = g["realized_at_2R_net"].values
    ci_lo, _ = boot_ci(arr)
    recent_rows.append({"_cell": cell, "n_recent": len(g),
                        "mean_R_recent": float(arr.mean()),
                        "ci_lo_recent": ci_lo,
                        "wr_recent": float((arr>0).mean())})
recent = pd.DataFrame(recent_rows)
final = robust.merge(recent, on="_cell", how="left")
strict = final[(final.mean_R_recent.fillna(-99) > 0) & (final.ci_lo_recent.fillna(-99) > 0)].copy()

print(f"\n=== FINAL FILTER PROGRESSION ===")
print(f"  total cells (corrected):          {len(piv):,}")
print(f"  double-survivors:                 {len(ds):,}")
print(f"  + 95% CI > 0 both eras:           {len(ci_pass):,}")
print(f"  + walk-forward >=3/4:             {len(robust):,}")
print(f"  + recent 6mo pos + CI > 0:        {len(strict):,}")

if len(strict):
    print(f"\n=== CORRECTED STRICT SURVIVORS (n={len(strict)}) ===")
    cols = CELL + ["n_h","mean_R_h","ci_h_lo","windows_positive","n_recent","mean_R_recent","ci_lo_recent","wr_recent"]
    print(strict.sort_values("ci_lo_recent", ascending=False)[cols].to_string(index=False, float_format="%.3f"))
else:
    print("\n=== ZERO CORRECTED STRICT SURVIVORS ===")
    print("v2's headline edge is fully a look-ahead artifact. No genuine deployable cell remains.")

strict.to_csv(OUT / "corrected_26pair_strict.csv", index=False)
print(f"\nsaved -> {OUT}")
