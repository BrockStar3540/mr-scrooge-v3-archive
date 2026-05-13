"""Step 6 v2: direction-repair classification using audit's existing counterfactual.

Honest scope finding (v1 attempt failed):
  All 88 direction_repair_or_skip rows are AFTER 2026-04-13 (factor audit cutoff).
  V1 lookup against per_trade_factors_filled.csv.gz returned 0 nearby candidates
  for every row. Factor file simply doesn't reach.

  20 rows are Apr 14-17 (pre-V3-observer; no candidate stream exists at all)
  68 rows are Apr 20+ (V3 observer scans.jsonl available but heavy to query)

V2 approach: use the broker audit's existing `audit_best_counterfactual_r`.
  audit_best_counterfactual_model is `simple_2R` for all 88 — same-direction
  trade walked forward against a 2R target. Audit's verdict per row:
    +2.0 → same direction would have hit target (timing repair valid)
     0.0 → same direction never developed (skip)
    -1.0 → same direction would have lost too (skip; opposite worth checking)

This populates same_direction_timing_repair / skip_required cleanly.
The opposite-direction question is flagged as `opp_direction_unresolved` for
the -1.0 subset (where same direction failed = opposite is at least worth
asking about) and explicitly NOT answered without scans.jsonl follow-on.
"""
import pandas as pd
from pathlib import Path

LEDGER = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet")
CLUSTERS = Path("/home/ubuntu/mr-scrooge-v3/research/winner-clusters-v0/winner_clusters_v1.csv")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/direction-repair-lookup")

PAIR_FAMILY = {
    "EUR_USD":"usd_base","GBP_USD":"usd_base","AUD_USD":"usd_base","NZD_USD":"usd_base",
    "USD_JPY":"usd_base","USD_CHF":"usd_base","USD_CAD":"usd_base","USD_MXN":"usd_base",
    "EUR_GBP":"eur_cross","EUR_AUD":"eur_cross","EUR_NZD":"eur_cross","EUR_CAD":"eur_cross",
    "EUR_CHF":"eur_cross","EUR_JPY":"eur_cross",
    "GBP_AUD":"gbp_cross","GBP_NZD":"gbp_cross","GBP_CAD":"gbp_cross","GBP_CHF":"gbp_cross","GBP_JPY":"gbp_cross",
    "AUD_NZD":"antipodean_cross","AUD_CAD":"antipodean_cross","AUD_CHF":"antipodean_cross",
    "AUD_JPY":"antipodean_cross","NZD_JPY":"antipodean_cross","CAD_JPY":"antipodean_cross","CHF_JPY":"antipodean_cross",
}

df = pd.read_parquet(LEDGER)
target = df[df["repair_taxonomy"] == "direction_repair_or_skip"].copy()
target["entry_ts"] = pd.to_datetime(target["entry_ts"], utc=True, errors="coerce")
print(f"target rows: {len(target)}")

# Load winner clusters for nearest-cluster lookup
clusters = pd.read_csv(CLUSTERS)
clusters_dict = {}
for _, c in clusters.iterrows():
    if c["is_cluster"]:
        key = (c["strategy"], c["pair_family"], c["session"], c["direction"])
        clusters_dict[key] = c["cluster_id"]

cutoff_v3 = pd.Timestamp("2026-04-20", tz="UTC")

