#!/usr/bin/env python3
"""
Factor Hunt — extract EVERY measurable aspect of each trade from raw OANDA data.
Compare winners vs losers on ALL dimensions to find missing scoring factors.
"""

import os
import requests
import statistics
from datetime import datetime
import time as _time

API_KEY = os.environ["OANDA_API_KEY"]
ACCT = os.environ["OANDA_ACCOUNT_ID"]
ENV = os.environ.get("OANDA_ENVIRONMENT", "live")
BASE = "https://api-fxtrade.oanda.com" if ENV == "live" else "https://api-fxpractice.oanda.com"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}


def get_candles(pair, gran, to_time, count=50):
    _time.sleep(0.4)
    params = {"granularity": gran, "count": str(count), "price": "MBA", "to": to_time}
    r = requests.get(f"{BASE}/v3/instruments/{pair}/candles", headers=HEADERS, params=params)
    return r.json().get("candles", [])


def ema(closes, period):
    if len(closes) < period:
        return None
    m = 2 / (period + 1)
    e = sum(closes[:period]) / period
    for p in closes[period:]:
        e = (p - e) * m + e
    return e


def rsi(closes, period=14):
    if len(closes) < period + 1:
        return None
    changes = [closes[i] - closes[i - 1] for i in range(1, len(closes))]
    recent = changes[-period:]
    g = [c for c in recent if c > 0]
    lo = [-c for c in recent if c < 0]
    ag = sum(g) / period if g else 0.0001
    al = sum(lo) / period if lo else 0.0001
    return round(100 - (100 / (1 + ag / al)), 1)


