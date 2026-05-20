"""Generate the soft-deprioritize list: (regime, pair, direction) tuples that
- have NO bank coverage at any tier/session
- AND consumed >= 50 entry_filter evaluations today

Per Brock 2026-05-20: soft deprioritize, not hard skip. Keep a 20%
sampling rate so we don't go blind on the deprioritized tuples and so
we can detect regime drift / new evidence.

Output: data/router_deprioritize.json (config artifact for scan_pipeline).
"""
import json
from collections import Counter
import pandas as pd

V9 = "/home/ubuntu/mr-scrooge-v3/data/routing_table_v9_observe.parquet"
LEDGER = "/home/ubuntu/mr-scrooge-v3/data/seed-telemetry.jsonl"
OUT = "/home/ubuntu/mr-scrooge-v3/data/router_deprioritize.json"

TRADE_TIERS = {"Seed-Pro", "Pro", "Elite"}
SINCE = "2026-05-20T06:03"

# Bank coverage: exact, regime-flip, direction-flip
v9 = pd.read_parquet(V9)
bank = v9[v9.tier.isin(TRADE_TIERS)].drop_duplicates(
    ["technical_regime_53", "pair", "direction", "strategy"])
exact = set(zip(bank.technical_regime_53, bank.pair, bank.direction))
by_pair_dir = set(zip(bank.pair, bank.direction))
by_pair_regime = set(zip(bank.pair, bank.technical_regime_53))

# Live traffic since v1.5 flip
tuple_counts = Counter()
with open(LEDGER) as f:
    for line in f:
        try: r = json.loads(line)
        except: continue
        if r.get("ts", "") < SINCE: continue
        if r.get("gate") != "entry_filter": continue
        tuple_counts[(r.get("regime53"), r.get("symbol"), r.get("direction"))] += 1

# No-coverage = none of exact / regime-flip / direction-flip
no_cov = []
for (rg, pair, d), n in tuple_counts.items():
    if (rg, pair, d) in exact: continue
    if (pair, d) in by_pair_dir: continue   # regime-flip available
    if (pair, rg) in by_pair_regime: continue  # direction-flip available
    no_cov.append((rg, pair, d, n))

# Filter to high-volume traffic only
THRESHOLD = 50
qualified = [(rg, pair, d, n) for (rg, pair, d, n) in no_cov if n >= THRESHOLD]
qualified.sort(key=lambda x: -x[3])

print(f"=== Soft-deprioritize list (no bank coverage at all, >= {THRESHOLD} evals today) ===")
print(f"{'rg':<5}{'pair':<10}{'dir':<6}{'evals':>6}")
for rg, pair, d, n in qualified:
    print(f"{rg:<5}{pair:<10}{d:<6}{n:>6}")
print(f"\ntotal tuples: {len(qualified)}  consumed evals today: {sum(n for _,_,_,n in qualified):,}")

config = {
    "version": 1,
    "created_at": "2026-05-20T16:00:00Z",
    "description": "Soft-deprioritize list. Tuples with no v9_observe trade-tier coverage AND >=50 live evals today. scan_pipeline keeps a 20% sample to detect regime drift, drops the other 80%.",
    "sample_rate": 0.20,
    "tuples": [
        {"regime53": rg, "pair": pair, "direction": d, "evals_24h": n}
        for rg, pair, d, n in qualified
    ],
}
with open(OUT, "w") as f:
    json.dump(config, f, indent=2)
print(f"\nwrote {OUT}")
