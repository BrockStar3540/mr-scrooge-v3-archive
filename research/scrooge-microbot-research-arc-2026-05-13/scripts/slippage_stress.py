"""Step D: Slippage Monte Carlo on the 4 vol-conditional spread survivors.

Model: random adverse slippage on both entry and exit. Pip ranges depend on
volume context:

  vol_ratio < 0.2  → entry slip ∈ U[0, 2] pips, exit slip ∈ U[0, 2] pips
  vol_ratio < 0.4  → entry slip ∈ U[0, 1.5] pips, exit slip ∈ U[0, 1.5] pips
  else             → entry slip ∈ U[0, 0.8] pips, exit slip ∈ U[0, 0.8] pips

USD_MXN multiplied 3x for all bands (high-spread exotic).
JPY pairs adjusted because pip_size = 0.01.

Each Monte Carlo draw applies fresh slippage to ALL trades in the cell, then
computes mean_R. We do 1000 draws and report: median, 5th pctile, 95th pctile,
fraction of draws where mean_R remains > 0.

This is on top of the vol-conditional spread already applied.
"""
import pandas as pd
import numpy as np
import re
from pathlib import Path

ROOT = Path("/tmp/scrooge-research")
IN  = ROOT / "strategy-library-v1"
OUT = ROOT / "reports"

