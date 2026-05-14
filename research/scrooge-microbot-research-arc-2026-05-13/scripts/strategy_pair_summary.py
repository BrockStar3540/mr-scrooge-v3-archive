"""Per (strategy, pair, direction) winners/losers summary.

Pure raw scorecard from the foundational parquet. No filters, no gates,
no regime discovery. Just counts and means.

Output: strategy_pair_summary.csv with columns:
  strategy_id, category, pair, pair_family, direction,
  n_total, n_winners, n_losers, win_rate,
  mean_R, mean_R_winners, mean_R_losers,
  mfe_R_median, mae_R_median,
  date_first, date_last,
  n_2019, n_2020, n_2021, n_2022, n_2023, n_2024, n_2025, n_2026,
  mean_R_2019, mean_R_2020, ..., mean_R_2026
"""
import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path("/Users/brock-mini-mac/scrooge-research")
PARQUET = ROOT / "all_strategies_all_pairs_trades.parquet"
OUT = ROOT / "strategy_pair_summary.csv"

print("loading parquet ...")
df = pd.read_parquet(PARQUET)
df["entry_ts"] = pd.to_datetime(df["entry_ts"], utc=True)
df["year"] = df["entry_ts"].dt.year
print(f"  {len(df):,} rows, {df.strategy_id.nunique()} strategies, {df.pair.nunique()} pairs")

# Year-by-year sub-counts and mean R
years = sorted(df["year"].unique())
def per_year_stats(sub):
    out = {}
    for y in years:
        s = sub[sub.year == y]
        out[f"n_{y}"] = len(s)
        out[f"mean_R_{y}"] = round(float(s.realized_R.mean()), 4) if len(s) > 0 else None
    return pd.Series(out)

print("aggregating ...")
agg = df.groupby(["strategy_id","category","pair","pair_family","direction"]).agg(
    n_total=("realized_R","size"),
    n_winners=("is_win","sum"),
    mean_R=("realized_R","mean"),
    mfe_R_median=("mfe_R","median"),
    mae_R_median=("mae_R","median"),
    date_first=("entry_ts","min"),
    date_last=("entry_ts","max"),
).reset_index()
agg["n_winners"] = agg["n_winners"].astype(int)
agg["n_losers"] = agg["n_total"] - agg["n_winners"]
agg["win_rate"] = (agg["n_winners"] / agg["n_total"]).round(4)
agg["mean_R"] = agg["mean_R"].round(4)
agg["mfe_R_median"] = agg["mfe_R_median"].round(4)
agg["mae_R_median"] = agg["mae_R_median"].round(4)

# Mean R for winners and losers separately
win_loss = df.groupby(["strategy_id","pair","direction","is_win"])["realized_R"].mean().unstack().reset_index()
win_loss = win_loss.rename(columns={True: "mean_R_winners", False: "mean_R_losers"})
win_loss["mean_R_winners"] = win_loss["mean_R_winners"].round(4)
win_loss["mean_R_losers"] = win_loss["mean_R_losers"].round(4)
agg = agg.merge(win_loss, on=["strategy_id","pair","direction"], how="left")

# Per-year columns
yearly = df.groupby(["strategy_id","pair","direction"]).apply(per_year_stats).reset_index()
agg = agg.merge(yearly, on=["strategy_id","pair","direction"], how="left")

# Reorder columns
order = ["strategy_id","category","pair","pair_family","direction",
         "n_total","n_winners","n_losers","win_rate",
         "mean_R","mean_R_winners","mean_R_losers",
         "mfe_R_median","mae_R_median",
         "date_first","date_last"]
order += [c for c in agg.columns if c.startswith("n_2") or c.startswith("mean_R_2")]
agg = agg[order].sort_values(["strategy_id","pair","direction"])

agg.to_csv(OUT, index=False)
print(f"\nsaved {OUT}: {len(agg)} (strategy, pair, direction) rows")
print(f"  size: {OUT.stat().st_size/1024:.1f} KB")
print()

# Top of table by mean_R, by strategy, by pair
print("=== HIGHEST mean_R (top 20, n>=500) ===")
top = agg[agg.n_total >= 500].sort_values("mean_R", ascending=False).head(20)
print(top[["strategy_id","pair","direction","n_total","n_winners","n_losers","win_rate","mean_R"]].to_string(index=False, float_format="%.3f"))

print()
print("=== LOWEST mean_R (top 20, n>=500) ===")
bot = agg[agg.n_total >= 500].sort_values("mean_R").head(20)
print(bot[["strategy_id","pair","direction","n_total","n_winners","n_losers","win_rate","mean_R"]].to_string(index=False, float_format="%.3f"))

print()
print("=== Strategy-family overall: rows count + best/worst by mean_R ===")
fam_summary = agg.groupby("strategy_id").agg(
    pairs=("pair","nunique"),
    total_trades=("n_total","sum"),
    avg_mean_R=("mean_R","mean"),
    best_mean_R=("mean_R","max"),
    worst_mean_R=("mean_R","min"),
).reset_index().sort_values("avg_mean_R", ascending=False)
print(fam_summary.to_string(index=False, float_format="%.4f"))
