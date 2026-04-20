"""M1 re-run of Part B (management simulation) for Mr. Scrooge V3 backtest.

Only simulates the 11 trades the V3 scorer accepted in the prior M5 run.
Part A scorer results are taken as-is from the prior run (don't depend on
candle granularity).

Key differences vs run_backtest.py:
- Granularity: M1 instead of M5
- Fetches bid + ask + mid candles (price=BAM) so SL triggers use the correct side
  (longs: bid_low ≤ SL; shorts: ask_high ≥ SL)
- Separate cache dir candles_cache_m1/
- Pre-entry context: open_time - 15min, close_time + 5min
- Extra diagnostics on the 4 prior M5 full-SL losers: did they reach +0.5R BE
  trigger on M1? sequence of low vs high?
"""
from __future__ import annotations

import csv
import json
import os
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ENV_PATH = Path.home() / "mr-scrooge-v3" / ".env"
for line in ENV_PATH.read_text().splitlines():
    line = line.strip()
    if not line or line.startswith("#") or "=" not in line:
        continue
    k, v = line.split("=", 1)
    os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

sys.path.insert(0, str(Path.home() / "mr-scrooge-v3" / "src"))

from scrooge_v3.strategies.v3_scorer import V3HybridScorer, ScorerResult  # noqa: E402
from scrooge_v3.core.types import TradeDirection  # noqa: E402

import urllib.request
import urllib.parse
import urllib.error

REPO = Path.home() / "mr-scrooge-v3"
DATA_CSV = REPO / "data" / "trades_features.csv"
BT_DIR = REPO / "backtests"
CACHE_DIR = BT_DIR / "candles_cache_m1"
REPORT_PATH = BT_DIR / "report_m1.md"
M5_REPORT_PATH = BT_DIR / "report.md"

BT_DIR.mkdir(exist_ok=True)
CACHE_DIR.mkdir(exist_ok=True)

CFG_MGMT = {
    "tp1_r": 1.0,
    "tp1_fraction": 0.50,
    "be_trigger_r": 0.5, "be_trigger_min_pips": 2.0,
    "be_offset_r": 0.1, "be_offset_min_pips": 1.0,
    "ratchet_trigger_r": 1.0, "ratchet_trigger_min_pips": 3.0,
    "ratchet_lock_pct": 0.50,
    "margin_utilization": 0.40,
}

OANDA_URL = os.environ.get("OANDA_API_URL", "https://api-fxpractice.oanda.com")
OANDA_TOKEN = os.environ.get("OANDA_API_TOKEN", "")

# The 11 trades accepted by the scorer in the prior run (from report.md Part B)
ACCEPTED_TRADE_IDS = {"5873","5765","5755","5723","5713","5591","5573","5509","5464","5438","5309"}

# Prior M5 results to compare against (from report.md table)
PRIOR_M5 = {
    "5873": {"exit_reason":"sl_hit","R":-1.00,"mfe":0.47,"mae":-1.09,"tp1":False,"be":False,"usd":-400.00},
    "5765": {"exit_reason":"invalid_R","R":0.00,"mfe":0.00,"mae":0.00,"tp1":False,"be":False,"usd":0.00},
    "5755": {"exit_reason":"be_hit","R":0.78,"mfe":1.12,"mae":-0.60,"tp1":True,"be":True,"usd":312.00},
    "5723": {"exit_reason":"invalid_R","R":0.00,"mfe":0.00,"mae":0.00,"tp1":False,"be":False,"usd":0.00},
    "5713": {"exit_reason":"be_hit","R":0.24,"mfe":0.81,"mae":-0.52,"tp1":False,"be":True,"usd":95.24},
    "5591": {"exit_reason":"sl_hit","R":-1.00,"mfe":0.01,"mae":-1.19,"tp1":False,"be":False,"usd":-400.00},
    "5573": {"exit_reason":"be_hit","R":0.17,"mfe":0.58,"mae":-0.66,"tp1":False,"be":True,"usd":67.80},
    "5509": {"exit_reason":"sl_hit","R":-1.00,"mfe":0.47,"mae":-1.79,"tp1":False,"be":False,"usd":-400.00},
    "5464": {"exit_reason":"be_hit","R":0.27,"mfe":0.57,"mae":-0.78,"tp1":False,"be":True,"usd":108.11},
    "5438": {"exit_reason":"sl_hit","R":-1.00,"mfe":0.58,"mae":-1.21,"tp1":False,"be":False,"usd":-400.00},
    "5309": {"exit_reason":"be_hit","R":0.19,"mfe":0.63,"mae":-0.67,"tp1":False,"be":True,"usd":74.07},
}

