"""A. Build live_validated_parent_cells.csv from the telemetry ledger.

Brock 2026-05-18: isolate the cells where the shadow gate emitted
`shave_rule_satisfied` repeatedly. Those are the parents for the strike
expansion -- live shadow evidence now outranks corpus OOS for probes.

Per-parent stats:
  live_passes      shadow rows with shave_rule_satisfied
  live_vetos       shadow rows with shave_rule_violated on the same cell
  pass_rate        passes / (passes + vetos) on this cell
  live_block_now   the cell's current live-gate block reason
  v9_*            in-sample stats from v9_observe (if present)
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import pandas as pd


def load_ledger(p):
    rows = []
    with open(p) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            try: rows.append(json.loads(line))
            except Exception: pass
    return pd.DataFrame(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--v9-observe", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--min-passes", type=int, default=2)
    args = ap.parse_args()
    out = Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)

    df = load_ledger(args.ledger)
    shadow = df[df.gate == "entry_filter_shadow"].copy()
    live = df[df.gate == "entry_filter"].copy()

    # Cell key for shadow rows
    sh_key_cols = ["regime53","symbol","cell_strategy","direction","session_bucket"]
    # passes
    passed = shadow[shadow.block_reason == "shave_rule_satisfied"]
    pass_counts = passed.groupby(sh_key_cols).size().reset_index(name="live_passes")
    # vetos (shave_rule_violated) on the SAME cell
    veto = shadow[shadow.block_reason.str.startswith("shave_rule_violated", na=False)]
    veto_counts = veto.groupby(sh_key_cols).size().reset_index(name="live_vetos")
    # shave_rule + factors (take from a representative passed row)
    rep = passed.drop_duplicates(subset=sh_key_cols)[
        sh_key_cols + ["shave_rule", "cell_family", "cell_tier"]
    ]

    parents = pass_counts.merge(rep, on=sh_key_cols, how="left")
    parents = parents.merge(veto_counts, on=sh_key_cols, how="left")
    parents["live_vetos"] = parents["live_vetos"].fillna(0).astype(int)
    parents["pass_rate"] = parents["live_passes"] / (parents["live_passes"] + parents["live_vetos"])
    parents = parents.rename(columns={"symbol": "pair", "cell_family": "family"})

    # Filter to qualifying parents
    parents = parents[parents.live_passes >= args.min_passes].copy()

    # Current live block reason for the same tuple (from live gate)
    live_block = live.groupby(["regime53","symbol","direction","session_bucket"])\
                     ["block_reason"].agg(lambda s: s.value_counts().idxmax() if len(s) else None)\
                     .reset_index().rename(columns={"symbol":"pair","block_reason":"current_live_block"})
    parents = parents.merge(live_block, on=["regime53","pair","direction","session_bucket"], how="left")

    # Enrich with v9 in-sample stats
    v9 = pd.read_parquet(args.v9_observe)
    v9_keys = v9.drop_duplicates(subset=["parent_regime","pair","strategy","direction","session_bucket"])
    v9_lookup = v9_keys.set_index(["parent_regime","pair","strategy","direction","session_bucket"])

    def enrich(r):
        k = (r.regime53, r.pair, r.cell_strategy, r.direction, r.session_bucket)
        try:
            v = v9_lookup.loc[k]
            return pd.Series({
                "v9_tier": v.tier,
                "v9_n_unique": int(v.get("n_unique", 0) or 0),
                "v9_wr": float(v.get("wr", 0) or 0),
                "v9_wilson_lb": float(v.get("wilson_lb", 0) or 0),
            })
        except KeyError:
            return pd.Series({"v9_tier": None, "v9_n_unique": 0, "v9_wr": 0.0, "v9_wilson_lb": 0.0})

    parents = pd.concat([parents, parents.apply(enrich, axis=1)], axis=1)
    parents = parents.sort_values(["live_passes","v9_wilson_lb"], ascending=False)

    csv_path = out / "live_validated_parent_cells.csv"
    parents.to_csv(csv_path, index=False)
    print(f"-> {csv_path}  ({len(parents)} parents)")

    # Markdown
    md = ["# Live-validated parent cells", ""]
    md.append(f"Built from {len(df):,} ledger rows ({len(passed)} shave-passes, {len(veto)} shave-vetos).")
    md.append(f"Filter: shave_rule_satisfied >= {args.min_passes}")
    md.append("")
    md.append("| regime | pair | family | strategy | dir | session | "
              "passes | vetos | pass_rate | v9_tier | v9_n | v9_wr | v9_lb | current_live_block | shave_rule |")
    md.append("|---|---|---|---|---|---|---:|---:|---:|---|---:|---:|---:|---|---|")
    for _, r in parents.iterrows():
        rule = (r.shave_rule or "")[:100] + ("..." if isinstance(r.shave_rule, str) and len(r.shave_rule)>100 else "")
        md.append(
            f"| {r.regime53} | {r.pair} | {r.family} | {r.cell_strategy} | {r.direction} | "
            f"{r.session_bucket} | {int(r.live_passes)} | {int(r.live_vetos)} | {r.pass_rate:.3f} | "
            f"{r.v9_tier} | {r.v9_n_unique} | {r.v9_wr:.3f} | {r.v9_wilson_lb:.3f} | "
            f"{r.current_live_block or '-'} | `{rule}` |"
        )
    md_path = out / "live_validated_parent_cells.md"
    md_path.write_text("\n".join(md))
    print(f"-> {md_path}")


if __name__ == "__main__":
    main()
