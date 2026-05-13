"""Step 6: direction-repair lookup on 88 direction_repair_or_skip rows.

For each row, search per_trade_factors_filled.csv.gz for filled candidates
within ±30 min on same pair. Classify:

  direction_repair                   opposite-direction winner exists nearby
  same_direction_timing_repair       same-direction winner exists nearby
  skip_required                      no winners nearby
  no_clean_answer                    data ambiguous / no clean local structure

Preserve per row:
  - best opposite-direction candidate timestamp + realized_r + strategy + factor_snapshot_id
  - best same-direction candidate timestamp + realized_r + strategy
  - nearest winner cluster (from winner_clusters_v1.csv) if any
"""
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import timedelta

LEDGER = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet")
FACTORS = "/home/ubuntu/Oanda-Bot-Trainer/data/replay/v2/factor_audit/per_trade_factors_filled.csv.gz"
CLUSTERS = Path("/home/ubuntu/mr-scrooge-v3/research/winner-clusters-v0/winner_clusters_v1.csv")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/direction-repair-lookup")
OUT.mkdir(parents=True, exist_ok=True)

# === Load ===
print("loading ledger ...")
df = pd.read_parquet(LEDGER)
target = df[df["repair_taxonomy"] == "direction_repair_or_skip"].copy()
target["entry_ts"] = pd.to_datetime(target["entry_ts"], utc=True, errors="coerce")
target = target[target["entry_ts"].notna()]
print(f"  direction_repair_or_skip rows with valid entry_ts: {len(target)}")

print("\nloading factor candidates (filled only) ...")
fct = pd.read_csv(FACTORS, parse_dates=["ts"])
fct["ts"] = pd.to_datetime(fct["ts"], utc=True)
print(f"  filled candidates: {len(fct)}")
print(f"  candidates with realized_r > 0: {(fct['realized_r'] > 0).sum():,}")

print("\nloading winner clusters ...")
clusters = pd.read_csv(CLUSTERS)
clusters_dict = {}
for _, c in clusters.iterrows():
    if c["is_cluster"]:
        key = (c["strategy"], c["pair_family"], c["session"], c["direction"])
        clusters_dict[key] = c["cluster_id"]
print(f"  loaded {len(clusters_dict)} winner clusters")


PAIR_FAMILY = {
    "EUR_USD":"usd_base","GBP_USD":"usd_base","AUD_USD":"usd_base","NZD_USD":"usd_base",
    "USD_JPY":"usd_base","USD_CHF":"usd_base","USD_CAD":"usd_base","USD_MXN":"usd_base",
    "EUR_GBP":"eur_cross","EUR_AUD":"eur_cross","EUR_NZD":"eur_cross","EUR_CAD":"eur_cross",
    "EUR_CHF":"eur_cross","EUR_JPY":"eur_cross",
    "GBP_AUD":"gbp_cross","GBP_NZD":"gbp_cross","GBP_CAD":"gbp_cross","GBP_CHF":"gbp_cross","GBP_JPY":"gbp_cross",
    "AUD_NZD":"antipodean_cross","AUD_CAD":"antipodean_cross","AUD_CHF":"antipodean_cross",
    "AUD_JPY":"antipodean_cross","NZD_JPY":"antipodean_cross","CAD_JPY":"antipodean_cross","CHF_JPY":"antipodean_cross",
}

# === Per-row lookup ===
print("\nrunning lookup ...")
WINDOW = timedelta(minutes=30)
results = []

