import pandas as pd, json
from pathlib import Path

LEDGER = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/winner-clusters-v0")

df = pd.read_parquet(LEDGER)
df["_strategy"] = df["bot_actual_strategy"].fillna(df["strategy_label"]).fillna("unknown")
df["_session"] = df["session_bucket"].fillna(df["session"]).fillna("unknown")
winners = df[df["repair_taxonomy"] == "actual_winner"].copy()

clusters = []
for keys, grp in winners.groupby(["_strategy", "pair_family", "_session", "direction"]):
    s, pf, ses, dr = keys
    cluster_id = f"{s[:4]}_{pf[:3]}_{ses[:3]}_{dr[:1]}"
    src_mix = grp["source_label"].value_counts()
    realized = pd.to_numeric(grp["actual_realized_r"], errors="coerce")
    mfe = pd.to_numeric(grp["actual_mfe_r"], errors="coerce")
    exit_dict = {str(k): int(v) for k, v in grp["actual_exit_reason"].value_counts().items()}
    clusters.append({
        "cluster_id": cluster_id,
        "strategy": s, "pair_family": pf, "session": ses, "direction": dr,
        "n_winners": int(len(grp)),
        "n_broker": int(src_mix.get("bot_actual_winner", 0)),
        "n_human": int(src_mix.get("manual_human", 0)),
        "n_ai_curated": int(src_mix.get("manual_ai_curated", 0)),
        "median_realized_r": float(realized.median()) if realized.notna().any() else None,
        "p25_realized_r": float(realized.quantile(0.25)) if realized.notna().any() else None,
        "p75_realized_r": float(realized.quantile(0.75)) if realized.notna().any() else None,
        "median_mfe_r": float(mfe.median()) if mfe.notna().any() else None,
        "pairs": ",".join(sorted(grp["pair"].unique().tolist())),
        "exit_reasons": json.dumps(exit_dict),
        "is_cluster": bool(len(grp) >= 2),
    })

clusters_df = pd.DataFrame(clusters).sort_values("n_winners", ascending=False)
out_path = OUT / "winner_clusters_v1.csv"
clusters_df.to_csv(out_path, index=False)
print(f"wrote {out_path}: {len(clusters_df)} cells")
print(f"Real clusters (n>=2): {clusters_df.is_cluster.sum()}")
print(f"Singletons: {(~clusters_df.is_cluster).sum()}")
print()
print("Top 15 clusters by n_winners (with trust label split):")
top = clusters_df[clusters_df.is_cluster].head(15)[
    ["cluster_id","strategy","pair_family","session","direction",
     "n_winners","n_broker","n_human","n_ai_curated","median_realized_r","median_mfe_r"]
]
print(top.to_string(index=False))
