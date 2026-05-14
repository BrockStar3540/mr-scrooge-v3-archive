"""Multi-(strategy, pair, direction) contrast set mining.

For each combination with n_winners >= 200 AND n_losers >= 200:
  - Discretize continuous features into quartiles (per-combo, on TRAIN only)
  - FP-Growth on winners with min_support = max(0.02, 20/n_winners)
  - Fisher's exact test vs losers
  - Bonferroni correction per combo
  - Merge overlapping itemsets (Jaccard >= 0.5)
  - Validate on TEST (chronological split: train < 2024-01-01)
  - Keep if test mean R > 0 AND test CI lower > 0

Output: contrast_regimes_discovered.csv
"""
import pandas as pd
import numpy as np
from pathlib import Path
from scipy.stats import fisher_exact
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.preprocessing import TransactionEncoder
import sys, time

ROOT = Path("/Users/brock-mini-mac/scrooge-research")
PARQUET = ROOT / "all_strategies_all_pairs_trades.parquet"
OUT = ROOT / "reports"
OUT.mkdir(exist_ok=True, parents=True)
RESULT_CSV = OUT / "contrast_regimes_discovered.csv"

CONT_FEATURES = ["ADX14","ATR_ratio","BB_compress","RSI14","price_pos","volume_ratio"]
# session_bucket and technical_regime_53 are already categorical
# hour_utc binned into 4-hour buckets
TRAIN_END = pd.Timestamp("2024-01-01", tz="UTC")

print("loading foundational parquet ...", flush=True)
t0 = time.time()
full = pd.read_parquet(PARQUET)
full["entry_ts"] = pd.to_datetime(full["entry_ts"], utc=True)
print(f"  loaded {len(full):,} rows in {time.time()-t0:.1f}s", flush=True)

# Build cell key
combos = full.groupby(["strategy_id","pair","direction"]).agg(
    n_total=("realized_R","size"),
    n_winners=("is_win","sum"),
).reset_index()
combos["n_losers"] = combos["n_total"] - combos["n_winners"]
combos = combos[(combos["n_winners"] >= 200) & (combos["n_losers"] >= 200)]
print(f"  combos with n_winners>=200 AND n_losers>=200: {len(combos):,}", flush=True)


def bin_quartile(s_train, s_full):
    """Compute quartile edges from TRAIN; apply to FULL (train+test)."""
    s_train_num = pd.to_numeric(s_train, errors="coerce").dropna()
    if len(s_train_num) < 4:
        return pd.Series([None] * len(s_full), index=s_full.index, dtype="object")
    try:
        _, edges = pd.qcut(s_train_num, 4, retbins=True, duplicates="drop")
    except Exception:
        return pd.Series([None] * len(s_full), index=s_full.index, dtype="object")
    if len(edges) < 3:
        return pd.Series([None] * len(s_full), index=s_full.index, dtype="object")
    edges = list(edges)
    edges[0] = -np.inf; edges[-1] = np.inf
    bin_ids = pd.cut(pd.to_numeric(s_full, errors="coerce"), bins=edges,
                     labels=False, include_lowest=True)
    return bin_ids


