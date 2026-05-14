"""Loosened unbiased regime discovery.

Per Brock 2026-05-13 directive: previous unbiased run still imposed a global
win_rate >= 0.40 gate, which is unfair to low-WR / high-R-multiple pockets.

This pass:
  - REMOVE win_rate gate (use mean R only)
  - min_samples_leaf=30 (was 60) — let rarer pockets emerge
  - require n_d >= 30, n_h >= 15
  - require mean_R_d > 0 AND mean_R_h > 0
  - require CI lower bound > 0 in HOLDOUT only (discovery CI used for ranking)
  - require recent 6mo positive (no CI gate, just sign — to avoid killing
    rare cells)
  - keep fire-time concentration audit (≤40% any hour, ≤40% any weekday)
  - rollover hours 21-23 UTC excluded
  - hour_utc not a feature

Runs on Mini.
"""
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.tree import DecisionTreeClassifier, _tree

ROOT = Path("/Users/brock-mini-mac/scrooge-research")
IN = ROOT / "strategy-library-v1"
OUT = ROOT / "reports"
OUT.mkdir(exist_ok=True, parents=True)

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
all_trades["era"] = np.where(all_trades["entry_ts"] < pd.Timestamp("2025-01-01", tz="UTC"),
                              "discovery", "holdout")
all_trades["is_winner"] = (all_trades["realized_R"] > 0).astype(int)
print(f"  {len(all_trades):,} total")

before = len(all_trades)
all_trades = all_trades[(all_trades["hour_utc"] < 21) | (all_trades["hour_utc"] >= 23)].copy()
print(f"  killed 21-23 UTC: {before - len(all_trades):,}")
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
        if op == "<=": m &= col <= thr
        else:          m &= col > thr
    return m

def boot_ci_low(arr, B=400, alpha=0.05, rng=None):
    n = len(arr)
    if n < 5: return np.nan
    idx = rng.integers(0, n, size=(B, n))
    return float(np.quantile(arr[idx].mean(axis=1), alpha/2))


hold_end = all_trades[all_trades.era=="holdout"]["entry_ts"].max()
recent_start = hold_end - pd.Timedelta(days=180)
wf_edges = pd.date_range(pd.Timestamp("2025-01-01", tz="UTC"),
                          hold_end + pd.Timedelta("1d"), periods=5)

# === Use REGRESSION tree on mean R instead of classification on is_winner ===
# This is the philosophical fix: optimize directly for mean R, not raw win-rate.
from sklearn.tree import DecisionTreeRegressor

rng = np.random.default_rng(42)
combos = all_trades.groupby(["strategy","pair"]).size().reset_index(name="n")
combos = combos[combos["n"] >= 200]
print(f"  combos n>=200: {len(combos)}")

print("\n=== LOOSENED DISCOVERY (regressor on mean R, no WR gate, min_leaf=30) ===")

