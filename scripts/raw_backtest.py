#!/usr/bin/env python3
"""
Raw OANDA data backtest — NO bot logs.

For each closed trade:
1. Pull daily candles → reconstruct the box (PDH/PDL) at entry time
2. Pull 5M candles around entry time → find signal candle
3. Calculate natural stop from candle extreme
4. Calculate spread from bid/ask candles at entry
5. Run 10 formula variations
6. Report: which formulas let winners through, which block losers
"""

import os
import requests
from datetime import datetime, timedelta

API_KEY = os.environ["OANDA_API_KEY"]
ACCT = os.environ["OANDA_ACCOUNT_ID"]
ENV = os.environ.get("OANDA_ENVIRONMENT", "practice")
BASE = "https://api-fxtrade.oanda.com" if ENV == "live" else "https://api-fxpractice.oanda.com"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}


def get_candles(pair, granularity, time_from, count=50):
    """Pull candles starting from a specific time."""
    params = {"granularity": granularity, "count": str(count), "price": "MBA"}
    if time_from:
        params["from"] = time_from
    r = requests.get(f"{BASE}/v3/instruments/{pair}/candles", headers=HEADERS, params=params)
    return r.json().get("candles", [])


def get_candles_before(pair, granularity, time_before, count=50):
    """Pull candles ending at a specific time."""
    params = {"granularity": granularity, "count": str(count), "price": "MBA",
              "to": time_before}
    r = requests.get(f"{BASE}/v3/instruments/{pair}/candles", headers=HEADERS, params=params)
    return r.json().get("candles", [])


def build_box(daily_candles, entry_time_str):
    """Find prior completed day's high/low for the box."""
    entry_date = entry_time_str[:10]
    prior = None
    for c in reversed(daily_candles):
        c_date = c["time"][:10]
        if c_date < entry_date:
            h = float(c["mid"]["h"])
            l = float(c["mid"]["l"])
            if (h - l) / l > 0.0005:  # skip tiny bars
                prior = c
                break
    if not prior:
        return None
    return {
        "PDH": float(prior["mid"]["h"]),
        "PDL": float(prior["mid"]["l"]),
    }


def find_signal_candle(bars_5m, entry_price, direction, pip):
    """Find the reversal candle nearest to entry time.

    The signal candle is the first reversal candle (green for long, red for short)
    that appears after a directional push. We look at the last few candles before entry.
    """
    if not bars_5m or len(bars_5m) < 3:
        return None

    # Look at last 5 candles for the signal candle
    for i in range(len(bars_5m) - 1, max(len(bars_5m) - 6, 0), -1):
        c = bars_5m[i]
        m = c["mid"]
        o, h, l, cl = float(m["o"]), float(m["h"]), float(m["l"]), float(m["c"])

        if direction == "long" and cl > o:
            # Green candle — potential long signal
            return {"high": h, "low": l, "open": o, "close": cl,
                    "lower_wick": min(o, cl) - l, "upper_wick": h - max(o, cl),
                    "body": abs(cl - o), "range": h - l}
        elif direction == "short" and cl < o:
            # Red candle — potential short signal
            return {"high": h, "low": l, "open": o, "close": cl,
                    "lower_wick": min(o, cl) - l, "upper_wick": h - max(o, cl),
                    "body": abs(cl - o), "range": h - l}

    return None


def calc_natural_stop(signal_candle, direction, pip):
    """Natural stop = signal candle extreme + buffer."""
    if not signal_candle:
        return None
    buffer = 2 * pip
    if direction == "long":
        return signal_candle["low"] - buffer
    else:
        return signal_candle["high"] + buffer


def get_spread_at_entry(bars_5m_ba, entry_idx):
    """Estimate spread from bid/ask candle data near entry."""
    if not bars_5m_ba or entry_idx >= len(bars_5m_ba):
        return 0
    c = bars_5m_ba[min(entry_idx, len(bars_5m_ba) - 1)]
    ask_c = float(c.get("ask", {}).get("c", 0))
    bid_c = float(c.get("bid", {}).get("c", 0))
    if ask_c > 0 and bid_c > 0:
        return ask_c - bid_c
    return 0


