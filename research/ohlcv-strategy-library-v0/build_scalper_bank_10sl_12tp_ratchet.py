"""Workstream #4: Build scalper bank under 10/12/ratchet model.

For each (regime, pair, direction, family) signature:
  - Compute clean-only WR (clean_win / non-ambiguous count)
  - Compute clean expected pips/trade
  - Optionally try depth-1 / depth-2 factor splits to lift expectancy
  - Accept cells where:
      n_clean >= 13   (>= 0.5 fires/wk)
      pop_kept >= 5%
      expected_pips_per_trade > 0
  - Objective: clean_fires_per_week * expected_pips_per_trade

Outputs:
  scalper_bank_cells_10sl_12tp_ratchet.csv
  scalper_bank_with_frequency_10sl_12tp_ratchet.csv
  scalper_bank_summary_10sl_12tp_ratchet.md
"""
import pandas as pd
import numpy as np
import pyarrow.parquet as pq
from itertools import combinations

CORPUS = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/scalper_corpus_10sl_12tp_ratchet.parquet"
OUT_CELLS = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/scalper_bank_cells_10sl_12tp_ratchet.csv"
OUT_FREQ  = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/scalper_bank_with_frequency_10sl_12tp_ratchet.csv"
OUT_MD    = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/scalper_bank_summary_10sl_12tp_ratchet.md"

MIN_N_CLEAN  = 13
MIN_POP_FRAC = 0.05
QUANTILES    = [0.20, 0.35, 0.50, 0.65, 0.80]
FACTOR_COLS  = ["ATR_ratio","BB_compress","ADX14","RSI14","price_pos","volume_ratio"]

def wilson_lb(wins, n, z=1.28):
    if n == 0: return 0.0
    p = wins / n
    return (p + z*z/(2*n) - z*np.sqrt(p*(1-p)/n + z*z/(4*n*n))) / (1 + z*z/n)

print("loading 10/12/ratchet corpus (projection)...", flush=True)
needed = ["technical_regime_53","pair","direction","family","entry_ts",
          "outcome_10sl_12tp_ratchet","realized_pips_estimated",
          "is_win_10sl_12tp_ratchet","is_clean_10sl_12tp_ratchet",
          "session_bucket","hour_utc"] + FACTOR_COLS
df = pq.read_table(CORPUS, columns=needed).to_pandas()
print(f"corpus rows: {len(df):,}", flush=True)

df["entry_ts"] = pd.to_datetime(df.entry_ts, utc=True)
weeks = (df.entry_ts.max() - df.entry_ts.min()).days / 7.0
print(f"weeks: {weeks:.0f}", flush=True)

df = df[df.family.isin(["direct","dbb_trend","reversal"])]
print(f"after family filter: {len(df):,}", flush=True)

sigs = df[["technical_regime_53","pair","direction","family"]].drop_duplicates()
print(f"signatures: {len(sigs)}", flush=True)

# Precompute clean flag
df["_is_clean"] = df.is_clean_10sl_12tp_ratchet
df["_pips"] = df.realized_pips_estimated.fillna(0.0)

winners = []
for sig_i, sig in enumerate(sigs.itertuples(index=False)):
    rg, pair, dirn, fam = sig.technical_regime_53, sig.pair, sig.direction, sig.family
    sub = df[(df.technical_regime_53 == rg) & (df.pair == pair)
             & (df.direction == dirn) & (df.family == fam)]
    if len(sub) < MIN_N_CLEAN * 4: continue
    base_clean = sub[sub._is_clean]
    if len(base_clean) < MIN_N_CLEAN: continue
    base_ev = base_clean._pips.mean()
    base_wr = base_clean.is_win_10sl_12tp_ratchet.mean()

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

    all_rules = [[]] + [[s] for s in splits]
    for d1, d2 in combinations(splits, 2):
        if d1[0] == d2[0]: continue
        all_rules.append([d1, d2])

    best = None
    for clauses in all_rules:
        if clauses:
            mask = eval_mask(clauses)
            kept = sub[mask]
        else:
            kept = sub
        if clauses and len(kept) / len(sub) < MIN_POP_FRAC: continue
        kept_clean = kept[kept._is_clean]
        n_c = len(kept_clean)
        if n_c < MIN_N_CLEAN: continue
        ev_pips = kept_clean._pips.mean()
        if ev_pips <= 0: continue
        wins_c = int(kept_clean.is_win_10sl_12tp_ratchet.sum())
        wr_c = wins_c / n_c
        n_amb = int((kept.outcome_10sl_12tp_ratchet.isin(["ambiguous_win_or_stop","ambiguous_other"])).sum())
        amb_rate = n_amb / max(1, len(kept))
        total_kept = len(kept)
        fpw = total_kept / weeks
        clean_fpw = n_c / weeks
        expected_pips_per_week = clean_fpw * ev_pips
        rule = "(no filter)" if not clauses else " AND ".join(f"{c[0]}{c[1]}{c[2]:.6g}" for c in clauses)
        cand = {
            "regime": rg, "pair": pair, "direction": dirn, "family": fam,
            "rule": rule, "rule_depth": len(clauses),
            "n_clean": n_c, "wins_clean": wins_c, "wr_clean": wr_c,
            "expected_pips_per_trade": ev_pips,
            "expected_pips_per_week": expected_pips_per_week,
            "fires_per_week": fpw,
            "clean_fires_per_week": clean_fpw,
            "fires_per_month": fpw * 4.33,
            "activations_per_month": clean_fpw * 4.33,
            "ambiguity_rate": amb_rate,
            "wilson_lb": wilson_lb(wins_c, n_c),
            "baseline_clean_ev_pips": base_ev,
            "baseline_clean_wr": base_wr,
            "pop_kept_frac": len(kept) / len(sub),
        }
        if best is None or cand["expected_pips_per_week"] > best["expected_pips_per_week"]:
            best = cand
    if best:
        winners.append(best)

