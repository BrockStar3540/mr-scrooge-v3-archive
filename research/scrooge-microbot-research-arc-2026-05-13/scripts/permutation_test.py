"""Step B: Permutation test on the Step-A pipeline.

For each iteration:
  1. Shuffle realized_R within each (strategy, pair) group.
  2. Run the same Step A discovery + triple gate.
  3. Count strict survivors.

Output: distribution of "survivors under null" vs the real Step A count of 14.
If real 14 falls in the upper tail (>=95th percentile of null), the edge is real.

Compute budget: 50 shuffles. ~3 min each on subset of combos = ~2.5 hours.
"""
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.tree import DecisionTreeClassifier, _tree
import sys

ROOT = Path("/tmp/scrooge-research")
IN  = ROOT / "strategy-library-v1"
OUT = ROOT / "reports"
N_PERMUTATIONS = int(sys.argv[1]) if len(sys.argv) > 1 else 50

PAIRS = ["EUR_USD","GBP_USD","AUD_USD","NZD_USD","USD_JPY","USD_CHF","USD_CAD","USD_MXN",
         "EUR_GBP","EUR_AUD","EUR_NZD","EUR_CAD","EUR_CHF","EUR_JPY",
         "GBP_AUD","GBP_NZD","GBP_CAD","GBP_CHF","GBP_JPY",
         "AUD_CAD","AUD_CHF","AUD_JPY","AUD_NZD","CAD_JPY","CHF_JPY","NZD_JPY"]

FEATURES = ["adx14","rsi14","atr_ratio","bb_width_rank","price_pos","vol_ratio",
            "ema20_dist","ema50_dist","zscore20","weekday","spread_cost_R"]

print(f"Permutation test: {N_PERMUTATIONS} iterations")
print("loading data ...")
parts = []
for p in PAIRS:
    f = IN / f"trades_{p}.parquet"
    if not f.exists(): continue
    parts.append(pd.read_parquet(f))
all_trades = pd.concat(parts, ignore_index=True)
all_trades["entry_ts"] = pd.to_datetime(all_trades["entry_ts"], utc=True)
all_trades["era"] = np.where(all_trades["entry_ts"] < pd.Timestamp("2025-01-01", tz="UTC"), "discovery", "holdout")
# kill rollover
all_trades = all_trades[(all_trades["hour_utc"] < 21) | (all_trades["hour_utc"] >= 22)].copy()
print(f"  {len(all_trades):,} trades after rollover kill")

# Pre-filter feature dropna
all_trades = all_trades.dropna(subset=FEATURES + ["realized_R"]).copy()
print(f"  {len(all_trades):,} after dropna on features")


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
        if op == "<=": m &= (col <= thr)
        else:          m &= (col >  thr)
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
combos = combos[combos["n"] >= 300]
print(f"  combos: {len(combos)}")

def run_discovery(trades_df, rng):
    """Returns strict-survivor count."""
    n_strict = 0
    for _, row in combos.iterrows():
        strat, pair = row["strategy"], row["pair"]
        sub = trades_df[(trades_df.strategy == strat) & (trades_df.pair == pair)]
        sub_d = sub[sub.era == "discovery"]; sub_h = sub[sub.era == "holdout"]
        if len(sub_d) < 100 or len(sub_h) < 30: continue
        # winner label from possibly-shuffled R
        wins_d = (sub_d["realized_R"].values > 0).astype(int)
        if wins_d.sum() < 10 or wins_d.sum() > len(wins_d) - 10: continue
        clf = DecisionTreeClassifier(max_depth=4, min_samples_leaf=60, random_state=42)
        try: clf.fit(sub_d[FEATURES].values, wins_d)
        except: continue
        for path in tree_paths(clf, FEATURES):
            md = apply_rule(sub_d, path); mh = apply_rule(sub_h, path)
            n_d = md.sum(); n_h = mh.sum()
            if n_d < 50 or n_h < 15: continue
            r_d = sub_d["realized_R"].values[md]
            r_h = sub_h["realized_R"].values[mh]
            wr_d = (r_d > 0).mean()
            if wr_d < 0.40: continue
            mR_d = r_d.mean(); mR_h = r_h.mean()
            if mR_d <= 0 or mR_h <= 0: continue
            ci_d_lo = boot_ci_low(r_d, rng=rng)
            ci_h_lo = boot_ci_low(r_h, rng=rng)
            if ci_d_lo <= 0 or ci_h_lo <= 0: continue
            # walk-forward
            wf_pos = 0; wf_enough = 0
            for i in range(4):
                w_mask = mh & ((sub_h.entry_ts.values >= np.datetime64(wf_edges[i])) &
                               (sub_h.entry_ts.values <  np.datetime64(wf_edges[i+1])))
                r_w = sub_h["realized_R"].values[w_mask]
                if len(r_w) >= 5: wf_enough += 1
                if len(r_w) > 0 and r_w.mean() > 0: wf_pos += 1
            if wf_pos < 3 or wf_enough < 3: continue
            # recent
            rec_mask = mh & (sub_h.entry_ts.values >= np.datetime64(recent_start))
            r_rec = sub_h["realized_R"].values[rec_mask]
            if len(r_rec) < 5: continue
            if r_rec.mean() <= 0: continue
            ci_rec_lo = boot_ci_low(r_rec, rng=rng)
            if ci_rec_lo <= 0: continue
            n_strict += 1
    return n_strict

# Real (unshuffled) - sanity check we get ~14
print("\nsanity check (no shuffle): expected ~14 strict survivors")
real_count = run_discovery(all_trades, np.random.default_rng(42))
print(f"  got: {real_count}")

# Permutations
print(f"\nrunning {N_PERMUTATIONS} permutations ...")
null_counts = []
rng_master = np.random.default_rng(0)
for k in range(N_PERMUTATIONS):
    perm_seed = rng_master.integers(0, 2**31)
    perm_rng = np.random.default_rng(perm_seed)
    # Shuffle realized_R within each (strategy, pair) group, preserving entry_ts order
    shuffled = all_trades.copy()
    for (strat, pair), idx in shuffled.groupby(["strategy","pair"]).groups.items():
        idx = list(idx)
        if len(idx) < 2: continue
        vals = shuffled.loc[idx, "realized_R"].values.copy()
        perm_rng.shuffle(vals)
        shuffled.loc[idx, "realized_R"] = vals
    null = run_discovery(shuffled, perm_rng)
    null_counts.append(null)
    print(f"  perm {k+1:3d}/{N_PERMUTATIONS}: {null} strict survivors", flush=True)

null_arr = np.array(null_counts)
print(f"\n=== PERMUTATION RESULTS ===")
print(f"  real (unshuffled): {real_count}")
print(f"  null distribution: n={len(null_arr)}, mean={null_arr.mean():.2f}, median={np.median(null_arr):.1f}, max={null_arr.max()}, std={null_arr.std():.2f}")
print(f"  95th pctile of null: {np.quantile(null_arr, 0.95):.1f}")
print(f"  99th pctile of null: {np.quantile(null_arr, 0.99):.1f}")
p_value = (null_arr >= real_count).mean()
print(f"  p-value (P[null >= real]): {p_value:.4f}")
if p_value < 0.05:
    print(f"  → Real survivors EXCEED 95th percentile of null. STATISTICALLY SIGNIFICANT.")
else:
    print(f"  → Real survivors NOT significant vs null.")

pd.DataFrame({"perm": range(len(null_arr)), "null_strict_count": null_arr}).to_csv(
    OUT / "permutation_null_distribution.csv", index=False)
print(f"\nsaved -> {OUT}/permutation_null_distribution.csv")
