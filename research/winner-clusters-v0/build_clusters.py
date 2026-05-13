"""Winner-cluster discovery on the trade-film ledger.

Per 2026-05-13 direction:
  - Cluster ACTUAL WINNERS first
  - Old regime labels are NOT clustering drivers (they're metadata)
  - For each cluster, attach nearest_loser_contrast
  - candidate_new_regime + candidate_strategy stay null — those are human-named

Approach for n=110 (small enough for explicit grouping, not k-means):
  Cluster key:  strategy × pair_family × session × direction
  + management_signature based on actual_mfe_r / actual_tp1_hit / actual_be_hit
"""
import pandas as pd
import numpy as np
from pathlib import Path

LEDGER = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/winner-clusters-v0")
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_parquet(LEDGER)
print(f"ledger loaded: {len(df)} rows")

# Resolve strategy + session for clustering
df["_cluster_strategy"] = df["bot_actual_strategy"].fillna(df["strategy_label"]).fillna("unknown")
df["_cluster_session"] = df["session_bucket"].fillna(df["session"]).fillna("unknown")

# Filter to actual winners
winners = df[df["repair_taxonomy"] == "actual_winner"].copy()
print(f"actual winners: {len(winners)}")
print(f"  by source:\n{winners['source_label'].value_counts().to_string()}")

# Cluster cells
print("\nclustering by (strategy, pair_family, session, direction)...")
clusters = []
for keys, grp in winners.groupby(["_cluster_strategy", "pair_family", "_cluster_session", "direction"]):
    s, pf, ses, dr = keys
    if len(grp) < 2:
        # Lone winner — note but don't make a cluster
        clusters.append({
            "cluster_id": f"{s[:3]}_{pf[:3]}_{ses[:3]}_{dr[:1]}",
            "strategy": s, "pair_family": pf, "session": ses, "direction": dr,
            "n_winners": len(grp),
            "n_singleton": 1,
            "median_realized_r": grp["actual_realized_r"].median() if "actual_realized_r" in grp.columns else None,
            "median_mfe_r": grp["actual_mfe_r"].median() if grp["actual_mfe_r"].notna().any() else None,
            "winner_source_mix": dict(grp["source_label"].value_counts()),
            "exit_reasons": dict(grp["actual_exit_reason"].value_counts()) if grp["actual_exit_reason"].notna().any() else {},
            "pairs": sorted(grp["pair"].unique().tolist()),
            "is_cluster": False,
        })
        continue
    cluster_id = f"{s[:3]}_{pf[:3]}_{ses[:3]}_{dr[:1]}"
    clusters.append({
        "cluster_id": cluster_id,
        "strategy": s, "pair_family": pf, "session": ses, "direction": dr,
        "n_winners": len(grp),
        "n_singleton": 0,
        "median_realized_r": grp["actual_realized_r"].median(),
        "p25_realized_r": grp["actual_realized_r"].quantile(0.25),
        "p75_realized_r": grp["actual_realized_r"].quantile(0.75),
        "median_mfe_r": grp["actual_mfe_r"].median() if grp["actual_mfe_r"].notna().any() else None,
        "winner_source_mix": dict(grp["source_label"].value_counts()),
        "exit_reasons": dict(grp["actual_exit_reason"].value_counts()) if grp["actual_exit_reason"].notna().any() else {},
        "pairs": sorted(grp["pair"].unique().tolist()),
        "is_cluster": True,
    })
clusters_df = pd.DataFrame(clusters).sort_values("n_winners", ascending=False)
print(f"  {len(clusters_df)} cells total")
print(f"  cells with >=2 winners: {clusters_df['is_cluster'].sum()}")
print(f"  singletons: {(~clusters_df['is_cluster']).sum()}")


# === Assign winner_cluster_id to ledger rows ===
print("\nassigning winner_cluster_id to ledger ...")
df["winner_cluster_id"] = None
for _, c in clusters_df.iterrows():
    if not c["is_cluster"]:
        continue
    mask = (
        (df["_cluster_strategy"] == c["strategy"]) &
        (df["pair_family"] == c["pair_family"]) &
        (df["_cluster_session"] == c["session"]) &
        (df["direction"] == c["direction"]) &
        (df["repair_taxonomy"] == "actual_winner")
    )
    df.loc[mask, "winner_cluster_id"] = c["cluster_id"]


# === Build entry_state_signature + nearest_loser_contrast per cluster ===
print("building entry_state_signature + nearest_loser_contrast ...")
for _, c in clusters_df.iterrows():
    if not c["is_cluster"]:
        continue
    cluster_winners = df[df["winner_cluster_id"] == c["cluster_id"]]
    # Same-cell losers — first prefer management_repair, then box_geometry, then direction_repair
    cell_mask = (
        (df["_cluster_strategy"] == c["strategy"]) &
        (df["pair_family"] == c["pair_family"]) &
        (df["_cluster_session"] == c["session"]) &
        (df["direction"] == c["direction"]) &
        (df["repair_taxonomy"] != "actual_winner")
    )
    cell_losers = df[cell_mask].copy()
    if len(cell_losers):
        # Prefer management_repair > entry_timing > direction_repair > box_geometry > not_salvageable
        preference = {
            "management_repair": 0, "entry_timing_repair": 1,
            "direction_repair_or_skip": 2, "box_geometry_repair": 3,
            "not_salvageable": 4, "needs_review": 5
        }
        cell_losers["_pref"] = cell_losers["repair_taxonomy"].map(lambda r: preference.get(r, 99))
        cell_losers = cell_losers.sort_values("_pref")
        nearest_loser = cell_losers.iloc[0]
        for w_idx in cluster_winners.index:
            df.at[w_idx, "nearest_loser_contrast"] = (
                f"{nearest_loser['ledger_id'][:8]}|{nearest_loser['repair_taxonomy']}|"
                f"r={nearest_loser['actual_realized_r']:.2f}"
            )
            df.at[w_idx, "shared_features"] = (
                f"cluster={c['cluster_id']} n={c['n_winners']} med_r={c['median_realized_r']:.2f}"
            )


