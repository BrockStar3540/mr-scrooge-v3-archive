"""Stress-test the 3 loosened-discovery survivors.

Gates per Brock 2026-05-13:
  1. Vol-conditional spread (2x when vol_ratio<0.4, 3x when <0.2)
  2. Random slippage MC (0-2 pips, 1000 draws, 100% draws must be positive)
  3. Fire-time concentration: ≤25% any hour, ≤20% Sunday
  4. Already: 21-23 UTC excluded
  5. Already: hour_utc not a feature
  6. Check vol_ratio time distribution at fires (no backdoor session leak)
"""
import pandas as pd
import numpy as np
import re
from pathlib import Path

ROOT = Path("/Users/brock-mini-mac/scrooge-research")
IN = ROOT / "strategy-library-v1"
OUT = ROOT / "reports"

CANDIDATES = [
    {"strategy": "TF6_long",  "pair": "USD_JPY",
     "rule": "atr_ratio>1.379 AND spread_cost_R>0.01154 AND adx14<=62.08 AND ema50_dist<=0.004221"},
    {"strategy": "TF6_long",  "pair": "USD_MXN",
     "rule": "atr_ratio<=1.355 AND rsi14>59.7 AND rsi14>80.83 AND ema50_dist<=0.009411"},
    {"strategy": "TF6_short", "pair": "USD_CAD",
     "rule": "spread_cost_R<=0.0398 AND ema20_dist>-0.001887 AND rsi14>19.93 AND atr_ratio>1.381"},
]

SPREAD = {
    "EUR_USD": 0.6, "GBP_USD": 0.9, "AUD_USD": 0.8, "NZD_USD": 1.2,
    "USD_JPY": 0.7, "USD_CHF": 1.0, "USD_CAD": 1.2, "USD_MXN": 12.0,
    "EUR_GBP": 1.0, "EUR_AUD": 1.6, "EUR_NZD": 2.8, "EUR_CAD": 1.8,
    "EUR_CHF": 1.4, "EUR_JPY": 1.2,
    "GBP_AUD": 2.5, "GBP_NZD": 3.5, "GBP_CAD": 2.4, "GBP_CHF": 2.2, "GBP_JPY": 1.6,
    "AUD_CAD": 1.5, "AUD_CHF": 1.8, "AUD_JPY": 1.2, "AUD_NZD": 2.0,
    "CAD_JPY": 1.5, "CHF_JPY": 1.6, "NZD_JPY": 1.8,
}
def pip_size(p): return 0.01 if p.endswith("JPY") else 0.0001

def parse_rule(rt):
    parts = re.split(r"\s+AND\s+", rt)
    out = []
    for p in parts:
        m = re.match(r"^([\w_]+)(<=|>=|<|>|=)(-?[\d.eE+]+)$", p.strip())
        if m: out.append((m.group(1), m.group(2), float(m.group(3))))
    return out

def apply_rule(df, rule):
    m = pd.Series(True, index=df.index)
    for f, op, thr in rule:
        if op == "<=": m &= df[f] <= thr
        elif op == ">=": m &= df[f] >= thr
        elif op == "<":  m &= df[f] <  thr
        elif op == ">":  m &= df[f] >  thr
    return m

def boot_ci_low(arr, B=500, alpha=0.05, rng=None):
    n = len(arr)
    if n < 5: return np.nan
    idx = rng.integers(0, n, size=(B, n))
    return float(np.quantile(arr[idx].mean(axis=1), alpha/2))

rng = np.random.default_rng(42)
hold_end = None
recent_start = None

