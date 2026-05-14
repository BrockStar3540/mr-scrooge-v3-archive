"""Test 2: winner vs loser regime cross-tab.

For each (strategy_id, pair, direction) and each of the 53 technical regimes,
counts winners and losers. Shows:
  - Which regimes have winners-only (or losers-only) for each strategy×pair
  - Regimes where winners cluster but losers also cluster (mixed = not useful)
  - Regimes where winners >> losers (good potential filter)
  - Regimes where losers >> winners (good "skip" filter)
"""
import pandas as pd
import numpy as np
from pathlib import Path

ROOT = Path("/Users/brock-mini-mac/scrooge-research")
PARQUET = ROOT / "all_strategies_all_pairs_trades.parquet"
OUT = ROOT

print("loading parquet ...")
df = pd.read_parquet(PARQUET, columns=[
    "strategy_id","pair","direction","technical_regime_53","technical_regime_desc",
    "is_win","realized_R","entry_ts",
])
df["entry_ts"] = pd.to_datetime(df["entry_ts"], utc=True)
print(f"  {len(df):,} trades")
print(f"  unique regimes: {df.technical_regime_53.nunique()}")

# === Per (strategy, pair, direction, regime) summary ===
agg = df.groupby(["strategy_id","pair","direction","technical_regime_53","technical_regime_desc"]).agg(
    n=("realized_R","size"),
    wins=("is_win","sum"),
    mean_R=("realized_R","mean"),
).reset_index()
agg["wins"] = agg["wins"].astype(int)
agg["losses"] = agg["n"] - agg["wins"]
agg["win_rate"] = (agg["wins"] / agg["n"]).round(4)
agg["mean_R"] = agg["mean_R"].round(4)

# Bring in cell-level totals
cell = df.groupby(["strategy_id","pair","direction"]).agg(
    cell_n=("realized_R","size"),
    cell_wins=("is_win","sum"),
).reset_index()
cell["cell_wins"] = cell["cell_wins"].astype(int)
cell["cell_win_rate"] = (cell["cell_wins"] / cell["cell_n"]).round(4)

agg = agg.merge(cell, on=["strategy_id","pair","direction"])

# Lift = win_rate in this regime / overall win_rate for the cell
agg["wr_lift"] = (agg["win_rate"] / agg["cell_win_rate"]).round(4)
# Regime fire share
agg["regime_share"] = (agg["n"] / agg["cell_n"]).round(4)

agg.to_csv(OUT / "test2_regime_crosstab_full.csv", index=False)
print(f"\nsaved test2_regime_crosstab_full.csv: {len(agg):,} rows")

# === SUMMARY 1: regimes with winner-rate >= 50% AND n >= 30 ===
print("\n=== A) Regimes with win_rate >= 50% and n >= 30 (per strategy x pair x direction) ===")
good = agg[(agg.win_rate >= 0.50) & (agg.n >= 30)].sort_values("win_rate", ascending=False)
print(f"  cells: {len(good)}")
print(good[["strategy_id","pair","direction","technical_regime_53","technical_regime_desc",
            "n","wins","losses","win_rate","mean_R","cell_win_rate","wr_lift","regime_share"]].head(30).to_string(index=False, float_format="%.3f"))
good.to_csv(OUT / "test2_winning_regime_cells.csv", index=False)

# === SUMMARY 2: per-(strategy, pair) - which regimes do winners ONLY appear in ===
print("\n=== B) Winner-only regimes (zero losses in that regime, n_winners >= 5) ===")
winner_only = agg[(agg.losses == 0) & (agg.wins >= 5)].sort_values("wins", ascending=False)
print(f"  cells: {len(winner_only)}")
if len(winner_only):
    print(winner_only[["strategy_id","pair","direction","technical_regime_53","technical_regime_desc",
                       "n","wins","mean_R"]].head(20).to_string(index=False, float_format="%.3f"))

