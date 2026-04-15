#!/usr/bin/env python3
"""
Scoring Simulator — test OLD vs NEW scoring formulas against real OANDA trades.

For each trade:
1. Pull raw candle data at entry time
2. Reconstruct all scoring inputs from market data
3. Run both OLD and NEW scoring formulas
4. Compare: which formula better separates winners from losers?

Scoring formulas tested:
  OLD = current V1/V2 system
  NEW = recipe-calibrated (remove OTR, reduce RR/ATR, add wall proximity + conviction)
  AGGRESSIVE = maximum recipe alignment (strongest penalties)
"""

import os
import requests
import statistics
from datetime import datetime

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
    sym = t["instrument"]
    units = float(t["initialUnits"])
    entry = float(t["price"])
    pnl = float(t["realizedPL"])
    open_time = t["openTime"]
    direction = "short" if units < 0 else "long"
    pip = 0.01 if "JPY" in sym else 0.0001

    daily = candles(sym, "D", open_time, count=15)
    hourly = candles(sym, "H1", open_time, count=50)
    bars_5m = candles(sym, "M5", open_time, count=60)

    if len(daily) < 3 or len(bars_5m) < 20:
        return None

    # Box
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
    box_pips = box_range / pip

    # Box position (0=PDL, 1=PDH)
    box_position = (entry - pdl) / box_range if box_range > 0 else 0.5
    dist_to_pdh = abs(entry - pdh) / pip
    dist_to_pdl = abs(entry - pdl) / pip

    if direction == "long":
        at_correct_wall = box_position < 0.40
        wall_proximity_pct = (entry - pdl) / box_range if box_range > 0 else 1.0
    else:
        at_correct_wall = box_position > 0.60
        wall_proximity_pct = (pdh - entry) / box_range if box_range > 0 else 1.0

    # ATR
    atrs = []
    for i in range(1, len(daily)):
        h = float(daily[i]["mid"]["h"])
        l = float(daily[i]["mid"]["l"])
        pc = float(daily[i-1]["mid"]["c"])
        atrs.append(max(h - l, abs(h - pc), abs(l - pc)))
    atr = sum(atrs) / len(atrs) if atrs else box_range

    # ADR consumed
    today_c = daily[-1]["mid"] if daily else None
    if today_c:
        adr_consumed = (float(today_c["h"]) - float(today_c["l"])) / atr if atr > 0 else 0
    else:
        adr_consumed = 0

    # Spread
    last = bars_5m[-1] if bars_5m else None
    if last:
        ask = float(last.get("ask", {}).get("c", 0))
        bid = float(last.get("bid", {}).get("c", 0))
        spread = (ask - bid) if ask > 0 and bid > 0 else pip * 2
    else:
        spread = pip * 2
    spread_pips = spread / pip
    otr = (2 * spread) / half_box if half_box > 0 else 1

    # Signal candle
    signal_candle = None
    directional_count = 0
    for i in range(len(bars_5m) - 1, max(len(bars_5m) - 8, -1), -1):
        m = bars_5m[i]["mid"]
        o, h, l, c = float(m["o"]), float(m["h"]), float(m["l"]), float(m["c"])
        if signal_candle is None:
            if (direction == "long" and c > o) or (direction == "short" and c < o):
                body = abs(c - o) or pip * 0.1
                lower_wick = min(o, c) - l
                upper_wick = h - max(o, c)
                wick = lower_wick if direction == "long" else upper_wick
                signal_candle = {"body": body, "wick": wick, "low": l, "high": h,
                                 "wick_ratio": wick / body}
        else:
            if (direction == "long" and c < o) or (direction == "short" and c > o):
                directional_count += 1
            else:
                break

    # Natural stop
    if signal_candle:
        if direction == "long":
            natural_stop_pips = (entry - (signal_candle["low"] - 2 * pip)) / pip
        else:
            natural_stop_pips = ((signal_candle["high"] + 2 * pip) - entry) / pip
        wick_ratio = signal_candle["wick_ratio"]
    else:
        natural_stop_pips = 10
        wick_ratio = 0

    # RR
    tp2_dist = half_box / pip
    tp1_dist = tp2_dist / 2
    rr_tp1 = tp1_dist / natural_stop_pips if natural_stop_pips > 0 else 0
    rr_tp2 = tp2_dist / natural_stop_pips if natural_stop_pips > 0 else 0

    # BB position
    closes_1h = [float(c["mid"]["c"]) for c in hourly[-20:]] if len(hourly) >= 20 else []
    if len(closes_1h) >= 20:
        mean = sum(closes_1h) / len(closes_1h)
        std = statistics.stdev(closes_1h)
        if std > 0:
            z_score = (entry - mean) / std
            upper = mean + 2 * std
            lower = mean - 2 * std
            width = upper - lower
            bb_pos = (entry - lower) / width if width > 0 else 0.5
        else:
            z_score = 0
            bb_pos = 0.5
    else:
        z_score = 0
        bb_pos = 0.5

    # RSI
    if len(bars_5m) >= 15:
        closes_5m = [float(c["mid"]["c"]) for c in bars_5m[-15:]]
        changes = [closes_5m[i] - closes_5m[i-1] for i in range(1, len(closes_5m))]
        gains = [c for c in changes if c > 0]
        losses = [-c for c in changes if c < 0]
        avg_gain = sum(gains) / 14 if gains else 0.001
        avg_loss = sum(losses) / 14 if losses else 0.001
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
    else:
        rsi = 50

    # EMA slope
    if len(closes_1h) >= 10:
        ema_slope = (sum(closes_1h[-5:]) / 5 - sum(closes_1h[-10:-5]) / 5) / (sum(closes_1h[-10:-5]) / 5) * 100
    else:
        ema_slope = 0
    is_ranging = abs(ema_slope) < 0.02

    # Zone tier (approximate from touch count)
    zone_tier = 2  # default

    # Counter-trend
    is_ct = False  # can't determine without full EMA50, approximate
    if len(closes_1h) >= 50:
        ema50 = sum(closes_1h[-50:]) / 50 if len(closes_1h) >= 50 else mean
        if direction == "long" and entry > ema50:
            is_ct = True
        elif direction == "short" and entry < ema50:
            is_ct = True

    return {
        "sym": sym, "dir": direction, "pnl": pnl, "won": pnl > 0,
        "zone_tier": zone_tier, "adr_consumed": adr_consumed,
        "otr": otr, "rr_tp1": rr_tp1, "rr_tp2": rr_tp2,
        "wick_ratio": wick_ratio, "directional_count": directional_count,
        "natural_stop_pips": natural_stop_pips,
        "z_score": z_score, "bb_pos": bb_pos, "rsi": rsi,
        "box_position": box_position, "wall_proximity_pct": wall_proximity_pct,
        "at_correct_wall": at_correct_wall,
        "is_ranging": is_ranging, "is_ct": is_ct, "ema_slope": ema_slope,
        "spread_pips": spread_pips, "box_pips": box_pips,
    }


