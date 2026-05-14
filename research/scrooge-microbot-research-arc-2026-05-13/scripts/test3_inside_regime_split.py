"""Test 3: split mixed regimes from the inside.

For each (strategy_id, pair, direction, technical_regime_53) cell where
winners and losers cluster TOGETHER in mass (n >= 200, n_winners >= 50,
n_losers >= 50, win_rate roughly between 15% and 60%), find sub-conditions
that separate winners from losers WITHIN the regime.

Approach:
  - For each such cell, compute per-factor Cohen's d (winners vs losers) IN
    that cell only.
  - For factors with |d| >= 0.3, build a "custom sub-regime" by binning the
    factor and identifying the bin(s) where winners cluster.
  - Use a small decision tree (max_depth=2, min_samples_leaf=30) on the
    cell's trades to find the cleanest split.

Output: per dominant (strategy, pair, direction, regime) cell:
  - top 3 separating factors
  - the decision-tree-derived sub-regime rule
  - sub-cell stats: n, win_rate, mean_R for the SPLIT cell
  - chronological out-of-sample check: split learned on 2019-2023, applied
    to 2024-Apr 2026

This is the right kind of analysis: skip the 53-regime theory, learn
sub-regimes empirically from the data inside each mass-mixed regime.
"""
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.tree import DecisionTreeClassifier, _tree

ROOT = Path("/Users/brock-mini-mac/scrooge-research")
PARQUET = ROOT / "all_strategies_all_pairs_trades.parquet"

NUMERIC_FACTORS = ["ADX14","ATR_ratio","BB_compress","RSI14","price_pos","volume_ratio"]
TRAIN_END = pd.Timestamp("2024-01-01", tz="UTC")

print("loading parquet ...")
cols = ["strategy_id","pair","direction","is_win","realized_R","entry_ts",
        "technical_regime_53","technical_regime_desc"] + NUMERIC_FACTORS
df = pd.read_parquet(PARQUET, columns=cols)
df["entry_ts"] = pd.to_datetime(df["entry_ts"], utc=True)
df["weekday"] = df["entry_ts"].dt.weekday.astype(float)
df["hour_utc"] = df["entry_ts"].dt.hour.astype(float)
NUMERIC_FACTORS = NUMERIC_FACTORS + ["weekday","hour_utc"]
print(f"  {len(df):,} trades")

# === Identify mass-mixed regime cells ===
regime_cell = df.groupby(["strategy_id","pair","direction","technical_regime_53","technical_regime_desc"]).agg(
    n=("is_win","size"),
    w=("is_win","sum"),
    mean_R=("realized_R","mean"),
).reset_index()
regime_cell["w"] = regime_cell["w"].astype(int)
regime_cell["l"] = regime_cell["n"] - regime_cell["w"]
regime_cell["wr"] = regime_cell["w"] / regime_cell["n"]
mass_mixed = regime_cell[
    (regime_cell["n"] >= 200) &
    (regime_cell["w"] >= 50) &
    (regime_cell["l"] >= 50) &
    (regime_cell["wr"] >= 0.10) &
    (regime_cell["wr"] <= 0.70)
].sort_values("n", ascending=False)
print(f"\nmass-mixed (n>=200, w>=50, l>=50, 10%<=wr<=70%): {len(mass_mixed)} cells")

def cohens_d(w_arr, l_arr):
    w_arr = pd.to_numeric(w_arr, errors="coerce").dropna()
    l_arr = pd.to_numeric(l_arr, errors="coerce").dropna()
    if len(w_arr) < 20 or len(l_arr) < 20: return np.nan
    s1, s2 = w_arr.std(ddof=1), l_arr.std(ddof=1)
    pooled = np.sqrt(((len(w_arr)-1)*s1**2 + (len(l_arr)-1)*s2**2) / (len(w_arr) + len(l_arr) - 2))
    if pooled == 0 or pd.isna(pooled): return np.nan
    return float((w_arr.mean() - l_arr.mean()) / pooled)

def tree_paths(tree, fnames):
    t = tree.tree_; rules = []
    def rec(node, path):
        if t.children_left[node] == _tree.TREE_LEAF:
            rules.append(path[:]); return
        f = fnames[t.feature[node]]; thr = t.threshold[node]
        rec(t.children_left[node], path + [(f,"<=",thr)])
        rec(t.children_right[node], path + [(f,">",thr)])
    rec(0, []); return rules

def apply_rule(df_, rule):
    m = np.ones(len(df_), dtype=bool)
    for f, op, thr in rule:
        col = df_[f].values
        if op == "<=": m &= col <= thr
        else:          m &= col > thr
    return m

def boot_ci_low(arr, B=300, rng=None):
    n = len(arr)
    if n < 5: return -np.inf
    idx = rng.integers(0, n, size=(B, n))
    return float(np.quantile(arr[idx].mean(axis=1), 0.025))

rng = np.random.default_rng(42)
results = []
print(f"\nsplitting cells (max_depth=2 decision tree per cell) ...")