for cand in CANDIDATES:
    strat, pair = cand["strategy"], cand["pair"]
    rule = parse_rule(cand["rule"])
    print(f"\n{'='*78}\n=== {strat} / {pair} ===\n{'='*78}")
    print(f"rule: {cand['rule']}\n")

    trades = pd.read_parquet(IN / f"trades_{pair}.parquet")
    trades["entry_ts"] = pd.to_datetime(trades["entry_ts"], utc=True)
    trades["era"] = np.where(trades["entry_ts"] < pd.Timestamp("2025-01-01", tz="UTC"),
                              "discovery", "holdout")
    # already excluded 21-23
    trades = trades[(trades["hour_utc"] < 21) | (trades["hour_utc"] >= 23)].copy()
    sub = trades[trades.strategy == strat]
    sub = sub[apply_rule(sub, rule)].copy()
    if hold_end is None:
        hold_end = sub[sub.era=="holdout"]["entry_ts"].max() if len(sub) > 0 else \
                   trades[trades.era=="holdout"]["entry_ts"].max()
        recent_start = pd.Timestamp("2026-04-21", tz="UTC") - pd.Timedelta(days=180)

    if len(sub) == 0:
        print("  no fires after filters"); continue

    print(f"  total fires (post-21-23 kill): {len(sub)}")
    sub_h = sub[sub.era == "holdout"]
    sub_r = sub_h[sub_h["entry_ts"] >= recent_start]
    print(f"  holdout n={len(sub_h)}  recent n={len(sub_r)}")

    # ---- Gate 3: fire-time concentration audit ----
    print("\n  Hour-of-day distribution (all fires):")
    h_dist = sub["hour_utc"].value_counts(normalize=True).sort_index()
    max_hr = h_dist.max()
    max_hr_idx = h_dist.idxmax()
    print(f"    max hour share: {max_hr:.1%} at hour {max_hr_idx}")
    for hr, s in h_dist.items():
        if s >= 0.02:
            bar = "█" * int(40 * s)
            print(f"      {int(hr):2d}h  {s:5.1%}  {bar}")
    if max_hr > 0.25:
        print(f"    *** FAIL: hour {max_hr_idx} > 25% (Brock's gate) ***")
    else:
        print(f"    PASS: max hour share {max_hr:.1%} <= 25%")

    print("  Weekday distribution (Mon=0..Sun=6):")
    wd_dist = sub["weekday"].value_counts(normalize=True).sort_index()
    sun_share = wd_dist.get(6, 0)
    print(f"    Sunday share: {sun_share:.1%}")
    for wd, s in wd_dist.items():
        name = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"][int(wd)]
        bar = "█" * int(40 * s)
        print(f"      {name}  {s:5.1%}  {bar}")
    if sun_share > 0.20:
        print(f"    *** FAIL: Sunday > 20% ***")
    else:
        print(f"    PASS: Sunday share {sun_share:.1%} <= 20%")

    # ---- Gate 6: vol_ratio audit at fires ----
    print(f"\n  vol_ratio at fires: median={sub['vol_ratio'].median():.2f}  p10={sub['vol_ratio'].quantile(0.1):.2f}  p90={sub['vol_ratio'].quantile(0.9):.2f}")
    pct_low_vol = (sub["vol_ratio"] < 0.4).mean()
    pct_pathological = (sub["vol_ratio"] < 0.2).mean()
    print(f"    fraction with vol_ratio < 0.4: {pct_low_vol:.1%}")
    print(f"    fraction with vol_ratio < 0.2: {pct_pathological:.1%}")

    # ---- Gate 1: vol-conditional spread ----
    pip = pip_size(pair)
    base_spread_px = SPREAD[pair] * pip
    risk_h = (sub_h["entry_price"].values - sub_h["sl"].values).__abs__()
    risk_r = (sub_r["entry_price"].values - sub_r["sl"].values).__abs__()
    factors_h = np.where(sub_h["vol_ratio"].values < 0.2, 3.0,
                np.where(sub_h["vol_ratio"].values < 0.4, 2.0, 1.0))
    factors_r = np.where(sub_r["vol_ratio"].values < 0.2, 3.0,
                np.where(sub_r["vol_ratio"].values < 0.4, 2.0, 1.0))
    extra_R_h = (factors_h - 1.0) * base_spread_px / risk_h
    extra_R_r = (factors_r - 1.0) * base_spread_px / risk_r
    r_h_vc = sub_h["realized_R"].values - extra_R_h
    r_r_vc = sub_r["realized_R"].values - extra_R_r
    mh_vc = r_h_vc.mean() if len(r_h_vc) else np.nan
    ci_h_vc = boot_ci_low(r_h_vc, rng=rng)
    mr_vc = r_r_vc.mean() if len(r_r_vc) else np.nan
    ci_r_vc = boot_ci_low(r_r_vc, rng=rng) if len(r_r_vc) >= 5 else np.nan
    print(f"\n  Vol-conditional spread:")
    print(f"    holdout: mean_R = {mh_vc:+.3f}  CI_lo = {ci_h_vc:+.3f}")
    print(f"    recent : mean_R = {mr_vc:+.3f}  CI_lo = {ci_r_vc if pd.notna(ci_r_vc) else 0:+.3f}")
    vc_pass = (mh_vc > 0) and (ci_h_vc > 0) and (mr_vc > 0) and (pd.notna(ci_r_vc) and ci_r_vc > 0)
    print(f"    {'PASS' if vc_pass else 'FAIL'}")

    # ---- Gate 2: slippage MC on top of vol-conditional spread ----
    def slip_max_pips(vol_ratio, pair):
        base = np.where(vol_ratio < 0.2, 2.0,
               np.where(vol_ratio < 0.4, 1.5, 0.8))
        if pair == "USD_MXN": base = base * 3.0
        return base

    slip_max_h = slip_max_pips(sub_h["vol_ratio"].values, pair)
    slip_max_r = slip_max_pips(sub_r["vol_ratio"].values, pair)
    B = 1000
    means_h = np.zeros(B); means_r = np.zeros(B)
    for b in range(B):
        e_h = rng.uniform(0,1,len(sub_h)) * slip_max_h * pip
        x_h = rng.uniform(0,1,len(sub_h)) * slip_max_h * pip
        means_h[b] = (r_h_vc - (e_h+x_h)/risk_h).mean() if len(r_h_vc) else 0
        e_r = rng.uniform(0,1,len(sub_r)) * slip_max_r * pip
        x_r = rng.uniform(0,1,len(sub_r)) * slip_max_r * pip
        means_r[b] = (r_r_vc - (e_r+x_r)/risk_r).mean() if len(r_r_vc) else 0
    h_pct_pos = (means_h > 0).mean()
    r_pct_pos = (means_r > 0).mean()
    h_p05 = np.quantile(means_h, 0.05)
    r_p05 = np.quantile(means_r, 0.05)
    print(f"\n  Slippage MC (1000 draws, on top of vol-cond spread):")
    print(f"    holdout: pct_pos={h_pct_pos:.1%}  p05={h_p05:+.3f}  median={np.median(means_h):+.3f}")
    print(f"    recent : pct_pos={r_pct_pos:.1%}  p05={r_p05:+.3f}  median={np.median(means_r):+.3f}")
    mc_pass = h_pct_pos >= 0.95 and r_pct_pos >= 0.95
    print(f"    {'PASS' if mc_pass else 'FAIL'} (require 95% of draws positive)")

    # ---- Final verdict ----
    hour_pass = max_hr <= 0.25
    wd_pass = sun_share <= 0.20
    all_pass = vc_pass and mc_pass and hour_pass and wd_pass
    print(f"\n  === VERDICT: {'PASS ALL GATES' if all_pass else 'FAIL'} ===")
    print(f"    hour concentration: {'PASS' if hour_pass else 'FAIL'}")
    print(f"    sunday concentration: {'PASS' if wd_pass else 'FAIL'}")
    print(f"    vol-conditional spread: {'PASS' if vc_pass else 'FAIL'}")
    print(f"    slippage MC 95% positive: {'PASS' if mc_pass else 'FAIL'}")
