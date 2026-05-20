"""v10_fast_v1.5: bank-driven expansion (+7 cells, top-session-only).

Driven by the bank schedule map (research/.../bank_schedule_map_2026-05-19.py):
the 7 highest-evidence trade-tier signatures absent from v1.4, each
deployed on its single 'top_session_by_winners' (honest, not fanned).

Adds 162 historical winners (+72% over v1.4 coverage) without any
synthetic session expansion.
"""
import pandas as pd

V14_PATH = "data/routing_table_v10_fast_v1_4.parquet"
V9_PATH = "data/routing_table_v9_observe.parquet"

# (regime, pair, direction, strategy, top_session_only)
TARGETS = [
    ("C01", "USD_JPY", "short", "echo_box_fade_v2",                  "ny_close"),
    ("C01", "GBP_NZD", "long",  "alpha_breakout_retest_v2",          "ny_open"),
    ("C01", "EUR_AUD", "short", "alpha_pullback_v2",                 "asia"),
    ("C01", "NZD_USD", "long",  "alpha_pullback_v2",                 "london_open"),
    ("C01", "USD_CHF", "long",  "echo_box_fade_v2",                  "ny_mid"),
    ("C02", "EUR_NZD", "long",  "charlie_pullback_continuation_v2",  "ny_mid"),
    ("C02", "GBP_NZD", "long",  "charlie_pullback_continuation_v2",  "asia"),
]

v14 = pd.read_parquet(V14_PATH)
v9 = pd.read_parquet(V9_PATH)

print(f"v1.4 base: {len(v14)} rows")

add_rows = []
for regime, pair, direction, strategy, session in TARGETS:
    match = v9[
        (v9.parent_regime == regime)
        & (v9.pair == pair)
        & (v9.direction == direction)
        & (v9.strategy == strategy)
        & (v9.session_bucket == session)
    ]
    if len(match) == 0:
        print(f"  MISSING: {regime}/{pair}/{direction}/{strategy}/{session}")
        continue
    if len(match) > 1:
        print(f"  WARN multiple rows for {regime}/{pair}/{direction}/{strategy}/{session}: {len(match)}; taking first")
    row = match.iloc[0].copy()
    add_rows.append(row)
    print(f"  + {regime}/{pair:<8}/{direction:<5}/{strategy:<35}/{session:<11}  "
          f"tier={row.tier:<8} wr={row.wr:.3f} wlb={row.wilson_lb:.3f} n={int(row.n_unique)}")

add_df = pd.DataFrame(add_rows)
print(f"\nadds: {len(add_df)} rows")

if "promote_source" not in add_df.columns:
    add_df["promote_source"] = "bank_schedule_map_top_session_2026-05-20"
else:
    add_df["promote_source"] = "bank_schedule_map_top_session_2026-05-20"

v1_5 = pd.concat([v14, add_df[v14.columns]], ignore_index=True)
print(f"\nv10_fast_v1.5 total: {len(v1_5)} rows  unique leaves: {len(v1_5.drop_duplicates(['parent_regime','pair','direction','strategy','session_bucket']))}")
print()
print("v1.5 by family:")
print(v1_5.groupby("family").size().to_string())
print()
print("v1.5 by tier:")
print(v1_5.groupby("tier").size().to_string())
print()
print("v1.5 by session_bucket:")
print(v1_5.groupby("session_bucket").size().sort_values(ascending=False).to_string())
print()
print("v1.5 by pair:")
print(v1_5.groupby("pair").size().sort_values(ascending=False).to_string())

out = "data/routing_table_v10_fast_v1_5.parquet"
v1_5.to_parquet(out, index=False)
print(f"\nwrote {out}")