# === SUMMARY 3: per-(strategy, pair) - which regimes do losers ONLY appear in (n>=20) ===
print("\n=== C) Loser-heavy regimes (win_rate <= 5%, n >= 50) — candidates to SKIP ===")
loser_heavy = agg[(agg.win_rate <= 0.05) & (agg.n >= 50)].sort_values("losses", ascending=False)
print(f"  cells: {len(loser_heavy)}")
if len(loser_heavy):
    print(loser_heavy[["strategy_id","pair","direction","technical_regime_53","technical_regime_desc",
                       "n","wins","losses","mean_R"]].head(20).to_string(index=False, float_format="%.3f"))
loser_heavy.to_csv(OUT / "test2_loser_heavy_regimes.csv", index=False)

# === SUMMARY 4: For TF6 (our shipped family) — full regime breakdown for shipped + held-back cells
print("\n=== D) TF6 ma_ribbon: per-regime stats for shipped + held-back cells ===")
tf6_pairs = [
    ("TF6_ma_ribbon_short", "USD_JPY", "short"),   # shipped
    ("TF6_ma_ribbon_long",  "USD_MXN", "long"),    # shipped
    ("TF6_ma_ribbon_long",  "USD_JPY", "long"),    # held
    ("TF6_ma_ribbon_short", "USD_CAD", "short"),   # held
]
for strat, pair, dirn in tf6_pairs:
    sub = agg[(agg.strategy_id == strat) & (agg.pair == pair) & (agg.direction == dirn)].sort_values("wr_lift", ascending=False)
    if len(sub) == 0: continue
    overall_wr = sub.cell_win_rate.iloc[0]
    overall_n = sub.cell_n.iloc[0]
    print(f"\n  {strat} / {pair} / {dirn}  overall n={overall_n} wr={overall_wr:.3f}")
    print(sub.head(15)[["technical_regime_53","technical_regime_desc","n","wins","losses","win_rate","wr_lift","mean_R","regime_share"]].to_string(index=False, float_format="%.3f"))

# === SUMMARY 5: do winners share regimes with losers, or are they separable? ===
print("\n=== E) Per (strategy, pair, direction): regime separation ===")
# For each cell, compute: how many distinct regimes contain >=10 winners?
#                         how many of those ALSO contain >=10 losers?
sep = df.groupby(["strategy_id","pair","direction","technical_regime_53"]).agg(
    n=("is_win","size"), w=("is_win","sum")
).reset_index()
sep["w"] = sep["w"].astype(int)
sep["l"] = sep["n"] - sep["w"]
sep["winner_dom"] = (sep.w >= 10) & (sep.w >= 2*sep.l)  # winners dominate (2:1+)
sep["loser_dom"]  = (sep.l >= 10) & (sep.l >= 2*sep.w)  # losers dominate
sep["mixed"]      = (sep.w >= 5) & (sep.l >= 5) & ~(sep.winner_dom | sep.loser_dom)
sep_summary = sep.groupby(["strategy_id","pair","direction"]).agg(
    n_total_trades=("n","sum"),
    n_winner_regimes=("winner_dom","sum"),
    n_loser_regimes=("loser_dom","sum"),
    n_mixed_regimes=("mixed","sum"),
).reset_index()
sep_summary = sep_summary.merge(cell, on=["strategy_id","pair","direction"])
sep_summary["separability"] = (sep_summary["n_winner_regimes"] /
    (sep_summary["n_winner_regimes"] + sep_summary["n_mixed_regimes"] + 0.001)).round(3)
sep_summary = sep_summary[sep_summary.cell_n >= 500].sort_values("separability", ascending=False)
print(f"  cells with n>=500: {len(sep_summary)}")
print(f"  cells with at least 1 winner-dominant regime: {(sep_summary.n_winner_regimes > 0).sum()}")
print(f"\nTop 30 most-separable cells:")
print(sep_summary.head(30)[["strategy_id","pair","direction","cell_n","cell_win_rate",
                             "n_winner_regimes","n_loser_regimes","n_mixed_regimes",
                             "separability"]].to_string(index=False, float_format="%.3f"))
sep_summary.to_csv(OUT / "test2_regime_separability.csv", index=False)
print(f"\nsaved:")
for f in ["test2_regime_crosstab_full.csv","test2_winning_regime_cells.csv",
          "test2_loser_heavy_regimes.csv","test2_regime_separability.csv"]:
    p = OUT / f
    print(f"  {p.name}: {p.stat().st_size/1024:.1f} KB")
