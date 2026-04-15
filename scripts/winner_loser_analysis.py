#!/usr/bin/env python3
"""
Analyze what separates winners from losers.
Goal: find metrics that filter losers WITHOUT blocking winners.
"""

import os
import requests
import json

API_KEY = os.environ["OANDA_API_KEY"]
ACCT = os.environ["OANDA_ACCOUNT_ID"]
BASE = os.environ.get("OANDA_URL", "https://api-fxpractice.oanda.com")
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

# Get closed trades
r = requests.get(f"{BASE}/v3/accounts/{ACCT}/trades", headers=HEADERS,
                 params={"state": "CLOSED", "count": "50"})
trades = r.json().get("trades", [])

# Also load entry-context data for regime info
context_data = {}
for path in [
    os.path.expanduser("~/.openclaw/workspace/agents/mr-scrooge-v2/data/entry-context.jsonl"),
    os.path.expanduser("~/.openclaw/workspace/agents/mr-scrooge/data/entry-context.jsonl"),
]:
    try:
        with open(path) as f:
            for line in f:
                d = json.loads(line.strip())
                tid = d.get("trade_id", "")
                context_data[tid] = d
    except:
        pass

print(f"Loaded {len(trades)} trades, {len(context_data)} entry contexts")
print()

winners = []
losers = []

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
    open_t = t.get("openTime", "")[:19]
    close_t = t.get("closeTime", "")[:19]
    client_id = t.get("clientExtensions", {}).get("id", "")

    # Duration
    from datetime import datetime
    try:
        ot = datetime.fromisoformat(open_t.replace("Z", "+00:00"))
        ct = datetime.fromisoformat(close_t.replace("Z", "+00:00"))
        duration_min = (ct - ot).total_seconds() / 60
    except:
        duration_min = 0

    if direction == "long":
        sl_dist = (entry - sl_p) / pip if sl_p > 0 else 0
        tp_dist = (tp_p - entry) / pip if tp_p > 0 else 0
        move_pips = (close_p - entry) / pip
    else:
        sl_dist = (sl_p - entry) / pip if sl_p > 0 else 0
        tp_dist = (entry - tp_p) / pip if tp_p > 0 else 0
        move_pips = (entry - close_p) / pip

    rr = tp_dist / sl_dist if sl_dist > 0 else 0
    spread_cost = float(t.get("financing", 0))

    # Get context data if available
    ctx = context_data.get(client_id, {})
    regime_state = ctx.get("regime_state", "UNKNOWN")
    regime_score = ctx.get("regime_score", None)
    signal_type = ctx.get("signal_type", "unknown")
    signal_score = ctx.get("signal_score", 0)
    zone_tier = ctx.get("zone_tier", 0)
    bb_pos = ctx.get("bb_position_1h", 0)
    trend = ctx.get("trend_1h", "unknown")
    ema20_aligned = ctx.get("ema20_aligned", None)
    z_score = ctx.get("z_score_1h", 0)
    volume_ratio = ctx.get("volume_ratio_5m", 0)
    adr_consumed = ctx.get("adr_consumed_pct", 0)

    record = {
        "sym": sym, "dir": direction, "pnl": pnl, "won": pnl > 0,
        "entry": entry, "close": close_p, "sl_dist": sl_dist, "tp_dist": tp_dist,
        "rr": rr, "move_pips": move_pips, "duration_min": duration_min,
        "regime_state": regime_state, "regime_score": regime_score,
        "signal_type": signal_type, "signal_score": signal_score,
        "zone_tier": zone_tier, "bb_pos": bb_pos, "trend": trend,
        "ema20_aligned": ema20_aligned, "z_score": z_score,
        "volume_ratio": volume_ratio, "adr_consumed": adr_consumed,
        "pip": pip, "client_id": client_id,
    }

    if pnl > 0:
        winners.append(record)
    else:
        losers.append(record)

print(f"Winners: {len(winners)} (total: ${sum(r['pnl'] for r in winners):+,.2f})")
print(f"Losers:  {len(losers)} (total: ${sum(r['pnl'] for r in losers):+,.2f})")
print(f"Net:     ${sum(r['pnl'] for r in winners) + sum(r['pnl'] for r in losers):+,.2f}")
print()

