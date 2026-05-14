"""Step B: full discovery on the formula library trades with 21-23 UTC banned.

Same decision-tree discovery as Step A but:
  - Kill 21-23 UTC entirely (was: only 21-22)
  - hour_utc still excluded from features
  - Look for new candidates that weren't in the original 14

Also adds a fire-time-concentration gate: any cell where >40% of fires land
in a single hour is rejected as a backdoor-session-filter artifact.
"""
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.tree import DecisionTreeClassifier, _tree

ROOT = Path("/tmp/scrooge-research")
IN  = ROOT / "strategy-library-v1"
OUT = ROOT / "reports"

PAIRS = ["EUR_USD","GBP_USD","AUD_USD","NZD_USD","USD_JPY","USD_CHF","USD_CAD","USD_MXN",
         "EUR_GBP","EUR_AUD","EUR_NZD","EUR_CAD","EUR_CHF","EUR_JPY",
         "GBP_AUD","GBP_NZD","GBP_CAD","GBP_CHF","GBP_JPY",
         "AUD_CAD","AUD_CHF","AUD_JPY","AUD_NZD","CAD_JPY","CHF_JPY","NZD_JPY"]

FEATURES = ["adx14","rsi14","atr_ratio","bb_width_rank","price_pos","vol_ratio",
            "ema20_dist","ema50_dist","zscore20","weekday","spread_cost_R"]

print("loading parquets ...")
parts = []
for p in PAIRS:
    f = IN / f"trades_{p}.parquet"
    if not f.exists(): continue
    parts.append(pd.read_parquet(f))
all_trades = pd.concat(parts, ignore_index=True)
all_trades["entry_ts"] = pd.to_datetime(all_trades["entry_ts"], utc=True)
all_trades["era"] = np.where(all_trades["entry_ts"] < pd.Timestamp("2025-01-01", tz="UTC"), "discovery", "holdout")
all_trades["is_winner"] = (all_trades["realized_R"] > 0).astype(int)
print(f"  {len(all_trades):,} total")

# KILL 21-23 UTC
before = len(all_trades)
all_trades = all_trades[(all_trades["hour_utc"] < 21) | (all_trades["hour_utc"] >= 23)].copy()
print(f"  killed 21-23 UTC: {before - len(all_trades):,} trades")
print(f"  remaining: {len(all_trades):,}")

all_trades = all_trades.dropna(subset=FEATURES + ["realized_R"]).copy()
print(f"  after dropna: {len(all_trades):,}")


def tree_paths(tree, fnames):
    t = tree.tree_; rules = []
    def rec(node, path):
        if t.children_left[node] == _tree.TREE_LEAF:
            rules.append(path[:]); return
        f = fnames[t.feature[node]]; thr = t.threshold[node]
        rec(t.children_left[node], path + [(f,"<=",thr)])
        rec(t.children_right[node], path + [(f,">",thr)])
    rec(0, []); return rules

def apply_rule_np(df, rule):
    m = np.ones(len(df), dtype=bool)
    for f, op, thr in rule:
        col = df[f].values
        if op == "<=": m &= (col <= thr)
        else:          m &= (col > thr)
    return m

def boot_ci(arr, B=400, rng=None):
    n = len(arr)
    if n < 5: return np.nan
    idx = rng.integers(0, n, size=(B, n))
    return float(np.quantile(arr[idx].mean(axis=1), 0.025))

hold_end = all_trades[all_trades.era=="holdout"]["entry_ts"].max()
recent_start = hold_end - pd.Timedelta(days=180)
wf_edges = pd.date_range(pd.Timestamp("2025-01-01", tz="UTC"),
                          hold_end + pd.Timedelta("1d"), periods=5)

rng = np.random.default_rng(42)
rows = []
combos = all_trades.groupby(["strategy","pair"]).size().reset_index(name="n")
combos = combos[combos["n"] >= 300]
print(f"\n  combos with n>=300: {len(combos)}")

