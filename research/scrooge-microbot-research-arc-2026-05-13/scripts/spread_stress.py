"""Step C: Spread-realism stress test on the 14 Step-A survivors.

The strategy library used average per-pair spread. For trades that fire in
low-volume conditions (vol_ratio < 0.4), real-world spreads typically widen
1.5-3x. We re-simulate the 14 survivor trades with two adverse-spread models:

  Model 1 — Static 1.5x spread (mild stress)
  Model 2 — Volume-conditional spread:
      vol_ratio < 0.2  → 3.0x spread
      vol_ratio < 0.4  → 2.0x spread
      else             → 1.0x spread

For each survivor cell we recompute realized_R under each spread model and
check whether the recent-6mo CI lower bound stays above 0.

Operates entirely on the existing trade parquets — no re-walking needed
because we can adjust realized_R analytically:

  new_realized = old_realized - (extra_spread_cost / risk_in_atr_units)

where extra_spread_cost = (new_spread - old_spread) * pip_size / 2 per side
(applied to both entry and exit = full spread of extra).
"""
import pandas as pd
import numpy as np
import re
from pathlib import Path

ROOT = Path("/tmp/scrooge-research")
IN  = ROOT / "strategy-library-v1"
OUT = ROOT / "reports"

PAIRS = ["EUR_USD","GBP_USD","AUD_USD","NZD_USD","USD_JPY","USD_CHF","USD_CAD","USD_MXN",
         "EUR_GBP","EUR_AUD","EUR_NZD","EUR_CAD","EUR_CHF","EUR_JPY",
         "GBP_AUD","GBP_NZD","GBP_CAD","GBP_CHF","GBP_JPY",
         "AUD_CAD","AUD_CHF","AUD_JPY","AUD_NZD","CAD_JPY","CHF_JPY","NZD_JPY"]

# Load step A strict survivors
strict = pd.read_csv(OUT / "stepA_strict.csv")
print(f"loaded {len(strict)} step-A strict survivors")

def parse_rule(rule_text):
    """Parse 'feat<=val AND feat>val AND ...' into list of (feat, op, val)."""
    if pd.isna(rule_text) or rule_text == "ALL": return []
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

def boot_ci(arr, B=400, alpha=0.05, rng=None):
    if rng is None: rng = np.random.default_rng(0)
    n = len(arr)
    if n < 5: return np.nan, np.nan
    idx = rng.integers(0, n, size=(B, n))
    means = arr[idx].mean(axis=1)
    return float(np.quantile(means, alpha/2)), float(np.quantile(means, 1-alpha/2))

# Load all trades once
print("loading trade parquets ...")
parts = []
for p in PAIRS:
    f = IN / f"trades_{p}.parquet"
    if not f.exists(): continue
    parts.append(pd.read_parquet(f))
all_trades = pd.concat(parts, ignore_index=True)
all_trades["entry_ts"] = pd.to_datetime(all_trades["entry_ts"], utc=True)
all_trades["era"] = np.where(all_trades["entry_ts"] < pd.Timestamp("2025-01-01", tz="UTC"), "discovery", "holdout")
# Filter rollover
all_trades = all_trades[(all_trades["hour_utc"] < 21) | (all_trades["hour_utc"] >= 22)].copy()
all_trades["risk"] = (all_trades["entry_price"] - all_trades["sl"]).abs()
print(f"  total trades after rollover kill: {len(all_trades):,}")

hold_end = all_trades[all_trades.era == "holdout"]["entry_ts"].max()
recent_start = hold_end - pd.Timedelta(days=180)

# === Apply spread stress per survivor cell ===
rng = np.random.default_rng(42)
out_rows = []
print(f"\n=== SPREAD STRESS on {len(strict)} survivors ===")

def vol_conditional_spread_factor(vol_ratio):
    return np.where(vol_ratio < 0.2, 3.0,
            np.where(vol_ratio < 0.4, 2.0, 1.0))

