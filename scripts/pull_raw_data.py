#!/usr/bin/env python3
"""
TRANSPARENT RAW DATA PULL — Every API call visible, every calculation shown.

This script:
1. Pulls closed trades from OANDA REST API
2. For EACH trade, pulls the raw candle data that existed at entry time
3. Saves ALL raw candles to JSON files (auditable)
4. Computes every feature from those candles (shows the math)
5. Saves the final feature table as CSV

Every intermediate step is saved. Nothing is hidden.
"""

import os
import sys
import json
import csv
import time
import statistics
import requests
from datetime import datetime
from pathlib import Path

# === CONFIGURATION ===
API_KEY = os.environ.get("OANDA_API_KEY", "")
ACCT = os.environ.get("OANDA_ACCOUNT_ID", "")
ENV = os.environ.get("OANDA_ENVIRONMENT", "live")

if ENV == "live":
    BASE = "https://api-fxtrade.oanda.com"
else:
    BASE = "https://api-fxpractice.oanda.com"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

OUTPUT_DIR = Path("/tmp/scrooge_raw_data")
OUTPUT_DIR.mkdir(exist_ok=True)

RATE_LIMIT_SLEEP = 0.4  # seconds between API calls


def api_call(url, params=None):
    """Make an API call with full logging."""
    time.sleep(RATE_LIMIT_SLEEP)
    full_url = f"{BASE}{url}"
    print(f"    API CALL: GET {full_url}")
    if params:
        print(f"    PARAMS: {json.dumps(params)}")

    try:
        r = requests.get(full_url, headers=HEADERS, params=params, timeout=15)
        print(f"    STATUS: {r.status_code}")

        if r.status_code != 200:
            print(f"    ERROR: {r.text[:200]}")
            return None

        data = r.json()
        return data

    except Exception as e:
        print(f"    EXCEPTION: {e}")
        return None


def pull_trades(count=50):
    """Step 1: Pull closed trades from OANDA."""
    print("=" * 80)
    print(f"STEP 1: PULLING {count} CLOSED TRADES")
    print(f"  Account: {ACCT}")
    print(f"  Server: {BASE}")
    print("=" * 80)

    data = api_call(f"/v3/accounts/{ACCT}/trades",
                    {"state": "CLOSED", "count": str(count)})

    if not data:
        print("FAILED to pull trades")
        return []

    trades = data.get("trades", [])
    print(f"\n  Got {len(trades)} trades")

    # Save raw trade data
    trade_file = OUTPUT_DIR / "01_raw_trades.json"
    with open(trade_file, "w") as f:
        json.dump(trades, f, indent=2)
    print(f"  Saved to: {trade_file}")

    # Show summary
    for i, t in enumerate(trades):
        sym = t.get("instrument", "?")
        units = float(t.get("initialUnits", 0))
        price = t.get("price", "?")
        pnl = float(t.get("realizedPL", 0))
        ot = t.get("openTime", "")[:19]
        ct = t.get("closeTime", "")[:19]
        sl = t.get("stopLossOrder", {}).get("price", "none")
        tp = t.get("takeProfitOrder", {}).get("price", "none")
        direction = "SHORT" if units < 0 else "LONG"
        print(f"  [{i+1}] {sym} {direction} {abs(units):.0f} @ {price} | "
              f"PnL: ${pnl:+,.2f} | {ot} -> {ct} | SL: {sl} TP: {tp}")

    return trades