# Analysis 1: Regime state
print("=" * 80)
print("METRIC 1: REGIME STATE")
print("=" * 80)
for state in ["NORMAL", "CAUTION", "RESTRICTED", "BLOCKED", "UNKNOWN"]:
    w = [r for r in winners if r["regime_state"] == state]
    l = [r for r in losers if r["regime_state"] == state]
    total = len(w) + len(l)
    if total == 0:
        continue
    wr = len(w) / total * 100 if total > 0 else 0
    w_pnl = sum(r["pnl"] for r in w)
    l_pnl = sum(r["pnl"] for r in l)
    net = w_pnl + l_pnl
    print(f"  {state:<12} {len(w)}W/{len(l)}L  WR={wr:.0f}%  Net=${net:+,.2f}")
    if state in ["RESTRICTED", "BLOCKED", "CAUTION"]:
        print(f"    -> If we blocked {state}: lose {len(w)} winners (${w_pnl:+,.2f}), avoid {len(l)} losers (${l_pnl:+,.2f})")

# Analysis 2: Regime score
print()
print("=" * 80)
print("METRIC 2: REGIME SCORE")
print("=" * 80)
for threshold in [2, 1, 0, -1, -2, -3, -4]:
    w = [r for r in winners if r["regime_score"] is not None and r["regime_score"] >= threshold]
    l = [r for r in losers if r["regime_score"] is not None and r["regime_score"] >= threshold]
    w_blocked = [r for r in winners if r["regime_score"] is not None and r["regime_score"] < threshold]
    l_blocked = [r for r in losers if r["regime_score"] is not None and r["regime_score"] < threshold]
    total = len(w) + len(l)
    wr = len(w) / total * 100 if total > 0 else 0
    net = sum(r["pnl"] for r in w) + sum(r["pnl"] for r in l)
    blocked_win_pnl = sum(r["pnl"] for r in w_blocked)
    blocked_loss_pnl = sum(r["pnl"] for r in l_blocked)
    print(f"  Score >= {threshold:+d}: {len(w)}W/{len(l)}L ({wr:.0f}% WR) Net=${net:+,.2f} | Blocked: {len(w_blocked)}W/${blocked_win_pnl:+,.0f}, {len(l_blocked)}L/${blocked_loss_pnl:+,.0f}")

# Analysis 3: Duration
print()
print("=" * 80)
print("METRIC 3: TRADE DURATION")
print("=" * 80)
for bracket_name, low, high in [("<30min", 0, 30), ("30m-2h", 30, 120), ("2h-6h", 120, 360), ("6h+", 360, 99999)]:
    w = [r for r in winners if low <= r["duration_min"] < high]
    l = [r for r in losers if low <= r["duration_min"] < high]
    total = len(w) + len(l)
    if total == 0:
        continue
    wr = len(w) / total * 100
    net = sum(r["pnl"] for r in w) + sum(r["pnl"] for r in l)
    print(f"  {bracket_name:<10} {len(w)}W/{len(l)}L  WR={wr:.0f}%  Net=${net:+,.2f}")

# Analysis 4: Signal type
print()
print("=" * 80)
print("METRIC 4: SIGNAL TYPE")
print("=" * 80)
for sig in set(r["signal_type"] for r in winners + losers):
    w = [r for r in winners if r["signal_type"] == sig]
    l = [r for r in losers if r["signal_type"] == sig]
    total = len(w) + len(l)
    if total == 0:
        continue
    wr = len(w) / total * 100
    net = sum(r["pnl"] for r in w) + sum(r["pnl"] for r in l)
    print(f"  {sig:<20} {len(w)}W/{len(l)}L  WR={wr:.0f}%  Net=${net:+,.2f}")

# Analysis 5: EMA alignment
print()
print("=" * 80)
print("METRIC 5: EMA20 ALIGNMENT (with-trend vs counter-trend)")
print("=" * 80)
for aligned in [True, False, None]:
    w = [r for r in winners if r["ema20_aligned"] == aligned]
    l = [r for r in losers if r["ema20_aligned"] == aligned]
    total = len(w) + len(l)
    if total == 0:
        continue
    wr = len(w) / total * 100
    net = sum(r["pnl"] for r in w) + sum(r["pnl"] for r in l)
    label = "Aligned" if aligned else ("Counter-trend" if aligned is False else "Unknown")
    print(f"  {label:<15} {len(w)}W/{len(l)}L  WR={wr:.0f}%  Net=${net:+,.2f}")
    if aligned is False:
        print(f"    -> If blocked CT: lose {len(w)} winners (${sum(r['pnl'] for r in w):+,.2f}), avoid {len(l)} losers (${sum(r['pnl'] for r in l):+,.2f})")

