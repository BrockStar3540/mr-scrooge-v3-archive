"""Workstream #2: Build scalper bank from scalper_corpus_6x12.parquet.

For each (regime, pair, direction, family) signature:
  - Compute baseline clean WR (clean_win / clean_total) using ONLY clean outcomes
  - Try depth-1 and depth-2 factor splits on (ATR_ratio, BB_compress, ADX14,
    RSI14, price_pos, volume_ratio) at quantiles 20/35/50/65/80
  - Accept cells where:
      n_clean >= 13           (>=0.5 fires/week of clean-resolution trades)
      pop_kept >= 5%          (no extreme clamping)
      wr_clean >= 0.33        (breakeven at 2:1 R:R)
      expectancy > 0
  - Objective: clean_wins_per_week = n_clean / weeks * wr_clean
  - Per cell, also compute "probable_WR" = (clean_wins + amb/2) / (clean + amb)
    as a less-conservative estimate.
"""
import pandas as pd
import numpy as np
import pyarrow.parquet as pq
from itertools import combinations

CORPUS = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/scalper_corpus_6x12.parquet"
OUT_CELLS = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/scalper_bank_cells.csv"
OUT_FREQ = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/scalper_bank_with_frequency.csv"
OUT_MD = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/scalper_bank_summary.md"

MIN_N_CLEAN     = 13      # >= 0.5 clean fires/week
MIN_POP_FRAC    = 0.05    # no extreme clamping
MIN_CLEAN_WR    = 0.33    # breakeven at 2:1
QUANTILES       = [0.20, 0.35, 0.50, 0.65, 0.80]
FACTOR_COLS     = ["ATR_ratio","BB_compress","ADX14","RSI14","price_pos","volume_ratio"]

def wilson_lb(wins, n, z=1.28):
    if n == 0: return 0.0
    p = wins / n
    return (p + z*z/(2*n) - z*np.sqrt(p*(1-p)/n + z*z/(4*n*n))) / (1 + z*z/n)

print("loading scalper corpus (streaming projection)...", flush=True)
# Only load columns we need to keep memory bounded
needed = ["technical_regime_53","pair","direction","family","strategy_id",
          "entry_ts","scalp_outcome","is_win_6x12","session_bucket","hour_utc"] + FACTOR_COLS
df = pq.read_table(CORPUS, columns=needed).to_pandas()
print(f"corpus rows: {len(df):,}", flush=True)

# Time span -> weeks
df["entry_ts"] = pd.to_datetime(df.entry_ts, utc=True)
weeks = (df.entry_ts.max() - df.entry_ts.min()).days / 7.0
print(f"corpus span: {df.entry_ts.min()} -> {df.entry_ts.max()}  ({weeks:.0f} weeks)", flush=True)

# Drop "other" family (rare strategy ids that don't map cleanly)
df = df[df.family.isin(["direct","dbb_trend","reversal"])]
print(f"after family filter: {len(df):,}", flush=True)

# Signatures to scan
sigs = df[["technical_regime_53","pair","direction","family"]].drop_duplicates()
print(f"signatures to scan: {len(sigs)}", flush=True)

# Iterate
winners = []
for sig_i, sig in enumerate(sigs.itertuples(index=False)):
    rg, pair, dirn, fam = sig.technical_regime_53, sig.pair, sig.direction, sig.family
    sub = df[(df.technical_regime_53 == rg) & (df.pair == pair)
             & (df.direction == dirn) & (df.family == fam)]
    # Counts
    clean_mask = sub.scalp_outcome.isin(["clean_win","clean_loss"])
    n_clean_all = int(clean_mask.sum())
    n_amb_all = int((sub.scalp_outcome == "ambiguous").sum())
    if n_clean_all < MIN_N_CLEAN * 4: continue
    baseline_clean_wr = (sub.scalp_outcome == "clean_win").sum() / max(1, n_clean_all)

    # Generate candidate splits
    splits = []
    for col in FACTOR_COLS:
        if col not in sub.columns: continue
        vals = pd.to_numeric(sub[col], errors="coerce").dropna()
        if len(vals) < MIN_N_CLEAN * 4: continue
        for q in QUANTILES:
            thr = float(vals.quantile(q))
            for op in ("<=", ">="):
                splits.append((col, op, thr))

    def eval_mask(clauses):
        m = pd.Series(True, index=sub.index)
        for col, op, thr in clauses:
            s = pd.to_numeric(sub[col], errors="coerce")
            if op == "<=": m &= (s <= thr)
            else:           m &= (s >= thr)
        return m

    best = None
    # Try baseline (no shave) + depth-1 + depth-2 (skip same-factor combos)
    all_rule_sets = [[]] + [[s] for s in splits]
    # Limit depth-2 combinations
    for d1, d2 in combinations(splits, 2):
        if d1[0] == d2[0]: continue
        all_rule_sets.append([d1, d2])

    for clauses in all_rule_sets:
        if clauses:
            mask = eval_mask(clauses)
            kept = sub[mask]
        else:
            kept = sub
        if len(kept) / len(sub) < MIN_POP_FRAC and clauses: continue
        c = kept[kept.scalp_outcome.isin(["clean_win","clean_loss"])]
        n_c = len(c)
        if n_c < MIN_N_CLEAN: continue
        wins_c = int((c.scalp_outcome == "clean_win").sum())
        wr_c = wins_c / n_c
        if wr_c < MIN_CLEAN_WR: continue
        # Expectancy at 2:1
        ev_per_trade = wr_c * 2.0 - (1 - wr_c) * 1.0
        if ev_per_trade <= 0: continue
        # Frequency: total kept (clean + ambiguous + neither) / weeks
        n_total_kept = len(kept)
        fires_per_week = n_total_kept / weeks
        clean_fires_per_week = n_c / weeks
        expected_R_per_week = clean_fires_per_week * ev_per_trade
        # probable WR (amb @ 50%)
        n_amb_kept = int((kept.scalp_outcome == "ambiguous").sum())
        denom = n_c + n_amb_kept
        probable_wr = (wins_c + n_amb_kept / 2) / denom if denom else 0.0

        rule = "(no filter)" if not clauses else " AND ".join(f"{c[0]}{c[1]}{c[2]:.6g}" for c in clauses)
        cand = {
            "regime": rg, "pair": pair, "direction": dirn, "family": fam,
            "rule": rule, "rule_depth": len(clauses),
            "n_clean": n_c, "wins_clean": wins_c, "wr_clean": wr_c,
            "n_amb_kept": n_amb_kept, "n_total_kept": n_total_kept,
            "wilson_lb": wilson_lb(wins_c, n_c),
            "fires_per_week": fires_per_week,
            "clean_fires_per_week": clean_fires_per_week,
            "fires_per_month": fires_per_week * 4.33,
            "expectancy_R_per_trade": ev_per_trade,
            "expected_R_per_week": expected_R_per_week,
            "probable_wr_amb_50": probable_wr,
            "pop_kept_frac": len(kept) / len(sub),
            "baseline_clean_wr": baseline_clean_wr,
        }
        if best is None or cand["expected_R_per_week"] > best["expected_R_per_week"]:
            best = cand
    if best:
        winners.append(best)