def pull_candles_for_trade(trade, trade_num):
    """Step 2: For one trade, pull ALL candle data at entry time."""
    sym = trade["instrument"]
    entry_time = trade["openTime"]
    entry_price = float(trade["price"])
    pnl = float(trade["realizedPL"])

    print(f"\n{'='*80}")
    print(f"STEP 2.{trade_num}: PULLING CANDLES FOR {sym} (entry: {entry_time[:19]})")
    print(f"  Entry price: {entry_price}")
    print(f"  P&L: ${pnl:+,.2f}")
    print(f"{'='*80}")

    candle_data = {}

    # Pull Daily candles (15 bars before entry)
    print(f"\n  --- DAILY CANDLES (15 bars) ---")
    data = api_call(f"/v3/instruments/{sym}/candles",
                    {"granularity": "D", "count": "15", "price": "MBA",
                     "to": entry_time})
    if data:
        daily = data.get("candles", [])
        candle_data["daily"] = daily
        print(f"  Got {len(daily)} daily candles")
        for c in daily[-3:]:
            m = c["mid"]
            print(f"    {c['time'][:10]}: O={m['o']} H={m['h']} L={m['l']} C={m['c']}")
    else:
        candle_data["daily"] = []

    # Pull Hourly candles (60 bars before entry)
    print(f"\n  --- HOURLY CANDLES (60 bars) ---")
    data = api_call(f"/v3/instruments/{sym}/candles",
                    {"granularity": "H1", "count": "60", "price": "MBA",
                     "to": entry_time})
    if data:
        hourly = data.get("candles", [])
        candle_data["hourly"] = hourly
        print(f"  Got {len(hourly)} hourly candles")
        print(f"  First: {hourly[0]['time'][:16] if hourly else 'none'}")
        print(f"  Last:  {hourly[-1]['time'][:16] if hourly else 'none'}")
    else:
        candle_data["hourly"] = []

    # Pull 5-Minute candles (80 bars before entry)
    print(f"\n  --- 5-MINUTE CANDLES (80 bars) ---")
    data = api_call(f"/v3/instruments/{sym}/candles",
                    {"granularity": "M5", "count": "80", "price": "MBA",
                     "to": entry_time})
    if data:
        m5 = data.get("candles", [])
        candle_data["m5"] = m5
        print(f"  Got {len(m5)} M5 candles")
        # Show last 5 candles before entry
        print(f"  Last 5 candles before entry:")
        for c in m5[-5:]:
            m = c["mid"]
            t = c["time"][11:16]
            print(f"    {t}: O={m['o']} H={m['h']} L={m['l']} C={m['c']}")
    else:
        candle_data["m5"] = []

    # Save all candle data for this trade
    candle_file = OUTPUT_DIR / f"02_candles_trade_{trade_num}_{sym}.json"
    with open(candle_file, "w") as f:
        json.dump(candle_data, f, indent=2)
    print(f"\n  Raw candles saved to: {candle_file}")

    return candle_data


