#!/usr/bin/env python3
"""
COMPLETE Factor Matrix — every measurable aspect with distribution buckets.
Runs against BOTH V1 live and V2 practice for maximum sample.
Raw OANDA data only.
"""

import os
import requests
import statistics
from datetime import datetime
import time as _t
import json

API_KEY = os.environ["OANDA_API_KEY"]
ACCT = os.environ["OANDA_ACCOUNT_ID"]
BASE = os.environ.get("OANDA_BASE", "https://api-fxtrade.oanda.com")
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}


def cndl(pair, gran, to_time, count=50):
    _t.sleep(0.35)
    p = {"granularity": gran, "count": str(count), "price": "MBA", "to": to_time}
    try:
        r = requests.get(f"{BASE}/v3/instruments/{pair}/candles", headers=HEADERS, params=p, timeout=10)
        return r.json().get("candles", [])
    except:
        return []


def ema_calc(closes, period):
    if len(closes) < period: return None
    m = 2 / (period + 1)
    e = sum(closes[:period]) / period
    for p in closes[period:]: e = (p - e) * m + e
    return e


def rsi_calc(closes, period=14):
    if len(closes) < period + 1: return None
    ch = [closes[i] - closes[i-1] for i in range(1, len(closes))]
    rc = ch[-period:]
    g = sum(c for c in rc if c > 0) / period or 0.0001
    l = sum(-c for c in rc if c < 0) / period or 0.0001
    return round(100 - (100 / (1 + g/l)), 1)


def compute_bb_state(closes_5m):
    """Compute double BB state from 5M closes — Band A (20/2) + Band B (4/4)."""
    if len(closes_5m) < 20:
        return "UNKNOWN", {}

    # Band A: 20-period SMA +/- 2 std on close
    sma20 = sum(closes_5m[-20:]) / 20
    std20 = statistics.stdev(closes_5m[-20:]) if len(closes_5m[-20:]) > 1 else 0.0001
    upper_a = sma20 + 2 * std20
    lower_a = sma20 - 2 * std20

    # Band B: 4-period SMA +/- 4 std on close (using close as proxy for open)
    n_b = min(4, len(closes_5m))
    sma4 = sum(closes_5m[-n_b:]) / n_b
    std4 = statistics.stdev(closes_5m[-n_b:]) if n_b >= 2 else 0.0001
    upper_b = sma4 + 4 * std4
    lower_b = sma4 - 4 * std4

    c = closes_5m[-1]
    c1 = closes_5m[-2] if len(closes_5m) >= 2 else c
    c2 = closes_5m[-3] if len(closes_5m) >= 3 else c1

    meta = {"upper_a": upper_a, "lower_a": lower_a, "upper_b": upper_b,
            "lower_b": lower_b, "sma20": sma20, "close": c}

    # Priority order
    if c > upper_b and upper_b > upper_a:
        return "EXTREME_UP", meta
    if c < lower_b and lower_b < lower_a:
        return "EXTREME_DOWN", meta
    if c <= upper_a and (c1 > upper_a or c2 > upper_a):
        return "REJECTION_SHORT", meta
    if c >= lower_a and (c1 < lower_a or c2 < lower_a):
        return "REJECTION_LONG", meta
    if c > upper_a and c1 > upper_a and c >= c1:
        return "BREAKOUT_UP", meta
    if c < lower_a and c1 < lower_a and c <= c1:
        return "BREAKOUT_DOWN", meta
    if c > upper_a:
        return "STRETCH_UP", meta
    if c < lower_a:
        return "STRETCH_DOWN", meta
    return "NORMAL", meta


