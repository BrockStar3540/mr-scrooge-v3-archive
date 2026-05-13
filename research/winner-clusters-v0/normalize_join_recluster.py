"""Steps 1-4 in one pass:
  1. Rename box_geometry_repair → correct_box_replay_required
  2. Normalize session labels (tokyo_only→asia, london_only→london, etc.)
  3. Join 79-key factor snapshots to broker winner rows
  4. Rerun winner clustering with normalized + factor-enriched data

Per 2026-05-13 direction. No regime naming, no candidate promotion.
Trust labels kept separate: bot_actual_winner / manual_human / manual_ai_curated.
"""
import pandas as pd
import json
import numpy as np
from pathlib import Path

LEDGER = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/winner-clusters-v0")

df = pd.read_parquet(LEDGER)
print(f"loaded ledger: {len(df)} rows, {len(df.columns)} cols")

# === Step 1: rename ===
mask_rename = df["repair_taxonomy"] == "box_geometry_repair"
df.loc[mask_rename, "repair_taxonomy"] = "correct_box_replay_required"
print(f"step 1: renamed {mask_rename.sum()} rows box_geometry_repair → correct_box_replay_required")

# === Step 2: normalize session labels ===
SESSION_MAP = {
    "tokyo_only": "asia",
    "asia_only": "asia",
    "asia": "asia",
    "london_only": "london",
    "london": "london",
    "london_ny_overlap": "overlap",
    "overlap": "overlap",
    "ny_only": "ny_pm",
    "ny_pm": "ny_pm",
    "ny_overlap": "overlap",
    "unknown": "unknown",
    "all": "all",
}
pre_sessions = df["session_bucket"].value_counts().to_dict()
df["session_bucket_raw"] = df["session_bucket"]  # preserve original
df["session_bucket"] = df["session_bucket"].map(lambda x: SESSION_MAP.get(x, x) if pd.notna(x) else x)
df["session"] = df["session"].map(lambda x: SESSION_MAP.get(x, x) if pd.notna(x) else x)
post_sessions = df["session_bucket"].value_counts().to_dict()
print(f"step 2: session bucket distribution")
print(f"  before: {pre_sessions}")
print(f"  after:  {post_sessions}")

# === Step 3: factor-snapshot join ===
print(f"\nstep 3: loading factor snapshots ...")
snapshots = {}
with open("/home/ubuntu/Oanda-Bot-Trainer/data/replay/v2/audits/live_broker_factor_snapshots.jsonl") as f:
    for line in f:
        d = json.loads(line)
        snapshots[d["factor_snapshot_id"]] = d["features"]
print(f"  loaded {len(snapshots)} snapshots")

# Identify factor columns to attach
all_factor_keys = set()
for s in snapshots.values():
    all_factor_keys.update(s.keys())
factor_cols = sorted(all_factor_keys)
print(f"  factor keys: {len(factor_cols)}")

# Add columns to ledger
broker_mask = df["source_label"].str.startswith("bot_actual_") & df["factor_snapshot_id"].notna()
n_broker_with_snap = broker_mask.sum()
print(f"  broker rows with factor_snapshot_id: {n_broker_with_snap}")

attached = 0
for col in factor_cols:
    col_name = f"factor_{col}"
    if col_name not in df.columns:
        df[col_name] = None
for idx, row in df[broker_mask].iterrows():
    sid = row["factor_snapshot_id"]
    if sid in snapshots:
        for k, v in snapshots[sid].items():
            df.at[idx, f"factor_{k}"] = v
        attached += 1
print(f"  attached factors to {attached} broker rows")

# === Step 4: rerun winner clustering with normalized data ===
print(f"\nstep 4: winner-cluster discovery v1 (normalized + factor-enriched)")

# Resolve clustering keys
df["_strategy"] = df["bot_actual_strategy"].fillna(df["strategy_label"]).fillna("unknown")
df["_session"] = df["session_bucket"].fillna(df["session"]).fillna("unknown")

winners = df[df["repair_taxonomy"] == "actual_winner"].copy()
print(f"  actual winners: {len(winners)}")
print(f"  source mix:\n{winners['source_label'].value_counts().to_string()}")
print(f"  normalized sessions:\n{winners['_session'].value_counts().to_string()}")

# Reset prior cluster annotation
df["winner_cluster_id"] = None
df["shared_features"] = None
df["nearest_loser_contrast"] = None