def compute_features(trade, candle_data, trade_num):
    """Step 3: Compute every feature from raw candles. Show the math."""
    sym = trade["instrument"]
    units = float(trade["initialUnits"])
    entry = float(trade["price"])
    pnl = float(trade["realizedPL"])
    ot = trade["openTime"]
    ct = trade["closeTime"]
    d = "S" if units < 0 else "L"
    pip = 0.01 if "JPY" in sym else 0.0001

    daily = candle_data.get("daily", [])
    hourly = candle_data.get("hourly", [])
    m5 = candle_data.get("m5", [])

    print(f"\n{'='*80}")
    print(f"STEP 3.{trade_num}: COMPUTING FEATURES FOR {sym}")
    print(f"{'='*80}")

    if len(daily) < 3 or len(m5) < 20 or len(hourly) < 20:
        print(f"  SKIP: insufficient data (daily={len(daily)}, m5={len(m5)}, hourly={len(hourly)})")
        return None

    # Duration
    try:
        odt = datetime.fromisoformat(ot[:26].replace("Z", "+00:00"))
        cdt = datetime.fromisoformat(ct[:26].replace("Z", "+00:00"))
        dur = (cdt - odt).total_seconds() / 60
        hour = odt.hour
    except:
        dur = 0; hour = 12

    # === BOX ===
    print(f"\n  --- BOX (prior day high/low) ---")
    entry_date = ot[:10]
    prior_day = None
    for c in reversed(daily):
        if c["time"][:10] < entry_date:
            h, l = float(c["mid"]["h"]), float(c["mid"]["l"])
            if (h - l) / l > 0.0005:
                prior_day = c
                break

    if not prior_day:
        print(f"  SKIP: no valid prior day found")
        return None

    pdh = float(prior_day["mid"]["h"])
    pdl = float(prior_day["mid"]["l"])
    bx = pdh - pdl
    hf = bx / 2
    bxp = bx / pip
    bpos = (entry - pdl) / bx if bx > 0 else 0.5
    wp = (entry - pdl) / bx if d == "L" else (pdh - entry) / bx
    wp = wp if bx > 0 else 1

    print(f"  Prior day: {prior_day['time'][:10]}")
    print(f"  PDH = {pdh}, PDL = {pdl}")
    print(f"  Box range = {bx} ({bxp:.0f} pips)")
    print(f"  Half box = {hf}")
    print(f"  Entry = {entry}, Box position = {bpos:.3f}")
    print(f"  Wall proximity = {wp:.3f}")

    # === ATR ===
    print(f"\n  --- ATR ---")
    atrs = []
    for i in range(1, len(daily)):
        h = float(daily[i]["mid"]["h"])
        l = float(daily[i]["mid"]["l"])
        pc = float(daily[i-1]["mid"]["c"])
        tr = max(h - l, abs(h - pc), abs(l - pc))
        atrs.append(tr)
    atr = sum(atrs) / len(atrs) if atrs else bx
    print(f"  ATR (14-day avg): {atr} ({atr/pip:.0f} pips)")

    # === ADR CONSUMED ===
    tc = daily[-1]["mid"]
    adr = (float(tc["h"]) - float(tc["l"])) / atr if atr > 0 else 0
    print(f"  Today range: {float(tc['h'])} - {float(tc['l'])} = {float(tc['h'])-float(tc['l'])}")
    print(f"  ADR consumed: {adr:.3f}")

    # === BOX AGE ===
    try:
        pdt = datetime.fromisoformat(prior_day["time"][:26].replace("Z", "+00:00"))
        bage = (odt - pdt).total_seconds() / 3600
    except:
        bage = 24
    print(f"  Box age: {bage:.1f} hours")

    # === SPREAD ===
    print(f"\n  --- SPREAD ---")
    la = m5[-1]
    ask = float(la.get("ask", {}).get("c", 0))
    bid = float(la.get("bid", {}).get("c", 0))
    sprd = (ask - bid) if ask > 0 and bid > 0 else pip * 2
    sp = sprd / pip
    otr_pct = 2 * sprd / hf * 100 if hf > 0 else 100
    print(f"  Bid = {bid}, Ask = {ask}")
    print(f"  Spread = {sprd} ({sp:.1f} pips)")
    print(f"  OTR = {otr_pct:.1f}%")

    # === SIGNAL CANDLE ===
    print(f"\n  --- SIGNAL CANDLE ---")
    sig = None; dc = 0; mom = 0
    for i in range(len(m5) - 1, max(len(m5) - 8, -1), -1):
        mm = m5[i]["mid"]
        o, h, l, c = float(mm["o"]), float(mm["h"]), float(mm["l"]), float(mm["c"])
        if sig is None:
            if (d == "L" and c > o) or (d == "S" and c < o):
                body = abs(c - o) or pip * 0.1
                rng = h - l or pip * 0.1
                wk = (min(o, c) - l) if d == "L" else (h - max(o, c))
                sig = {"low": l, "high": h, "wick_r": wk / body, "body_pct": body / rng}
                stype = "JW" if wk / body >= 1.5 and body / rng <= 0.30 else "STD"
                print(f"  Signal candle found at index {i}: O={o} H={h} L={l} C={c}")
                print(f"  Body = {body:.5f}, Wick = {wk:.5f}")
                print(f"  Wick ratio = {wk/body:.2f}, Body% = {body/rng:.2f}")
                print(f"  Type: {stype}")
        else:
            if (d == "L" and c < o) or (d == "S" and c > o):
                dc += 1
            else:
                break

    for i in range(len(m5) - 2, max(len(m5) - 12, -1), -1):
        mm = m5[i]["mid"]
        c, o = float(mm["c"]), float(mm["o"])
        if (d == "L" and c < o) or (d == "S" and c > o):
            mom += 1
        else:
            break

    if sig:
        if d == "L":
            ns = (entry - (sig["low"] - 2 * pip)) / pip
        else:
            ns = ((sig["high"] + 2 * pip) - entry) / pip
        bp = sig["body_pct"]
    else:
        ns = 10; bp = 0.5; stype = "?"

    print(f"  Natural stop = {ns:.1f} pips")
    print(f"  Directional candles = {dc}")
    print(f"  Momentum candles = {mom}")

    # === BB / Z-SCORE ===
    print(f"\n  --- BOLLINGER / Z-SCORE ---")
    c1h = [float(c["mid"]["c"]) for c in hourly[-20:]]
    mn = sum(c1h) / len(c1h)
    sd = statistics.stdev(c1h) if len(c1h) > 1 else 0.0001
    zs = (entry - mn) / sd if sd > 0 else 0
    ub = mn + 2 * sd; lb = mn - 2 * sd; w = ub - lb
    bbp = (entry - lb) / w if w > 0 else 0.5
    print(f"  1H SMA20 = {mn:.5f}, StdDev = {sd:.5f}")
    print(f"  Upper BB = {ub:.5f}, Lower BB = {lb:.5f}")
    print(f"  BB position = {bbp:.3f}")
    print(f"  Z-score = {zs:.3f}")

    # === DOUBLE BB STATE ===
    c5m = [float(c["mid"]["c"]) for c in m5[-25:]]
    s20 = sum(c5m[-20:]) / 20 if len(c5m) >= 20 else entry
    sd20 = statistics.stdev(c5m[-20:]) if len(c5m[-20:]) > 1 else 0.0001
    ua = s20 + 2 * sd20; la_bb = s20 - 2 * sd20
    n_b = min(4, len(c5m)); s4 = sum(c5m[-n_b:]) / n_b
    sd4 = statistics.stdev(c5m[-n_b:]) if n_b >= 2 else 0.0001
    ub_b = s4 + 4 * sd4; lb_b = s4 - 4 * sd4
    cc = c5m[-1]; c1 = c5m[-2] if len(c5m) >= 2 else cc; c2 = c5m[-3] if len(c5m) >= 3 else c1

    if cc > ub_b and ub_b > ua: bbs = "EXT_UP"
    elif cc < lb_b and lb_b < la_bb: bbs = "EXT_DN"
    elif cc <= ua and (c1 > ua or c2 > ua): bbs = "REJ_S"
    elif cc >= la_bb and (c1 < la_bb or c2 < la_bb): bbs = "REJ_L"
    elif cc > ua and c1 > ua and cc >= c1: bbs = "BRK_UP"
    elif cc < la_bb and c1 < la_bb and cc <= c1: bbs = "BRK_DN"
    elif cc > ua: bbs = "STR_UP"
    elif cc < la_bb: bbs = "STR_DN"
    else: bbs = "NORM"

    print(f"\n  --- DOUBLE BB STATE ---")
    print(f"  Band A (20/2): upper={ua:.5f}, lower={la_bb:.5f}")
    print(f"  Band B (4/4):  upper={ub_b:.5f}, lower={lb_b:.5f}")
    print(f"  Current close: {cc:.5f}")
    print(f"  State: {bbs}")

    # === SMA20 DISTANCE ===
    sma20 = sum(c5m[-20:]) / 20 if len(c5m) >= 20 else entry
    sma_d = (entry - sma20) / pip
    print(f"\n  --- SMA20 DISTANCE ---")
    print(f"  5M SMA20 = {sma20:.5f}")
    print(f"  Distance = {sma_d:.2f} pips")

    # === RSI ===
    cr5 = [float(c["mid"]["c"]) for c in m5[-15:]]
    if len(cr5) >= 15:
        ch = [cr5[i] - cr5[i-1] for i in range(1, len(cr5))]
        rc = ch[-14:]
        g = sum(c for c in rc if c > 0) / 14 or 0.0001
        l_rsi = sum(-c for c in rc if c < 0) / 14 or 0.0001
        rsi = round(100 - (100 / (1 + g / l_rsi)), 1)
    else:
        rsi = 50.0
    print(f"\n  --- RSI ---")
    print(f"  RSI(14) on 5M = {rsi}")

    # === EMA ===
    print(f"\n  --- EMA ---")
    ah = [float(c["mid"]["c"]) for c in hourly]

    def calc_ema(closes, period):
        if len(closes) < period: return None
        m = 2 / (period + 1); e = sum(closes[:period]) / period
        for p in closes[period:]: e = (p - e) * m + e
        return e

    e20 = calc_ema(ah, 20)
    e50 = calc_ema(ah, 50)
    e20d = abs(entry - e20) / bx * 100 if e20 and bx > 0 else 50
    e50d = abs(entry - e50) / bx * 100 if e50 and bx > 0 else 50
    is_ct = False
    if e50:
        is_ct = (d == "L" and entry > e50) or (d == "S" and entry < e50)
    print(f"  EMA20 = {e20:.5f}" if e20 else "  EMA20 = N/A")
    print(f"  EMA50 = {e50:.5f}" if e50 else "  EMA50 = N/A")
    print(f"  EMA20 distance = {e20d:.1f}% of box")
    print(f"  EMA50 distance = {e50d:.1f}% of box")
    print(f"  Counter-trend = {is_ct}")

    # === EMA SLOPE ===
    if len(ah) >= 10:
        sl = (sum(ah[-5:]) / 5 - sum(ah[-10:-5]) / 5) / (sum(ah[-10:-5]) / 5) * 100
    else:
        sl = 0
    is_rng = abs(sl) < 0.02
    print(f"  EMA slope = {sl:.4f}%")
    print(f"  Is ranging = {is_rng}")

    # === VOLUME RATIO ===
    if len(m5) >= 20:
        rr = [float(b["mid"]["h"]) - float(b["mid"]["l"]) for b in m5[-5:]]
        ro = [float(b["mid"]["h"]) - float(b["mid"]["l"]) for b in m5[-20:-5]]
        vr = (sum(rr) / 5) / (sum(ro) / 15) if sum(ro) > 0 else 1
    else:
        vr = 1
    print(f"\n  --- VOLUME RATIO ---")
    print(f"  Recent 5-bar avg range: {sum(rr)/5:.5f}" if len(m5) >= 20 else "")
    print(f"  Older 15-bar avg range: {sum(ro)/15:.5f}" if len(m5) >= 20 else "")
    print(f"  Ratio: {vr:.2f}")

    # === ZONE TIER ===
    dalign = any(abs(entry - dl) / dl < 0.002 for dl in [pdh, pdl])
    zt = 1 if dalign else 3
    print(f"\n  --- ZONE TIER ---")
    print(f"  Daily aligned = {dalign}")
    print(f"  Zone tier = {zt}")

    # === TOUCHES ===
    tch_buf = abs(pdh) * 0.001
    tch = sum(1 for h in hourly[-24:]
              if abs(float(h["mid"]["h"]) - pdh) <= tch_buf or
                 abs(float(h["mid"]["l"]) - pdl) <= tch_buf)
    print(f"  PDH/PDL touches (24h) = {tch}")

    # === RESULT ===
    feature_row = {
        "trade_id": trade.get("id", ""),
        "sym": sym, "d": d, "entry": entry,
        "pnl": round(pnl, 2), "won": 1 if pnl > 0 else 0,
        "open_time": ot[:19], "close_time": ct[:19],
        "hour": hour, "bage": round(bage, 1), "dur": round(dur, 1),
        "bxp": round(bxp, 1), "bpos": round(bpos, 3), "wp": round(wp, 3),
        "adr": round(adr, 3), "otr": round(otr_pct, 1), "sp": round(sp, 2),
        "ns": round(ns, 1), "dc": dc, "mom": mom,
        "sma_d": round(sma_d, 2), "bbp": round(bbp, 3), "zs": round(zs, 3),
        "rsi": round(rsi, 1), "bbs": bbs, "stype": stype,
        "e50d": round(e50d, 1), "e20d": round(e20d, 1),
        "sl": round(sl, 4), "is_rng": 1 if is_rng else 0,
        "is_ct": 1 if is_ct else 0, "vr": round(vr, 2),
        "bp": round(bp, 3), "zt": zt, "tch": tch,
    }

    print(f"\n  FEATURE ROW:")
    for k, v in feature_row.items():
        print(f"    {k}: {v}")

    return feature_row


