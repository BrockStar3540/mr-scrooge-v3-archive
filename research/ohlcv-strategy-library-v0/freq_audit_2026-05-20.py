"""Phase 3 deliverable: deployable bank with frequency.

For every trade-tier cell in v9_observe, compute:
  - total historical fires       (n_unique after shave_rule)
  - corpus date span             (min/max entry_ts)
  - fires per week
  - fires per month
  - typical session
  - whether each cell would actually fire in a normal week

Flag cells as:
  - GHOST          fires < 0.25/week        (basically never)
  - RARE           fires < 1/week
  - MODERATE       1-3 fires/week
  - REGULAR        > 3 fires/week
"""
import re
import json
import pandas as pd
import pyarrow.parquet as pq

V9 = "/home/ubuntu/mr-scrooge-v3/data/routing_table_v9_observe.parquet"
CORPUS_PATH = "/home/ubuntu/mr-scrooge-v3/research/routing-table-v2-2026-05-14/ml_training_corpus.parquet"
OUT_CSV = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/deployable_bank_with_frequency.csv"

TRADE_TIERS = {"Seed-Pro", "Pro", "Elite"}
CLAUSE_RE = re.compile(r"(\w+)\s*(==|>=|<=|>|<|!=)\s*([\w\.\-]+)")

def parse_clauses(rule):
    out = []
    for feat, op, val in CLAUSE_RE.findall(rule or ""):
        try: val_f = float(val)
        except ValueError: val_f = val
        out.append((feat, op, val_f))
    return out

def apply_clauses(df, clauses):
    mask = pd.Series(True, index=df.index)
    for feat, op, val in clauses:
        col = "close_pos" if feat == "price_pos" else feat
        if col not in df.columns:
            continue
        s = df[col]
        if isinstance(val, str):
            if op == "==": mask &= (s.astype(str) == val)
            elif op == "!=": mask &= (s.astype(str) != val)
            continue
        if op == "<=": mask &= (s <= val)
        elif op == ">=": mask &= (s >= val)
        elif op == "<":  mask &= (s <  val)
        elif op == ">":  mask &= (s >  val)
        elif op == "==": mask &= (s == val)
        elif op == "!=": mask &= (s != val)
    return df[mask]

v9 = pd.read_parquet(V9)
bank = v9[v9.tier.isin(TRADE_TIERS)].drop_duplicates(
    ["technical_regime_53","pair","direction","strategy"]
).copy()
print(f"trade-tier signatures: {len(bank)}")

print("Loading corpus...")
schema = pq.read_schema(CORPUS_PATH)
available = {f.name for f in schema}
wanted = ["source","strategy_id","pair","direction","entry_ts","is_win",
          "technical_regime_53","hour_utc","day_of_week",
          "ATR_ratio","BB_compress","ADX14","RSI14","close_pos"]
cols = [c for c in wanted if c in available]
corpus = pq.read_table(CORPUS_PATH, columns=cols).to_pandas()
# probe dedup by entry_ts+pair+direction
corpus = corpus.drop_duplicates(["entry_ts","pair","direction","strategy_id"])
print(f"corpus rows (deduped): {len(corpus):,}")

corpus_min = corpus.entry_ts.min()
corpus_max = corpus.entry_ts.max()
corpus_weeks = (corpus_max - corpus_min).days / 7.0
print(f"corpus span: {corpus_min} -> {corpus_max}  ({corpus_weeks:.0f} weeks)")
print()

rows = []
for _, c in bank.iterrows():
    rg = c.parent_regime
    pair = c.pair
    direction = c.direction
    strat = c.strategy
    rule = c.shave_rule or ""

    base = corpus[(corpus.technical_regime_53 == rg)
                  & (corpus.pair == pair)
                  & (corpus.direction == direction)
                  & (corpus.strategy_id == strat)]
    clauses = [cl for cl in parse_clauses(rule) if cl[0] != "session_bucket"]
    matched = apply_clauses(base, clauses)
    n_total = len(matched)
    n_winners = int(matched.is_win.sum()) if "is_win" in matched.columns else 0
    fires_per_week = n_total / corpus_weeks
    fires_per_month = fires_per_week * 4.33

    if fires_per_week < 0.25:
        freq_class = "GHOST"
    elif fires_per_week < 1:
        freq_class = "RARE"
    elif fires_per_week <= 3:
        freq_class = "MODERATE"
    else:
        freq_class = "REGULAR"

    realized_wr = (n_winners / n_total) if n_total else 0.0

    rows.append({
        "pair": pair, "regime": rg, "direction": direction,
        "strategy": strat, "family": c.family, "tier": c.tier,
        "v9_wr": float(c.wr), "v9_wilson_lb": float(c.wilson_lb),
        "v9_n_unique": int(c.n_unique),
        "corpus_n_after_rule": n_total,
        "corpus_winners_after_rule": n_winners,
        "corpus_wr_after_rule": realized_wr,
        "fires_per_week": fires_per_week,
        "fires_per_month": fires_per_month,
        "freq_class": freq_class,
        "shave_rule": rule,
    })

df = pd.DataFrame(rows).sort_values("fires_per_week", ascending=False)
df.to_csv(OUT_CSV, index=False)

print("=" * 90)
print("FREQUENCY CLASS DISTRIBUTION")
print("=" * 90)
print(df.groupby("freq_class").agg(
    cells=("strategy","count"),
    median_fires_per_week=("fires_per_week","median"),
    median_wr=("corpus_wr_after_rule","median"),
).reindex(["REGULAR","MODERATE","RARE","GHOST"]).to_string())
print()

print("=" * 90)
print("REGULAR + MODERATE cells (the actually tradable bank)")
print("=" * 90)
tradable = df[df.freq_class.isin(["REGULAR","MODERATE"])]
if len(tradable):
    print(tradable[["pair","regime","direction","family","strategy","tier",
                    "v9_wr","corpus_wr_after_rule","fires_per_week","fires_per_month"]].to_string(index=False))
else:
    print("(none — entire bank is RARE or GHOST class)")
print()

print("=" * 90)
print("GHOST cells (essentially never fire)")
print("=" * 90)
ghosts = df[df.freq_class == "GHOST"]
print(ghosts[["pair","regime","direction","strategy","tier",
              "v9_n_unique","corpus_n_after_rule","fires_per_week"]].to_string(index=False))
print()
print(f"wrote {OUT_CSV}")
