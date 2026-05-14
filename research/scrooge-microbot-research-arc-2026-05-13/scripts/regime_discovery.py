"""Strategy-First Regime Discovery Engine.

For each (trigger, pair):
  1. Build feature matrix at entry — using only bias-free features (corrected
     M15/M1 labels, plus all entry-time indicators already in the v2 parquet).
  2. Fit decision tree on DISCOVERY trades to predict winner (realized_at_2R_net > 0).
  3. Extract tree leaves with win_rate >= 0.40 and n_d >= 50 (the discovered regime).
  4. For each discovered regime, evaluate on HOLDOUT: mean_R, 95% CI lower bound,
     walk-forward across 4 windows, recent 6mo gate.
  5. Output: per (trigger, pair), the discovered regime rules + their out-of-sample stats.

Pilot scope: 5 pairs × 6 trigger families (T1, T2, T7-long, T7-short, T8-long, T8-short).
"""
import pandas as pd
import numpy as np
import json
from pathlib import Path
from sklearn.tree import DecisionTreeClassifier, _tree

ROOT = Path("/tmp/scrooge-research")
PARQUET = ROOT / "raw-m5-v2" / "raw_m5_v2_candidate_events.parquet"
DUKA = ROOT / "dukascopy"
OUT = ROOT / "reports"

# Pilot scope
PAIRS = ["USD_JPY","EUR_USD","GBP_USD","USD_MXN","EUR_JPY"]
TRIGGERS = ["T1_bb_lower_reclaim","T2_bb_upper_reject",
            "T7_pdl_proximity_reversal","T7_pdh_proximity_reversal",
            "T8_pdl_failed_breakdown","T8_pdh_failed_breakout"]

# === Step 1: Corrected M15/H1 labels (load from existing per-pair JSONLs) ===
def load_m5(pair):
    bars = []
    for f in sorted(DUKA.glob(f"{pair}_M5_*.jsonl")):
        for line in open(f):
            try:
                d = json.loads(line)
                bars.append({"time": d["time"],
                             "high": (d["high_bid"]+d["high_ask"])/2,
                             "low":  (d["low_bid"]+d["low_ask"])/2,
                             "close":(d["close_bid"]+d["close_ask"])/2})
            except: pass
    df = pd.DataFrame(bars)
    df["ts"] = pd.to_datetime(df["time"], utc=True)
    return df.sort_values("ts").reset_index(drop=True)

def corrected_features(df_m5):
    """Bias-free M15/H1 features keyed to bar-END times."""
    d = df_m5.set_index("ts")[["high","low","close"]]
    # M15
    m15 = d.resample("15min").agg({"high":"max","low":"min","close":"last"}).dropna()
    m15["ema20"] = m15["close"].ewm(span=20, adjust=False).mean()
    m15["dist_pct"] = (m15["close"] - m15["ema20"]) / m15["ema20"]
    m15["trend"] = np.where(m15["close"] > m15["ema20"]*1.0005, "up",
                    np.where(m15["close"] < m15["ema20"]*0.9995, "down", "flat"))
    m15["atr_pctile"] = ((m15["high"]-m15["low"]).rolling(96).rank(pct=True))  # 24h window
    m15.index = m15.index + pd.Timedelta("15min")
    m15 = m15[["trend","dist_pct","atr_pctile"]].rename(columns={
        "trend":"m15_trend_fix","dist_pct":"m15_ema_dist","atr_pctile":"m15_atr_pctile"
    }).reset_index()
    # H1
    h1 = d.resample("1h").agg({"high":"max","low":"min","close":"last"}).dropna()
    h1["range_rank_48"] = (h1["high"]-h1["low"]).rolling(48).rank(pct=True)
    h1["ema20"] = h1["close"].ewm(span=20, adjust=False).mean()
    h1["dist_pct"] = (h1["close"] - h1["ema20"]) / h1["ema20"]
    h1["regime"] = np.where(h1["range_rank_48"] < 0.25, "consolidation",
                    np.where(h1["range_rank_48"] > 0.75, "breakout", "in_range"))
    h1["trend"] = np.where(h1["close"] > h1["ema20"]*1.001, "up",
                  np.where(h1["close"] < h1["ema20"]*0.999, "down", "flat"))
    h1.index = h1.index + pd.Timedelta("1h")
    h1 = h1[["regime","trend","dist_pct","range_rank_48"]].rename(columns={
        "regime":"h1_regime_fix","trend":"h1_trend_fix",
        "dist_pct":"h1_ema_dist","range_rank_48":"h1_range_rank"
    }).reset_index()
    df = df_m5[["ts"]].sort_values("ts")
    df = pd.merge_asof(df, m15.sort_values("ts"), on="ts", direction="backward")
    df = pd.merge_asof(df, h1.sort_values("ts"),  on="ts", direction="backward")
    return df

