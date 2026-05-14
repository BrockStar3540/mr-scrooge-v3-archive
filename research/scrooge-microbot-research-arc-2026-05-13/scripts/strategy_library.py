"""Strategy library — 15 vectorizable formulas from Brock's 2026-05-13 spec.

Per strategy: produces a fire mask + direction over the full M5 series.
Forward-walk simulates outcome (R-multiple net of spread cost) for every fire.

Outputs per (strategy × pair):
  trades parquet: entry_ts, direction, entry_price, sl, tp, realized_R_net,
                  mfe_R, mae_R, exit_reason, plus context features at entry.
"""
import pandas as pd
import numpy as np
import json
from pathlib import Path

ROOT = Path("/tmp/scrooge-research")
DUKA = ROOT / "dukascopy"
OUT  = ROOT / "strategy-library-v1"
OUT.mkdir(exist_ok=True)

PAIRS = ["EUR_USD","GBP_USD","AUD_USD","NZD_USD","USD_JPY","USD_CHF","USD_CAD","USD_MXN",
         "EUR_GBP","EUR_AUD","EUR_NZD","EUR_CAD","EUR_CHF","EUR_JPY",
         "GBP_AUD","GBP_NZD","GBP_CAD","GBP_CHF","GBP_JPY",
         "AUD_CAD","AUD_CHF","AUD_JPY","AUD_NZD","CAD_JPY","CHF_JPY","NZD_JPY"]

SPREAD_PIPS = {
    "EUR_USD": 0.6, "GBP_USD": 0.9, "AUD_USD": 0.8, "NZD_USD": 1.2,
    "USD_JPY": 0.7, "USD_CHF": 1.0, "USD_CAD": 1.2, "USD_MXN": 12.0,
    "EUR_GBP": 1.0, "EUR_AUD": 1.6, "EUR_NZD": 2.8, "EUR_CAD": 1.8,
    "EUR_CHF": 1.4, "EUR_JPY": 1.2,
    "GBP_AUD": 2.5, "GBP_NZD": 3.5, "GBP_CAD": 2.4, "GBP_CHF": 2.2, "GBP_JPY": 1.6,
    "AUD_CAD": 1.5, "AUD_CHF": 1.8, "AUD_JPY": 1.2, "AUD_NZD": 2.0,
    "CAD_JPY": 1.5, "CHF_JPY": 1.6, "NZD_JPY": 1.8,
}

def pip_size(p): return 0.01 if p.endswith("JPY") else 0.0001


# ============================================================
# DATA LOAD + INDICATORS
# ============================================================

def load_m5(pair):
    bars = []
    for f in sorted(DUKA.glob(f"{pair}_M5_*.jsonl")):
        for line in open(f):
            try:
                d = json.loads(line)
                bars.append({
                    "time": d["time"],
                    "open": (d["open_bid"]+d["open_ask"])/2,
                    "high": (d["high_bid"]+d["high_ask"])/2,
                    "low":  (d["low_bid"]+d["low_ask"])/2,
                    "close":(d["close_bid"]+d["close_ask"])/2,
                    "volume": d.get("volume_bid", 0) + d.get("volume_ask", 0),
                })
            except: pass
    df = pd.DataFrame(bars)
    df["ts"] = pd.to_datetime(df["time"], utc=True)
    df = df.sort_values("ts").reset_index(drop=True)
    df = df.drop(columns=["time"])
    return df


