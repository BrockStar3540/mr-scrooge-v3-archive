"""Raw-M5 Winner Factory v2.

Per Brock 2026-05-13 v2 spec:
  1. Exclude rollover entirely (UTC 21-22 hour).
  2. Apply realistic spread/slippage penalty before scoring.
  3. Expand to all 4 pair families: usd_base, eur_cross, gbp_cross, antipodean_cross.
  4. Add structural triggers:
       T7  pdh_pdl_proximity_reversal
       T8  pdh_pdl_failed_breakout
       T9  session_open_impulse_fade
       T10 compression_expansion_breakout
     (T1-T6 from v1 retained.)
  5. M5 entries; M15 trend alignment + H1 range context as features.
  6. Output winners and losers split by trigger × family × pair × direction × session_quarter × M15_trend × H1_regime.

v2 is NOT the final search. It expands the universe v1 narrowed prematurely.
"""
import pandas as pd
import numpy as np
import json
from pathlib import Path

DUKA = Path("/data/oanda-bot-trainer-cache/dukascopy")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/raw-m5-winner-factory-v2")
OUT.mkdir(parents=True, exist_ok=True)

PAIRS = {
    "usd_base": ["EUR_USD","GBP_USD","AUD_USD","NZD_USD","USD_JPY","USD_CHF","USD_CAD","USD_MXN"],
    "eur_cross": ["EUR_GBP","EUR_AUD","EUR_NZD","EUR_CAD","EUR_CHF","EUR_JPY"],
    "gbp_cross": ["GBP_AUD","GBP_NZD","GBP_CAD","GBP_CHF","GBP_JPY"],
    "antipodean_cross": ["AUD_CAD","AUD_CHF","AUD_JPY","AUD_NZD","CAD_JPY","CHF_JPY","NZD_JPY"],
}
PAIR_FAMILY = {p: fam for fam, lst in PAIRS.items() for p in lst}

# Typical M5 spread in pips (conservative — averaged across sessions, ex-rollover)
SPREAD_PIPS = {
    "EUR_USD": 0.6, "GBP_USD": 0.9, "AUD_USD": 0.8, "NZD_USD": 1.2,
    "USD_JPY": 0.7, "USD_CHF": 1.0, "USD_CAD": 1.2, "USD_MXN": 12.0,
    "EUR_GBP": 1.0, "EUR_AUD": 1.6, "EUR_NZD": 2.8, "EUR_CAD": 1.8,
    "EUR_CHF": 1.4, "EUR_JPY": 1.2,
    "GBP_AUD": 2.5, "GBP_NZD": 3.5, "GBP_CAD": 2.4, "GBP_CHF": 2.2, "GBP_JPY": 1.6,
    "AUD_CAD": 1.5, "AUD_CHF": 1.8, "AUD_JPY": 1.2, "AUD_NZD": 2.0,
    "CAD_JPY": 1.5, "CHF_JPY": 1.6, "NZD_JPY": 1.8,
}

DISCOVERY_END = pd.Timestamp("2025-01-01", tz="UTC")
MAX_HOLD_BARS = 300  # 25h on M5


def pip_size(pair): return 0.01 if pair.endswith("JPY") else 0.0001


def load_pair_m5(pair):
    bars = []
    for f in sorted(Path(DUKA / pair).glob(f"{pair}_M5_*.jsonl")):
        for line in open(f):
            try:
                d = json.loads(line)
                bars.append({
                    "time": d["time"],
                    "open": (d["open_bid"] + d["open_ask"]) / 2,
                    "high": (d["high_bid"] + d["high_ask"]) / 2,
                    "low":  (d["low_bid"]  + d["low_ask"])  / 2,
                    "close":(d["close_bid"]+ d["close_ask"])/ 2,
                })
            except: pass
    df = pd.DataFrame(bars)
    if df.empty: return df
    df["ts"] = pd.to_datetime(df["time"], utc=True)
    return df.sort_values("ts").reset_index(drop=True)


