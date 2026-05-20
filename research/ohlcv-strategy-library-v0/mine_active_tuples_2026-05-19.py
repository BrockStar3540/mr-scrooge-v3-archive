"""Surgical mining pass for the 7 active uncovered tuples.

Per Brock 2026-05-19 23:30Z: A+B in parallel, not C. Mine only the active
slices the bot is generating candidates for right now. Do NOT promote to
live -- output a v1.5 candidate set for review.

Targets are the top-blocked exact tuples from today's seed-telemetry
(15:08Z onward, post-router-fallback patch).
"""
import sys
from pathlib import Path

# Import the existing miner functions
sys.path.insert(0, "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0")
from expand_telemetry_driven import (
    expand_live_gap, dedup_probe, family_for, session_bucket_for_hour,
    score, STRICT_MIN_N, STRICT_MIN_WR_LIVE_GAP, NEAR_MIN_N, NEAR_MIN_WR,
)

import pandas as pd
import pyarrow.parquet as pq

CORPUS_PATH = "/home/ubuntu/mr-scrooge-v3/research/routing-table-v2-2026-05-14/ml_training_corpus.parquet"
OUT_DIR = Path("/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/mining-2026-05-19-active")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Targets: top blocked tuples from today's telemetry post-15:08Z.
# Each row maps to (regime53, symbol, session_bucket, direction, candidate_family).
# candidate_family is what the BB-classifier-route emitted -- all "direct" here.
TARGETS = [
    # pair, regime, dir, session, blocked_count
    ("EUR_JPY",  "C02", "long",  "ny_mid",   107),
    ("NZD_USD",  "C02", "long",  "ny_mid",   107),
    ("CAD_JPY",  "C02", "short", "ny_mid",   100),
    ("USD_CAD",  "C02", "short", "ny_mid",    67),
    ("GBP_USD",  "C02", "short", "ny_mid",    66),
    ("GBP_CAD",  "C01", "short", "ny_mid",    66),
    ("EUR_NZD",  "C02", "short", "ny_mid",    52),
    ("USD_CAD",  "C02", "short", "ny_close",  48),
    ("NZD_USD",  "C02", "long",  "ny_close",  48),
    ("EUR_JPY",  "C02", "long",  "ny_close",  48),
    ("GBP_USD",  "C01", "short", "ny_mid",    45),
    ("GBP_CAD",  "C02", "short", "ny_close",  45),
    ("GBP_USD",  "C02", "short", "ny_close",  41),
    ("GBP_CAD",  "C02", "short", "ny_mid",    38),
    ("CAD_JPY",  "C02", "long",  "ny_close",  31),
]

targets_df = pd.DataFrame([
    {"regime53": t[1], "symbol": t[0], "direction": t[2],
     "session_bucket": t[3], "candidate_family": "direct",
     "blocked_count": t[4]}
    for t in TARGETS
])

print(f"=== Surgical mining: {len(targets_df)} active tuples ===")
print(targets_df.to_string(index=False))
print()

print(f"Loading corpus: {CORPUS_PATH}")
# Corpus schema check
schema = pq.read_schema(CORPUS_PATH)
available = {f.name for f in schema}
print(f"  available cols: {sorted(available)[:20]}...")
wanted = ["source", "strategy_id", "pair", "direction", "entry_ts",
          "is_win", "technical_regime_53", "hour_utc",
          "ATR_ratio", "BB_compress", "ADX14", "RSI14",
          "bb_position", "volume_ratio", "close_pos"]
cols = [c for c in wanted if c in available]
print(f"  loading: {cols}")
corpus = pq.read_table(CORPUS_PATH, columns=cols).to_pandas()
print(f"corpus rows: {len(corpus):,}")
print()

# Run the live-gap miner on these exact tuples
result = expand_live_gap(targets_df, corpus,
                         min_n=STRICT_MIN_N,
                         min_wr=STRICT_MIN_WR_LIVE_GAP)

print(f"\n=== mining output: {len(result)} rows ===")
if result.empty:
    print("NO HITS. Possible causes: zero corpus rows for these tuples,")
    print("family mismatch (corpus's 'direct' strategy_id may differ), or")
    print("hour_utc session-bucket mapping in corpus rows.")
else:
    # Join blocked_count for context
    result = result.merge(
        targets_df[["regime53","symbol","session_bucket","direction","blocked_count"]],
        left_on=["regime53","pair","session_bucket","direction"],
        right_on=["regime53","symbol","session_bucket","direction"],
        how="left",
    )
    print("\n=== STRICT WINNERS (deployable now) ===")
    sw = result[result.outcome_tier == "strict_winner"]
    if not sw.empty:
        print(sw[["pair","regime53","direction","session_bucket","child_rule",
                  "n_unique","wr_unique","wilson_lb","blocked_count"]].to_string(index=False))
    else:
        print("(none)")
    print()
    print("=== NEAR-MISS CANDIDATES (research queue) ===")
    nm = result[result.outcome_tier == "near_miss_candidate"]
    if not nm.empty:
        print(nm[["pair","regime53","direction","session_bucket","child_rule",
                  "n_unique","wr_unique","wilson_lb","blocked_count"]].to_string(index=False))
    else:
        print("(none)")
    print()
    print("=== DEAD (need more data or different approach) ===")
    dead = result[result.outcome_tier == "dead"]
    if not dead.empty:
        print(dead[["pair","regime53","direction","session_bucket","blocked_count"]].to_string(index=False))
    print()

    out_csv = OUT_DIR / "active_tuples_mining_2026-05-19.csv"
    result.to_csv(out_csv, index=False)
    print(f"wrote {out_csv}")