def compute_indicators(df):
    c, h, l, v = df["close"], df["high"], df["low"], df["volume"]
    # ATR(14) Wilder
    tr = pd.concat([h-l, (h-c.shift(1)).abs(), (l-c.shift(1)).abs()], axis=1).max(axis=1)
    df["atr14"] = tr.ewm(alpha=1/14, adjust=False).mean()
    # EMAs
    df["ema9"]  = c.ewm(span=9,  adjust=False).mean()
    df["ema20"] = c.ewm(span=20, adjust=False).mean()
    df["ema21"] = c.ewm(span=21, adjust=False).mean()
    df["ema50"] = c.ewm(span=50, adjust=False).mean()
    # BB(20,2)
    sma20 = c.rolling(20).mean()
    std20 = c.rolling(20).std(ddof=0)
    df["bb_mid"] = sma20
    df["bb_upper"] = sma20 + 2*std20
    df["bb_lower"] = sma20 - 2*std20
    df["bb_width"] = (df["bb_upper"]-df["bb_lower"]) / sma20
    # RSI(14) EWMA
    delta = c.diff()
    gain = delta.clip(lower=0).ewm(alpha=1/14, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1/14, adjust=False).mean()
    df["rsi14"] = 100 - 100/(1+gain/loss)
    # Volume ratio (vs 20-period SMA)
    df["vol_sma20"] = v.rolling(20).mean()
    df["vol_ratio"] = v / df["vol_sma20"]
    # price_pos = (close - 20bar low) / (20bar high - 20bar low)
    hh20 = h.rolling(20).max()
    ll20 = l.rolling(20).min()
    df["price_pos"] = (c - ll20) / (hh20 - ll20).replace(0, np.nan)
    df["price_pos"] = df["price_pos"].clip(0, 1)
    # 20-bar prev high/low (for breakouts using -20..-1, NOT current)
    df["high20_prev"] = h.shift(1).rolling(20).max()
    df["low20_prev"]  = l.shift(1).rolling(20).min()
    # ADX(14)
    up_move   = h.diff()
    down_move = -l.diff()
    plus_dm  = pd.Series(np.where((up_move>down_move) & (up_move>0), up_move, 0.0), index=df.index)
    minus_dm = pd.Series(np.where((down_move>up_move) & (down_move>0), down_move, 0.0), index=df.index)
    atr_for_adx = tr.ewm(alpha=1/14, adjust=False).mean()
    plus_di  = 100 * (plus_dm.ewm(alpha=1/14, adjust=False).mean() / atr_for_adx)
    minus_di = 100 * (minus_dm.ewm(alpha=1/14, adjust=False).mean() / atr_for_adx)
    dx = 100 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
    df["adx14"] = dx.ewm(alpha=1/14, adjust=False).mean()
    # Z-score (20)
    df["zscore20"] = (c - sma20) / std20
    # Williams %R
    hh14 = h.rolling(14).max()
    ll14 = l.rolling(14).min()
    df["williams_r"] = (hh14 - c) / (hh14 - ll14).replace(0, np.nan) * -100
    # ATR_ratio = atr14 / daily_atr_avg (rolling 288 bars = 24h)
    df["atr_ratio"] = df["atr14"] / df["atr14"].rolling(288).mean()
    # bb_width ratio
    df["bb_width_rank"] = df["bb_width"].rolling(288).rank(pct=True)
    return df


# ============================================================
# STRATEGY FIRE MASKS — each returns (entry_mask, direction, sl_series, tp_series)
# direction: 'long' or 'short' (or 'both' is split into two strategies)
# We treat each as a single direction. For both-direction strategies, we split.
# ============================================================

def TF1_ema_crossover_long(df):
    """EMA9 > EMA21 crossover. Long only here."""
    mask = (df["ema9"] > df["ema21"]) & (df["ema9"].shift(1) <= df["ema21"].shift(1)) & (df["adx14"] >= 25)
    ep = df["close"]
    sl = ep - 1.5 * df["atr14"]
    tp = ep + 3.0 * df["atr14"]
    return mask, "long", ep, sl, tp

def TF1_ema_crossover_short(df):
    mask = (df["ema9"] < df["ema21"]) & (df["ema9"].shift(1) >= df["ema21"].shift(1)) & (df["adx14"] >= 25)
    ep = df["close"]
    sl = ep + 1.5 * df["atr14"]
    tp = ep - 3.0 * df["atr14"]
    return mask, "short", ep, sl, tp

def TF2_pullback_ema20_long(df):
    mask = ((df["close"] > df["ema20"]) & (df["low"] < df["ema20"]) &
            (df["low"] > df["ema20"]*0.998) & (df["vol_ratio"] > 0.7))
    ep = df["close"]
    sl = df["low"].rolling(5).min()  # min(low[-5:])
    risk = (ep - sl).abs()
    tp = ep + 2 * risk
    return mask, "long", ep, sl, tp

