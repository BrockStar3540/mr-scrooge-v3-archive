#!/usr/bin/env python3
"""
10 Formula Variations for Entry/SL/TP Configuration
Pulls live OANDA data and tests each formula against all pairs.
"""

import os
import requests
import json

API_KEY = os.environ["OANDA_API_KEY"]
ACCOUNT = os.environ["OANDA_ACCOUNT_ID"]
BASE = os.environ.get("OANDA_URL", "https://api-fxtrade.oanda.com")
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

PAIRS = [
    "USD_JPY", "EUR_USD", "GBP_USD", "AUD_CAD", "EUR_CAD",
    "CHF_JPY", "GBP_JPY", "AUD_CHF", "EUR_GBP", "NZD_USD",
]

def fetch_pair_data(pair):
    pip = 0.01 if "JPY" in pair else 0.0001

    # Daily bars
    r = requests.get(f"{BASE}/v3/instruments/{pair}/candles", headers=HEADERS,
                     params={"granularity": "D", "count": "5", "price": "MBA"})
    daily = r.json().get("candles", [])

    # 5M bars
    r2 = requests.get(f"{BASE}/v3/instruments/{pair}/candles", headers=HEADERS,
                      params={"granularity": "M5", "count": "100", "price": "MBA"})
    bars = r2.json().get("candles", [])

    # Live spread
    r3 = requests.get(f"{BASE}/v3/accounts/{ACCOUNT}/pricing", headers=HEADERS,
                      params={"instruments": pair})
    pricing = r3.json().get("prices", [{}])[0]
    bid = float(pricing.get("bids", [{"price": "0"}])[0]["price"])
    ask = float(pricing.get("asks", [{"price": "0"}])[0]["price"])
    spread = ask - bid
    mid = (bid + ask) / 2

    # Prior day box (skip tiny bars)
    valid_prior = None
    for i in range(2, min(len(daily), 5)):
        d = daily[-i]
        h, l = float(d["mid"]["h"]), float(d["mid"]["l"])
        if (h - l) / l > 0.0005:
            valid_prior = d
            break
    if not valid_prior:
        return None

    PDH = float(valid_prior["mid"]["h"])
    PDL = float(valid_prior["mid"]["l"])
    box = PDH - PDL
    half = box / 2

    # 5M candle stats
    ranges_5m = []
    wicks = []
    for b in bars[-50:]:
        bm = b["mid"]
        o, h, l, c = float(bm["o"]), float(bm["h"]), float(bm["l"]), float(bm["c"])
        ranges_5m.append(h - l)
        body = abs(c - o) or pip * 0.1
        lower_wick = min(o, c) - l
        upper_wick = h - max(o, c)
        wicks.append(max(lower_wick, upper_wick))

    avg_range = sum(ranges_5m) / len(ranges_5m) if ranges_5m else pip
    avg_wick = sum(wicks) / len(wicks) if wicks else pip

    # ATR
    atrs = []
    for i in range(1, len(daily)):
        h = float(daily[i]["mid"]["h"])
        l = float(daily[i]["mid"]["l"])
        pc = float(daily[i-1]["mid"]["c"])
        tr = max(h - l, abs(h - pc), abs(l - pc))
        atrs.append(tr)
    atr = sum(atrs) / len(atrs) if atrs else box

    return {
        "PDH": PDH, "PDL": PDL, "box": box, "half": half,
        "spread": spread, "mid": mid, "pip": pip, "atr": atr,
        "avg_5m_range": avg_range, "avg_wick": avg_wick,
    }


# Define 10 formulas
FORMULAS = {
    "F01_current": {
        "desc": "CURRENT: SL floor 0.25% price, RR 1.35 vs TP2",
        "sl": lambda d: max(d["avg_wick"], d["mid"] * 0.0025),
        "tp": lambda d: d["half"],
        "rr_min": 1.35,
    },
    "F02_floor15": {
        "desc": "SL floor lowered to 0.15% price",
        "sl": lambda d: max(d["avg_wick"], d["mid"] * 0.0015),
        "tp": lambda d: d["half"],
        "rr_min": 1.35,
    },
    "F03_floor10": {
        "desc": "SL floor lowered to 0.10% price",
        "sl": lambda d: max(d["avg_wick"], d["mid"] * 0.0010),
        "tp": lambda d: d["half"],
        "rr_min": 1.35,
    },
    "F04_no_floor": {
        "desc": "No SL floor, pure candle stop, RR 1.35",
        "sl": lambda d: d["avg_wick"] + d["spread"],
        "tp": lambda d: d["half"],
        "rr_min": 1.35,
    },
    "F05_no_rr": {
        "desc": "No SL floor, NO RR gate, profitability only",
        "sl": lambda d: d["avg_wick"] + d["spread"],
        "tp": lambda d: d["half"],
        "rr_min": 0,
    },
    "F06_box_floor": {
        "desc": "SL floor = 15% of box (scales with structure)",
        "sl": lambda d: max(d["avg_wick"], d["box"] * 0.15),
        "tp": lambda d: d["half"],
        "rr_min": 1.35,
    },
    "F07_atr_floor": {
        "desc": "SL floor = 10% of ATR (scales with volatility)",
        "sl": lambda d: max(d["avg_wick"], d["atr"] * 0.10),
        "tp": lambda d: d["half"],
        "rr_min": 1.35,
    },
    "F08_rr_vs_tp1": {
        "desc": "RR gate vs TP1 (center), threshold 0.80",
        "sl": lambda d: max(d["avg_wick"], d["mid"] * 0.0015),
        "tp": lambda d: d["half"] * 0.5,
        "rr_min": 0.80,
    },
    "F09_hybrid": {
        "desc": "SL=max(candle, 10%box, 2xspread), RR 1.0",
        "sl": lambda d: max(d["avg_wick"], d["box"] * 0.10, d["spread"] * 2),
        "tp": lambda d: d["half"],
        "rr_min": 1.0,
    },
    "F10_viability": {
        "desc": "PROPOSED: candle+spread SL, no RR, harvest viability",
        "sl": lambda d: d["avg_wick"] + d["spread"],
        "tp": lambda d: d["half"] * 0.40,
        "rr_min": 0,
    },
}


