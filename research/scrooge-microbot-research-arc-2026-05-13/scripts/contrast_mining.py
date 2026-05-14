"""Contrast set mining on MR2_long / EUR_USD.

Goal: find conjunctions of feature conditions where winners are overrepresented
vs losers (lift > 1.5, p < 0.05 Bonferroni-corrected), then validate
out-of-sample and stress-test.

Approach:
  1. Load MR2_long EUR_USD trades.
  2. Discretize features into quartiles → categorical bins.
  3. Build winner & loser transaction sets.
  4. FP-Growth on winners with min_support=0.02.
  5. For each frequent itemset, Fisher's exact test vs losers.
  6. Bonferroni-correct.
  7. Merge overlapping itemsets (Jaccard > 0.5).
  8. Validate on holdout: positive mean R, CI > 0.
  9. Stress test (vol-conditional spread, slippage MC, concentration audits).
"""
import pandas as pd
import numpy as np
from pathlib import Path
from scipy.stats import fisher_exact
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.preprocessing import TransactionEncoder

ROOT = Path("/Users/brock-mini-mac/scrooge-research")
IN = ROOT / "strategy-library-v1"
OUT = ROOT / "reports"

STRATEGY = "MR2_long"
PAIR = "EUR_USD"

print(f"Contrast set mining: {STRATEGY} / {PAIR}\n")

trades = pd.read_parquet(IN / f"trades_{PAIR}.parquet")
trades["entry_ts"] = pd.to_datetime(trades["entry_ts"], utc=True)
trades["era"] = np.where(trades["entry_ts"] < pd.Timestamp("2025-01-01", tz="UTC"),
                          "discovery", "holdout")
trades = trades[(trades["hour_utc"] < 21) | (trades["hour_utc"] >= 23)].copy()
sub = trades[trades.strategy == STRATEGY].copy()
print(f"loaded {len(sub)} {STRATEGY} {PAIR} trades")
sub["is_winner"] = (sub["realized_R"] > 0).astype(int)
print(f"  winners: {sub.is_winner.sum()}, losers: {(1-sub.is_winner).sum()}")
print(f"  overall mean_R: {sub.realized_R.mean():+.3f}")
print(f"  overall win_rate: {sub.is_winner.mean():.1%}")

# Use ONLY discovery period for itemset mining
disc = sub[sub.era == "discovery"].copy()
hold = sub[sub.era == "holdout"].copy()
print(f"  discovery n={len(disc)}, holdout n={len(hold)}")

if disc["is_winner"].sum() < 200 or (1 - disc["is_winner"]).sum() < 200:
    print("FAIL: insufficient winners or losers in discovery (need >=200 each)")
    raise SystemExit(1)

# === Discretize features into quartile bins ===
FEATURES = ["adx14","rsi14","atr_ratio","bb_width_rank","price_pos","vol_ratio",
            "ema20_dist","ema50_dist","zscore20","spread_cost_R"]
CATEGORICAL = ["weekday","hour_utc"]  # used as bin tags

def bin_feature(s, name, n_bins=4):
    s = pd.to_numeric(s, errors="coerce")
    try:
        cats, edges = pd.qcut(s, n_bins, retbins=True, duplicates="drop", labels=False)
    except Exception:
        return pd.Series(["nan"] * len(s), index=s.index)
    out = []
    for v, e in zip(cats, edges if hasattr(edges, "__len__") else []):
        pass
    labels = []
    for v in cats:
        if pd.isna(v):
            labels.append(f"{name}_nan")
        else:
            iv = int(v)
            labels.append(f"{name}_q{iv+1}")
    return pd.Series(labels, index=s.index)

print("\ndiscretizing features into quartiles ...")
items_per_trade = []
for idx, r in disc.iterrows():
    txn = []
    for f in FEATURES:
        v = r.get(f)
        if pd.notna(v):
            # Use the column-wise bin (computed below); placeholder for now
            pass
    items_per_trade.append(txn)

# Vectorized binning
disc_items = pd.DataFrame(index=disc.index)
for f in FEATURES:
    disc_items[f] = bin_feature(disc[f], f, n_bins=4)
