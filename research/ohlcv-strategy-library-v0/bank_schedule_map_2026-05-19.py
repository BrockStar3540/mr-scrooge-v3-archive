"""Winning-Bank Schedule Map -- where does the validated bank actually live?

Phase 1: For every trade-tier cell in v9_observe + v10_fast_v1.4, derive:
  - the shave_rule's underlying winning rows in the corpus
  - hour_utc distribution of THOSE winners
  - which (pair, regime, direction) actually has real evidence
  - flag synthetic-session fan-out (when shave_rule contains hour_utc
    but the cell is fanned across all 7 sessions)

Phase 2: Cross-tab against today's actual scan effort from seed-telemetry
to quantify the mismatch.
"""
import re
import json
import sys
from collections import defaultdict, Counter
sys.path.insert(0, "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0")
from expand_telemetry_driven import dedup_probe, family_for, session_bucket_for_hour
import pandas as pd
import pyarrow.parquet as pq

V9_PATH = "/home/ubuntu/mr-scrooge-v3/data/routing_table_v9_observe.parquet"
V14_PATH = "/home/ubuntu/mr-scrooge-v3/data/routing_table_v10_fast_v1_4.parquet"
CORPUS_PATH = "/home/ubuntu/mr-scrooge-v3/research/routing-table-v2-2026-05-14/ml_training_corpus.parquet"

TRADE_TIERS = {"Seed-Pro", "Pro", "Elite"}

# ----------------------------------------------------------------------
# 1) Load the bank: dedup to (regime, pair, direction, strategy, tier)
# ----------------------------------------------------------------------
v9 = pd.read_parquet(V9_PATH)
v14 = pd.read_parquet(V14_PATH)

bank = v9[v9.tier.isin(TRADE_TIERS)].copy()
# dedup synthetic session fanout
bank = bank.drop_duplicates(["technical_regime_53","pair","direction","strategy"])
print(f"v9_observe trade-tier cells (unique signatures): {len(bank)}")
print(f"v10_fast_v1.4 cells (total rows incl session fanout): {len(v14)}")
v14_dedup = v14.drop_duplicates(["technical_regime_53","pair","direction","strategy"])
print(f"v10_fast_v1.4 unique signatures: {len(v14_dedup)}")
print()

# ----------------------------------------------------------------------
# 2) Load corpus
# ----------------------------------------------------------------------
print(f"Loading corpus ({CORPUS_PATH})...")
schema = pq.read_schema(CORPUS_PATH)
available = {f.name for f in schema}
wanted = ["source","strategy_id","pair","direction","entry_ts","is_win",
          "technical_regime_53","hour_utc","day_of_week",
          "ATR_ratio","BB_compress","ADX14","RSI14","close_pos"]
cols = [c for c in wanted if c in available]
corpus = pq.read_table(CORPUS_PATH, columns=cols).to_pandas()
corpus = dedup_probe(corpus)
print(f"corpus rows (deduped): {len(corpus):,}")
print()

# ----------------------------------------------------------------------
# 3) Rule clause parser
# ----------------------------------------------------------------------
CLAUSE_RE = re.compile(r"(\w+)\s*(==|>=|<=|>|<|!=)\s*([\w\.\-]+)")

def parse_clauses(rule: str):
    out = []
    for feat, op, val in CLAUSE_RE.findall(rule or ""):
        try: val_f = float(val)
        except ValueError: val_f = val  # categorical (e.g. session_bucket)
        out.append((feat, op, val_f))
    return out

def apply_clauses(df: pd.DataFrame, clauses: list) -> pd.DataFrame:
    mask = pd.Series(True, index=df.index)
    for feat, op, val in clauses:
        # alias: price_pos -> close_pos
        col = "close_pos" if feat == "price_pos" else feat
        if col not in df.columns:
            # if column missing (e.g. session_bucket, volume_ratio), skip
            continue
        s = df[col]
        if isinstance(val, str):
            # categorical eq
            if op == "==": mask &= (s.astype(str) == val)
            elif op == "!=": mask &= (s.astype(str) != val)
            continue
        # numeric
        if op == "<=": mask &= (s <= val)
        elif op == ">=": mask &= (s >= val)
        elif op == "<":  mask &= (s <  val)
        elif op == ">":  mask &= (s >  val)
        elif op == "==": mask &= (s == val)
        elif op == "!=": mask &= (s != val)
    return df[mask]

