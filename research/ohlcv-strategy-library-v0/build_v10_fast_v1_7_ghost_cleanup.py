"""v10_fast_v1.7: GHOST cleanup.

Per Brock 2026-05-20 deployment rule: cells firing <0.25/week (GHOSTS)
should not be live. Strip them from v1.6 -> v1.7.

Reads deployable_bank_with_frequency.csv for the freq_class assignments.
"""
import pandas as pd

V16 = "data/routing_table_v10_fast_v1_6.parquet"
FREQ_CSV = "research/ohlcv-strategy-library-v0/deployable_bank_with_frequency.csv"

v16 = pd.read_parquet(V16)
freq = pd.read_csv(FREQ_CSV)
print(f"v1.6 rows: {len(v16)}")
print(f"freq_audit rows: {len(freq)}")

# GHOST signatures (regime, pair, direction, strategy)
ghosts = freq[freq.freq_class == "GHOST"]
ghost_keys = set(zip(ghosts.regime, ghosts.pair, ghosts.direction, ghosts.strategy))
print(f"GHOST signatures: {len(ghost_keys)}")
for k in sorted(ghost_keys):
    print(f"  {k}")

# Drop GHOSTs from v1.6
def is_ghost(r):
    return (r["parent_regime"], r["pair"], r["direction"], r["strategy"]) in ghost_keys

mask = v16.apply(is_ghost, axis=1)
print(f"\nrows to drop from v1.6: {mask.sum()}")
print(v16[mask][["parent_regime","pair","direction","strategy","session_bucket","tier"]].to_string(index=False))

v17 = v16[~mask].copy()
print(f"\nv1.7 rows: {len(v17)}  (v1.6 had {len(v16)})")
print("v1.7 by pair:")
print(v17.groupby("pair").size().sort_values(ascending=False).to_string())
print("\nv1.7 by family:")
print(v17.groupby("family").size().sort_values(ascending=False).to_string())

out = "data/routing_table_v10_fast_v1_7.parquet"
v17.to_parquet(out, index=False)
print(f"\nwrote {out}")