PRIOR_M5_SL_LOSERS = {"5873","5591","5509","5438"}


def pip_size(symbol: str) -> float:
    return 0.01 if "JPY" in symbol else 0.0001


def fetch_candles_m1(symbol: str, start: datetime, end: datetime) -> list[dict]:
    """Fetch M1 BAM (bid+ask+mid) candles for [start, end], chunked to <=5000/call, cached."""
    cache_key = f"{symbol}_M1_{start.isoformat()}_{end.isoformat()}.json".replace(":", "-")
    cache_file = CACHE_DIR / cache_key
    if cache_file.exists():
        return json.loads(cache_file.read_text())

    out: list[dict] = []
    cur = start
    # M1 = 60/hour. 5000/60 ≈ 83h — our windows are well below that, but loop anyway for safety.
    while cur < end:
        chunk_end = min(end, cur + timedelta(hours=80))
        params = {
            "from": cur.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "to":   chunk_end.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "granularity": "M1",
            "price": "BAM",
        }
        url = f"{OANDA_URL}/v3/instruments/{symbol}/candles?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {OANDA_TOKEN}"})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            body = e.read().decode() if hasattr(e, 'read') else str(e)
            print(f"  OANDA ERR {symbol} {cur}-{chunk_end}: {e.code} {body[:200]}", file=sys.stderr)
            return []
        candles = data.get("candles", [])
        out.extend(candles)
        cur = chunk_end
        time.sleep(0.15)  # gentle throttle

    cache_file.write_text(json.dumps(out))
    return out


def score_from_row(scorer: V3HybridScorer, row: dict) -> ScorerResult:
    """Copied from run_backtest.py so we can determine tier for output consistency."""
    f = {
        "hour": int(row["hour"]),
        "bage": float(row["bage"]),
        "ns":   float(row["ns"]),
        "vr":   float(row["vr"]),
        "mom":  float(row["mom"]),
        "dc":   float(row["dc"]),
        "zs":   float(row["zs"]),
        "bbp":  float(row["bbp"]),
        "e50d": float(row["e50d"]),
        "e20d": float(row["e20d"]),
        "otr":  float(row["otr"]),
        "adr":  float(row["adr"]),
        "dur":  60.0,
        "wp":   float(row["wp"]),
        "bp":   float(row["bp"]),
        "bbs":  row["bbs"],
        "rsi":  float(row["rsi"]),
        "_price": float(row["entry"]),
        "_ema20": 0.0, "_ema50": 0.0,
        "_box_range": 0.0, "_pdh": 0.0, "_pdl": 0.0,
        "_box_age_h": float(row["bage"]),
        "_spread": float(row.get("sp", 0.0)),
    }
    from scrooge_v3.core.types import TradeCandidate as TC
    direction = TradeDirection.LONG if row["d"] == "L" else TradeDirection.SHORT
    cand = TC(
        symbol=row["sym"], direction=direction, strategy="reversal",
        entry_price=float(row["entry"]),
        stop_price=float(row["entry"]) + (f["ns"] * pip_size(row["sym"]) * (1 if direction == TradeDirection.SHORT else -1)),
        metadata={"strategy_family": ""},
    )
    return scorer._compute_score(f, cand)


@dataclass
class SimResultM1:
    accepted: bool = True
    tier: str = ""
    exit_reason: str = ""
    exit_price: float = 0.0
    realized_R: float = 0.0
    realized_usd: float = 0.0
    mfe_R: float = 0.0
    mae_R: float = 0.0
    tp1_hit: bool = False
    be_moved: bool = False
    ratchet_hit: bool = False
    be_fire_time: str = ""
    tp1_fire_time: str = ""
    exit_time: str = ""
    # diagnostic for prior-SL cases: did price reach +0.5R BE trigger at all?
    reached_be_trigger: bool = False
    be_trigger_time: str = ""
    # sequence: did BE-trigger high precede adverse low that would've tripped full SL?
    first_adverse_sl_time: str = ""
    notes: str = ""


