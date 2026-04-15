#!/usr/bin/env python3
"""
Trade Recipe Analysis — Reverse engineer what makes a good trade.

For each closed trade, reconstruct EVERYTHING from raw OANDA candle data:
- Box geometry (PDH/PDL, range, position in box)
- Entry quality (distance to zone, signal candle properties)
- Market state (trend, volatility, spread conditions)
- Momentum (candle patterns leading into entry)
- Timing (session, duration, time of day)

Then compare winners vs losers to find the RECIPE.
"""

import os
import requests
from datetime import datetime, timedelta
import statistics

API_KEY = os.environ["OANDA_API_KEY"]
ACCT = os.environ["OANDA_ACCOUNT_ID"]
ENV = os.environ.get("OANDA_ENVIRONMENT", "practice")
BASE = "https://api-fxtrade.oanda.com" if ENV == "live" else "https://api-fxpractice.oanda.com"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}


def candles(pair, gran, to_time, count=50):
    params = {"granularity": gran, "count": str(count), "price": "MBA", "to": to_time}
    r = requests.get(f"{BASE}/v3/instruments/{pair}/candles", headers=HEADERS, params=params)
    return r.json().get("candles", [])


def analyze_trade(t):
    """Reconstruct all data points from raw OANDA candles at entry time."""
    sym = t["instrument"]
    units = float(t["initialUnits"])
    entry = float(t["price"])
    close_p = float(t["averageClosePrice"])
    pnl = float(t["realizedPL"])
    open_time = t["openTime"]
    close_time = t["closeTime"]
    direction = "short" if units < 0 else "long"
    pip = 0.01 if "JPY" in sym else 0.0001

    # Duration
    try:
        ot = datetime.fromisoformat(open_time[:26].replace("Z", "+00:00"))
        ct = datetime.fromisoformat(close_time[:26].replace("Z", "+00:00"))
        duration_min = (ct - ot).total_seconds() / 60
    except:
        duration_min = 0

    hour_utc = int(open_time[11:13])

    # --- RAW DATA PULLS ---
    daily = candles(sym, "D", open_time, count=15)
    hourly = candles(sym, "H1", open_time, count=50)
    bars_5m = candles(sym, "M5", open_time, count=60)

    if len(daily) < 3 or len(bars_5m) < 10:
        return None

    # === 1. BOX GEOMETRY ===
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
    box_range = pdh - pdl
    half_box = box_range / 2
    center = pdl + half_box

    # Position in box (0 = PDL, 1 = PDH)
    box_position = (entry - pdl) / box_range if box_range > 0 else 0.5

    # Distance to nearest wall
    dist_to_pdh = abs(entry - pdh) / pip
    dist_to_pdl = abs(entry - pdl) / pip
    dist_to_nearest_wall = min(dist_to_pdh, dist_to_pdl)

    # Is entry near correct wall? (long near PDL, short near PDH)
    if direction == "long":
        at_correct_wall = dist_to_pdl < dist_to_pdh
        dist_to_target_wall = dist_to_pdl
    else:
        at_correct_wall = dist_to_pdh < dist_to_pdl
        dist_to_target_wall = dist_to_pdh

    # === 2. ATR / VOLATILITY ===
    atrs = []
    for i in range(1, len(daily)):
        h = float(daily[i]["mid"]["h"])
        l = float(daily[i]["mid"]["l"])
        pc = float(daily[i-1]["mid"]["c"])
        atrs.append(max(h - l, abs(h - pc), abs(l - pc)))
    atr = sum(atrs) / len(atrs) if atrs else box_range
    atr_pips = atr / pip
    box_pips = box_range / pip

    # Box-to-ATR ratio (how much of daily range this box represents)
    box_atr_ratio = box_range / atr if atr > 0 else 0

    # ADR consumed at entry (how much of today's range used)
    today_candle = daily[-1] if daily else None
    if today_candle:
        today_h = float(today_candle["mid"]["h"])
        today_l = float(today_candle["mid"]["l"])
        today_range = today_h - today_l
        adr_consumed = today_range / atr if atr > 0 else 0
    else:
        adr_consumed = 0

    # === 3. SPREAD ===
    last_5m = bars_5m[-1] if bars_5m else None
    if last_5m:
        ask = float(last_5m.get("ask", {}).get("c", 0))
        bid = float(last_5m.get("bid", {}).get("c", 0))
        spread = (ask - bid) if ask > 0 and bid > 0 else pip * 2
    else:
        spread = pip * 2
    spread_pips = spread / pip
    spread_pct_of_half = spread / half_box if half_box > 0 else 1
    otr = (2 * spread) / half_box if half_box > 0 else 1

    # === 4. SIGNAL CANDLE QUALITY ===
    # Find the reversal candle (last candle before entry matching direction)
    signal_candle = None
    directional_count = 0  # sucker move strength
    for i in range(len(bars_5m) - 1, max(len(bars_5m) - 8, -1), -1):
        m = bars_5m[i]["mid"]
        o, h, l, c = float(m["o"]), float(m["h"]), float(m["l"]), float(m["c"])
        if signal_candle is None:
            if (direction == "long" and c > o) or (direction == "short" and c < o):
                body = abs(c - o) or pip * 0.1
                lower_wick = min(o, c) - l
                upper_wick = h - max(o, c)
                signal_candle = {
                    "body": body, "range": h - l,
                    "lower_wick": lower_wick, "upper_wick": upper_wick,
                    "wick_ratio": (lower_wick / body) if direction == "long" else (upper_wick / body),
                    "body_pct": body / (h - l) if (h - l) > 0 else 0,
                    "low": l, "high": h,
                }
        else:
            # Count directional candles before the signal candle
            if (direction == "long" and c < o) or (direction == "short" and c > o):
                directional_count += 1
            else:
                break

    # Natural stop from signal candle
    if signal_candle:
        if direction == "long":
            natural_stop = signal_candle["low"] - 2 * pip
            sl_natural_pips = (entry - natural_stop) / pip
        else:
            natural_stop = signal_candle["high"] + 2 * pip
            sl_natural_pips = (natural_stop - entry) / pip
        wick_ratio = signal_candle["wick_ratio"]
        body_pct = signal_candle["body_pct"]
    else:
        sl_natural_pips = 10
        wick_ratio = 0
        body_pct = 0.5

    # === 5. TREND / EMA ===
    # 50-period EMA on hourly closes
    if len(hourly) >= 50:
        closes_1h = [float(c["mid"]["c"]) for c in hourly[-50:]]
        # Simple EMA approximation
        ema50 = sum(closes_1h) / len(closes_1h)
        ema20 = sum(closes_1h[-20:]) / 20

        if direction == "long":
            with_trend = entry < ema50  # buying below EMA = with downtrend reversal
            ema_aligned = ema20 < ema50  # falling EMAs
        else:
            with_trend = entry > ema50
            ema_aligned = ema20 > ema50

        # EMA slope (trend strength)
        if len(closes_1h) >= 10:
            ema_slope = (sum(closes_1h[-5:]) / 5 - sum(closes_1h[-10:-5]) / 5) / (sum(closes_1h[-10:-5]) / 5) * 100
        else:
            ema_slope = 0
    else:
        with_trend = None
        ema_aligned = None
        ema_slope = 0

    # === 6. BOLLINGER BAND POSITION ===
    if len(bars_5m) >= 20:
        closes_5m = [float(c["mid"]["c"]) for c in bars_5m[-20:]]
        sma20 = sum(closes_5m) / 20
        std20 = statistics.stdev(closes_5m) if len(closes_5m) > 1 else 0
        upper_bb = sma20 + 2 * std20
        lower_bb = sma20 - 2 * std20
        bb_width = upper_bb - lower_bb
        bb_position = (entry - lower_bb) / bb_width if bb_width > 0 else 0.5

        # Is price at BB extreme?
        bb_extreme = bb_position > 0.90 or bb_position < 0.10
    else:
        bb_position = 0.5
        bb_extreme = False
        bb_width = 0

    # === 7. MOMENTUM (5M bars) ===
    if len(bars_5m) >= 10:
        ranges_5m = [float(c["mid"]["h"]) - float(c["mid"]["l"]) for c in bars_5m[-10:]]
        avg_range_5m = sum(ranges_5m) / len(ranges_5m)
        last_range = ranges_5m[-1]
        range_expansion = last_range / avg_range_5m if avg_range_5m > 0 else 1

        # RSI approximation (14-period)
        if len(bars_5m) >= 15:
            changes = [float(bars_5m[i]["mid"]["c"]) - float(bars_5m[i-1]["mid"]["c"])
                       for i in range(len(bars_5m)-14, len(bars_5m))]
            gains = [c for c in changes if c > 0]
            losses = [-c for c in changes if c < 0]
            avg_gain = sum(gains) / 14 if gains else 0.001
            avg_loss = sum(losses) / 14 if losses else 0.001
            rs = avg_gain / avg_loss if avg_loss > 0 else 100
            rsi = 100 - (100 / (1 + rs))
        else:
            rsi = 50
    else:
        avg_range_5m = 0
        range_expansion = 1
        rsi = 50

    # === 8. VOLUME PROXY (range-based since forex has no true volume) ===
    if len(bars_5m) >= 20:
        recent_ranges = [float(c["mid"]["h"]) - float(c["mid"]["l"]) for c in bars_5m[-5:]]
        older_ranges = [float(c["mid"]["h"]) - float(c["mid"]["l"]) for c in bars_5m[-20:-5]]
        volume_ratio = (sum(recent_ranges) / len(recent_ranges)) / (sum(older_ranges) / len(older_ranges)) if sum(older_ranges) > 0 else 1
    else:
        volume_ratio = 1

    # === 9. SESSION ===
    if 21 <= hour_utc or hour_utc < 6:
        session = "Sydney"
    elif 0 <= hour_utc < 9:
        session = "Tokyo"
    elif 7 <= hour_utc < 16:
        session = "London"
    elif 13 <= hour_utc < 22:
        session = "NewYork"
    else:
        session = "Off"

    return {
        "sym": sym, "dir": direction, "pnl": pnl, "won": pnl > 0,
        "entry": entry, "duration_min": duration_min, "hour_utc": hour_utc,
        "session": session,
        # Box
        "box_pips": box_pips, "half_pips": half_box / pip,
        "box_position": box_position, "at_correct_wall": at_correct_wall,
        "dist_to_wall_pips": dist_to_target_wall,
        "box_atr_ratio": box_atr_ratio,
        # Volatility
        "atr_pips": atr_pips, "adr_consumed": adr_consumed,
        # Spread
        "spread_pips": spread_pips, "spread_pct_half": spread_pct_of_half,
        "otr": otr,
        # Signal candle
        "wick_ratio": wick_ratio, "body_pct": body_pct,
        "sl_natural_pips": sl_natural_pips,
        "directional_count": directional_count,
        # Trend
        "with_trend": with_trend, "ema_aligned": ema_aligned,
        "ema_slope": ema_slope,
        # BB
        "bb_position": bb_position, "bb_extreme": bb_extreme,
        # Momentum
        "range_expansion": range_expansion, "rsi": rsi,
        "volume_ratio": volume_ratio,
    }