if not winners:
    print("ZERO cells.")
    raise SystemExit(0)
out = pd.DataFrame(winners).sort_values("expected_pips_per_week", ascending=False)
out["freq_class"] = pd.cut(out.fires_per_week, [0,0.25,1,3,1e9],
                          labels=["GHOST","RARE","MODERATE","REGULAR"])
out.to_csv(OUT_CELLS, index=False)
out.to_csv(OUT_FREQ, index=False)

print(f"\n=== bank cells: {len(out)} ===")
print(out.groupby("freq_class").agg(
    cells=("rule","count"),
    median_fpw=("fires_per_week","median"),
    median_clean_wr=("wr_clean","median"),
    median_ev_pips_per_trade=("expected_pips_per_trade","median"),
    median_ev_pips_per_week=("expected_pips_per_week","median"),
).reindex(["REGULAR","MODERATE","RARE","GHOST"]).to_string())
print()
print("=== TOP 30 BY expected_pips_per_week ===")
print(out.head(30)[["pair","regime","direction","family","rule_depth",
                    "n_clean","wr_clean","expected_pips_per_trade",
                    "fires_per_week","expected_pips_per_week",
                    "ambiguity_rate","wilson_lb"]].to_string(index=False))

with open(OUT_MD,"w") as f:
    f.write("# Scalper Bank Summary — 10-pip SL / 12-pip TP1 / ratchet\n\n")
    f.write(f"Built 2026-05-21 from `scalper_corpus_10sl_12tp_ratchet.parquet` ({len(df):,} rows, {weeks:.0f} weeks).\n\n")
    f.write(f"Objective: `clean_fires_per_week × expected_pips_per_trade` with depth-1 / depth-2 factor splits.\n")
    f.write(f"Bars: n_clean>=13, pop_kept>=5%, expected_pips_per_trade>0.\n\n")
    f.write(f"**Total cells: {len(out)}**\n\n")
    f.write(f"## Frequency class distribution\n\n```\n")
    f.write(out.groupby("freq_class").agg(
        cells=("rule","count"),
        median_fpw=("fires_per_week","median"),
        median_clean_wr=("wr_clean","median"),
        median_ev_pips_per_trade=("expected_pips_per_trade","median"),
        median_ev_pips_per_week=("expected_pips_per_week","median"),
    ).reindex(["REGULAR","MODERATE","RARE","GHOST"]).to_string())
    f.write("\n```\n\n")
    f.write(f"## Top 25 cells (by expected_pips_per_week)\n\n")
    f.write("| pair | regime | dir | family | rule | depth | n_clean | WR | E[pips]/trade | fires/wk | E[pips]/wk | amb_rate | wilson_lb |\n")
    f.write("|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|\n")
    for _, r in out.head(25).iterrows():
        f.write(f"| {r.pair} | {r.regime} | {r.direction} | {r.family} | `{r.rule}` | {int(r.rule_depth)} | {int(r.n_clean)} | {r.wr_clean:.3f} | {r.expected_pips_per_trade:+.2f} | {r.fires_per_week:.2f} | {r.expected_pips_per_week:+.2f} | {r.ambiguity_rate:.2f} | {r.wilson_lb:.3f} |\n")
    f.write(f"\n## Caveats\n\n")
    f.write(f"- Ambiguous bin (~69%) was excluded from the per-cell WR; cells with low ambiguity rate are more trustworthy.\n")
    f.write(f"- Ratchet `_likely` outcomes assume favorable MFE happened before adverse MAE; OHLC refinement is the next pass.\n")
    f.write(f"- Frequency class uses `fires_per_week` (total kept, including ambiguous) not clean-only. The bot will actually see all the rows; the ambiguous ones won't reliably win or lose.\n")

print(f"\nwrote {OUT_CELLS}")
print(f"wrote {OUT_FREQ}")
print(f"wrote {OUT_MD}")
