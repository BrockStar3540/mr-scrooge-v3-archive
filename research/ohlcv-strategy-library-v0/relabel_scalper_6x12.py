"""Workstream #1: Streaming scalper relabeler (memory-bounded).

Per-file: load -> filter -> classify -> append to ParquetWriter.
Keeps peak memory ~700MB for the largest single pair file.
"""
import glob
import os
import pandas as pd
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq

TRADE_LOG_GLOB = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/trade_log_all_*.parquet"
OUT_PARQUET = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/scalper_corpus_6x12.parquet"
OUT_CSV     = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/scalper_trade_labels.csv"
OUT_MD      = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/scalper_labeling_summary.md"

SCALP_SL_PIPS = 6.0
SCALP_TP_PIPS = 12.0

def pip_size_for(pair):
    return 0.01 if ("JPY" in pair or "MXN" in pair) else 0.0001

def family_for(sid):
    sid = (sid or "").lower()
    if any(k in sid for k in ("breakout_retest", "echo_box_fade", "compression_breakout", "alpha_pullback", "extended_fade")): return "direct"
    if any(k in sid for k in ("tf6_ma_ribbon", "tf3_supertrend", "pullback_continuation")): return "dbb_trend"
    if any(k in sid for k in ("failed_momentum", "bb_lower_reclaim")): return "reversal"
    return "other"

OUT_COLS = ["pair","strategy_id","family","category","direction","entry_ts",
            "technical_regime_53","technical_regime_desc","session_bucket","hour_utc",
            "entry_price","stop_loss",
            "original_R_in_pips","scalp_tp_R","scalp_sl_R",
            "mfe_R","mae_R","mfe_pips","mae_pips",
            "realized_R","exit_reason","is_win",
            "scalp_outcome","is_win_6x12",
            "ADX14","ATR_ratio","BB_compress","RSI14","price_pos","volume_ratio","era"]

paths = sorted(glob.glob(TRADE_LOG_GLOB))
print(f"loading {len(paths)} trade log files (streaming mode)...", flush=True)

# Counters
total = 0
clean_win = 0
clean_loss = 0
ambiguous = 0
neither = 0
old_win = 0

# Per-signature aggregator for bank-building (clean-only)
sig_n = {}
sig_w = {}

writer = None
sample_for_csv = []

for i, p in enumerate(paths):
    pair_name = os.path.basename(p).replace("trade_log_all_", "").replace(".parquet", "").upper()
    df = pd.read_parquet(p)
    if "mfe_R" not in df.columns or "mae_R" not in df.columns:
        print(f"  skip {pair_name}: missing MFE/MAE", flush=True)
        continue
    n_in = len(df)
    df = df.dropna(subset=["entry_price","stop_loss","mfe_R","mae_R"])
    df["pip_size"] = pip_size_for(pair_name)
    df["original_R_in_pips"] = (df.entry_price - df.stop_loss).abs() / df.pip_size
    df = df[df.original_R_in_pips > 0.5]
    df["scalp_tp_R"] = SCALP_TP_PIPS / df.original_R_in_pips
    df["scalp_sl_R"] = SCALP_SL_PIPS / df.original_R_in_pips

    tp_hit = df.mfe_R >= df.scalp_tp_R
    sl_hit = df.mae_R >= df.scalp_sl_R
    outcome = np.full(len(df), "neither", dtype=object)
    outcome[tp_hit & ~sl_hit] = "clean_win"
    outcome[~tp_hit & sl_hit] = "clean_loss"
    outcome[tp_hit & sl_hit] = "ambiguous"
    df["scalp_outcome"] = outcome
    df["is_win_6x12"] = (df.scalp_outcome == "clean_win")
    df["mfe_pips"] = df.mfe_R * df.original_R_in_pips
    df["mae_pips"] = df.mae_R * df.original_R_in_pips
    df["family"] = df.strategy_id.map(family_for)

    # Counters
    total += len(df)
    cw = int((df.scalp_outcome == "clean_win").sum())
    cl = int((df.scalp_outcome == "clean_loss").sum())
    amb = int((df.scalp_outcome == "ambiguous").sum())
    neither_n = int((df.scalp_outcome == "neither").sum())
    clean_win += cw; clean_loss += cl; ambiguous += amb; neither += neither_n
    if "is_win" in df.columns:
        old_win += int(df.is_win.sum())

    # Per-signature aggregation (clean only)
    clean_mask = df.scalp_outcome.isin(["clean_win","clean_loss"])
    clean = df[clean_mask]
    if len(clean):
        grp = clean.groupby(["technical_regime_53","pair","direction","family"]).agg(
            n=("is_win_6x12","count"),
            w=("is_win_6x12","sum"),
        )
        for key, row in grp.iterrows():
            sig_n[key] = sig_n.get(key, 0) + int(row["n"])
            sig_w[key] = sig_w.get(key, 0) + int(row["w"])

    # Output write
    out_df = df.reindex(columns=OUT_COLS)
    table = pa.Table.from_pandas(out_df, preserve_index=False)
    if writer is None:
        writer = pq.ParquetWriter(OUT_PARQUET, table.schema)
    writer.write_table(table)

    # Sample for CSV
    if len(out_df) > 0:
        sample_for_csv.append(out_df.sample(n=min(200, len(out_df)), random_state=42))

    print(f"  {i+1:>2}/{len(paths)}  {pair_name:<10}  in={n_in:>7,}  out={len(df):>7,}  win={cw:>6,}  loss={cl:>6,}  amb={amb:>6,}  neither={neither_n:>6,}", flush=True)