for idx, row in target.iterrows():
    pair = row["pair"]
    entry_ts = row["entry_ts"]
    bot_dir = row["direction"]  # what the bot did
    pf = PAIR_FAMILY.get(pair, "other")

    # Nearby candidates on same pair within ±30 min
    nearby = fct[
        (fct["symbol"] == pair) &
        (fct["ts"] >= entry_ts - WINDOW) &
        (fct["ts"] <= entry_ts + WINDOW)
    ]

    if len(nearby) == 0:
        results.append({
            "idx": idx, "ledger_id": row["ledger_id"], "pair": pair,
            "entry_ts": entry_ts, "bot_direction": bot_dir,
            "n_nearby_candidates": 0,
            "best_opp_ts": None, "best_opp_r": None, "best_opp_strategy": None, "best_opp_snapshot": None,
            "best_same_ts": None, "best_same_r": None, "best_same_strategy": None, "best_same_snapshot": None,
            "step6_recommendation": "skip_required",
            "step6_evidence": "no candidates in ±30min window",
            "session_bucket": row.get("session_bucket"),
            "session_quarter": row.get("session_quarter"),
            "pair_family": pf,
            "bot_actual_strategy": row.get("bot_actual_strategy"),
            "nearest_winner_cluster": None,
        })
        continue

    # Opposite direction winners
    opp_dir = "short" if bot_dir == "long" else "long"
    opp_cands = nearby[(nearby["direction"] == opp_dir) & (nearby["realized_r"] > 0)]
    opp_cands = opp_cands.sort_values("realized_r", ascending=False)

    # Same direction winners
    same_cands = nearby[(nearby["direction"] == bot_dir) & (nearby["realized_r"] > 0)]
    same_cands = same_cands.sort_values("realized_r", ascending=False)

    best_opp = opp_cands.iloc[0] if len(opp_cands) else None
    best_same = same_cands.iloc[0] if len(same_cands) else None

    # Classify
    if best_opp is not None and best_same is not None:
        # Both directions have winners nearby — pick the one with bigger realized_r
        if float(best_opp["realized_r"]) > float(best_same["realized_r"]) * 1.5:
            rec = "direction_repair"
            evidence = (
                f"opposite-dir winner exists: {opp_dir} at {best_opp['ts']} r={best_opp['realized_r']:+.2f} "
                f"strategy={best_opp['strategy']} (vs same-dir winner r={best_same['realized_r']:+.2f})"
            )
        elif float(best_same["realized_r"]) > float(best_opp["realized_r"]) * 1.5:
            rec = "same_direction_timing_repair"
            evidence = (
                f"same-dir winner exists: {bot_dir} at {best_same['ts']} r={best_same['realized_r']:+.2f} "
                f"strategy={best_same['strategy']} (vs opp-dir winner r={best_opp['realized_r']:+.2f})"
            )
        else:
            rec = "no_clean_answer"
            evidence = (
                f"both directions have winners nearby — opp r={best_opp['realized_r']:+.2f}, "
                f"same r={best_same['realized_r']:+.2f}; can't cleanly attribute"
            )
    elif best_opp is not None:
        rec = "direction_repair"
        evidence = (
            f"opposite-dir winner exists: {opp_dir} at {best_opp['ts']} r={best_opp['realized_r']:+.2f} "
            f"strategy={best_opp['strategy']} (no same-dir winner nearby)"
        )
    elif best_same is not None:
        rec = "same_direction_timing_repair"
        evidence = (
            f"same-dir winner exists: {bot_dir} at {best_same['ts']} r={best_same['realized_r']:+.2f} "
            f"strategy={best_same['strategy']} (no opp-dir winner nearby)"
        )
    else:
        # No winners either direction
        # Were there any filled candidates at all? If so, all lost → skip
        rec = "skip_required"
        evidence = f"{len(nearby)} nearby candidates, none winning either direction"

    # Nearest winner cluster lookup
    correct_dir = opp_dir if rec == "direction_repair" else bot_dir
    cluster_key_strategy = (
        best_opp["strategy"] if rec == "direction_repair" and best_opp is not None else
        best_same["strategy"] if rec == "same_direction_timing_repair" and best_same is not None else
        row.get("bot_actual_strategy", "unknown")
    )
    nearest = clusters_dict.get((cluster_key_strategy, pf, row.get("session_bucket"), correct_dir))

    results.append({
        "idx": idx, "ledger_id": row["ledger_id"], "pair": pair,
        "entry_ts": entry_ts, "bot_direction": bot_dir,
        "n_nearby_candidates": int(len(nearby)),
        "best_opp_ts": best_opp["ts"] if best_opp is not None else None,
        "best_opp_r": float(best_opp["realized_r"]) if best_opp is not None else None,
        "best_opp_strategy": best_opp["strategy"] if best_opp is not None else None,
        "best_opp_snapshot": best_opp["candidate_id"] if best_opp is not None else None,
        "best_same_ts": best_same["ts"] if best_same is not None else None,
        "best_same_r": float(best_same["realized_r"]) if best_same is not None else None,
        "best_same_strategy": best_same["strategy"] if best_same is not None else None,
        "best_same_snapshot": best_same["candidate_id"] if best_same is not None else None,
        "step6_recommendation": rec,
        "step6_evidence": evidence,
        "session_bucket": row.get("session_bucket"),
        "session_quarter": row.get("session_quarter"),
        "pair_family": pf,
        "bot_actual_strategy": row.get("bot_actual_strategy"),
        "nearest_winner_cluster": nearest,
    })