for _, surv in strict.iterrows():
    strat = surv["strategy"]; pair = surv["pair"]
    sub = all_trades[(all_trades.strategy == strat) & (all_trades.pair == pair)].copy()
    rule = parse_rule(surv["rule"])
    sub = sub[apply_rule(sub, rule)]
    if len(sub) == 0: continue

    # Original spread cost is already baked into realized_R. Recompute extra cost
    # for the stress multiplier.
    pip = 0.01 if pair.endswith("JPY") else 0.0001
    base_spread_pips = surv["mean_R_h"] * 0  # placeholder; the strat lib uses per-pair table

    # Look up base spread
    SPREAD = {
        "EUR_USD": 0.6, "GBP_USD": 0.9, "AUD_USD": 0.8, "NZD_USD": 1.2,
        "USD_JPY": 0.7, "USD_CHF": 1.0, "USD_CAD": 1.2, "USD_MXN": 12.0,
        "EUR_GBP": 1.0, "EUR_AUD": 1.6, "EUR_NZD": 2.8, "EUR_CAD": 1.8,
        "EUR_CHF": 1.4, "EUR_JPY": 1.2,
        "GBP_AUD": 2.5, "GBP_NZD": 3.5, "GBP_CAD": 2.4, "GBP_CHF": 2.2, "GBP_JPY": 1.6,
        "AUD_CAD": 1.5, "AUD_CHF": 1.8, "AUD_JPY": 1.2, "AUD_NZD": 2.0,
        "CAD_JPY": 1.5, "CHF_JPY": 1.6, "NZD_JPY": 1.8,
    }
    base_spread_pips = SPREAD[pair]
    base_spread_px = base_spread_pips * pip
    risk_px = sub["risk"].values

    # extra_R_cost = (new_spread - base_spread) / risk
    # 1.5x: extra = 0.5 * base_spread_px / risk
    extra_1p5 = 0.5 * base_spread_px / risk_px
    factors = vol_conditional_spread_factor(sub["vol_ratio"].values)
    extra_vol = (factors - 1.0) * base_spread_px / risk_px

    r_orig = sub["realized_R"].values
    r_1p5 = r_orig - extra_1p5
    r_vol = r_orig - extra_vol

    # Per-era stats
    is_h = (sub.era == "holdout").values
    is_recent = (sub["entry_ts"].values >= np.datetime64(recent_start))
    rec_h = is_h & is_recent

    def stats(r, mask):
        rr = r[mask]
        if len(rr) < 5: return {"n": len(rr), "mean": np.nan, "ci_lo": np.nan, "wr": np.nan}
        ci_lo, _ = boot_ci(rr, rng=rng)
        return {"n": len(rr), "mean": float(rr.mean()), "ci_lo": ci_lo, "wr": float((rr>0).mean())}

    s_h_orig = stats(r_orig, is_h)
    s_h_15  = stats(r_1p5, is_h)
    s_h_vol = stats(r_vol, is_h)
    s_r_orig = stats(r_orig, rec_h)
    s_r_15  = stats(r_1p5, rec_h)
    s_r_vol = stats(r_vol, rec_h)

    survives_1p5 = (s_h_15["mean"] > 0) and (s_h_15["ci_lo"] > 0) and (s_r_15["mean"] > 0) and (s_r_15["ci_lo"] > 0)
    survives_vol = (s_h_vol["mean"] > 0) and (s_h_vol["ci_lo"] > 0) and (s_r_vol["mean"] > 0) and (s_r_vol["ci_lo"] > 0)

    out_rows.append({
        "strategy": strat, "pair": pair, "rule": surv["rule"],
        "n_h": s_h_orig["n"], "n_recent": s_r_orig["n"],
        "wr_h_orig": s_h_orig["wr"], "wr_recent_orig": s_r_orig["wr"],
        "mean_R_h_orig": s_h_orig["mean"], "ci_h_orig": s_h_orig["ci_lo"],
        "mean_R_recent_orig": s_r_orig["mean"], "ci_recent_orig": s_r_orig["ci_lo"],

        "mean_R_h_1p5x": s_h_15["mean"], "ci_h_1p5x": s_h_15["ci_lo"],
        "mean_R_recent_1p5x": s_r_15["mean"], "ci_recent_1p5x": s_r_15["ci_lo"],
        "survives_1p5x": survives_1p5,

        "mean_R_h_volcond": s_h_vol["mean"], "ci_h_volcond": s_h_vol["ci_lo"],
        "mean_R_recent_volcond": s_r_vol["mean"], "ci_recent_volcond": s_r_vol["ci_lo"],
        "survives_volcond": survives_vol,
    })

result = pd.DataFrame(out_rows)
result.to_csv(OUT / "stepC_spread_stress.csv", index=False)

print("\n=== ORIGINAL vs 1.5× SPREAD vs VOL-CONDITIONAL ===")
cols = ["strategy","pair","n_h","n_recent",
        "mean_R_h_orig","ci_h_orig",
        "mean_R_h_1p5x","ci_h_1p5x","survives_1p5x",
        "mean_R_h_volcond","ci_h_volcond","survives_volcond"]
print(result[cols].to_string(index=False, float_format="%.3f"))

print(f"\nsurvivors under 1.5× spread:    {result['survives_1p5x'].sum()} / {len(result)}")
print(f"survivors under vol-conditional: {result['survives_volcond'].sum()} / {len(result)}")

print(f"\nrecent-window stress:")
cols2 = ["strategy","pair","n_recent","mean_R_recent_orig","ci_recent_orig","mean_R_recent_1p5x","ci_recent_1p5x","mean_R_recent_volcond","ci_recent_volcond"]
print(result[cols2].to_string(index=False, float_format="%.3f"))

print(f"\nsaved -> {OUT}/stepC_spread_stress.csv")
