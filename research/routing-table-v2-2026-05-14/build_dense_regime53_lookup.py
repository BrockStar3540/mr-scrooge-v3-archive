"""Build dense (pair, ts) -> technical_regime_53 lookup.

Computes regime53 for EVERY M5 bar (not just where textbook strategies fired).
Resolves the 49% "unknown" gap in the last-6mo analysis.

Classifier: copied verbatim from
  /home/ubuntu/mr-scrooge-v3/research/technical-regime-53-atlas-v1/build_regime_atlas_v1.py

Inputs:  dukascopy M5 + daily JSONLs on Mini
Output:  ~/scrooge-research/dense_regime53_lookup_last6mo.parquet
         columns: pair, ts, technical_regime_53, technical_regime_desc,
                  ATR14, ATR_ratio, BB_width, BB_compress, ADX14, EMA_slope,
                  RSI14, close_pos
"""
import glob
import json
from pathlib import Path
import numpy as np
import pandas as pd

DUKA = Path("/Users/brock-mini-mac/scrooge-research/dukascopy")
OUT_PARQUET = Path("/Users/brock-mini-mac/scrooge-research/dense_regime53_lookup_last6mo.parquet")
WINDOW_START = pd.Timestamp("2025-10-22", tz="UTC")
HARD_LATEST = pd.Timestamp("2026-04-22", tz="UTC")

PAIRS = [
    "EUR_USD","GBP_USD","AUD_USD","NZD_USD","USD_JPY","USD_CHF","USD_CAD","USD_MXN",
    "EUR_GBP","EUR_AUD","EUR_NZD","EUR_CAD","EUR_CHF","EUR_JPY",
    "GBP_AUD","GBP_NZD","GBP_CAD","GBP_CHF","GBP_JPY",
    "AUD_CAD","AUD_CHF","AUD_JPY","AUD_NZD","CAD_JPY","CHF_JPY","NZD_JPY",
]

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
                try:
                    d = json.loads(line)
                    rows.append({
                        "ts": pd.Timestamp(d["time"]),
                        "open": (d["open_bid"] + d["open_ask"]) / 2.0,
                        "high": (d["high_bid"] + d["high_ask"]) / 2.0,
                        "low":  (d["low_bid"]  + d["low_ask"])  / 2.0,
                        "close":(d["close_bid"]+ d["close_ask"]) / 2.0,
                    })
                except Exception:
                    pass
    if not rows: return pd.DataFrame()
    df = pd.DataFrame(rows).sort_values("ts").drop_duplicates("ts").reset_index(drop=True)
    df["ts"] = pd.to_datetime(df["ts"], utc=True)
    return df


def compute_atr(high, low, close, alpha=1/14):
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=alpha, adjust=False).mean()


def compute_rsi(close):
    delta = close.diff()
    gain = delta.clip(lower=0).ewm(alpha=1/14, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1/14, adjust=False).mean()
    return 100 - 100 / (1 + gain / loss.replace(0, np.nan))


def compute_adx(high, low, close):
    up_move = high.diff()
    down_move = -low.diff()
    plus_dm  = pd.Series(np.where((up_move > down_move) & (up_move > 0), up_move, 0.0), index=high.index)
    minus_dm = pd.Series(np.where((down_move > up_move) & (down_move > 0), down_move, 0.0), index=high.index)
    atr = compute_atr(high, low, close)
    plus_di  = 100 * plus_dm.ewm(alpha=1/14, adjust=False).mean() / atr.replace(0, np.nan)
    minus_di = 100 * minus_dm.ewm(alpha=1/14, adjust=False).mean() / atr.replace(0, np.nan)
    dx = 100 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
    return dx.ewm(alpha=1/14, adjust=False).mean()