def run_formulas(entry, sl_natural_pips, half_box_pips, box_pips, spread_pips, atr_pips, mid):
    """Run all 10 formula variations. Returns dict of formula_name -> (passed, rr, sl_used)."""
    pip = 0.01 if mid > 10 else 0.0001
    results = {}

    formulas = [
        ("F01_curr_025", max(sl_natural_pips, mid * 0.0025 / pip), half_box_pips, 1.35),
        ("F02_flr_015",  max(sl_natural_pips, mid * 0.0015 / pip), half_box_pips, 1.35),
        ("F03_flr_010",  max(sl_natural_pips, mid * 0.0010 / pip), half_box_pips, 1.35),
        ("F04_no_floor", sl_natural_pips + spread_pips,            half_box_pips, 1.35),
        ("F05_no_rr",    sl_natural_pips + spread_pips,            half_box_pips, 0.0),
        ("F06_box_15",   max(sl_natural_pips, box_pips * 0.15),    half_box_pips, 1.35),
        ("F07_atr_10",   max(sl_natural_pips, atr_pips * 0.10),    half_box_pips, 1.35),
        ("F08_tp1_rr",   max(sl_natural_pips, mid * 0.0015 / pip), half_box_pips * 0.5, 0.80),
        ("F09_hybrid",   max(sl_natural_pips, box_pips * 0.10, spread_pips * 2), half_box_pips, 1.0),
        ("F10_viable",   sl_natural_pips + spread_pips,            half_box_pips * 0.40, 0.0),
    ]

    for name, sl, tp, rr_min in formulas:
        if sl <= 0:
            results[name] = (False, 0, sl, "zero_sl")
            continue
        rr = tp / sl if sl > 0 else 0

        # Always check: can profit after spread?
        net = tp - 2 * spread_pips
        profitable = net > 0

        # Noise check: SL > 2x spread
        noise_ok = sl > spread_pips * 2

        # Spread check: < 15% of half box
        spread_ok = spread_pips / half_box_pips < 0.15 if half_box_pips > 0 else False

        # RR check
        rr_ok = rr >= rr_min if rr_min > 0 else True

        passed = profitable and noise_ok and spread_ok and rr_ok
        reason = ""
        if not rr_ok:
            reason = "RR"
        elif not profitable:
            reason = "$$"
        elif not spread_ok:
            reason = "SP"
        elif not noise_ok:
            reason = "SN"

        results[name] = (passed, rr, sl, reason)

    return results