def simulate_trade_m1(row: dict, tier: str, account_equity_usd: float = 1000.0) -> SimResultM1:
    symbol = row["sym"]
    direction = TradeDirection.LONG if row["d"] == "L" else TradeDirection.SHORT
    entry_price = float(row["entry"])
    ns_pips = float(row["ns"])
    psize = pip_size(symbol)
    R = ns_pips * psize
    if R <= 0:
        return SimResultM1(tier=tier, exit_reason="invalid_R", notes="ns<=0")

    if direction == TradeDirection.LONG:
        sl = entry_price - R
        tp1 = entry_price + CFG_MGMT["tp1_r"] * R
    else:
        sl = entry_price + R
        tp1 = entry_price - CFG_MGMT["tp1_r"] * R
    original_sl = sl

    open_time = datetime.fromisoformat(row["open_time"]).replace(tzinfo=timezone.utc)
    close_time = datetime.fromisoformat(row["close_time"]).replace(tzinfo=timezone.utc)
    fetch_start = open_time - timedelta(minutes=15)
    fetch_end = close_time + timedelta(minutes=5)
    # 48h hard cap for safety
    fetch_end = min(fetch_end, open_time + timedelta(hours=48))

    candles = fetch_candles_m1(symbol, fetch_start, fetch_end)
    if not candles:
        return SimResultM1(tier=tier, exit_reason="no_candles", notes="fetch failed")

    # Filter: only bars at/after open_time for the sim loop
    sim_candles = [c for c in candles if c.get("complete", True) and c.get("time")]

    be_trigger_dist = max(CFG_MGMT["be_trigger_r"] * R, CFG_MGMT["be_trigger_min_pips"] * psize)
    be_offset_dist  = max(CFG_MGMT["be_offset_r"]  * R, CFG_MGMT["be_offset_min_pips"]  * psize)
    rat_trigger_dist = max(CFG_MGMT["ratchet_trigger_r"] * R, CFG_MGMT["ratchet_trigger_min_pips"] * psize)
    lock_pct = CFG_MGMT["ratchet_lock_pct"]

    tp1_hit = False
    be_moved = False
    ratchet_hit = False
    peak_price = entry_price      # for longs (use ask to be conservative? use mid for MFE anchor — standard)
    trough_price = entry_price    # for shorts
    mfe_R = 0.0
    mae_R = 0.0
    exit_reason = "timeout"
    exit_price = entry_price
    exit_time = ""
    be_fire_time = ""
    tp1_fire_time = ""

    reached_be_trigger = False
    be_trigger_time = ""
    first_adverse_sl_time = ""

    res = SimResultM1(tier=tier)

    for c in sim_candles:
        t = c["time"]
        # parse time (only keep at/after open_time)
        try:
            ct = datetime.fromisoformat(t.replace("Z","+00:00"))
        except Exception:
            continue
        if ct < open_time:
            continue

        bid = c.get("bid", {})
        ask = c.get("ask", {})
        mid = c.get("mid", {})
        if not (bid and ask and mid):
            continue
        bid_h = float(bid["h"]); bid_l = float(bid["l"])
        ask_h = float(ask["h"]); ask_l = float(ask["l"])
        mid_h = float(mid["h"]); mid_l = float(mid["l"]); mid_c = float(mid["c"])

        # For longs: SL trigger = bid_low (what we'd sell at). MFE uses bid_high (fav side).
        # For shorts: SL trigger = ask_high (what we'd buy back at). MFE uses ask_low (fav side).
        if direction == TradeDirection.LONG:
            fav_high = bid_h    # our exit-side favorable high
            unfav_low = bid_l   # adverse low that trips SL
            peak_price = max(peak_price, fav_high)
            mfe_R = max(mfe_R, (peak_price - entry_price) / R)
            mae_R = min(mae_R, (unfav_low - entry_price) / R)
        else:
            fav_low = ask_l
            unfav_high = ask_h
            trough_price = min(trough_price, fav_low)
            mfe_R = max(mfe_R, (entry_price - trough_price) / R)
            mae_R = min(mae_R, (entry_price - unfav_high) / R)

        # Diagnostic: did we reach BE trigger (+0.5R on favorable extreme)?
        if not reached_be_trigger:
            if direction == TradeDirection.LONG:
                fav_dist = fav_high - entry_price
            else:
                fav_dist = entry_price - fav_low
            if fav_dist >= be_trigger_dist:
                reached_be_trigger = True
                be_trigger_time = t

        # Diagnostic: when would original full SL have first been tripped?
        if not first_adverse_sl_time:
            if direction == TradeDirection.LONG and bid_l <= original_sl:
                first_adverse_sl_time = t
            elif direction == TradeDirection.SHORT and ask_h >= original_sl:
                first_adverse_sl_time = t

        # --- management checks ---
        # Check SL (may be original or moved BE/ratchet)
        sl_hit = (direction == TradeDirection.LONG and bid_l <= sl) or \
                 (direction == TradeDirection.SHORT and ask_h >= sl)
        tp1_touched = (not tp1_hit) and (
            (direction == TradeDirection.LONG and bid_h >= tp1) or
            (direction == TradeDirection.SHORT and ask_l <= tp1)
        )

        # Intrabar ordering on M1: still ambiguous (60s bar) but much finer than M5.
        # Conservative policy matching M5 run: SL before TP1 if both in same bar.
        if sl_hit and tp1_touched:
            exit_price = sl
            exit_reason = "sl_same_bar_as_tp1" if not be_moved else "be_hit"
            exit_time = t
            break
        if sl_hit:
            exit_price = sl
            exit_reason = "sl_hit" if not be_moved else "be_hit"
            exit_time = t
            break
        if tp1_touched:
            tp1_hit = True
            tp1_fire_time = t
            # move SL to BE on remainder
            if direction == TradeDirection.LONG:
                new_sl = entry_price + be_offset_dist
                if new_sl > sl:
                    sl = new_sl
                    if not be_moved:
                        be_moved = True
                        be_fire_time = t
            else:
                new_sl = entry_price - be_offset_dist
                if new_sl < sl:
                    sl = new_sl
                    if not be_moved:
                        be_moved = True
                        be_fire_time = t

        # BE check (uses favorable extreme of current bar)
        if not be_moved:
            if direction == TradeDirection.LONG:
                profit_dist = fav_high - entry_price
                if profit_dist >= be_trigger_dist:
                    new_sl = entry_price + be_offset_dist
                    if new_sl > sl:
                        sl = new_sl
                        be_moved = True
                        be_fire_time = t
            else:
                profit_dist = entry_price - fav_low
                if profit_dist >= be_trigger_dist:
                    new_sl = entry_price - be_offset_dist
                    if new_sl < sl:
                        sl = new_sl
                        be_moved = True
                        be_fire_time = t

        # Ratchet
        if direction == TradeDirection.LONG:
            profit_dist = peak_price - entry_price
        else:
            profit_dist = entry_price - trough_price
        if profit_dist >= rat_trigger_dist:
            locked = profit_dist * lock_pct
            if direction == TradeDirection.LONG:
                cand_sl = entry_price + locked
                if cand_sl > sl:
                    sl = cand_sl
                    ratchet_hit = True
            else:
                cand_sl = entry_price - locked
                if cand_sl < sl:
                    sl = cand_sl
                    ratchet_hit = True

    if exit_reason == "timeout" and sim_candles:
        # mark-to-market at final close
        last = sim_candles[-1]
        if direction == TradeDirection.LONG:
            exit_price = float(last["bid"]["c"])
        else:
            exit_price = float(last["ask"]["c"])
        exit_time = last["time"]

    # PnL
    if tp1_hit:
        remainder_dist = (exit_price - entry_price) if direction == TradeDirection.LONG else (entry_price - exit_price)
        remainder_R = remainder_dist / R
        realized_R = 0.5 * 1.0 + 0.5 * remainder_R
    else:
        final_dist = (exit_price - entry_price) if direction == TradeDirection.LONG else (entry_price - exit_price)
        realized_R = final_dist / R

    dollar_risked = account_equity_usd * CFG_MGMT["margin_utilization"]
    realized_usd = realized_R * dollar_risked

    res.exit_reason = exit_reason
    res.exit_price = exit_price
    res.realized_R = realized_R
    res.realized_usd = realized_usd
    res.mfe_R = mfe_R
    res.mae_R = mae_R
    res.tp1_hit = tp1_hit
    res.be_moved = be_moved
    res.ratchet_hit = ratchet_hit
    res.be_fire_time = be_fire_time
    res.tp1_fire_time = tp1_fire_time
    res.exit_time = exit_time
    res.reached_be_trigger = reached_be_trigger
    res.be_trigger_time = be_trigger_time
    res.first_adverse_sl_time = first_adverse_sl_time
    return res