total_leaves = 0
rows = []
for _, row in combos.iterrows():
    strat, pair = row["strategy"], row["pair"]
    sub = all_trades[(all_trades.strategy == strat) & (all_trades.pair == pair)]
    sub_d = sub[sub.era == "discovery"]; sub_h = sub[sub.era == "holdout"]
    if len(sub_d) < 100 or len(sub_h) < 30: continue
    base_mr_d = float(sub_d["realized_R"].mean())
    base_mr_h = float(sub_h["realized_R"].mean())

    # Regress mean R on features. The tree finds splits that maximize variance
    # in mean R between regions.
    reg = DecisionTreeRegressor(max_depth=4, min_samples_leaf=30, random_state=42)
    try: reg.fit(sub_d[FEATURES].values, sub_d["realized_R"].values)
    except: continue

    for path in tree_paths(reg, FEATURES):
        total_leaves += 1
        md = apply_rule_np(sub_d, path); mh = apply_rule_np(sub_h, path)
        n_d = md.sum(); n_h = mh.sum()
        if n_d < 30 or n_h < 15: continue
        r_d = sub_d["realized_R"].values[md]; r_h = sub_h["realized_R"].values[mh]
        mR_d = r_d.mean(); mR_h = r_h.mean()
        # No win_rate gate.
        if mR_d <= 0 or mR_h <= 0: continue
        ci_h_lo = boot_ci_low(r_h, rng=rng)
        if ci_h_lo <= 0: continue  # holdout CI gate retained
        # walk-forward
        wf_pos = 0; wf_enough = 0
        for i in range(4):
            wmask = mh & ((sub_h.entry_ts.values >= np.datetime64(wf_edges[i])) &
                          (sub_h.entry_ts.values <  np.datetime64(wf_edges[i+1])))
            rw = sub_h["realized_R"].values[wmask]
            if len(rw) >= 3: wf_enough += 1
            if len(rw) > 0 and rw.mean() > 0: wf_pos += 1
        if wf_pos < 3: continue
        # recent 6mo positive (no CI gate, just sign)
        rec_mask = mh & (sub_h.entry_ts.values >= np.datetime64(recent_start))
        rrec = sub_h["realized_R"].values[rec_mask]
        if len(rrec) < 3 or rrec.mean() <= 0: continue
        rec_ci_lo = boot_ci_low(rrec, rng=rng) if len(rrec) >= 5 else np.nan
        # concentration audits
        all_fires = pd.concat([sub_d[md], sub_h[mh]])
        if len(all_fires) == 0: continue
        hr_share = float(all_fires["hour_utc"].value_counts(normalize=True).max())
        wd_share = float(all_fires["weekday"].value_counts(normalize=True).max())
        if hr_share > 0.40 or wd_share > 0.40: continue
        rule_text = " AND ".join(f"{f}{op}{thr:.4g}" for f,op,thr in path) or "ALL"
        wr_d = float((r_d > 0).mean())
        wr_h = float((r_h > 0).mean())
        rows.append({
            "strategy": strat, "pair": pair, "rule": rule_text,
            "base_mR_d": base_mr_d, "base_mR_h": base_mr_h,
            "n_d": int(n_d), "wr_d": wr_d, "mean_R_d": float(mR_d),
            "n_h": int(n_h), "wr_h": wr_h, "mean_R_h": float(mR_h), "ci_h_lo": ci_h_lo,
            "wf_pos": wf_pos,
            "n_recent": len(rrec), "mean_R_recent": float(rrec.mean()), "ci_lo_recent": rec_ci_lo,
            "hr_share_max": hr_share, "wd_share_max": wd_share,
            "lift_R_h": float(mR_h) - base_mr_h,
        })

print(f"  leaves evaluated: {total_leaves}")
res = pd.DataFrame(rows)
print(f"  candidates passing all gates: {len(res)}")
res.to_csv(OUT / "loosened_discovery_candidates.csv", index=False)

if len(res):
    print("\n=== ALL CANDIDATES (sorted by ci_h_lo) ===")
    cols = ["strategy","pair","rule","n_d","wr_d","mean_R_d","base_mR_d",
            "n_h","wr_h","mean_R_h","ci_h_lo","wf_pos",
            "n_recent","mean_R_recent","ci_lo_recent","hr_share_max","wd_share_max","lift_R_h"]
    print(res.sort_values("ci_h_lo", ascending=False)[cols].head(40).to_string(index=False, float_format="%.3f"))

    print("\n=== BY STRATEGY FAMILY ===")
    fam = res.groupby("strategy").agg(
        n_candidates=("rule","size"),
        pairs=("pair","nunique"),
        best_mR_h=("mean_R_h","max"),
        best_ci_h=("ci_h_lo","max"),
        best_recent_R=("mean_R_recent","max"),
    ).reset_index().sort_values("n_candidates", ascending=False)
    print(fam.to_string(index=False, float_format="%.3f"))

    print("\n=== LOW-WR HIGH-R POCKETS (WR < 0.40 but mean_R > 0 in holdout — Brock's case) ===")
    low_wr = res[res.wr_h < 0.40].sort_values("mean_R_h", ascending=False)
    print(f"  count: {len(low_wr)}")
    if len(low_wr):
        print(low_wr[["strategy","pair","rule","n_h","wr_h","mean_R_h","ci_h_lo","n_recent","mean_R_recent"]].head(15).to_string(index=False, float_format="%.3f"))
else:
    print("  NO candidates pass under loosened gates.")
print(f"\nsaved -> {OUT}/loosened_discovery_candidates.csv")