# ----------------------------------------------------------------------
# 4) Derive each cell's true hour distribution from corpus
# ----------------------------------------------------------------------
print("Deriving per-cell hour distribution...")
rows = []
for _, c in bank.iterrows():
    rg = c.parent_regime
    pair = c.pair
    direction = c.direction
    strat = c.strategy
    family = c.family
    tier = c.tier
    wr = c.wr
    wlb = c.wilson_lb
    n_unique = c.n_unique
    rule = c.shave_rule or ""
    has_hour_clause = "hour_utc" in rule
    has_session_clause = "session_bucket" in rule

    # Filter corpus to this signature
    base = corpus[(corpus.technical_regime_53 == rg)
                  & (corpus.pair == pair)
                  & (corpus.direction == direction)]
    base = base[base.strategy_id == strat]

    clauses = parse_clauses(rule)
    # remove session_bucket clause (corpus doesn't have it)
    clauses_no_sess = [c for c in clauses if c[0] != "session_bucket"]
    matched = apply_clauses(base, clauses_no_sess)
    matched_wins = matched[matched.is_win == True]

    # Hour distribution of WINNERS
    hr_winners = matched_wins.hour_utc.value_counts().sort_index().to_dict() if len(matched_wins) else {}
    hr_all = matched.hour_utc.value_counts().sort_index().to_dict() if len(matched) else {}

    # Approximate typical session(s) based on winner hours
    typical_sessions = Counter()
    for h, n in hr_winners.items():
        typical_sessions[session_bucket_for_hour(int(h))] += int(n)
    top_session = typical_sessions.most_common(1)[0] if typical_sessions else (None, 0)

    rows.append({
        "regime": rg, "pair": pair, "direction": direction,
        "strategy": strat, "family": family, "tier": tier,
        "wr": wr, "wilson_lb": wlb, "n_unique_v9": int(n_unique),
        "corpus_n_after_rule": len(matched),
        "corpus_wins_after_rule": len(matched_wins),
        "corpus_wr_after_rule": (len(matched_wins) / len(matched)) if len(matched) else 0.0,
        "has_hour_clause": has_hour_clause,
        "has_session_clause": has_session_clause,
        "top_session_by_winners": top_session[0],
        "top_session_winner_count": top_session[1],
        "shave_rule": rule,
        "hour_distribution_winners": str(hr_winners),
    })

bank_map = pd.DataFrame(rows)
bank_map.to_csv("/tmp/bank_schedule_map.csv", index=False)
print(f"bank_map rows: {len(bank_map)}")
print()

# ----------------------------------------------------------------------
# 5) Where does the validated bank actually live?
# ----------------------------------------------------------------------
print("=" * 78)
print("BANK LIVES BY SESSION (top sessions for winning rows)")
print("=" * 78)
print(bank_map.groupby("top_session_by_winners").agg(
    cells=("strategy","count"),
    total_winners=("corpus_wins_after_rule","sum"),
).sort_values("total_winners", ascending=False).to_string())
print()
print("=" * 78)
print("BANK LIVES BY PAIR")
print("=" * 78)
print(bank_map.groupby("pair").agg(
    cells=("strategy","count"),
    total_winners=("corpus_wins_after_rule","sum"),
).sort_values("total_winners", ascending=False).head(15).to_string())
print()
print("=" * 78)
print("BANK LIVES BY FAMILY")
print("=" * 78)
print(bank_map.groupby("family").agg(
    cells=("strategy","count"),
    total_winners=("corpus_wins_after_rule","sum"),
).sort_values("total_winners", ascending=False).to_string())
print()
print("=" * 78)
print("BANK LIVES BY (PAIR x DIRECTION) -- TOP 20")
print("=" * 78)
print(bank_map.groupby(["pair","direction"]).agg(
    cells=("strategy","count"),
    n=("corpus_n_after_rule","sum"),
    winners=("corpus_wins_after_rule","sum"),
).sort_values("winners", ascending=False).head(20).to_string())
print()
print("=" * 78)
print("SYNTHETIC vs HONEST: cells with hour_utc clause")
print("=" * 78)
print(bank_map.groupby("has_hour_clause").agg(
    cells=("strategy","count"),
    total_winners=("corpus_wins_after_rule","sum"),
).to_string())
print()
print("=" * 78)
print("WHICH OF THESE ARE IN v10_fast_v1.4 (live)?")
print("=" * 78)
live_keys = set(zip(v14_dedup.parent_regime, v14_dedup.pair, v14_dedup.direction, v14_dedup.strategy))
bank_map["in_v14_live"] = bank_map.apply(lambda r: (r.regime, r.pair, r.direction, r.strategy) in live_keys, axis=1)
print(f"trade-tier signatures in bank: {len(bank_map)}")
print(f"signatures currently LIVE in v10_fast_v1.4: {bank_map.in_v14_live.sum()}")
print(f"signatures in bank but NOT live: {(~bank_map.in_v14_live).sum()}")
print()
print("=" * 78)
print("HIGHEST-EVIDENCE CELLS NOT IN v1.4 (top 25 by winners)")
print("=" * 78)
absent = bank_map[~bank_map.in_v14_live].sort_values("corpus_wins_after_rule", ascending=False).head(25)
print(absent[["pair","regime","direction","family","strategy","tier","wr","wilson_lb",
              "corpus_n_after_rule","corpus_wins_after_rule","corpus_wr_after_rule",
              "top_session_by_winners","has_hour_clause"]].to_string(index=False))