def compute_indicators(df):
    c = df["close"]; h = df["high"]; l = df["low"]
    # BB(20,2) on M5 close
    sma = c.rolling(20).mean()
    std = c.rolling(20).std(ddof=0)
    df["bb_upper"] = sma + 2 * std
    df["bb_lower"] = sma - 2 * std
    df["sma_20"] = sma
    bw = df["bb_upper"] - df["bb_lower"]
    df["bb_position"] = (c - df["bb_lower"]) / bw
    df["bbw_a_bps"] = (bw / sma) * 10000.0
    # rolling BBW for compression detection
    df["bbw_pct_rank_50"] = df["bbw_a_bps"].rolling(50).rank(pct=True)
    # RSI
    delta = c.diff()
    gain = delta.clip(lower=0).ewm(alpha=1/14, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1/14, adjust=False).mean()
    df["rsi"] = 100 - 100/(1 + gain/loss)
    # EMAs
    df["ema20"] = c.ewm(span=20, adjust=False).mean()
    df["ema50"] = c.ewm(span=50, adjust=False).mean()
    df["ema20_dist_bps"] = (c - df["ema20"]) / df["ema20"] * 10000.0
    # ATR
    tr = pd.concat([h-l, (h-c.shift(1)).abs(), (l-c.shift(1)).abs()], axis=1).max(axis=1)
    df["atr14"] = tr.ewm(span=14, adjust=False).mean()
    df["atr14_pct_rank_50"] = df["atr14"].rolling(50).rank(pct=True)
    # echo
    rng = h - l
    df["echo_range_ratio"] = rng / rng.shift(1).rolling(20).mean()
    # prior bars
    df["prev_high"] = h.shift(1)
    df["prev_low"] = l.shift(1)
    df["prev_close"] = c.shift(1)
    return df


def add_pdh_pdl(df):
    """Prior trading day high/low using UTC day boundaries."""
    df["utc_date"] = df["ts"].dt.date
    daily = df.groupby("utc_date").agg(daily_high=("high","max"), daily_low=("low","min")).reset_index()
    daily["pdh"] = daily["daily_high"].shift(1)
    daily["pdl"] = daily["daily_low"].shift(1)
    df = df.merge(daily[["utc_date","pdh","pdl"]], on="utc_date", how="left")
    return df


def add_m15_h1_context(df_m5):
    """Compute M15 trend (price vs EMA20_M15) and H1 range regime as joined features."""
    d = df_m5.set_index("ts")[["open","high","low","close"]]
    # M15 resample
    m15 = d.resample("15min").agg({"open":"first","high":"max","low":"min","close":"last"}).dropna()
    m15["ema20"] = m15["close"].ewm(span=20, adjust=False).mean()
    m15["trend"] = np.where(m15["close"] > m15["ema20"]*1.0005, "up",
                    np.where(m15["close"] < m15["ema20"]*0.9995, "down", "flat"))
    m15 = m15[["trend"]].rename(columns={"trend":"m15_trend"})
    # H1 resample
    h1 = d.resample("1h").agg({"open":"first","high":"max","low":"min","close":"last"}).dropna()
    h1_range = h1["high"] - h1["low"]
    h1_range_rank = h1_range.rolling(48).rank(pct=True)  # 48h rolling rank
    # classify: range_low (rank<0.25) -> consolidation; rank>0.75 -> breakout; else in_range
    h1["regime"] = np.where(h1_range_rank < 0.25, "consolidation",
                    np.where(h1_range_rank > 0.75, "breakout", "in_range"))
    h1 = h1[["regime"]].rename(columns={"regime":"h1_regime"})
    # Forward-fill onto M5 grid using merge_asof
    df = df_m5.copy()
    df = df.sort_values("ts")
    m15 = m15.reset_index().sort_values("ts")
    h1 = h1.reset_index().sort_values("ts")
    df = pd.merge_asof(df, m15, on="ts", direction="backward")
    df = pd.merge_asof(df, h1, on="ts", direction="backward")
    return df


