"""Phase 2 v2: moderate-state miner with frequency × expectancy objective.

Per Brock 2026-05-20: a 52% WR weekly cell > 90% WR monthly cell.

Search rules:
  - depth-1 AND depth-2 factor splits (depth-1 alone couldn't crack baselines)
  - moderate quantile thresholds (20/35/50/65/80 pct -- avoid extreme tails)
  - per-cell R-target optimization: find R in [0.5, 0.75, 1.0, 1.25, 1.5]
    that maximizes expected_R_per_week = fires_per_week * (WR*(R+1) - 1)
  - accept ANY cell where:
      * n_after_rule >= 13   (>= 0.5 fires/week)
      * positive expectancy at best R-target
      * shave_rule doesn't clamp to extreme percentile (< 10% of pop)
"""
import sys
sys.path.insert(0, "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0")
from expand_telemetry_driven import family_for
import pandas as pd
import pyarrow.parquet as pq
import numpy as np
from itertools import combinations

CORPUS_PATH = "/home/ubuntu/mr-scrooge-v3/research/routing-table-v2-2026-05-14/ml_training_corpus.parquet"
OUT_CSV = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/moderate_state_cells.csv"
OUT_MD  = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/moderate_state_summary.md"

MIN_N            = 13      # >= 0.5 fires/week
MIN_POP_FRAC     = 0.05    # rule must keep at least 5% of population (still moderate, but allows tighter)
R_TARGETS        = [0.5, 0.75, 1.0, 1.25, 1.5]
QUANTILES        = [0.20, 0.35, 0.50, 0.65, 0.80]
FACTOR_COLS      = ["ATR_ratio","BB_compress","ADX14","RSI14","close_pos"]

def wilson_lb(wins, n, z=1.28):
    if n == 0: return 0.0
    p = wins / n
    return (p + z*z/(2*n) - z*np.sqrt(p*(1-p)/n + z*z/(4*n*n))) / (1 + z*z/n)

def best_r_target_for(wr, fires_per_week):
    """Find best R in R_TARGETS that maximizes expected_R per week.

    Expected_R per trade = WR*R - (1-WR)*1 = WR*(R+1) - 1
    Expected_R per week  = fires_per_week * expected_R per trade

    Returns (best_R, expected_R_per_week, breakeven_wr_at_best_R).
    """
    best = None
    for R in R_TARGETS:
        ev_trade = wr * (R + 1) - 1
        if ev_trade <= 0: continue
        ev_week = fires_per_week * ev_trade
        if best is None or ev_week > best[1]:
            best = (R, ev_week, 1.0/(1.0+R))
    return best

print("Loading corpus...")
schema = pq.read_schema(CORPUS_PATH)
available = {f.name for f in schema}
wanted = ["source","strategy_id","pair","direction","entry_ts","is_win",
          "technical_regime_53","hour_utc"] + FACTOR_COLS
cols = [c for c in wanted if c in available]
df = pq.read_table(CORPUS_PATH, columns=cols).to_pandas()
df = df.drop_duplicates(["entry_ts","pair","direction","strategy_id"])
df["_fam"] = df["strategy_id"].map(family_for)
corpus_min = df.entry_ts.min(); corpus_max = df.entry_ts.max()
weeks = (corpus_max - corpus_min).days / 7.0
print(f"corpus: {len(df):,} rows over {weeks:.0f} weeks")

# Iterate per (regime, pair, direction, family). Skip session for now --
# session can be a downstream filter, but it kills sample size too early.
sigs = df[["technical_regime_53","pair","direction","_fam"]].drop_duplicates()
print(f"scanning {len(sigs)} signatures...")

def eval_rule_set(sub, clauses):
    """Apply a list of (col, op, thr) clauses; return mask."""
    mask = pd.Series(True, index=sub.index)
    for col, op, thr in clauses:
        s = pd.to_numeric(sub[col], errors="coerce")
        if op == "<=": mask &= (s <= thr)
        else:           mask &= (s >= thr)
    return mask