def build_transactions(df, bin_edges_per_feature):
    """Build a list of frozensets per row."""
    n = len(df)
    feature_cols = []
    for f in CONT_FEATURES:
        bin_id = bin_edges_per_feature.get(f)
        if bin_id is None: continue
        col = []
        for v in bin_id.values:
            if pd.isna(v): col.append(None)
            else: col.append(f"{f}_q{int(v)+1}")
        feature_cols.append(col)
    # session_bucket
    sb = df["session_bucket"].astype(str).values
    feature_cols.append([f"sess_{x}" for x in sb])
    # hour_bucket
    hb = (df["hour_utc"].values // 4).astype(int)
    feature_cols.append([f"hr_{x}" for x in hb])
    # technical_regime_53
    tr = df["technical_regime_53"].astype(str).values
    feature_cols.append([f"tr53_{x}" for x in tr])
    # weekday
    wd = df["entry_ts"].dt.weekday.values
    feature_cols.append([f"wd_{x}" for x in wd])
    # Transpose: each row is a list of items
    transactions = []
    for i in range(n):
        items = []
        for fc in feature_cols:
            v = fc[i]
            if v is not None and "nan" not in v.lower():
                items.append(v)
        transactions.append(items)
    return transactions


def boot_ci_low(arr, B=400, rng=None):
    n = len(arr)
    if n < 5: return -np.inf
    idx = rng.integers(0, n, size=(B, n))
    return float(np.quantile(arr[idx].mean(axis=1), 0.025))


def jaccard(a, b):
    A = set(a); B = set(b)
    return len(A & B) / len(A | B) if (A | B) else 0


def process_combo(strat, pair, direction, sub, rng):
    """Run the full contrast pipeline for one combo. Return list of result dicts."""
    sub = sub.copy()
    train = sub[sub["entry_ts"] < TRAIN_END]
    test  = sub[sub["entry_ts"] >= TRAIN_END]
    if len(train) < 500 or len(test) < 50:
        return []
    n_w_train = int(train["is_win"].sum())
    n_l_train = int(len(train) - n_w_train)
    if n_w_train < 200 or n_l_train < 200:
        return []

    # Compute bin edges on full train, apply to full sub (train+test)
    bin_per_f = {}
    for f in CONT_FEATURES:
        bin_per_f[f] = bin_quartile(train[f], sub[f])
    # Build transactions for train (mining) and test (validation)
    train_idx = sub["entry_ts"] < TRAIN_END
    test_idx  = sub["entry_ts"] >= TRAIN_END
    train_tx = build_transactions(train, {f: bin_per_f[f][train_idx] for f in CONT_FEATURES})
    test_tx  = build_transactions(test,  {f: bin_per_f[f][test_idx]  for f in CONT_FEATURES})

    is_win_train = train["is_win"].astype(bool).values
    winners_tx = [t for i, t in enumerate(train_tx) if is_win_train[i]]
    losers_tx  = [t for i, t in enumerate(train_tx) if not is_win_train[i]]
    n_w = len(winners_tx); n_l = len(losers_tx)
    if n_w < 200 or n_l < 200: return []

    # FP-Growth on winners
    te = TransactionEncoder()
    try:
        W = te.fit_transform(winners_tx)
        W_df = pd.DataFrame(W, columns=te.columns_)
    except Exception:
        return []
    min_support = max(0.02, 20 / n_w)
    try:
        freq = fpgrowth(W_df, min_support=min_support, max_len=4, use_colnames=True)
    except Exception:
        return []
    if len(freq) == 0: return []
    freq = freq[freq["itemsets"].apply(lambda s: len(s) >= 2)]
    if len(freq) == 0: return []

    # Pre-index losers for fast subset checks
    loser_sets = [set(t) for t in losers_tx]
    winner_sets = [set(t) for t in winners_tx]

    rows = []
    for _, r in freq.iterrows():
        item = frozenset(r["itemsets"])
        w_in = sum(1 for t in winner_sets if item <= t)
        l_in = sum(1 for t in loser_sets  if item <= t)
        if w_in < 10: continue
        w_rate = w_in / n_w
        l_rate = l_in / n_l if n_l else 1
        lift = w_rate / l_rate if l_rate > 0 else float("inf")
        if lift < 1.5: continue
        # Fisher exact greater
        try:
            _, p = fisher_exact([[w_in, n_w - w_in], [l_in, n_l - l_in]], alternative="greater")
        except Exception:
            continue
        rows.append({"items": list(item), "w_in": w_in, "l_in": l_in,
                     "lift": lift, "p": p})
    if not rows: return []
    df_strong = pd.DataFrame(rows)
    N_tests = len(freq)  # the number of itemsets considered for Fisher tests
    alpha_bon = 0.05 / max(N_tests, 1)
    df_strong = df_strong[df_strong["p"] < alpha_bon].sort_values("p")
    if len(df_strong) == 0: return []

    # Merge overlapping (Jaccard >= 0.5)
    df_strong = df_strong.reset_index(drop=True)
    used = set()
    merged_reps = []
    for i, ri in df_strong.iterrows():
        if i in used: continue
        cluster = [i]
        for j in range(i+1, len(df_strong)):
            if j in used: continue
            if jaccard(ri["items"], df_strong.iloc[j]["items"]) >= 0.5:
                cluster.append(j); used.add(j)
        used.add(i)
        cluster_df = df_strong.iloc[cluster]
        # Pick the rep: smallest itemset in cluster (most general)
        rep = cluster_df.assign(size=cluster_df["items"].apply(len)).sort_values(["size","p"]).iloc[0]
        merged_reps.append({
            "items": rep["items"], "w_in": int(rep["w_in"]), "l_in": int(rep["l_in"]),
            "lift": float(rep["lift"]), "p": float(rep["p"]),
            "cluster_size": len(cluster),
        })

    # === Validate each merged regime on TEST ===
    is_test = sub["entry_ts"] >= TRAIN_END
    test_R = sub.loc[is_test, "realized_R"].values
    test_sets = [set(t) for t in test_tx]
    survivors = []
    for m in merged_reps:
        items = set(m["items"])
        mask = np.array([items <= ts for ts in test_sets])
        n_test_in = int(mask.sum())
        if n_test_in < 15: continue
        r = test_R[mask]
        mr = float(r.mean())
        if mr <= 0: continue
        ci_lo = boot_ci_low(r, rng=rng)
        if ci_lo <= 0: continue
        wr = float((r > 0).mean())
        survivors.append({
            "strategy_id": strat, "pair": pair, "direction": direction,
            "regime_rule": " AND ".join(sorted(m["items"])),
            "n_winners_train": n_w, "n_losers_train": n_l,
            "regime_n_winners_train": m["w_in"], "regime_n_losers_train": m["l_in"],
            "lift_train": round(m["lift"], 4),
            "p_value_train": m["p"],
            "n_tests_train": N_tests,
            "test_n": n_test_in,
            "test_wr": round(wr, 4),
            "test_mean_R": round(mr, 4),
            "test_CI_lower": round(ci_lo, 4),
            "cluster_size": m["cluster_size"],
        })
    return survivors


# Main loop
rng = np.random.default_rng(42)
print(f"\nrunning contrast mining on {len(combos)} combos ...", flush=True)
all_survivors = []
t0 = time.time()
n_done = 0
n_with_results = 0
for _, c in combos.iterrows():
    strat = c["strategy_id"]; pair = c["pair"]; direction = c["direction"]
    sub = full[(full.strategy_id == strat) & (full.pair == pair) & (full.direction == direction)]
    try:
        survs = process_combo(strat, pair, direction, sub, rng)
    except Exception as e:
        print(f"  ERR {strat} {pair} {direction}: {e}", flush=True)
        continue
    if survs:
        all_survivors.extend(survs)
        n_with_results += 1
    n_done += 1
    if n_done % 50 == 0 or n_done == len(combos):
        elapsed = time.time() - t0
        rate = n_done / elapsed
        eta = (len(combos) - n_done) / rate / 60 if rate > 0 else 0
        print(f"  {n_done}/{len(combos)} combos ({rate:.1f}/s, ETA {eta:.1f} min), "
              f"survivors so far: {len(all_survivors)} from {n_with_results} combos",
              flush=True)

print(f"\nDONE — {len(all_survivors)} survivors across {n_with_results} combos", flush=True)
res = pd.DataFrame(all_survivors)
if len(res):
    res = res.sort_values("test_CI_lower", ascending=False)
res.to_csv(RESULT_CSV, index=False)
print(f"saved -> {RESULT_CSV}", flush=True)

if len(res):
    print(f"\nTop 30 by test_CI_lower:")
    cols = ["strategy_id","pair","direction","regime_rule",
            "regime_n_winners_train","lift_train","p_value_train",
            "test_n","test_wr","test_mean_R","test_CI_lower"]
    print(res[cols].head(30).to_string(index=False, float_format="%.4f"))
    print(f"\nBy strategy family:")
    fam = res.groupby("strategy_id").agg(
        n_regimes=("regime_rule","size"),
        pairs=("pair","nunique"),
        best_test_R=("test_mean_R","max"),
        best_ci=("test_CI_lower","max"),
    ).reset_index().sort_values("n_regimes", ascending=False)
    print(fam.head(30).to_string(index=False, float_format="%.4f"))
