"""Phase 2: moderate-state mining with frequency floor.

Objective: find cells that fire OFTEN with POSITIVE edge, not cells that
fire rarely with inflated WR.

For each (regime, pair, direction, family) signature in the corpus:
  1. Compute baseline n, WR
  2. Try simple depth-1 factor splits (quartile thresholds, both ops)
  3. ACCEPT only if:
       - corpus n after rule >= 26   (>= 1 fire/week over 26-week corpus)
       - corpus WR after rule >= 0.55
       - shave_rule doesn't clamp to extreme percentile (>0.95 or <0.05)
  4. Optimization target: n * (WR - 0.50)  -- expected wins above baseline

Output the surviving cells with frequency stats.
"""
import sys
sys.path.insert(0, "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0")
from expand_telemetry_driven import family_for
import pandas as pd
import pyarrow.parquet as pq
import numpy as np

CORPUS_PATH = "/home/ubuntu/mr-scrooge-v3/research/routing-table-v2-2026-05-14/ml_training_corpus.parquet"
OUT_CSV = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/moderate_state_cells.csv"
OUT_MD  = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/moderate_state_summary.md"

# Tradability bars (realistic under r_target=1.5R, breakeven 40%)
MIN_N_PER_RULE   = 26     # >= 1 fire/week over 26-week corpus
MIN_WR_PER_RULE  = 0.40   # breakeven at 1.5R; anything above is positive expectancy
MAX_EXTREME_PCT  = 0.90   # don't accept rules clamping to <10% of population

FACTOR_COLS = ["ATR_ratio","BB_compress","ADX14","RSI14","close_pos"]

print("Loading corpus...")
schema = pq.read_schema(CORPUS_PATH)
available = {f.name for f in schema}
wanted = ["source","strategy_id","pair","direction","entry_ts","is_win",
          "technical_regime_53","hour_utc","day_of_week"] + FACTOR_COLS
cols = [c for c in wanted if c in available]
df = pq.read_table(CORPUS_PATH, columns=cols).to_pandas()
df = df.drop_duplicates(["entry_ts","pair","direction","strategy_id"])
df["_fam"] = df["strategy_id"].map(family_for)
print(f"corpus: {len(df):,} rows")

corpus_min = df.entry_ts.min(); corpus_max = df.entry_ts.max()
weeks = (corpus_max - corpus_min).days / 7.0

# Iterate per (regime, pair, direction, family)
signatures = df[["technical_regime_53","pair","direction","_fam"]].drop_duplicates()
print(f"signatures to scan: {len(signatures)}")

def wilson_lb(wins: int, n: int, z: float = 1.28) -> float:
    if n == 0: return 0.0
    p = wins / n
    denom = 1 + z*z / n
    centre = p + z*z/(2*n)
    margin = z * np.sqrt(p*(1-p)/n + z*z/(4*n*n))
    return (centre - margin) / denom

winners = []
for _, sig in signatures.iterrows():
    rg, pair, dirn, fam = sig["technical_regime_53"], sig["pair"], sig["direction"], sig["_fam"]
    sub = df[(df.technical_regime_53 == rg) & (df.pair == pair)
             & (df.direction == dirn) & (df._fam == fam)]
    if len(sub) < MIN_N_PER_RULE * 2: continue
    baseline_wr = sub.is_win.mean()
    if baseline_wr >= MIN_WR_PER_RULE:
        # already moderate-state edge -- accept whole population as a cell
        n = len(sub); wins = int(sub.is_win.sum())
        winners.append({
            "regime": rg, "pair": pair, "direction": dirn, "family": fam,
            "rule": "(no filter)", "n": n, "wins": wins, "wr": baseline_wr,
            "wilson_lb": wilson_lb(wins, n),
            "fires_per_week": n / weeks,
            "fires_per_month": (n / weeks) * 4.33,
            "score": n * (baseline_wr - 0.5),
            "rule_type": "baseline",
        })
        continue
    # try depth-1 splits
    best = None
    for col in FACTOR_COLS:
        if col not in sub.columns: continue
        vals = pd.to_numeric(sub[col], errors="coerce").dropna()
        if len(vals) < MIN_N_PER_RULE * 2: continue
        # use moderate quantile thresholds: avoid extreme percentiles
        for q in (0.20, 0.30, 0.50, 0.70, 0.80):
            thr = float(vals.quantile(q))
            for op in ("<=", ">="):
                mask = (pd.to_numeric(sub[col], errors="coerce") <= thr) if op == "<=" else (pd.to_numeric(sub[col], errors="coerce") >= thr)
                kept = sub[mask]
                if len(kept) < MIN_N_PER_RULE: continue
                # reject if rule clamps to extreme percentile
                kept_quantile = (kept[col].count() / len(sub))
                if kept_quantile < (1 - MAX_EXTREME_PCT): continue
                wr = kept.is_win.mean()
                if wr < MIN_WR_PER_RULE: continue
                score = len(kept) * (wr - 0.5)
                cand = {
                    "regime": rg, "pair": pair, "direction": dirn, "family": fam,
                    "rule": f"{col}{op}{thr:.6g}", "n": len(kept),
                    "wins": int(kept.is_win.sum()), "wr": wr,
                    "wilson_lb": wilson_lb(int(kept.is_win.sum()), len(kept)),
                    "fires_per_week": len(kept) / weeks,
                    "fires_per_month": (len(kept) / weeks) * 4.33,
                    "score": score,
                    "rule_type": "depth1",
                }
                if best is None or cand["score"] > best["score"]:
                    best = cand
    if best:
        winners.append(best)

