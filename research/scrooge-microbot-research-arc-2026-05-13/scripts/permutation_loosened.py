"""Permutation test on the LOOSENED discovery pipeline.

Shuffles realized_R within each (strategy, pair) group and re-runs the full
loosened discovery + stress stack. Counts strict-pass survivors per shuffle.

Real (unshuffled) baseline: 1-3 survivors after stress stack.
Compare against the null distribution of strict survivors under shuffled labels.
"""
import pandas as pd
import numpy as np
import sys
from pathlib import Path
from sklearn.tree import DecisionTreeRegressor, _tree

ROOT = Path("/Users/brock-mini-mac/scrooge-research")
IN = ROOT / "strategy-library-v1"
OUT = ROOT / "reports"

N_PERMS = int(sys.argv[1]) if len(sys.argv) > 1 else 50

PAIRS = ["EUR_USD","GBP_USD","AUD_USD","NZD_USD","USD_JPY","USD_CHF","USD_CAD","USD_MXN",
         "EUR_GBP","EUR_AUD","EUR_NZD","EUR_CAD","EUR_CHF","EUR_JPY",
         "GBP_AUD","GBP_NZD","GBP_CAD","GBP_CHF","GBP_JPY",
         "AUD_CAD","AUD_CHF","AUD_JPY","AUD_NZD","CAD_JPY","CHF_JPY","NZD_JPY"]

FEATURES = ["adx14","rsi14","atr_ratio","bb_width_rank","price_pos","vol_ratio",
            "ema20_dist","ema50_dist","zscore20","weekday","spread_cost_R"]

print("loading parquets ...", flush=True)
parts = []
for p in PAIRS:
    f = IN / f"trades_{p}.parquet"
    if not f.exists(): continue
    parts.append(pd.read_parquet(f))
all_trades = pd.concat(parts, ignore_index=True)
all_trades["entry_ts"] = pd.to_datetime(all_trades["entry_ts"], utc=True)
all_trades["era"] = np.where(all_trades["entry_ts"] < pd.Timestamp("2025-01-01", tz="UTC"),
                              "discovery", "holdout")
all_trades = all_trades[(all_trades["hour_utc"] < 21) | (all_trades["hour_utc"] >= 23)].copy()
all_trades = all_trades.dropna(subset=FEATURES + ["realized_R"]).copy()
print(f"  {len(all_trades):,} after dropna", flush=True)


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
        if op == "<=": m &= col <= thr
        else:          m &= col > thr
    return m

def boot_ci_low(arr, B=200, alpha=0.05, rng=None):
    n = len(arr)
    if n < 5: return -np.inf
    idx = rng.integers(0, n, size=(B, n))
    return float(np.quantile(arr[idx].mean(axis=1), alpha/2))

hold_end = all_trades[all_trades.era=="holdout"]["entry_ts"].max()
recent_start = hold_end - pd.Timedelta(days=180)
wf_edges = pd.date_range(pd.Timestamp("2025-01-01", tz="UTC"),
                          hold_end + pd.Timedelta("1d"), periods=5)

combos = all_trades.groupby(["strategy","pair"]).size().reset_index(name="n")
combos = combos[combos["n"] >= 200]
print(f"  combos: {len(combos)}", flush=True)


def discovery_pass(trades_df, rng):
    """Count strict-pass survivors under the loosened pipeline + stress stack."""
    n_strict = 0
    for _, row in combos.iterrows():
        strat, pair = row["strategy"], row["pair"]
        sub = trades_df[(trades_df.strategy == strat) & (trades_df.pair == pair)]
        sub_d = sub[sub.era == "discovery"]; sub_h = sub[sub.era == "holdout"]
        if len(sub_d) < 100 or len(sub_h) < 30: continue

        reg = DecisionTreeRegressor(max_depth=4, min_samples_leaf=30, random_state=42)
        try: reg.fit(sub_d[FEATURES].values, sub_d["realized_R"].values)
        except: continue

        for path in tree_paths(reg, FEATURES):
            md = apply_rule_np(sub_d, path); mh = apply_rule_np(sub_h, path)
            n_d = md.sum(); n_h = mh.sum()
            if n_d < 30 or n_h < 15: continue
            r_d = sub_d["realized_R"].values[md]; r_h = sub_h["realized_R"].values[mh]
            mR_d = r_d.mean(); mR_h = r_h.mean()
            if mR_d <= 0 or mR_h <= 0: continue
            ci_h_lo = boot_ci_low(r_h, rng=rng)
            if ci_h_lo <= 0: continue
            # walk-forward 3/4
            wf_pos = 0
            for i in range(4):
                wmask = mh & ((sub_h.entry_ts.values >= np.datetime64(wf_edges[i])) &
                              (sub_h.entry_ts.values <  np.datetime64(wf_edges[i+1])))
                rw = sub_h["realized_R"].values[wmask]
                if len(rw) > 0 and rw.mean() > 0: wf_pos += 1
            if wf_pos < 3: continue
            # recent positive
            rec_mask = mh & (sub_h.entry_ts.values >= np.datetime64(recent_start))
            rrec = sub_h["realized_R"].values[rec_mask]
            if len(rrec) < 3 or rrec.mean() <= 0: continue
            # concentration
            all_fires = pd.concat([sub_d[md], sub_h[mh]])
            hr_share = float(all_fires["hour_utc"].value_counts(normalize=True).max())
            wd_share = float(all_fires["weekday"].value_counts(normalize=True).max())
            if hr_share > 0.40 or wd_share > 0.40: continue
            n_strict += 1
    return n_strict


print("\nsanity (real, unshuffled):", flush=True)
real_count = discovery_pass(all_trades, np.random.default_rng(42))
print(f"  real strict count: {real_count}", flush=True)

print(f"\nrunning {N_PERMS} permutations ...", flush=True)
null_counts = []
rng_master = np.random.default_rng(0)
for k in range(N_PERMS):
    perm_seed = rng_master.integers(0, 2**31)
    perm_rng = np.random.default_rng(perm_seed)
    shuffled = all_trades.copy()
    for (strat, pair), idx in shuffled.groupby(["strategy","pair"]).groups.items():
        idx_list = list(idx)
        if len(idx_list) < 2: continue
        vals = shuffled.loc[idx_list, "realized_R"].values.copy()
        perm_rng.shuffle(vals)
        shuffled.loc[idx_list, "realized_R"] = vals
    null = discovery_pass(shuffled, perm_rng)
    null_counts.append(null)
    print(f"  perm {k+1:3d}/{N_PERMS}: {null} strict survivors", flush=True)

null_arr = np.array(null_counts)
print(f"\n=== PERMUTATION RESULTS ===", flush=True)
print(f"  real (unshuffled): {real_count}")
print(f"  null distribution: n={len(null_arr)} mean={null_arr.mean():.2f} median={np.median(null_arr):.1f} max={null_arr.max()} std={null_arr.std():.2f}")
print(f"  95th pctile of null: {np.quantile(null_arr, 0.95):.1f}")
p_value = (null_arr >= real_count).mean()
print(f"  p-value (P[null >= real]): {p_value:.4f}")
if p_value < 0.05:
    print(f"  --> SIGNIFICANT")
else:
    print(f"  --> NOT significant")
pd.DataFrame({"null_strict_count": null_arr}).to_csv(
    OUT / "permutation_loosened_null.csv", index=False)
