"""Build v10_fast_v1.2 = current 14 + surgical JPY overlay.

Selection rule per Brock 2026-05-18:
- C02 first, TF6_ma_ribbon_long
- 4 pairs seen heavily in today's telemetry: AUD/GBP/CHF/USD JPY
- 3 active sessions seen in today's telemetry: london_open, ny_open, ny_mid
- trade tier only (Seed-Pro / Pro / Elite)
- 4 sigs x 3 sessions = 12 JPY rows added
"""
import pandas as pd

v10 = pd.read_parquet("data/routing_table_v10_fast_v1_1.parquet")
v9 = pd.read_parquet("data/routing_table_v9_observe.parquet")

ACTIVE_SESSIONS = {"london_open", "ny_open", "ny_mid"}
TRADE_TIERS = {"Seed-Pro", "Pro", "Elite"}
JPY_TARGET_PAIRS = {"AUD_JPY", "GBP_JPY", "CHF_JPY", "USD_JPY"}

c02_filter = (
    v9.pair.isin(JPY_TARGET_PAIRS)
    & (v9.parent_regime == "C02")
    & (v9.strategy == "TF6_ma_ribbon_long")
    & v9.tier.isin(TRADE_TIERS)
    & v9.session_bucket.isin(ACTIVE_SESSIONS)
)
c02_rows = v9[c02_filter].copy()
print(f"C02 JPY adds: {len(c02_rows)} rows")
print(c02_rows[["parent_regime","pair","strategy","direction","session_bucket","tier","wr","wilson_lb","n_unique"]].to_string(index=False))

c02_rows["promote_source"] = "v9_observe_jpy_overlay_2026-05-18"

v1_2 = pd.concat([v10, c02_rows[v10.columns]], ignore_index=True)
print()
print(f"v10_fast_v1.2 total cells: {len(v1_2)}")
print(f"  current cells: {len(v10)}")
print(f"  JPY additions: {len(c02_rows)}")
print()
print("v1.2 by pair:")
print(v1_2.groupby("pair").size().sort_values(ascending=False).to_string())
print()
print("v1.2 by tier:")
print(v1_2.groupby("tier").size().to_string())

out = "data/routing_table_v10_fast_v1_2.parquet"
v1_2.to_parquet(out, index=False)
print(f"\nwrote {out}")