for ci, c in mass_mixed.iterrows():
    strat = c["strategy_id"]; pair = c["pair"]; dirn = c["direction"]
    reg = c["technical_regime_53"]; reg_desc = c["technical_regime_desc"]
    sub = df[(df.strategy_id == strat) & (df.pair == pair) &
             (df.direction == dirn) & (df.technical_regime_53 == reg)].copy()
    sub = sub.dropna(subset=NUMERIC_FACTORS)
    if len(sub) < 200: continue
    train = sub[sub.entry_ts < TRAIN_END]
    test = sub[sub.entry_ts >= TRAIN_END]
    if len(train) < 100 or len(test) < 30: continue
    if train["is_win"].sum() < 30 or (1 - train["is_win"]).sum() < 30: continue

    # Per-factor Cohen's d in train
    win_train = train[train.is_win == True]
    los_train = train[train.is_win == False]
    factor_ds = []
    for f in NUMERIC_FACTORS:
        d = cohens_d(win_train[f], los_train[f])
        if not pd.isna(d):
            factor_ds.append((f, d))
    factor_ds.sort(key=lambda x: abs(x[1]), reverse=True)
    top3 = factor_ds[:3]

    # Decision tree max_depth=2 on train within this cell
    clf = DecisionTreeClassifier(max_depth=2, min_samples_leaf=30, random_state=42)
    try: clf.fit(train[NUMERIC_FACTORS].values, train["is_win"].astype(int).values)
    except: continue
    # Walk leaves, pick the one with highest win_rate on TRAIN that has >=20 trades
    best_rule = None; best_leaf = None
    for path in tree_paths(clf, NUMERIC_FACTORS):
        m_train = apply_rule(train, path)
        if m_train.sum() < 30: continue
        wr_train = train["is_win"].values[m_train].mean()
        if best_leaf is None or wr_train > best_leaf["wr_train"]:
            best_leaf = {
                "rule": path, "n_train": int(m_train.sum()),
                "wr_train": float(wr_train),
                "mean_R_train": float(train["realized_R"].values[m_train].mean()),
            }
            best_rule = path
    if best_rule is None: continue

    # Apply to test
    m_test = apply_rule(test, best_rule)
    n_test = int(m_test.sum())
    if n_test < 15: continue
    test_R = test["realized_R"].values[m_test]
    test_wr = float(test["is_win"].values[m_test].mean())
    test_mean_R = float(test_R.mean())
    test_ci_lo = boot_ci_low(test_R, rng=rng)
    rule_text = " AND ".join(f"{f}{op}{thr:.4g}" for f,op,thr in best_rule) or "ALL"

    results.append({
        "strategy_id": strat, "pair": pair, "direction": dirn,
        "regime": reg, "regime_desc": reg_desc,
        "cell_n_total": int(c["n"]), "cell_winners": int(c["w"]),
        "cell_losers": int(c["l"]), "cell_wr": round(float(c["wr"]), 4),
        "cell_mean_R": round(float(c["mean_R"]), 4),
        "top1_factor": top3[0][0] if len(top3) > 0 else "",
        "top1_d":      round(top3[0][1], 4) if len(top3) > 0 else None,
        "top2_factor": top3[1][0] if len(top3) > 1 else "",
        "top2_d":      round(top3[1][1], 4) if len(top3) > 1 else None,
        "top3_factor": top3[2][0] if len(top3) > 2 else "",
        "top3_d":      round(top3[2][1], 4) if len(top3) > 2 else None,
        "split_rule": rule_text,
        "split_n_train": best_leaf["n_train"],
        "split_wr_train": round(best_leaf["wr_train"], 4),
        "split_mean_R_train": round(best_leaf["mean_R_train"], 4),
        "split_n_test": n_test,
        "split_wr_test": round(test_wr, 4),
        "split_mean_R_test": round(test_mean_R, 4),
        "split_ci_lo_test": round(test_ci_lo, 4),
        "wr_lift_test": round(test_wr / float(c["wr"]), 4) if c["wr"] > 0 else None,
    })

res = pd.DataFrame(results)
res = res.sort_values("split_ci_lo_test", ascending=False)
res.to_csv(ROOT / "test3_inside_regime_splits.csv", index=False)
print(f"\nprocessed {len(mass_mixed)} mass-mixed cells -> {len(res)} with valid splits")

if len(res):
    print(f"\n=== SPLITS WHERE TEST MEAN R > 0 AND CI LOWER > 0 ===")
    survivors = res[(res.split_mean_R_test > 0) & (res.split_ci_lo_test > 0)]
    print(f"  count: {len(survivors)}")
    if len(survivors):
        cols = ["strategy_id","pair","direction","regime","regime_desc",
                "cell_wr","split_rule","split_n_train","split_wr_train",
                "split_n_test","split_wr_test","split_mean_R_test","split_ci_lo_test","wr_lift_test"]
        print(survivors[cols].head(30).to_string(index=False, float_format="%.4f"))

    print(f"\n=== TOP 20 BY TEST CI LOWER (incl. negatives) ===")
    cols = ["strategy_id","pair","direction","regime","cell_wr","top1_factor","top1_d","top2_factor","top2_d",
            "split_rule","split_n_test","split_wr_test","split_mean_R_test","split_ci_lo_test"]
    print(res[cols].head(20).to_string(index=False, float_format="%.4f"))

    print(f"\n=== TOP FACTORS as #1 DISCRIMINATOR ACROSS CELLS ===")
    fc = res["top1_factor"].value_counts()
    print(fc.to_string())

print(f"\nsaved test3_inside_regime_splits.csv: {len(res)} rows")
