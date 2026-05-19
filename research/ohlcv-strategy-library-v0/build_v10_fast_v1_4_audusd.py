"""v10_fast_v1.4: surgical AUD_USD long C02 overlay (+3 cells)

Driven by live telemetry (london_open audit 2026-05-19 06:24Z-07:04Z):
  31 AUD_USD long C02 candidates blocked by entry_filter no_routing_match.
  v9_observe has Elite cell TF6_ma_ribbon_long for this tuple.

Cell properties:
  strategy   = TF6_ma_ribbon_long
  family     = dbb_trend
  tier       = Elite
  wr         = 0.6512
  wilson_lb  = 0.554
  n_unique   = 43
  shave_rule = RSI14>73.24 AND BB_compress>0.1742 AND BB_compress<=0.200982
              (session-agnostic, no hour_utc clause -- honest cell)

Sessions added: london_open, ny_open, ny_mid (matches v1.2 pattern).
TF3_supertrend_long Elite cell NOT included -- has hour_utc 12-15 clause
(would be inert outside NY hours; v9 builder fan-out artifact).
"""
import pandas as pd

v10_v1_2 = pd.read_parquet("data/routing_table_v10_fast_v1_2.parquet")
v9 = pd.read_parquet("data/routing_table_v9_observe.parquet")

ACTIVE_SESSIONS = {"london_open", "ny_open", "ny_mid"}
ADD_FILTER = (
    (v9.parent_regime == "C02")
    & (v9.pair == "AUD_USD")
    & (v9.direction == "long")
    & (v9.strategy == "TF6_ma_ribbon_long")
    & (v9.tier == "Elite")
    & v9.session_bucket.isin(ACTIVE_SESSIONS)
)
add_rows = v9[ADD_FILTER].copy()
print(f"AUD_USD long C02 Elite TF6_ma_ribbon_long adds: {len(add_rows)} rows")
print(add_rows[["parent_regime","pair","strategy","direction","session_bucket","tier","wr","wilson_lb","n_unique","shave_rule"]].to_string(index=False))

add_rows["promote_source"] = "telemetry_driven_audud_long_2026-05-19"

v1_4 = pd.concat([v10_v1_2, add_rows[v10_v1_2.columns]], ignore_index=True)
print()
print(f"v10_fast_v1.4 total cells: {len(v1_4)}")
print(f"  v1.2 inheritance: {len(v10_v1_2)}")
print(f"  v1.4 additions:   {len(add_rows)}")
print()
print("v1.4 by pair:")
print(v1_4.groupby("pair").size().sort_values(ascending=False).to_string())

out = "data/routing_table_v10_fast_v1_4.parquet"
v1_4.to_parquet(out, index=False)
print(f"\nwrote {out}")
