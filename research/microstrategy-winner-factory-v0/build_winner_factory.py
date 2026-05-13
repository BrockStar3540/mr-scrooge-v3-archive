"""Winner-first microstrategy factory v0, streaming version.

Mine the completed v2 corpus for repeated clean-winner entry-state shapes.
Old regime/probe labels are annotations only; the primary grain is pair family,
direction, session, session quarter, and raw feature bins.
"""
from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import pandas as pd
import pyarrow.parquet as pq

CORPUS = Path("/home/ubuntu/Oanda-Bot-Trainer/data/replay/v3_full_corpus/v2_2.0R")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/microstrategy-winner-factory-v0")
OUT.mkdir(parents=True, exist_ok=True)

PAIR_FAMILY = {
    "EUR_USD": "usd_base", "GBP_USD": "usd_base", "AUD_USD": "usd_base", "NZD_USD": "usd_base",
    "USD_JPY": "usd_base", "USD_CHF": "usd_base", "USD_CAD": "usd_base", "USD_MXN": "usd_base",
    "EUR_GBP": "eur_cross", "EUR_AUD": "eur_cross", "EUR_NZD": "eur_cross", "EUR_CAD": "eur_cross",
    "EUR_CHF": "eur_cross", "EUR_JPY": "eur_cross",
    "GBP_AUD": "gbp_cross", "GBP_NZD": "gbp_cross", "GBP_CAD": "gbp_cross", "GBP_CHF": "gbp_cross", "GBP_JPY": "gbp_cross",
    "AUD_NZD": "antipodean_cross", "AUD_CAD": "antipodean_cross", "AUD_CHF": "antipodean_cross", "AUD_JPY": "antipodean_cross",
    "NZD_JPY": "antipodean_cross", "CAD_JPY": "antipodean_cross", "CHF_JPY": "antipodean_cross",
}

KEEP = [
    "trade_id", "entry_ts", "pair", "symbol", "direction", "filled", "realized_r", "mfe_r", "mae_r",
    "session_label", "regime_label", "probe_name", "year", "quarter", "feature_snapshot",
]
GRAIN = [
    "pair_family", "direction", "session_bucket", "session_quarter",
    "bb_pos_bin", "rsi_bin", "ema20_dist_bin", "bbw_bin", "echo_ratio_bin",
]
COARSE_GRAIN = ["pair_family", "direction", "session_bucket"]


def session_bucket_from_hour(hour: int) -> str:
    h = int(hour) % 24
    if 22 <= h or h < 6: return "asia"
    if 6 <= h < 12: return "london"
    if 12 <= h < 16: return "overlap"
    if 16 <= h < 21: return "ny_pm"
    return "rollover"


