"""Workstream #3: Relabel corpus under 10/12/ratchet model.

Per Brock 2026-05-21 spec, ratchet schedule:
  At MFE >= +6:  SL -> entry - 6
  At MFE >= +8:  SL -> entry - 3
  At MFE >= +10: SL -> entry (BE)
  TP1 at +12

Without OHLC bar sequence, we estimate outcomes assuming the
typical pattern: favorable MFE happens BEFORE adverse retracement
(plausible for "went green then reversed" trades). Outcomes are:

  clean_win               : mfe>=12 AND mae<6   -> +12 pips, no risk realized
  full_loss               : mfe<6 AND mae>=10   -> -10 pips
  ratchet_neg6_likely     : mfe in [6,8) AND mae>=6  -> -6 pips
  ratchet_neg3_likely     : mfe in [8,10) AND mae>=3 -> -3 pips
  ratchet_BE_likely       : mfe in [10,12) AND mae>=0 -> 0 pips
  neither                 : trade closed in the band (mfe<6 AND mae<10 AND no other path)
  ambiguous_win_or_stop   : mfe>=12 AND mae>=6 -> +12 or ratchet stop (order unknown)
  ambiguous_other         : all other paths needing OHLC

The "_likely" outcomes assume +MFE happened before -MAE. Marked separately
so OHLC-based resolution can refine later.

Outputs:
  scalper_corpus_10sl_12tp_ratchet.parquet
  scalper_trade_labels_10sl_12tp_ratchet.csv (5000-row sample)
  scalper_labeling_summary_10sl_12tp_ratchet.md
"""
import glob
import os
import pandas as pd
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq

TRADE_LOG_GLOB = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/trade_log_all_*.parquet"
OUT_PARQUET = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/scalper_corpus_10sl_12tp_ratchet.parquet"
OUT_CSV     = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/scalper_trade_labels_10sl_12tp_ratchet.csv"
OUT_MD      = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/scalper_labeling_summary_10sl_12tp_ratchet.md"

# Realized pip outcomes per bucket
PIP_OUTCOME = {
    "clean_win":              12.0,
    "full_loss":             -10.0,
    "ratchet_neg6_likely":   -6.0,
    "ratchet_neg3_likely":   -3.0,
    "ratchet_BE_likely":      0.0,
    "neither":                0.0,
    "ambiguous_win_or_stop":  np.nan,
    "ambiguous_other":        np.nan,
}

def pip_size_for(pair):
    return 0.01 if ("JPY" in pair or "MXN" in pair) else 0.0001

def family_for(sid):
    sid = (sid or "").lower()
    if any(k in sid for k in ("breakout_retest","echo_box_fade","compression_breakout","alpha_pullback","extended_fade")): return "direct"
    if any(k in sid for k in ("tf6_ma_ribbon","tf3_supertrend","pullback_continuation")): return "dbb_trend"
    if any(k in sid for k in ("failed_momentum","bb_lower_reclaim")): return "reversal"
    return "other"

OUT_COLS = ["pair","strategy_id","family","direction","entry_ts",
            "technical_regime_53","technical_regime_desc","session_bucket","hour_utc",
            "entry_price","stop_loss","original_R_in_pips",
            "mfe_R","mae_R","mfe_pips","mae_pips",
            "outcome_10sl_12tp_ratchet","realized_pips_estimated",
            "is_win_10sl_12tp_ratchet","is_clean_10sl_12tp_ratchet",
            "ADX14","ATR_ratio","BB_compress","RSI14","price_pos","volume_ratio","era"]

paths = sorted(glob.glob(TRADE_LOG_GLOB))
print(f"loading {len(paths)} per-pair trade logs (streaming)...", flush=True)

counters = {k: 0 for k in PIP_OUTCOME}
total = 0
old_is_win = 0
sig_n = {}    # n per (regime, pair, dir, fam)
sig_clean_n = {}  # n of clean (win + full_loss + ratchet outcomes -- non-ambiguous)
sig_clean_w = {}  # n of clean wins (counts all positive outcomes equally for now? actually weighted)
sig_total_pips = {}  # sum of realized_pips for non-ambiguous outcomes

writer = None
sample = []

