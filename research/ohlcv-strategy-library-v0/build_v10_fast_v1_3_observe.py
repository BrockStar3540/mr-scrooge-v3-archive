"""Build v10_fast_v1.3 — observe-only artifact.

Per Brock 2026-05-18: the v9 builder synthesizes session rows from
session-agnostic cells (verified via audit_jpy_asia_evidence.py — the
source corpus has no session_bucket column). So the asia/asia_late JPY
rows are NOT row-level Asia-validated. Promote to observe-only;
do NOT flip the live trade table.

Composition:
  - 14 cells from v10_fast_v1.1 (NY-focused originals)
  - 12 cells from v1.2 (london_open / ny_open / ny_mid JPY adds)
  -  8 candidate asia + asia_late JPY rows (NEW, for shadow only)
  = 34 cells / 23 leaves

This file is written to disk but the live config is NOT flipped.
"""
import pandas as pd

v10_v1_2 = pd.read_parquet("data/routing_table_v10_fast_v1_2.parquet")
v9 = pd.read_parquet("data/routing_table_v9_observe.parquet")

OBSERVE_ONLY_SESSIONS = {"asia", "asia_late"}
TRADE_TIERS = {"Seed-Pro", "Pro", "Elite"}
JPY_TARGET_PAIRS = {"AUD_JPY", "GBP_JPY", "CHF_JPY", "USD_JPY"}

asia_filter = (
    v9.pair.isin(JPY_TARGET_PAIRS)
    & (v9.parent_regime == "C02")
    & (v9.strategy == "TF6_ma_ribbon_long")
    & v9.tier.isin(TRADE_TIERS)
    & v9.session_bucket.isin(OBSERVE_ONLY_SESSIONS)
)
asia_rows = v9[asia_filter].copy()
print(f"asia/asia_late JPY adds (observe-only): {len(asia_rows)}")
print(asia_rows[["parent_regime","pair","strategy","direction","session_bucket","tier","wr","wilson_lb","n_unique","shave_rule"]].to_string(index=False))

asia_rows["promote_source"] = "v9_synthetic_session_fanout_OBSERVE_ONLY_2026-05-18"

v1_3 = pd.concat([v10_v1_2, asia_rows[v10_v1_2.columns]], ignore_index=True)
print()
print(f"v10_fast_v1.3 (observe artifact) total cells: {len(v1_3)}")
print(f"  v1.2 inheritance: {len(v10_v1_2)}")
print(f"  observe-only JPY asia adds: {len(asia_rows)}")
print()
print("v1.3 cells by session_bucket:")
print(v1_3.groupby("session_bucket").size().sort_values(ascending=False).to_string())

out = "data/routing_table_v10_fast_v1_3.parquet"
v1_3.to_parquet(out, index=False)
print(f"\nwrote {out}")
print("** NOT flipped live. Config still points to v1.2. **")