def main():
    # Get all closed trades
    r = requests.get(f"{BASE}/v3/accounts/{ACCT}/trades", headers=HEADERS,
                     params={"state": "CLOSED", "count": "50"})
    trades = r.json().get("trades", [])
    print(f"Fetched {len(trades)} closed trades from OANDA")
    print()

    trade_analyses = []
    errors = 0

    for t in trades:
        sym = t.get("instrument", "")
        units = float(t.get("initialUnits", 0))
        entry_price = float(t.get("price", 0))
        close_price = float(t.get("averageClosePrice", 0))
        pnl = float(t.get("realizedPL", 0))
        open_time = t.get("openTime", "")
        direction = "short" if units < 0 else "long"
        pip = 0.01 if "JPY" in sym else 0.0001

        try:
            # 1. Pull daily candles around entry time
            daily = get_candles_before(sym, "D", open_time, count=10)
            box = build_box(daily, open_time)
            if not box:
                errors += 1
                continue

            pdh, pdl = box["PDH"], box["PDL"]
            box_range = pdh - pdl
            half_box = box_range / 2

            # 2. Pull 5M candles before entry
            bars_5m = get_candles_before(sym, "M5", open_time, count=20)

            # 3. Find signal candle and natural stop
            signal = find_signal_candle(bars_5m, entry_price, direction, pip)
            if signal:
                natural_stop = calc_natural_stop(signal, direction, pip)
                if direction == "long":
                    sl_natural_pips = (entry_price - natural_stop) / pip
                else:
                    sl_natural_pips = (natural_stop - entry_price) / pip
            else:
                # Fallback: use avg 5M range as proxy
                ranges = [float(b["mid"]["h"]) - float(b["mid"]["l"]) for b in bars_5m[-10:]]
                avg_range = sum(ranges) / len(ranges) if ranges else pip * 10
                sl_natural_pips = avg_range / pip
                natural_stop = 0

            # 4. Estimate spread at entry from bid/ask
            bars_ba = get_candles_before(sym, "M5", open_time, count=5)
            if bars_ba:
                last_ba = bars_ba[-1]
                ask_h = float(last_ba.get("ask", {}).get("c", 0))
                bid_h = float(last_ba.get("bid", {}).get("c", 0))
                spread = (ask_h - bid_h) if ask_h > 0 and bid_h > 0 else pip * 2
            else:
                spread = pip * 2
            spread_pips = spread / pip

            # 5. ATR from daily
            atrs = []
            for i in range(1, len(daily)):
                h = float(daily[i]["mid"]["h"])
                l = float(daily[i]["mid"]["l"])
                pc = float(daily[i-1]["mid"]["c"])
                tr = max(h - l, abs(h - pc), abs(l - pc))
                atrs.append(tr)
            atr = sum(atrs) / len(atrs) if atrs else box_range
            atr_pips = atr / pip

            box_pips = box_range / pip
            half_pips = half_box / pip

            # 6. Run formulas
            formula_results = run_formulas(
                entry_price, sl_natural_pips, half_pips, box_pips,
                spread_pips, atr_pips, entry_price
            )

            trade_analyses.append({
                "sym": sym, "dir": direction, "pnl": pnl, "won": pnl > 0,
                "entry": entry_price, "close": close_price,
                "pdh": pdh, "pdl": pdl, "box_pips": box_pips,
                "half_pips": half_pips, "spread_pips": spread_pips,
                "sl_natural_pips": sl_natural_pips, "atr_pips": atr_pips,
                "open_time": open_time[:16], "formulas": formula_results,
                "wick_ratio": signal["lower_wick"] / signal["body"] if signal and signal["body"] > 0 and direction == "long"
                    else signal["upper_wick"] / signal["body"] if signal and signal["body"] > 0
                    else 0,
            })

        except Exception as e:
            errors += 1
            print(f"  Error on {sym} {open_time[:16]}: {e}")

    print(f"Analyzed {len(trade_analyses)} trades ({errors} errors)")
    print()

    # Display results
    fnames = ["F01_curr_025", "F02_flr_015", "F03_flr_010", "F04_no_floor",
              "F05_no_rr", "F06_box_15", "F07_atr_10", "F09_hybrid"]

    print("=" * 160)
    print("RAW DATA BACKTEST — FORMULA COMPARISON")
    print("=" * 160)
    hdr = f"{'Pair':<10} {'Dir':<5} {'PnL':>9} {'W/L':<4} {'Box':>5} {'Half':>5} {'Sprd':>5} {'NatSL':>5} {'ATR':>5} |"
    for fn in fnames:
        hdr += f" {fn[-7:]:>7}"
    print(hdr)
    print("-" * 160)

    for ta in trade_analyses:
        row = f"{ta['sym']:<10} {ta['dir']:<5} {ta['pnl']:>+9.0f} {'W' if ta['won'] else 'L':<4} {ta['box_pips']:>4.0f}p {ta['half_pips']:>4.0f}p {ta['spread_pips']:>4.1f}p {ta['sl_natural_pips']:>4.0f}p {ta['atr_pips']:>4.0f}p |"
        for fn in fnames:
            passed, rr, sl, reason = ta["formulas"][fn]
            mark = f"{rr:>5.1f}+" if passed else f"{rr:>4.1f}{reason:>2}-"
            row += f" {mark}"
        print(row)

    # Summary
    print()
    print("=" * 160)
    print("FORMULA SUMMARY")
    print("=" * 160)
    print(f"{'Formula':<15} {'Passed':>6} {'WinCap':>7} {'LossBlk':>8} {'PnL$':>12} {'AvgWin$':>9} {'AvgLoss$':>10} {'BlockedWin$':>12}")
    print("-" * 100)

    for fn in fnames:
        passed_w = [ta for ta in trade_analyses if ta["formulas"][fn][0] and ta["won"]]
        passed_l = [ta for ta in trade_analyses if ta["formulas"][fn][0] and not ta["won"]]
        blocked_w = [ta for ta in trade_analyses if not ta["formulas"][fn][0] and ta["won"]]
        blocked_l = [ta for ta in trade_analyses if not ta["formulas"][fn][0] and not ta["won"]]

        total_w = len(passed_w) + len(blocked_w)
        total_l = len(passed_l) + len(blocked_l)
        passed_total = len(passed_w) + len(passed_l)
        pnl_passed = sum(ta["pnl"] for ta in passed_w) + sum(ta["pnl"] for ta in passed_l)
        avg_win = sum(ta["pnl"] for ta in passed_w) / len(passed_w) if passed_w else 0
        avg_loss = sum(ta["pnl"] for ta in passed_l) / len(passed_l) if passed_l else 0
        blocked_w_pnl = sum(ta["pnl"] for ta in blocked_w)

        wc = f"{len(passed_w)}/{total_w}"
        lb = f"{len(blocked_l)}/{total_l}"
        print(f"{fn:<15} {passed_total:>6} {wc:>7} {lb:>8} {pnl_passed:>+11,.0f} {avg_win:>+8,.0f} {avg_loss:>+9,.0f} {blocked_w_pnl:>+11,.0f}")


if __name__ == "__main__":
    main()
