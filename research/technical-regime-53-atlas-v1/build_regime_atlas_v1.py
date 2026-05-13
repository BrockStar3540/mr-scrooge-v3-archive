"""Technical Regime 53 Atlas v1: bar-true OHLCV classifier.

Implements Brock's 53-regime priority tree from raw Dukascopy M5/D1 bars,
then joins the exact regime label to the Daily Textbook Trade Encyclopedia
candidate events.
"""
from __future__ import annotations

import glob
import json
from pathlib import Path

import numpy as np
import pandas as pd

DUKA = Path("/data/oanda-bot-trainer-cache/dukascopy")
ROOT = Path("/home/ubuntu/mr-scrooge-v3")
SRC = ROOT / "research/raw-m5-winner-factory-v2/raw_m5_v2_candidate_events.parquet"
OUT = ROOT / "research/technical-regime-53-atlas-v1"
OUT.mkdir(parents=True, exist_ok=True)

DISCOVERY_END = pd.Timestamp("2025-01-01", tz="UTC")

REGIME_DESC = {
    "M01": "stop_hunt_up_high_adx", "M02": "stop_hunt_up_low_adx",
    "M03": "stop_hunt_dn_high_adx", "M04": "stop_hunt_dn_low_adx",
    "F01": "false_break_up_strong_trend", "F02": "false_break_up",
    "F03": "false_break_dn_strong_trend", "F04": "false_break_dn",
    "B01": "breakout_up_high_vol_trend", "B02": "breakout_up_strong_adx_low_vol",
    "B03": "breakout_up_moderate_adx", "B04": "breakout_up_weak",
    "B05": "breakout_dn_high_vol_trend", "B06": "breakout_dn_strong_adx_low_vol",
    "B07": "breakout_dn_moderate_adx", "B08": "breakout_dn_weak",
    "C01": "tight_coil_low_adx", "C02": "tight_coil_adx",
    "C03": "compressed_bb_active_atr_low_adx", "C04": "compressed_bb_active_atr_adx",
    "X01": "expansion_strong_uptrend", "X02": "expansion_strong_downtrend",
    "X03": "expansion_strong_adx_flat", "X04": "expansion_moderate_trend", "X05": "expansion_no_trend",
    "T01": "strong_uptrend_extended", "T02": "strong_uptrend_room",
    "T03": "strong_downtrend_extended", "T04": "strong_downtrend_room",
    "T05": "moderate_uptrend", "T06": "moderate_downtrend", "T07": "directional_drift_flat",
    "O01": "overbought_range", "O02": "overbought_trend_caution",
    "O03": "oversold_range", "O04": "oversold_trend_caution",
    "O05": "moderately_overbought", "O06": "moderately_oversold",
    "R01": "wide_volatile_range", "R02": "wide_quiet_range", "R03": "normal_range", "R04": "tight_range",
    "S01": "quiet_asia", "S02": "active_asia", "S03": "volatile_asia",
    "S04": "london_midrange_drift", "S05": "quiet_ny", "S06": "active_ny",
    "Z01": "catch_all",
}


def load_ohlc(glob_pattern: str) -> pd.DataFrame:
    rows = []
    for f in sorted(glob.glob(glob_pattern)):
        with open(f) as fh:
            for line in fh:
                d = json.loads(line)
                rows.append({
                    "ts": pd.Timestamp(d["time"]),
                    "open": (d["open_bid"] + d["open_ask"]) / 2.0,
                    "high": (d["high_bid"] + d["high_ask"]) / 2.0,
                    "low": (d["low_bid"] + d["low_ask"]) / 2.0,
                    "close": (d["close_bid"] + d["close_ask"]) / 2.0,
                    "volume": (d.get("volume_bid", 0.0) + d.get("volume_ask", 0.0)) / 2.0,
                })
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(rows).sort_values("ts").drop_duplicates("ts").reset_index(drop=True)
    df["ts"] = pd.to_datetime(df["ts"], utc=True)
    return df


def compute_atr(high: pd.Series, low: pd.Series, close: pd.Series, alpha: float = 1/14) -> pd.Series:
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=alpha, adjust=False).mean()