def TF2_pullback_ema20_short(df):
    mask = ((df["close"] < df["ema20"]) & (df["high"] > df["ema20"]) &
            (df["high"] < df["ema20"]*1.002) & (df["vol_ratio"] > 0.7))
    ep = df["close"]
    sl = df["high"].rolling(5).max()
    risk = (sl - ep).abs()
    tp = ep - 2 * risk
    return mask, "short", ep, sl, tp

def TF6_ma_ribbon_long(df):
    rising = ((df["ema9"] > df["ema9"].shift(1)) & (df["ema21"] > df["ema21"].shift(1)) &
              (df["ema50"] > df["ema50"].shift(1)))
    slope = (df["ema50"] - df["ema50"].shift(5)) / df["ema50"].shift(5)
    mask = (df["ema9"] > df["ema21"]) & (df["ema21"] > df["ema50"]) & rising & (slope > 0.0005)
    ep = df["close"]
    sl = df["low"].rolling(10).min()
    risk = (ep - sl).abs()
    tp = ep + 2 * risk
    return mask, "long", ep, sl, tp

def TF6_ma_ribbon_short(df):
    falling = ((df["ema9"] < df["ema9"].shift(1)) & (df["ema21"] < df["ema21"].shift(1)) &
               (df["ema50"] < df["ema50"].shift(1)))
    slope = (df["ema50"] - df["ema50"].shift(5)) / df["ema50"].shift(5)
    mask = (df["ema9"] < df["ema21"]) & (df["ema21"] < df["ema50"]) & falling & (slope < -0.0005)
    ep = df["close"]
    sl = df["high"].rolling(10).max()
    risk = (sl - ep).abs()
    tp = ep - 2 * risk
    return mask, "short", ep, sl, tp

def MR1_rsi_extreme_long(df):
    mask = (df["rsi14"] < 25) & (df["adx14"] < 20)
    ep = df["close"]; sl = ep - 1.5*df["atr14"]; tp = ep + 2*(ep-sl).abs()
    return mask, "long", ep, sl, tp

def MR1_rsi_extreme_short(df):
    mask = (df["rsi14"] > 75) & (df["adx14"] < 20)
    ep = df["close"]; sl = ep + 1.5*df["atr14"]; tp = ep - 2*(sl-ep).abs()
    return mask, "short", ep, sl, tp

def MR2_bb_reversion_long(df):
    mask = (df["close"] < df["bb_lower"]) & (df["vol_ratio"] < 1.5)
    ep = df["close"]; sl = ep - 2*df["atr14"]; tp = df["bb_mid"]
    return mask, "long", ep, sl, tp

def MR2_bb_reversion_short(df):
    mask = (df["close"] > df["bb_upper"]) & (df["vol_ratio"] < 1.5)
    ep = df["close"]; sl = ep + 2*df["atr14"]; tp = df["bb_mid"]
    return mask, "short", ep, sl, tp

def MR4_zscore_long(df):
    mask = (df["zscore20"] < -2.0) & (df["adx14"] < 25)
    ep = df["close"]; sl = ep - 1.5*df["atr14"]; tp = ep + 1.5*(ep-sl).abs()
    return mask, "long", ep, sl, tp

def MR4_zscore_short(df):
    mask = (df["zscore20"] > 2.0) & (df["adx14"] < 25)
    ep = df["close"]; sl = ep + 1.5*df["atr14"]; tp = ep - 1.5*(sl-ep).abs()
    return mask, "short", ep, sl, tp

def MR5_williams_long(df):
    mask = df["williams_r"] < -90
    ep = df["close"]; sl = ep - 1.2*df["atr14"]; tp = ep + 2*(ep-sl).abs()
    return mask, "long", ep, sl, tp

def MR5_williams_short(df):
    mask = df["williams_r"] > -10
    ep = df["close"]; sl = ep + 1.2*df["atr14"]; tp = ep - 2*(sl-ep).abs()
    return mask, "short", ep, sl, tp

def BR1_range_breakout_long(df):
    mask = ((df["close"] > df["high20_prev"]*1.002) & (df["adx14"] >= 20) & (df["vol_ratio"] > 1.1))
    ep = df["close"]; sl = ep - 2*df["atr14"]; tp = ep + 3*df["atr14"]
    return mask, "long", ep, sl, tp