print("Building corrected features for pilot pairs ...")
fix_parts = []
for p in PAIRS:
    print(f"  [{p}]")
    fx = corrected_features(load_m5(p))
    fx["pair"] = p
    fix_parts.append(fx)
fix_all = pd.concat(fix_parts, ignore_index=True).rename(columns={"ts":"entry_ts"})
del fix_parts

# === Step 2: Load v2 parquet, filter to pilot, join corrected features ===
print("\nloading v2 parquet ...")
v2 = pd.read_parquet(PARQUET)
v2["entry_ts"] = pd.to_datetime(v2["entry_ts"], utc=True)
v2 = v2[v2["pair"].isin(PAIRS) & v2["trigger_type"].isin(TRIGGERS)].copy()
print(f"pilot candidates: {len(v2):,}")
joined = v2.merge(fix_all, on=["pair","entry_ts"], how="left")
del v2, fix_all

joined["is_winner"] = (joined["realized_at_2R_net"] > 0).astype(int)
joined["era"] = np.where(joined["entry_ts"] < pd.Timestamp("2025-01-01", tz="UTC"), "discovery", "holdout")
joined["hour_utc"] = joined["entry_ts"].dt.hour
joined["weekday"] = joined["entry_ts"].dt.weekday

# Numeric features for the tree
def session_to_num(s):
    base = {"asia":1,"london":2,"overlap":3,"ny_pm":4,"rollover":5}.get(s.split("_")[0], 0)
    q = int(s[-1]) if s[-1].isdigit() else 0
    return base * 10 + q

joined["session_num"] = joined["session_quarter"].apply(session_to_num)
m15_map = {"up":1,"flat":0,"down":-1}
h1_reg_map = {"breakout":2,"in_range":1,"consolidation":0}
h1_tr_map = {"up":1,"flat":0,"down":-1}
joined["m15_trend_num"] = joined["m15_trend_fix"].map(m15_map).fillna(0)
joined["h1_regime_num"] = joined["h1_regime_fix"].map(h1_reg_map).fillna(0)
joined["h1_trend_num"] = joined["h1_trend_fix"].map(h1_tr_map).fillna(0)

FEATURES = [
    "session_num", "hour_utc", "weekday",
    "m15_trend_num", "m15_ema_dist", "m15_atr_pctile",
    "h1_regime_num", "h1_trend_num", "h1_ema_dist", "h1_range_rank",
    "bb_position", "rsi", "ema20_dist_bps",
    "bbw_a_bps", "echo_range_ratio", "atr14", "stop_pips",
    "spread_cost_R",
]

# Numeric coercion + dropna
for col in FEATURES:
    joined[col] = pd.to_numeric(joined[col], errors="coerce")
joined = joined.dropna(subset=FEATURES).copy()
print(f"after dropna on features: {len(joined):,}")

# === Step 3: Per (trigger, pair) decision tree → discovered regimes ===
print("\n=== DISCOVERING REGIMES ===\n")

def tree_paths_to_rules(tree, feature_names):
    """Walk tree, return list of (rule_text, leaf_idx, path_conditions)."""
    t = tree.tree_
    rules = []
    def recurse(node, path):
        if t.children_left[node] == _tree.TREE_LEAF:
            rules.append((path[:], node))
            return
        f = feature_names[t.feature[node]]
        thr = t.threshold[node]
        recurse(t.children_left[node],  path + [(f, "<=", thr)])
        recurse(t.children_right[node], path + [(f, ">",  thr)])
    recurse(0, [])
    return rules