def main():
    rows = []
    with open(DATA_CSV) as fh:
        for r in csv.DictReader(fh):
            rows.append(r)

    accepted_rows = [r for r in rows if r["trade_id"] in ACCEPTED_TRADE_IDS]
    print(f"Loaded {len(rows)} trades, {len(accepted_rows)} accepted (target 11)")
    assert len(accepted_rows) == 11, f"expected 11 accepted, got {len(accepted_rows)}"

    scorer = V3HybridScorer()
    tiers: dict[str, str] = {}
    for r in accepted_rows:
        tiers[r["trade_id"]] = score_from_row(scorer, r).tier

    sim_results: dict[str, SimResultM1] = {}
    for i, row in enumerate(accepted_rows):
        tid = row["trade_id"]
        print(f"[{i+1}/{len(accepted_rows)}] {tid} {row['sym']} {row['d']} — M1 sim")
        sim_results[tid] = simulate_trade_m1(row, tiers[tid])

    # --- report ---
    lines = []
    lines.append("# Mr. Scrooge V3 — M1 Backtest (Part B re-run)")
    lines.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
    lines.append("")
    lines.append("## Purpose")
    lines.append("Re-run the management simulation on the 11 V3-accepted trades using **M1** bid+ask candles")
    lines.append("instead of M5 mid. M5 under-resolves intrabar motion and may have made current V3 management")
    lines.append("look worse than it is — especially for BE/ratchet triggers that depend on catching the +0.5R")
    lines.append("favorable extreme before an adverse move trips full SL.")
    lines.append("")
    lines.append("## Environment")
    lines.append("- Granularity: **M1**, price=BAM (bid+ask+mid)")
    lines.append("- Long SL trigger: bid_low ≤ SL.  Short SL trigger: ask_high ≥ SL.")
    lines.append("- Long favorable extreme (MFE/BE trigger): bid_high.  Short: ask_low.")
    lines.append("- Window: open_time - 15min → close_time + 5min (48h hard cap)")
    lines.append("- Management params same as M5 run (config/default.json Phase-4).")
    lines.append("- Part A (scorer tiers) reused from prior run — not re-scored.")
    lines.append("")

    lines.append("## Per-Trade M1 Results")
    lines.append("")
    lines.append("| tid | sym | d | tier | exit | realized_R | MFE_R | MAE_R | tp1 | be | ratchet | be_time | tp1_time |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in accepted_rows:
        tid = r["trade_id"]
        s = sim_results[tid]
        lines.append(
            f"| {tid} | {r['sym']} | {r['d']} | {s.tier} | {s.exit_reason} | {s.realized_R:+.2f} | "
            f"{s.mfe_R:+.2f} | {s.mae_R:+.2f} | {'Y' if s.tp1_hit else '-'} | {'Y' if s.be_moved else '-'} | "
            f"{'Y' if s.ratchet_hit else '-'} | {s.be_fire_time[:19] if s.be_fire_time else '-'} | "
            f"{s.tp1_fire_time[:19] if s.tp1_fire_time else '-'} |"
        )

    # Aggregate
    tot_R_m1 = sum(s.realized_R for s in sim_results.values())
    tot_usd_m1 = sum(s.realized_usd for s in sim_results.values())
    be_n_m1 = sum(1 for s in sim_results.values() if s.be_moved)
    tp1_n_m1 = sum(1 for s in sim_results.values() if s.tp1_hit)
    wins_m1 = sum(1 for s in sim_results.values() if s.realized_R > 0.05)
    losses_m1 = sum(1 for s in sim_results.values() if s.realized_R < -0.05)
    be_only_m1 = sum(1 for s in sim_results.values() if -0.05 <= s.realized_R <= 0.05)

    tot_R_m5 = sum(PRIOR_M5[t]["R"] for t in ACCEPTED_TRADE_IDS)
    tot_usd_m5 = sum(PRIOR_M5[t]["usd"] for t in ACCEPTED_TRADE_IDS)
    be_n_m5 = sum(1 for t in ACCEPTED_TRADE_IDS if PRIOR_M5[t]["be"])
    tp1_n_m5 = sum(1 for t in ACCEPTED_TRADE_IDS if PRIOR_M5[t]["tp1"])

    lines.append("")
    lines.append("## Aggregate — M1 vs M5")
    lines.append("")
    lines.append("| metric | M5 (prior) | M1 (new) | delta |")
    lines.append("|---|---|---|---|")
    lines.append(f"| N BE fired | {be_n_m5} | {be_n_m1} | {be_n_m1 - be_n_m5:+d} |")
    lines.append(f"| N TP1 hit | {tp1_n_m5} | {tp1_n_m1} | {tp1_n_m1 - tp1_n_m5:+d} |")
    lines.append(f"| Total R | {tot_R_m5:+.2f} | {tot_R_m1:+.2f} | {tot_R_m1 - tot_R_m5:+.2f} |")
    lines.append(f"| Total $ @ $400 risk | ${tot_usd_m5:+.2f} | ${tot_usd_m1:+.2f} | ${tot_usd_m1 - tot_usd_m5:+.2f} |")
    lines.append(f"| Wins / Losses / BE | (see prior) | {wins_m1}W / {losses_m1}L / {be_only_m1}BE | — |")
    lines.append("")

    # Side-by-side per trade
    lines.append("## Side-by-Side Per Trade (M5 vs M1)")
    lines.append("")
    lines.append("| tid | M5 exit | M5 R | M5 MFE | M1 exit | M1 R | M1 MFE | M1 MAE | delta R |")
    lines.append("|---|---|---|---|---|---|---|---|---|")
    for r in accepted_rows:
        tid = r["trade_id"]
        p = PRIOR_M5[tid]
        s = sim_results[tid]
        lines.append(
            f"| {tid} | {p['exit_reason']} | {p['R']:+.2f} | {p['mfe']:+.2f} | "
            f"{s.exit_reason} | {s.realized_R:+.2f} | {s.mfe_R:+.2f} | {s.mae_R:+.2f} | "
            f"{s.realized_R - p['R']:+.2f} |"
        )
    lines.append("")

    # Special diagnostic for the 4 full-SL losers
    lines.append("## Diagnostic: The 4 Prior M5 Full-SL Losers")
    lines.append("")
    lines.append("The key question: on M1 tick-finer data, did these trades reach +0.5R (BE trigger)")
    lines.append("**before** the adverse low that would have tripped the original -1R SL?")
    lines.append("")
    lines.append("| tid | sym | reached +0.5R? | BE-trigger time | first adverse -1R time | order | M1 MFE | M1 MAE | M1 exit |")
    lines.append("|---|---|---|---|---|---|---|---|---|")
    for tid in ["5873","5591","5509","5438"]:
        r = next(rr for rr in accepted_rows if rr["trade_id"] == tid)
        s = sim_results[tid]
        if s.be_trigger_time and s.first_adverse_sl_time:
            order = "BE first (saved)" if s.be_trigger_time <= s.first_adverse_sl_time else "SL first (unsavable)"
        elif s.be_trigger_time and not s.first_adverse_sl_time:
            order = "BE only (no full SL hit)"
        elif s.first_adverse_sl_time and not s.be_trigger_time:
            order = "SL only (never reached BE trigger)"
        else:
            order = "neither in window"
        lines.append(
            f"| {tid} | {r['sym']} | {'YES' if s.reached_be_trigger else 'NO'} | "
            f"{s.be_trigger_time[:19] if s.be_trigger_time else '-'} | "
            f"{s.first_adverse_sl_time[:19] if s.first_adverse_sl_time else '-'} | "
            f"{order} | {s.mfe_R:+.2f} | {s.mae_R:+.2f} | {s.exit_reason} |"
        )

    # Conclusion
    lines.append("")
    lines.append("## Conclusion")
    lines.append("")
    saved = sum(1 for tid in PRIOR_M5_SL_LOSERS
                if sim_results[tid].be_trigger_time and
                (not sim_results[tid].first_adverse_sl_time or
                 sim_results[tid].be_trigger_time <= sim_results[tid].first_adverse_sl_time))
    delta_R = tot_R_m1 - tot_R_m5
    if delta_R > 0.5 and saved >= 2:
        conclusion = (
            f"The M5 simulation was **under-resolving** intrabar action. On M1 data, "
            f"{saved}/4 prior full-SL losers actually reached the +0.5R BE trigger "
            f"before their adverse move, meaning BE would have saved them on tick-level execution. "
            f"Net realized R improves by {delta_R:+.2f}. Current V3 management thresholds are not "
            f"inherently too tight — the prior M5 sim made them look that way by missing the "
            f"favorable extreme inside 5-minute bars. **Recommendation: keep current be_trigger_r=0.5, "
            f"be_offset_r=0.1; do NOT loosen.** The M5 framework itself is the artifact."
        )
    elif delta_R > 0 and saved >= 1:
        conclusion = (
            f"Mixed signal. M1 shows {saved}/4 prior-SL trades reached BE trigger first "
            f"(net R {delta_R:+.2f}). Some of the M5 result is genuine adverse follow-through, "
            f"some was under-resolution. Current thresholds are plausibly correct but a larger "
            f"out-of-sample dataset is needed before any tuning move."
        )
    else:
        conclusion = (
            f"M1 data does not rescue the losers: {saved}/4 reached BE trigger before adverse "
            f"full-SL move. Net realized R change: {delta_R:+.2f}. This suggests the current "
            f"management thresholds (be_trigger_r=0.5, tp1_r=1.0) may be too tight for this "
            f"dataset's volatility profile, OR the scorer is accepting trades whose structure "
            f"does not actually produce favorable excursions. Need larger out-of-sample dataset "
            f"before recalibrating — this dataset is already overfit per prior caveats."
        )
    lines.append(conclusion)
    lines.append("")

    # Recommendation based on MFE/MAE
    lines.append("## MFE / MAE Distribution on M1")
    lines.append("")
    mfes = [s.mfe_R for s in sim_results.values() if s.mfe_R > 0]
    maes = [s.mae_R for s in sim_results.values() if s.mae_R < 0]
    if mfes:
        mfes_s = sorted(mfes)
        lines.append(f"- MFE_R (n={len(mfes)}): min={mfes_s[0]:+.2f} median={mfes_s[len(mfes_s)//2]:+.2f} "
                     f"p75={mfes_s[len(mfes_s)*3//4]:+.2f} max={mfes_s[-1]:+.2f}")
    if maes:
        maes_s = sorted(maes)
        lines.append(f"- MAE_R (n={len(maes)}): min={maes_s[0]:+.2f} p25={maes_s[len(maes_s)//4]:+.2f} "
                     f"median={maes_s[len(maes_s)//2]:+.2f} max={maes_s[-1]:+.2f}")
    ge05 = sum(1 for s in sim_results.values() if s.mfe_R >= 0.5)
    ge10 = sum(1 for s in sim_results.values() if s.mfe_R >= 1.0)
    lines.append(f"- Trades with MFE ≥ 0.5R (BE trigger reachable): **{ge05}/11**")
    lines.append(f"- Trades with MFE ≥ 1.0R (TP1 reachable): **{ge10}/11**")
    lines.append("")
    lines.append("## Caveats")
    lines.append("- M1 is still a 60s aggregation — not true tick — so intrabar ordering is still an assumption "
                 "(conservative: SL before TP1 when both in same bar).")
    lines.append("- Spread cost not modeled; slippage not modeled (fills at exact SL/TP).")
    lines.append("- Same dataset-overfit caveat applies: scorer was calibrated on these 50 trades.")
    lines.append("- N=11 accepted; directional signal only.")
    lines.append("")

    out = "\n".join(lines)
    print(out)
    REPORT_PATH.write_text(out)
    print(f"\nReport saved to {REPORT_PATH}")

if __name__ == "__main__":
    main()
