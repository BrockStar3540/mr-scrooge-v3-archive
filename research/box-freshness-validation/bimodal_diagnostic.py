"""Bimodal diagnostic on box_age_hours.

Question: are fresh (<48h) and stale (>168h) boxes produced by different mechanisms?

Hypotheses to test:
  H1: Stale boxes are weekend-gap artifacts (Monday entries on Friday boxes)
  H2: Stale boxes are alt-box-system entries (V3 has primary vs alternative box paths)
  H3: Stale boxes cluster in specific bug windows (B-068 to B-074)
  H4: Stale boxes happen across all otherwise-valid trades
  H5: factor_box_age_hours and factor_ctx_box_age_hours encode different things
  H6: Stale boxes correlate with regime state (e.g., RESTRICTED or alt-box flagged)

Cross-tabs needed:
  fresh/stale × { pair_family, session_bucket, weekday, hour_utc,
                  bot_actual_strategy, regime_id, regime_score,
                  box_boundary_context (bug exposure), ctx_box presence,
                  repair_taxonomy }
"""
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timezone

LEDGER = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/box-freshness-validation")

df = pd.read_parquet(LEDGER)
mask = (
    df["source_label"].isin(["bot_actual_winner", "bot_actual_loser"]) &
    df["factor_box_age_hours"].notna()
)
pool = df[mask].copy()
pool["box_age"] = pd.to_numeric(pool["factor_box_age_hours"], errors="coerce")
pool["realized_r"] = pd.to_numeric(pool["actual_realized_r"], errors="coerce")
pool["is_winner"] = pool["realized_r"] > 0
pool["entry_ts"] = pd.to_datetime(pool["entry_ts"], utc=True, errors="coerce")

# Note: INCLUDE contaminated rows in the bimodal diagnostic (we want to see if
# stale boxes correlate with bug windows, so exclusion would mask the signal)
print(f"diagnostic pool: {len(pool)} broker rows with box_age (including contaminated)")

# Buckets
pool["box_age_bucket"] = np.where(
    pool["box_age"] < 48, "fresh<48",
    np.where(pool["box_age"] > 168, "stale>168", "middle_48_168")
)
print(f"\nbucket distribution:")
print(pool["box_age_bucket"].value_counts().to_string())
print()

# =================================================================
# H1: weekend gap effect
# =================================================================
pool["weekday"] = pool["entry_ts"].dt.day_name().str[:3]
print("=== H1: WEEKEND GAP — entry weekday × box_age_bucket ===")
print(pool.groupby(["weekday", "box_age_bucket"]).size().unstack(fill_value=0).to_string())
print()
print("entries Monday-Tuesday split fresh/stale:")
monday_tuesday = pool[pool["weekday"].isin(["Mon", "Tue"])]
print(monday_tuesday["box_age_bucket"].value_counts().to_string())
print(f"\nmonday-only:")
mon = pool[pool["weekday"] == "Mon"]
print(mon["box_age_bucket"].value_counts().to_string())
print()

# =================================================================
# H2: alt-box system — compare factor_box_age vs factor_ctx_box_age
# =================================================================
print("=== H2: ALT-BOX vs PRIMARY-BOX SYSTEM ===")
pool["ctx_box_age"] = pd.to_numeric(pool["factor_ctx_box_age_hours"], errors="coerce")
# Does ctx_box_age differ from box_age?
both = pool.dropna(subset=["box_age", "ctx_box_age"])
print(f"  rows with both box_age and ctx_box_age: {len(both)}")
if len(both):
    print(f"  rows where they differ by >1h: {(abs(both['box_age'] - both['ctx_box_age']) > 1).sum()}")
    print(f"  box_age vs ctx_box_age stats:")
    print(f"    box_age:    min={both['box_age'].min():.1f} median={both['box_age'].median():.1f} max={both['box_age'].max():.1f}")
    print(f"    ctx_box_age: min={both['ctx_box_age'].min():.1f} median={both['ctx_box_age'].median():.1f} max={both['ctx_box_age'].max():.1f}")
print()

# Cross-tab: is ctx_box_age tracking the alt-box?
print("ctx_box_age presence (non-null) by box_age_bucket:")
pool["ctx_box_age_present"] = pool["ctx_box_age"].notna()
print(pool.groupby(["box_age_bucket", "ctx_box_age_present"]).size().unstack(fill_value=0).to_string())
print()

