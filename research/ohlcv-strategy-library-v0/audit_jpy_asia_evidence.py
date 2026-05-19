"""Audit whether the 4 JPY signatures in v9_observe have GENUINE asia-session
evidence at row level, vs. synthetic fan-outs from the v9 builder.

For each signature (parent_regime, pair, strategy, direction):
  1. The v9 cell's shave_rule -- does it self-restrict to non-asia sessions?
  2. The underlying ml_training_corpus row counts in session_bucket=asia
  3. The asia-only WR
  4. Whether any shadow rows today flagged shave_rule_satisfied on asia
"""
import json
import pandas as pd

V9_PATH = "data/routing_table_v9_observe.parquet"
CORPUS_PATH = "research/routing-table-v2-2026-05-14/ml_training_corpus.parquet"
TELEMETRY_PATH = "data/seed-telemetry.jsonl"

SIGS = [
    ("C02", "AUD_JPY", "TF6_ma_ribbon_long", "long"),
    ("C02", "GBP_JPY", "TF6_ma_ribbon_long", "long"),
    ("C02", "CHF_JPY", "TF6_ma_ribbon_long", "long"),
    ("C02", "USD_JPY", "TF6_ma_ribbon_long", "long"),
]

print("=" * 80)
print("V9 CELL: shave_rule + tier per signature")
print("=" * 80)
v9 = pd.read_parquet(V9_PATH)
for sig in SIGS:
    regime, pair, strat, direction = sig
    row = v9[
        (v9.parent_regime == regime)
        & (v9.pair == pair)
        & (v9.strategy == strat)
        & (v9.direction == direction)
        & (v9.session_bucket == "asia")
    ]
    if len(row) == 0:
        print(f"  {sig}: NO ROW IN V9 for asia session")
        continue
    r = row.iloc[0]
    print(f"  {sig}:")
    print(f"    tier={r.tier}  wr={r.wr:.3f}  wilson_lb={r.wilson_lb:.3f}  n_unique={r.n_unique}")
    print(f"    shave_rule={r.shave_rule!r}")
    print(f"    source_bank={r.source_bank}")

print()
print("=" * 80)
print("CORPUS: actual asia-session row counts + WR per signature")
print("=" * 80)
corpus = pd.read_parquet(CORPUS_PATH)
print(f"corpus rows: {len(corpus):,}  cols: {list(corpus.columns)[:20]}")
print(f"  session_bucket values: {sorted(corpus.session_bucket.dropna().unique().tolist()) if 'session_bucket' in corpus.columns else 'N/A'}")
print()

# Probe 2x dedup -- match the v9 builder
if "probe_seq" in corpus.columns:
    # dedup pairs by halving probe rows
    corpus_d = corpus.copy()
    print(f"  probe_seq values: {corpus.probe_seq.value_counts().head().to_dict()}")
else:
    corpus_d = corpus.copy()

for sig in SIGS:
    regime, pair, strat, direction = sig
    # Try several strategy column names
    strat_col = None
    for c in ("root_strategy_id", "strategy_id", "strategy", "strategy_name"):
        if c in corpus.columns:
            strat_col = c
            break
    direction_col = "direction" if "direction" in corpus.columns else None
    regime_col = "technical_regime_53" if "technical_regime_53" in corpus.columns else None
    pair_col = "pair" if "pair" in corpus.columns else "symbol"

    if not all([strat_col, direction_col, regime_col, pair_col]):
        print(f"  missing column: strat={strat_col} dir={direction_col} regime={regime_col} pair={pair_col}")
        break

    base = corpus_d[
        (corpus_d[regime_col] == regime)
        & (corpus_d[pair_col] == pair)
        & (corpus_d[strat_col] == strat)
        & (corpus_d[direction_col] == direction)
    ]
    if len(base) == 0:
        print(f"  {sig}: 0 corpus rows (strat may need different name)")
        continue

    # Probe dedup -- v9 used probe 2x divide; emulate by keeping unique trade_id
    if "trade_id" in base.columns:
        base_d = base.drop_duplicates("trade_id")
    else:
        base_d = base
    asia = base_d[base_d.session_bucket == "asia"] if "session_bucket" in base_d.columns else pd.DataFrame()
    all_sess_wr = base_d.is_win.mean() if "is_win" in base_d.columns else float("nan")
    asia_wr = asia.is_win.mean() if len(asia) and "is_win" in asia.columns else float("nan")
    print(f"  {sig}:")
    print(f"    total unique rows: {len(base_d):,}  (raw: {len(base):,})")
    print(f"    asia unique rows:  {len(asia):,}  asia_WR={asia_wr:.3f}  all_WR={all_sess_wr:.3f}")
    if len(asia) > 0 and "session_bucket" in base_d.columns:
        print(f"    session distribution: {base_d.session_bucket.value_counts().to_dict()}")

print()
print("=" * 80)
print("TELEMETRY: any asia shadow-passes today for these signatures?")
print("=" * 80)
hits = 0
asia_passes = 0
asia_blocks = {}
with open(TELEMETRY_PATH) as f:
    for line in f:
        try: r = json.loads(line)
        except: continue
        sym = r.get("symbol","")
        if not any(sym == p for _,p,_,_ in SIGS): continue
        if r.get("regime53") != "C02": continue
        if r.get("session_bucket") != "asia": continue
        if r.get("direction") != "long": continue
        hits += 1
        cell_strat = r.get("cell_strategy") or ""
        br = r.get("block_reason","")
        if cell_strat == "TF6_ma_ribbon_long":
            if "shave_rule_satisfied" in br or r.get("passed"):
                asia_passes += 1
            asia_blocks[br[:80]] = asia_blocks.get(br[:80], 0) + 1
print(f"  asia C02 long candidates for these 4 pairs: {hits}")
print(f"  matched a TF6_ma_ribbon_long cell: {sum(asia_blocks.values())}")
print(f"  shave_rule_satisfied (cell passed): {asia_passes}")
print(f"  block reasons against TF6 cell during asia:")
for k, v in sorted(asia_blocks.items(), key=lambda x:-x[1])[:10]:
    print(f"    {v:>4}  {k}")
