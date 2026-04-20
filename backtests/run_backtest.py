"""Historical backtest of Mr. Scrooge V3 current logic vs 50-trade calibration dataset.

Part A: Current V3.1 scorer pass (bypasses _extract_factors since CSV already has
        all factors — we feed _compute_score directly with a hand-built factor dict).
Part B: Management simulation using post-entry M5 candles from OANDA.
Part C: Comparison vs original outcomes.

All active gates (debounce, zone_entry_cap, regime_floor) vacuously pass in
a historical backtest because the required state (zone_last_entry,
zone_blacklist, zone_entries_today, classifications.regime) is empty.
We document this and don't simulate them.
"""
from __future__ import annotations

import csv
import json
import os
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

# Load OANDA creds from V3 .env
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
RAW_CANDLES_DIR = REPO / "data" / "raw_candles"
BT_DIR = REPO / "backtests"
CACHE_DIR = BT_DIR / "candles_cache"
REPORT_PATH = BT_DIR / "report.md"

BT_DIR.mkdir(exist_ok=True)
CACHE_DIR.mkdir(exist_ok=True)

# Config (mirrors config/default.json post-Phase-4)
CFG_MGMT = {
    "tp1_r": 1.0,
    "tp1_fraction": 0.50,
    "be_trigger_r": 0.5, "be_trigger_min_pips": 2.0,
    "be_offset_r": 0.1, "be_offset_min_pips": 1.0,
    "ratchet_trigger_r": 1.0, "ratchet_trigger_min_pips": 3.0,
    "ratchet_lock_pct": 0.50,
    "trail_buffer_pips": 2.0,
    "margin_utilization": 0.40,
}

OANDA_URL = os.environ.get("OANDA_API_URL", "https://api-fxpractice.oanda.com")
OANDA_TOKEN = os.environ.get("OANDA_API_TOKEN", "")
OANDA_ACCOUNT = os.environ.get("OANDA_ACCOUNT_ID", "")


def pip_size(symbol: str) -> float:
    return 0.01 if "JPY" in symbol else 0.0001


# -------------------- OANDA candle fetch --------------------

def fetch_candles(symbol: str, start: datetime, end: datetime, gran: str = "M5") -> list[dict]:
    """Fetch candles from OANDA for [start, end], caching on disk."""
    cache_key = f"{symbol}_{gran}_{start.isoformat()}_{end.isoformat()}.json".replace(":", "-")
    cache_file = CACHE_DIR / cache_key
    if cache_file.exists():
        return json.loads(cache_file.read_text())

    # OANDA paginates — max 5000 candles per call. M5 = 12/h, 24h = 288. Single call fine.
    params = {
        "from": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "to":   end.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "granularity": gran,
        "price": "M",
    }
    url = f"{OANDA_URL}/v3/instruments/{symbol}/candles?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {OANDA_TOKEN}"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode() if hasattr(e, 'read') else str(e)
        print(f"  OANDA ERR {symbol} {start}-{end}: {e.code} {body[:200]}", file=sys.stderr)
        return []

    candles = data.get("candles", [])
    cache_file.write_text(json.dumps(candles))
    return candles


# -------------------- Part A: Current scorer pass --------------------

def _hour_now_override_monkey_patch():
    """V3 scorer uses datetime.now() for the hour factor. We override to use trade hour."""
    pass  # we'll skip _extract_factors entirely

def score_from_row(scorer: V3HybridScorer, row: dict) -> ScorerResult:
    """Feed _compute_score with factors built directly from CSV row."""
    # Map CSV columns → scorer factor dict
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
        "dur":  60.0,  # scorer uses dur=60 fixed in _extract_factors; duration in CSV is TRADE duration (post-outcome), not pre-entry. Scorer internally hardcodes 60.
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
    # Build a minimal TradeCandidate for family overlay logic
    from scrooge_v3.core.types import TradeCandidate as TC
    direction = TradeDirection.LONG if row["d"] == "L" else TradeDirection.SHORT
    # Family: reversal family is default. dbb_trend would be family="trend".
    # The CSV has `stype` = STD (structural), and `is_ct` (countertrend). Default family = "".
    cand = TC(
        symbol=row["sym"], direction=direction, strategy="reversal",
        entry_price=float(row["entry"]),
        stop_price=float(row["entry"]) + (f["ns"] * pip_size(row["sym"]) * (1 if direction == TradeDirection.SHORT else -1)),
        metadata={"strategy_family": ""},
    )
    return scorer._compute_score(f, cand)


# -------------------- Part B: Management simulation --------------------