def BR1_range_breakout_short(df):
    mask = ((df["close"] < df["low20_prev"]*0.998) & (df["adx14"] >= 20) & (df["vol_ratio"] > 1.1))
    ep = df["close"]; sl = ep + 2*df["atr14"]; tp = ep - 3*df["atr14"]
    return mask, "short", ep, sl, tp

def BR3_inside_bar_long(df):
    inside = (df["high"].shift(1) < df["high"].shift(2)) & (df["low"].shift(1) > df["low"].shift(2))
    mask = inside & (df["close"] > df["high"].shift(1))
    ep = df["close"]; sl = df["low"].shift(1); tp = ep + 2*(ep-sl).abs()
    return mask, "long", ep, sl, tp

def BR3_inside_bar_short(df):
    inside = (df["high"].shift(1) < df["high"].shift(2)) & (df["low"].shift(1) > df["low"].shift(2))
    mask = inside & (df["close"] < df["low"].shift(1))
    ep = df["close"]; sl = df["high"].shift(1); tp = ep - 2*(sl-ep).abs()
    return mask, "short", ep, sl, tp

def CP1_coil_breakout_long(df):
    coil = (df["bb_width_rank"] <= 0.25) & (df["bb_width_rank"].shift(1) <= 0.25) & (df["bb_width_rank"].shift(2) <= 0.25)
    mask = coil & (df["close"] > df["high"].shift(1).rolling(5).max()) & (df["vol_ratio"] > 1.2)
    ep = df["close"]; sl = ep - 1.5*df["atr14"]; tp = ep + 2*df["atr14"]
    return mask, "long", ep, sl, tp

def CP1_coil_breakout_short(df):
    coil = (df["bb_width_rank"] <= 0.25) & (df["bb_width_rank"].shift(1) <= 0.25) & (df["bb_width_rank"].shift(2) <= 0.25)
    mask = coil & (df["close"] < df["low"].shift(1).rolling(5).min()) & (df["vol_ratio"] > 1.2)
    ep = df["close"]; sl = ep + 1.5*df["atr14"]; tp = ep - 2*df["atr14"]
    return mask, "short", ep, sl, tp

def EX1_momentum_expansion_long(df):
    mask = ((df["atr_ratio"] >= 1.5) & (df["close"] > df["ema50"]) &
            (df["close"] > df["open"]*1.002) & (df["adx14"] >= 40))
    ep = df["close"]; sl = ep - 2*df["atr14"]; tp = ep + 3*df["atr14"]
    return mask, "long", ep, sl, tp

def EX1_momentum_expansion_short(df):
    mask = ((df["atr_ratio"] >= 1.5) & (df["close"] < df["ema50"]) &
            (df["close"] < df["open"]*0.998) & (df["adx14"] >= 40))
    ep = df["close"]; sl = ep + 2*df["atr14"]; tp = ep - 3*df["atr14"]
    return mask, "short", ep, sl, tp

def EX2_expansion_pullback_long(df):
    slope = (df["ema20"] - df["ema20"].shift(5)) / df["ema20"].shift(5)
    mask = (df["atr_ratio"] >= 1.3) & (df["rsi14"] < 50) & (df["close"] < df["ema20"]) & (slope > 0.001)
    ep = df["close"]; sl = ep - 1.5*df["atr14"]; tp = ep + 2*(ep-sl).abs()
    return mask, "long", ep, sl, tp

def EX3_volspike_fade_short(df):
    mask = (df["atr_ratio"] >= 2.0) & (df["close"] > df["bb_upper"]) & (df["adx14"] < 30)
    ep = df["close"]; sl = ep + 1.2*df["atr14"]; tp = ep - 2*(sl-ep).abs()
    return mask, "short", ep, sl, tp

def RG1_range_scalp_short(df):
    mask = (df["adx14"] < 20) & (df["price_pos"] > 0.85)
    ep = df["close"]; sl = ep + 1.0*df["atr14"]; tp = ep - 1.5*(sl-ep).abs()
    return mask, "short", ep, sl, tp