def extract_all(t):
    """Extract EVERY measurable aspect from raw candle data."""
    sym = t["instrument"]
    units = float(t["initialUnits"])
    entry = float(t["price"])
    close_p = float(t["averageClosePrice"])
    pnl = float(t["realizedPL"])
    open_time = t["openTime"]
    close_time = t["closeTime"]
    direction = "short" if units < 0 else "long"
    pip = 0.01 if "JPY" in sym else 0.0001

    try:
        ot = datetime.fromisoformat(open_time[:26].replace("Z", "+00:00"))
        ct = datetime.fromisoformat(close_time[:26].replace("Z", "+00:00"))
        duration_min = (ct - ot).total_seconds() / 60
        hour_utc = ot.hour
    except:
        duration_min = 0
        hour_utc = 12

    daily = get_candles(sym, "D", open_time, 15)
    hourly = get_candles(sym, "H1", open_time, 60)
    bars_5m = get_candles(sym, "M5", open_time, 60)

    if len(daily) < 3 or len(bars_5m) < 15 or len(hourly) < 20:
        return None

    # --- BOX ---
    entry_date = open_time[:10]
    prior_day = None
    for c in reversed(daily):
        if c["time"][:10] < entry_date:
            h, l = float(c["mid"]["h"]), float(c["mid"]["l"])
            if (h - l) / l > 0.0005:
                prior_day = c
                break
    if not prior_day:
        return None

    pdh = float(prior_day["mid"]["h"])
    pdl = float(prior_day["mid"]["l"])
    box = pdh - pdl
    half = box / 2
    box_pips = box / pip
    center = pdl + half
    box_pos = (entry - pdl) / box if box > 0 else 0.5

    # Wall proximity
    dist_pdh_pips = abs(entry - pdh) / pip
    dist_pdl_pips = abs(entry - pdl) / pip
    if direction == "long":
        wall_prox = (entry - pdl) / box if box > 0 else 1
        at_correct = box_pos < 0.40
    else:
        wall_prox = (pdh - entry) / box if box > 0 else 1
        at_correct = box_pos > 0.60

    # --- ATR ---
    atrs = []
    for i in range(1, len(daily)):
        h = float(daily[i]["mid"]["h"])
        l = float(daily[i]["mid"]["l"])
        pc = float(daily[i - 1]["mid"]["c"])
        atrs.append(max(h - l, abs(h - pc), abs(l - pc)))
    atr = sum(atrs) / len(atrs) if atrs else box
    atr_pips = atr / pip
    atr_box_ratio = atr / box if box > 0 else 1

    # ADR consumed
    tc = daily[-1]["mid"]
    adr_consumed = (float(tc["h"]) - float(tc["l"])) / atr if atr > 0 else 0

    # --- SPREAD ---
    last = bars_5m[-1]
    ask = float(last.get("ask", {}).get("c", 0))
    bid = float(last.get("bid", {}).get("c", 0))
    spread = (ask - bid) if ask > 0 and bid > 0 else pip * 2
    spread_pips = spread / pip
    spread_pct_half = spread / half * 100 if half > 0 else 100
    otr = 2 * spread / half * 100 if half > 0 else 100

    # --- SIGNAL CANDLE ---
    sig_candle = None
    dir_count = 0
    for i in range(len(bars_5m) - 1, max(len(bars_5m) - 8, -1), -1):
        m = bars_5m[i]["mid"]
        o, h, l, c = float(m["o"]), float(m["h"]), float(m["l"]), float(m["c"])
        if sig_candle is None:
            if (direction == "long" and c > o) or (direction == "short" and c < o):
                body = abs(c - o) or pip * 0.1
                rng = h - l or pip * 0.1
                lower_wick = min(o, c) - l
                upper_wick = h - max(o, c)
                wick = lower_wick if direction == "long" else upper_wick
                sig_candle = {
                    "low": l, "high": h, "body": body, "range": rng,
                    "wick": wick, "wick_ratio": wick / body,
                    "body_pct": body / rng,
                }
        else:
            if (direction == "long" and c < o) or (direction == "short" and c > o):
                dir_count += 1
            else:
                break

    # Natural stop
    if sig_candle:
        if direction == "long":
            nat_stop_pips = (entry - (sig_candle["low"] - 2 * pip)) / pip
        else:
            nat_stop_pips = ((sig_candle["high"] + 2 * pip) - entry) / pip
        wick_ratio = sig_candle["wick_ratio"]
        body_pct = sig_candle["body_pct"]
        candle_range_pips = sig_candle["range"] / pip
    else:
        nat_stop_pips = 10
        wick_ratio = 0
        body_pct = 0.5
        candle_range_pips = 0

    # Spread as % of natural stop
    spread_sl_ratio = spread_pips / nat_stop_pips if nat_stop_pips > 0 else 99

    # --- BB / Z-SCORE ---
    closes_1h = [float(c["mid"]["c"]) for c in hourly[-20:]]
    mean_1h = sum(closes_1h) / len(closes_1h)
    std_1h = statistics.stdev(closes_1h) if len(closes_1h) > 1 else 0.0001
    z_score = (entry - mean_1h) / std_1h if std_1h > 0 else 0
    upper_bb = mean_1h + 2 * std_1h
    lower_bb = mean_1h - 2 * std_1h
    bb_width = upper_bb - lower_bb
    bb_pos = (entry - lower_bb) / bb_width if bb_width > 0 else 0.5

    # --- RSI ---
    closes_5m = [float(c["mid"]["c"]) for c in bars_5m[-15:]]
    rsi_val = rsi(closes_5m) or 50

    # --- EMAs ---
    all_1h = [float(c["mid"]["c"]) for c in hourly]
    ema20 = ema(all_1h, 20)
    ema50 = ema(all_1h, 50)

    # EMA distances (% of box)
    ema20_dist_pct = abs(entry - ema20) / box * 100 if ema20 and box > 0 else 0
    ema50_dist_pct = abs(entry - ema50) / box * 100 if ema50 and box > 0 else 0

    # Entry above/below EMA
    entry_above_ema20 = entry > ema20 if ema20 else None
    entry_above_ema50 = entry > ema50 if ema50 else None

    # Counter-trend
    if ema50:
        is_ct = (direction == "long" and entry > ema50) or \
                (direction == "short" and entry < ema50)
    else:
        is_ct = False

    # EMA slope
    if len(all_1h) >= 10:
        r5 = sum(all_1h[-5:]) / 5
        p5 = sum(all_1h[-10:-5]) / 5
        ema_slope = (r5 - p5) / p5 * 100 if p5 > 0 else 0
    else:
        ema_slope = 0
    is_ranging = abs(ema_slope) < 0.02

    # --- VOLUME PROXY ---
    if len(bars_5m) >= 20:
        recent_r = [float(b["mid"]["h"]) - float(b["mid"]["l"]) for b in bars_5m[-5:]]
        older_r = [float(b["mid"]["h"]) - float(b["mid"]["l"]) for b in bars_5m[-20:-5]]
        vol_ratio = (sum(recent_r) / 5) / (sum(older_r) / 15) if sum(older_r) > 0 else 1
    else:
        vol_ratio = 1

    # --- CANDLE PATTERN BEFORE ENTRY ---
    # Count consecutive same-direction candles approaching the zone
    momentum_candles = 0
    for i in range(len(bars_5m) - 2, max(len(bars_5m) - 12, -1), -1):
        m = bars_5m[i]["mid"]
        c, o = float(m["c"]), float(m["o"])
        if direction == "long" and c < o:
            momentum_candles += 1
        elif direction == "short" and c > o:
            momentum_candles += 1
        else:
            break

    # --- PDH/PDL TOUCHES ---
    touch_buf = abs(pdh) * 0.001
    touches_24h = 0
    for h_bar in hourly[-24:]:
        hh = float(h_bar["mid"]["h"])
        hl = float(h_bar["mid"]["l"])
        if abs(hh - pdh) <= touch_buf or abs(hl - pdl) <= touch_buf:
            touches_24h += 1

    # --- DISTANCE FROM CENTER ---
    dist_center_pct = abs(entry - center) / half * 100 if half > 0 else 0

    # --- 5M BAR RANGE STATS ---
    ranges_5m = [float(b["mid"]["h"]) - float(b["mid"]["l"]) for b in bars_5m[-10:]]
    avg_range_5m = sum(ranges_5m) / len(ranges_5m) if ranges_5m else pip
    last_range = ranges_5m[-1] if ranges_5m else 0
    range_expansion = last_range / avg_range_5m if avg_range_5m > 0 else 1

    # --- PRIOR DAY'S CANDLE CHARACTER ---
    prior_close = float(prior_day["mid"]["c"])
    prior_open = float(prior_day["mid"]["o"])
    prior_bullish = prior_close > prior_open
    prior_body_pct = abs(prior_close - prior_open) / box if box > 0 else 0

    return {
        "sym": sym, "dir": direction, "pnl": pnl, "won": pnl > 0,
        "entry": entry, "duration_min": duration_min, "hour_utc": hour_utc,
        # Box
        "box_pips": box_pips, "box_pos": box_pos, "wall_prox": wall_prox,
        "at_correct": at_correct, "dist_center_pct": dist_center_pct,
        "atr_pips": atr_pips, "atr_box_ratio": atr_box_ratio,
        "adr_consumed": adr_consumed,
        # Spread
        "spread_pips": spread_pips, "spread_pct_half": spread_pct_half,
        "otr": otr, "spread_sl_ratio": spread_sl_ratio,
        # Signal candle
        "nat_stop_pips": nat_stop_pips, "wick_ratio": wick_ratio,
        "body_pct": body_pct, "candle_range_pips": candle_range_pips,
        "dir_count": dir_count, "momentum_candles": momentum_candles,
        # BB / z / RSI
        "bb_pos": bb_pos, "z_score": z_score, "rsi": rsi_val,
        # EMA
        "ema20_dist_pct": ema20_dist_pct, "ema50_dist_pct": ema50_dist_pct,
        "ema_slope": ema_slope, "is_ranging": is_ranging, "is_ct": is_ct,
        # Volume / momentum
        "vol_ratio": vol_ratio, "range_expansion": range_expansion,
        # Structure
        "touches_24h": touches_24h, "prior_bullish": prior_bullish,
        "prior_body_pct": prior_body_pct,
    }