def compute_rsi(close: pd.Series) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0).ewm(alpha=1/14, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1/14, adjust=False).mean()
    return 100 - 100 / (1 + gain / loss.replace(0, np.nan))


def compute_adx(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    up_move = high.diff()
    down_move = -low.diff()
    plus_dm = pd.Series(np.where((up_move > down_move) & (up_move > 0), up_move, 0.0), index=high.index)
    minus_dm = pd.Series(np.where((down_move > up_move) & (down_move > 0), down_move, 0.0), index=high.index)
    atr = compute_atr(high, low, close)
    plus_di = 100 * plus_dm.ewm(alpha=1/14, adjust=False).mean() / atr.replace(0, np.nan)
    minus_di = 100 * minus_dm.ewm(alpha=1/14, adjust=False).mean() / atr.replace(0, np.nan)
    dx = 100 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
    return dx.ewm(alpha=1/14, adjust=False).mean()


def compute_daily_baselines(pair: str) -> pd.DataFrame:
    ddf = load_ohlc(str(DUKA / pair / f"{pair}_D_*.jsonl"))
    if ddf.empty:
        return pd.DataFrame(columns=["date", "daily_atr20_avg", "daily_bbwidth20_avg"])
    ddf["daily_atr14"] = compute_atr(ddf["high"], ddf["low"], ddf["close"])
    mid = ddf["close"].rolling(20).mean()
    std = ddf["close"].rolling(20).std(ddof=0)
    ddf["daily_bb_width"] = ((mid + 2*std) - (mid - 2*std)) / mid
    ddf["daily_atr20_avg"] = ddf["daily_atr14"].rolling(20).mean().shift(1)
    ddf["daily_bbwidth20_avg"] = ddf["daily_bb_width"].rolling(20).mean().shift(1)
    ddf["date"] = ddf["ts"].dt.floor("D")
    return ddf[["date", "daily_atr20_avg", "daily_bbwidth20_avg"]].dropna()


def compute_m5_indicators(pair: str) -> pd.DataFrame:
    df = load_ohlc(str(DUKA / pair / f"{pair}_M5_*.jsonl"))
    if df.empty:
        return df
    high, low, close = df["high"], df["low"], df["close"]
    df["ATR14"] = compute_atr(high, low, close)
    mid = close.rolling(20).mean()
    std = close.rolling(20).std(ddof=0)
    upper = mid + 2*std
    lower = mid - 2*std
    df["BB_width"] = (upper - lower) / mid
    df["ADX14"] = compute_adx(high, low, close)
    df["EMA50"] = close.ewm(span=50, adjust=False).mean()
    df["EMA_slope"] = (df["EMA50"] - df["EMA50"].shift(10)) / df["EMA50"].shift(10)
    df["RSI14"] = compute_rsi(close)
    df["max_20"] = high.shift(1).rolling(20).max()
    df["min_20"] = low.shift(1).rolling(20).min()
    rng = (df["max_20"] - df["min_20"]).replace(0, np.nan)
    df["close_pos"] = (close - df["min_20"]) / rng
    df["price_pos"] = df["close_pos"]
    df["breakout_up"] = close > df["max_20"] * 1.002
    df["breakout_dn"] = close < df["min_20"] * 0.998
    bo_up_recent = df["breakout_up"].shift(1).rolling(2).max().fillna(0).astype(bool)
    bo_dn_recent = df["breakout_dn"].shift(1).rolling(2).max().fillna(0).astype(bool)
    df["false_break_up"] = bo_up_recent & (close <= df["max_20"])
    df["false_break_dn"] = bo_dn_recent & (close >= df["min_20"])
    sweep_up = low < df["min_20"] * 0.998
    sweep_dn = high > df["max_20"] * 1.002
    df["stop_hunt_up"] = sweep_up.rolling(2).max().fillna(0).astype(bool) & (close > df["min_20"])
    df["stop_hunt_dn"] = sweep_dn.rolling(2).max().fillna(0).astype(bool) & (close < df["max_20"])
    df["date"] = df["ts"].dt.floor("D")
    bases = compute_daily_baselines(pair)
    if bases.empty:
        df["ATR_ratio"] = np.nan
        df["BB_compress"] = np.nan
    else:
        df = df.merge(bases, on="date", how="left")
        df["ATR_ratio"] = df["ATR14"] / df["daily_atr20_avg"]
        df["BB_compress"] = df["BB_width"] / df["daily_bbwidth20_avg"]
    return df


def assign_regimes(df: pd.DataFrame) -> pd.DataFrame:
    n = len(df)
    code = np.array(["Z01"] * n, dtype=object)
    desc = np.array([REGIME_DESC["Z01"]] * n, dtype=object)
    unmatched = np.ones(n, dtype=bool)

    def put(name: str, cond) -> None:
        nonlocal unmatched, code, desc
        m = np.asarray(cond.fillna(False) if hasattr(cond, "fillna") else cond, dtype=bool) & unmatched
        code[m] = name
        desc[m] = REGIME_DESC[name]
        unmatched[m] = False

    h = df["ts"].dt.hour
    session_asia = (h >= 0) & (h < 8)
    session_london = (h >= 8) & (h < 16)
    session_ny = (h >= 16) & (h < 24)
    cp_mid = df["close_pos"].between(0.45, 0.55)
    abs_slope = df["EMA_slope"].abs()

    put("M01", df["stop_hunt_up"] & (df["ADX14"] >= 20))
    put("M02", df["stop_hunt_up"] & (df["ADX14"] < 20))
    put("M03", df["stop_hunt_dn"] & (df["ADX14"] >= 20))
    put("M04", df["stop_hunt_dn"] & (df["ADX14"] < 20))
    put("F01", df["false_break_up"] & (df["ADX14"] >= 30))
    put("F02", df["false_break_up"] & (df["ADX14"] < 30))
    put("F03", df["false_break_dn"] & (df["ADX14"] >= 30))
    put("F04", df["false_break_dn"] & (df["ADX14"] < 30))
    put("B01", df["breakout_up"] & (df["ADX14"] >= 40) & (df["ATR_ratio"] >= 1.2))
    put("B02", df["breakout_up"] & (df["ADX14"] >= 40) & (df["ATR_ratio"] < 1.2))
    put("B03", df["breakout_up"] & (df["ADX14"] < 40) & (df["ADX14"] >= 25))
    put("B04", df["breakout_up"] & (df["ADX14"] < 25))
    put("B05", df["breakout_dn"] & (df["ADX14"] >= 40) & (df["ATR_ratio"] >= 1.2))
    put("B06", df["breakout_dn"] & (df["ADX14"] >= 40) & (df["ATR_ratio"] < 1.2))
    put("B07", df["breakout_dn"] & (df["ADX14"] < 40) & (df["ADX14"] >= 25))
    put("B08", df["breakout_dn"] & (df["ADX14"] < 25))
    put("C01", (df["BB_compress"] <= 0.75) & (df["ATR_ratio"] <= 0.8) & (df["ADX14"] < 20))
    put("C02", (df["BB_compress"] <= 0.75) & (df["ATR_ratio"] <= 0.8) & (df["ADX14"] >= 20))
    put("C03", (df["BB_compress"] <= 0.75) & (df["ATR_ratio"] > 0.8) & (df["ADX14"] < 20))
    put("C04", (df["BB_compress"] <= 0.75) & (df["ATR_ratio"] > 0.8) & (df["ADX14"] >= 20))
    put("X01", (df["ATR_ratio"] >= 1.5) & (df["ADX14"] >= 40) & (df["EMA_slope"] > 0.002))
    put("X02", (df["ATR_ratio"] >= 1.5) & (df["ADX14"] >= 40) & (df["EMA_slope"] < -0.002))
    put("X03", (df["ATR_ratio"] >= 1.5) & (df["ADX14"] >= 40) & (abs_slope <= 0.002))
    put("X04", (df["ATR_ratio"] >= 1.5) & (df["ADX14"] < 40) & (df["ADX14"] >= 25))
    put("X05", (df["ATR_ratio"] >= 1.5) & (df["ADX14"] < 25))
    put("T01", (df["ADX14"] >= 40) & (df["EMA_slope"] > 0.002) & (df["close_pos"] >= 0.8))
    put("T02", (df["ADX14"] >= 40) & (df["EMA_slope"] > 0.002) & (df["close_pos"] < 0.8))
    put("T03", (df["ADX14"] >= 40) & (df["EMA_slope"] < -0.002) & (df["close_pos"] <= 0.2))
    put("T04", (df["ADX14"] >= 40) & (df["EMA_slope"] < -0.002) & (df["close_pos"] > 0.2))
    put("T05", (df["ADX14"] >= 25) & (df["ADX14"] < 40) & (df["EMA_slope"] > 0.001))
    put("T06", (df["ADX14"] >= 25) & (df["ADX14"] < 40) & (df["EMA_slope"] < -0.001))
    put("T07", (df["ADX14"] >= 25) & (df["ADX14"] < 40) & (abs_slope <= 0.001))
    put("O01", (df["RSI14"] > 80) & (df["close_pos"] > 0.9) & (df["ADX14"] < 25))
    put("O02", (df["RSI14"] > 80) & (df["close_pos"] > 0.9) & (df["ADX14"] >= 25))
    put("O03", (df["RSI14"] < 20) & (df["close_pos"] < 0.1) & (df["ADX14"] < 25))
    put("O04", (df["RSI14"] < 20) & (df["close_pos"] < 0.1) & (df["ADX14"] >= 25))
    put("O05", (df["RSI14"] > 70) & (df["RSI14"] <= 80) & (df["close_pos"] > 0.85))
    put("O06", (df["RSI14"] < 30) & (df["RSI14"] >= 20) & (df["close_pos"] < 0.15))
    put("R01", (df["ADX14"] < 20) & (df["BB_width"] >= 0.05) & (df["ATR_ratio"] >= 1.0))
    put("R02", (df["ADX14"] < 20) & (df["BB_width"] >= 0.05) & (df["ATR_ratio"] < 1.0))
    put("R03", (df["ADX14"] < 20) & (df["BB_width"] < 0.05) & (df["BB_width"] >= 0.02))
    put("R04", (df["ADX14"] < 20) & (df["BB_width"] < 0.02))
    put("S01", session_asia & (df["ATR_ratio"] < 0.6) & (df["ADX14"] < 20))
    put("S02", session_asia & (df["ATR_ratio"] >= 0.6) & (df["ATR_ratio"] < 1.0))
    put("S03", session_asia & (df["ATR_ratio"] >= 1.0))
    put("S04", session_london & cp_mid & (df["ADX14"] < 20))
    put("S05", session_ny & (df["ATR_ratio"] < 0.7))
    put("S06", session_ny & (df["ATR_ratio"] >= 0.7))

    out = df[["ts", "ATR14", "ATR_ratio", "BB_width", "BB_compress", "ADX14", "EMA_slope", "RSI14", "close_pos"]].copy()
    out["technical_regime_53"] = code
    out["technical_regime_desc"] = desc
    return out


def summarize(joined: pd.DataFrame) -> None:
    joined["era"] = np.where(joined["entry_ts"] < DISCOVERY_END, "discovery", "holdout")
    joined["strategy_name"] = joined.get("strategy_name", pd.Series(index=joined.index, dtype=object)).fillna(joined["trigger_type"])
    if "row_type" in joined.columns:
        repaired = joined[joined["row_type"].eq("repaired_winner")].copy()
        fp = joined[joined["row_type"].eq("first_pass")].copy()
    else:
        repaired = joined[joined["clean_2r"].astype(bool)].copy()
        fp = joined.copy()

    group_cols = ["technical_regime_53", "technical_regime_desc", "strategy_name", "pair_family", "direction"]
    rep_sum = repaired.groupby(group_cols).agg(
        repaired_winners=("entry_ts", "size"),
        median_R=("realized_at_2R_net", "median"),
        median_mfe=("mfe_r_net", "median"),
        median_mae=("mae_r", "median"),
        discovery_winners=("era", lambda x: int((x == "discovery").sum())),
        holdout_winners=("era", lambda x: int((x == "holdout").sum())),
    ).reset_index().sort_values(["repaired_winners", "median_R"], ascending=[False, False])
    rep_sum.to_csv(OUT / "strategy_x_regime53_repaired_winners_bartrue.csv", index=False)

    fp_sum = fp.groupby(group_cols).agg(
        first_pass_n=("entry_ts", "size"),
        first_pass_win_rate=("clean_2r", "mean"),
        mean_R=("realized_at_2R_net", "mean"),
        median_mfe=("mfe_r_net", "median"),
    ).reset_index().sort_values("first_pass_n", ascending=False)
    fp_sum.to_csv(OUT / "strategy_x_regime53_first_pass_bartrue.csv", index=False)

    coverage = joined.groupby(["technical_regime_53", "technical_regime_desc"]).agg(
        rows=("entry_ts", "size"),
        first_pass_win_rate=("clean_2r", "mean"),
        mean_R=("realized_at_2R_net", "mean"),
    ).reset_index().sort_values("rows", ascending=False)
    coverage.to_csv(OUT / "regime53_ledger_coverage_bartrue.csv", index=False)

    with open(OUT / "summary.md", "w") as f:
        f.write("# Technical Regime 53 Atlas v1\n\n")
        f.write("Bar-true implementation of Brock's 53-regime OHLCV decision tree, joined to the daily textbook trade encyclopedia.\n\n")
        f.write("## Implementation Notes\n\n")
        f.write("- M5 indicators: ATR14, BB_width, ADX14, EMA50 slope, RSI14, close_pos.\n")
        f.write("- Daily baselines: prior completed 20-day average daily ATR14 and daily BB_width.\n")
        f.write("- Breakout/sweep thresholds use prior 20-bar high/low to avoid current-bar self-reference.\n")
        f.write("- Priority order follows the supplied 53-regime tree.\n\n")
        f.write("## Coverage\n\n")
        f.write(f"- Candidate rows labeled: {len(joined):,}\n")
        f.write(f"- Regimes represented: {joined['technical_regime_53'].nunique()}\n")
        f.write(f"- Repaired winners represented: {len(repaired):,}\n\n")
        f.write("## Top Repaired Winner Synchrony\n\n")
        f.write(rep_sum.head(30).to_markdown(index=False))
        f.write("\n\n## First-Pass Strategy x Regime\n\n")
        f.write(fp_sum.head(20).to_markdown(index=False))
        f.write("\n\n## Read This Correctly\n\n")
        f.write("The repaired-winner table is the strategy-discovery map: it says where the same-day winning trade existed after replay. The first-pass table says what a deterministic selector would have done before repair. A microstrategy candidate needs both: a repeated repaired-winner shape and a first-pass selector that can be made positive without hindsight.\n")


def main() -> None:
    events = pd.read_parquet(SRC)
    events["entry_ts"] = pd.to_datetime(events["entry_ts"], utc=True)
    pairs = sorted(events["pair"].unique())
    labeled_parts = []
    print(f"Loaded {len(events):,} candidate rows across {len(pairs)} pairs")
    for pair in pairs:
        pair_events = events[events["pair"] == pair].copy()
        print(f"[{pair}] events={len(pair_events):,}: computing bar-true regimes", flush=True)
        bars = compute_m5_indicators(pair)
        if bars.empty:
            print("  no bars; skipping", flush=True)
            continue
        labels = assign_regimes(bars)
        labels["pair"] = pair
        merged = pair_events.merge(labels, left_on=["pair", "entry_ts"], right_on=["pair", "ts"], how="left")
        miss = int(merged["technical_regime_53"].isna().sum())
        if miss:
            print(f"  warning: {miss:,} event rows did not match bar labels", flush=True)
        labeled_parts.append(merged.drop(columns=["ts"], errors="ignore"))
        print(f"  regimes={merged['technical_regime_53'].nunique()} top={merged['technical_regime_53'].value_counts().head(3).to_dict()}", flush=True)
    joined = pd.concat(labeled_parts, ignore_index=True)
    joined.to_parquet(OUT / "daily_trade_ledger_with_regime53_bartrue.parquet", index=False)
    joined.to_csv(OUT / "daily_trade_ledger_with_regime53_bartrue.csv", index=False)
    summarize(joined)
    print(f"Done. Outputs in {OUT}", flush=True)


if __name__ == "__main__":
    main()