def apply_rule(df, rule):
    mask = pd.Series(True, index=df.index)
    for feat, op, thr in rule:
        if op == "<=": mask &= (df[feat] <= thr)
        else:          mask &= (df[feat] >  thr)
    return mask


def boot_ci(arr, B=500, alpha=0.05, rng=None):
    if rng is None: rng = np.random.default_rng(0)
    n = len(arr)
    if n < 5: return np.nan, np.nan
    idx = rng.integers(0, n, size=(B, n))
    means = arr[idx].mean(axis=1)
    return float(np.quantile(means, alpha/2)), float(np.quantile(means, 1-alpha/2))


hold_end = joined[joined.era == "holdout"]["entry_ts"].max()
recent_start = hold_end - pd.Timedelta(days=180)
wf_edges = pd.date_range(pd.Timestamp("2025-01-01", tz="UTC"),
                          hold_end + pd.Timedelta("1d"), periods=5)

regime_rows = []
rng = np.random.default_rng(42)

for trigger in TRIGGERS:
    for pair in PAIRS:
        sub = joined[(joined.trigger_type == trigger) & (joined.pair == pair)].copy()
        if len(sub) < 200: continue
        sub_d = sub[sub.era == "discovery"]
        sub_h = sub[sub.era == "holdout"]
        if len(sub_d) < 100 or len(sub_h) < 30: continue

        # baseline expectancy
        base_R_d = sub_d["realized_at_2R_net"].mean()
        base_R_h = sub_h["realized_at_2R_net"].mean()
        base_wr_d = sub_d["is_winner"].mean()

        # Fit tree
        clf = DecisionTreeClassifier(max_depth=4, min_samples_leaf=80, random_state=42)
        clf.fit(sub_d[FEATURES].values, sub_d["is_winner"].values)
        rules = tree_paths_to_rules(clf, FEATURES)

        # Score each leaf
        for path, leaf_node in rules:
            mask_d = apply_rule(sub_d, path)
            mask_h = apply_rule(sub_h, path)
            n_d = int(mask_d.sum()); n_h = int(mask_h.sum())
            if n_d < 50 or n_h < 15: continue
            r_d = sub_d.loc[mask_d, "realized_at_2R_net"]
            r_h = sub_h.loc[mask_h, "realized_at_2R_net"]
            wr_d = (r_d > 0).mean()
            wr_h = (r_h > 0).mean()
            if wr_d < 0.40: continue
            mean_R_d = r_d.mean()
            mean_R_h = r_h.mean()
            if mean_R_d <= 0 or mean_R_h <= 0: continue
            ci_d_lo, _ = boot_ci(r_d.values, rng=rng)
            ci_h_lo, _ = boot_ci(r_h.values, rng=rng)
            # walk-forward
            wf_means = []; wf_ns = []
            for i in range(4):
                w = sub_h[mask_h & (sub_h.entry_ts >= wf_edges[i]) & (sub_h.entry_ts < wf_edges[i+1])]
                wf_means.append(float(w["realized_at_2R_net"].mean()) if len(w) > 0 else np.nan)
                wf_ns.append(len(w))
            wf_pos = sum(1 for m in wf_means if (not pd.isna(m)) and m > 0)
            wf_enough = sum(1 for n in wf_ns if n >= 5)
            # recent 6mo
            rec = sub_h[mask_h & (sub_h.entry_ts >= recent_start)]
            rec_arr = rec["realized_at_2R_net"].values
            rec_mean = float(rec_arr.mean()) if len(rec_arr) >= 5 else np.nan
            rec_ci_lo, _ = boot_ci(rec_arr, rng=rng) if len(rec_arr) >= 5 else (np.nan, np.nan)
            # Rule text
            rule_text = " AND ".join(f"{f} {op} {thr:.4g}" for f, op, thr in path) or "ALL"
            regime_rows.append({
                "trigger": trigger, "pair": pair, "rule": rule_text,
                "depth": len(path),
                "n_d": n_d, "wr_d": float(wr_d), "mean_R_d": float(mean_R_d), "ci_d_lo": ci_d_lo,
                "n_h": n_h, "wr_h": float(wr_h), "mean_R_h": float(mean_R_h), "ci_h_lo": ci_h_lo,
                "wf_pos": wf_pos, "wf_enough": wf_enough,
                "n_recent": len(rec_arr), "mean_R_recent": rec_mean, "ci_lo_recent": rec_ci_lo,
                "base_mean_R_d": float(base_R_d), "base_mean_R_h": float(base_R_h),
                "lift_R_d": float(mean_R_d) - float(base_R_d),
                "lift_R_h": float(mean_R_h) - float(base_R_h),
            })