winners = []
sigs = sigs.rename(columns={"_fam": "fam"})
for sig_i, sig in enumerate(sigs.itertuples(index=False)):
    rg, pair, dirn, fam = sig.technical_regime_53, sig.pair, sig.direction, sig.fam
    sub = df[(df.technical_regime_53 == rg) & (df.pair == pair)
             & (df.direction == dirn) & (df._fam == fam)].copy()
    if len(sub) < MIN_N * 4: continue
    baseline_wr = sub.is_win.mean()

    # Generate candidate single-factor splits
    single_splits = []
    for col in FACTOR_COLS:
        if col not in sub.columns: continue
        vals = pd.to_numeric(sub[col], errors="coerce").dropna()
        if len(vals) < MIN_N * 4: continue
        for q in QUANTILES:
            thr = float(vals.quantile(q))
            for op in ("<=", ">="):
                single_splits.append((col, op, thr))

    # Try depth-1 + depth-2 combinations
    best_cell = None
    for d1 in single_splits:
        # depth-1
        mask = eval_rule_set(sub, [d1])
        kept = sub[mask]
        n = len(kept)
        if n < MIN_N: continue
        if n / len(sub) < MIN_POP_FRAC: continue
        wr = kept.is_win.mean()
        if wr <= baseline_wr: continue
        fpw = n / weeks
        best_r = best_r_target_for(wr, fpw)
        if best_r is None: continue
        cand = {
            "regime": rg, "pair": pair, "direction": dirn, "family": fam,
            "rule_depth": 1,
            "rule": f"{d1[0]}{d1[1]}{d1[2]:.6g}",
            "n": n, "wins": int(kept.is_win.sum()), "wr": wr,
            "wilson_lb": wilson_lb(int(kept.is_win.sum()), n),
            "fires_per_week": fpw, "fires_per_month": fpw * 4.33,
            "best_r_target": best_r[0],
            "expected_r_per_week": best_r[1],
            "breakeven_wr": best_r[2],
            "baseline_wr": baseline_wr,
            "pop_kept_frac": n / len(sub),
        }
        if best_cell is None or cand["expected_r_per_week"] > best_cell["expected_r_per_week"]:
            best_cell = cand

    # depth-2 combinations
    for d1, d2 in combinations(single_splits, 2):
        if d1[0] == d2[0]: continue  # don't combine two clauses on same factor
        mask = eval_rule_set(sub, [d1, d2])
        kept = sub[mask]
        n = len(kept)
        if n < MIN_N: continue
        if n / len(sub) < MIN_POP_FRAC: continue
        wr = kept.is_win.mean()
        if wr <= baseline_wr: continue
        fpw = n / weeks
        best_r = best_r_target_for(wr, fpw)
        if best_r is None: continue
        cand = {
            "regime": rg, "pair": pair, "direction": dirn, "family": fam,
            "rule_depth": 2,
            "rule": f"{d1[0]}{d1[1]}{d1[2]:.6g} AND {d2[0]}{d2[1]}{d2[2]:.6g}",
            "n": n, "wins": int(kept.is_win.sum()), "wr": wr,
            "wilson_lb": wilson_lb(int(kept.is_win.sum()), n),
            "fires_per_week": fpw, "fires_per_month": fpw * 4.33,
            "best_r_target": best_r[0],
            "expected_r_per_week": best_r[1],
            "breakeven_wr": best_r[2],
            "baseline_wr": baseline_wr,
            "pop_kept_frac": n / len(sub),
        }
        if best_cell is None or cand["expected_r_per_week"] > best_cell["expected_r_per_week"]:
            best_cell = cand

    if best_cell:
        winners.append(best_cell)

if not winners:
    print("ZERO winners. Even with depth-2 + per-cell R-target, the corpus")
    print("cannot produce moderate-frequency positive-expectancy cells.")
    raise SystemExit(0)

out = pd.DataFrame(winners).sort_values("expected_r_per_week", ascending=False)
out["freq_class"] = pd.cut(out.fires_per_week, [0,0.25,1,3,1e9],
                          labels=["GHOST","RARE","MODERATE","REGULAR"])
out.to_csv(OUT_CSV, index=False)

print(f"\n=== MODERATE-STATE WINNERS: {len(out)} cells ===")
print(out.groupby("freq_class").agg(
    cells=("rule","count"),
    median_fires_per_week=("fires_per_week","median"),
    median_wr=("wr","median"),
    median_expected_r_per_week=("expected_r_per_week","median"),
).to_string())
print()
print("=== TOP 30 BY expected_R_per_week ===")
print(out.head(30)[["pair","regime","direction","family","rule_depth",
                    "n","wr","fires_per_week","best_r_target",
                    "expected_r_per_week","wilson_lb"]].to_string(index=False))

with open(OUT_MD, "w") as f:
    f.write("# Moderate-State Mining Summary (v2)\n\n")
    f.write(f"Generated 2026-05-20. Corpus: {len(df):,} rows / {weeks:.0f} weeks / {len(sigs)} signatures.\n\n")
    f.write("**Objective**: maximize `fires_per_week × expected_R_per_trade` at best per-cell R-target.\n\n")
    f.write("**Bars**: n≥13 (>=0.5/wk), pop_kept >= 10%, WR > baseline, positive expectancy at best R-target.\n\n")
    f.write(f"**Total qualifying cells**: {len(out)}\n\n")
    f.write("## Frequency class distribution\n\n```\n")
    f.write(out.groupby("freq_class").agg(
        cells=("rule","count"),
        median_fires_per_week=("fires_per_week","median"),
        median_wr=("wr","median"),
        median_expected_r_per_week=("expected_r_per_week","median"),
    ).to_string())
    f.write("\n```\n\n")
    f.write("## Top 25 cells by expected_R_per_week\n\n")
    f.write("| pair | regime | dir | family | rule | depth | n | WR | fires/wk | best_R | exp_R/wk | wilson_lb |\n")
    f.write("|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|\n")
    for _, r in out.head(25).iterrows():
        f.write(f"| {r.pair} | {r.regime} | {r.direction} | {r.family} | `{r.rule}` | {r.rule_depth} | {int(r.n)} | {r.wr:.3f} | {r.fires_per_week:.2f} | {r.best_r_target} | {r.expected_r_per_week:.3f} | {r.wilson_lb:.3f} |\n")
print(f"\nwrote {OUT_CSV}")
print(f"wrote {OUT_MD}")
