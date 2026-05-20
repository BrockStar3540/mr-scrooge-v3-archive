"""Strict bank audit + live-activity alignment.

Two outputs:

1) Strict bank narrow-window audit
   For each trade-tier signature in v9_observe, parse EVERY clause in
   the shave_rule (not just hour_utc). Classify cell as:
     - genuinely broad      (no time/regime-restricting clause)
     - hour-narrow          (has hour_utc clause)
     - factor-narrow        (has ADX14/ATR/RSI clamp that's tight)
     - dual-narrow          (combination)

2) Live-activity aligned bank lookup
   For each (regime, pair, direction) actually being generated today,
   find the bank's closest cell:
     - exact (same regime, pair, direction)
     - regime-flip   (different regime but same pair+direction)
     - direction-flip (different direction but same pair+regime)
     - none

   Outputs how much of today's live traffic actually has bank coverage
   at any tier.
"""
import json
import re
from collections import Counter, defaultdict
import pandas as pd

V9 = "/home/ubuntu/mr-scrooge-v3/data/routing_table_v9_observe.parquet"
V15 = "/home/ubuntu/mr-scrooge-v3/data/routing_table_v10_fast_v1_5.parquet"
LEDGER = "/home/ubuntu/mr-scrooge-v3/data/seed-telemetry.jsonl"

TRADE_TIERS = {"Seed-Pro", "Pro", "Elite"}
SINCE = "2026-05-20T06:03"   # since v1.5 went live

CLAUSE_RE = re.compile(r"(\w+)\s*(==|>=|<=|>|<|!=)\s*([\w\.\-]+)")

# ----------------------------------------------------------------------
# 1) Strict narrow-window audit
# ----------------------------------------------------------------------
v9 = pd.read_parquet(V9)
bank = v9[v9.tier.isin(TRADE_TIERS)].copy()
bank = bank.drop_duplicates(["technical_regime_53","pair","direction","strategy"])

NARROWING_FEATURES = {"hour_utc","ADX14","ATR_ratio","BB_compress","RSI14","volume_ratio","close_pos","price_pos"}

rows = []
for _, c in bank.iterrows():
    rule = c.shave_rule or ""
    clauses = CLAUSE_RE.findall(rule)
    feats = sorted({f for f,_,_ in clauses})
    narrow_feats = sorted([f for f in feats if f in NARROWING_FEATURES])
    has_hour = "hour_utc" in feats
    # detect factor-narrow: any inequality clamp on technical factors
    factor_narrow = any(f in narrow_feats for f in ["ADX14","ATR_ratio","RSI14","volume_ratio","close_pos","price_pos","BB_compress"])
    if has_hour and factor_narrow:
        cls = "dual-narrow"
    elif has_hour:
        cls = "hour-narrow"
    elif factor_narrow:
        cls = "factor-narrow"
    else:
        cls = "broad"
    rows.append({
        "pair": c.pair, "regime": c.parent_regime, "direction": c.direction,
        "strategy": c.strategy, "family": c.family, "tier": c.tier,
        "wr": c.wr, "wilson_lb": c.wilson_lb, "n_unique": int(c.n_unique),
        "shave_rule": rule, "feats": ",".join(feats),
        "narrowness": cls,
    })
audit = pd.DataFrame(rows)

print("=" * 78)
print("STRICT NARROWNESS AUDIT — every trade-tier signature in v9_observe")
print("=" * 78)
print(audit.groupby("narrowness").size().sort_values(ascending=False).to_string())
print()

# Show the few truly-broad cells
print("=== TRULY BROAD cells (no narrowing clauses) ===")
broad = audit[audit.narrowness == "broad"]
if len(broad):
    print(broad[["pair","regime","direction","family","strategy","tier","wr","n_unique","shave_rule"]].to_string(index=False))
else:
    print("(none)")
print()

# v1.5 live signatures and their narrowness
v15 = pd.read_parquet(V15).drop_duplicates(["technical_regime_53","pair","direction","strategy"])
live_sigs = set(zip(v15.technical_regime_53, v15.pair, v15.direction, v15.strategy))
audit["in_v1_5_live"] = audit.apply(lambda r: (r.regime, r.pair, r.direction, r.strategy) in live_sigs, axis=1)
print("=== v1.5 live signatures, narrowness breakdown ===")
print(audit[audit.in_v1_5_live].groupby("narrowness").size().to_string())
print()

# Print all v1.5 live signatures with their narrowness + rules
print("=== Every v1.5 live signature, with its rule ===")
for _, r in audit[audit.in_v1_5_live].sort_values("narrowness").iterrows():
    print(f"  {r.narrowness:<13} {r.pair:<8} {r.regime} {r.direction:<5} {r.tier:<8} {r.strategy:<35}")
    print(f"      rule: {r.shave_rule}")
print()

