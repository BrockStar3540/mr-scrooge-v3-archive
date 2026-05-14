"""Weekly review of observe-mode micro-bot shadow signals.

Reads:
  data/observe-tf6-usdjpy.jsonl       (TF6_short USDJPY observer)
  data/observe-tf6-long-usdmxn.jsonl  (TF6_long USDMXN observer)

Reports per bot:
  - signals total / this week / this month
  - mean spread at fire vs. research baseline
  - hour-of-day distribution
  - weekday distribution
  - realized R for fires whose forward window has now elapsed (using
    dukascopy cache if available, else OANDA broker fetch)
  - comparison vs research holdout distribution (research stats hard-coded
    from the discovery commits)

Usage (on EC2 or any machine with access to the JSONLs):
  python3 observe_weekly_review.py [--data-dir /path/to/data]

Designed to be run weekly. Idempotent / read-only.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

import pandas as pd
import numpy as np

# Hard-coded research-holdout reference for each observer (from MICRO_BOTS.md)
RESEARCH = {
    "TF6_short_USD_JPY": {
        "symbol": "USD_JPY",
        "direction": "short",
        "research_recent_n": 23,
        "research_recent_mean_R": 1.19,
        "research_recent_CI_lo": 0.67,
        "research_holdout_n": 100,
        "research_holdout_mean_R": 0.32,
        "research_baseline_spread_pips": 0.7,
        "discovery_methodology": "strict_classifier_min_leaf_60_WR40",
        "permutation_p_value": 0.2,
        "expected_fires_per_week": 2.0,
    },
    "TF6_long_USD_MXN": {
        "symbol": "USD_MXN",
        "direction": "long",
        "research_recent_n": 36,
        "research_recent_mean_R": 0.56,
        "research_recent_CI_lo": 0.06,
        "research_holdout_n": 60,
        "research_holdout_mean_R": 0.38,
        "research_baseline_spread_pips": 12.0,
        "discovery_methodology": "loosened_regressor_min_leaf_30_no_WR_gate",
        "permutation_p_value": None,
        "expected_fires_per_week": 1.5,
    },
}

DEFAULT_FILES = {
    "TF6_short_USD_JPY": "data/observe-tf6-usdjpy.jsonl",
    "TF6_long_USD_MXN":  "data/observe-tf6-long-usdmxn.jsonl",
}


def load_signals(jsonl_path: Path) -> pd.DataFrame:
    if not jsonl_path.exists():
        return pd.DataFrame()
    rows = []
    with open(jsonl_path) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    if not rows: return pd.DataFrame()
    df = pd.json_normalize(rows)
    df["bar_ts"] = pd.to_datetime(df["bar_ts"], utc=True)
    df["logged_at"] = pd.to_datetime(df["logged_at"], utc=True)
    return df.sort_values("bar_ts").reset_index(drop=True)


def forward_walk_outcome(pair: str, entry_ts: pd.Timestamp, entry_px: float, stop: float, tp_2r: float, direction: str, duka_dir: Path, max_bars: int = 300) -> dict | None:
    """Walk forward through M5 bars after entry. Return realized_R or None if data not yet available."""
    # Find the M5 jsonl files spanning entry_ts
    bars = []
    for f in sorted(duka_dir.glob(f"{pair}_M5_*.jsonl")):
        # Quick filename-based date check
        for line in open(f):
            try:
                d = json.loads(line)
                ts = pd.to_datetime(d["time"], utc=True)
                if ts < entry_ts: continue
                bars.append({
                    "ts": ts,
                    "high": (d["high_bid"] + d["high_ask"]) / 2,
                    "low":  (d["low_bid"]  + d["low_ask"])  / 2,
                })
                if len(bars) > max_bars: break
            except Exception:
                continue
        if len(bars) > max_bars: break
    if len(bars) < 5: return None
    risk = abs(entry_px - stop)
    if risk <= 0: return None
    mfe = mae = 0.0
    for bar in bars[:max_bars]:
        if direction == "long":
            fav = bar["high"] - entry_px
            adv = entry_px - bar["low"]
            if fav > mfe: mfe = fav
            if adv > mae: mae = adv
            if bar["low"] <= stop:
                return {"realized_R": -1.0, "exit_reason": "stop", "mfe_R": mfe/risk, "mae_R": mae/risk}
            if bar["high"] >= tp_2r:
                return {"realized_R": 2.0, "exit_reason": "tp", "mfe_R": mfe/risk, "mae_R": mae/risk}
        else:
            fav = entry_px - bar["low"]
            adv = bar["high"] - entry_px
            if fav > mfe: mfe = fav
            if adv > mae: mae = adv
            if bar["high"] >= stop:
                return {"realized_R": -1.0, "exit_reason": "stop", "mfe_R": mfe/risk, "mae_R": mae/risk}
            if bar["low"] <= tp_2r:
                return {"realized_R": 2.0, "exit_reason": "tp", "mfe_R": mfe/risk, "mae_R": mae/risk}
    return {"realized_R": 0.0, "exit_reason": "time", "mfe_R": mfe/risk, "mae_R": mae/risk}


def review_observer(bot_key: str, df: pd.DataFrame, duka_dir: Path) -> dict:
    """Build a per-bot summary dict."""
    cfg = RESEARCH[bot_key]
    now = datetime.now(timezone.utc)
    week_ago = now - timedelta(days=7)
    month_ago = now - timedelta(days=30)

    summary = {"bot": bot_key, **{k: cfg[k] for k in cfg}}
    if df.empty:
        summary.update({"n_total": 0, "n_week": 0, "n_month": 0, "status": "no_signals_yet"})
        return summary

    summary["n_total"] = len(df)
    summary["n_week"] = int((df["bar_ts"] >= week_ago).sum())
    summary["n_month"] = int((df["bar_ts"] >= month_ago).sum())
    summary["first_signal"] = df["bar_ts"].min().isoformat()
    summary["last_signal"] = df["bar_ts"].max().isoformat()

    # Spread at fire (if logged)
    if "spread_at_fire_pips" in df.columns:
        sp = pd.to_numeric(df["spread_at_fire_pips"], errors="coerce").dropna()
        if len(sp) > 0:
            summary["spread_at_fire_mean_pips"] = round(float(sp.mean()), 3)
            summary["spread_at_fire_median_pips"] = round(float(sp.median()), 3)
            summary["spread_at_fire_p95_pips"] = round(float(sp.quantile(0.95)), 3)
            summary["spread_vs_research_ratio"] = round(float(sp.mean() / cfg["research_baseline_spread_pips"]), 2)

    # Hour and weekday distributions
    hours = df["bar_ts"].dt.hour.value_counts().sort_index()
    summary["hour_distribution"] = {int(h): int(n) for h, n in hours.items()}
    wd = df["bar_ts"].dt.weekday.value_counts().sort_index()
    summary["weekday_distribution"] = {int(w): int(n) for w, n in wd.items()}

    # Forward-walk realized R for fires whose 25h window has elapsed
    if duka_dir.exists():
        cutoff = now - timedelta(hours=25)
        resolvable = df[df["bar_ts"] < cutoff].copy()
        outcomes = []
        for _, sig in resolvable.iterrows():
            o = forward_walk_outcome(cfg["symbol"], sig["bar_ts"], sig["entry"], sig["stop"], sig["tp_2r"], cfg["direction"], duka_dir)
            if o is not None:
                outcomes.append(o)
        if outcomes:
            r = np.array([o["realized_R"] for o in outcomes])
            summary["live_n_resolved"] = len(r)
            summary["live_mean_R"] = round(float(r.mean()), 4)
            summary["live_win_rate"] = round(float((r > 0).mean()), 4)
            if len(r) >= 5:
                # bootstrap CI lower
                rng = np.random.default_rng(42)
                idx = rng.integers(0, len(r), size=(500, len(r)))
                ci_lo = float(np.quantile(r[idx].mean(axis=1), 0.025))
                summary["live_CI_lower"] = round(ci_lo, 4)
                summary["live_research_ratio"] = round(float(r.mean()) / cfg["research_recent_mean_R"], 2)

    # Status verdict
    n_needed_for_judgment = 10
    if summary.get("live_n_resolved", 0) >= n_needed_for_judgment:
        live_mr = summary.get("live_mean_R", 0)
        research_mr = cfg["research_recent_mean_R"]
        if live_mr > research_mr * 0.5 and summary.get("live_CI_lower", -99) > 0:
            summary["status"] = "matching_research"
        elif live_mr > 0:
            summary["status"] = "underperforming_research_but_positive"
        else:
            summary["status"] = "live_negative"
    else:
        summary["status"] = f"too_few_resolved_signals_{summary.get('live_n_resolved', 0)}_of_{n_needed_for_judgment}"

    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path,
                        default=Path("/home/ubuntu/mr-scrooge-v3/data"),
                        help="Directory containing observer JSONL files")
    parser.add_argument("--duka-dir", type=Path,
                        default=Path("/data/oanda-bot-trainer-cache/dukascopy"),
                        help="Dukascopy M5 cache root (subdirs per pair)")
    parser.add_argument("--out", type=Path,
                        default=Path("/tmp/observer_weekly_review.json"),
                        help="Where to write the review JSON")
    args = parser.parse_args()

    review = {"generated_at": datetime.now(timezone.utc).isoformat(), "bots": {}}
    for bot, rel_path in DEFAULT_FILES.items():
        jsonl_path = args.data_dir / Path(rel_path).name
        df = load_signals(jsonl_path)
        duka_pair_dir = args.duka_dir / RESEARCH[bot]["symbol"]
        s = review_observer(bot, df, duka_pair_dir if duka_pair_dir.exists() else Path("/nonexistent"))
        review["bots"][bot] = s

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w") as f:
        json.dump(review, f, indent=2, default=str)
    print(json.dumps(review, indent=2, default=str))


if __name__ == "__main__":
    main()
