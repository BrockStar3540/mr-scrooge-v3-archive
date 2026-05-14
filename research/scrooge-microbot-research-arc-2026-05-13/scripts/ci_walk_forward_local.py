"""CI filter + walk-forward — Mini-local version.

Runs on the v2 parquet pulled to Mini. Outputs CSVs to /tmp/scrooge-research/reports/.
"""
import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path("/tmp/scrooge-research")
PARQUET = ROOT / "raw-m5-v2" / "raw_m5_v2_candidate_events.parquet"
PAIR_CSV = ROOT / "raw-m5-v2" / "raw_m5_v2_clusters_pair_grain.csv"
OUT = ROOT / "reports"
OUT.mkdir(parents=True, exist_ok=True)

print("loading parquet ...")
df = pd.read_parquet(PARQUET)
df["entry_ts"] = pd.to_datetime(df["entry_ts"], utc=True)
print(f"loaded {len(df):,} rows  |  mem: ~{df.memory_usage(deep=True).sum()/1e9:.2f} GB")

CELL = ["trigger_type","pair","direction","session_quarter","m15_trend","h1_regime"]

pair_clusters = pd.read_csv(PAIR_CSV)
ds = pair_clusters[(pair_clusters.n_disc >= 50) & (pair_clusters.n_hold >= 15) &
                   (pair_clusters.mean_R_2r_disc > 0) & (pair_clusters.mean_R_2r_hold > 0)].copy()
print(f"pair-grain double-survivor cells: {len(ds)}")

df["_cell"] = df[CELL].astype(str).agg("|".join, axis=1)
ds["_cell"] = ds[CELL].astype(str).agg("|".join, axis=1)
df_cells = df[df["_cell"].isin(set(ds["_cell"]))].copy()
print(f"candidates inside survivor cells: {len(df_cells):,}")

# free the giant df we no longer need
del df

# === Bootstrap CI ===
print("\ncomputing bootstrap 95% CI (500 resamples)...")
rng = np.random.default_rng(42)
B = 500

def boot_ci(arr, B=500, alpha=0.05):
    n = len(arr)
    if n < 5: return np.nan, np.nan
    idx = rng.integers(0, n, size=(B, n))
    means = arr[idx].mean(axis=1)
    return float(np.quantile(means, alpha/2)), float(np.quantile(means, 1-alpha/2))

ci_rows = []
groups = list(df_cells.groupby("_cell"))
print(f"  {len(groups)} groups to bootstrap ...")
for i, (cell, g) in enumerate(groups):
    g_d = g[g.era == "discovery"]["realized_at_2R_net"].values
    g_h = g[g.era == "holdout"]["realized_at_2R_net"].values
    if len(g_d) < 50 or len(g_h) < 15: continue
    ci_d_lo, ci_d_hi = boot_ci(g_d)
    ci_h_lo, ci_h_hi = boot_ci(g_h)
    ci_rows.append({
        "_cell": cell, "n_d": len(g_d), "n_h": len(g_h),
        "mean_R_d": float(g_d.mean()), "ci_d_lo": ci_d_lo, "ci_d_hi": ci_d_hi,
        "mean_R_h": float(g_h.mean()), "ci_h_lo": ci_h_lo, "ci_h_hi": ci_h_hi,
        "win_rate_d": float((g_d > 0).mean()),
        "win_rate_h": float((g_h > 0).mean()),
    })
    if (i+1) % 100 == 0: print(f"   ... {i+1}/{len(groups)}")

ci_df = pd.DataFrame(ci_rows)
desc = ds[["_cell"] + CELL].drop_duplicates("_cell")
ci_df = ci_df.merge(desc, on="_cell")
ci_df.to_csv(OUT / "ci_per_cell.csv", index=False)

ci_pass = ci_df[(ci_df["ci_d_lo"] > 0) & (ci_df["ci_h_lo"] > 0)].sort_values("ci_h_lo", ascending=False)
print(f"\n=== CI FILTER (lower bound of 95% CI > 0 in BOTH eras) ===")
print(f"  cells passing: {len(ci_pass)} / {len(ci_df)}")
print(f"\nTop 20:")
print(ci_pass[CELL + ["n_d","n_h","mean_R_d","ci_d_lo","mean_R_h","ci_h_lo","win_rate_h"]].head(20).to_string(index=False, float_format="%.3f"))