# ----------------------------------------------------------------------
# 2) Live-activity aligned bank lookup
# ----------------------------------------------------------------------
# Build map: (regime, pair, direction) -> {strategies in bank, tiers, sessions}
bank_index = defaultdict(list)
for _, c in bank.iterrows():
    bank_index[(c.parent_regime, c.pair, c.direction)].append({
        "strategy": c.strategy, "family": c.family, "tier": c.tier,
        "session_bucket": c.session_bucket, "wr": c.wr, "n_unique": int(c.n_unique),
    })
# secondary indexes for fuzzy match
bank_by_pair_dir = defaultdict(list)
bank_by_pair_regime = defaultdict(list)
for k, v in bank_index.items():
    bank_by_pair_dir[(k[1], k[2])].extend([{**c, "regime": k[0]} for c in v])
    bank_by_pair_regime[(k[1], k[0])].extend([{**c, "direction": k[2]} for c in v])

# Count live-traffic tuples since v1.5
tuple_counts = Counter()
with open(LEDGER) as f:
    for line in f:
        try: r = json.loads(line)
        except: continue
        if r.get("ts","") < SINCE: continue
        if r.get("gate") != "entry_filter": continue
        k = (r.get("regime53"), r.get("symbol"), r.get("direction"))
        tuple_counts[k] += 1

print("=" * 78)
print(f"LIVE-ACTIVITY ALIGNED BANK COVERAGE (since v1.5 flip)")
print(f"Total live (regime,pair,direction) tuples seen: {len(tuple_counts)}")
print(f"Total entry_filter evaluations:                  {sum(tuple_counts.values()):,}")
print("=" * 78)

exact_covered = 0
regime_flip_only = 0
direction_flip_only = 0
no_coverage = 0
exact_covered_evals = 0
regime_flip_evals = 0
direction_flip_evals = 0
no_cov_evals = 0
no_cov_tuples = []

for (rg, pair, d), n in sorted(tuple_counts.items(), key=lambda x: -x[1]):
    exact = bank_index.get((rg, pair, d), [])
    if exact:
        exact_covered += 1
        exact_covered_evals += n
        continue
    # try same pair+direction, any regime
    pdf = bank_by_pair_dir.get((pair, d), [])
    if pdf:
        regime_flip_only += 1
        regime_flip_evals += n
        continue
    # try same pair+regime, any direction
    prg = bank_by_pair_regime.get((pair, rg), [])
    if prg:
        direction_flip_only += 1
        direction_flip_evals += n
        continue
    no_coverage += 1
    no_cov_evals += n
    no_cov_tuples.append((rg, pair, d, n))

print(f"\n{'category':<24}{'tuples':>8}{'evaluations':>14}")
print(f"{'exact bank coverage':<24}{exact_covered:>8}{exact_covered_evals:>14}")
print(f"{'regime-flip only':<24}{regime_flip_only:>8}{regime_flip_evals:>14}")
print(f"{'direction-flip only':<24}{direction_flip_only:>8}{direction_flip_evals:>14}")
print(f"{'NO COVERAGE':<24}{no_coverage:>8}{no_cov_evals:>14}")
print()

print("=== TOP TUPLES WITH EXACT BANK COVERAGE BUT NO LIVE PASSES ===")
exact_in_traffic = [
    ((rg, pair, d), n, bank_index[(rg, pair, d)])
    for (rg, pair, d), n in tuple_counts.most_common(30)
    if bank_index.get((rg, pair, d))
]
for (rg, pair, d), n, cells in exact_in_traffic[:10]:
    sess_set = sorted({c["session_bucket"] for c in cells})
    strats = sorted({c["strategy"] for c in cells})
    tiers = sorted({c["tier"] for c in cells})
    print(f"  evals={n:>4}  {rg}/{pair}/{d:<5}  bank: tiers={tiers} sessions={sess_set}")
    for s in strats[:3]:
        print(f"      strategy={s}")
print()

print("=== TOP NO-COVERAGE TUPLES (dead traffic) ===")
for (rg, pair, d, n) in sorted(no_cov_tuples, key=lambda x: -x[3])[:15]:
    print(f"  evals={n:>4}  {rg}/{pair}/{d:<5}")
print()

print("=== TOP REGIME-FLIP-ONLY TUPLES (bank has different regime) ===")
regime_flip_tuples = []
for (rg, pair, d), n in tuple_counts.items():
    if (rg, pair, d) in bank_index: continue
    pdf = bank_by_pair_dir.get((pair, d), [])
    if pdf and not bank_by_pair_regime.get((pair, rg)):
        regime_flip_tuples.append((rg, pair, d, n, pdf))
for (rg, pair, d, n, pdf) in sorted(regime_flip_tuples, key=lambda x:-x[3])[:10]:
    bank_regimes = sorted({c["regime"] for c in pdf})
    print(f"  evals={n:>4}  live={rg}/{pair}/{d}  bank-has={bank_regimes}/{pair}/{d}")