def session_quarter(hour: int, minute: int) -> str:
    minute_of_day = int(hour) * 60 + int(minute)
    shifted = minute_of_day + (24 * 60 if hour < 6 else 0)
    bucket = session_bucket_from_hour(hour)
    ranges = {
        "asia": (22 * 60, 30 * 60), "london": (6 * 60, 12 * 60),
        "overlap": (12 * 60, 16 * 60), "ny_pm": (16 * 60, 21 * 60), "rollover": (21 * 60, 22 * 60),
    }
    start, end = ranges[bucket]
    if bucket != "asia": shifted = minute_of_day
    q = min(4, max(1, int((shifted - start) // ((end - start) / 4.0)) + 1))
    return f"{bucket}_q{q}"


def parse_snapshot(s):
    if not isinstance(s, str) or not s:
        return (np.nan, np.nan, np.nan, np.nan, np.nan)
    try:
        x = json.loads(s)
    except Exception:
        return (np.nan, np.nan, np.nan, np.nan, np.nan)
    def f(k):
        try: return float(x.get(k))
        except Exception: return np.nan
    return (f("bb_position"), f("rsi"), f("ema20_dist_pct"), f("bbw_a_bps"), f("echo_range_ratio"))


def bb_bin(x):
    if pd.isna(x): return "bb_unknown"
    if x < -0.05: return "below_band"
    if x < 0.10: return "lower_rail"
    if x < 0.35: return "lower_band"
    if x <= 0.65: return "middle"
    if x <= 0.90: return "upper_band"
    if x <= 1.05: return "upper_rail"
    return "above_band"


def rsi_bin(x):
    if pd.isna(x): return "rsi_unknown"
    if x < 30: return "oversold"
    if x < 45: return "low"
    if x <= 55: return "mid"
    if x <= 70: return "high"
    return "overbought"


def ema_bin(x):
    if pd.isna(x): return "ema_unknown"
    ax = abs(float(x))
    if ax < 10: return "ema_near"
    if ax < 30: return "ema_mid"
    if ax < 60: return "ema_far"
    return "ema_stretched"


def bbw_bin(x):
    if pd.isna(x): return "bbw_unknown"
    if x < 5: return "bbw_tight"
    if x < 15: return "bbw_mid"
    if x < 30: return "bbw_wide"
    return "bbw_explosive"


def echo_bin(x):
    if pd.isna(x): return "echo_unknown"
    if x < 0.70: return "echo_compressed"
    if x < 1.00: return "echo_mid"
    if x < 1.40: return "echo_expanded"
    return "echo_explosive"


def wilson_low(pos, n, z=1.96):
    pos = np.asarray(pos, dtype=float); n = np.asarray(n, dtype=float)
    phat = np.divide(pos, n, out=np.zeros_like(pos), where=n > 0)
    denom = 1 + z*z/n
    center = phat + z*z/(2*n)
    spread = z * np.sqrt((phat*(1-phat) + z*z/(4*n)) / n)
    return (center - spread) / denom


def prep_chunk(df):
    df = df[df["filled"] == True].copy()
    if "pair" not in df.columns and "symbol" in df.columns:
        df["pair"] = df["symbol"]
    df["entry_ts"] = pd.to_datetime(df["entry_ts"], utc=True, errors="coerce")
    for c in ["mfe_r", "mae_r", "realized_r"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.dropna(subset=["entry_ts", "pair", "direction", "mfe_r", "mae_r", "realized_r"])
    df["pair_family"] = df["pair"].map(PAIR_FAMILY).fillna("other")
    df["hour_utc"] = df["entry_ts"].dt.hour
    df["minute_utc"] = df["entry_ts"].dt.minute
    df["session_bucket"] = df["hour_utc"].map(session_bucket_from_hour)
    df["session_quarter"] = [session_quarter(h, m) for h, m in zip(df["hour_utc"], df["minute_utc"])]
    df["period"] = np.where(df["entry_ts"] < pd.Timestamp("2025-01-01", tz="UTC"), "discovery", "holdout")

    parsed = [parse_snapshot(x) for x in df["feature_snapshot"]]
    feat = pd.DataFrame(parsed, columns=["bb_position", "rsi", "ema20_dist_pct", "bbw_a_bps", "echo_range_ratio"], index=df.index)
    df["bb_pos_bin"] = feat["bb_position"].map(bb_bin)
    df["rsi_bin"] = feat["rsi"].map(rsi_bin)
    df["ema20_dist_bin"] = feat["ema20_dist_pct"].map(ema_bin)
    df["bbw_bin"] = feat["bbw_a_bps"].map(bbw_bin)
    df["echo_ratio_bin"] = feat["echo_range_ratio"].map(echo_bin)

    df["clean_2r_winner"] = (df["mfe_r"] >= 2.0) & (df["mae_r"] <= 0.75)
    df["clean_1r_winner"] = (df["mfe_r"] >= 1.0) & (df["mae_r"] <= 0.50)
    df["potential_2r"] = df["mfe_r"] >= 2.0
    df["potential_1r"] = df["mfe_r"] >= 1.0
    df["gave_back_green"] = (df["mfe_r"] >= 0.75) & (df["realized_r"] <= -0.10)
    df["clean_stop"] = (df["mae_r"] >= 0.95) & (df["mfe_r"] < 0.25)
    return df


def aggregate(df, grain):
    return df.groupby(grain, dropna=False).agg(
        n=("realized_r", "size"),
        pairs=("pair", "nunique"),
        years=("year", "nunique"),
        periods=("period", "nunique"),
        clean_2r=("clean_2r_winner", "sum"),
        clean_1r=("clean_1r_winner", "sum"),
        potential_2r=("potential_2r", "sum"),
        potential_1r=("potential_1r", "sum"),
        gave_back=("gave_back_green", "sum"),
        clean_stop=("clean_stop", "sum"),
        sum_mfe_r=("mfe_r", "sum"),
        sum_mae_r=("mae_r", "sum"),
        sum_realized_r=("realized_r", "sum"),
    ).reset_index()


def combine_aggs(parts, grain):
    x = pd.concat(parts, ignore_index=True)
    sum_cols = [c for c in x.columns if c not in grain]
    out = x.groupby(grain, dropna=False)[sum_cols].sum().reset_index()
    out["mean_mfe_r"] = out["sum_mfe_r"] / out["n"]
    out["mean_mae_r"] = out["sum_mae_r"] / out["n"]
    out["mean_realized_r"] = out["sum_realized_r"] / out["n"]
    for c in ["clean_2r", "clean_1r", "potential_2r", "potential_1r", "gave_back", "clean_stop"]:
        out[f"{c}_rate"] = out[c] / out["n"]
    return out


def main():
    files = sorted(CORPUS.glob("*.parquet"))
    if not files:
        raise SystemExit(f"No parquet files at {CORPUS}")
    schema_cols = set(pq.ParquetFile(files[0]).schema.names)
    cols = [c for c in KEEP if c in schema_cols]
    print(f"streaming {len(files)} chunks")

    cell_parts = []
    coarse_parts = []
    label_parts = []
    total_n = total_clean2 = total_pot2 = total_giveback = 0

    for i, f in enumerate(files, 1):
        df = pd.read_parquet(f, columns=cols)
        df = prep_chunk(df)
        total_n += len(df)
        total_clean2 += int(df["clean_2r_winner"].sum())
        total_pot2 += int(df["potential_2r"].sum())
        total_giveback += int(df["gave_back_green"].sum())
        cell_parts.append(aggregate(df, GRAIN))
        coarse_parts.append(aggregate(df, COARSE_GRAIN))
        # Keep old label counts for annotation at same grain.
        lab = df.groupby(GRAIN + ["regime_label", "probe_name"], dropna=False).size().reset_index(name="label_n")
        label_parts.append(lab)
        if i % 25 == 0 or i == len(files):
            print(f"  {i}/{len(files)} chunks; trades={total_n:,}; clean2={total_clean2:,}")

    cells = combine_aggs(cell_parts, GRAIN)
    coarse = combine_aggs(coarse_parts, COARSE_GRAIN)
    global_clean2 = total_clean2 / total_n
    global_pot2 = total_pot2 / total_n
    cells["clean_2r_wilson_low"] = wilson_low(cells["clean_2r"], cells["n"])
    cells["potential_2r_wilson_low"] = wilson_low(cells["potential_2r"], cells["n"])
    cells["clean2_enrichment"] = cells["clean_2r_rate"] / max(global_clean2, 1e-9)
    cells["pot2_enrichment"] = cells["potential_2r_rate"] / max(global_pot2, 1e-9)
    cells = cells.sort_values(["clean_2r_wilson_low", "clean_2r", "clean2_enrichment"], ascending=False)

    candidates = cells[
        (cells["n"] >= 100)
        & (cells["clean_2r"] >= 20)
        & (cells["clean_2r_wilson_low"] >= max(global_clean2 * 1.25, 0.03))
        & (cells["clean2_enrichment"] >= 1.50)
    ].copy().sort_values(["clean_2r_wilson_low", "clean_2r", "mean_realized_r"], ascending=False)

    labels = pd.concat(label_parts, ignore_index=True)
    labels = labels.groupby(GRAIN + ["regime_label", "probe_name"], dropna=False)["label_n"].sum().reset_index()
    ann_rows = []
    if len(candidates):
        cand_keys = set(map(tuple, candidates[GRAIN].itertuples(index=False, name=None)))
        labels["_key"] = list(map(tuple, labels[GRAIN].itertuples(index=False, name=None)))
        sub = labels[labels["_key"].isin(cand_keys)].copy()
        for key, g in sub.groupby(GRAIN, dropna=False):
            total = g["label_n"].sum()
            regimes = (g.groupby("regime_label")["label_n"].sum().sort_values(ascending=False).head(5) / total).round(4).to_dict()
            probes = (g.groupby("probe_name")["label_n"].sum().sort_values(ascending=False).head(8) / total).round(4).to_dict()
            ann_rows.append({**dict(zip(GRAIN, key)), "n": int(total), "regime_mix_top": json.dumps(regimes), "probe_mix_top": json.dumps(probes)})
    annotations = pd.DataFrame(ann_rows)

    cells.to_parquet(OUT / "micro_cells.parquet", index=False)
    cells.to_csv(OUT / "micro_cells.csv", index=False)
    candidates.to_csv(OUT / "microstrategy_candidates.csv", index=False)
    coarse.sort_values(["clean_2r", "clean_2r_rate"], ascending=False).to_csv(OUT / "winner_signature_modes.csv", index=False)
    annotations.to_csv(OUT / "old_label_annotations.csv", index=False)

    report = []
    report.append("# Microstrategy Winner Factory v0")
    report.append("")
    report.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
    report.append(f"Corpus filled trades: {total_n:,} from {len(files)} chunks")
    report.append("")
    report.append("## Frame")
    report.append("")
    report.append("This is winner-first mining. Old regime/probe labels are demoted to annotations. The miner asks: which repeated entry-state shapes produced clean 2R winners on old chart data?")
    report.append("")
    report.append("## Base Rates")
    report.append("")
    report.append(f"- Clean 2R winners: {total_clean2:,} / {total_n:,} = {global_clean2:.2%}")
    report.append(f"- Potential 2R reachers: {total_pot2:,} / {total_n:,} = {global_pot2:.2%}")
    report.append(f"- Gave-back green: {total_giveback:,} / {total_n:,} = {total_giveback / total_n:.2%}")
    report.append("")
    report.append("## Candidate Microstrategy Cells")
    report.append("")
    report.append("Criteria: n>=100, clean_2R>=20, Wilson lower bound above baseline, clean2 enrichment >=1.5x.")
    report.append("")
    if len(candidates):
        show_cols = GRAIN + ["n", "clean_2r", "clean_2r_rate", "clean_2r_wilson_low", "clean2_enrichment", "potential_2r_rate", "gave_back_rate", "mean_mfe_r", "mean_mae_r", "mean_realized_r"]
        report.append(candidates.head(30)[show_cols].to_markdown(index=False, floatfmt=".3f"))
    else:
        report.append("No cells passed strict v0 criteria.")
    report.append("")
    report.append("## Coarse Winner Pockets")
    report.append("")
    show_coarse = coarse.sort_values(["clean_2r", "clean_2r_rate"], ascending=False).head(25)
    report.append(show_coarse[["pair_family", "direction", "session_bucket", "n", "clean_2r", "clean_2r_rate", "potential_2r_rate", "gave_back_rate", "mean_mfe_r", "mean_mae_r", "mean_realized_r"]].to_markdown(index=False, floatfmt=".3f"))
    report.append("")
    report.append("## Next Step")
    report.append("")
    report.append("Take the top candidate cells and build standalone microstrategy specs: entry definition, invalidation, management, and kill tests across discovery/holdout. v1 should generate entries directly from raw M5 bars, not inherited probe candidates.")
    (OUT / "summary.md").write_text("\n".join(report) + "\n")

    print(f"total trades: {total_n:,}")
    print(f"cells: {len(cells):,}; candidates: {len(candidates):,}")
    if len(candidates):
        print(candidates.head(12)[GRAIN + ["n", "clean_2r", "clean_2r_rate", "clean2_enrichment"]].to_string(index=False))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