results_df = pd.DataFrame(results)
print(f"\nresults: {len(results_df)} rows")

print(f"\n=== STEP 6 RECOMMENDATION DISTRIBUTION ===")
rec = results_df["step6_recommendation"].value_counts()
n = len(results_df)
for k, v in rec.items():
    print(f"  {k}: {v}/{n} = {v/n*100:.1f}%")

print(f"\n=== BY PAIR FAMILY ===")
pf_b = results_df.groupby("pair_family")["step6_recommendation"].value_counts().unstack(fill_value=0)
print(pf_b.to_string())

print(f"\n=== BY SESSION BUCKET ===")
sb_b = results_df.groupby("session_bucket")["step6_recommendation"].value_counts().unstack(fill_value=0)
print(sb_b.to_string())

print(f"\n=== BY BOT_ACTUAL_STRATEGY ===")
bs_b = results_df.groupby("bot_actual_strategy")["step6_recommendation"].value_counts().unstack(fill_value=0)
print(bs_b.to_string())

print(f"\n=== NEAREST WINNER CLUSTER MATCHES ===")
print(f"  rows with nearest cluster: {results_df['nearest_winner_cluster'].notna().sum()}/{n}")
print(results_df["nearest_winner_cluster"].value_counts().head(10).to_string())

print(f"\n=== HIGH-R OPPORTUNITIES ===")
# Rows where bot_actual was a loss but opp_r is significantly positive
opp_signal = results_df[(results_df["best_opp_r"].notna()) & (results_df["best_opp_r"] >= 1.0)]
print(f"  rows where opposite direction would have realized ≥+1.0R: {len(opp_signal)}")
if len(opp_signal):
    print(opp_signal[["ledger_id","pair","bot_direction","best_opp_r","best_opp_strategy","step6_recommendation","session_bucket"]].head(10).to_string(index=False))

# Save results
results_df.to_csv(OUT / "forensic_results.csv", index=False)
results_df.to_parquet(OUT / "forensic_results.parquet", index=False)

# Update ledger
print(f"\nupdating ledger with step 6 columns ...")
for col in ["best_opp_ts","best_opp_r","best_opp_strategy","best_same_ts","best_same_r",
            "best_same_strategy","step6_recommendation","step6_evidence","nearest_winner_cluster_step6"]:
    df[col] = None

for r in results:
    idx = r["idx"]
    df.at[idx, "best_opp_ts"] = str(r["best_opp_ts"]) if r["best_opp_ts"] is not None else None
    df.at[idx, "best_opp_r"] = r["best_opp_r"]
    df.at[idx, "best_opp_strategy"] = r["best_opp_strategy"]
    df.at[idx, "best_same_ts"] = str(r["best_same_ts"]) if r["best_same_ts"] is not None else None
    df.at[idx, "best_same_r"] = r["best_same_r"]
    df.at[idx, "best_same_strategy"] = r["best_same_strategy"]
    df.at[idx, "step6_recommendation"] = r["step6_recommendation"]
    df.at[idx, "step6_evidence"] = r["step6_evidence"]
    df.at[idx, "nearest_winner_cluster_step6"] = r["nearest_winner_cluster"]

# Coerce types for parquet
for c in df.columns:
    if df[c].dtype == "object" and c not in ("correct_pdh","correct_pdl","reconstructed_entry_price","best_opp_r","best_same_r"):
        df[c] = df[c].astype(str).replace({"nan": None, "None": None, "<NA>": None})
df.to_parquet(LEDGER, index=False)
df.to_csv(LEDGER.with_suffix(".csv"), index=False)
print(f"saved ledger: {len(df)} rows, {len(df.columns)} cols")