for _, row in combos.iterrows():
    strat, pair = row["strategy"], row["pair"]
    sub = all_trades[(all_trades.strategy == strat) & (all_trades.pair == pair)]
    sub_d = sub[sub.era == "discovery"]; sub_h = sub[sub.era == "holdout"]
    if len(sub_d) < 100 or len(sub_h) < 30: continue
    clf = DecisionTreeClassifier(max_depth=4, min_samples_leaf=60, random_state=42)
    try: clf.fit(sub_d[FEATURES].values, sub_d["is_winner"].values)
    except: continue
    base_mr_h = sub_h["realized_R"].mean()
    for path in tree_paths(clf, FEATURES):
        md = apply_rule_np(sub_d, path); mh = apply_rule_np(sub_h, path)
        n_d = md.sum(); n_h = mh.sum()
        if n_d < 50 or n_h < 15: continue
        r_d = sub_d["realized_R"].values[md]; r_h = sub_h["realized_R"].values[mh]
        wr_d = (r_d > 0).mean()
        if wr_d < 0.40: continue
        mR_d = r_d.mean(); mR_h = r_h.mean()
        if mR_d <= 0 or mR_h <= 0: continue
        ci_d_lo = boot_ci(r_d, rng=rng)
        ci_h_lo = boot_ci(r_h, rng=rng)
        if ci_d_lo <= 0 or ci_h_lo <= 0: continue
        # walk-forward
        wf_pos = 0; wf_enough = 0
        for i in range(4):
            wmask = mh & ((sub_h.entry_ts.values >= np.datetime64(wf_edges[i])) &
                          (sub_h.entry_ts.values <  np.datetime64(wf_edges[i+1])))
            rw = sub_h["realized_R"].values[wmask]
            if len(rw) >= 5: wf_enough += 1
            if len(rw) > 0 and rw.mean() > 0: wf_pos += 1
        if wf_pos < 3 or wf_enough < 3: continue
        # recent
        rec_mask = mh & (sub_h.entry_ts.values >= np.datetime64(recent_start))
        rrec = sub_h["realized_R"].values[rec_mask]
        if len(rrec) < 5 or rrec.mean() <= 0: continue
        ci_rec_lo = boot_ci(rrec, rng=rng)
        if ci_rec_lo <= 0: continue
        # FIRE-TIME CONCENTRATION GATE: reject if any single hour has >40% of fires
        all_fires = pd.concat([sub_d[md], sub_h[mh]])
        hr_share_max = all_fires["hour_utc"].value_counts(normalize=True).max() if len(all_fires) else 0
        if hr_share_max > 0.40: continue
        # weekday concentration
        wd_share_max = all_fires["weekday"].value_counts(normalize=True).max() if len(all_fires) else 0
        rule_text = " AND ".join(f"{f}{op}{thr:.4g}" for f,op,thr in path) or "ALL"
        rows.append({
            "strategy": strat, "pair": pair, "rule": rule_text,
            "n_d": int(n_d), "n_h": int(n_h),
            "mean_R_d": float(mR_d), "ci_d_lo": ci_d_lo,
            "mean_R_h": float(mR_h), "ci_h_lo": ci_h_lo,
            "wf_pos": wf_pos,
            "n_recent": len(rrec), "mean_R_recent": float(rrec.mean()), "ci_lo_recent": ci_rec_lo,
            "lift_R_h": float(mR_h) - float(base_mr_h),
            "hr_max_share": float(hr_share_max),
            "wd_max_share": float(wd_share_max),
        })

res = pd.DataFrame(rows)
res.to_csv(OUT / "stepB_no21_23_concentration_filtered.csv", index=False)
print(f"\n=== STEP B SURVIVORS (no 21-23 UTC, no single-hour >40%) ===")
print(f"  count: {len(res)}")
if len(res):
    cols = ["strategy","pair","rule","n_d","n_h","mean_R_h","ci_h_lo","n_recent","mean_R_recent","ci_lo_recent","hr_max_share","wd_max_share","lift_R_h"]
    print(res.sort_values("ci_lo_recent", ascending=False)[cols].to_string(index=False, float_format="%.3f"))