def main():
    print("=" * 80)
    print("SCROOGE V3 — TRANSPARENT RAW DATA EXTRACTION")
    print(f"Server: {BASE}")
    print(f"Account: {ACCT}")
    print(f"Output: {OUTPUT_DIR}")
    print("=" * 80)

    # Step 1: Pull trades
    trades = pull_trades(count=50)
    if not trades:
        print("No trades found. Exiting.")
        return

    # Step 2 + 3: For each trade, pull candles and compute features
    all_features = []
    for i, trade in enumerate(trades):
        sym = trade.get("instrument", "?")
        pnl = float(trade.get("realizedPL", 0))
        print(f"\n\n{'#'*80}")
        print(f"# TRADE {i+1}/{len(trades)}: {sym} ${pnl:+,.2f}")
        print(f"{'#'*80}")

        candle_data = pull_candles_for_trade(trade, i + 1)
        features = compute_features(trade, candle_data, i + 1)

        if features:
            all_features.append(features)

    # Step 4: Save complete feature table
    if all_features:
        csv_path = OUTPUT_DIR / "03_features_complete.csv"
        keys = list(all_features[0].keys())
        with open(csv_path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(all_features)

        jsonl_path = OUTPUT_DIR / "03_features_complete.jsonl"
        with open(jsonl_path, "w") as f:
            for row in all_features:
                f.write(json.dumps(row) + "\n")

        print(f"\n\n{'='*80}")
        print(f"COMPLETE: {len(all_features)} trades extracted")
        print(f"  CSV: {csv_path}")
        print(f"  JSONL: {jsonl_path}")
        print(f"  Raw candle JSON files: {OUTPUT_DIR}/02_candles_trade_*.json")
        print(f"  Raw trade data: {OUTPUT_DIR}/01_raw_trades.json")
        print(f"{'='*80}")


if __name__ == "__main__":
    main()
