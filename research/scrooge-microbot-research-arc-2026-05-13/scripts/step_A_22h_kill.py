"""Step A': re-stat the 14 survivors after also killing 22-23 UTC."""
import pandas as pd
import numpy as np
import re
from pathlib import Path

ROOT = Path("/tmp/scrooge-research")
IN  = ROOT / "strategy-library-v1"
OUT = ROOT / "reports"

strict14 = pd.read_csv(OUT / "stepA_strict.csv")

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

def boot_ci(arr, B=400, alpha=0.05, rng=None):
    if rng is None: rng = np.random.default_rng(0)
    n = len(arr)
    if n < 5: return np.nan
    idx = rng.integers(0, n, size=(B, n))
    return float(np.quantile(arr[idx].mean(axis=1), alpha/2))

rng = np.random.default_rng(42)
rows = []
print("=== Step A' — also kill 22-23 UTC, recheck 14 step-A survivors ===\n")
for _, surv in strict14.iterrows():
    strat, pair = surv["strategy"], surv["pair"]
    trades = pd.read_parquet(IN / f"trades_{pair}.parquet")
    trades["entry_ts"] = pd.to_datetime(trades["entry_ts"], utc=True)
    trades["era"] = np.where(trades["entry_ts"] < pd.Timestamp("2025-01-01", tz="UTC"), "discovery", "holdout")
    # KILL 21-23 UTC entirely
    trades = trades[(trades["hour_utc"] < 21) | (trades["hour_utc"] >= 23)].copy()
    sub = trades[trades.strategy == strat]
    sub = sub[apply_rule(sub, parse_rule(surv["rule"]))]
    sub_h = sub[sub.era == "holdout"]
    hold_end = sub_h["entry_ts"].max() if len(sub_h) else pd.Timestamp("2026-04-21", tz="UTC")
    recent_start = pd.Timestamp("2026-04-21", tz="UTC") - pd.Timedelta(days=180)
    sub_r = sub_h[sub_h["entry_ts"] >= recent_start]

    if len(sub_h) < 5:
        rows.append({"strategy": strat, "pair": pair, "n_h": len(sub_h),
                     "mean_R_h": np.nan, "ci_h_lo": np.nan,
                     "n_recent": len(sub_r), "mean_R_recent": np.nan, "ci_recent_lo": np.nan,
                     "survives": False})
        continue
    rh = sub_h["realized_R"].values
    rr = sub_r["realized_R"].values
    ci_h = boot_ci(rh, rng=rng)
    ci_r = boot_ci(rr, rng=rng) if len(rr) >= 5 else np.nan
    mh = float(rh.mean())
    mr = float(rr.mean()) if len(rr) else np.nan
    survives = (mh > 0) and (ci_h > 0) and (not np.isnan(mr)) and (mr > 0) and (not np.isnan(ci_r)) and (ci_r > 0)
    rows.append({"strategy": strat, "pair": pair,
                 "n_h": len(sub_h), "mean_R_h": mh, "ci_h_lo": ci_h,
                 "n_recent": len(sub_r), "mean_R_recent": mr, "ci_recent_lo": ci_r,
                 "survives": survives})

res = pd.DataFrame(rows)
res.to_csv(OUT / "stepA_prime_22h_kill.csv", index=False)
print(res.to_string(index=False, float_format="%.3f"))
print(f"\n=== SURVIVORS after also killing 22-23 UTC: {res['survives'].sum()} / {len(res)} ===")
print(res[res["survives"]].to_string(index=False, float_format="%.3f"))