# Analysis 6: Pair
print()
print("=" * 80)
print("METRIC 6: BY PAIR")
print("=" * 80)
for sym in sorted(set(r["sym"] for r in winners + losers)):
    w = [r for r in winners if r["sym"] == sym]
    l = [r for r in losers if r["sym"] == sym]
    total = len(w) + len(l)
    wr = len(w) / total * 100 if total > 0 else 0
    net = sum(r["pnl"] for r in w) + sum(r["pnl"] for r in l)
    print(f"  {sym:<12} {len(w)}W/{len(l)}L  WR={wr:.0f}%  Net=${net:+,.2f}")

# Analysis 7: ADR consumed
print()
print("=" * 80)
print("METRIC 7: ADR CONSUMED AT ENTRY")
print("=" * 80)
for bracket_name, low, high in [("<60%", 0, 0.6), ("60-80%", 0.6, 0.8), ("80-100%", 0.8, 1.0), (">100%", 1.0, 99)]:
    w = [r for r in winners if r["adr_consumed"] and low <= r["adr_consumed"] < high]
    l = [r for r in losers if r["adr_consumed"] and low <= r["adr_consumed"] < high]
    total = len(w) + len(l)
    if total == 0:
        continue
    wr = len(w) / total * 100
    net = sum(r["pnl"] for r in w) + sum(r["pnl"] for r in l)
    print(f"  ADR {bracket_name:<8} {len(w)}W/{len(l)}L  WR={wr:.0f}%  Net=${net:+,.2f}")

# Analysis 8: Signal score
print()
print("=" * 80)
print("METRIC 8: SIGNAL SCORE BRACKETS")
print("=" * 80)
for bracket_name, low, high in [("1-30", 1, 31), ("31-50", 31, 51), ("51-65", 51, 66), ("66-80", 66, 81), ("80+", 81, 999)]:
    w = [r for r in winners if r["signal_score"] and low <= r["signal_score"] < high]
    l = [r for r in losers if r["signal_score"] and low <= r["signal_score"] < high]
    total = len(w) + len(l)
    if total == 0:
        continue
    wr = len(w) / total * 100
    net = sum(r["pnl"] for r in w) + sum(r["pnl"] for r in l)
    print(f"  Score {bracket_name:<6} {len(w)}W/{len(l)}L  WR={wr:.0f}%  Net=${net:+,.2f}")

# GRAND SUMMARY: What combination would have been best?
print()
print("=" * 80)
print("COMBINED FILTER SIMULATION")
print("=" * 80)

filters = [
    ("No filter (take all)", lambda r: True),
    ("Regime >= 0 only", lambda r: r["regime_score"] is not None and r["regime_score"] >= 0),
    ("Regime >= +1 only", lambda r: r["regime_score"] is not None and r["regime_score"] >= 1),
    ("Regime >= +2 only", lambda r: r["regime_score"] is not None and r["regime_score"] >= 2),
    ("EMA aligned only", lambda r: r["ema20_aligned"] == True),
    ("No USD_MXN", lambda r: r["sym"] != "USD_MXN"),
    ("Regime >= 0 + No MXN", lambda r: (r["regime_score"] is not None and r["regime_score"] >= 0) and r["sym"] != "USD_MXN"),
    ("Score >= 60", lambda r: r["signal_score"] and r["signal_score"] >= 60),
    ("Score >= 60 + Regime >= 0", lambda r: (r["signal_score"] and r["signal_score"] >= 60) and (r["regime_score"] is not None and r["regime_score"] >= 0)),
    ("ADR < 100% + Regime >= 0", lambda r: (r["adr_consumed"] and r["adr_consumed"] < 1.0) and (r["regime_score"] is not None and r["regime_score"] >= 0)),
]

all_trades = winners + losers
print(f"{'Filter':<35} {'W':>3} {'L':>3} {'WR':>5} {'Net PnL':>12} {'Win$':>10} {'Loss$':>10} {'Blocked W':>10}")
print("-" * 100)

for name, fn in filters:
    passed = [r for r in all_trades if fn(r)]
    blocked = [r for r in all_trades if not fn(r)]
    w = [r for r in passed if r["won"]]
    l = [r for r in passed if not r["won"]]
    bw = [r for r in blocked if r["won"]]
    total = len(w) + len(l)
    wr = len(w) / total * 100 if total > 0 else 0
    net = sum(r["pnl"] for r in passed)
    w_pnl = sum(r["pnl"] for r in w)
    l_pnl = sum(r["pnl"] for r in l)
    bw_pnl = sum(r["pnl"] for r in bw)
    print(f"{name:<35} {len(w):>3} {len(l):>3} {wr:>4.0f}% {net:>+11,.2f} {w_pnl:>+9,.0f} {l_pnl:>+9,.0f} {len(bw):>3}/${bw_pnl:+,.0f}")