def RG2_support_bounce_long(df):
    mask = (df["adx14"] < 20) & (df["price_pos"] < 0.15)
    ep = df["close"]; sl = ep - 1.0*df["atr14"]; tp = ep + 1.5*(ep-sl).abs()
    return mask, "long", ep, sl, tp

def HY1_trend_pullback_reversal_long(df):
    slope = (df["ema20"] - df["ema20"].shift(5))
    mask = (slope > 0) & (df["rsi14"] < 40) & (df["price_pos"] < 0.4) & (df["adx14"] >= 25)
    ep = df["close"]; sl = ep - 1.5*df["atr14"]; tp = ep + 2.5*(ep-sl).abs()
    return mask, "long", ep, sl, tp

def HY3_overbought_pullback_uptrend_long(df):
    slope = (df["ema20"] - df["ema20"].shift(5))
    mask = (slope > 0) & (df["rsi14"] > 70) & (df["close"] < df["ema20"]) & (df["adx14"] >= 25)
    ep = df["close"]; sl = ep - 1.2*df["atr14"]; tp = ep + 2*(ep-sl).abs()
    return mask, "long", ep, sl, tp

def MO1_exhaustion_after_spike_short(df):
    mask = ((df["close"].shift(1) > df["bb_upper"].shift(1)) & (df["vol_ratio"].shift(1) > 2.0) &
            (df["close"] < df["close"].shift(1)))
    ep = df["close"]; sl = ep + 1.2*df["atr14"]; tp = ep - 1.5*(sl-ep).abs()
    return mask, "short", ep, sl, tp

def MO3_engulfing_short(df):
    bullish_prev = df["close"].shift(1) > df["open"].shift(1)
    engulf = (df["open"] < df["close"].shift(1)) & (df["close"] < df["open"])
    mask = bullish_prev & engulf & (df["price_pos"] > 0.9) & (df["rsi14"] > 70)
    ep = df["close"]; sl = ep + 1.0*df["atr14"]; tp = ep - 1.5*(sl-ep).abs()
    return mask, "short", ep, sl, tp


STRATEGIES = {
    "TF1_long":  TF1_ema_crossover_long,    "TF1_short": TF1_ema_crossover_short,
    "TF2_long":  TF2_pullback_ema20_long,   "TF2_short": TF2_pullback_ema20_short,
    "TF6_long":  TF6_ma_ribbon_long,        "TF6_short": TF6_ma_ribbon_short,
    "MR1_long":  MR1_rsi_extreme_long,      "MR1_short": MR1_rsi_extreme_short,
    "MR2_long":  MR2_bb_reversion_long,     "MR2_short": MR2_bb_reversion_short,
    "MR4_long":  MR4_zscore_long,           "MR4_short": MR4_zscore_short,
    "MR5_long":  MR5_williams_long,         "MR5_short": MR5_williams_short,
    "BR1_long":  BR1_range_breakout_long,   "BR1_short": BR1_range_breakout_short,
    "BR3_long":  BR3_inside_bar_long,       "BR3_short": BR3_inside_bar_short,
    "CP1_long":  CP1_coil_breakout_long,    "CP1_short": CP1_coil_breakout_short,
    "EX1_long":  EX1_momentum_expansion_long, "EX1_short": EX1_momentum_expansion_short,
    "EX2_long":  EX2_expansion_pullback_long,
    "EX3_short": EX3_volspike_fade_short,
    "RG1_short": RG1_range_scalp_short,
    "RG2_long":  RG2_support_bounce_long,
    "HY1_long":  HY1_trend_pullback_reversal_long,
    "HY3_long":  HY3_overbought_pullback_uptrend_long,
    "MO1_short": MO1_exhaustion_after_spike_short,
    "MO3_short": MO3_engulfing_short,
}


# ============================================================
# FORWARD WALK
# ============================================================