# =================================================================
# H3: bug-window correlation
# =================================================================
print("=== H3: BUG WINDOW EXPOSURE × box_age_bucket ===")
pool["has_bug_context"] = pool["box_boundary_context"].notna() & (pool["box_boundary_context"] != "None") & (pool["box_boundary_context"] != "")
print(pool.groupby(["box_age_bucket", "has_bug_context"]).size().unstack(fill_value=0).to_string())
print()
# Distinct bug contexts in stale bucket
stale = pool[pool["box_age_bucket"] == "stale>168"]
print(f"box_boundary_context distribution in STALE bucket:")
print(stale["box_boundary_context"].fillna("(no bug)").value_counts().to_string())
print()
fresh = pool[pool["box_age_bucket"] == "fresh<48"]
print(f"box_boundary_context distribution in FRESH bucket:")
print(fresh["box_boundary_context"].fillna("(no bug)").value_counts().to_string())
print()

# =================================================================
# H4: repair_taxonomy × box_age_bucket
# =================================================================
print("=== H4: REPAIR TAXONOMY × box_age_bucket ===")
print(pool.groupby(["repair_taxonomy", "box_age_bucket"]).size().unstack(fill_value=0).to_string())
print()

# =================================================================
# H5: regime state correlation
# =================================================================
print("=== H5: REGIME STATE (V1/V2 CAUTION/NORMAL/RESTRICTED via audit) × box_age_bucket ===")
# audit_classification is V1/V2 state
print("audit_classification × box_age_bucket:")
print(pool.groupby(["audit_classification", "box_age_bucket"]).size().unstack(fill_value=0).to_string())
print()
pool["regime_score_num"] = pd.to_numeric(pool["factor_regime_score"], errors="coerce")
pool["regime_conf_num"] = pd.to_numeric(pool["factor_regime_confidence"], errors="coerce")
print("regime_score by bucket (median):")
print(pool.groupby("box_age_bucket")["regime_score_num"].agg(["median","mean","std","count"]).to_string())
print()
print("regime_confidence by bucket (median):")
print(pool.groupby("box_age_bucket")["regime_conf_num"].agg(["median","mean","std","count"]).to_string())
print()

# =================================================================
# H6: pair × bucket × session × strategy
# =================================================================
print("=== H6: PAIR_FAMILY × box_age_bucket ===")
print(pool.groupby(["pair_family", "box_age_bucket"]).size().unstack(fill_value=0).to_string())
print()
print("=== SESSION_BUCKET × box_age_bucket ===")
print(pool.groupby(["session_bucket", "box_age_bucket"]).size().unstack(fill_value=0).to_string())
print()
print("=== BOT_ACTUAL_STRATEGY × box_age_bucket ===")
print(pool.groupby("bot_actual_strategy", dropna=False)["box_age_bucket"].value_counts().unstack(fill_value=0).to_string())
print()
print("=== HOUR_UTC × box_age_bucket ===")
pool["hour_utc_num"] = pool["entry_ts"].dt.hour
print(pool.groupby(["hour_utc_num", "box_age_bucket"]).size().unstack(fill_value=0).to_string())
print()

# =================================================================
# Box range as proxy: what's the box_range distribution by bucket?
# Stale boxes might have wider/narrower boxes than fresh
# =================================================================
print("=== box_range BY BUCKET ===")
pool["box_range_num"] = pd.to_numeric(pool["factor_box_range"], errors="coerce")
print(pool.groupby("box_age_bucket")["box_range_num"].agg(["median","mean","std","count"]).to_string())
print()

# =================================================================
# wall_proximity by bucket (stale might be middle-of-box?)
# =================================================================
print("=== wall_proximity BY BUCKET ===")
pool["wall_prox_num"] = pd.to_numeric(pool["factor_wall_proximity"], errors="coerce")
print(pool.groupby("box_age_bucket")["wall_prox_num"].agg(["median","mean","std","count"]).to_string())
print()

# Save diagnostic to file
diag_out = OUT / "bimodal_diagnostic.csv"
pool[["ledger_id","pair","pair_family","direction","entry_ts","weekday","hour_utc_num",
      "session_bucket","bot_actual_strategy","box_age","ctx_box_age","box_range_num",
      "wall_prox_num","is_winner","repair_taxonomy","box_age_bucket",
      "box_boundary_context","audit_classification","regime_score_num","regime_conf_num"]].to_csv(diag_out, index=False)
print(f"\nfull row-level diagnostic saved: {diag_out}")
