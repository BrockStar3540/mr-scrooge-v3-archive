#!/usr/bin/env python3
"""Backtest 10 formula variations against actual OANDA closed trades."""

import os
import requests

API_KEY = os.environ["OANDA_API_KEY"]
ACCT = os.environ["OANDA_ACCOUNT_ID"]
BASE = os.environ.get("OANDA_URL", "https://api-fxpractice.oanda.com")
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

# Get closed trades
r = requests.get(f"{BASE}/v3/accounts/{ACCT}/trades", headers=HEADERS,
                 params={"state": "CLOSED", "count": "50"})
trades = r.json().get("trades", [])

results = []
for t in trades:
    sym = t.get("instrument", "")
    units = float(t.get("initialUnits", 0))
    entry = float(t.get("price", 0))
    close_p = float(t.get("averageClosePrice", 0))
    pnl = float(t.get("realizedPL", 0))
    sl_p = float(t.get("stopLossOrder", {}).get("price", 0))
    tp_p = float(t.get("takeProfitOrder", {}).get("price", 0))
    direction = "short" if units < 0 else "long"
    pip = 0.01 if "JPY" in sym else 0.0001
    open_t = t.get("openTime", "")[:16]
    close_t = t.get("closeTime", "")[:16]

    if direction == "long":
        sl_dist = (entry - sl_p) / pip if sl_p > 0 else 0
        tp_dist = (tp_p - entry) / pip if tp_p > 0 else 0
    else:
        sl_dist = (sl_p - entry) / pip if sl_p > 0 else 0
        tp_dist = (entry - tp_p) / pip if tp_p > 0 else 0

    rr = tp_dist / sl_dist if sl_dist > 0 else 0

    results.append({
        "sym": sym, "dir": direction, "entry": entry, "close": close_p,
        "pnl": pnl, "won": pnl > 0, "sl_dist": sl_dist, "tp_dist": tp_dist,
        "rr": rr, "pip": pip, "open_t": open_t, "close_t": close_t,
    })

print(f"Loaded {len(results)} closed trades")
print()

# Trade details
print("=" * 130)
print("ACTUAL TRADES WITH FORMULA PASS/BLOCK")
print("=" * 130)
print(f"{'Pair':<12} {'Dir':<6} {'PnL':>10} {'W/L':<5} {'SL':>6} {'TP':>6} {'RR':>5} | {'F01':>3} {'F02':>3} {'F03':>3} {'F06':>3} {'F07':>3} {'F09':>3}")
print("-" * 130)

formula_results = {k: {"wp": 0, "wb": 0, "lp": 0, "lb": 0, "pnl_passed": 0.0}
                   for k in ["F01", "F02", "F03", "F06", "F07", "F09"]}

for t in results:
    pip = t["pip"]
    mid = t["entry"]
    sl = t["sl_dist"]
    tp = t["tp_dist"]
    box_proxy = tp * 2

    checks = {}

    # F01: Current (SL floor 0.25%, RR 1.35)
    floor = mid * 0.0025 / pip
    eff_rr = tp / max(sl, floor) if max(sl, floor) > 0 else 0
    checks["F01"] = eff_rr >= 1.35

    # F02: Floor 0.15%
    floor = mid * 0.0015 / pip
    eff_rr = tp / max(sl, floor) if max(sl, floor) > 0 else 0
    checks["F02"] = eff_rr >= 1.35

    # F03: Floor 0.10%
    floor = mid * 0.0010 / pip
    eff_rr = tp / max(sl, floor) if max(sl, floor) > 0 else 0
    checks["F03"] = eff_rr >= 1.35

    # F06: Box 15% floor
    floor = box_proxy * 0.15
    eff_rr = tp / max(sl, floor) if max(sl, floor) > 0 else 0
    checks["F06"] = eff_rr >= 1.35

    # F07: ATR 10% (use box as ATR proxy)
    floor = box_proxy * 0.10 * 1.5  # ATR ~ 1.5x box
    eff_rr = tp / max(sl, floor) if max(sl, floor) > 0 else 0
    checks["F07"] = eff_rr >= 1.35

    # F09: Hybrid (max candle, 10% box, no fixed), RR 1.0
    floor = box_proxy * 0.10
    eff_rr = tp / max(sl, floor) if max(sl, floor) > 0 else 0
    checks["F09"] = eff_rr >= 1.0

    # Track stats
    for k, passed in checks.items():
        if t["won"] and passed:
            formula_results[k]["wp"] += 1
            formula_results[k]["pnl_passed"] += t["pnl"]
        elif t["won"] and not passed:
            formula_results[k]["wb"] += 1
        elif not t["won"] and passed:
            formula_results[k]["lp"] += 1
            formula_results[k]["pnl_passed"] += t["pnl"]
        else:
            formula_results[k]["lb"] += 1

    wl = " WIN" if t["won"] else "LOSS"
    marks = " | "
    for k in ["F01", "F02", "F03", "F06", "F07", "F09"]:
        marks += f"  {'P' if checks[k] else 'B'} "

    print(f"{t['sym']:<12} {t['dir']:<6} {t['pnl']:>+10.2f} {wl:<5} {sl:>5.0f}p {tp:>5.0f}p {t['rr']:>5.2f}{marks}")

# Summary
total_wins = sum(1 for t in results if t["won"])
total_losses = sum(1 for t in results if not t["won"])
total_pnl = sum(t["pnl"] for t in results)

print()
print("=" * 130)
print(f"TOTALS: {len(results)} trades, {total_wins} wins, {total_losses} losses, PnL: ${total_pnl:+,.2f}")
print("=" * 130)
print()
print(f"{'Formula':<8} {'Win Cap':>8} {'Loss Blk':>9} {'Passed':>7} {'PnL if taken':>13} {'Description'}")
print("-" * 100)

descs = {
    "F01": "Current: SL floor 0.25% price, RR 1.35",
    "F02": "SL floor 0.15% price, RR 1.35",
    "F03": "SL floor 0.10% price, RR 1.35",
    "F06": "SL floor 15% of box, RR 1.35",
    "F07": "SL floor 10% of ATR, RR 1.35",
    "F09": "Hybrid (10% box floor), RR 1.0",
}

for k in ["F01", "F02", "F03", "F06", "F07", "F09"]:
    fr = formula_results[k]
    tw = fr["wp"] + fr["wb"]
    tl = fr["lp"] + fr["lb"]
    wc = f"{fr['wp']}/{tw}" if tw > 0 else "0/0"
    lb = f"{fr['lb']}/{tl}" if tl > 0 else "0/0"
    passed = fr["wp"] + fr["lp"]
    pnl_p = fr["pnl_passed"]
    print(f"{k:<8} {wc:>8} {lb:>9} {passed:>7} {pnl_p:>+12,.2f}  {descs[k]}")

print()
print("Win Cap = winners that would have been allowed through")
print("Loss Blk = losers that would have been blocked")
print("PnL if taken = total P&L of trades that passed the formula")
