"""v10_fast_v1.1 builder -- slice-aware expansion of v10_fast.

Brock 2026-05-18 war-room: include cells for the CURRENT live slice
that have honest in-sample evidence. Three groups:

  Group A: original 7 live-validated parents (HIGH confidence)
  Group B: boundary siblings from strike-pass-B (in-sample strict winners
           of Group A parents, +1/+2/+3/+5% widened)
  Group C: v9_observe Seed cells for the current slice (C02 + active
           sessions + top live pairs) with wr_unique >= 0.85 and n >= 10
           These are in-sample-only but match the active live slice.

All promoted to tier='Seed-Pro' so the existing live gate at
min_tier=Seed-Pro fires them. Each row carries a `promote_source` field
so we can attribute live performance back.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--v10-fast", required=True)
    ap.add_argument("--v9-observe", required=True)
    ap.add_argument("--strike-strict", required=True)
    ap.add_argument("--ranked-candidates", required=True,
                    help="current_slice_ranked_candidates.csv from war-room")
    ap.add_argument("--current-regime", default="C02")
    ap.add_argument("--active-sessions", default="ny_close,ny_mid,ny_open",
                    help="comma-separated sessions to include (active for today + tomorrow)")
    ap.add_argument("--top-pairs", default="USD_CHF,EUR_CAD,EUR_NZD,AUD_USD,EUR_AUD,NZD_USD,EUR_GBP,GBP_CHF,GBP_USD,EUR_USD,GBP_CAD,GBP_AUD,USD_CAD,USD_JPY,EUR_JPY,EUR_CHF")
    ap.add_argument("--group-c-min-wr", type=float, default=0.85)
    ap.add_argument("--group-c-min-n", type=int, default=10)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    sessions = args.active_sessions.split(",")
    pairs = args.top_pairs.split(",")
    now_iso = datetime.now(timezone.utc).isoformat()

    print(f"=== Building v10_fast_v1.1 ===")
    print(f"  regime: {args.current_regime}")
    print(f"  active sessions: {sessions}")
    print(f"  top pairs: {pairs}")

    # Group A: original v10_fast
    v10 = pd.read_parquet(args.v10_fast)
    print(f"\nGroup A (live-validated parents): {len(v10)} rows / "
          f"{v10.drop_duplicates(subset=['parent_regime','pair','strategy','direction','session_bucket']).shape[0]} unique cells")

    # Group B: strike-pass-B strict winners (boundary siblings)
    strike = pd.read_csv(args.strike_strict)
    # Filter to current regime + active sessions + top pairs
    sb = strike[
        strike.regime53.eq(args.current_regime)
        & strike.pair.isin(pairs)
    ].copy()
    # The strict-winners CSV has session_bucket from parent; some are
    # session-clause-free in the child_rule, so they apply across sessions.
    print(f"\nGroup B (boundary siblings, strict winners): {len(sb)} candidates")

    # Group C: v9_observe Seed cells for slice
    v9 = pd.read_parquet(args.v9_observe)
    v9_in_slice = v9[
        v9.parent_regime.eq(args.current_regime)
        & v9.pair.isin(pairs)
        & v9.session_bucket.isin(sessions)
        & v9.tier.eq("Seed")
        & (v9.wr >= args.group_c_min_wr)
        & (v9.n_unique >= args.group_c_min_n)
    ].drop_duplicates(subset=["parent_regime","pair","strategy","direction","session_bucket"])
    # Cap Group C size by ranking on wilson_lb
    if "wilson_lb" in v9_in_slice.columns:
        v9_in_slice = v9_in_slice.sort_values("wilson_lb", ascending=False).head(40)
    print(f"\nGroup C (v9_observe Seed in slice, wr>={args.group_c_min_wr} n>={args.group_c_min_n}): {len(v9_in_slice)} cells")

    # Build output rows
    rows = []
    # Group A: pass through
    for _, r in v10.iterrows():
        d = r.to_dict()
        d["tier"] = "Seed-Pro"
        d["promote_source"] = "A_live_validated_parent"
        d["last_updated"] = now_iso
        rows.append(d)

    # Group B: build v8-schema rows from strike-pass strict winners
    # Each row needs: parent_regime, pair, strategy, direction, session_bucket,
    # shave_rule (=child_rule), family, tier=Seed-Pro, n_unique, wins_unique,
    # wr, wilson_lb, source, promote_source, etc.
    v9_lookup = v9.drop_duplicates(subset=["parent_regime","pair","strategy","direction","session_bucket"]).set_index(
        ["parent_regime","pair","strategy","direction","session_bucket"]
    )
    for _, r in sb.iterrows():
        cs = r.get("cell_strategy")
        if pd.isna(cs): continue
        # Use parent's session_bucket from v9 lookup if possible
        try:
            v9row = v9_lookup.loc[(r.regime53, r.pair, cs, r.direction, r.session_bucket)]
            base = v9row.to_dict()
        except KeyError:
            # Synthesize from strike row
            base = {
                "parent_regime": r.regime53,
                "technical_regime_53": r.regime53,
                "pair": r.pair,
                "strategy": cs,
                "family": r.get("family"),
                "direction": r.direction,
                "session_bucket": r.get("session_bucket") or "ny_mid",
                "sub_regime": r.regime53,
                "technical_regime_desc": "",
                "r_target": 1.5,
                "score_boost": 0.0,
                "loser_skip_rule": "",
                "winner_lift": 0.0, "parent_n": 0, "parent_wr": 0.0,
                "source_bank": "strike_b_sibling",
                "oos_status": "untested",
                "promotion_status": "candidate",
            }
        base["tier"] = "Seed-Pro"
        base["n"] = int(r.n_unique)
        base["n_unique"] = int(r.n_unique)
        base["wins"] = int(r.wins_unique)
        base["wr"] = float(r.wr_unique)
        base["wilson_lb"] = float(r.wilson_lb)
        base["sum_R"] = 0.0
        base["mean_R"] = 0.0
        base["source"] = f"strike_boundary_widen_{int(r.widen_pct*100) if r.widen_pct else '0'}pct"
        base["shave_rule"] = r.child_rule
        base["promote_source"] = "B_boundary_sibling"
        base["last_updated"] = now_iso
        rows.append(base)

    # Group C: pass through v9_observe rows with tier upgraded
    for _, r in v9_in_slice.iterrows():
        d = r.to_dict()
        d["tier"] = "Seed-Pro"
        d["promote_source"] = "C_slice_v9_seed"
        d["last_updated"] = now_iso
        rows.append(d)

    df = pd.DataFrame(rows)
    # Dedup at v8 deploy granularity, prefer Group A > B > C
    src_rank = {"A_live_validated_parent": 0, "B_boundary_sibling": 1, "C_slice_v9_seed": 2}
    df["_rank"] = df["promote_source"].map(src_rank).fillna(99).astype(int)
    df = df.sort_values("_rank").drop_duplicates(
        subset=["parent_regime","pair","strategy","direction","session_bucket"], keep="first",
    )
    df = df.drop(columns=["_rank"])

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(args.out, index=False)
    print(f"\n-> {args.out}")
    print(f"  total rows: {len(df)}")
    print(f"  by promote_source: {df.promote_source.value_counts().to_dict()}")
    print(f"  by family:        {df.family.value_counts().to_dict()}")
    print(f"  by session:       {df.session_bucket.value_counts().to_dict()}")
    print(f"  by pair:          {df.pair.value_counts().to_dict()}")


if __name__ == "__main__":
    main()
