"""Surgical v10_fast_v1.1 -- original 10 + 4 explicit slice fallbacks.

Per Brock 2026-05-18: don't broad-relax; add only the 4 slice-specific
current-fallback cells identified by the war-room pass.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd

# Explicit current-slice fallback list (Brock 2026-05-18 war-room)
FALLBACKS = [
    # (regime, pair, strategy, direction, session, family)
    ("C02", "USD_CHF", "alpha_pullback_v2",          "long",  "ny_close", "dbb_trend"),
    ("C02", "USD_CHF", "alpha_extended_fade_v2",     "short", "ny_close", "reversal"),
    ("C02", "EUR_CAD", "charlie_compression_breakout","long", "ny_close", "direct"),
    ("C02", "EUR_CAD", "TF6_ma_ribbon_short",        "short", "ny_close", "dbb_trend"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--v10-fast", required=True)
    ap.add_argument("--v9-observe", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    v10 = pd.read_parquet(args.v10_fast)
    v9 = pd.read_parquet(args.v9_observe)
    v9_lookup = v9.drop_duplicates(subset=["parent_regime","pair","strategy","direction","session_bucket"]).set_index(
        ["parent_regime","pair","strategy","direction","session_bucket"]
    )
    now_iso = datetime.now(timezone.utc).isoformat()

    rows = []
    # Group A: pass-through originals, mark source
    for _, r in v10.iterrows():
        d = r.to_dict()
        d["tier"] = "Seed-Pro"
        d["promote_source"] = "A_live_validated_parent"
        d["last_updated"] = now_iso
        rows.append(d)

    # Group C: explicit fallbacks for current slice (ny_close)
    found = 0
    missed = []
    for (regime, pair, strat, direction, session, family) in FALLBACKS:
        try:
            base = v9_lookup.loc[(regime, pair, strat, direction, session)].to_dict()
        except KeyError:
            missed.append((regime, pair, strat, direction, session))
            continue
        # multi-index .loc strips the key columns -- restore them
        base["parent_regime"] = regime
        base["pair"] = pair
        base["strategy"] = strat
        base["direction"] = direction
        base["session_bucket"] = session
        base["sub_regime"] = regime
        base["technical_regime_53"] = regime
        base["family"] = family
        base["tier"] = "Seed-Pro"
        base["promote_source"] = "C_slice_fallback"
        base["last_updated"] = now_iso
        rows.append(base)
        found += 1

    df = pd.DataFrame(rows)
    df = df.drop_duplicates(
        subset=["parent_regime","pair","strategy","direction","session_bucket"], keep="first",
    )

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(args.out, index=False)
    print(f"Wrote {len(df)} rows ({found} fallbacks found, {len(missed)} missed)")
    if missed:
        for m in missed:
            print(f"  MISSED in v9_observe: {m}")
    print(f"  by source: {df.promote_source.value_counts().to_dict()}")
    print(f"  by family: {df.family.value_counts().to_dict()}")
    print(f"  by session: {df.session_bucket.value_counts().to_dict()}")


if __name__ == "__main__":
    main()