def score_old(d):
    """Current V1/V2 scoring system."""
    pts = 0
    breakdown = {}

    # Layer 2: Base
    tier_base = {1: 30, 2: 20, 3: 12}.get(d["zone_tier"], 6)
    pts += tier_base; breakdown["zone"] = tier_base

    atr_pct = d["adr_consumed"]
    if 0.35 <= atr_pct <= 0.75: atr_pts = 20
    elif 0.20 <= atr_pct < 0.35 or 0.75 < atr_pct <= 0.90: atr_pts = 12
    elif atr_pct > 0.90: atr_pts = 4
    else: atr_pts = 6
    pts += atr_pts; breakdown["atr"] = atr_pts

    otr = d["rr_tp2"]  # using RR as OTR proxy
    if otr >= 2.0: otr_pts = 15
    elif otr >= 1.5: otr_pts = 10
    elif otr >= 1.2: otr_pts = 5
    else: otr_pts = 0
    pts += otr_pts; breakdown["otr"] = otr_pts

    rr = d["rr_tp1"]
    if rr >= 2.0: rr_pts = 15
    elif rr >= 1.5: rr_pts = 10
    elif rr >= 1.0: rr_pts = 5
    else: rr_pts = 0
    pts += rr_pts; breakdown["rr"] = rr_pts

    # Pattern (approximate — assume JW for all)
    pts += 15; breakdown["pattern"] = 15

    # Layer 3
    abs_z = abs(d["z_score"])
    if abs_z >= 2.0: z_pts = 10
    elif abs_z >= 1.5: z_pts = 6
    elif abs_z >= 1.0: z_pts = 3
    else: z_pts = 0
    pts += z_pts; breakdown["z_edge"] = z_pts

    bb_extreme = d["bb_pos"] if d["dir"] == "short" else (1.0 - d["bb_pos"])
    if bb_extreme >= 0.85: bb_pts = 8
    elif bb_extreme >= 0.70: bb_pts = 4
    else: bb_pts = 0
    pts += bb_pts; breakdown["bb_edge"] = bb_pts

    if d["is_ranging"]:
        pts -= 20; breakdown["ranging"] = -20

    # z-align
    if (d["dir"] == "long" and d["z_score"] < -0.5) or (d["dir"] == "short" and d["z_score"] > 0.5):
        pts += 5; breakdown["z_align"] = 5

    return pts, breakdown