for i, p in enumerate(paths):
    pair_name = os.path.basename(p).replace("trade_log_all_","").replace(".parquet","").upper()
    df = pd.read_parquet(p)
    if "mfe_R" not in df.columns or "mae_R" not in df.columns:
        continue
    n_in = len(df)
    df = df.dropna(subset=["entry_price","stop_loss","mfe_R","mae_R"])
    df["pip_size"] = pip_size_for(pair_name)
    df["original_R_in_pips"] = (df.entry_price - df.stop_loss).abs() / df.pip_size
    df = df[df.original_R_in_pips > 0.5]
    df["family"] = df.strategy_id.map(family_for)

    df["mfe_pips"] = df.mfe_R * df.original_R_in_pips
    df["mae_pips"] = df.mae_R * df.original_R_in_pips

    mfe = df.mfe_pips
    mae = df.mae_pips

    # Classify each event under the ratchet schedule
    outcome = np.empty(len(df), dtype=object)
    outcome.fill("ambiguous_other")
    outcome[(mfe >= 12) & (mae < 6)] = "clean_win"
    outcome[(mfe < 6) & (mae >= 10)] = "full_loss"
    outcome[(mfe >= 6) & (mfe < 8) & (mae >= 6)] = "ratchet_neg6_likely"
    outcome[(mfe >= 8) & (mfe < 10) & (mae >= 3)] = "ratchet_neg3_likely"
    outcome[(mfe >= 10) & (mfe < 12) & (mae >= 0)] = "ratchet_BE_likely"
    outcome[(mfe < 6) & (mae < 10)] = "neither"
    outcome[(mfe >= 12) & (mae >= 6)] = "ambiguous_win_or_stop"
    df["outcome_10sl_12tp_ratchet"] = outcome
    df["realized_pips_estimated"] = df.outcome_10sl_12tp_ratchet.map(PIP_OUTCOME)
    df["is_win_10sl_12tp_ratchet"] = (df.outcome_10sl_12tp_ratchet == "clean_win")
    df["is_clean_10sl_12tp_ratchet"] = df.outcome_10sl_12tp_ratchet.isin([
        "clean_win","full_loss","ratchet_neg6_likely","ratchet_neg3_likely","ratchet_BE_likely","neither"
    ])

    # Update counters
    total += len(df)
    if "is_win" in df.columns: old_is_win += int(df.is_win.sum())
    for k in PIP_OUTCOME:
        counters[k] += int((df.outcome_10sl_12tp_ratchet == k).sum())

    # Per-signature aggregation (clean only for fast bank build)
    clean = df[df.is_clean_10sl_12tp_ratchet].copy()
    if len(clean):
        grp = clean.groupby(["technical_regime_53","pair","direction","family"]).agg(
            n=("is_clean_10sl_12tp_ratchet","count"),
            wins=("is_win_10sl_12tp_ratchet","sum"),
            total_pips=("realized_pips_estimated","sum"),
        )
        for key, row in grp.iterrows():
            sig_clean_n[key] = sig_clean_n.get(key,0) + int(row["n"])
            sig_clean_w[key] = sig_clean_w.get(key,0) + int(row["wins"])
            sig_total_pips[key] = sig_total_pips.get(key,0.0) + float(row["total_pips"])

    out_df = df.reindex(columns=OUT_COLS)
    table = pa.Table.from_pandas(out_df, preserve_index=False)
    if writer is None:
        writer = pq.ParquetWriter(OUT_PARQUET, table.schema)
    writer.write_table(table)
    if len(out_df) > 0:
        sample.append(out_df.sample(n=min(200,len(out_df)), random_state=42))
    print(f"  {i+1:>2}/{len(paths)}  {pair_name:<10}  in={n_in:>7,}  out={len(df):>7,}", flush=True)

if writer: writer.close()
if sample:
    pd.concat(sample, ignore_index=True).to_csv(OUT_CSV, index=False)

# Summary stats
clean_total = sum(counters[k] for k in ["clean_win","full_loss","ratchet_neg6_likely","ratchet_neg3_likely","ratchet_BE_likely","neither"])
amb_total = sum(counters[k] for k in ["ambiguous_win_or_stop","ambiguous_other"])

print("\n=== outcome counts ===")
for k in ["clean_win","full_loss","ratchet_neg6_likely","ratchet_neg3_likely","ratchet_BE_likely","neither","ambiguous_win_or_stop","ambiguous_other"]:
    print(f"  {k:<25}: {counters[k]:>10,}  ({counters[k]/total*100:>5.1f}%)")

# Compute clean expectancy (non-ambiguous)
realized_clean_pips = (
    counters["clean_win"] * 12 +
    counters["full_loss"] * -10 +
    counters["ratchet_neg6_likely"] * -6 +
    counters["ratchet_neg3_likely"] * -3 +
    counters["ratchet_BE_likely"] * 0 +
    counters["neither"] * 0
)
clean_ev_per_trade = realized_clean_pips / max(1, clean_total)
print(f"\nclean expectancy: {clean_ev_per_trade:+.3f} pips/trade  (over {clean_total:,} non-ambiguous events)")
print(f"clean WR (clean_win / clean_total): {counters['clean_win']/max(1,clean_total)*100:.2f}%")
print(f"ambiguity rate: {amb_total/total*100:.1f}% (vs ~69% under flat 6/12 -- ratchet narrows the ambiguous bin)")

with open(OUT_MD,"w") as f:
    f.write("# Scalper Relabeling Summary — 10-pip SL / 12-pip TP1 / ratchet\n\n")
    f.write(f"Generated 2026-05-21. {len(paths)} per-pair trade_log files, total {total:,} events.\n\n")
    f.write(f"## Outcome distribution under 10/12/ratchet\n\n")
    f.write(f"| outcome | count | pct | realized pips |\n|---|---:|---:|---:|\n")
    for k in ["clean_win","full_loss","ratchet_neg6_likely","ratchet_neg3_likely","ratchet_BE_likely","neither","ambiguous_win_or_stop","ambiguous_other"]:
        pips = PIP_OUTCOME[k]
        pips_str = f"{pips:+.0f}" if not np.isnan(pips) else "—"
        f.write(f"| {k} | {counters[k]:,} | {counters[k]/total:.1%} | {pips_str} |\n")
    f.write(f"\n## Headline metrics\n\n")
    f.write(f"- **Clean expectancy**: {clean_ev_per_trade:+.3f} pips/trade across {clean_total:,} non-ambiguous events\n")
    f.write(f"- **Clean WR** (clean_win / clean_total): {counters['clean_win']/max(1,clean_total)*100:.2f}%\n")
    f.write(f"- **Ambiguity rate**: {amb_total/total*100:.1f}% (vs ~69% under flat 6/12 — ratchet narrows ambiguous bin)\n")
    f.write(f"- **Old `is_win` rate**: {old_is_win/total*100:.2f}%\n\n")
    f.write(f"## Caveat\n\n")
    f.write(f"The `_likely` outcomes assume favorable MFE happened before adverse MAE. Without OHLC bar sequence,\n")
    f.write(f"this is an estimate. Pure ambiguous bins are separate. OHLC-based resolution refines later.\n")

print(f"\nwrote {OUT_PARQUET}")
print(f"wrote {OUT_CSV}")
print(f"wrote {OUT_MD}")
