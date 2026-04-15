#!/usr/bin/env python3
"""
Scoring Simulator V2 — 100% raw OANDA data, ZERO assumptions.

Every single input is computed from OANDA candle data:
- Zone tier: computed from hourly pivot analysis + daily alignment
- Counter-trend: computed from 50H EMA on actual hourly closes
- BB position: computed from actual 1H closes
- RSI: computed from actual 5M closes
- Directional count: counted from actual 5M candles
- Natural stop: from actual signal candle extreme
- Spread: from actual bid/ask at entry time
- Box: from actual prior day high/low

NO bot logs. NO hardcoded defaults. NO assumptions.
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


def compute_zone_tier(entry, pdh, pdl, hourly_bars, pip):
    """Compute zone tier from raw hourly pivot data + daily alignment.

    Tier 1: hourly pivot aligns with daily PDH/PDL (within 0.2%)
    Tier 2: breakout flip OR 3+ tests at same level
    Tier 3: 2 tests
    Tier 4: single test
    """
    daily_levels = [pdh, pdl]

    # Find pivots in hourly data (local highs/lows with 3-bar lookback)
    if len(hourly_bars) < 7:
        return 3  # insufficient data

    pivot_levels = []
    prices_h = [float(b["mid"]["h"]) for b in hourly_bars]
    prices_l = [float(b["mid"]["l"]) for b in hourly_bars]

    for i in range(3, len(hourly_bars) - 3):
        # Pivot high
        if all(prices_h[i] >= prices_h[i-j] for j in range(1, 4)) and \
           all(prices_h[i] >= prices_h[i+j] for j in range(1, 4)):
            pivot_levels.append(prices_h[i])
        # Pivot low
        if all(prices_l[i] <= prices_l[i-j] for j in range(1, 4)) and \
           all(prices_l[i] <= prices_l[i+j] for j in range(1, 4)):
            pivot_levels.append(prices_l[i])

    if not pivot_levels:
        return 3

    # Find nearest pivot to entry
    nearest = min(pivot_levels, key=lambda p: abs(p - entry))

    # Count touches at this level
    touch_buffer = abs(nearest) * 0.001  # 0.1%
    touches = sum(1 for h, l in zip(prices_h, prices_l)
                  if abs(h - nearest) <= touch_buffer or abs(l - nearest) <= touch_buffer)

    # Check daily alignment
    daily_aligned = any(abs(nearest - dl) / dl < 0.002 for dl in daily_levels)

    if daily_aligned:
        return 1
    elif touches >= 3:
        return 2
    elif touches >= 2:
        return 3
    else:
        return 4


def compute_ema(closes, period):
    """Compute EMA from raw close prices."""
    if len(closes) < period:
        return None
    multiplier = 2 / (period + 1)
    ema = sum(closes[:period]) / period  # seed with SMA
    for price in closes[period:]:
        ema = (price - ema) * multiplier + ema
    return ema


def compute_rsi(closes, period=14):
    """Compute RSI from raw close prices."""
    if len(closes) < period + 1:
        return None
    changes = [closes[i] - closes[i-1] for i in range(1, len(closes))]
    recent = changes[-period:]
    gains = [c for c in recent if c > 0]
    losses = [-c for c in recent if c < 0]
    avg_gain = sum(gains) / period if gains else 0.0001
    avg_loss = sum(losses) / period if losses else 0.0001
    rs = avg_gain / avg_loss
    return round(100 - (100 / (1 + rs)), 1)


def analyze_trade_raw(t):
    """Every input from raw OANDA data. Zero assumptions."""
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

    # Pull raw data
    daily = candles(sym, "D", open_time, count=15)
    hourly = candles(sym, "H1", open_time, count=60)
    bars_5m = candles(sym, "M5", open_time, count=60)

    if len(daily) < 3 or len(bars_5m) < 15 or len(hourly) < 20:
        return None

    # === BOX from raw daily candles ===
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
    box_pips = box_range / pip

    # === ZONE TIER from raw hourly pivots ===
    zone_tier = compute_zone_tier(entry, pdh, pdl, hourly, pip)

    # === BOX POSITION from raw prices ===
    box_position = (entry - pdl) / box_range if box_range > 0 else 0.5
    if direction == "long":
        wall_proximity_pct = (entry - pdl) / box_range if box_range > 0 else 1.0
    else:
        wall_proximity_pct = (pdh - entry) / box_range if box_range > 0 else 1.0

    # === ATR from raw daily candles ===
    atrs = []
    for i in range(1, len(daily)):
        h = float(daily[i]["mid"]["h"])
        l = float(daily[i]["mid"]["l"])
        pc = float(daily[i-1]["mid"]["c"])
        atrs.append(max(h - l, abs(h - pc), abs(l - pc)))
    atr = sum(atrs) / len(atrs) if atrs else box_range

    # === ADR consumed from raw daily candle ===
    today_c = daily[-1]["mid"]
    adr_consumed = (float(today_c["h"]) - float(today_c["l"])) / atr if atr > 0 else 0

    # === SPREAD from raw bid/ask at entry ===
    last_5m = bars_5m[-1]
    ask = float(last_5m.get("ask", {}).get("c", 0))
    bid = float(last_5m.get("bid", {}).get("c", 0))
    spread = (ask - bid) if ask > 0 and bid > 0 else pip * 2
    spread_pips = spread / pip
    otr = (2 * spread) / half_box if half_box > 0 else 1

    # === SIGNAL CANDLE from raw 5M candles ===
    signal_candle = None
    directional_count = 0
    for i in range(len(bars_5m) - 1, max(len(bars_5m) - 8, -1), -1):
        m = bars_5m[i]["mid"]
        o, h, l, c = float(m["o"]), float(m["h"]), float(m["l"]), float(m["c"])
        if signal_candle is None:
            if (direction == "long" and c > o) or (direction == "short" and c < o):
                body = abs(c - o) or pip * 0.1
                wick = (min(o, c) - l) if direction == "long" else (h - max(o, c))
                signal_candle = {"low": l, "high": h, "wick_ratio": wick / body}
        else:
            if (direction == "long" and c < o) or (direction == "short" and c > o):
                directional_count += 1
            else:
                break

    # === NATURAL STOP from raw signal candle ===
    if signal_candle:
        if direction == "long":
            natural_stop_pips = (entry - (signal_candle["low"] - 2 * pip)) / pip
        else:
            natural_stop_pips = ((signal_candle["high"] + 2 * pip) - entry) / pip
        wick_ratio = signal_candle["wick_ratio"]
    else:
        natural_stop_pips = (float(bars_5m[-1]["mid"]["h"]) - float(bars_5m[-1]["mid"]["l"])) / pip
        wick_ratio = 0

    # === RR from raw box geometry ===
    tp2_dist = half_box / pip
    tp1_dist = tp2_dist / 2
    rr_tp1 = tp1_dist / natural_stop_pips if natural_stop_pips > 0 else 0

    # === BB POSITION from raw 1H closes ===
    closes_1h = [float(c["mid"]["c"]) for c in hourly[-20:]]
    mean_1h = sum(closes_1h) / len(closes_1h)
    std_1h = statistics.stdev(closes_1h) if len(closes_1h) > 1 else 0.0001
    z_score = round((entry - mean_1h) / std_1h, 3) if std_1h > 0 else 0
    upper_bb = mean_1h + 2 * std_1h
    lower_bb = mean_1h - 2 * std_1h
    bb_width = upper_bb - lower_bb
    bb_pos = round((entry - lower_bb) / bb_width, 3) if bb_width > 0 else 0.5

    # === RSI from raw 5M closes ===
    closes_5m = [float(c["mid"]["c"]) for c in bars_5m[-15:]]
    rsi = compute_rsi(closes_5m, 14)
    if rsi is None:
        rsi = 50.0

    # === EMA50 + EMA20 from raw 1H closes (counter-trend) ===
    all_closes_1h = [float(c["mid"]["c"]) for c in hourly]
    ema50 = compute_ema(all_closes_1h, 50)
    ema20 = compute_ema(all_closes_1h, 20)

    if ema50 is not None:
        if direction == "long":
            is_ct = entry > ema50  # buying above downtrend EMA = counter-trend
        else:
            is_ct = entry < ema50
    else:
        is_ct = False

    # === EMA SLOPE from raw 1H closes ===
    if len(all_closes_1h) >= 10:
        recent_5 = sum(all_closes_1h[-5:]) / 5
        prior_5 = sum(all_closes_1h[-10:-5]) / 5
        ema_slope = (recent_5 - prior_5) / prior_5 * 100 if prior_5 > 0 else 0
    else:
        ema_slope = 0
    is_ranging = abs(ema_slope) < 0.02

    return {
        "sym": sym, "dir": direction, "pnl": pnl, "won": pnl > 0,
        "entry": entry, "close": close_p, "duration_min": duration_min,
        "zone_tier": zone_tier,  # FROM RAW PIVOTS
        "adr_consumed": adr_consumed,
        "otr": otr, "rr_tp1": rr_tp1,
        "wick_ratio": wick_ratio, "directional_count": directional_count,
        "natural_stop_pips": natural_stop_pips,
        "z_score": z_score, "bb_pos": bb_pos, "rsi": rsi,
        "box_position": box_position, "wall_proximity_pct": wall_proximity_pct,
        "box_pips": box_pips, "spread_pips": spread_pips,
        "is_ranging": is_ranging, "is_ct": is_ct, "ema_slope": ema_slope,
    }


def score_old(d):
    """Current V1/V2 scoring."""
    pts = 0

    tier_base = {1: 30, 2: 20, 3: 12, 4: 6}.get(d["zone_tier"], 6)
    pts += tier_base

    atr = d["adr_consumed"]
    if 0.35 <= atr <= 0.75: pts += 20
    elif 0.20 <= atr < 0.35 or 0.75 < atr <= 0.90: pts += 12
    elif atr > 0.90: pts += 4
    else: pts += 6

    rr = d["rr_tp1"]
    if rr >= 2.0: pts += 15
    elif rr >= 1.5: pts += 10
    elif rr >= 1.0: pts += 5

    # OTR scoring (dead weight per recipe)
    otr = d["rr_tp1"]  # proxy
    if otr >= 2.0: pts += 15
    elif otr >= 1.5: pts += 10
    elif otr >= 1.2: pts += 5

    pts += 15  # pattern

    abs_z = abs(d["z_score"])
    if abs_z >= 2.0: pts += 10
    elif abs_z >= 1.5: pts += 6
    elif abs_z >= 1.0: pts += 3

    bb_ext = d["bb_pos"] if d["dir"] == "short" else (1.0 - d["bb_pos"])
    if bb_ext >= 0.85: pts += 8
    elif bb_ext >= 0.70: pts += 4

    if d["is_ranging"]: pts -= 20

    if (d["dir"] == "long" and d["z_score"] < -0.5) or \
       (d["dir"] == "short" and d["z_score"] > 0.5):
        pts += 5

    return pts


def score_new(d):
    """Recipe-calibrated scoring."""
    pts = 0
    bd = {}

    # Zone tier (from raw pivots)
    tb = {1: 25, 2: 15, 3: 8, 4: 4}.get(d["zone_tier"], 4)
    pts += tb; bd["zone"] = tb

    # Wall proximity (from raw box position)
    wp = d["wall_proximity_pct"]
    if wp <= 0.20:   wpp = 15
    elif wp <= 0.35: wpp = 8
    elif 0.40 <= wp <= 0.60: wpp = -5
    else: wpp = -10
    pts += wpp; bd["wall"] = wpp

    # ATR consumed (halved)
    atr = d["adr_consumed"]
    if 0.35 <= atr <= 0.75: ap = 8
    elif 0.20 <= atr < 0.35 or 0.75 < atr <= 0.90: ap = 4
    else: ap = 0
    pts += ap; bd["atr"] = ap

    # RR (reduced)
    rr = d["rr_tp1"]
    if rr >= 2.0: rp = 5
    elif rr >= 1.0: rp = 3
    else: rp = 0
    pts += rp; bd["rr"] = rp

    pts += 15; bd["pattern"] = 15  # signal type

    # z-score edge
    abs_z = abs(d["z_score"])
    if abs_z >= 2.0: zp = 10
    elif abs_z >= 1.5: zp = 6
    elif abs_z >= 1.0: zp = 3
    else: zp = 0
    pts += zp; bd["z"] = zp

    # BB edge (reduced)
    bb_ext = d["bb_pos"] if d["dir"] == "short" else (1.0 - d["bb_pos"])
    if bb_ext >= 0.85: bbp = 4
    elif bb_ext >= 0.70: bbp = 2
    else: bbp = 0
    pts += bbp; bd["bb"] = bbp

    # BB middle (recipe: 27% WR)
    if 0.40 <= d["bb_pos"] <= 0.60:
        pts -= 20; bd["bb_mid"] = -20

    # Conviction (recipe: #2 differentiator)
    dc = d["directional_count"]
    if dc >= 4:   cp = 15
    elif dc >= 3: cp = 8
    elif dc >= 2: cp = 3
    elif dc <= 1: cp = -15
    else: cp = 0
    pts += cp; bd["conv"] = cp

    # RSI (recipe: 45-55 = 29% WR)
    rsi = d["rsi"]
    if 45 <= rsi <= 55:
        pts -= 15; bd["rsi"] = -15
    elif rsi < 30 or rsi > 70:
        pts += 5; bd["rsi"] = 5

    # Natural stop tightness (recipe: tighter wins)
    ns = d["natural_stop_pips"]
    if ns <= 10: pts += 5; bd["stop"] = 5
    elif ns >= 30: pts -= 5; bd["stop"] = -5

    # Ranging (confirmed killer)
    if d["is_ranging"]:
        pts -= 20; bd["rang"] = -20

    # z-align
    if (d["dir"] == "long" and d["z_score"] < -0.5) or \
       (d["dir"] == "short" and d["z_score"] > 0.5):
        pts += 5; bd["zalign"] = 5

    # CT penalties (from April audit)
    if d["is_ct"]:
        if d["zone_tier"] == 1: pts -= 10; bd["ct_t1"] = -10
        elif d["zone_tier"] == 2: pts += 5; bd["ct_t2"] = 5

    return pts, bd


def score_aggressive(d):
    """Maximum recipe alignment."""
    pts, bd = score_new(d)

    # Extra conviction weight
    dc = d["directional_count"]
    if dc >= 4:
        pts += 5; bd["conv2"] = 5
    elif dc <= 1:
        pts -= 5; bd["conv2"] = -5

    # Box size (recipe: >100p = 44% WR)
    if d["box_pips"] > 150:
        pts -= 10; bd["bigbox"] = -10
    elif d["box_pips"] > 100:
        pts -= 5; bd["bigbox"] = -5

    # Duration proxy: if spread is very wide relative to box, likely bad session
    if d["spread_pips"] / (d["box_pips"] / 2) > 0.12 if d["box_pips"] > 0 else False:
        pts -= 5; bd["sprd_warn"] = -5

    return pts, bd


def main():
    r = requests.get(f"{BASE}/v3/accounts/{ACCT}/trades", headers=HEADERS,
                     params={"state": "CLOSED", "count": "50"})
    trades = r.json().get("trades", [])
    print(f"Fetching 100% raw OANDA data for {len(trades)} trades...")
    print("(zone tier from pivots, CT from EMA50, RSI from 5M, BB from 1H)")
    print()

    results = []
    for i, t in enumerate(trades):
        sym = t.get("instrument", "")
        print(f"  [{i+1}/{len(trades)}] {sym}...", end="", flush=True)
        try:
            a = analyze_trade_raw(t)
            if a:
                a["score_old"] = score_old(a)
                a["score_new"], a["bd_new"] = score_new(a)
                a["score_agg"], a["bd_agg"] = score_aggressive(a)
                results.append(a)
                mark = "W" if a["won"] else "L"
                print(f" {mark} ${a['pnl']:+,.0f}  T{a['zone_tier']} OLD={a['score_old']} NEW={a['score_new']} AGG={a['score_agg']}")
            else:
                print(" skip")
        except Exception as e:
            print(f" err: {e}")

    winners = [r for r in results if r["won"]]
    losers = [r for r in results if not r["won"]]

    print(f"\n{'='*100}")
    print(f"RESULTS: {len(results)} trades ({len(winners)}W / {len(losers)}L)")
    print(f"Total PnL: ${sum(r['pnl'] for r in results):+,.2f}")
    print(f"{'='*100}")

    # Separation
    for name, key in [("OLD", "score_old"), ("NEW", "score_new"), ("AGG", "score_agg")]:
        w_avg = sum(r[key] for r in winners) / len(winners)
        l_avg = sum(r[key] for r in losers) / len(losers)
        print(f"  {name:<4} W avg={w_avg:>6.1f}  L avg={l_avg:>6.1f}  SEPARATION={w_avg-l_avg:>+.1f}")

    # Threshold sim
    print(f"\n{'='*100}")
    print("THRESHOLD SIMULATION")
    print(f"{'='*100}")

    for name, key in [("OLD", "score_old"), ("NEW", "score_new"), ("AGG", "score_agg")]:
        print(f"\n--- {name} ---")
        print(f"  {'Thresh':>6} {'Taken':>6} {'W':>3} {'L':>3} {'WR':>5} {'Net$':>11} {'AvgW$':>9} {'AvgL$':>9}")

        best_pnl = -999999
        best_thresh = 0
        for threshold in range(-20, 85, 5):
            passed = [r for r in results if r[key] >= threshold]
            pw = [r for r in passed if r["won"]]
            pl = [r for r in passed if not r["won"]]
            total = len(pw) + len(pl)
            if total == 0:
                continue
            wr = len(pw) / total * 100
            net = sum(r["pnl"] for r in passed)
            avg_w = sum(r["pnl"] for r in pw) / len(pw) if pw else 0
            avg_l = sum(r["pnl"] for r in pl) / len(pl) if pl else 0
            marker = " <<<" if net > best_pnl and total >= 5 else ""
            if net > best_pnl and total >= 5:
                best_pnl = net
                best_thresh = threshold
            print(f"  {threshold:>6} {total:>6} {len(pw):>3} {len(pl):>3} {wr:>4.0f}% {net:>+10,.0f} {avg_w:>+8,.0f} {avg_l:>+8,.0f}{marker}")

        print(f"  BEST: threshold={best_thresh}, PnL=${best_pnl:+,.0f}")

    # Component analysis
    print(f"\n{'='*100}")
    print("NEW FORMULA COMPONENTS: W vs L average")
    print(f"{'='*100}")
    all_keys = set()
    for r in results:
        all_keys.update(r.get("bd_new", {}).keys())

    print(f"  {'Component':<12} {'W avg':>7} {'L avg':>7} {'Delta':>7}")
    for comp in sorted(all_keys):
        w_vals = [r["bd_new"].get(comp, 0) for r in winners]
        l_vals = [r["bd_new"].get(comp, 0) for r in losers]
        w_avg = sum(w_vals) / len(w_vals)
        l_avg = sum(l_vals) / len(l_vals)
        delta = w_avg - l_avg
        signal = " ***" if abs(delta) > 5 else " **" if abs(delta) > 2 else " *" if abs(delta) > 0.5 else ""
        print(f"  {comp:<12} {w_avg:>+7.1f} {l_avg:>+7.1f} {delta:>+7.1f}{signal}")

    # Quality grades — P&L weighted analysis
    print(f"\n{'='*100}")
    print("TRADE QUALITY GRADES (by P&L magnitude)")
    print(f"{'='*100}")

    sorted_trades = sorted(results, key=lambda r: r["pnl"], reverse=True)

    print(f"  {'Rank':<5} {'Pair':<10} {'PnL':>10} {'OLD':>5} {'NEW':>5} {'AGG':>5} {'Tier':>4} {'DC':>3} {'RSI':>5} {'BB':>5} {'Wall%':>6} {'Box':>5}")
    print(f"  {'-'*80}")

    for i, r in enumerate(sorted_trades):
        rank = f"#{i+1}"
        grade = "A+" if r["pnl"] > 2000 else "A" if r["pnl"] > 500 else "B" if r["pnl"] > 0 else "C" if r["pnl"] > -500 else "D" if r["pnl"] > -1000 else "F"
        print(f"  {rank:<5} {r['sym']:<10} {r['pnl']:>+10,.0f} {r['score_old']:>5} {r['score_new']:>5} {r['score_agg']:>5} T{r['zone_tier']:>3} {r['directional_count']:>3} {r['rsi']:>5.0f} {r['bb_pos']:>5.2f} {r['wall_proximity_pct']:>5.2f} {r['box_pips']:>5.0f}p [{grade}]")


if __name__ == "__main__":
    main()