def score_new(d):
    """Recipe-calibrated scoring — reduce dead weight, amplify real signals."""
    pts = 0
    breakdown = {}

    # Layer 2: Base (reduced dead weight)
    tier_base = {1: 25, 2: 15, 3: 8}.get(d["zone_tier"], 4)
    pts += tier_base; breakdown["zone"] = tier_base

    # Wall proximity (NEW — #1 differentiator)
    wp = d["wall_proximity_pct"]
    if wp <= 0.20:  # within 20% of correct wall
        wp_pts = 15
    elif wp <= 0.35:
        wp_pts = 8
    elif 0.40 <= wp <= 0.60:  # middle
        wp_pts = -5
    else:
        wp_pts = -10  # at wrong wall
    pts += wp_pts; breakdown["wall_prox"] = wp_pts

    # ATR consumed (halved)
    atr_pct = d["adr_consumed"]
    if 0.35 <= atr_pct <= 0.75: atr_pts = 8
    elif 0.20 <= atr_pct < 0.35 or 0.75 < atr_pct <= 0.90: atr_pts = 4
    else: atr_pts = 0
    pts += atr_pts; breakdown["atr"] = atr_pts

    # RR (sharply reduced — doesn't differentiate)
    rr = d["rr_tp1"]
    if rr >= 2.0: rr_pts = 5
    elif rr >= 1.0: rr_pts = 3
    else: rr_pts = 0
    pts += rr_pts; breakdown["rr"] = rr_pts

    # OTR: REMOVED (0% signal)

    # Pattern
    pts += 15; breakdown["pattern"] = 15

    # Layer 3: Amplified real signals
    abs_z = abs(d["z_score"])
    if abs_z >= 2.0: z_pts = 10
    elif abs_z >= 1.5: z_pts = 6
    elif abs_z >= 1.0: z_pts = 3
    else: z_pts = 0
    pts += z_pts; breakdown["z_edge"] = z_pts

    # BB edge (reduced)
    bb_extreme = d["bb_pos"] if d["dir"] == "short" else (1.0 - d["bb_pos"])
    if bb_extreme >= 0.85: bb_pts = 4
    elif bb_extreme >= 0.70: bb_pts = 2
    else: bb_pts = 0
    pts += bb_pts; breakdown["bb_edge"] = bb_pts

    # BB middle penalty (STRONGER)
    if 0.40 <= d["bb_pos"] <= 0.60:
        pts -= 20; breakdown["bb_middle"] = -20

    # Directional conviction (STRONGER — recipe: #2 differentiator)
    dc = d["directional_count"]
    if dc >= 4:
        conv_pts = 15
    elif dc >= 3:
        conv_pts = 8
    elif dc >= 2:
        conv_pts = 3
    elif dc <= 1:
        conv_pts = -15
    else:
        conv_pts = 0
    pts += conv_pts; breakdown["conviction"] = conv_pts

    # RSI conviction
    rsi = d["rsi"]
    if 45 <= rsi <= 55:
        pts -= 15; breakdown["rsi_neutral"] = -15
    elif rsi < 30 or rsi > 70:
        pts += 5; breakdown["rsi_extreme"] = 5

    # Natural stop tightness (NEW — recipe: tighter stops win)
    nsp = d["natural_stop_pips"]
    if nsp <= 10:
        pts += 5; breakdown["tight_stop"] = 5
    elif nsp >= 30:
        pts -= 5; breakdown["wide_stop"] = -5

    if d["is_ranging"]:
        pts -= 20; breakdown["ranging"] = -20

    if (d["dir"] == "long" and d["z_score"] < -0.5) or (d["dir"] == "short" and d["z_score"] > 0.5):
        pts += 5; breakdown["z_align"] = 5

    return pts, breakdown