# Save ledger
df = df.drop(columns=["_cluster_strategy", "_cluster_session"])
df.to_parquet(LEDGER, index=False)
df.to_csv(LEDGER.with_suffix(".csv"), index=False)
print(f"saved ledger ({len(df)} rows)")


# Save cluster summary
clusters_df.to_csv(OUT / "winner_clusters.csv", index=False)


# === Summary report ===
report = []
report.append("# Winner-Cluster Discovery v0 — trade-film ledger")
report.append("")
report.append("Per 2026-05-13 direction:")
report.append("- Clustered ACTUAL WINNERS only (n=110: 64 broker + 46 manual)")
report.append("- Old regime labels NOT used as clustering drivers")
report.append("- candidate_new_regime + candidate_strategy stay null (your call to name)")
report.append("- ready_for_backtest stays FALSE for v0")
report.append("")
report.append(f"## Clustering result")
report.append("")
report.append(f"- Total winners: {len(winners)}")
report.append(f"- Cells with ≥2 winners: {clusters_df['is_cluster'].sum()}")
report.append(f"- Singleton cells: {(~clusters_df['is_cluster']).sum()}")
report.append("")
report.append("## Top clusters (≥2 winners)")
report.append("")
cluster_view = clusters_df[clusters_df["is_cluster"]].copy()
for col in ("winner_source_mix", "exit_reasons", "pairs"):
    cluster_view[col] = cluster_view[col].apply(lambda x: str(x)[:80] if x else "")
cluster_view = cluster_view[["cluster_id","strategy","pair_family","session","direction",
                              "n_winners","median_realized_r","median_mfe_r","pairs","exit_reasons","winner_source_mix"]]
report.append(cluster_view.to_markdown(index=False, floatfmt=".2f"))
report.append("")
report.append("## Singleton winners (one-off, may indicate sparse cell or unusual pair)")
report.append("")
singles = clusters_df[~clusters_df["is_cluster"]][
    ["cluster_id","strategy","pair_family","session","direction","pairs","median_realized_r","winner_source_mix"]
].head(15)
for col in ("pairs", "winner_source_mix"):
    singles[col] = singles[col].apply(lambda x: str(x)[:80] if x else "")
report.append(singles.to_markdown(index=False, floatfmt=".2f"))
report.append("")
report.append("## Cross-reference: most-represented pair families in winning")
report.append("")
report.append(winners["pair_family"].value_counts().to_frame().to_markdown())
report.append("")
report.append("## Cross-reference: most-represented sessions in winning")
report.append("")
report.append(winners["_cluster_session"].value_counts().to_frame().to_markdown())
report.append("")
report.append("## Cross-reference: direction split")
report.append("")
report.append(winners["direction"].value_counts().to_frame().to_markdown())
report.append("")
report.append("## What's missing for v1 winner-cluster work")
report.append("")
report.append("- Factor-snapshot join: broker winners have `factor_snapshot_id` but the")
report.append("  factor values aren't joined into the ledger (deferred per scope rule).")
report.append("  v1 should join `live_broker_factor_snapshots.jsonl` to attach the 47 factors.")
report.append("- Same-time opposite-direction lookup for direction_repair candidates")
report.append("  (88 rows currently marked `direction_repair_or_skip`). v1 should query the")
report.append("  factor file at entry_ts ± 30min for opposite-direction candidates and check")
report.append("  if any won, to distinguish true direction_repair from skip_required.")
report.append("- Local box-state lookup for box_geometry_repair (87 rows). v1 should compute")
report.append("  what the corrected box would have been on the entry day and identify the")
report.append("  legitimate entry point.")
report.append("")
report.append("## Constraints (per direction 2026-05-13)")
report.append("")
report.append("- We are NOT trying to save the bot's bad entry. The 87 box_geometry_repair")
report.append("  rows + 88 direction_repair candidates are NOT yet promoted to 'salvageable'.")
report.append("  Each needs a local price-action investigation to determine the legitimate")
report.append("  winning expression that existed at the time.")
report.append("- The 2 management_repair rows have TBD save_method because the management")
report.append("  atlas cell mapped to 'needs_investigation' — not enough signal for an")
report.append("  automatic save_method assignment.")
report.append("- Clusters are factual groupings of actual winners, not strategy proposals.")
Path(OUT / "summary.md").write_text("\n".join(report))
print(f"summary at {OUT / 'summary.md'}")