if writer:
    writer.close()
print(f"\nwrote {OUT_PARQUET}", flush=True)

if sample_for_csv:
    pd.concat(sample_for_csv, ignore_index=True).to_csv(OUT_CSV, index=False)
    print(f"wrote {OUT_CSV}", flush=True)

# Markdown summary
clean_total = clean_win + clean_loss
clean_wr = clean_win / clean_total if clean_total else 0.0
worst_wr = clean_win / total if total else 0.0
best_wr = (clean_win + ambiguous) / total if total else 0.0
old_wr = old_win / total if total else 0.0

with open(OUT_MD, "w") as f:
    f.write(f"# Scalper Relabeling Summary (6 pip SL / 12 pip TP)\n\n")
    f.write(f"Generated 2026-05-21 (streaming pass over {len(paths)} per-pair trade_log files).\n\n")
    f.write(f"**Total events after sanity filters**: {total:,}\n\n")
    f.write(f"## Outcome distribution under 6/12 first-touch\n\n")
    f.write(f"| outcome | count | pct |\n|---|---:|---:|\n")
    f.write(f"| **clean_win** (touched +12 before -6) | {clean_win:,} | {clean_win/total:.1%} |\n")
    f.write(f"| **clean_loss** (touched -6 before +12) | {clean_loss:,} | {clean_loss/total:.1%} |\n")
    f.write(f"| ambiguous (both touched, order unknown) | {ambiguous:,} | {ambiguous/total:.1%} |\n")
    f.write(f"| neither (trade closed inside the band) | {neither:,} | {neither/total:.1%} |\n\n")
    f.write(f"## Win-rate bounds\n\n")
    f.write(f"- **Clean-only WR**: {clean_wr:.3f}\n")
    f.write(f"- **Worst-case WR**: {worst_wr:.3f}\n")
    f.write(f"- **Best-case WR**: {best_wr:.3f}\n")
    f.write(f"- **Old `is_win` WR**: {old_wr:.3f}\n\n")
    if clean_wr > old_wr:
        f.write(f"**Scalper resolution lifts clean WR from {old_wr:.3f} to {clean_wr:.3f} (+{(clean_wr-old_wr)*100:.1f} pts)**\n\n")
    f.write(f"## Top signatures by n (clean-only) — sneak peek\n\n")
    rows = []
    for k in sig_n:
        if sig_n[k] >= 20:
            rg, pair, d, fam = k
            wr = sig_w[k] / sig_n[k]
            rows.append((rg, pair, d, fam, sig_n[k], sig_w[k], wr))
    rows.sort(key=lambda r: -r[4])
    f.write(f"| regime | pair | dir | family | n | wins | WR |\n|---|---|---|---|---:|---:|---:|\n")
    for rg, pair, d, fam, n, w, wr in rows[:25]:
        f.write(f"| {rg} | {pair} | {d} | {fam} | {n} | {w} | {wr:.3f} |\n")
print(f"wrote {OUT_MD}", flush=True)
print("\n=== FINAL ===")
print(f"total events: {total:,}")
print(f"clean_win:    {clean_win:,} ({clean_win/total:.1%})")
print(f"clean_loss:   {clean_loss:,} ({clean_loss/total:.1%})")
print(f"ambiguous:    {ambiguous:,} ({ambiguous/total:.1%})")
print(f"neither:      {neither:,} ({neither/total:.1%})")
print(f"clean WR:     {clean_wr:.3f}  (vs old is_win WR: {old_wr:.3f})")