def score_aggressive(d):
    """Maximum recipe alignment — heaviest penalties."""
    pts, breakdown = score_new(d)

    # Even stronger conviction (double weight)
    dc = d["directional_count"]
    if dc >= 4:
        pts += 5; breakdown["conv_bonus2"] = 5  # total +20 for 4+ candles
    elif dc <= 1:
        pts -= 5; breakdown["conv_penalty2"] = -5  # total -20 for 0-1 candles

    # Box size penalty (recipe: >100p = 44% WR)
    if d["box_pips"] > 150:
        pts -= 10; breakdown["wide_box"] = -10
    elif d["box_pips"] > 100:
        pts -= 5; breakdown["wide_box"] = -5

    return pts, breakdown


def main():
    r = requests.get(f"{BASE}/v3/accounts/{ACCT}/trades", headers=HEADERS,
                     params={"state": "CLOSED", "count": "50"})
    trades = r.json().get("trades", [])
    print(f"Fetching raw data for {len(trades)} trades...")

    results = []
    for i, t in enumerate(trades):
        sym = t.get("instrument", "")
        print(f"  [{i+1}/{len(trades)}] {sym}...", end="", flush=True)
        try:
            a = analyze_trade(t)
            if a:
                results.append(a)
                print(f" {'W' if a['won'] else 'L'} ${a['pnl']:+,.0f}")
            else:
                print(" skip")
        except Exception as e:
            print(f" err: {e}")

    winners = [r for r in results if r["won"]]
    losers = [r for r in results if not r["won"]]
    print(f"\nAnalyzed {len(results)} trades: {len(winners)}W / {len(losers)}L")
    print(f"Total PnL: ${sum(r['pnl'] for r in results):+,.2f}")

    # Score all trades with all formulas
    for r in results:
        r["score_old"], r["bd_old"] = score_old(r)
        r["score_new"], r["bd_new"] = score_new(r)
        r["score_agg"], r["bd_agg"] = score_aggressive(r)

    # Display
    print()
    print("=" * 130)
    print("TRADE-BY-TRADE SCORING COMPARISON")
    print("=" * 130)
    print(f"{'Pair':<10} {'Dir':<5} {'PnL':>9} {'W/L':<3} {'OLD':>5} {'NEW':>5} {'AGG':>5} | {'OLD breakdown':<40} | {'NEW breakdown'}")
    print("-" * 130)

    for r in results:
        old_top = sorted(r["bd_old"].items(), key=lambda x: abs(x[1]), reverse=True)[:4]
        new_top = sorted(r["bd_new"].items(), key=lambda x: abs(x[1]), reverse=True)[:4]
        old_str = " ".join(f"{k}={v:+d}" for k, v in old_top)
        new_str = " ".join(f"{k}={v:+d}" for k, v in new_top)
        wl = "W" if r["won"] else "L"
        print(f"{r['sym']:<10} {r['dir']:<5} {r['pnl']:>+9,.0f} {wl:<3} {r['score_old']:>5} {r['score_new']:>5} {r['score_agg']:>5} | {old_str:<40} | {new_str}")

    # Score distribution analysis
    print()
    print("=" * 130)
    print("SCORE DISTRIBUTION: WINNERS vs LOSERS")
    print("=" * 130)

    for name, key in [("OLD", "score_old"), ("NEW", "score_new"), ("AGGRESSIVE", "score_agg")]:
        w_scores = sorted([r[key] for r in winners])
        l_scores = sorted([r[key] for r in losers])
        w_avg = sum(w_scores) / len(w_scores) if w_scores else 0
        l_avg = sum(l_scores) / len(l_scores) if l_scores else 0
        separation = w_avg - l_avg

        print(f"\n  {name} Formula:")
        print(f"    Winners: avg={w_avg:.1f}  min={min(w_scores):.0f}  max={max(w_scores):.0f}  median={w_scores[len(w_scores)//2]:.0f}")
        print(f"    Losers:  avg={l_avg:.1f}  min={min(l_scores):.0f}  max={max(l_scores):.0f}  median={l_scores[len(l_scores)//2]:.0f}")
        print(f"    SEPARATION: {separation:+.1f} pts (higher = better discrimination)")

    # Threshold simulation
    print()
    print("=" * 130)
    print("THRESHOLD SIMULATION: What min_entry_score maximizes P&L?")
    print("=" * 130)

    for name, key in [("OLD", "score_old"), ("NEW", "score_new"), ("AGGRESSIVE", "score_agg")]:
        print(f"\n  {name}:")
        print(f"  {'Threshold':>10} {'Passed':>7} {'W':>3} {'L':>3} {'WR':>5} {'Net PnL':>12} {'Blocked W$':>11} {'Blocked L$':>11}")
        print(f"  {'-'*70}")

        for threshold in range(0, 80, 5):
            passed = [r for r in results if r[key] >= threshold]
            blocked = [r for r in results if r[key] < threshold]
            pw = [r for r in passed if r["won"]]
            pl = [r for r in passed if not r["won"]]
            bw = [r for r in blocked if r["won"]]
            bl = [r for r in blocked if not r["won"]]

            total_passed = len(pw) + len(pl)
            wr = len(pw) / total_passed * 100 if total_passed > 0 else 0
            net = sum(r["pnl"] for r in passed)
            bw_pnl = sum(r["pnl"] for r in bw)
            bl_pnl = sum(r["pnl"] for r in bl)

            marker = " <--" if net > 0 and total_passed >= 5 else ""
            print(f"  {threshold:>10} {total_passed:>7} {len(pw):>3} {len(pl):>3} {wr:>4.0f}% {net:>+11,.0f} {bw_pnl:>+10,.0f} {bl_pnl:>+10,.0f}{marker}")

    # Component correlation with outcome
    print()
    print("=" * 130)
    print("NEW FORMULA: COMPONENT CONTRIBUTION TO WIN/LOSS")
    print("=" * 130)

    components = ["zone", "wall_prox", "atr", "rr", "pattern", "z_edge", "bb_edge",
                  "bb_middle", "conviction", "rsi_neutral", "rsi_extreme",
                  "tight_stop", "wide_stop", "ranging", "z_align"]

    print(f"  {'Component':<15} {'W avg':>7} {'L avg':>7} {'Delta':>7} {'Signal'}")
    for comp in components:
        w_vals = [r["bd_new"].get(comp, 0) for r in winners]
        l_vals = [r["bd_new"].get(comp, 0) for r in losers]
        w_avg = sum(w_vals) / len(w_vals) if w_vals else 0
        l_avg = sum(l_vals) / len(l_vals) if l_vals else 0
        delta = w_avg - l_avg
        signal = "***" if abs(delta) > 5 else "**" if abs(delta) > 2 else "*" if abs(delta) > 0.5 else ""
        print(f"  {comp:<15} {w_avg:>+7.1f} {l_avg:>+7.1f} {delta:>+7.1f} {signal}")


if __name__ == "__main__":
    main()