def extract(t):
    sym = t["instrument"]
    units = float(t["initialUnits"])
    entry = float(t["price"])
    close_p = float(t["averageClosePrice"])
    pnl = float(t["realizedPL"])
    open_time = t["openTime"]
    close_time = t["closeTime"]
    d = "short" if units < 0 else "long"
    pip = 0.01 if "JPY" in sym else 0.0001
    sl_p = float(t.get("stopLossOrder", {}).get("price", 0))
    tp_p = float(t.get("takeProfitOrder", {}).get("price", 0))

    try:
        ot = datetime.fromisoformat(open_time[:26].replace("Z", "+00:00"))
        ct = datetime.fromisoformat(close_time[:26].replace("Z", "+00:00"))
        dur_min = (ct - ot).total_seconds() / 60
        hour = ot.hour
    except:
        dur_min = 0; hour = 12

    daily = cndl(sym, "D", open_time, 15)
    hourly = cndl(sym, "H1", open_time, 60)
    m5 = cndl(sym, "M5", open_time, 80)

    if len(daily) < 3 or len(m5) < 20 or len(hourly) < 20:
        return None

    # Box
    ed = open_time[:10]
    pd = None
    for c in reversed(daily):
        if c["time"][:10] < ed:
            h, l = float(c["mid"]["h"]), float(c["mid"]["l"])
            if (h - l) / l > 0.0005: pd = c; break
    if not pd: return None

    pdh = float(pd["mid"]["h"]); pdl = float(pd["mid"]["l"])
    bx = pdh - pdl; hf = bx / 2; ctr = pdl + hf
    bx_p = bx / pip
    bx_pos = (entry - pdl) / bx if bx > 0 else 0.5

    if d == "long":
        wall_p = (entry - pdl) / bx if bx > 0 else 1
        at_correct = bx_pos < 0.40
    else:
        wall_p = (pdh - entry) / bx if bx > 0 else 1
        at_correct = bx_pos > 0.60

    # ATR
    atrs = []
    for i in range(1, len(daily)):
        h = float(daily[i]["mid"]["h"]); l = float(daily[i]["mid"]["l"])
        pc = float(daily[i-1]["mid"]["c"])
        atrs.append(max(h-l, abs(h-pc), abs(l-pc)))
    atr = sum(atrs)/len(atrs) if atrs else bx
    atr_p = atr / pip
    atr_bx = atr / bx if bx > 0 else 1

    # ADR consumed
    tc = daily[-1]["mid"]
    adr = (float(tc["h"]) - float(tc["l"])) / atr if atr > 0 else 0

    # Box age (hours since prior day close)
    try:
        pd_time = datetime.fromisoformat(pd["time"][:26].replace("Z", "+00:00"))
        box_age_hrs = (ot - pd_time).total_seconds() / 3600
    except:
        box_age_hrs = 24

    # Spread
    la = m5[-1]
    ask = float(la.get("ask", {}).get("c", 0))
    bid = float(la.get("bid", {}).get("c", 0))
    sprd = (ask - bid) if ask > 0 and bid > 0 else pip * 2
    sprd_p = sprd / pip
    sprd_hf = sprd / hf * 100 if hf > 0 else 100
    otr = 2 * sprd / hf * 100 if hf > 0 else 100

    # Signal candle
    sig = None; dir_ct = 0; mom_ct = 0
    for i in range(len(m5)-1, max(len(m5)-8, -1), -1):
        mm = m5[i]["mid"]
        o, h, l, c = float(mm["o"]), float(mm["h"]), float(mm["l"]), float(mm["c"])
        if sig is None:
            if (d == "long" and c > o) or (d == "short" and c < o):
                body = abs(c-o) or pip*0.1
                rng = h-l or pip*0.1
                lw = min(o,c) - l; uw = h - max(o,c)
                wk = lw if d == "long" else uw
                sig = {"low": l, "high": h, "wick": wk, "body": body,
                       "wick_ratio": wk/body, "body_pct": body/rng, "range": rng}
        else:
            if (d == "long" and c < o) or (d == "short" and c > o):
                dir_ct += 1
            else: break

    # Momentum (consecutive same-dir before signal)
    for i in range(len(m5)-2, max(len(m5)-12, -1), -1):
        mm = m5[i]["mid"]
        c, o = float(mm["c"]), float(mm["o"])
        if (d == "long" and c < o) or (d == "short" and c > o):
            mom_ct += 1
        else: break

    if sig:
        if d == "long": ns = (entry - (sig["low"] - 2*pip)) / pip
        else: ns = ((sig["high"] + 2*pip) - entry) / pip
        wr = sig["wick_ratio"]; bp = sig["body_pct"]; cr = sig["range"]/pip

        # Classify signal type from candle
        if wr >= 1.5 and bp <= 0.30:
            sig_type = "wick_rejection"
        elif sig.get("range", 0) > 0:
            # Check for engulfing
            if len(m5) >= 2:
                prev = m5[-2]["mid"]
                ph, pl = float(prev["h"]), float(prev["l"])
                if sig["high"] > ph and sig["low"] < pl:
                    sig_type = "engulfing"
                else:
                    sig_type = "standard"
            else:
                sig_type = "standard"
        else:
            sig_type = "standard"
    else:
        ns = 10; wr = 0; bp = 0.5; cr = 0; sig_type = "none"

    sprd_sl = sprd_p / ns * 100 if ns > 0 else 999

    # BB + z-score (1H)
    cl1h = [float(c["mid"]["c"]) for c in hourly[-20:]]
    mn = sum(cl1h)/len(cl1h); sd = statistics.stdev(cl1h) if len(cl1h) > 1 else 0.0001
    zs = (entry - mn) / sd if sd > 0 else 0
    ub = mn + 2*sd; lb = mn - 2*sd; w = ub - lb
    bbp = (entry - lb) / w if w > 0 else 0.5

    # Double BB state (5M)
    cl5m = [float(c["mid"]["c"]) for c in m5[-25:]]
    bb_state, bb_meta = compute_bb_state(cl5m)

    # RSI
    cl5m_r = [float(c["mid"]["c"]) for c in m5[-15:]]
    rsi_v = rsi_calc(cl5m_r) or 50

    # EMAs
    all1h = [float(c["mid"]["c"]) for c in hourly]
    e20 = ema_calc(all1h, 20); e50 = ema_calc(all1h, 50)
    e20d = abs(entry - e20) / bx * 100 if e20 and bx > 0 else 0
    e50d = abs(entry - e50) / bx * 100 if e50 and bx > 0 else 0

    # CT
    is_ct = False
    if e50:
        is_ct = (d == "long" and entry > e50) or (d == "short" and entry < e50)

    # Ranging
    if len(all1h) >= 10:
        sl = (sum(all1h[-5:])/5 - sum(all1h[-10:-5])/5) / (sum(all1h[-10:-5])/5) * 100
    else: sl = 0
    is_rng = abs(sl) < 0.02

    # Volume
    if len(m5) >= 20:
        rr = [float(b["mid"]["h"])-float(b["mid"]["l"]) for b in m5[-5:]]
        ro = [float(b["mid"]["h"])-float(b["mid"]["l"]) for b in m5[-20:-5]]
        vr = (sum(rr)/5) / (sum(ro)/15) if sum(ro) > 0 else 1
    else: vr = 1

    # Touches
    tb = abs(pdh) * 0.001
    tch = sum(1 for h in hourly[-24:] if abs(float(h["mid"]["h"])-pdh) <= tb or abs(float(h["mid"]["l"])-pdl) <= tb)

    # Gap detection
    today = daily[-1]["mid"]
    today_open = float(today["o"])
    gap_up = today_open > pdh * 1.005
    gap_down = today_open < pdl * 0.995
    gap = "UP" if gap_up else "DOWN" if gap_down else "NONE"

    # Structure (is price inside box?)
    inside_box = pdl <= entry <= pdh
    above_box = entry > pdh
    below_box = entry < pdl

    # Prior day character
    po = float(pd["mid"]["o"]); pc = float(pd["mid"]["c"])
    prior_bull = pc > po

    # Distance from SMA20 (5M)
    sma20_5m = bb_meta.get("sma20", entry)
    dist_sma20_pips = (entry - sma20_5m) / pip

    return {
        "sym": sym, "dir": d, "pnl": pnl, "won": pnl > 0,
        # Box
        "box_pips": bx_p, "box_pos": bx_pos, "wall_prox": wall_p,
        "at_correct": at_correct, "box_age_hrs": box_age_hrs,
        # ATR
        "atr_pips": atr_p, "atr_box_ratio": atr_bx, "adr_consumed": adr,
        # Spread
        "spread_pips": sprd_p, "spread_pct_half": sprd_hf, "otr": otr,
        "spread_sl_pct": sprd_sl,
        # Signal
        "nat_stop": ns, "wick_ratio": wr, "body_pct": bp,
        "candle_range": cr, "dir_count": dir_ct, "mom_count": mom_ct,
        "sig_type": sig_type,
        # BB / z / RSI
        "bb_pos": bbp, "z_score": zs, "rsi": rsi_v,
        "bb_state": bb_state, "dist_sma20": dist_sma20_pips,
        # EMA
        "ema20_dist": e20d, "ema50_dist": e50d, "ema_slope": sl,
        "is_ranging": is_rng, "is_ct": is_ct,
        # Volume
        "vol_ratio": vr,
        # Structure
        "touches": tch, "gap": gap, "inside_box": inside_box,
        "prior_bull": prior_bull,
        # Timing
        "dur_min": dur_min, "hour": hour,
    }