def detect_triggers(df, pair):
    """Vectorized + scalar trigger detection."""
    triggers = []
    # T1: BB lower band reclaim (long)
    m = (df["prev_low"] <= df["bb_lower"].shift(1)) & (df["close"] > df["bb_lower"])
    for i in df.index[m]: triggers.append((i, "T1_bb_lower_reclaim", "long"))
    # T2: BB upper band reject (short)
    m = (df["prev_high"] >= df["bb_upper"].shift(1)) & (df["close"] < df["bb_upper"])
    for i in df.index[m]: triggers.append((i, "T2_bb_upper_reject", "short"))
    # T3: band reentry long
    m = (df["prev_close"] < df["bb_lower"].shift(1)) & (df["close"] > df["bb_lower"])
    for i in df.index[m]: triggers.append((i, "T3_band_reentry_long", "long"))
    # T4: band reentry short
    m = (df["prev_close"] > df["bb_upper"].shift(1)) & (df["close"] < df["bb_upper"])
    for i in df.index[m]: triggers.append((i, "T4_band_reentry_short", "short"))
    # T5: EMA20 reclaim
    delta = df["ema20"] * 0.0005
    m = (df["prev_close"] < (df["ema20"].shift(1) - delta.shift(1))) & (df["close"] > df["ema20"])
    for i in df.index[m]: triggers.append((i, "T5_ema20_reclaim_long", "long"))
    # T6: EMA20 reject
    m = (df["prev_close"] > (df["ema20"].shift(1) + delta.shift(1))) & (df["close"] < df["ema20"])
    for i in df.index[m]: triggers.append((i, "T6_ema20_reject_short", "short"))
    # T7: PDH/PDL proximity reversal (within 5 bps of PDH or PDL, then rejection)
    ps = pip_size(pair)
    prox_long = (df["prev_low"] <= df["pdl"] + 10*ps) & (df["prev_low"] >= df["pdl"] - 10*ps) & (df["close"] > df["prev_close"])
    for i in df.index[prox_long]: triggers.append((i, "T7_pdl_proximity_reversal", "long"))
    prox_short = (df["prev_high"] >= df["pdh"] - 10*ps) & (df["prev_high"] <= df["pdh"] + 10*ps) & (df["close"] < df["prev_close"])
    for i in df.index[prox_short]: triggers.append((i, "T7_pdh_proximity_reversal", "short"))
    # T8: failed PDH/PDL breakout (prev bar broke through, current closes back inside)
    fail_long = (df["prev_low"] < df["pdl"]) & (df["close"] > df["pdl"])
    for i in df.index[fail_long]: triggers.append((i, "T8_pdl_failed_breakdown", "long"))
    fail_short = (df["prev_high"] > df["pdh"]) & (df["close"] < df["pdh"])
    for i in df.index[fail_short]: triggers.append((i, "T8_pdh_failed_breakout", "short"))
    # T9: session-open impulse/fade (first bar of session_quarter q1 with large range — opp-direction fade)
    # We mark the first M5 bar of each new session bucket as candidate IF its range > 1.5× recent.
    df["hour"] = df["ts"].dt.hour
    df["minute"] = df["ts"].dt.minute
    # asia opens 22:00, london 06:00, overlap 12:00, ny_pm 16:00
    open_mask = ((df["hour"]==22) & (df["minute"]==0)) | \
                ((df["hour"]==6)  & (df["minute"]==0)) | \
                ((df["hour"]==12) & (df["minute"]==0)) | \
                ((df["hour"]==16) & (df["minute"]==0))
    big_range = df["echo_range_ratio"] >= 1.5
    op_big = open_mask & big_range
    # fade direction: if open bar closed up, fade short; if closed down, fade long
    op_big_up = op_big & (df["close"] > df["open"])
    op_big_dn = op_big & (df["close"] < df["open"])
    for i in df.index[op_big_up]: triggers.append((i, "T9_session_open_fade", "short"))
    for i in df.index[op_big_dn]: triggers.append((i, "T9_session_open_fade", "long"))
    # T10: compression+expansion (prev BBW rank <= 0.20, current BBW rank >= 0.60, direction = bar direction)
    comp = (df["bbw_pct_rank_50"].shift(1) <= 0.20) & (df["bbw_pct_rank_50"] >= 0.60)
    comp_up = comp & (df["close"] > df["open"])
    comp_dn = comp & (df["close"] < df["open"])
    for i in df.index[comp_up]: triggers.append((i, "T10_compression_expansion", "long"))
    for i in df.index[comp_dn]: triggers.append((i, "T10_compression_expansion", "short"))
    return triggers