# Build clusters
clusters = []
for keys, grp in winners.groupby(["_strategy", "pair_family", "_session", "direction"]):
    s, pf, ses, dr = keys
    cluster_id = f"{s[:4]}_{pf[:3]}_{ses[:3]}_{dr[:1]}"
    src_mix = grp["source_label"].value_counts().to_dict()
    n_broker = src_mix.get("bot_actual_winner", 0)
    n_human = src_mix.get("manual_human", 0)
    n_ai = src_mix.get("manual_ai_curated", 0)

    # Factor signature (mean) — broker winners only since manual mostly lacks 47-factor data
    broker_sub = grp[grp["source_label"] == "bot_actual_winner"]
    factor_sig = {}
    if len(broker_sub):
        for col in factor_cols:
            fcol = f"factor_{col}"
            if fcol in broker_sub.columns:
                vals = broker_sub[fcol].dropna()
                if len(vals) >= 2:
                    factor_sig[col] = {"median": float(vals.median()), "n": len(vals)}

    clusters.append({
        "cluster_id": cluster_id,
        "strategy": s, "pair_family": pf, "session": ses, "direction": dr,
        "n_winners": len(grp),
        "n_broker": n_broker, "n_human": n_human, "n_ai_curated": n_ai,
        "median_realized_r": grp["actual_realized_r"].median(),
        "p25_realized_r": grp["actual_realized_r"].quantile(0.25),
        "p75_realized_r": grp["actual_realized_r"].quantile(0.75),
        "median_mfe_r": grp["actual_mfe_r"].median() if grp["actual_mfe_r"].notna().any() else None,
        "pairs": sorted(grp["pair"].unique().tolist()),
        "exit_reasons": dict(grp["actual_exit_reason"].value_counts()),
        "factor_signature_keys": sorted(factor_sig.keys()),
        "is_cluster": len(grp) >= 2,
    })
clusters_df = pd.DataFrame(clusters).sort_values("n_winners", ascending=False)

# Store the factor signatures separately (since they're dicts)
import json as _json
factor_sigs_per_cluster = {}
for c in clusters:
    cid = c["cluster_id"]
    # Recompute factor signature
    broker_sub = winners[
        (winners["_strategy"] == c["strategy"]) &
        (winners["pair_family"] == c["pair_family"]) &
        (winners["_session"] == c["session"]) &
        (winners["direction"] == c["direction"]) &
        (winners["source_label"] == "bot_actual_winner")
    ]
    sig = {}
    if len(broker_sub):
        for col in factor_cols:
            fcol = f"factor_{col}"
            if fcol in broker_sub.columns:
                vals = pd.to_numeric(broker_sub[fcol], errors="coerce").dropna()
                if len(vals) >= 2:
                    sig[col] = {"median": float(vals.median()),
                                "q25": float(vals.quantile(0.25)),
                                "q75": float(vals.quantile(0.75)),
                                "n": int(len(vals))}
    factor_sigs_per_cluster[cid] = sig
(OUT / "factor_signatures.json").write_text(_json.dumps(factor_sigs_per_cluster, indent=2))

# Assign winner_cluster_id back to ledger
for c in clusters:
    if not c["is_cluster"]:
        continue
    mask = (
        (df["_strategy"] == c["strategy"]) &
        (df["pair_family"] == c["pair_family"]) &
        (df["_session"] == c["session"]) &
        (df["direction"] == c["direction"]) &
        (df["repair_taxonomy"] == "actual_winner")
    )
    df.loc[mask, "winner_cluster_id"] = c["cluster_id"]
    df.loc[mask, "shared_features"] = f"cluster={c['cluster_id']} n={c['n_winners']} med_r={c['median_realized_r']:.2f}"

    # Nearest loser contrast: any same-cell non-winner
    cell_losers = df[
        (df["_strategy"] == c["strategy"]) &
        (df["pair_family"] == c["pair_family"]) &
        (df["_session"] == c["session"]) &
        (df["direction"] == c["direction"]) &
        (df["repair_taxonomy"] != "actual_winner")
    ]
    if len(cell_losers):
        # Prefer rows that have full factor data (broker) and that didn't enter on a bug
        preference_loc = cell_losers["valid_entry_location"] == True
        cleaner_losers = cell_losers[preference_loc] if preference_loc.any() else cell_losers
        nl = cleaner_losers.iloc[0]
        df.loc[mask, "nearest_loser_contrast"] = (
            f"{nl['ledger_id'][:8]}|{nl['repair_taxonomy']}|"
            f"r={nl['actual_realized_r']:.2f}" if pd.notna(nl['actual_realized_r']) else
            f"{nl['ledger_id'][:8]}|{nl['repair_taxonomy']}|r=?"
        )

# Save
df = df.drop(columns=["_strategy", "_session"], errors="ignore")
# Coerce string types for parquet stability
for c in df.columns:
    if df[c].dtype == "object":
        df[c] = df[c].astype(str).replace({"nan": None, "None": None, "<NA>": None})
df.to_parquet(LEDGER, index=False)
df.to_csv(LEDGER.with_suffix(".csv"), index=False)
print(f"\nsaved ledger: {len(df)} rows, {len(df.columns)} cols")

# Cluster table
clusters_df["pairs"] = clusters_df["pairs"].apply(lambda x: ",".join(x))
clusters_df["exit_reasons"] = clusters_df["exit_reasons"].apply(lambda x: _json.dumps(x))
clusters_df["factor_signature_keys"] = clusters_df["factor_signature_keys"].apply(lambda x: ",".join(x[:10]))
clusters_df.to_csv(OUT / "winner_clusters_v1.csv", index=False)
print(f"saved {OUT / 'winner_clusters_v1.csv'}")

n_real = clusters_df["is_cluster"].sum()
print(f"\nReal clusters (n>=2): {n_real}")
print(f"Singletons: {(~clusters_df['is_cluster']).sum()}")
print(f"\nTop 12 by n_winners:")
print(clusters_df[clusters_df.is_cluster].head(12)[
    ["cluster_id","strategy","pair_family","session","direction",
     "n_winners","n_broker","n_human","n_ai_curated",
     "median_realized_r","median_mfe_r"]
].to_string(index=False))