def show_dist(results, key, label, buckets):
    winners = [r for r in results if r["won"]]
    losers = [r for r in results if not r["won"]]
    print(f"\n  {label}:")
    for lo, hi, bl in buckets:
        w = [r for r in winners if r.get(key) is not None and lo <= r[key] < hi]
        l = [r for r in losers if r.get(key) is not None and lo <= r[key] < hi]
        tot = len(w) + len(l)
        if tot == 0: continue
        wr = len(w) / tot * 100
        wp = sum(r["pnl"] for r in w)
        lp = sum(r["pnl"] for r in l)
        net = wp + lp
        bar = "#" * len(w) + "." * len(l)
        print(f"    {bl:<14} {len(w):>2}W/{len(l):<2}L WR={wr:>4.0f}% Net=${net:>+9,.0f} {bar}")


def show_cat(results, key, label):
    winners = [r for r in results if r["won"]]
    losers = [r for r in results if not r["won"]]
    cats = sorted(set(r[key] for r in results if r.get(key) is not None))
    print(f"\n  {label}:")
    for cat in cats:
        w = [r for r in winners if r[key] == cat]
        l = [r for r in losers if r[key] == cat]
        tot = len(w) + len(l)
        if tot == 0: continue
        wr = len(w) / tot * 100
        net = sum(r["pnl"] for r in w) + sum(r["pnl"] for r in l)
        bar = "#" * len(w) + "." * len(l)
        print(f"    {str(cat):<18} {len(w):>2}W/{len(l):<2}L WR={wr:>4.0f}% Net=${net:>+9,.0f} {bar}")