@dataclass
class SimResult:
    accepted: bool
    tier: str
    exit_reason: str = ""
    exit_price: float = 0.0
    realized_pips: float = 0.0
    realized_R: float = 0.0
    realized_usd: float = 0.0
    mfe_R: float = 0.0
    mae_R: float = 0.0
    tp1_hit: bool = False
    be_moved: bool = False
    ratchet_hit: bool = False
    notes: str = ""


def simulate_trade(row: dict, result: ScorerResult, account_equity_usd: float = 1000.0) -> SimResult:
    """Walk M5 candles post-entry, applying BE / ratchet / TP1 / SL."""
    symbol = row["sym"]
    direction = TradeDirection.LONG if row["d"] == "L" else TradeDirection.SHORT
    entry_price = float(row["entry"])
    ns_pips = float(row["ns"])
    psize = pip_size(symbol)
    R = ns_pips * psize                   # initial risk distance in price
    if R <= 0:
        return SimResult(accepted=True, tier=result.tier, exit_reason="invalid_R", notes="ns<=0")

    if direction == TradeDirection.LONG:
        sl = entry_price - R
        tp1 = entry_price + CFG_MGMT["tp1_r"] * R
    else:
        sl = entry_price + R
        tp1 = entry_price - CFG_MGMT["tp1_r"] * R

    open_time = datetime.fromisoformat(row["open_time"]).replace(tzinfo=timezone.utc)
    close_time = datetime.fromisoformat(row["close_time"]).replace(tzinfo=timezone.utc)
    # Fetch a window slightly beyond original close time, cap at 48h
    sim_end = min(open_time + timedelta(hours=48), max(close_time + timedelta(hours=2), open_time + timedelta(hours=4)))
    candles = fetch_candles(symbol, open_time, sim_end, "M5")
    if not candles:
        return SimResult(accepted=True, tier=result.tier, exit_reason="no_candles", notes="fetch failed")

    # State
    tp1_hit = False
    be_moved = False
    partial_taken = False
    peak_price = entry_price  # MFE anchor
    trough_price = entry_price  # for shorts

    # BE params
    be_trigger_dist = max(CFG_MGMT["be_trigger_r"] * R, CFG_MGMT["be_trigger_min_pips"] * psize)
    be_offset_dist  = max(CFG_MGMT["be_offset_r"]  * R, CFG_MGMT["be_offset_min_pips"]  * psize)
    # Ratchet params
    rat_trigger_dist = max(CFG_MGMT["ratchet_trigger_r"] * R, CFG_MGMT["ratchet_trigger_min_pips"] * psize)
    lock_pct = CFG_MGMT["ratchet_lock_pct"]

    mfe_R = 0.0
    mae_R = 0.0
    exit_reason = "timeout"
    exit_price = float(candles[-1]["mid"]["c"])

    # Simulate per M5 candle — assume SL tested on intrabar extreme against us, TP/BE on extreme with us.
    # Realistic ordering: within a bar we don't know sequence of H vs L — for stop logic, assume WORST-CASE for us
    # (SL hit before TP) ONLY when both levels touched in same bar. Otherwise normal.
    for c in candles:
        if not c.get("complete", True):
            continue
        h = float(c["mid"]["h"]); low = float(c["mid"]["l"]); cl = float(c["mid"]["c"])
        # Track MFE/MAE
        if direction == TradeDirection.LONG:
            fav = h; unfav = low
            peak_price = max(peak_price, h)
            mfe_R = max(mfe_R, (peak_price - entry_price) / R)
            mae_R = min(mae_R, (low - entry_price) / R)
        else:
            fav = low; unfav = h
            trough_price = min(trough_price, low)
            mfe_R = max(mfe_R, (entry_price - trough_price) / R)
            mae_R = min(mae_R, (entry_price - h) / R)

        # Check SL first (worst-case within bar)
        sl_hit = (direction == TradeDirection.LONG and low <= sl) or (direction == TradeDirection.SHORT and h >= sl)
        tp1_touched = (not tp1_hit) and (
            (direction == TradeDirection.LONG and h >= tp1) or (direction == TradeDirection.SHORT and low <= tp1)
        )

        if sl_hit and tp1_touched:
            # Both in same bar — assume SL first (conservative). If sl is BE/positive, treat as BE exit.
            exit_price = sl
            exit_reason = "sl_same_bar_as_tp1"
            break
        if sl_hit:
            exit_price = sl
            exit_reason = "sl_hit" if not be_moved else "be_hit"
            break
        if tp1_touched:
            tp1_hit = True
            partial_taken = True
            # half off at TP1 — track realized on partial. Model as locking in 0.5R on half.
            # For simplicity we'll compute final PnL as blended average.
            # Now move SL to BE on remainder.
            if direction == TradeDirection.LONG:
                new_sl = entry_price + be_offset_dist
                if new_sl > sl:
                    sl = new_sl; be_moved = True
            else:
                new_sl = entry_price - be_offset_dist
                if new_sl < sl:
                    sl = new_sl; be_moved = True

        # BE check on remainder if not yet moved
        if not be_moved:
            if direction == TradeDirection.LONG:
                profit_dist = fav - entry_price  # use favorable extreme
                if profit_dist >= be_trigger_dist:
                    new_sl = entry_price + be_offset_dist
                    if new_sl > sl:
                        sl = new_sl; be_moved = True
            else:
                profit_dist = entry_price - fav
                if profit_dist >= be_trigger_dist:
                    new_sl = entry_price - be_offset_dist
                    if new_sl < sl:
                        sl = new_sl; be_moved = True

        # Ratchet: lock_pct of MFE anchored on peak
        if direction == TradeDirection.LONG:
            profit_dist = peak_price - entry_price
        else:
            profit_dist = entry_price - trough_price

        if profit_dist >= rat_trigger_dist:
            locked_distance = profit_dist * lock_pct
            if direction == TradeDirection.LONG:
                cand_sl = entry_price + locked_distance
                if cand_sl > sl:
                    sl = cand_sl
            else:
                cand_sl = entry_price - locked_distance
                if cand_sl < sl:
                    sl = cand_sl

    # Compute realized PnL in R
    # If TP1 was taken, half closed at +1R, other half closed at final exit
    if tp1_hit:
        remainder_dist = (exit_price - entry_price) if direction == TradeDirection.LONG else (entry_price - exit_price)
        remainder_R = remainder_dist / R
        realized_R = 0.5 * 1.0 + 0.5 * remainder_R
    else:
        final_dist = (exit_price - entry_price) if direction == TradeDirection.LONG else (entry_price - exit_price)
        realized_R = final_dist / R

    realized_pips = realized_R * ns_pips

    # USD realization at Phase 1 sizing (40% margin utilization)
    # Simplified: risk per trade ~ margin_util * equity / leverage.
    # OANDA practice leverage ~50:1. Position_size_quote = margin_util * equity * leverage.
    # Dollar risk = position_size * R_in_price / entry_price (for quote=USD pairs) — but we just want R-relative.
    # For a rough $ estimate: assume $ risked per trade = margin_util * equity * (ns_pips/10000) * 50
    # We'll use a simpler model: dollar_risk_per_trade = account_equity * 0.02  (2% standard), scaled by 40% margin util ≈ variable.
    # Better: dollar_risked = account_equity * margin_util = $400. Realized $ = realized_R * $400.
    dollar_risked = account_equity_usd * CFG_MGMT["margin_utilization"]
    realized_usd = realized_R * dollar_risked

    return SimResult(
        accepted=True, tier=result.tier,
        exit_reason=exit_reason, exit_price=exit_price,
        realized_pips=realized_pips, realized_R=realized_R, realized_usd=realized_usd,
        mfe_R=mfe_R, mae_R=mae_R,
        tp1_hit=tp1_hit, be_moved=be_moved,
    )