reg = pd.DataFrame(regime_rows)
reg.to_csv(OUT / "regime_discovery_pilot.csv", index=False)
print(f"discovered candidate regimes: {len(reg)}")

# Apply triple gate
ci_pass = reg[(reg.ci_d_lo > 0) & (reg.ci_h_lo > 0)].copy()
print(f"  + 95% CI lower > 0 both eras: {len(ci_pass)}")
robust = ci_pass[(ci_pass.wf_pos >= 3) & (ci_pass.wf_enough >= 3)].copy()
print(f"  + walk-forward >=3/4:         {len(robust)}")
strict = robust[(robust.mean_R_recent.fillna(-99) > 0) & (robust.ci_lo_recent.fillna(-99) > 0)].copy()
print(f"  + recent 6mo + CI > 0:        {len(strict)}")

print("\n=== DISCOVERED REGIME RULES (strict survivors) ===")
if len(strict):
    cols = ["trigger","pair","rule","n_d","wr_d","mean_R_d","ci_d_lo","n_h","wr_h","mean_R_h","ci_h_lo","wf_pos","n_recent","mean_R_recent","ci_lo_recent","lift_R_h"]
    print(strict.sort_values("ci_lo_recent", ascending=False)[cols].to_string(index=False, float_format="%.3f"))
else:
    print("ZERO strict survivors from decision-tree regime discovery either.")
    # Show what passed CI but not walk-forward
    print(f"\nCI-pass but failed walk-forward: {len(ci_pass) - len(robust)}")
    if len(ci_pass):
        print("\nTop 10 CI-pass regimes (sorted by holdout CI lower):")
        cols = ["trigger","pair","rule","n_d","wr_d","mean_R_d","ci_d_lo","n_h","mean_R_h","ci_h_lo","wf_pos"]
        print(ci_pass.sort_values("ci_h_lo", ascending=False)[cols].head(10).to_string(index=False, float_format="%.3f"))

strict.to_csv(OUT / "regime_discovery_strict_survivors.csv", index=False)
ci_pass.to_csv(OUT / "regime_discovery_ci_pass.csv", index=False)

# Per (trigger, pair) baseline expectancy for context
print("\n=== BASELINE EXPECTANCY per (trigger, pair) ===")
base_rows = []
for t in TRIGGERS:
    for p in PAIRS:
        s = joined[(joined.trigger_type == t) & (joined.pair == p)]
        sd = s[s.era == "discovery"]; sh = s[s.era == "holdout"]
        if len(sd) < 100 or len(sh) < 30: continue
        base_rows.append({"trigger": t, "pair": p,
                          "n_d": len(sd), "wr_d": float(sd["is_winner"].mean()),
                          "mean_R_d": float(sd["realized_at_2R_net"].mean()),
                          "n_h": len(sh), "wr_h": float(sh["is_winner"].mean()),
                          "mean_R_h": float(sh["realized_at_2R_net"].mean())})
print(pd.DataFrame(base_rows).to_string(index=False, float_format="%.3f"))
pd.DataFrame(base_rows).to_csv(OUT / "regime_discovery_baseline.csv", index=False)
print(f"\nsaved -> {OUT}")
