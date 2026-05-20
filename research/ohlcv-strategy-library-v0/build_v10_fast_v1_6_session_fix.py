"""v10_fast_v1.6 = v1.5 with session corrections per actual shave_rule.

Two v1.5 cells were deployed on the wrong session because the bank's
top_session_by_winners derivation didn't honor embedded session_bucket
clauses in the shave_rule:

  1. USD_JPY C01 short echo_box_fade_v2
     - v1.5 deployed: ny_close
     - rule: session_bucket==london_open AND volume_ratio>=1.47619
     - CORRECT: london_open

  2. GBP_NZD C01 long alpha_breakout_retest_v2
     - v1.5 deployed: ny_open
     - rule: ATR_ratio<=0.0824531 AND session_bucket==asia
     - CORRECT: asia

The other 5 v1.5 cells have shave_rules with no session/hour clause, so
the top-session-only deploy strategy (asia / london_open / ny_mid)
remains valid; keep as-is.

No other changes from v1.5.
"""
import pandas as pd

V15 = "data/routing_table_v10_fast_v1_5.parquet"
V9 = "data/routing_table_v9_observe.parquet"

v15 = pd.read_parquet(V15)
v9 = pd.read_parquet(V9)

# 1. Drop the two wrong-session rows
drop_mask = (
    ((v15.parent_regime == "C01") & (v15.pair == "USD_JPY")
     & (v15.direction == "short") & (v15.strategy == "echo_box_fade_v2")
     & (v15.session_bucket == "ny_close"))
    | ((v15.parent_regime == "C01") & (v15.pair == "GBP_NZD")
       & (v15.direction == "long") & (v15.strategy == "alpha_breakout_retest_v2")
       & (v15.session_bucket == "ny_open"))
)
print(f"dropping {drop_mask.sum()} wrong-session rows:")
print(v15[drop_mask][["parent_regime","pair","direction","strategy","session_bucket","shave_rule"]].to_string(index=False))
v16 = v15[~drop_mask].copy()

# 2. Pull the corrected-session rows from v9
def lift(pair, regime, direction, strategy, true_session):
    m = v9[(v9.parent_regime==regime) & (v9.pair==pair) & (v9.direction==direction)
           & (v9.strategy==strategy) & (v9.session_bucket==true_session)]
    if len(m) == 0:
        raise SystemExit(f"missing v9 row for {regime}/{pair}/{direction}/{strategy}/{true_session}")
    row = m.iloc[0].copy()
    row["promote_source"] = "v1_6_session_correction_2026-05-20"
    return row

adds = [
    lift("USD_JPY","C01","short","echo_box_fade_v2","london_open"),
    lift("GBP_NZD","C01","long","alpha_breakout_retest_v2","asia"),
]
add_df = pd.DataFrame(adds)
print(f"\nadding {len(add_df)} corrected-session rows:")
print(add_df[["parent_regime","pair","direction","strategy","session_bucket","shave_rule"]].to_string(index=False))

v16 = pd.concat([v16, add_df[v16.columns]], ignore_index=True)
print(f"\nv10_fast_v1.6 total: {len(v16)} rows  unique leaves: {len(v16.drop_duplicates(['parent_regime','pair','direction','strategy','session_bucket']))}")

out = "data/routing_table_v10_fast_v1_6.parquet"
v16.to_parquet(out, index=False)
print(f"\nwrote {out}")
