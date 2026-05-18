"""E. Build next_expansion_zones.csv combining:
    - live_shadow_pass     (highest evidence)
    - live_shadow_block    (the bot is hitting these tuples right now)
    - 6m_regime_frequency  (long-term market regime activity)
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
    ap.add_argument("--regime-6m", required=True)
    ap.add_argument("--v9-observe", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    df = load_ledger(args.ledger)
    shadow = df[df.gate == "entry_filter_shadow"]
    live = df[df.gate == "entry_filter"]
    reg6m = pd.read_csv(args.regime_6m)
    v9 = pd.read_parquet(args.v9_observe)

    # Live shadow passes per cell (highest evidence)
    sp = shadow[shadow.block_reason == "shave_rule_satisfied"]
    sp_g = sp.groupby(["regime53","symbol","cell_strategy","direction","session_bucket"])\
             .size().reset_index(name="live_passes")
    sp_g = sp_g.rename(columns={"symbol":"pair"})
    sp_g["source"] = "live_shadow_pass"
    sp_g["family"] = sp_g["cell_strategy"].map(lambda s: shadow[shadow.cell_strategy==s].cell_family.iloc[0] if (shadow.cell_strategy==s).any() else None)

    # Live shadow blocks (bot is generating candidates here but can't fire)
    sb = shadow[shadow.block_reason.str.startswith("shave_rule_violated", na=False)]
    sb_g = sb.groupby(["regime53","symbol","cell_strategy","direction","session_bucket"])\
             .size().reset_index(name="live_blocks")
    sb_g = sb_g.rename(columns={"symbol":"pair"})
    sb_g = sb_g[sb_g.live_blocks >= 30]
    sb_g["source"] = "live_shadow_block"
    sb_g["family"] = sb_g["cell_strategy"].map(lambda s: shadow[shadow.cell_strategy==s].cell_family.iloc[0] if (shadow.cell_strategy==s).any() else None)

    # 6m regime hot zones (top 50 by volume within C01/C02)
    hot6m = reg6m[reg6m.technical_regime_53.isin(["C01","C02"])].copy()
    hot6m = hot6m.sort_values("n", ascending=False).head(50)
    hot6m = hot6m.rename(columns={"technical_regime_53":"regime53"})
    hot6m["source"] = "6m_regime_frequency"
    hot6m["cell_strategy"] = None
    hot6m["live_passes"] = 0
    hot6m["live_blocks"] = 0
    hot6m["six_m_n"] = hot6m["n"]
    hot6m["six_m_wr"] = hot6m["wr"]
    hot6m = hot6m[["regime53","pair","family","direction","session_bucket",
                   "cell_strategy","source","live_passes","live_blocks",
                   "six_m_n","six_m_wr"]]

    sp_g["six_m_n"] = 0; sp_g["six_m_wr"] = 0.0; sp_g["live_blocks"] = 0
    sb_g["six_m_n"] = 0; sb_g["six_m_wr"] = 0.0; sb_g["live_passes"] = 0

    common = ["regime53","pair","family","direction","session_bucket",
              "cell_strategy","source","live_passes","live_blocks","six_m_n","six_m_wr"]
    combined = pd.concat([sp_g[common], sb_g[common], hot6m[common]], ignore_index=True)

    # Priority ranking
    def rank(r):
        if r.source == "live_shadow_pass": return 1
        if r.source == "live_shadow_block" and r.live_blocks >= 100: return 2
        if r.source == "live_shadow_block": return 3
        return 4

    # Expansion type
    def exp_type(r):
        if r.source == "live_shadow_pass": return "boundary_thin"
        if r.source == "live_shadow_block": return "session_sibling" if "shave_rule_violated: session_bucket" in str(r.get("block_reason","")) else "boundary_thin"
        if r.family == "direct": return "direct_uplift"
        return "textbook_hole_fill"

    combined["priority_rank"] = combined.apply(rank, axis=1)
    combined["expansion_type"] = combined.apply(exp_type, axis=1)
    combined = combined.sort_values(["priority_rank","live_passes","live_blocks","six_m_n"],
                                    ascending=[True, False, False, False])
    combined.to_csv(args.out, index=False)
    print(f"-> {args.out} ({len(combined)} zones)")
    print(f"\nPriority distribution:")
    for r, g in combined.groupby("priority_rank"):
        print(f"  rank {r}: {len(g)} zones ({g.source.value_counts().to_dict()})")


if __name__ == "__main__":
    main()
