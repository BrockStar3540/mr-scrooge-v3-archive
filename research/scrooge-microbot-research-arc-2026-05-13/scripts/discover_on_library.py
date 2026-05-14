"""Strategy-First Regime Discovery on the strategy-library trades.

Per (strategy × pair): fit decision tree to predict winner; extract leaf rules;
apply triple gate (CI both eras > 0, walk-forward >=3/4, recent 6mo + CI > 0).
"""
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.tree import DecisionTreeClassifier, _tree
import glob

ROOT = Path("/tmp/scrooge-research")
IN  = ROOT / "strategy-library-v1"
OUT = ROOT / "reports"

PAIRS = ["EUR_USD","GBP_USD","AUD_USD","NZD_USD","USD_JPY","USD_CHF","USD_CAD","USD_MXN",
         "EUR_GBP","EUR_AUD","EUR_NZD","EUR_CAD","EUR_CHF","EUR_JPY",
         "GBP_AUD","GBP_NZD","GBP_CAD","GBP_CHF","GBP_JPY",
         "AUD_CAD","AUD_CHF","AUD_JPY","AUD_NZD","CAD_JPY","CHF_JPY","NZD_JPY"]

FEATURES = ["adx14","rsi14","atr_ratio","bb_width_rank","price_pos","vol_ratio",
            "ema20_dist","ema50_dist","zscore20","hour_utc","weekday","spread_cost_R"]

# === Load all trades ===
print("loading all trade parquets ...")
parts = []
for p in PAIRS:
    f = IN / f"trades_{p}.parquet"
    if not f.exists(): continue
    df = pd.read_parquet(f)
    parts.append(df)
all_trades = pd.concat(parts, ignore_index=True)
print(f"total: {len(all_trades):,} trades across {len(parts)} pairs")

all_trades["entry_ts"] = pd.to_datetime(all_trades["entry_ts"], utc=True)
all_trades["era"] = np.where(all_trades["entry_ts"] < pd.Timestamp("2025-01-01", tz="UTC"), "discovery", "holdout")
all_trades["is_winner"] = (all_trades["realized_R"] > 0).astype(int)

# baseline expectancy per strategy x pair
print("\n=== BASELINE PER (strategy, pair) ===")
base = all_trades.groupby(["strategy","pair","era"]).agg(
    n=("realized_R","size"),
    mean_R=("realized_R","mean"),
    wr=("is_winner","mean"),
).reset_index()
base_piv = base.pivot_table(index=["strategy","pair"], columns="era", values=["n","mean_R","wr"]).reset_index()
base_piv.columns = [(f"{a}_{b}" if b else a) for a,b in base_piv.columns]
base_piv = base_piv.rename(columns={"n_discovery":"n_d","n_holdout":"n_h",
                                    "mean_R_discovery":"mean_R_d","mean_R_holdout":"mean_R_h",
                                    "wr_discovery":"wr_d","wr_holdout":"wr_h"})
base_piv.to_csv(OUT / "library_baseline.csv", index=False)
print(f"  strategy×pair combos: {len(base_piv)}")

# Show strategies with unconditional positive holdout (the easy ones — usually none)
unc_pos = base_piv[(base_piv.n_h >= 30) & (base_piv.mean_R_h > 0)]
print(f"\n  unconditional positive holdout (n_h>=30, mean_R_h > 0): {len(unc_pos)}")
if len(unc_pos):
    print(unc_pos.sort_values("mean_R_h", ascending=False).head(20).to_string(index=False, float_format="%.3f"))

# === Decision-tree regime discovery per (strategy, pair) ===
print("\n=== REGIME DISCOVERY (decision tree, max_depth=4, min_leaf=60) ===")

def tree_paths(tree, fnames):
    t = tree.tree_; rules = []
    def rec(node, path):
        if t.children_left[node] == _tree.TREE_LEAF:
            rules.append(path[:]); return
        f = fnames[t.feature[node]]; thr = t.threshold[node]
        rec(t.children_left[node], path + [(f,"<=",thr)])
        rec(t.children_right[node], path + [(f,">",thr)])
    rec(0, [])
    return rules

def apply_rule(df, rule):
    m = pd.Series(True, index=df.index)
    for f, op, thr in rule:
        if op == "<=": m &= (df[f] <= thr)
        else:          m &= (df[f] >  thr)
    return m

def boot_ci(arr, B=400, alpha=0.05, rng=None):
    if rng is None: rng = np.random.default_rng(0)
    n = len(arr)
    if n < 5: return np.nan, np.nan
    idx = rng.integers(0, n, size=(B, n))
    means = arr[idx].mean(axis=1)
    return float(np.quantile(means, alpha/2)), float(np.quantile(means, 1-alpha/2))

hold_end = all_trades[all_trades.era=="holdout"]["entry_ts"].max()
recent_start = hold_end - pd.Timedelta(days=180)
wf_edges = pd.date_range(pd.Timestamp("2025-01-01", tz="UTC"),
                          hold_end + pd.Timedelta("1d"), periods=5)

rng = np.random.default_rng(42)
regime_rows = []
combos = all_trades.groupby(["strategy","pair"]).size().reset_index(name="n")
combos = combos[combos["n"] >= 300]
print(f"  combos with n>=300: {len(combos)}")

