"""Test 1: 47-factor winner vs loser analysis.

For each (strategy_id, pair, direction) with n_winners >= 100 AND n_losers >= 100:
  - Compute factor values at entry for every trade (already in foundational
    parquet for ~10 factors; compute the rest from dukascopy if needed)
  - Mean / median / std of factor per winner-set vs loser-set
  - Cohen's d effect size
  - KS test p-value
  - Rank factors by |Cohen's d| for each cell

Output: per-cell top-N factors that distinguish winners from losers.

Step 1 (this script): use ONLY the factors already in the foundational parquet.
That's enough to find the biggest differentiators without recomputing.

Foundational parquet already has these factor-like columns:
  ADX14, ATR_ratio, BB_compress, RSI14, price_pos, volume_ratio,
  hour_utc, session_bucket, technical_regime_53
Plus derived from entry_ts: weekday, minute_of_day.
Plus trade outcome features (mfe_R, mae_R) — these are POST-entry, not factors.

We compute Cohen's d + KS test for each numeric factor per cell, rank by |d|.
"""
import pandas as pd
import numpy as np
from pathlib import Path
from scipy.stats import ks_2samp

ROOT = Path("/Users/brock-mini-mac/scrooge-research")
PARQUET = ROOT / "all_strategies_all_pairs_trades.parquet"

NUMERIC_FACTORS = ["ADX14","ATR_ratio","BB_compress","RSI14","price_pos","volume_ratio"]
CAT_FACTORS = ["session_bucket","technical_regime_53"]

print("loading parquet ...")
cols = ["strategy_id","pair","direction","is_win","realized_R","entry_ts"] + NUMERIC_FACTORS + CAT_FACTORS
df = pd.read_parquet(PARQUET, columns=cols)
df["entry_ts"] = pd.to_datetime(df["entry_ts"], utc=True)
df["weekday"] = df["entry_ts"].dt.weekday
df["hour_utc"] = df["entry_ts"].dt.hour
df["minute_of_day"] = df["entry_ts"].dt.hour * 60 + df["entry_ts"].dt.minute
NUMERIC_FACTORS += ["weekday","hour_utc","minute_of_day"]
print(f"  {len(df):,} rows")

def cohens_d(w, l):
    """Effect size between two arrays."""
    w = pd.to_numeric(w, errors="coerce").dropna()
    l = pd.to_numeric(l, errors="coerce").dropna()
    if len(w) < 30 or len(l) < 30: return np.nan
    n1, n2 = len(w), len(l)
    s1, s2 = w.std(ddof=1), l.std(ddof=1)
    pooled = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1 + n2 - 2))
    if pooled == 0 or pd.isna(pooled): return np.nan
    return float((w.mean() - l.mean()) / pooled)

print("\nrunning factor analysis per cell ...")
results = []
combos = df.groupby(["strategy_id","pair","direction"]).agg(
    n=("is_win","size"), nw=("is_win","sum")
).reset_index()
combos["nl"] = combos["n"] - combos["nw"]
combos = combos[(combos["nw"] >= 100) & (combos["nl"] >= 100)]
print(f"  combos with n_w>=100 AND n_l>=100: {len(combos)}")

import time
t0 = time.time()
for idx, c in combos.iterrows():
    strat, pair, dirn = c["strategy_id"], c["pair"], c["direction"]
    sub = df[(df.strategy_id == strat) & (df.pair == pair) & (df.direction == dirn)]
    win = sub[sub.is_win == True]
    los = sub[sub.is_win == False]
    cell_row = {
        "strategy_id": strat, "pair": pair, "direction": dirn,
        "n_total": len(sub), "n_winners": len(win), "n_losers": len(los),
        "cell_mean_R": round(sub.realized_R.mean(), 4),
    }
    factor_rows = []
    for f in NUMERIC_FACTORS:
        w = pd.to_numeric(win[f], errors="coerce").dropna()
        l = pd.to_numeric(los[f], errors="coerce").dropna()
        if len(w) < 30 or len(l) < 30: continue
        d = cohens_d(w, l)
        if pd.isna(d): continue
        try:
            ks_stat, ks_p = ks_2samp(w, l)
        except Exception:
            ks_stat, ks_p = np.nan, np.nan
        factor_rows.append({
            "factor": f,
            "w_mean": round(float(w.mean()), 4),
            "l_mean": round(float(l.mean()), 4),
            "w_median": round(float(w.median()), 4),
            "l_median": round(float(l.median()), 4),
            "diff": round(float(w.mean() - l.mean()), 4),
            "cohens_d": round(d, 4),
            "ks_stat": round(float(ks_stat), 4),
            "ks_p": float(ks_p),
        })
    # Rank by |cohens_d|
    factor_rows.sort(key=lambda x: abs(x["cohens_d"]), reverse=True)
    for rank, fr in enumerate(factor_rows, 1):
        results.append({**cell_row, "factor_rank": rank, **fr})
    if (idx % 100 == 0) and idx > 0:
        elapsed = time.time() - t0
        print(f"  processed {idx} combos in {elapsed:.1f}s", flush=True)

res = pd.DataFrame(results)
print(f"\ntotal (cell, factor) rows: {len(res):,}")
print(f"unique cells covered: {res[['strategy_id','pair','direction']].drop_duplicates().shape[0]}")
res.to_csv(ROOT / "test1_factor_analysis_full.csv", index=False)

# Top discriminator per cell
top_per_cell = res[res.factor_rank == 1].copy()
top_per_cell["abs_d"] = top_per_cell["cohens_d"].abs()
top_per_cell = top_per_cell.sort_values("abs_d", ascending=False)
top_per_cell.to_csv(ROOT / "test1_top_factor_per_cell.csv", index=False)

print(f"\n=== TOP DISCRIMINATOR per cell (sorted by |Cohen's d|) ===")
print("Strong separation = |d| >= 0.5 (medium effect); >= 0.8 = large")
strong = top_per_cell[top_per_cell.abs_d >= 0.5].copy()
print(f"  cells with strong top-factor separation (|d| >= 0.5): {len(strong)}")
if len(strong):
    cols_show = ["strategy_id","pair","direction","n_winners","n_losers","factor",
                 "w_mean","l_mean","diff","cohens_d","ks_p"]
    print(strong[cols_show].head(40).to_string(index=False, float_format="%.4f"))

# Frequency of "winning" factor as top discriminator
print(f"\n=== HOW OFTEN IS EACH FACTOR THE #1 DISCRIMINATOR? (across {len(top_per_cell)} cells) ===")
fc = top_per_cell["factor"].value_counts()
for f, n in fc.items():
    sub = top_per_cell[top_per_cell.factor == f]
    avg_d = sub.abs_d.mean()
    print(f"  {f:20s}  cells={n:4d}  avg|d|={avg_d:.3f}")

# === Save the "top 2 factors per cell" for use as candidate filter ===
top2 = res[res.factor_rank <= 2].copy()
top2.to_csv(ROOT / "test1_top2_factors_per_cell.csv", index=False)
print(f"\nsaved:")
for f in ["test1_factor_analysis_full.csv","test1_top_factor_per_cell.csv","test1_top2_factors_per_cell.csv"]:
    p = ROOT / f
    print(f"  {p.name}: {p.stat().st_size/1024:.1f} KB")