def main():
    r = requests.get(f"{BASE}/v3/accounts/{ACCT}/trades", headers=HEADERS,
                     params={"state": "CLOSED", "count": "50"})
    trades = r.json().get("trades", [])
    print(f"Pulling raw data for {len(trades)} trades from {BASE}...")

    results = []
    for i, t in enumerate(trades):
        sym = t.get("instrument", "")
        pnl = float(t.get("realizedPL", 0))
        print(f"  [{i+1}/{len(trades)}] {sym} ${pnl:+,.0f}...", end="", flush=True)
        try:
            a = extract(t)
            if a:
                results.append(a)
                print(f" {a['bb_state']}")
            else:
                print(" skip")
        except Exception as e:
            print(f" err: {e}")

    winners = [r for r in results if r["won"]]
    losers = [r for r in results if not r["won"]]
    print(f"\nTotal: {len(results)} ({len(winners)}W / {len(losers)}L)")
    print(f"Net: ${sum(r['pnl'] for r in results):+,.2f}")

    # === COMPLETE DISTRIBUTION ANALYSIS ===
    print()
    print("=" * 90)
    print("COMPLETE FACTOR DISTRIBUTIONS")
    print("=" * 90)

    # 1. PDH/PDL Touches
    show_dist(results, "touches", "PDH/PDL TOUCHES (24h hourly)",
              [(0,3,"0-2"), (3,6,"3-5"), (6,10,"6-9"), (10,15,"10-14"), (15,999,"15+")])

    # 2. OTR
    show_dist(results, "otr", "OTR (round-trip spread / half box %)",
              [(0,8,"<8%"), (8,12,"8-12%"), (12,18,"12-18%"), (18,25,"18-25%"), (25,999,"25%+")])

    # 3. ATR
    show_dist(results, "atr_pips", "ATR (pips)",
              [(0,50,"<50p"), (50,80,"50-80p"), (80,120,"80-120p"), (120,200,"120-200p"), (200,9999,"200p+")])

    # 4. ATR/Box ratio
    show_dist(results, "atr_box_ratio", "ATR / BOX RATIO",
              [(0,0.7,"<0.7"), (0.7,0.9,"0.7-0.9"), (0.9,1.1,"0.9-1.1"), (1.1,1.5,"1.1-1.5"), (1.5,99,"1.5+")])

    # 5. Box age
    show_dist(results, "box_age_hrs", "BOX AGE (hours since prior day)",
              [(0,12,"<12h"), (12,24,"12-24h"), (24,36,"24-36h"), (36,48,"36-48h"), (48,999,"48h+")])

    # 6. Spread
    show_dist(results, "spread_pips", "SPREAD (raw pips)",
              [(0,1.5,"<1.5p"), (1.5,3,"1.5-3p"), (3,5,"3-5p"), (5,10,"5-10p"), (10,999,"10p+")])

    # 7. Spread % of half
    show_dist(results, "spread_pct_half", "SPREAD % OF HALF BOX",
              [(0,5,"<5%"), (5,8,"5-8%"), (8,12,"8-12%"), (12,20,"12-20%"), (20,999,"20%+")])

    # 8. Spread/SL ratio
    show_dist(results, "spread_sl_pct", "SPREAD / NATURAL SL %",
              [(0,20,"<20%"), (20,40,"20-40%"), (40,60,"40-60%"), (60,100,"60-100%"), (100,9999,"100%+")])

    # 9. Signal type
    show_cat(results, "sig_type", "SIGNAL TYPE (wick_rejection / engulfing / standard)")

    # 10. Wick ratio
    show_dist(results, "wick_ratio", "WICK RATIO (wick / body)",
              [(0,0.3,"<0.3"), (0.3,0.7,"0.3-0.7"), (0.7,1.2,"0.7-1.2"), (1.2,2.0,"1.2-2.0"), (2.0,99,"2.0+")])

    # 11. Directional count (sucker move)
    show_dist(results, "dir_count", "DIRECTIONAL CANDLES (sucker move strength)",
              [(0,1,"0"), (1,2,"1"), (2,3,"2"), (3,4,"3"), (4,99,"4+")])

    # 12. Momentum candles
    show_dist(results, "mom_count", "MOMENTUM CANDLES (consecutive before signal)",
              [(0,1,"0"), (1,2,"1"), (2,3,"2"), (3,4,"3"), (4,99,"4+")])

    # 13. Z-score
    show_dist(results, "z_score", "Z-SCORE (1H)",
              [(-99,-1.5,"<-1.5"), (-1.5,-0.5,"-1.5 to -0.5"), (-0.5,0.5,"-0.5 to 0.5"),
               (0.5,1.5,"0.5 to 1.5"), (1.5,99,">1.5")])

    # 14. ADR consumed
    show_dist(results, "adr_consumed", "ADR CONSUMED",
              [(0,0.4,"<40%"), (0.4,0.6,"40-60%"), (0.6,0.8,"60-80%"),
               (0.8,1.0,"80-100%"), (1.0,99,"100%+")])

    # 15. BB position
    show_dist(results, "bb_pos", "BB POSITION (1H, 0=lower band, 1=upper)",
              [(0,0.15,"<0.15"), (0.15,0.35,"0.15-0.35"), (0.35,0.50,"0.35-0.50"),
               (0.50,0.65,"0.50-0.65"), (0.65,0.85,"0.65-0.85"), (0.85,1.5,"0.85+")])

    # 16. Double BB state
    show_cat(results, "bb_state", "DOUBLE BB STATE (5M)")

    # 17. RSI
    show_dist(results, "rsi", "RSI (14-period, 5M)",
              [(0,25,"<25"), (25,40,"25-40"), (40,50,"40-50"), (50,60,"50-60"),
               (60,75,"60-75"), (75,100,"75+")])

    # 18. Gap
    show_cat(results, "gap", "GAP DETECTION (today's open vs prior box)")

    # 19. Inside box
    show_cat(results, "inside_box", "INSIDE BOX (entry between PDL-PDH)")

    # 20. Counter-trend
    show_cat(results, "is_ct", "COUNTER-TREND (entry against EMA50)")

    # 21. Ranging
    show_cat(results, "is_ranging", "RANGING (EMA slope < 0.02%)")

    # 22. Box size
    show_dist(results, "box_pips", "BOX SIZE (pips)",
              [(0,40,"<40p"), (40,70,"40-70p"), (70,100,"70-100p"), (100,200,"100-200p"), (200,9999,"200p+")])

    # 23. Wall proximity
    show_dist(results, "wall_prox", "WALL PROXIMITY (0=at wall, 1=far)",
              [(0,0.15,"<0.15"), (0.15,0.30,"0.15-0.30"), (0.30,0.50,"0.30-0.50"),
               (0.50,0.70,"0.50-0.70"), (0.70,1.5,"0.70+")])

    # 24. Natural stop
    show_dist(results, "nat_stop", "NATURAL STOP (pips)",
              [(-99,1,"<=0 INV"), (1,4,"1-3p"), (4,7,"4-6p"), (7,12,"7-11p"), (12,999,"12p+")])

    # 25. Body %
    show_dist(results, "body_pct", "BODY % OF CANDLE RANGE",
              [(0,0.25,"<25%"), (0.25,0.40,"25-40%"), (0.40,0.55,"40-55%"),
               (0.55,0.70,"55-70%"), (0.70,1.01,"70%+")])

    # 26. Duration
    show_dist(results, "dur_min", "DURATION (minutes)",
              [(0,15,"<15m"), (15,60,"15-60m"), (60,180,"1-3h"), (180,360,"3-6h"), (360,9999,"6h+")])

    # 27. Hour of entry
    show_dist(results, "hour", "ENTRY HOUR (UTC)",
              [(0,4,"0-3"), (4,8,"4-7"), (8,12,"8-11"), (12,16,"12-15"), (16,20,"16-19"), (20,24,"20-23")])

    # 28. EMA slope
    show_dist(results, "ema_slope", "EMA SLOPE (%)",
              [(-99,-0.1,"<-0.1"), (-0.1,-0.02,"-0.1 to -0.02"), (-0.02,0.02,"RANGING"),
               (0.02,0.1,"0.02 to 0.1"), (0.1,99,">0.1")])

    # 29. Volume ratio
    show_dist(results, "vol_ratio", "VOLUME RATIO (recent / older ranges)",
              [(0,0.7,"<0.7"), (0.7,0.9,"0.7-0.9"), (0.9,1.1,"0.9-1.1"),
               (1.1,1.5,"1.1-1.5"), (1.5,99,"1.5+")])

    # 30. Prior day bullish
    show_cat(results, "prior_bull", "PRIOR DAY BULLISH")

    # 31. At correct wall
    show_cat(results, "at_correct", "AT CORRECT WALL")

    # 32. EMA20 distance
    show_dist(results, "ema20_dist", "EMA20 DISTANCE (% of box)",
              [(0,15,"<15%"), (15,30,"15-30%"), (30,50,"30-50%"), (50,80,"50-80%"), (80,999,"80%+")])

    # 33. EMA50 distance
    show_dist(results, "ema50_dist", "EMA50 DISTANCE (% of box)",
              [(0,20,"<20%"), (20,40,"20-40%"), (40,60,"40-60%"), (60,100,"60-100%"), (100,999,"100%+")])

    # 34. SMA20 distance (pips)
    show_dist(results, "dist_sma20", "DISTANCE FROM SMA20 (pips, signed)",
              [(-999,-20,"<-20p"), (-20,-5,"-20 to -5"), (-5,5,"-5 to 5"),
               (5,20,"5 to 20"), (20,999,">20p")])

    # === AVERAGES TABLE ===
    print()
    print("=" * 90)
    print("FACTOR AVERAGES (sorted by delta)")
    print("=" * 90)

    num_factors = [
        ("ema_slope", "EMA slope"), ("z_score", "Z-score"), ("wick_ratio", "Wick ratio"),
        ("spread_pips", "Spread"), ("atr_pips", "ATR"), ("dir_count", "Dir candles"),
        ("box_pips", "Box size"), ("dur_min", "Duration"), ("nat_stop", "Nat stop"),
        ("spread_sl_pct", "Spread/SL%"), ("spread_pct_half", "Spread%half"),
        ("otr", "OTR"), ("mom_count", "Momentum"), ("hour", "Hour UTC"),
        ("vol_ratio", "Vol ratio"), ("bb_pos", "BB pos"), ("body_pct", "Body%"),
        ("box_pos", "Box pos"), ("rsi", "RSI"), ("ema20_dist", "EMA20 dist"),
        ("ema50_dist", "EMA50 dist"), ("adr_consumed", "ADR"), ("atr_box_ratio", "ATR/Box"),
        ("touches", "Touches"), ("wall_prox", "Wall prox"), ("candle_range", "Candle rng"),
        ("box_age_hrs", "Box age"), ("dist_sma20", "SMA20 dist"),
    ]

    scored = []
    for key, label in num_factors:
        wv = [r[key] for r in winners if r.get(key) is not None]
        lv = [r[key] for r in losers if r.get(key) is not None]
        if not wv or not lv: continue
        wa = sum(wv)/len(wv); la = sum(lv)/len(lv)
        delta = (wa - la) / abs(la) * 100 if la != 0 else 0
        scored.append((abs(delta), label, wa, la, delta))

    scored.sort(reverse=True)
    print(f"\n  {'Factor':<20} {'W avg':>10} {'L avg':>10} {'Delta':>8} {'Sig'}")
    print(f"  {'-'*55}")
    for s, l, w, lo, d in scored:
        sig = "***" if s > 30 else "**" if s > 15 else "*" if s > 5 else ""
        print(f"  {l:<20} {w:>10.2f} {lo:>10.2f} {d:>+7.0f}% {sig}")


if __name__ == "__main__":
    main()