for _, row in combos.iterrows():
    strat, pair = row["strategy"], row["pair"]
    sub = all_trades[(all_trades.strategy == strat) & (all_trades.pair == pair)].copy()
    sub = sub.dropna(subset=FEATURES + ["realized_R"])
    sub_d = sub[sub.era == "discovery"]
    sub_h = sub[sub.era == "holdout"]
    if len(sub_d) < 100 or len(sub_h) < 30: continue
    base_mr_d = sub_d["realized_R"].mean()
    base_mr_h = sub_h["realized_R"].mean()

    clf = DecisionTreeClassifier(max_depth=4, min_samples_leaf=60, random_state=42)
    try:
        clf.fit(sub_d[FEATURES].values, sub_d["is_winner"].values)
    except Exception:
        continue
    for path in tree_paths(clf, FEATURES):
        md = apply_rule(sub_d, path); mh = apply_rule(sub_h, path)
        n_d = int(md.sum()); n_h = int(mh.sum())
        if n_d < 50 or n_h < 15: continue
        r_d = sub_d.loc[md, "realized_R"]; r_h = sub_h.loc[mh, "realized_R"]
        wr_d = (r_d > 0).mean(); wr_h = (r_h > 0).mean()
        if wr_d < 0.40: continue
        mR_d = r_d.mean(); mR_h = r_h.mean()
        if mR_d <= 0 or mR_h <= 0: continue
        ci_d_lo, _ = boot_ci(r_d.values, rng=rng)
        ci_h_lo, _ = boot_ci(r_h.values, rng=rng)
        # walk-forward 4 windows
        wf_means = []; wf_ns = []
        for i in range(4):
            w = sub_h[mh & (sub_h.entry_ts >= wf_edges[i]) & (sub_h.entry_ts < wf_edges[i+1])]
            wf_means.append(float(w["realized_R"].mean()) if len(w) > 0 else np.nan)
            wf_ns.append(len(w))
        wf_pos = sum(1 for m in wf_means if (not pd.isna(m)) and m > 0)
        wf_enough = sum(1 for n in wf_ns if n >= 5)
        # recent
        rec = sub_h[mh & (sub_h.entry_ts >= recent_start)]
        rec_mean = float(rec["realized_R"].mean()) if len(rec) >= 5 else np.nan
        rec_ci_lo, _ = boot_ci(rec["realized_R"].values, rng=rng) if len(rec) >= 5 else (np.nan, np.nan)
        rule_text = " AND ".join(f"{f}{op}{thr:.4g}" for f,op,thr in path) or "ALL"
        regime_rows.append({
            "strategy": strat, "pair": pair, "rule": rule_text, "depth": len(path),
            "base_mR_d": float(base_mr_d), "base_mR_h": float(base_mr_h),
            "n_d": n_d, "wr_d": float(wr_d), "mean_R_d": float(mR_d), "ci_d_lo": ci_d_lo,
            "n_h": n_h, "wr_h": float(wr_h), "mean_R_h": float(mR_h), "ci_h_lo": ci_h_lo,
            "wf_pos": wf_pos, "wf_enough": wf_enough,
            "n_recent": len(rec), "mean_R_recent": rec_mean, "ci_lo_recent": rec_ci_lo,
            "lift_R_h": float(mR_h) - float(base_mr_h),
        })

reg = pd.DataFrame(regime_rows)
reg.to_csv(OUT / "library_discovery_all_regimes.csv", index=False)
print(f"\n  total candidate regimes: {len(reg)}")

ci_pass = reg[(reg.ci_d_lo > 0) & (reg.ci_h_lo > 0)].copy()
print(f"  + CI > 0 both eras:         {len(ci_pass)}")
robust = ci_pass[(ci_pass.wf_pos >= 3) & (ci_pass.wf_enough >= 3)].copy()
print(f"  + walk-forward >=3/4:       {len(robust)}")
strict = robust[(robust.mean_R_recent.fillna(-99) > 0) & (robust.ci_lo_recent.fillna(-99) > 0)].copy()
print(f"  + recent 6mo + CI > 0:      {len(strict)}")

ci_pass.to_csv(OUT / "library_discovery_ci_pass.csv", index=False)
robust.to_csv(OUT / "library_discovery_walk_forward.csv", index=False)
strict.to_csv(OUT / "library_discovery_strict_survivors.csv", index=False)

if len(strict):
    print("\n=== STRICT SURVIVORS ===")
    cols = ["strategy","pair","rule","n_d","wr_d","mean_R_d","ci_d_lo","n_h","wr_h","mean_R_h","ci_h_lo","wf_pos","n_recent","mean_R_recent","ci_lo_recent","lift_R_h"]
    print(strict.sort_values("ci_lo_recent", ascending=False)[cols].to_string(index=False, float_format="%.3f"))
else:
    print("\n=== ZERO STRICT SURVIVORS ===")

# Also produce a strategy-level summary (which strategies even produce any CI-pass)
print("\n=== CI-PASS BY STRATEGY ===")
if len(ci_pass):
    sum_s = ci_pass.groupby("strategy").agg(
        n_regimes=("rule","size"),
        pairs=("pair","nunique"),
        best_mR_h=("mean_R_h","max"),
        best_ci_h=("ci_h_lo","max"),
    ).reset_index().sort_values("n_regimes", ascending=False)
    print(sum_s.to_string(index=False, float_format="%.3f"))

print(f"\nsaved -> {OUT}")