def forward_walk(highs, lows, ei, ep, sl, tp, direction, spread_cost, max_hold=300):
    """Walk M5 bars after ei. Return (realized_R_net, mfe_R, mae_R, exit_reason, exit_bars)."""
    if pd.isna(sl) or pd.isna(tp): return np.nan, 0, 0, "bad_sl_or_tp", 0
    risk = abs(ep - sl)
    if risk <= 0: return np.nan, 0, 0, "zero_risk", 0
    end = min(ei + max_hold, len(highs) - 1)
    mfe = mae = 0.0
    for i in range(ei + 1, end + 1):
        h, l = highs[i], lows[i]
        if direction == "long":
            fav = h - ep; adv = ep - l
            if fav > mfe: mfe = fav
            if adv > mae: mae = adv
            if l <= sl: return -1.0 - spread_cost/risk, mfe/risk, mae/risk, "stop", i-ei
            if h >= tp: return abs(tp-ep)/risk - spread_cost/risk, mfe/risk, mae/risk, "tp", i-ei
        else:
            fav = ep - l; adv = h - ep
            if fav > mfe: mfe = fav
            if adv > mae: mae = adv
            if h >= sl: return -1.0 - spread_cost/risk, mfe/risk, mae/risk, "stop", i-ei
            if l <= tp: return abs(ep-tp)/risk - spread_cost/risk, mfe/risk, mae/risk, "tp", i-ei
    return 0.0 - spread_cost/risk, mfe/risk, mae/risk, "time", end-ei


# ============================================================
# RUNNER
# ============================================================

def run_pair(pair):
    print(f"\n=== {pair} ===", flush=True)
    df = load_m5(pair)
    if len(df) < 1000:
        print(f"  insufficient bars: {len(df)}"); return None
    df = compute_indicators(df)
    spread_px = SPREAD_PIPS[pair] * pip_size(pair)
    spread_cost = spread_px / 2  # half-spread per exit
    highs = df["high"].values
    lows = df["low"].values
    ts = df["ts"].values

    all_trades = []
    for sname, sfunc in STRATEGIES.items():
        mask, direction, ep_s, sl_s, tp_s = sfunc(df)
        # Adjust entry/sl/tp for half-spread
        if direction == "long":
            ep_s = ep_s + spread_px/2
        else:
            ep_s = ep_s - spread_px/2
        idx = np.where(mask.fillna(False).values)[0]
        n_fires = len(idx)
        for i in idx:
            ep_i = ep_s.iloc[i]; sl_i = sl_s.iloc[i]; tp_i = tp_s.iloc[i]
            if pd.isna(ep_i) or pd.isna(sl_i) or pd.isna(tp_i): continue
            r, mfe, mae, reason, bars = forward_walk(highs, lows, i, ep_i, sl_i, tp_i, direction, spread_cost)
            all_trades.append({
                "strategy": sname, "pair": pair, "direction": direction,
                "entry_ts": ts[i], "entry_price": ep_i, "sl": sl_i, "tp": tp_i,
                "realized_R": r, "mfe_R": mfe, "mae_R": mae,
                "exit_reason": reason, "exit_bars": bars,
                # context features at entry
                "adx14": df["adx14"].iloc[i], "rsi14": df["rsi14"].iloc[i],
                "atr_ratio": df["atr_ratio"].iloc[i], "bb_width_rank": df["bb_width_rank"].iloc[i],
                "price_pos": df["price_pos"].iloc[i], "vol_ratio": df["vol_ratio"].iloc[i],
                "ema20_dist": (df["close"].iloc[i]-df["ema20"].iloc[i])/df["ema20"].iloc[i],
                "ema50_dist": (df["close"].iloc[i]-df["ema50"].iloc[i])/df["ema50"].iloc[i],
                "zscore20": df["zscore20"].iloc[i],
                "hour_utc": pd.Timestamp(ts[i]).hour,
                "weekday": pd.Timestamp(ts[i]).weekday(),
                "spread_cost_R": spread_cost / (abs(ep_i - sl_i) if abs(ep_i - sl_i) > 0 else 1),
            })
        print(f"  {sname:15s}  fires={n_fires}", flush=True)
    out_df = pd.DataFrame(all_trades)
    out_df.to_parquet(OUT / f"trades_{pair}.parquet", index=False)
    print(f"  wrote {len(out_df)} trades")
    return out_df


if __name__ == "__main__":
    import sys
    pairs_arg = sys.argv[1:] if len(sys.argv) > 1 else PAIRS
    print(f"Running strategy library on {len(pairs_arg)} pairs ...")
    for p in pairs_arg:
        run_pair(p)
    print("\nDONE")