results = []
for idx, row in target.iterrows():
    pair = row["pair"]
    pf = PAIR_FAMILY.get(pair, "other")
    bot_dir = row["direction"]
    entry_ts = row["entry_ts"]
    cf_r = pd.to_numeric(row.get("audit_best_counterfactual_r"), errors="coerce")
    actual_r = pd.to_numeric(row.get("actual_realized_r"), errors="coerce")
    mfe_r = pd.to_numeric(row.get("actual_mfe_r"), errors="coerce")

    data_window = "v3_era" if entry_ts >= cutoff_v3 else "pre_v3_observer"

    # Classify
    if pd.notna(cf_r) and cf_r >= 2.0:
        rec = "same_direction_timing_repair"
        evidence = f"audit counterfactual r=+{cf_r:.1f} (simple_2R model says same-dir would hit target)"
    elif pd.notna(cf_r) and cf_r == 0.0:
        rec = "skip_required"
        evidence = f"audit counterfactual r=0.0 (same direction never developed; opp-dir lookup blocked: factor file ends 2026-04-13)"
    elif pd.notna(cf_r) and cf_r <= -0.5:
        rec = "skip_required"
        evidence = f"audit counterfactual r={cf_r:.1f} (same direction would have lost too; opp-dir at minimum worth asking — data_unresolved)"
    else:
        rec = "no_clean_answer"
        evidence = f"audit counterfactual r={cf_r} unclear"

    # Nearest winner cluster (if same_direction_timing_repair)
    nearest = None
    if rec == "same_direction_timing_repair":
        strat = row.get("bot_actual_strategy", "unknown")
        sb = row.get("session_bucket")
        nearest = clusters_dict.get((strat, pf, sb, bot_dir))

    results.append({
        "idx": idx, "ledger_id": row["ledger_id"], "pair": pair,
        "entry_ts": entry_ts, "bot_direction": bot_dir, "pair_family": pf,
        "session_bucket": row.get("session_bucket"),
        "session_quarter": row.get("session_quarter"),
        "bot_actual_strategy": row.get("bot_actual_strategy"),
        "actual_realized_r": float(actual_r) if pd.notna(actual_r) else None,
        "actual_mfe_r": float(mfe_r) if pd.notna(mfe_r) else None,
        "audit_counterfactual_r": float(cf_r) if pd.notna(cf_r) else None,
        "data_window": data_window,
        "opp_direction_lookup_possible": data_window == "v3_era",
        "opp_direction_resolved": False,  # explicit: we did NOT do this lookup
        "step6_recommendation": rec,
        "step6_evidence": evidence,
        "nearest_winner_cluster": nearest,
    })

results_df = pd.DataFrame(results)

print(f"\nDate window distribution:")
print(results_df["data_window"].value_counts().to_string())

print(f"\nStep 6 RECOMMENDATION distribution:")
n = len(results_df)
rec = results_df["step6_recommendation"].value_counts()
for k, v in rec.items():
    print(f"  {k}: {v}/{n} = {v/n*100:.1f}%")

print(f"\nBy pair family:")
print(results_df.groupby("pair_family")["step6_recommendation"].value_counts().unstack(fill_value=0).to_string())

print(f"\nBy session bucket:")
print(results_df.groupby("session_bucket")["step6_recommendation"].value_counts().unstack(fill_value=0).to_string())

print(f"\nThe 6 same_direction_timing_repair cases:")
sdr = results_df[results_df["step6_recommendation"] == "same_direction_timing_repair"]
print(sdr[["ledger_id","pair","bot_direction","session_bucket","session_quarter",
           "bot_actual_strategy","actual_realized_r","audit_counterfactual_r","nearest_winner_cluster"]].to_string(index=False))

# Save results
results_df.to_csv(OUT / "forensic_results_v2.csv", index=False)
results_df.to_parquet(OUT / "forensic_results_v2.parquet", index=False)

# Update ledger
for col in ["step6_recommendation", "step6_evidence", "step6_data_window",
            "step6_opp_resolved", "step6_nearest_cluster"]:
    df[col] = None
for r in results:
    idx = r["idx"]
    df.at[idx, "step6_recommendation"] = r["step6_recommendation"]
    df.at[idx, "step6_evidence"] = r["step6_evidence"]
    df.at[idx, "step6_data_window"] = r["data_window"]
    df.at[idx, "step6_opp_resolved"] = r["opp_direction_resolved"]
    df.at[idx, "step6_nearest_cluster"] = r["nearest_winner_cluster"]

# clean parquet
for c in df.columns:
    if df[c].dtype == "object" and c not in ("correct_pdh","correct_pdl","reconstructed_entry_price",
                                              "best_opp_r","best_same_r","actual_realized_r",
                                              "actual_realized_pl","actual_mfe_r","actual_mae_r"):
        df[c] = df[c].astype(str).replace({"nan": None, "None": None, "<NA>": None})
df.to_parquet(LEDGER, index=False)
df.to_csv(LEDGER.with_suffix(".csv"), index=False)
print(f"\nsaved ledger: {len(df)} rows, {len(df.columns)} cols")
