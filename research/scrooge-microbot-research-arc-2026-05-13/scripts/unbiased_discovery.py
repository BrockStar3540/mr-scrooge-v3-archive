"""Unbiased regime discovery on all 30 strategies.

Key changes from prior runs:
  1. NO global-performance pre-filter on (strategy, pair). Strategies that are
     globally negative are kept — we want to find their POCKETS.
  2. Discovery does NOT require mean_R_d > 0. The discovery (training) phase
     fits a tree to predict winners. The pocket must hit win_rate >= 0.40 to
     even be tracked. mean_R_d may be negative if the strategy is broken
     globally but the discovered pocket reweights toward winners.
  3. Holdout MUST be positive (mean_R_h > 0) AND CI_h_lo > 0. This is the
     real gate.
  4. Apply all the audited gates: 21-23 UTC killed, hour-concentration ≤ 40%,
     weekday-concentration ≤ 40%, hour_utc removed as a feature, walk-forward
     positive in ≥3/4 windows, recent 6mo positive with CI > 0.
  5. Bonferroni-style: report both raw CI and Bonferroni-corrected CI bound
     (use 1 - alpha/N_tests for N_tests = number of leaves evaluated).
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

# Kill 21-23 UTC (proven artifact band)
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

rng = np.random.default_rng(42)
combos = all_trades.groupby(["strategy","pair"]).size().reset_index(name="n")
combos = combos[combos["n"] >= 300]
print(f"  combos with n>=300: {len(combos)}")

print("\n=== UNBIASED DISCOVERY (no global pre-filter on strategy performance) ===")
total_leaves_evaluated = 0
all_candidates = []
for _, row in combos.iterrows():
    strat, pair = row["strategy"], row["pair"]
    sub = all_trades[(all_trades.strategy == strat) & (all_trades.pair == pair)]
    sub_d = sub[sub.era == "discovery"]; sub_h = sub[sub.era == "holdout"]
    if len(sub_d) < 100 or len(sub_h) < 30: continue
    base_mr_d = sub_d["realized_R"].mean()
    base_mr_h = sub_h["realized_R"].mean()
    clf = DecisionTreeClassifier(max_depth=4, min_samples_leaf=60, random_state=42)
    try: clf.fit(sub_d[FEATURES].values, sub_d["is_winner"].values)
    except: continue
    for path in tree_paths(clf, FEATURES):
        total_leaves_evaluated += 1
        md = apply_rule_np(sub_d, path); mh = apply_rule_np(sub_h, path)
        n_d = md.sum(); n_h = mh.sum()
        if n_d < 50 or n_h < 15: continue
        r_d = sub_d["realized_R"].values[md]; r_h = sub_h["realized_R"].values[mh]
        wr_d = (r_d > 0).mean()
        # Allow negative mean_R_d as long as wr_d high enough
        if wr_d < 0.40: continue
        mR_h = r_h.mean()
        if mR_h <= 0: continue
        ci_h_lo = boot_ci_low(r_h, rng=rng)
        if ci_h_lo <= 0: continue
        # walk-forward
        wf_pos = 0; wf_enough = 0
        for i in range(4):
            wmask = mh & ((sub_h.entry_ts.values >= np.datetime64(wf_edges[i])) &
                          (sub_h.entry_ts.values <  np.datetime64(wf_edges[i+1])))
            rw = sub_h["realized_R"].values[wmask]
            if len(rw) >= 5: wf_enough += 1
            if len(rw) > 0 and rw.mean() > 0: wf_pos += 1
        if wf_pos < 3 or wf_enough < 3: continue
        # recent 6mo
        rec_mask = mh & (sub_h.entry_ts.values >= np.datetime64(recent_start))
        rrec = sub_h["realized_R"].values[rec_mask]
        if len(rrec) < 5 or rrec.mean() <= 0: continue
        ci_rec_lo = boot_ci_low(rrec, rng=rng)
        if ci_rec_lo <= 0: continue
        # FIRE-TIME CONCENTRATION GATE
        all_fires = pd.concat([sub_d[md], sub_h[mh]])
        hr_share_max = float(all_fires["hour_utc"].value_counts(normalize=True).max())
        if hr_share_max > 0.40: continue
        wd_share_max = float(all_fires["weekday"].value_counts(normalize=True).max())
        if wd_share_max > 0.40: continue
        rule_text = " AND ".join(f"{f}{op}{thr:.4g}" for f,op,thr in path) or "ALL"
        all_candidates.append({
            "strategy": strat, "pair": pair, "rule": rule_text,
            "base_mR_d": float(base_mr_d), "base_mR_h": float(base_mr_h),
            "n_d": int(n_d), "wr_d": float(wr_d),
            "mean_R_d": float(r_d.mean()), "ci_d_lo_raw": boot_ci_low(r_d, rng=rng),
            "n_h": int(n_h), "wr_h": float((r_h>0).mean()), "mean_R_h": float(mR_h),
            "ci_h_lo_raw": ci_h_lo,
            "wf_pos": wf_pos,
            "n_recent": len(rrec), "mean_R_recent": float(rrec.mean()), "ci_lo_recent": ci_rec_lo,
            "lift_R_h": float(mR_h) - float(base_mr_h),
            "hr_share_max": hr_share_max, "wd_share_max": wd_share_max,
        })

print(f"  total leaves evaluated: {total_leaves_evaluated}")
res = pd.DataFrame(all_candidates)
print(f"  candidates passing all gates: {len(res)}")

# Bonferroni-corrected CI (alpha = 0.05 / N_tests)
N = total_leaves_evaluated
alpha_bon = 0.05 / max(N, 1)
print(f"\n  Bonferroni: N_tests = {N}, alpha = {alpha_bon:.2e}")
# Bootstrap with stricter alpha
def boot_ci_low_alpha(arr, alpha, B=2000, rng=None):
    n = len(arr)
    if n < 5: return np.nan
    idx = rng.integers(0, n, size=(B, n))
    return float(np.quantile(arr[idx].mean(axis=1), alpha/2))

# For each candidate, compute Bonferroni CI on holdout and recent
bon_lo_h = []; bon_lo_rec = []
for _, c in res.iterrows():
    strat, pair = c["strategy"], c["pair"]
    rule = []
    for part in c["rule"].split(" AND "):
        for op in ("<=",">="," <"," >","<",">"):
            if op.strip() in part:
                p = part.replace("<=","|<=|").replace(">","|>|").replace("<","|<|")
                # simpler parser
                break
    # use the data already filtered
    sub = all_trades[(all_trades.strategy == strat) & (all_trades.pair == pair)]
    sub_h = sub[sub.era == "holdout"]
    # parse rule
    import re
    parts = re.split(r"\s+AND\s+", c["rule"])
    rule_tuples = []
    for pa in parts:
        m = re.match(r"^([\w_]+)(<=|>=|<|>|=)(-?[\d.eE+]+)$", pa.strip())
        if m: rule_tuples.append((m.group(1), m.group(2), float(m.group(3))))
    mh = apply_rule_np(sub_h, rule_tuples)
    r_h = sub_h["realized_R"].values[mh]
    rec_mask = mh & (sub_h.entry_ts.values >= np.datetime64(recent_start))
    r_rec = sub_h["realized_R"].values[rec_mask]
    bon_lo_h.append(boot_ci_low_alpha(r_h, alpha_bon, rng=rng))
    bon_lo_rec.append(boot_ci_low_alpha(r_rec, alpha_bon, rng=rng) if len(r_rec) >= 5 else np.nan)
res["ci_h_lo_bon"] = bon_lo_h
res["ci_rec_lo_bon"] = bon_lo_rec

# Survivors after Bonferroni
res["bonferroni_survives"] = (res["ci_h_lo_bon"] > 0) & (res["ci_rec_lo_bon"].fillna(-99) > 0)

print(f"\n  surviving Bonferroni: {res['bonferroni_survives'].sum()}")

res.to_csv(OUT / "unbiased_all_candidates.csv", index=False)

print("\n=== ALL CANDIDATES (raw, before Bonferroni) ===")
if len(res):
    cols = ["strategy","pair","rule","n_d","wr_d","mean_R_d","base_mR_d","n_h","wr_h","mean_R_h","ci_h_lo_raw","wf_pos","n_recent","mean_R_recent","ci_lo_recent","lift_R_h","hr_share_max","wd_share_max"]
    print(res.sort_values("ci_lo_recent", ascending=False)[cols].to_string(index=False, float_format="%.3f"))

print("\n=== BONFERRONI-SURVIVING CANDIDATES ===")
bs = res[res["bonferroni_survives"]]
if len(bs):
    cols = ["strategy","pair","rule","n_d","n_h","mean_R_d","mean_R_h","ci_h_lo_bon","n_recent","mean_R_recent","ci_rec_lo_bon"]
    print(bs.sort_values("ci_rec_lo_bon", ascending=False)[cols].to_string(index=False, float_format="%.3f"))
else:
    print("  ZERO Bonferroni-surviving candidates.")

# Per-strategy summary
print("\n=== CANDIDATES BY STRATEGY FAMILY ===")
if len(res):
    sum_s = res.groupby("strategy").agg(
        n_candidates=("rule","size"),
        pairs=("pair","nunique"),
        best_mR_h=("mean_R_h","max"),
        best_ci_h_raw=("ci_h_lo_raw","max"),
        best_ci_rec=("ci_lo_recent","max"),
    ).reset_index().sort_values("n_candidates", ascending=False)
    print(sum_s.to_string(index=False, float_format="%.3f"))
