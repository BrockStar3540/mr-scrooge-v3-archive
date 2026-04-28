"""Per-feature win-rate analysis. For every feature, bucket trades by decile
and report win rate. The widest WR spreads = the strongest discriminators."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

REPO = Path.home() / "mr-scrooge-v3"
sys.path.insert(0, str(REPO / "src"))
from scrooge_v3.advisors.ml_observer.features import FEATURE_NAMES

REPLAY = Path.home() / "Oanda-Bot-Trainer" / "data" / "replay"
HIST = REPO / "data" / "ml-observer-offline" / "historic_replay.parquet"
OUT = REPO / "data" / "ml-observer-offline" / "factor_analysis.md"


def parse_mf(raw):
    if isinstance(raw, dict): return raw
    if isinstance(raw, str):
        try: return json.loads(raw.replace("Infinity", "1e9").replace("NaN", "0"))
        except: return {}
    return {}


def vec(mf):
    out = []
    for n in FEATURE_NAMES:
        try:
            v = float(mf.get(n, 0.0))
            if not np.isfinite(v): v = 0.0
        except: v = 0.0
        out.append(v)
    return out


def build_corpus():
    """Big sim corpus: 18,858 trades from 180d replay."""
    sc = pd.read_parquet(REPLAY / "oanda_180d_scans_accepted.parquet")
    tr = pd.read_parquet(REPLAY / "oanda_180d_training_set.parquet")
    sc["ts"] = pd.to_datetime(sc["ts"], utc=True)
    tr["ts"] = pd.to_datetime(tr["ts"], utc=True)
    j = sc[["ts", "symbol", "ml_features"]].merge(
        tr[["ts", "symbol", "is_win", "realized_r"]],
        on=["symbol", "ts"], how="inner",
    )
    feats = pd.DataFrame([vec(parse_mf(m)) for m in j["ml_features"]],
                         columns=FEATURE_NAMES)
    feats["__win__"] = j["is_win"].astype(int).values
    feats["__r__"] = j["realized_r"].values
    return feats


def build_historic():
    """Real OANDA trades."""
    df = pd.read_parquet(HIST)
    df = df[df["ml_features"].notna()].copy()
    feats = pd.DataFrame([vec(parse_mf(m)) for m in df["ml_features"]],
                         columns=FEATURE_NAMES)
    feats["__win__"] = df["win"].astype(int).values
    feats["__pl__"] = df["pl"].values
    feats["__label__"] = df["label"].values
    return feats


def per_feature_deciles(df, feature_names, target="__win__", min_n=20, n_buckets=10):
    """For each feature, split into n_buckets quantile buckets, compute target mean per bucket.
    Returns DataFrame: feature, low_wr, high_wr, spread, n_buckets_used."""
    rows = []
    base = df[target].mean()
    for f in feature_names:
        if df[f].nunique() < n_buckets:
            continue
        try:
            df["_b"] = pd.qcut(df[f], q=n_buckets, duplicates="drop")
        except Exception:
            continue
        g = df.groupby("_b", observed=True).agg(n=(target, "size"), wr=(target, "mean"))
        g = g[g["n"] >= min_n]
        if len(g) < 4: continue
        rows.append({
            "feature": f,
            "n_bins": len(g),
            "min_wr": g["wr"].min(),
            "max_wr": g["wr"].max(),
            "spread": g["wr"].max() - g["wr"].min(),
            "best_bin": str(g["wr"].idxmax()),
            "best_bin_wr": g["wr"].max(),
            "best_bin_n": int(g.loc[g["wr"].idxmax(), "n"]),
            "worst_bin": str(g["wr"].idxmin()),
            "worst_bin_wr": g["wr"].min(),
            "worst_bin_n": int(g.loc[g["wr"].idxmin(), "n"]),
        })
    out = pd.DataFrame(rows).sort_values("spread", ascending=False)
    out["lift_vs_base"] = out["max_wr"] - base
    return out, base


def feature_decile_table(df, feature, target="__win__"):
    """Detailed per-decile breakdown for one feature."""
    s = df[feature]
    df = df.copy()
    df["_b"] = pd.qcut(s, q=10, duplicates="drop")
    g = df.groupby("_b", observed=True).agg(n=(target, "size"), wr=(target, "mean"))
    return g


def main():
    print("loading 18k sim corpus...")
    sim = build_corpus()
    print(f"sim trades={len(sim)}, base WR={sim['__win__'].mean()*100:.1f}%")

    print("\nloading historic real trades...")
    hist = build_historic()
    print(f"historic trades={len(hist)}, base WR={hist['__win__'].mean()*100:.1f}%")

    print("\n=== TOP DISCRIMINATORS — 18k sim corpus ===")
    sim_top, sim_base = per_feature_deciles(sim, FEATURE_NAMES)
    print(f"baseline WR: {sim_base*100:.1f}%")
    print(sim_top.head(20)[["feature", "min_wr", "max_wr", "spread", "best_bin_wr", "best_bin_n", "worst_bin_wr", "worst_bin_n"]].to_string(index=False, float_format=lambda x: f"{x:.3f}"))

    print("\n=== TOP DISCRIMINATORS — 587 real trades ===")
    hist_top, hist_base = per_feature_deciles(hist, FEATURE_NAMES)
    print(f"baseline WR: {hist_base*100:.1f}%")
    print(hist_top.head(20)[["feature", "min_wr", "max_wr", "spread", "best_bin_wr", "best_bin_n", "worst_bin_wr", "worst_bin_n"]].to_string(index=False, float_format=lambda x: f"{x:.3f}"))

    # Cross-check: which features rank in top 10 in BOTH?
    sim_top10 = set(sim_top.head(15)["feature"].tolist())
    hist_top10 = set(hist_top.head(15)["feature"].tolist())
    overlap = sim_top10 & hist_top10
    print(f"\n=== ROBUST FEATURES (top 15 in both sim AND real) ===")
    print(", ".join(sorted(overlap)) or "(none)")

    # For top 6 robust features, dump full decile table from sim corpus
    print("\n=== DECILE TABLES — robust features (sim corpus) ===")
    for f in list(overlap)[:8]:
        print(f"\n--- {f} ---")
        print(feature_decile_table(sim, f).to_string(float_format=lambda x: f"{x:.3f}"))

    # Write report
    with open(OUT, "w") as fh:
        fh.write("# Factor Dial — Per-Feature Win-Rate Analysis\n\n")
        fh.write(f"**Corpora:** sim={len(sim)} trades, historic={len(hist)} trades\n\n")
        fh.write(f"**Baselines:** sim WR={sim_base*100:.1f}%, historic WR={hist_base*100:.1f}%\n\n")
        fh.write("## Top 20 discriminators — sim corpus (18,858 trades)\n\n")
        fh.write(sim_top.head(20).to_string(index=False))
        fh.write("\n\n## Top 20 discriminators — historic real trades (587)\n\n")
        fh.write(hist_top.head(20).to_string(index=False))
        fh.write(f"\n\n## Robust features (in top-15 of both)\n\n")
        fh.write(", ".join(sorted(overlap)) or "(none)")
        fh.write("\n")
    print(f"\nreport -> {OUT}")


if __name__ == "__main__":
    main()