def compute_daily_baselines(pair: str) -> pd.DataFrame:
    """Compute daily ATR20 + BBwidth20 baselines.

    Prefers _D_ files when present (legacy); falls back to resampling M5
    to daily when no daily files exist. The Mini currently has no _D_
    files — the fallback path is the live path.
    """
    ddf = load_ohlc(str(DUKA / f"{pair}_D_*.jsonl"))
    if ddf.empty:
        # 2026-05-15 fix: no daily files on disk. Resample M5 to D.
        mdf = load_ohlc(str(DUKA / f"{pair}_M5_*.jsonl"))
        if mdf.empty:
            return pd.DataFrame(columns=["date","daily_atr20_avg","daily_bbwidth20_avg"])
        mdf["date"] = mdf["ts"].dt.floor("D")
        ddf = mdf.groupby("date").agg(
            open=("open","first"), high=("high","max"),
            low=("low","min"),     close=("close","last"),
        ).reset_index().rename(columns={"date":"ts"})
        ddf["ts"] = pd.to_datetime(ddf["ts"], utc=True)
    ddf["daily_atr14"] = compute_atr(ddf["high"], ddf["low"], ddf["close"])
    mid = ddf["close"].rolling(20).mean()
    std = ddf["close"].rolling(20).std(ddof=0)
    ddf["daily_bb_width"] = ((mid + 2*std) - (mid - 2*std)) / mid
    ddf["daily_atr20_avg"] = ddf["daily_atr14"].rolling(20).mean().shift(1)
    ddf["daily_bbwidth20_avg"] = ddf["daily_bb_width"].rolling(20).mean().shift(1)
    ddf["date"] = ddf["ts"].dt.floor("D")
    return ddf[["date","daily_atr20_avg","daily_bbwidth20_avg"]].dropna()


def compute_m5_indicators(pair: str) -> pd.DataFrame:
    df = load_ohlc(str(DUKA / f"{pair}_M5_*.jsonl"))
    if df.empty: return df
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
    sa = (h >= 0) & (h < 8)
    sl = (h >= 8) & (h < 16)
    sn = (h >= 16) & (h < 24)
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
    put("S01", sa & (df["ATR_ratio"] < 0.6) & (df["ADX14"] < 20))
    put("S02", sa & (df["ATR_ratio"] >= 0.6) & (df["ATR_ratio"] < 1.0))
    put("S03", sa & (df["ATR_ratio"] >= 1.0))
    put("S04", sl & cp_mid & (df["ADX14"] < 20))
    put("S05", sn & (df["ATR_ratio"] < 0.7))
    put("S06", sn & (df["ATR_ratio"] >= 0.7))

    out = df[["ts","ATR14","ATR_ratio","BB_width","BB_compress","ADX14","EMA_slope","RSI14","close_pos"]].copy()
    out["technical_regime_53"] = code
    out["technical_regime_desc"] = desc
    return out


import time
t0 = time.time()
all_parts = []
for pair in PAIRS:
    print(f"[{pair}] computing indicators + regime ...", flush=True)
    df = compute_m5_indicators(pair)
    if df.empty:
        print(f"  empty"); continue
    df = df[(df.ts >= WINDOW_START - pd.Timedelta(days=30)) & (df.ts <= HARD_LATEST)]
    if df.empty: continue
    out = assign_regimes(df)
    out = out[out["ts"] >= WINDOW_START]  # cut warmup
    out["pair"] = pair
    out = out[["pair","ts","technical_regime_53","technical_regime_desc",
               "ATR14","ATR_ratio","BB_width","BB_compress","ADX14","EMA_slope","RSI14","close_pos"]]
    print(f"  rows: {len(out):,}  regimes: {out.technical_regime_53.nunique()}")
    all_parts.append(out)

dense = pd.concat(all_parts, ignore_index=True)
dense.to_parquet(OUT_PARQUET, index=False)
print(f"\nsaved {OUT_PARQUET}: {len(dense):,} rows in {time.time()-t0:.1f}s")
print()
print("=== overall regime coverage ===")
print(dense.technical_regime_53.value_counts().head(20).to_string())
print()
print(f"distinct regimes: {dense.technical_regime_53.nunique()}")
print(f"date range: {dense.ts.min()} to {dense.ts.max()}")