def safe_avg(values):
    return sum(values) / len(values) if values else 0


def safe_median(values):
    return statistics.median(values) if values else 0


def main():
    # Get closed trades
    r = requests.get(f"{BASE}/v3/accounts/{ACCT}/trades", headers=HEADERS,
                     params={"state": "CLOSED", "count": "50"})
    trades = r.json().get("trades", [])
    print(f"Fetching raw OANDA data for {len(trades)} trades...")
    print()

    results = []
    for i, t in enumerate(trades):
        sym = t.get("instrument", "")
        print(f"  [{i+1}/{len(trades)}] {sym} {t['openTime'][:16]}...", end="", flush=True)
        try:
            analysis = analyze_trade(t)
            if analysis:
                results.append(analysis)
                print(f" {'WIN' if analysis['won'] else 'LOSS'} ${analysis['pnl']:+,.0f}")
            else:
                print(" SKIP (insufficient data)")
        except Exception as e:
            print(f" ERROR: {e}")

    winners = [r for r in results if r["won"]]
    losers = [r for r in results if not r["won"]]

    print()
    print(f"Analyzed: {len(results)} trades ({len(winners)}W / {len(losers)}L)")
    print(f"Winners total: ${sum(r['pnl'] for r in winners):+,.2f}")
    print(f"Losers total:  ${sum(r['pnl'] for r in losers):+,.2f}")
    print()

    # === THE RECIPE ===
    print("=" * 100)
    print("THE RECIPE — WINNERS vs LOSERS (averages)")
    print("=" * 100)

    metrics = [
        ("BOX GEOMETRY", [
            ("box_pips", "Box size (pips)"),
            ("half_pips", "Half box (pips)"),
            ("box_position", "Position in box (0=PDL, 1=PDH)"),
            ("at_correct_wall", "At correct wall (long@PDL/short@PDH)"),
            ("dist_to_wall_pips", "Distance to target wall (pips)"),
            ("box_atr_ratio", "Box / ATR ratio"),
        ]),
        ("VOLATILITY / COST", [
            ("atr_pips", "ATR (pips)"),
            ("adr_consumed", "ADR consumed at entry"),
            ("spread_pips", "Spread (pips)"),
            ("spread_pct_half", "Spread % of half box"),
            ("otr", "OTR (round-trip spread / half box)"),
        ]),
        ("SIGNAL CANDLE", [
            ("wick_ratio", "Wick ratio (wick / body)"),
            ("body_pct", "Body % of candle range"),
            ("sl_natural_pips", "Natural stop (pips)"),
            ("directional_count", "Directional candles before signal"),
        ]),
        ("TREND / MOMENTUM", [
            ("with_trend", "With trend"),
            ("ema_aligned", "EMA20/50 aligned"),
            ("ema_slope", "EMA slope (%)"),
            ("bb_position", "BB position (0-1)"),
            ("bb_extreme", "At BB extreme"),
            ("range_expansion", "Range expansion ratio"),
            ("rsi", "RSI(14)"),
            ("volume_ratio", "Volume ratio (recent/older)"),
        ]),
        ("TIMING", [
            ("duration_min", "Duration (minutes)"),
            ("hour_utc", "Hour (UTC)"),
        ]),
    ]

    for category, items in metrics:
        print(f"\n--- {category} ---")
        print(f"{'Metric':<40} {'Winners':>10} {'Losers':>10} {'Delta':>10} {'Signal':>8}")
        for key, label in items:
            w_vals = [r[key] for r in winners if r[key] is not None and r[key] is not False and r[key] is not True]
            l_vals = [r[key] for r in losers if r[key] is not None and r[key] is not False and r[key] is not True]

            # Handle booleans
            if key in ("at_correct_wall", "with_trend", "ema_aligned", "bb_extreme"):
                w_true = sum(1 for r in winners if r[key] is True)
                l_true = sum(1 for r in losers if r[key] is True)
                w_pct = w_true / len(winners) * 100 if winners else 0
                l_pct = l_true / len(losers) * 100 if losers else 0
                delta = w_pct - l_pct
                signal = "***" if abs(delta) > 20 else "**" if abs(delta) > 10 else "*" if abs(delta) > 5 else ""
                print(f"  {label:<38} {w_pct:>9.0f}% {l_pct:>9.0f}% {delta:>+9.0f}% {signal}")
            elif w_vals and l_vals:
                w_avg = safe_avg(w_vals)
                l_avg = safe_avg(l_vals)
                if l_avg != 0:
                    delta_pct = (w_avg - l_avg) / abs(l_avg) * 100
                else:
                    delta_pct = 0
                signal = "***" if abs(delta_pct) > 30 else "**" if abs(delta_pct) > 15 else "*" if abs(delta_pct) > 5 else ""
                print(f"  {label:<38} {w_avg:>10.2f} {l_avg:>10.2f} {delta_pct:>+9.0f}% {signal}")

    # === DISTRIBUTION ANALYSIS ===
    print()
    print("=" * 100)
    print("DISTRIBUTION — Where do winners and losers cluster?")
    print("=" * 100)

    for key, label, buckets in [
        ("box_pips", "Box size", [(0, 40, "<40p"), (40, 70, "40-70p"), (70, 100, "70-100p"), (100, 9999, "100p+")]),
        ("spread_pct_half", "Spread % of half", [(0, 0.05, "<5%"), (0.05, 0.10, "5-10%"), (0.10, 0.15, "10-15%"), (0.15, 1, "15%+")]),
        ("otr", "OTR", [(0, 0.10, "<10%"), (0.10, 0.15, "10-15%"), (0.15, 0.25, "15-25%"), (0.25, 1, "25%+")]),
        ("wick_ratio", "Wick ratio", [(0, 0.5, "<0.5"), (0.5, 1.5, "0.5-1.5"), (1.5, 3, "1.5-3"), (3, 999, "3+")]),
        ("directional_count", "Sucker move candles", [(0, 2, "0-1"), (2, 4, "2-3"), (4, 6, "4-5"), (6, 99, "6+")]),
        ("duration_min", "Duration", [(0, 30, "<30m"), (30, 120, "30m-2h"), (120, 360, "2-6h"), (360, 99999, "6h+")]),
        ("bb_position", "BB position", [(0, 0.2, "<0.2"), (0.2, 0.4, "0.2-0.4"), (0.4, 0.6, "0.4-0.6"), (0.6, 0.8, "0.6-0.8"), (0.8, 1.01, "0.8+")]),
        ("adr_consumed", "ADR consumed", [(0, 0.5, "<50%"), (0.5, 0.8, "50-80%"), (0.8, 1.0, "80-100%"), (1.0, 99, "100%+")]),
        ("rsi", "RSI", [(0, 30, "<30"), (30, 45, "30-45"), (45, 55, "45-55"), (55, 70, "55-70"), (70, 100, "70+")]),
        ("box_atr_ratio", "Box/ATR", [(0, 0.5, "<0.5"), (0.5, 0.8, "0.5-0.8"), (0.8, 1.2, "0.8-1.2"), (1.2, 99, "1.2+")]),
    ]:
        print(f"\n  {label}:")
        for lo, hi, bucket_label in buckets:
            w = [r for r in winners if r.get(key) is not None and lo <= r[key] < hi]
            l = [r for r in losers if r.get(key) is not None and lo <= r[key] < hi]
            total = len(w) + len(l)
            if total == 0:
                continue
            wr = len(w) / total * 100
            net = sum(r["pnl"] for r in w) + sum(r["pnl"] for r in l)
            bar = "#" * len(w) + "." * len(l)
            print(f"    {bucket_label:<10} {len(w):>2}W/{len(l):<2}L  WR={wr:>4.0f}%  Net=${net:>+9,.0f}  {bar}")

    # === BY PAIR ===
    print()
    print("=" * 100)
    print("BY PAIR")
    print("=" * 100)
    for sym in sorted(set(r["sym"] for r in results)):
        w = [r for r in winners if r["sym"] == sym]
        l = [r for r in losers if r["sym"] == sym]
        total = len(w) + len(l)
        wr = len(w) / total * 100 if total > 0 else 0
        net = sum(r["pnl"] for r in w) + sum(r["pnl"] for r in l)
        avg_box = safe_avg([r["box_pips"] for r in w + l])
        avg_spread = safe_avg([r["spread_pips"] for r in w + l])
        avg_otr = safe_avg([r["otr"] for r in w + l])
        print(f"  {sym:<12} {len(w)}W/{len(l)}L WR={wr:>4.0f}% Net=${net:>+9,.0f}  box={avg_box:.0f}p spread={avg_spread:.1f}p otr={avg_otr:.1%}")


if __name__ == "__main__":
    main()