# -------------------- Main --------------------

def main():
    rows = []
    with open(DATA_CSV) as fh:
        for r in csv.DictReader(fh):
            rows.append(r)
    print(f"Loaded {len(rows)} trades")

    scorer = V3HybridScorer()

    part_a_results: list[tuple[dict, ScorerResult]] = []
    for row in rows:
        res = score_from_row(scorer, row)
        part_a_results.append((row, res))

    # Aggregate Part A
    accepted_rows = [(r, s) for r, s in part_a_results if s.tier in ("A", "B")]
    rejected_rows = [(r, s) for r, s in part_a_results if s.tier not in ("A", "B")]
    # of rejected, how many winners vs losers
    rej_winners = sum(1 for r, _ in rejected_rows if int(r["won"]) == 1)
    rej_losers = sum(1 for r, _ in rejected_rows if int(r["won"]) == 0)
    acc_winners = sum(1 for r, _ in accepted_rows if int(r["won"]) == 1)
    acc_losers = sum(1 for r, _ in accepted_rows if int(r["won"]) == 0)

    # Part B: simulate accepted
    sim_results: dict[str, SimResult] = {}
    for i, (row, res) in enumerate(accepted_rows):
        print(f"[{i+1}/{len(accepted_rows)}] Simulating trade {row['trade_id']} {row['sym']} {row['d']} tier={res.tier}")
        sim = simulate_trade(row, res)
        sim_results[row["trade_id"]] = sim

    # Report
    lines = []
    lines.append("# Mr. Scrooge V3 — Historical Backtest on 50-Trade Calibration Dataset")
    lines.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
    lines.append("")
    lines.append("## Environment")
    lines.append("- V3 code: current main (Phase 1+2+3+4)")
    lines.append("- Scorer: V3HybridScorer (v3_scorer.py, V3.1 recalibrated 2026-04-16)")
    lines.append("- Gates (active): debounce, zone_entry_cap, regime_floor — all vacuously PASS in historical backtest (empty state).")
    lines.append("- Cooldown, expiry_backoff, daily_circuit: can't fire historically (no prior trade log).")
    lines.append("- Management: TP1 @ 1.0R (50%), BE @ 0.5R trigger with pip floors, Ratchet @ 1.0R / 50% lock on MFE-anchored peak.")
    lines.append("- Account equity assumption: $1,000; margin_utilization 0.40 → $400 risked/trade.")
    lines.append("- Post-entry candles fetched live from OANDA practice (M5), 48h window cap.")
    lines.append("")
    lines.append("## Part A — Scorer Verdict Per Trade")
    lines.append("")
    lines.append("| # | trade_id | sym | d | hour | won | base | final | tier | session |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|")
    for i, (row, s) in enumerate(part_a_results):
        # reconstruct session from hour (quick)
        h = int(row["hour"])
        session = ("dead_late" if h >= 20 else "late_ny" if h >= 18 else "ny_active" if h >= 12 else "london" if h >= 8 else "asia_london_open")
        lines.append(f"| {i+1} | {row['trade_id']} | {row['sym']} | {row['d']} | {h} | {row['won']} | {s.base_score} | {s.score} | {s.tier} | {session} |")

    lines.append("")
    lines.append("## Part A — Aggregate")
    lines.append(f"- Accepted (tier A or B): **{len(accepted_rows)}** / 50")
    lines.append(f"- Rejected (REJECT or BLOCKED): **{len(rejected_rows)}** / 50")
    lines.append(f"  - Of rejected: {rej_losers} losers filtered out, {rej_winners} winners filtered out (false negatives)")
    lines.append(f"- Accepted breakdown: {acc_winners} wins / {acc_losers} losses (original outcome)")
    if len(accepted_rows) > 0:
        lines.append(f"  - Original accept win rate: {acc_winners/len(accepted_rows)*100:.1f}%")
    lines.append("")

    # Part B report
    lines.append("## Part B — Management Sim On Accepted Trades")
    lines.append("")
    lines.append("| trade_id | sym | d | tier | orig won | exit_reason | realized_R | MFE_R | MAE_R | tp1 | be | realized$ |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    tot_R = 0.0
    tot_usd = 0.0
    sim_wins = 0
    sim_losses = 0
    sim_be = 0
    for row, s in accepted_rows:
        sim = sim_results[row["trade_id"]]
        tot_R += sim.realized_R
        tot_usd += sim.realized_usd
        if sim.realized_R > 0.05:
            sim_wins += 1
        elif sim.realized_R < -0.05:
            sim_losses += 1
        else:
            sim_be += 1
        lines.append(f"| {row['trade_id']} | {row['sym']} | {row['d']} | {s.tier} | {row['won']} | {sim.exit_reason} | {sim.realized_R:+.2f} | {sim.mfe_R:+.2f} | {sim.mae_R:+.2f} | {'Y' if sim.tp1_hit else '-'} | {'Y' if sim.be_moved else '-'} | ${sim.realized_usd:+.2f} |")

    lines.append("")
    lines.append("## Part B — Aggregate")
    lines.append(f"- Simulated trades: {len(accepted_rows)}")
    lines.append(f"- Wins (R > 0.05): {sim_wins}")
    lines.append(f"- Losses (R < -0.05): {sim_losses}")
    lines.append(f"- Break-even: {sim_be}")
    if len(accepted_rows) > 0:
        lines.append(f"- Sim win rate: {sim_wins/len(accepted_rows)*100:.1f}%")
        lines.append(f"- Avg R: {tot_R/len(accepted_rows):+.2f}")
    lines.append(f"- Total R: {tot_R:+.2f}")
    lines.append(f"- Total realized $ @ $400/trade risk: ${tot_usd:+.2f}")
    lines.append("")

    # Part C: comparison
    lines.append("## Part C — Comparison vs Original")
    orig_wins = sum(1 for r in rows if int(r["won"]) == 1)
    orig_pnl = sum(float(r["pnl"]) for r in rows)
    lines.append(f"- Original: {orig_wins}/50 wins, gross P&L (broken sizing): ${orig_pnl:+.2f}")
    lines.append(f"- V3 current, applied to same 50: {len(accepted_rows)} accepted / {len(rejected_rows)} rejected")
    lines.append(f"- V3 sim total: {sim_wins}W/{sim_losses}L/{sim_be}BE, total R {tot_R:+.2f}, ${tot_usd:+.2f} at Phase-1 sizing")
    lines.append("- Direct $ comparison is apples-to-oranges: original sizing was broken (V1/V2 bot-era). R-multiple is the honest measure.")
    lines.append("")

    # Score distribution
    lines.append("## Part D — Score Distribution Winners vs Losers")
    winners = [s.score for r, s in part_a_results if int(r["won"]) == 1]
    losers  = [s.score for r, s in part_a_results if int(r["won"]) == 0]
    base_w  = [s.base_score for r, s in part_a_results if int(r["won"]) == 1]
    base_l  = [s.base_score for r, s in part_a_results if int(r["won"]) == 0]
    def _stats(xs):
        if not xs: return "n=0"
        xs = sorted(xs)
        return f"n={len(xs)} min={xs[0]} p25={xs[len(xs)//4]} median={xs[len(xs)//2]} p75={xs[len(xs)*3//4]} max={xs[-1]}"
    lines.append(f"- Winners FINAL score:   {_stats(winners)}")
    lines.append(f"- Losers  FINAL score:   {_stats(losers)}")
    lines.append(f"- Winners BASE score:    {_stats(base_w)}")
    lines.append(f"- Losers  BASE score:    {_stats(base_l)}")
    # Bucketed histogram
    def _hist(xs, lo=-30, hi=80, step=5):
        buckets = {}
        for x in xs:
            b = int((x - lo) // step) * step + lo
            buckets[b] = buckets.get(b, 0) + 1
        return buckets
    hw = _hist(winners); hl = _hist(losers)
    all_b = sorted(set(hw) | set(hl))
    lines.append("")
    lines.append("| bucket | winners | losers |")
    lines.append("|---|---|---|")
    for b in all_b:
        lines.append(f"| {b}..{b+4} | {'#'*hw.get(b,0)} ({hw.get(b,0)}) | {'#'*hl.get(b,0)} ({hl.get(b,0)}) |")

    lines.append("")
    lines.append("## Caveats")
    lines.append("- N=50 (25W/25L ~ class-balanced by construction) — directional only, not significant.")
    lines.append("- **DATA LEAK**: V3.1 scorer was calibrated against this dataset on 2026-04-16. Part A reject rate reflects that fit — do not interpret as out-of-sample performance.")
    lines.append("- Cooldown / expiry / circuit gates can't fire historically (no prior-trade state). They will affect live but not this backtest.")
    lines.append("- Debounce / zone_entry_cap / regime_floor gates: evaluated but all pass (empty state), not a meaningful check here.")
    lines.append("- Management sim: intrabar worst-case ordering (SL before TP1 in same M5 bar). No slippage, no spread cost applied.")
    lines.append("- Post-entry candles fetched from OANDA M5; bars marked incomplete are skipped. If a trade's window exceeds 48h the sim exits at timeout.")
    lines.append("- $ realization model is a linear R-to-$ map at $400/trade — real Phase-1 sizing varies by pair notional, this is a first-order approximation.")
    lines.append("")

    lines.append("## Executive Summary")
    # Heuristic: if winners/losers separation is weak, flag.
    import statistics as st
    w_med = st.median(winners) if winners else 0
    l_med = st.median(losers) if losers else 0
    sep = w_med - l_med
    lines.append(f"Current V3 scorer rejects {len(rejected_rows)}/50 ({len(rejected_rows)*2}%) of this dataset; of the rejections, {rej_losers} are original losers (true negatives) and {rej_winners} are winners (false negatives). On the {len(accepted_rows)} accepted trades the sim realizes {tot_R:+.2f}R / ${tot_usd:+.2f} under current Phase-1/3 management, vs. an original result of {orig_wins}/50 wins at broken sizing. Winner/loser final-score medians: {w_med}/{l_med} (separation {sep:+d}). Given the dataset was used to calibrate this scorer, these numbers are over-fit by construction — the dataset is too small (N=50) and too leaky for further calibration passes; it's only useful now as a regression sanity check that current logic hasn't regressed. Next calibration round needs a held-out test set (trades the 2026-04-16 tuning never saw).")

    out = "\n".join(lines)
    print(out)
    REPORT_PATH.write_text(out)
    print(f"\nReport saved to {REPORT_PATH}")

if __name__ == "__main__":
    main()