def main():
    # Fetch all pair data
    pair_data = {}
    for pair in PAIRS:
        try:
            d = fetch_pair_data(pair)
            if d:
                pair_data[pair] = d
        except Exception as e:
            print(f"Error: {pair}: {e}")

    # Pair details
    print("=" * 100)
    print("PAIR DETAILS (current market)")
    print("=" * 100)
    print(f"{'Pair':<12} {'Box':>6} {'Half':>6} {'Spread':>7} {'AvgWick':>8} {'ATR':>6} {'Sprd%':>6} {'OTR%':>5}")
    for pair, d in pair_data.items():
        p = d["pip"]
        sp = d["spread"] / d["half"] * 100 if d["half"] > 0 else 0
        otr = 2 * d["spread"] / d["half"] * 100 if d["half"] > 0 else 0
        print(f"{pair:<12} {d['box']/p:>5.0f}p {d['half']/p:>5.0f}p {d['spread']/p:>6.1f}p {d['avg_wick']/p:>7.1f}p {d['atr']/p:>5.0f}p {sp:>5.1f}% {otr:>4.1f}%")

    # Formula comparison
    print()
    print("=" * 100)
    print("10 FORMULA VARIATIONS")
    print("=" * 100)

    for fname, f in FORMULAS.items():
        print(f"\n--- {fname}: {f['desc']} ---")
        pass_count = 0
        block_count = 0
        details = []

        for pair, d in pair_data.items():
            p = d["pip"]
            sl = f["sl"](d)
            tp = f["tp"](d)
            rr = tp / sl if sl > 0 else 0

            # Profitability: target must exceed round-trip spread
            net = tp - 2 * d["spread"]
            profitable = net > 0

            # RR check
            rr_ok = rr >= f["rr_min"] if f["rr_min"] > 0 else True

            # Spread check: < 15% of half box
            spread_ok = d["spread"] / d["half"] < 0.15 if d["half"] > 0 else False

            # Stop noise check: SL > 2x spread
            noise_ok = sl > d["spread"] * 2

            viable = profitable and rr_ok and spread_ok and noise_ok

            if viable:
                pass_count += 1
                status = "PASS"
            else:
                block_count += 1
                if not rr_ok:
                    status = "BLOCK(RR)"
                elif not profitable:
                    status = "BLOCK($$)"
                elif not spread_ok:
                    status = "BLOCK(SP)"
                else:
                    status = "BLOCK(SN)"

            details.append(f"  {pair:<12} SL={sl/p:>5.0f}p  TP={tp/p:>5.0f}p  RR={rr:>5.2f}  Net={net/p:>5.1f}p  {status}")

        print(f"  RESULT: {pass_count} PASS / {block_count} BLOCK out of {len(pair_data)} pairs")
        for line in details:
            print(line)

    # Side-by-side summary
    print()
    print("=" * 100)
    print("SUMMARY: PASS COUNT PER FORMULA")
    print("=" * 100)
    print(f"{'Formula':<20} {'Pass':>5} {'Block':>6} {'Description'}")
    print("-" * 100)

    for fname, f in FORMULAS.items():
        pc = 0
        bc = 0
        for pair, d in pair_data.items():
            sl = f["sl"](d)
            tp = f["tp"](d)
            rr = tp / sl if sl > 0 else 0
            net = tp - 2 * d["spread"]
            profitable = net > 0
            rr_ok = rr >= f["rr_min"] if f["rr_min"] > 0 else True
            spread_ok = d["spread"] / d["half"] < 0.15 if d["half"] > 0 else False
            noise_ok = sl > d["spread"] * 2
            if profitable and rr_ok and spread_ok and noise_ok:
                pc += 1
            else:
                bc += 1
        bar = "#" * pc + "." * bc
        print(f"{fname:<20} {pc:>5} {bc:>6}  {bar}  {f['desc']}")


if __name__ == "__main__":
    main()