if not winners:
    print("ZERO scalper bank cells found.")
    raise SystemExit(0)

out = pd.DataFrame(winners).sort_values("expected_R_per_week", ascending=False)
out["freq_class"] = pd.cut(out.fires_per_week, [0,0.25,1,3,1e9],
                          labels=["GHOST","RARE","MODERATE","REGULAR"])
out.to_csv(OUT_CELLS, index=False)
out.to_csv(OUT_FREQ, index=False)

print(f"\n=== SCALPER BANK: {len(out)} cells ===")
print(out.groupby("freq_class").agg(
    cells=("rule","count"),
    median_fpw=("fires_per_week","median"),
    median_clean_wr=("wr_clean","median"),
    median_exp_R_per_wk=("expected_R_per_week","median"),
).reindex(["REGULAR","MODERATE","RARE","GHOST"]).to_string())
print()
print("=== TOP 30 BY expected_R_per_week ===")
print(out.head(30)[["pair","regime","direction","family","rule_depth",
                    "n_clean","wr_clean","fires_per_week",
                    "expectancy_R_per_trade","expected_R_per_week",
                    "probable_wr_amb_50","wilson_lb"]].to_string(index=False))

# Markdown summary
with open(OUT_MD, "w") as f:
    f.write("# Scalper Bank Summary (built 2026-05-21)\n\n")
    f.write(f"Corpus: scalper_corpus_6x12.parquet, {len(df):,} rows over {weeks:.0f} weeks, "
            f"{len(sigs)} signatures scanned.\n\n")
    f.write(f"Bars: n_clean>=13, pop_kept>=5%, clean_WR>=0.33 (breakeven at 2:1), positive expectancy.\n\n")
    f.write(f"**Total cells: {len(out)}**\n\n")
    f.write(f"## Frequency class distribution\n\n```\n")
    f.write(out.groupby("freq_class").agg(
        cells=("rule","count"),
        median_fpw=("fires_per_week","median"),
        median_clean_wr=("wr_clean","median"),
        median_exp_R_per_wk=("expected_R_per_week","median"),
    ).reindex(["REGULAR","MODERATE","RARE","GHOST"]).to_string())
    f.write("\n```\n\n")
    f.write(f"## Top 25 cells (sorted by expected_R_per_week)\n\n")
    f.write("| pair | regime | dir | family | rule | depth | n_clean | WR_clean | fires/wk | exp_R/trade | exp_R/wk | prob_WR | wilson_lb |\n")
    f.write("|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|\n")
    for _, r in out.head(25).iterrows():
        f.write(f"| {r.pair} | {r.regime} | {r.direction} | {r.family} | `{r.rule}` | {int(r.rule_depth)} | {int(r.n_clean)} | {r.wr_clean:.3f} | {r.fires_per_week:.2f} | {r.expectancy_R_per_trade:.3f} | {r.expected_R_per_week:.2f} | {r.probable_wr_amb_50:.3f} | {r.wilson_lb:.3f} |\n")
    f.write(f"\n## Caveat\n\n")
    f.write(f"Clean WR uses only unambiguous events ({((out.n_clean.sum())/(out.n_clean.sum()+out.n_amb_kept.sum()))*100:.0f}% of total).\n")
    f.write(f"The `probable_wr_amb_50` column estimates true WR assuming ambiguous events split 50/50.\n")
    f.write(f"OHLC-based resolution of ambiguous events is the natural next step.\n")
print(f"\nwrote {OUT_CELLS}")
print(f"wrote {OUT_FREQ}")
print(f"wrote {OUT_MD}")