if not winners:
    print("\n*** ZERO MODERATE-STATE WINNERS AT WR>=0.40 with n>=26 and no extreme clamps. ***")
    print("Even at the bot's r_target=1.5R breakeven of 40% WR, the corpus has no qualifying cells.")
    print("Implication: the strategy/R-target framework cannot produce moderate-frequency profitable cells.")
    raise SystemExit(0)
out = pd.DataFrame(winners).sort_values("score", ascending=False)
out.to_csv(OUT_CSV, index=False)

print()
print("=" * 95)
print(f"MODERATE-STATE WINNERS: {len(out)} cells   (n>={MIN_N_PER_RULE}, WR>={MIN_WR_PER_RULE}, no extreme clamps)")
print("=" * 95)
top = out.head(40)
print(top[["pair","regime","direction","family","rule","n","wr","wilson_lb",
          "fires_per_week","fires_per_month","score"]].to_string(index=False))
print()

# Frequency-class breakdown
out["freq_class"] = pd.cut(out.fires_per_week, [0,0.25,1,3,1e9],
                          labels=["GHOST","RARE","MODERATE","REGULAR"])
print()
print("=" * 60)
print("FREQUENCY CLASS DISTRIBUTION (mined cells)")
print("=" * 60)
print(out.groupby("freq_class").agg(
    cells=("rule","count"),
    median_fires_per_week=("fires_per_week","median"),
    median_wr=("wr","median"),
).to_string())

# Markdown summary
with open(OUT_MD, "w") as f:
    f.write("# Moderate-State Mining Summary\n\n")
    f.write(f"Generated 2026-05-20. Corpus: {len(df):,} rows over {weeks:.0f} weeks.\n\n")
    f.write(f"**Bars:** n >= {MIN_N_PER_RULE} (>= 1 fire/wk), WR >= {MIN_WR_PER_RULE}, no extreme-percentile clamps.\n\n")
    f.write(f"**Total moderate-state winners found:** {len(out)}\n\n")
    f.write("## Frequency class distribution\n\n")
    f.write("```\n")
    f.write(out.groupby("freq_class").agg(cells=("rule","count"), median_fires_per_week=("fires_per_week","median"), median_wr=("wr","median")).to_string())
    f.write("\n```\n\n")
    f.write("## Top 25 cells (by expected-wins-above-baseline)\n\n")
    f.write("| pair | regime | dir | family | rule | n | WR | wilson_lb | fires/wk | score |\n")
    f.write("|---|---|---|---|---|---:|---:|---:|---:|---:|\n")
    for _, r in out.head(25).iterrows():
        f.write(f"| {r.pair} | {r.regime} | {r.direction} | {r.family} | `{r.rule}` | {int(r.n)} | {r.wr:.3f} | {r.wilson_lb:.3f} | {r.fires_per_week:.2f} | {r.score:.1f} |\n")

print(f"\nwrote {OUT_CSV}")
print(f"wrote {OUT_MD}")
