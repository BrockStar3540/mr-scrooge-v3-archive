"""Validate top microstrategy candidates with discovery/holdout kill tests.

This takes the winner-first candidate cells and asks the next practical question:
which repeated winner shapes remain interesting after period split, pair
concentration, and old-label annotation?
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
CANDIDATES = OUT / "microstrategy_candidates.csv"
DISCOVERY_END = pd.Timestamp("2025-01-01", tz="UTC")
TOP_N = 25

PAIR_FAMILY = {
    "EUR_USD": "usd_base", "GBP_USD": "usd_base", "AUD_USD": "usd_base", "NZD_USD": "usd_base",
    "USD_JPY": "usd_base", "USD_CHF": "usd_base", "USD_CAD": "usd_base", "USD_MXN": "usd_base",
    "EUR_GBP": "eur_cross", "EUR_AUD": "eur_cross", "EUR_NZD": "eur_cross", "EUR_CAD": "eur_cross",
    "EUR_CHF": "eur_cross", "EUR_JPY": "eur_cross",
    "GBP_AUD": "gbp_cross", "GBP_NZD": "gbp_cross", "GBP_CAD": "gbp_cross", "GBP_CHF": "gbp_cross", "GBP_JPY": "gbp_cross",
    "AUD_NZD": "antipodean_cross", "AUD_CAD": "antipodean_cross", "AUD_CHF": "antipodean_cross", "AUD_JPY": "antipodean_cross",
    "NZD_JPY": "antipodean_cross", "CAD_JPY": "antipodean_cross", "CHF_JPY": "antipodean_cross",
}
KEEP = ["entry_ts", "pair", "symbol", "direction", "filled", "realized_r", "mfe_r", "mae_r", "regime_label", "probe_name", "feature_snapshot"]
GRAIN = ["pair_family", "direction", "session_bucket", "session_quarter", "bb_pos_bin", "rsi_bin", "ema20_dist_bin", "bbw_bin", "echo_ratio_bin"]


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
    ranges = {"asia": (22*60, 30*60), "london": (6*60, 12*60), "overlap": (12*60, 16*60), "ny_pm": (16*60, 21*60), "rollover": (21*60, 22*60)}
    start, end = ranges[bucket]
    if bucket != "asia": shifted = minute_of_day
    q = min(4, max(1, int((shifted - start) // ((end - start) / 4.0)) + 1))
    return f"{bucket}_q{q}"


def parse_snapshot(s):
    if not isinstance(s, str) or not s:
        return (np.nan, np.nan, np.nan, np.nan, np.nan)
    try: x = json.loads(s)
    except Exception: return (np.nan, np.nan, np.nan, np.nan, np.nan)
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
    ax=abs(float(x))
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
    if n <= 0: return 0.0
    phat = pos / n
    denom = 1 + z*z/n
    center = phat + z*z/(2*n)
    spread = z * np.sqrt((phat*(1-phat) + z*z/(4*n)) / n)
    return float((center - spread) / denom)


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
    parsed = [parse_snapshot(x) for x in df["feature_snapshot"]]
    feat = pd.DataFrame(parsed, columns=["bb_position", "rsi", "ema20_dist_pct", "bbw_a_bps", "echo_range_ratio"], index=df.index)
    df["bb_pos_bin"] = feat["bb_position"].map(bb_bin)
    df["rsi_bin"] = feat["rsi"].map(rsi_bin)
    df["ema20_dist_bin"] = feat["ema20_dist_pct"].map(ema_bin)
    df["bbw_bin"] = feat["bbw_a_bps"].map(bbw_bin)
    df["echo_ratio_bin"] = feat["echo_range_ratio"].map(echo_bin)
    df["period"] = np.where(df["entry_ts"] < DISCOVERY_END, "discovery", "holdout")
    df["clean_2r"] = (df["mfe_r"] >= 2.0) & (df["mae_r"] <= 0.75)
    df["potential_2r"] = df["mfe_r"] >= 2.0
    df["gave_back"] = (df["mfe_r"] >= 0.75) & (df["realized_r"] <= -0.10)
    return df


def score_verdict(disc, hold, global_rate):
    if disc["n"] < 25 or hold["n"] < 20:
        return "REWORK_thin_holdout"
    disc_ok = disc["clean_2r_rate"] >= global_rate * 1.25 and disc["clean_2r_wilson_low"] >= global_rate
    hold_ok = hold["clean_2r_rate"] >= global_rate * 1.25 and hold["clean_2r_wilson_low"] >= global_rate * 0.90
    conc_ok = max(disc["top_pair_clean_share"], hold["top_pair_clean_share"]) <= 0.55
    if disc_ok and hold_ok and conc_ok:
        return "PROMOTE_TO_RAW_M5_REPLAY"
    if disc_ok and not hold_ok:
        return "KILL_holdout_decay"
    if hold_ok and not disc_ok:
        return "REWORK_holdout_only"
    if not conc_ok:
        return "REWORK_pair_concentrated"
    return "KILL_no_period_edge"


def main():
    cand = pd.read_csv(CANDIDATES).head(TOP_N).copy()
    cand["micro_id"] = [f"MS-{i:03d}" for i in range(1, len(cand)+1)]
    keys = {r.micro_id: {c: getattr(r, c) for c in GRAIN} for r in cand.itertuples(index=False)}
    files = sorted(CORPUS.glob("*.parquet"))
    schema_cols = set(pq.ParquetFile(files[0]).schema.names)
    cols = [c for c in KEEP if c in schema_cols]

    rows = []
    pair_rows = []
    label_rows = []
    total_n = total_clean = 0
    print(f"validating {len(cand)} microstrategy candidates across {len(files)} corpus chunks")
    for i, f in enumerate(files, 1):
        df = prep_chunk(pd.read_parquet(f, columns=cols))
        total_n += len(df)
        total_clean += int(df["clean_2r"].sum())
        for mid, vals in keys.items():
            mask = np.ones(len(df), dtype=bool)
            for c, v in vals.items():
                mask &= (df[c].values == v)
            sub = df.loc[mask]
            if sub.empty:
                continue
            g = sub.groupby("period").agg(
                n=("realized_r", "size"), clean_2r=("clean_2r", "sum"), potential_2r=("potential_2r", "sum"), gave_back=("gave_back", "sum"),
                mean_mfe_r=("mfe_r", "mean"), mean_mae_r=("mae_r", "mean"), mean_realized_r=("realized_r", "mean"),
            ).reset_index()
            g.insert(0, "micro_id", mid)
            rows.append(g)
            pg = sub.groupby(["period", "pair"]).agg(n=("realized_r", "size"), clean_2r=("clean_2r", "sum"), mean_realized_r=("realized_r", "mean")).reset_index()
            pg.insert(0, "micro_id", mid)
            pair_rows.append(pg)
            lg = sub.groupby(["period", "regime_label", "probe_name"], dropna=False).size().reset_index(name="n")
            lg.insert(0, "micro_id", mid)
            label_rows.append(lg)
        if i % 25 == 0 or i == len(files):
            print(f"  {i}/{len(files)} chunks")

    global_rate = total_clean / total_n
    period_stats = pd.concat(rows, ignore_index=True).groupby(["micro_id", "period"], as_index=False).sum(numeric_only=True)
    for c in ["clean_2r", "potential_2r", "gave_back"]:
        period_stats[f"{c}_rate"] = period_stats[c] / period_stats["n"]
    period_stats["clean_2r_wilson_low"] = [wilson_low(p, n) for p, n in zip(period_stats["clean_2r"], period_stats["n"])]

    pair_stats = pd.concat(pair_rows, ignore_index=True).groupby(["micro_id", "period", "pair"], as_index=False).sum(numeric_only=True)
    concentration = []
    for (mid, period), g in pair_stats.groupby(["micro_id", "period"]):
        clean_sum = g["clean_2r"].sum()
        n_sum = g["n"].sum()
        top_clean = float(g["clean_2r"].max() / clean_sum) if clean_sum else 1.0
        top_n = float(g["n"].max() / n_sum) if n_sum else 1.0
        top_pair = str(g.sort_values(["clean_2r", "n"], ascending=False).iloc[0]["pair"])
        concentration.append({"micro_id": mid, "period": period, "top_pair": top_pair, "top_pair_clean_share": top_clean, "top_pair_n_share": top_n, "pairs": int(g["pair"].nunique())})
    conc = pd.DataFrame(concentration)
    period_stats = period_stats.merge(conc, on=["micro_id", "period"], how="left")

    # Flatten one row per microbot.
    out_rows = []
    for r in cand.itertuples(index=False):
        mid = r.micro_id
        d = period_stats[(period_stats.micro_id == mid) & (period_stats.period == "discovery")]
        h = period_stats[(period_stats.micro_id == mid) & (period_stats.period == "holdout")]
        dd = d.iloc[0].to_dict() if len(d) else {"n":0,"clean_2r":0,"clean_2r_rate":0,"clean_2r_wilson_low":0,"potential_2r_rate":0,"gave_back_rate":0,"mean_mfe_r":0,"mean_mae_r":0,"mean_realized_r":0,"top_pair_clean_share":1,"top_pair":"none","pairs":0}
        hh = h.iloc[0].to_dict() if len(h) else {"n":0,"clean_2r":0,"clean_2r_rate":0,"clean_2r_wilson_low":0,"potential_2r_rate":0,"gave_back_rate":0,"mean_mfe_r":0,"mean_mae_r":0,"mean_realized_r":0,"top_pair_clean_share":1,"top_pair":"none","pairs":0}
        verdict = score_verdict(dd, hh, global_rate)
        row = {"micro_id": mid, **{c:getattr(r,c) for c in GRAIN}, "overall_n": int(r.n), "overall_clean_2r_rate": float(r.clean_2r_rate), "overall_enrichment": float(r.clean2_enrichment), "verdict": verdict}
        for prefix, src in [("disc", dd), ("hold", hh)]:
            for c in ["n", "clean_2r", "clean_2r_rate", "clean_2r_wilson_low", "potential_2r_rate", "gave_back_rate", "mean_mfe_r", "mean_mae_r", "mean_realized_r", "top_pair", "top_pair_clean_share", "pairs"]:
                row[f"{prefix}_{c}"] = src.get(c)
        out_rows.append(row)
    verdicts = pd.DataFrame(out_rows)

    labels = pd.concat(label_rows, ignore_index=True).groupby(["micro_id", "period", "regime_label", "probe_name"], as_index=False)["n"].sum()
    labels.to_csv(OUT / "microbot_old_label_mix.csv", index=False)
    pair_stats.to_csv(OUT / "microbot_pair_stats.csv", index=False)
    period_stats.to_csv(OUT / "microbot_period_stats.csv", index=False)
    verdicts.to_csv(OUT / "microbot_validation_verdicts.csv", index=False)

    book=[]
    book.append("# Microbot Candidate Book v0")
    book.append("")
    book.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
    book.append(f"Validated top {len(cand)} winner-factory cells against discovery/holdout. Corpus clean-2R baseline: {global_rate:.2%}.")
    book.append("")
    book.append("## Verdict Counts")
    book.append("")
    vc = verdicts["verdict"].value_counts().reset_index()
    vc.columns=["verdict", "count"]
    book.append(vc.to_markdown(index=False))
    book.append("")
    book.append("## Candidate Verdicts")
    book.append("")
    show = verdicts[["micro_id", "verdict"] + GRAIN + ["disc_n", "disc_clean_2r_rate", "disc_top_pair", "disc_top_pair_clean_share", "hold_n", "hold_clean_2r_rate", "hold_top_pair", "hold_top_pair_clean_share", "hold_mean_realized_r"]]
    book.append(show.to_markdown(index=False, floatfmt=".3f"))
    book.append("")
    book.append("## Promotion Meaning")
    book.append("")
    book.append("`PROMOTE_TO_RAW_M5_REPLAY` does not mean production. It means this shape survived the first kill test and deserves a standalone raw-M5 microbot replay with explicit entry, stop, target, and management rules.")
    book.append("")
    book.append("## Next Build")
    book.append("")
    book.append("For promoted/rework cells, generate raw-M5 candidate entries directly from chart physics rather than filtering inherited probe rows. Then validate those entries across discovery/holdout and pair concentration again.")
    (OUT / "microbot_candidate_book.md").write_text("\n".join(book)+"\n")

    print(f"global clean2 baseline: {global_rate:.2%}")
    print(verdicts["verdict"].value_counts().to_string())
    print(verdicts[["micro_id","verdict","pair_family","direction","session_quarter","disc_clean_2r_rate","hold_clean_2r_rate","hold_n"]].to_string(index=False))
    print(f"wrote validation outputs to {OUT}")

if __name__ == "__main__":
    main()