def main():
    r = requests.get(f"{BASE}/v3/accounts/{ACCT}/trades", headers=HEADERS,
                     params={"state": "CLOSED", "count": "30"})
    trades = r.json().get("trades", [])
    print(f"Analyzing {len(trades)} V1 LIVE trades for hidden factors...")
    print()

    results = []
    for i, t in enumerate(trades):
        sym = t.get("instrument", "")
        pnl = float(t.get("realizedPL", 0))
        print(f"  [{i + 1}/{len(trades)}] {sym} ${pnl:+,.0f}...", end="", flush=True)
        try:
            a = extract_all(t)
            if a:
                results.append(a)
                print(f" OK")
            else:
                print(" skip")
        except Exception as e:
            print(f" err: {e}")

    winners = [r for r in results if r["won"]]
    losers = [r for r in results if not r["won"]]
    print(f"\nTotal: {len(results)} ({len(winners)}W / {len(losers)}L)")

    # === THE BIG COMPARISON ===
    print()
    print("=" * 90)
    print("EVERY FACTOR: Winners vs Losers")
    print("=" * 90)

    factors = [
        # Box geometry
        ("box_pips", "Box size (pips)"),
        ("box_pos", "Box position (0=PDL, 1=PDH)"),
        ("wall_prox", "Wall proximity (0=at wall, 1=far)"),
        ("at_correct", "At correct wall"),
        ("dist_center_pct", "Distance from center (% of half)"),
        # Volatility
        ("atr_pips", "ATR (pips)"),
        ("atr_box_ratio", "ATR / Box ratio"),
        ("adr_consumed", "ADR consumed"),
        # Cost
        ("spread_pips", "Spread (pips)"),
        ("spread_pct_half", "Spread % of half box"),
        ("otr", "OTR (round-trip %)"),
        ("spread_sl_ratio", "Spread / Natural SL ratio"),
        # Signal candle
        ("nat_stop_pips", "Natural stop (pips)"),
        ("wick_ratio", "Wick ratio"),
        ("body_pct", "Body % of candle range"),
        ("candle_range_pips", "Signal candle range (pips)"),
        ("dir_count", "Directional candle count"),
        ("momentum_candles", "Momentum candles (consecutive)"),
        # BB / z / RSI
        ("bb_pos", "BB position (0-1)"),
        ("z_score", "Z-score"),
        ("rsi", "RSI(14)"),
        # EMA
        ("ema20_dist_pct", "EMA20 distance (% of box)"),
        ("ema50_dist_pct", "EMA50 distance (% of box)"),
        ("ema_slope", "EMA slope (%)"),
        ("is_ranging", "Is ranging"),
        ("is_ct", "Is counter-trend"),
        # Volume
        ("vol_ratio", "Volume ratio (recent/older)"),
        ("range_expansion", "Range expansion"),
        # Structure
        ("touches_24h", "PDH/PDL touches (24h)"),
        ("prior_bullish", "Prior day bullish"),
        ("prior_body_pct", "Prior day body %"),
        # Timing
        ("duration_min", "Duration (minutes)"),
        ("hour_utc", "Entry hour (UTC)"),
    ]

    scored_factors = []
    for key, label in factors:
        w_vals = [r[key] for r in winners if r[key] is not None and not isinstance(r[key], bool)]
        l_vals = [r[key] for r in losers if r[key] is not None and not isinstance(r[key], bool)]

        if isinstance(results[0].get(key), bool):
            w_true = sum(1 for r in winners if r[key] is True)
            l_true = sum(1 for r in losers if r[key] is True)
            w_pct = w_true / len(winners) * 100 if winners else 0
            l_pct = l_true / len(losers) * 100 if losers else 0
            delta = w_pct - l_pct
            scored_factors.append((abs(delta), label, f"{w_pct:.0f}%", f"{l_pct:.0f}%", f"{delta:+.0f}%"))
        elif w_vals and l_vals:
            w_avg = sum(w_vals) / len(w_vals)
            l_avg = sum(l_vals) / len(l_vals)
            if l_avg != 0:
                delta = (w_avg - l_avg) / abs(l_avg) * 100
            else:
                delta = 0
            scored_factors.append((abs(delta), label, f"{w_avg:.2f}", f"{l_avg:.2f}", f"{delta:+.0f}%"))

    # Sort by signal strength
    scored_factors.sort(key=lambda x: x[0], reverse=True)

    print(f"\n{'Factor':<40} {'Winners':>10} {'Losers':>10} {'Delta':>10} {'Signal'}")
    print("-" * 80)
    for strength, label, w_str, l_str, delta_str in scored_factors:
        sig = "***" if strength > 30 else "**" if strength > 15 else "*" if strength > 5 else ""
        print(f"  {label:<38} {w_str:>10} {l_str:>10} {delta_str:>10} {sig}")

    # Show the strongest NEW factors not in current formula
    print()
    print("=" * 90)
    print("TOP NEW FACTORS (not currently in scoring formula)")
    print("=" * 90)
    already_in = {"dir_count", "bb_pos", "rsi", "ema_slope", "is_ranging", "z_score",
                  "wall_prox", "nat_stop_pips", "adr_consumed", "at_correct"}
    new_factors = [(s, l, w, lo, d) for s, l, w, lo, d in scored_factors
                   if not any(k in l.lower() for k in ["directional", "bb pos", "rsi", "ema slope",
                                                        "ranging", "z-score", "wall prox",
                                                        "natural stop", "adr consumed", "correct wall"])]
    for strength, label, w_str, l_str, delta_str in new_factors[:10]:
        print(f"  {label:<38} W={w_str:>10} L={l_str:>10} Delta={delta_str:>10}")


if __name__ == "__main__":
    main()