# === Walk-forward on holdout (4 windows) ===
hold_start = pd.Timestamp("2025-01-01", tz="UTC")
hold_end   = df_cells[df_cells.era == "holdout"]["entry_ts"].max()
print(f"\nholdout range: {hold_start.date()} to {hold_end.date()}")
window_edges = pd.date_range(hold_start, hold_end + pd.Timedelta("1d"), periods=5)
print(f"window edges: {[str(e.date()) for e in window_edges]}")

wf_rows = []
for cell in ci_pass["_cell"]:
    g = df_cells[df_cells["_cell"] == cell]
    means = []; ns = []
    for i in range(4):
        wg = g[(g.entry_ts >= window_edges[i]) & (g.entry_ts < window_edges[i+1])]
        means.append(float(wg["realized_at_2R_net"].mean()) if len(wg) > 0 else np.nan)
        ns.append(len(wg))
    pos_w = sum(1 for m in means if (not pd.isna(m)) and m > 0)
    enough_n = sum(1 for n in ns if n >= 5)
    wf_rows.append({
        "_cell": cell,
        "w1_n": ns[0], "w1_mean": means[0],
        "w2_n": ns[1], "w2_mean": means[1],
        "w3_n": ns[2], "w3_mean": means[2],
        "w4_n": ns[3], "w4_mean": means[3],
        "windows_positive": pos_w,
        "windows_with_n5": enough_n,
    })
wf_df = pd.DataFrame(wf_rows).merge(desc, on="_cell")
wf_df.to_csv(OUT / "walk_forward.csv", index=False)

robust = wf_df[(wf_df["windows_positive"] >= 3) & (wf_df["windows_with_n5"] >= 3)].copy()
print(f"\n=== WALK-FORWARD (positive R in >=3 of 4 holdout windows, n>=5 in 3+ windows) ===")
print(f"  cells passing: {len(robust)} / {len(ci_pass)}")
robust = robust.merge(ci_pass[["_cell","mean_R_h","ci_h_lo","win_rate_h","n_h"]], on="_cell")
print(robust.sort_values("ci_h_lo", ascending=False)[CELL + ["n_h","mean_R_h","ci_h_lo","windows_positive","w1_mean","w2_mean","w3_mean","w4_mean"]].head(20).to_string(index=False, float_format="%.3f"))

# === Most-recent 6mo ===
recent_start = hold_end - pd.Timedelta(days=180)
print(f"\n=== RECENT 6MO ({recent_start.date()} to {hold_end.date()}) ===")
recent_rows = []
for cell in ci_pass["_cell"]:
    g = df_cells[(df_cells["_cell"] == cell) & (df_cells.entry_ts >= recent_start)]
    if len(g) < 5: continue
    arr = g["realized_at_2R_net"].values
    ci_lo, ci_hi = boot_ci(arr)
    recent_rows.append({
        "_cell": cell, "n_recent": len(g),
        "mean_R_recent": float(arr.mean()),
        "ci_lo_recent": ci_lo,
        "win_rate_recent": float((arr > 0).mean()),
    })
recent_df = pd.DataFrame(recent_rows).merge(desc, on="_cell")
recent_df.to_csv(OUT / "recent_6mo.csv", index=False)

triple = robust.merge(recent_df[["_cell","n_recent","mean_R_recent","ci_lo_recent","win_rate_recent"]], on="_cell")
triple_pos = triple[triple["mean_R_recent"] > 0].copy()
triple_strict = triple_pos[triple_pos["ci_lo_recent"] > 0].copy()

print(f"\n=== TRIPLE GATE ===")
print(f"  CI-pass:                     {len(ci_pass)}")
print(f"  + walk-forward >=3/4:        {len(robust)}")
print(f"  + recent 6mo mean > 0:       {len(triple_pos)}")
print(f"  + recent 6mo CI lower > 0:   {len(triple_strict)}")

print(f"\nTop triple-strict survivors (sorted by recent CI lower bound):")
cols = CELL + ["n_h","mean_R_h","ci_h_lo","windows_positive","n_recent","mean_R_recent","ci_lo_recent","win_rate_recent"]
print(triple_strict.sort_values("ci_lo_recent", ascending=False)[cols].to_string(index=False, float_format="%.3f"))

triple_pos.to_csv(OUT / "triple_gate_positive.csv", index=False)
triple_strict.to_csv(OUT / "triple_gate_strict.csv", index=False)
print(f"\nsaved -> {OUT}")
