"""Diagnose where each TF6_short USD_JPY leaf dies in the unbiased pipeline."""
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.tree import DecisionTreeClassifier, _tree

ROOT = Path("/tmp/scrooge-research")
IN  = ROOT / "strategy-library-v1"

FEATURES = ["adx14","rsi14","atr_ratio","bb_width_rank","price_pos","vol_ratio",
            "ema20_dist","ema50_dist","zscore20","weekday","spread_cost_R"]

trades = pd.read_parquet(IN / "trades_USD_JPY.parquet")
trades["entry_ts"] = pd.to_datetime(trades["entry_ts"], utc=True)
trades["era"] = np.where(trades["entry_ts"] < pd.Timestamp("2025-01-01", tz="UTC"), "discovery", "holdout")
trades["is_winner"] = (trades["realized_R"] > 0).astype(int)
trades = trades[(trades["hour_utc"] < 21) | (trades["hour_utc"] >= 23)].copy()
sub = trades[trades.strategy == "TF6_short"].dropna(subset=FEATURES + ["realized_R"])
sub_d = sub[sub.era == "discovery"]; sub_h = sub[sub.era == "holdout"]
print(f"TF6_short USD_JPY: discovery n={len(sub_d)}, holdout n={len(sub_h)}")

clf = DecisionTreeClassifier(max_depth=4, min_samples_leaf=60, random_state=42)
clf.fit(sub_d[FEATURES].values, sub_d["is_winner"].values)

def tree_paths(tree, fnames):
    t = tree.tree_; rules = []
    def rec(node, path):
        if t.children_left[node] == _tree.TREE_LEAF:
            rules.append(path[:]); return
        f = fnames[t.feature[node]]; thr = t.threshold[node]
        rec(t.children_left[node], path + [(f,"<=",thr)])
        rec(t.children_right[node], path + [(f,">",thr)])
    rec(0, []); return rules

def apply_rule(df, rule):
    m = np.ones(len(df), dtype=bool)
    for f, op, thr in rule:
        col = df[f].values
        if op == "<=": m &= col <= thr
        else:          m &= col > thr
    return m

def boot_ci_low(arr, B=400, rng=None):
    n = len(arr)
    if n < 5: return np.nan
    idx = rng.integers(0, n, size=(B, n))
    return float(np.quantile(arr[idx].mean(axis=1), 0.025))

rng = np.random.default_rng(42)
paths = tree_paths(clf, FEATURES)
hold_end = sub_h["entry_ts"].max()
recent_start = hold_end - pd.Timedelta(days=180)

print(f"\nleaves: {len(paths)}\n")
print("LEAF DIAGNOSTIC:")
for i, p in enumerate(paths):
    md = apply_rule(sub_d, p); mh = apply_rule(sub_h, p)
    n_d = md.sum(); n_h = mh.sum()
    if n_d == 0 or n_h == 0: continue
    rd = sub_d["realized_R"].values[md]; rh = sub_h["realized_R"].values[mh]
    wr_d = (rd > 0).mean(); wr_h = (rh > 0).mean() if len(rh) else 0
    mR_h = rh.mean() if len(rh) else 0
    ci_h_lo = boot_ci_low(rh, rng=rng) if len(rh) >= 5 else np.nan
    fires = pd.concat([sub_d[md], sub_h[mh]])
    hr_max = fires["hour_utc"].value_counts(normalize=True).max() if len(fires) else 0
    wd_max = fires["weekday"].value_counts(normalize=True).max() if len(fires) else 0
    rec_mask = mh & (sub_h.entry_ts.values >= np.datetime64(recent_start))
    rec_r = sub_h["realized_R"].values[rec_mask]
    rec_mr = rec_r.mean() if len(rec_r) >= 5 else np.nan
    rec_ci = boot_ci_low(rec_r, rng=rng) if len(rec_r) >= 5 else np.nan
    rule_text = " AND ".join(f"{f}{op}{thr:.3g}" for f,op,thr in p) or "ALL"

    gate_status = []
    if n_d < 50: gate_status.append("n_d<50")
    if n_h < 15: gate_status.append("n_h<15")
    if wr_d < 0.40: gate_status.append(f"wr_d={wr_d:.2f}<0.40")
    if mR_h <= 0: gate_status.append(f"mR_h={mR_h:.2f}<=0")
    if pd.notna(ci_h_lo) and ci_h_lo <= 0: gate_status.append(f"ci_h_lo={ci_h_lo:.3f}<=0")
    if hr_max > 0.40: gate_status.append(f"hr_max={hr_max:.2f}>0.40")
    if wd_max > 0.40: gate_status.append(f"wd_max={wd_max:.2f}>0.40")
    if pd.notna(rec_mr) and rec_mr <= 0: gate_status.append(f"rec_mr={rec_mr:.2f}<=0")
    if pd.notna(rec_ci) and rec_ci <= 0: gate_status.append(f"rec_ci={rec_ci:.3f}<=0")
    if len(rec_r) < 5: gate_status.append(f"n_rec={len(rec_r)}<5")

    flag = "PASS" if not gate_status else "FAIL: " + ", ".join(gate_status)
    print(f"  leaf {i:2d}  n_d={n_d:4d} n_h={n_h:3d}  wr_d={wr_d:.2f}  mR_h={mR_h:+.2f}  ci_h={ci_h_lo if pd.notna(ci_h_lo) else 0:+.3f}  hr_max={hr_max:.2f}  wd_max={wd_max:.2f}  rec_n={len(rec_r):2d} rec_mr={rec_mr if pd.notna(rec_mr) else 0:+.2f}  [{flag}]")
    print(f"     rule: {rule_text}")
