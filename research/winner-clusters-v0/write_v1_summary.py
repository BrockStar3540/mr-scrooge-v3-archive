"""Write the v1 summary report and commit."""
import pandas as pd
import json
from pathlib import Path
from datetime import datetime, timezone

OUT = Path("/home/ubuntu/mr-scrooge-v3/research/winner-clusters-v0")
LEDGER = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet")

df = pd.read_parquet(LEDGER)
clusters_df = pd.read_csv(OUT / "winner_clusters_v1.csv")

# Pull the saved factor signatures
factor_sigs = {}
if (OUT / "factor_signatures.json").exists():
    factor_sigs = json.loads((OUT / "factor_signatures.json").read_text())

winners = df[df["repair_taxonomy"] == "actual_winner"]
report = []
report.append("# Winner-Cluster Discovery v1 (normalized + factor-enriched)")
report.append("")
report.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
report.append("")
report.append("## What changed from v0")
report.append("")
report.append("1. `box_geometry_repair` renamed → `correct_box_replay_required`")
report.append("   (rename reflects: contamination proven, repair not yet proven)")
report.append("2. Session labels normalized: tokyo_only→asia, asia_only→asia,")
report.append("   london_only→london, ny_only→ny_pm, london_ny_overlap→overlap")
report.append("3. 79-key factor snapshots joined to all 196 broker rows")
report.append("4. Winner clusters rerun on normalized + enriched data")
report.append("")
report.append("Ledger now has 149 columns (up from 69) — 79 factor_* + the same identity / outcome / repair columns.")
report.append("")
report.append("## Repair taxonomy distribution (unchanged from v0)")
report.append("")
report.append(df["repair_taxonomy"].value_counts().to_frame().to_markdown())
report.append("")
report.append("## Cluster outcomes")
report.append("")
report.append(f"- Total winners: {len(winners)}")
report.append(f"- Cells with ≥2 winners: {clusters_df['is_cluster'].sum()}")
report.append(f"- Singletons: {(~clusters_df['is_cluster']).sum()}")
report.append("")
report.append("## Top 15 clusters")
report.append("")
top = clusters_df[clusters_df.is_cluster].head(15)[
    ["cluster_id","strategy","pair_family","session","direction",
     "n_winners","n_broker","n_human","n_ai_curated","median_realized_r","median_mfe_r","pairs"]
]
report.append(top.to_markdown(index=False, floatfmt=".2f"))
report.append("")
report.append("## Cross-trust validation cells (broker + theory both have winners here)")
report.append("")
report.append("Cells where BOTH broker_winner AND (human OR ai_curated) winners exist —")
report.append("the strongest evidence that the cell is a real winner pocket, not a theory artifact.")
report.append("")
cross_trust = clusters_df[
    (clusters_df.is_cluster) &
    (clusters_df.n_broker >= 1) &
    ((clusters_df.n_human >= 1) | (clusters_df.n_ai_curated >= 1))
]
if len(cross_trust):
    report.append(cross_trust[
        ["cluster_id","strategy","pair_family","session","direction",
         "n_winners","n_broker","n_human","n_ai_curated","median_realized_r","median_mfe_r"]
    ].to_markdown(index=False, floatfmt=".2f"))
report.append("")
report.append("## Best clusters by realized R (top 10 by median, n_winners >= 3)")
report.append("")
best_r = clusters_df[(clusters_df.is_cluster) & (clusters_df.n_winners >= 3)].nlargest(10, "median_realized_r")[
    ["cluster_id","strategy","pair_family","session","direction",
     "n_winners","median_realized_r","median_mfe_r","pairs"]
]
report.append(best_r.to_markdown(index=False, floatfmt=".2f"))
report.append("")
report.append("## Distribution by axis after normalization")
report.append("")
report.append("### Pair family among winners")
report.append("")
report.append(winners["pair_family"].value_counts().to_frame().to_markdown())
report.append("")
report.append("### Session among winners")
report.append("")
report.append(winners["session_bucket"].value_counts().to_frame().to_markdown())
report.append("")
report.append("### Direction among winners")
report.append("")
report.append(winners["direction"].value_counts().to_frame().to_markdown())
report.append("")
report.append("## Factor signatures for the largest cross-trust clusters")
report.append("")
report.append("Median factor values across BROKER winners in each cluster (manual rows lack the 47+ factor set).")
report.append("")
for cid in cross_trust["cluster_id"].head(5):
    if cid in factor_sigs:
        sig = factor_sigs[cid]
        if not sig:
            continue
        report.append(f"### {cid}")
        report.append("")
        rows = []
        for k, v in sorted(sig.items()):
            rows.append({"factor": k, "median": v["median"], "q25": v["q25"], "q75": v["q75"], "n": v["n"]})
        sig_df = pd.DataFrame(rows)
        # Subset to interesting factors
        keep = ["bb_position", "bb_band_width_a_bps", "rsi", "adr_consumed", "atr",
                "ema20_dist_pct", "ema50_dist_pct", "regime_score", "regime_confidence",
                "rr_ratio", "wall_proximity", "z_score", "spread_pips", "otr_ratio",
                "volume_ratio", "box_age_hours", "score"]
        sig_df_view = sig_df[sig_df["factor"].isin(keep)]
        report.append(sig_df_view.to_markdown(index=False, floatfmt=".3f"))
        report.append("")
report.append("## Next steps (per direction 2026-05-13)")
report.append("")
report.append("Step 5 (next turn): box-geometry forensic for 87 `correct_box_replay_required` rows.")
report.append("Replay each contaminated entry's date+pair with correct PDH/PDL, identify the")
report.append("legitimate winning entry that existed at the time.")
report.append("")
report.append("Step 6 (after step 5): direction-repair forensic for 88 `direction_repair_or_skip`.")
report.append("Query factor file at entry_ts ± 30min for opposite-direction candidates.")
report.append("")
report.append("Still not yet: candidate_new_regime naming, candidate_strategy naming, ready_for_backtest.")
report.append("Clusters are visible but synchrony work continues.")

(OUT / "summary_v1.md").write_text("\n".join(report))
print(f"wrote {OUT / 'summary_v1.md'}")