# Categorical: weekday + hour buckets
disc_items["weekday"] = "wd_" + disc["weekday"].astype(int).astype(str)
disc_items["hour_bucket"] = "hr_" + (disc["hour_utc"] // 4).astype(int).astype(str)

# Build transactions
transactions = disc_items[FEATURES + ["weekday","hour_bucket"]].apply(
    lambda row: [x for x in row if isinstance(x, str)], axis=1).tolist()
print(f"  transactions: {len(transactions)}")

# Split into winner and loser transactions
winner_idx = disc.index[disc.is_winner == 1].tolist()
loser_idx  = disc.index[disc.is_winner == 0].tolist()
winners_tx = [transactions[disc.index.get_loc(i)] for i in winner_idx]
losers_tx  = [transactions[disc.index.get_loc(i)] for i in loser_idx]
print(f"  winners_tx: {len(winners_tx)}, losers_tx: {len(losers_tx)}")

# === FP-Growth on winners ===
te = TransactionEncoder()
W = te.fit_transform(winners_tx)
W_df = pd.DataFrame(W, columns=te.columns_)
print(f"  winner items: {len(te.columns_)}")
print("  running FP-Growth on winners (min_support=0.05)...")
freq = fpgrowth(W_df, min_support=0.05, max_len=4, use_colnames=True)
freq = freq.sort_values("support", ascending=False)
print(f"  frequent itemsets in winners: {len(freq)}")
freq = freq[freq["itemsets"].apply(lambda s: len(s) >= 2)]
print(f"    of length >= 2: {len(freq)}")

# === For each itemset, Fisher's exact test ===
def count_in_tx(itemset, tx_list):
    items = set(itemset)
    return sum(1 for t in tx_list if items.issubset(t))

print("\n  computing lift + Fisher tests ...")
n_w = len(winners_tx); n_l = len(losers_tx)
rows = []
for _, r in freq.iterrows():
    item = frozenset(r["itemsets"])
    w_in = count_in_tx(item, winners_tx)
    l_in = count_in_tx(item, losers_tx)
    if w_in < 10: continue
    # Fisher's exact: [[w_in, n_w-w_in],[l_in, n_l-l_in]]
    table = [[w_in, n_w - w_in], [l_in, n_l - l_in]]
    try:
        odds, p = fisher_exact(table, alternative="greater")
    except Exception:
        continue
    w_rate = w_in / n_w
    l_rate = l_in / n_l if n_l > 0 else 1
    lift = w_rate / l_rate if l_rate > 0 else float("inf")
    rows.append({
        "itemset": ", ".join(sorted(item)),
        "size": len(item),
        "w_in": w_in, "l_in": l_in,
        "w_rate": w_rate, "l_rate": l_rate,
        "lift": lift, "p": p,
    })
cm = pd.DataFrame(rows)
N_tests = len(cm)
print(f"  tested {N_tests} itemsets")
if N_tests == 0:
    print("no itemsets — abort"); raise SystemExit(0)
alpha_bon = 0.05 / N_tests
print(f"  Bonferroni alpha = {alpha_bon:.3e}")

# Keep lift > 1.5 AND p < bonferroni
strong = cm[(cm["lift"] >= 1.5) & (cm["p"] < alpha_bon)].sort_values("p")
print(f"\n=== STRONG ITEMSETS (lift>=1.5, p<Bonferroni) ===")
print(f"  count: {len(strong)}")
if len(strong) > 0:
    print(strong.head(15).to_string(index=False, float_format="%.4f"))

# === Merge overlapping (Jaccard > 0.5) ===
def jaccard(a, b):
    A = set(a.split(", ")); B = set(b.split(", "))
    return len(A & B) / len(A | B) if (A | B) else 0

merged = []
used = set()
for i, r in strong.reset_index(drop=True).iterrows():
    if i in used: continue
    cluster = [i]
    for j, r2 in strong.reset_index(drop=True).iloc[i+1:].iterrows():
        if jaccard(r["itemset"], r2["itemset"]) > 0.5:
            cluster.append(j); used.add(j)
    used.add(i)
    # Take the smallest itemset in cluster as the merged regime
    cluster_rows = strong.reset_index(drop=True).iloc[cluster]
    rep = cluster_rows.sort_values("size").iloc[0]
    merged.append({
        "regime": rep["itemset"],
        "size": int(rep["size"]),
        "w_in": int(rep["w_in"]),
        "l_in": int(rep["l_in"]),
        "lift": float(rep["lift"]),
        "p": float(rep["p"]),
        "cluster_size": len(cluster),
    })
merged_df = pd.DataFrame(merged)
print(f"\n=== MERGED REGIMES (Jaccard>0.5 cluster reps) ===")
print(f"  count: {len(merged_df)}")
if len(merged_df) > 0:
    print(merged_df.head(15).to_string(index=False, float_format="%.4f"))

# === Validate on HOLDOUT ===
# Build bins on full data using DISCOVERY-period bin edges
hold_items = pd.DataFrame(index=hold.index)
for f in FEATURES:
    # Use the quantiles from disc to define bins
    s_disc = pd.to_numeric(disc[f], errors="coerce").dropna()
    edges = s_disc.quantile([0,0.25,0.5,0.75,1.0]).values
    edges[0] = -np.inf; edges[-1] = np.inf
    s_hold = pd.to_numeric(hold[f], errors="coerce")
    bin_ids = pd.cut(s_hold, bins=edges, labels=False, include_lowest=True)
    hold_items[f] = bin_ids.apply(lambda v: f"{f}_q{int(v)+1}" if pd.notna(v) else f"{f}_nan")
hold_items["weekday"] = "wd_" + hold["weekday"].astype(int).astype(str)
hold_items["hour_bucket"] = "hr_" + (hold["hour_utc"] // 4).astype(int).astype(str)
hold_transactions = hold_items[FEATURES + ["weekday","hour_bucket"]].apply(
    lambda row: set([x for x in row if isinstance(x, str)]), axis=1).tolist()

print("\n=== HOLDOUT VALIDATION ===")
hold_rows = []
for _, m in merged_df.iterrows():
    items = set(m["regime"].split(", "))
    mask = np.array([items.issubset(t) for t in hold_transactions])
    h_in = mask.sum()
    if h_in < 15: continue
    r_h = hold["realized_R"].values[mask]
    mR_h = r_h.mean()
    wr_h = (r_h > 0).mean()
    # CI
    rng = np.random.default_rng(42)
    idx = rng.integers(0, len(r_h), size=(500, len(r_h)))
    ci_lo = float(np.quantile(r_h[idx].mean(axis=1), 0.025))
    hold_rows.append({
        "regime": m["regime"], "lift_disc": m["lift"], "p_disc": m["p"],
        "n_h": int(h_in), "wr_h": float(wr_h), "mean_R_h": float(mR_h),
        "ci_h_lo": ci_lo,
    })
hold_df = pd.DataFrame(hold_rows)
print(f"  regimes with holdout n>=15: {len(hold_df)}")
strict = hold_df[(hold_df["mean_R_h"] > 0) & (hold_df["ci_h_lo"] > 0)].sort_values("ci_h_lo", ascending=False)
print(f"  positive holdout AND CI > 0: {len(strict)}")
print(strict.to_string(index=False, float_format="%.4f"))

# Save
freq.to_csv(OUT / "contrast_mr2long_eurusd_itemsets.csv", index=False)
cm.to_csv(OUT / "contrast_mr2long_eurusd_tested.csv", index=False)
strong.to_csv(OUT / "contrast_mr2long_eurusd_strong.csv", index=False)
merged_df.to_csv(OUT / "contrast_mr2long_eurusd_merged.csv", index=False)
hold_df.to_csv(OUT / "contrast_mr2long_eurusd_holdout.csv", index=False)
strict.to_csv(OUT / "contrast_mr2long_eurusd_strict.csv", index=False)
print(f"\nsaved -> {OUT}/contrast_mr2long_eurusd_*.csv")