def session_quarter_of(hour, minute):
    """Bucket + quarter. Rollover (21-22) is its own bucket and will be filtered out."""
    h = int(hour) % 24
    minute_of_day = h * 60 + int(minute)
    if 22 <= h or h < 6:
        bucket = "asia"
        shifted = minute_of_day + (24*60 if h < 6 else 0)
        start, end = 22*60, 30*60
    elif 6 <= h < 12:
        bucket = "london"; shifted = minute_of_day
        start, end = 6*60, 12*60
    elif 12 <= h < 16:
        bucket = "overlap"; shifted = minute_of_day
        start, end = 12*60, 16*60
    elif 16 <= h < 21:
        bucket = "ny_pm"; shifted = minute_of_day
        start, end = 16*60, 21*60
    else:  # 21-22 rollover — will be auto-killed
        return "rollover", "rollover_q1"
    q = min(4, max(1, int((shifted - start) // ((end - start) / 4.0)) + 1))
    return bucket, f"{bucket}_q{q}"


def bb_bin(x):
    if pd.isna(x): return "bb_unknown"
    if x < -0.05: return "below_band"
    if x < 0.10:  return "lower_rail"
    if x < 0.35:  return "lower_band"
    if x <= 0.65: return "middle"
    if x <= 0.90: return "upper_band"
    if x <= 1.05: return "upper_rail"
    return "above_band"

def rsi_bin(x):
    if pd.isna(x): return "rsi_unknown"
    if x < 30:  return "oversold"
    if x < 45:  return "low"
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
    if x < 5:  return "bbw_tight"
    if x < 15: return "bbw_mid"
    if x < 30: return "bbw_wide"
    return "bbw_explosive"

def echo_bin(x):
    if pd.isna(x): return "echo_unknown"
    if x < 0.70: return "echo_compressed"
    if x < 1.00: return "echo_mid"
    if x < 1.40: return "echo_expanded"
    return "echo_explosive"


def forward_walk(df_high, df_low, ei, ep, sd, direction, spread_cost,
                  max_hold=MAX_HOLD_BARS):
    """Forward walk WITH spread cost. ep already includes entry-side slippage.
    spread_cost is the exit-side slippage in price units (subtract from fav, add to adv).
    Stop = ep -/+ sd. TPs at 1R, 1.5R, 2R measured in sd units.
    Returns (r_1r, r_15r, r_2r, mfe_r_net, mae_r, exit_reason, exit_bars).
    """
    end = min(ei + max_hold, len(df_high) - 1)
    mfe = 0.0; mae = 0.0
    if direction == "long":
        sl = ep - sd
        tp_2r = ep + 2*sd
    else:
        sl = ep + sd
        tp_2r = ep - 2*sd
    for i in range(ei + 1, end + 1):
        bh = df_high[i]; bl = df_low[i]
        if direction == "long":
            adv = ep - bl
            fav = bh - ep
            adverse_hit = bl <= sl
            tp_hit = bh >= tp_2r
        else:
            adv = bh - ep
            fav = ep - bl
            adverse_hit = bh >= sl
            tp_hit = bl <= tp_2r
        if fav > mfe: mfe = fav
        if adv > mae: mae = adv
        if adverse_hit:
            # exit at sl with extra slip = spread_cost
            mfe_net = max(0.0, mfe - spread_cost) / sd
            mae_net = (mae + spread_cost) / sd
            r_1r  = 1.0 if mfe_net >= 1.0 else -1.0 - (spread_cost/sd)
            r_15r = 1.5 if mfe_net >= 1.5 else -1.0 - (spread_cost/sd)
            r_2r  = 2.0 if mfe_net >= 2.0 else -1.0 - (spread_cost/sd)
            return r_1r, r_15r, r_2r, mfe_net, mae_net, "stop", i - ei
        if tp_hit:
            # TP-hit assumed; mfe at least 2R but we still pay spread_cost on exit
            return 1.0 - spread_cost/sd, 1.5 - spread_cost/sd, 2.0 - spread_cost/sd, \
                   (mfe - spread_cost)/sd, mae/sd, "tp_2r", i - ei
    mfe_net = max(0.0, mfe - spread_cost) / sd
    mae_net = (mae + spread_cost) / sd
    r_1r  = 1.0 if mfe_net >= 1.0 else 0.0 - spread_cost/sd
    r_15r = 1.5 if mfe_net >= 1.5 else 0.0 - spread_cost/sd
    r_2r  = 2.0 if mfe_net >= 2.0 else 0.0 - spread_cost/sd
    return r_1r, r_15r, r_2r, mfe_net, mae_net, "time", end - ei


print("Raw-M5 Winner Factory v2 starting ...")
all_pairs = [p for fam in PAIRS for p in PAIRS[fam]]
print(f"Pair scope: {len(all_pairs)} pairs across 4 families")
all_candidates = []

for pair in all_pairs:
    fam = PAIR_FAMILY[pair]
    print(f"\n[{pair}] ({fam}) loading ...", flush=True)
    df = load_pair_m5(pair)
    if df is None or len(df) < 1000:
        print(f"  skip (insufficient data: {len(df) if df is not None else 0})")
        continue
    df = compute_indicators(df)
    df = add_pdh_pdl(df)
    df = add_m15_h1_context(df)
    triggers = detect_triggers(df, pair)
    print(f"  triggers: {len(triggers)}")
    if not triggers: continue

    spread_px = SPREAD_PIPS[pair] * pip_size(pair)
    # entry slippage: spread/2 per side; exit slippage: spread/2.
    # ep_long = close + spread/2, ep_short = close - spread/2; total = spread (round trip)
    df_high = df["high"].values
    df_low = df["low"].values
    df_close = df["close"].values
    df_atr = df["atr14"].values
    df_ts = df["ts"].values
    df_open = df["open"].values

    rows = []
    for ei, trigger_type, direction in triggers:
        sd = df_atr[ei]
        if pd.isna(sd) or sd <= 0: continue
        ep_raw = df_close[ei]
        # entry-side slippage: long pays half-spread up; short pays half-spread down.
        if direction == "long": ep = ep_raw + spread_px / 2
        else:                    ep = ep_raw - spread_px / 2
        # exit-side cost
        spread_cost = spread_px / 2
        # spread cost is high relative to ATR for thin pairs — KILL if cost > 25% of ATR (uneconomic)
        if (spread_px / sd) > 0.25:
            continue
        ts = df["ts"].iloc[ei]
        bucket, sq = session_quarter_of(ts.hour, ts.minute)
        # ROLLOVER AUTO-KILL
        if bucket == "rollover": continue
        r_1r, r_15r, r_2r, mfe_r, mae_r, exit_reason, exit_bars = forward_walk(
            df_high, df_low, ei, ep, sd, direction, spread_cost
        )
        row = df.iloc[ei]
        rows.append({
            "pair": pair, "pair_family": fam,
            "entry_ts": ts, "direction": direction,
            "trigger_type": trigger_type,
            "session_bucket": bucket, "session_quarter": sq,
            "m15_trend": row.get("m15_trend", "unknown"),
            "h1_regime": row.get("h1_regime", "unknown"),
            "entry_price": ep, "atr14": sd,
            "spread_pips": SPREAD_PIPS[pair],
            "spread_cost_R": spread_px / sd,
            "stop_pips": sd / pip_size(pair),
            "bb_position": row["bb_position"], "bb_pos_bin": bb_bin(row["bb_position"]),
            "rsi": row["rsi"], "rsi_bin": rsi_bin(row["rsi"]),
            "ema20_dist_bps": row["ema20_dist_bps"], "ema20_dist_bin": ema_bin(row["ema20_dist_bps"]),
            "bbw_a_bps": row["bbw_a_bps"], "bbw_bin": bbw_bin(row["bbw_a_bps"]),
            "echo_range_ratio": row["echo_range_ratio"], "echo_ratio_bin": echo_bin(row["echo_range_ratio"]),
            "realized_at_1R_net": r_1r, "realized_at_1_5R_net": r_15r, "realized_at_2R_net": r_2r,
            "mfe_r_net": mfe_r, "mae_r": mae_r,
            "exit_reason": exit_reason, "exit_bars": exit_bars,
            "gave_back_green": (mfe_r > 0.5) and (r_2r <= 0),
            "clean_stop": (mae_r >= 0.95) and (mfe_r < 0.25),
            "clean_2r": (mfe_r >= 2.0) and (mae_r <= 0.75),
        })
    pdf = pd.DataFrame(rows)
    if len(pdf):
        print(f"  candidates (post-rollover-kill, post-cost-gate): {len(pdf)}")
        print(f"  clean_2r rate: {pdf['clean_2r'].mean()*100:.1f}%  mean R@2_net: {pdf['realized_at_2R_net'].mean():+.3f}")
        all_candidates.append(pdf)


if not all_candidates:
    print("\nNO candidates generated")
else:
    full = pd.concat(all_candidates, ignore_index=True)
    full["era"] = np.where(full["entry_ts"] < DISCOVERY_END, "discovery", "holdout")
    full.to_parquet(OUT / "raw_m5_v2_candidate_events.parquet", index=False)

    print(f"\n=== TOTAL CANDIDATES (v2): {len(full):,} ===")
    print(f"by family: {full['pair_family'].value_counts().to_dict()}")
    print(f"by era: {full['era'].value_counts().to_dict()}")
    print(f"by trigger:")
    print(full["trigger_type"].value_counts().to_string())

    # CELL: trigger × family × pair × direction × session_quarter × m15_trend × h1_regime
    CELL_FAMILY = ["trigger_type","pair_family","direction","session_quarter","m15_trend","h1_regime"]
    CELL_PAIR   = ["trigger_type","pair_family","pair","direction","session_quarter","m15_trend","h1_regime"]

    def agg_cells(d, keys):
        g = d.groupby(keys, dropna=False).agg(
            n=("entry_ts","size"),
            clean_2r_rate=("clean_2r","mean"),
            gave_back_rate=("gave_back_green","mean"),
            clean_stop_rate=("clean_stop","mean"),
            mfe_r_net_med=("mfe_r_net","median"),
            mae_r_med=("mae_r","median"),
            winner_rate_2r=("realized_at_2R_net", lambda x: (x>0).mean()),
            total_R_2r=("realized_at_2R_net","sum"),
            mean_R_2r=("realized_at_2R_net","mean"),
        ).reset_index()
        return g

    # Discovery-only / holdout-only
    print("\n=== CLUSTERING ===")
    disc = full[full["era"]=="discovery"]
    hold = full[full["era"]=="holdout"]

    fam_cells_disc = agg_cells(disc, CELL_FAMILY).rename(columns={c: c+"_disc" for c in
        ["n","clean_2r_rate","gave_back_rate","clean_stop_rate","mfe_r_net_med",
         "mae_r_med","winner_rate_2r","total_R_2r","mean_R_2r"]})
    fam_cells_hold = agg_cells(hold, CELL_FAMILY).rename(columns={c: c+"_hold" for c in
        ["n","clean_2r_rate","gave_back_rate","clean_stop_rate","mfe_r_net_med",
         "mae_r_med","winner_rate_2r","total_R_2r","mean_R_2r"]})
    fam_cells = fam_cells_disc.merge(fam_cells_hold, on=CELL_FAMILY, how="outer")
    fam_cells.to_csv(OUT / "raw_m5_v2_clusters_family_grain.csv", index=False)
    print(f"  family-grain cells: {len(fam_cells)}")

    pair_cells_disc = agg_cells(disc, CELL_PAIR).rename(columns={c: c+"_disc" for c in
        ["n","clean_2r_rate","gave_back_rate","clean_stop_rate","mfe_r_net_med",
         "mae_r_med","winner_rate_2r","total_R_2r","mean_R_2r"]})
    pair_cells_hold = agg_cells(hold, CELL_PAIR).rename(columns={c: c+"_hold" for c in
        ["n","clean_2r_rate","gave_back_rate","clean_stop_rate","mfe_r_net_med",
         "mae_r_med","winner_rate_2r","total_R_2r","mean_R_2r"]})
    pair_cells = pair_cells_disc.merge(pair_cells_hold, on=CELL_PAIR, how="outer")
    pair_cells.to_csv(OUT / "raw_m5_v2_clusters_pair_grain.csv", index=False)
    print(f"  pair-grain cells: {len(pair_cells)}")

    # PROMISING gates: family grain
    promising = fam_cells[
        (fam_cells["n_disc"] >= 100) &
        (fam_cells["clean_2r_rate_disc"] >= 0.35) &
        (fam_cells["n_hold"] >= 30) &
        (fam_cells["clean_2r_rate_hold"] >= 0.30) &
        (fam_cells["mean_R_2r_disc"] > 0.05) &
        (fam_cells["mean_R_2r_hold"] > 0.0)
    ].sort_values("mean_R_2r_disc", ascending=False)
    promising.to_csv(OUT / "raw_m5_v2_microstrategy_candidates.csv", index=False)
    print(f"\n  promising family-grain cells: {len(promising)}")
    if len(promising):
        print("\n=== TOP 20 PROMISING (family grain) ===")
        cols = ["trigger_type","pair_family","direction","session_quarter","m15_trend","h1_regime",
                "n_disc","clean_2r_rate_disc","mean_R_2r_disc",
                "n_hold","clean_2r_rate_hold","mean_R_2r_hold"]
        print(promising[cols].head(20).to_string(index=False))

    # LOSER cells (anti-promising) — useful as bot-skip rules
    losers = fam_cells[
        (fam_cells["n_disc"] >= 200) &
        (fam_cells["mean_R_2r_disc"] < -0.2) &
        (fam_cells["n_hold"] >= 50) &
        (fam_cells["mean_R_2r_hold"] < -0.1)
    ].sort_values("mean_R_2r_disc")
    losers.to_csv(OUT / "raw_m5_v2_skip_cells.csv", index=False)
    print(f"\n  loser cells (auto-skip candidates): {len(losers)}")
    if len(losers):
        print("\n=== TOP 10 LOSER CELLS ===")
        cols = ["trigger_type","pair_family","direction","session_quarter","m15_trend","h1_regime",
                "n_disc","clean_2r_rate_disc","mean_R_2r_disc",
                "n_hold","clean_2r_rate_hold","mean_R_2r_hold"]
        print(losers[cols].head(10).to_string(index=False))

    print(f"\nsaved {OUT}")