# The 4 survivors after vol-conditional spread test
SURVIVORS = [
    {"strategy": "TF6_short", "pair": "USD_JPY",
     "rule": "spread_cost_R>0.004112 AND weekday>1.5 AND bb_width_rank<=0.9983 AND ema50_dist<=-0.004768"},
    {"strategy": "MR4_long",  "pair": "CHF_JPY", "rule": "vol_ratio<=0.2397 AND vol_ratio<=0.08077"},
    {"strategy": "MR4_long",  "pair": "EUR_JPY", "rule": "vol_ratio<=0.7493 AND vol_ratio<=0.0781"},
    {"strategy": "MR4_long",  "pair": "AUD_JPY", "rule": "vol_ratio<=0.3576 AND rsi14<=35.09"},
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

def parse_rule(rule_text):
    parts = re.split(r"\s+AND\s+", rule_text)
    out = []
    for p in parts:
        m = re.match(r"^([\w_]+)(<=|>=|<|>|=)(-?[\d.eE+]+)$", p.strip())
        if m: out.append((m.group(1), m.group(2), float(m.group(3))))
    return out

def apply_rule(df, rule):
    m = pd.Series(True, index=df.index)
    for f, op, thr in rule:
        if op == "<=": m &= (df[f] <= thr)
        elif op == ">=": m &= (df[f] >= thr)
        elif op == "<":  m &= (df[f] <  thr)
        elif op == ">":  m &= (df[f] >  thr)
    return m

# Slippage in pips, vol-conditional
def slip_max_pips(vol_ratio, pair):
    base = np.where(vol_ratio < 0.2, 2.0,
            np.where(vol_ratio < 0.4, 1.5, 0.8))
    if pair == "USD_MXN":
        base = base * 3.0
    return base

print("=== Slippage Monte Carlo on 4 candidates ===\n")
all_trades_cache = {}
hold_end = None
recent_start = None
rng = np.random.default_rng(42)

results = []
for surv in SURVIVORS:
    pair = surv["pair"]; strat = surv["strategy"]
    f = IN / f"trades_{pair}.parquet"
    trades = pd.read_parquet(f)
    trades["entry_ts"] = pd.to_datetime(trades["entry_ts"], utc=True)
    trades["era"] = np.where(trades["entry_ts"] < pd.Timestamp("2025-01-01", tz="UTC"), "discovery", "holdout")
    trades = trades[(trades["hour_utc"] < 21) | (trades["hour_utc"] >= 22)].copy()
    if hold_end is None:
        hold_end = trades[trades.era=="holdout"]["entry_ts"].max()
        recent_start = hold_end - pd.Timedelta(days=180)

    sub = trades[trades.strategy == strat]
    sub = sub[apply_rule(sub, parse_rule(surv["rule"]))]
    sub_h = sub[sub.era == "holdout"].copy()
    sub_r = sub[(sub.era == "holdout") & (sub["entry_ts"] >= recent_start)].copy()

    # ALSO apply vol-conditional spread baseline (so this slippage is ON TOP of that)
    pip = pip_size(pair)
    base_spread_px = SPREAD[pair] * pip
    for d in (sub_h, sub_r):
        vol_factor = np.where(d["vol_ratio"].values < 0.2, 3.0,
                     np.where(d["vol_ratio"].values < 0.4, 2.0, 1.0))
        extra_R = (vol_factor - 1.0) * base_spread_px / d["risk_px"].values if False else (
                  (vol_factor - 1.0) * base_spread_px / (d["entry_price"].values - d["sl"].values).__abs__())
        d["R_after_spread"] = d["realized_R"].values - extra_R

    risk_h = (sub_h["entry_price"].values - sub_h["sl"].values).__abs__()
    risk_r = (sub_r["entry_price"].values - sub_r["sl"].values).__abs__()
    max_slip_pips_h = slip_max_pips(sub_h["vol_ratio"].values, pair)
    max_slip_pips_r = slip_max_pips(sub_r["vol_ratio"].values, pair)

    # Monte Carlo: 1000 draws of slippage
    B = 1000
    means_h = np.zeros(B)
    means_r = np.zeros(B)
    for b in range(B):
        entry_slip_h = rng.uniform(0, 1, len(sub_h)) * max_slip_pips_h * pip
        exit_slip_h  = rng.uniform(0, 1, len(sub_h)) * max_slip_pips_h * pip
        total_h = (entry_slip_h + exit_slip_h) / risk_h
        means_h[b] = (sub_h["R_after_spread"].values - total_h).mean()

        entry_slip_r = rng.uniform(0, 1, len(sub_r)) * max_slip_pips_r * pip
        exit_slip_r  = rng.uniform(0, 1, len(sub_r)) * max_slip_pips_r * pip
        total_r = (entry_slip_r + exit_slip_r) / risk_r
        means_r[b] = (sub_r["R_after_spread"].values - total_r).mean()

    results.append({
        "strategy": strat, "pair": pair, "n_h": len(sub_h), "n_r": len(sub_r),
        # Holdout mean R distribution under slippage
        "h_median": float(np.median(means_h)),
        "h_p05":    float(np.quantile(means_h, 0.05)),
        "h_p95":    float(np.quantile(means_h, 0.95)),
        "h_pct_pos": float((means_h > 0).mean()),
        # Recent mean R distribution under slippage
        "r_median": float(np.median(means_r)),
        "r_p05":    float(np.quantile(means_r, 0.05)),
        "r_p95":    float(np.quantile(means_r, 0.95)),
        "r_pct_pos": float((means_r > 0).mean()),
    })

result = pd.DataFrame(results)
result.to_csv(OUT / "stepD_slippage_mc.csv", index=False)

print(f"After 1000 Monte Carlo draws of slippage (on top of vol-conditional spread):\n")
cols_h = ["strategy","pair","n_h","h_median","h_p05","h_p95","h_pct_pos"]
print("Holdout (full):")
print(result[cols_h].to_string(index=False, float_format="%.3f"))

cols_r = ["strategy","pair","n_r","r_median","r_p05","r_p95","r_pct_pos"]
print("\nRecent 6mo:")
print(result[cols_r].to_string(index=False, float_format="%.3f"))

print("\nINTERPRETATION:")
print("  - h_pct_pos / r_pct_pos = fraction of slippage realizations with positive mean R")
print("  - h_p05 / r_p05 = 5th percentile = pessimistic-but-plausible outcome")
print(f"\nsaved -> {OUT}/stepD_slippage_mc.csv")
