"""Full per-tuple audit per Brock's template:

For each of the 6 blocked tuples:
  - trade-tier cells found?  (Seed-Pro / Pro / Elite)
  - Seed-only cells found?
  - best family/strategy fallback
  - n_unique, wr, wilson_lb
  - shadow near-miss evidence today
  - verdict: deployable / promote_candidate / needs_mining
"""
import json
import re
from collections import defaultdict, Counter
import pandas as pd

UNMET = [
    # (regime, pair, direction, blocked_count, slice_letter)
    ("C01", "GBP_JPY", "short", 22, "A"),
    ("C02", "CAD_JPY", "short", 16, "A"),
    ("C01", "NZD_USD", "short", 40, "B"),
    ("C02", "AUD_USD", "long",  31, "B"),
    ("C01", "AUD_USD", "long",   9, "B"),
    ("C02", "EUR_USD", "short",  4, "B"),
]
TRADE_TIERS = {"Seed-Pro", "Pro", "Elite"}
ACTIVE_SESSIONS = ("london_open", "ny_open", "ny_mid")

v9 = pd.read_parquet("/home/ubuntu/mr-scrooge-v3/data/routing_table_v9_observe.parquet")
v10 = pd.read_parquet("/home/ubuntu/mr-scrooge-v3/data/routing_table_v10_fast_v1_2.parquet")

# Load today's shadow telemetry for near-miss data
shadow_evidence = defaultdict(list)
with open("/home/ubuntu/mr-scrooge-v3/data/seed-telemetry.jsonl") as f:
    for line in f:
        try: r = json.loads(line)
        except: continue
        if r.get("ts","") < "2026-05-19T06:24": continue
        if r.get("gate") != "entry_filter_shadow": continue
        key = (r.get("regime53"), r.get("symbol"), r.get("direction"))
        shadow_evidence[key].append(r)

def parse_violation(s):
    m = re.search(r"([\w_]+)\s*([<>=]+)\s*([\d.\-]+).*got ([\d.\-]+)", s or "")
    if not m: return None
    threshold = float(m.group(3))
    if threshold == 0: return None
    got = float(m.group(4))
    return (m.group(1), m.group(2), threshold, got, abs(got - threshold) / abs(threshold) * 100)

print("=" * 90)
print("FULL UNMET-TUPLE AUDIT (v9_observe banks + today's shadow evidence)")
print("=" * 90)

verdicts = []
for regime, pair, direction, blocked, slc in UNMET:
    print()
    print("-" * 90)
    print(f"Slice {slc}: {regime} / {pair} / {direction}  (blocked today: {blocked})")
    print("-" * 90)

    # 1. v10_fast_v1.2 -- LIVE
    live = v10[(v10.parent_regime == regime) & (v10.pair == pair) & (v10.direction == direction)]
    print(f"  v10_fast_v1.2 LIVE cells: {len(live)}")

    # 2. v9_observe -- exact match
    base = v9[(v9.parent_regime == regime) & (v9.pair == pair) & (v9.direction == direction)]
    trade = base[base.tier.isin(TRADE_TIERS)]
    seed_only = base[base.tier == "Seed"]
    print(f"  v9_observe rows for ({regime},{pair},{direction}): {len(base)} total | "
          f"{len(trade)} trade-tier | {len(seed_only)} Seed | "
          f"{len(base)-len(trade)-len(seed_only)} below-Seed")

    # 3. Top trade-tier per (strategy, session) -- dedup the 7-session fan-out
    if len(trade) > 0:
        dedup = trade.drop_duplicates(["strategy","session_bucket"])[
            ["strategy","family","session_bucket","tier","wr","wilson_lb","n_unique","shave_rule"]
        ].sort_values(["wilson_lb","n_unique"], ascending=False)
        print(f"\n  TRADE-TIER cells (unique strategy x session):")
        for _, r in dedup.iterrows():
            rule = r.shave_rule or ""
            hour_clause = "** has hour_utc clause **" if "hour_utc" in rule else ""
            print(f"    {r.strategy:<35} fam={r.family:<10} sess={r.session_bucket:<11} "
                  f"{r.tier:<8} wr={r.wr:.3f} wlb={r.wilson_lb:.3f} n={int(r.n_unique):>3}  {hour_clause}")
            if hour_clause or len(rule) < 90:
                print(f"      rule: {rule}")

    # 4. Best Seed-only cells
    if len(seed_only) > 0:
        dedup_seed = seed_only.drop_duplicates(["strategy","session_bucket"])[
            ["strategy","family","session_bucket","tier","wr","wilson_lb","n_unique","shave_rule"]
        ].sort_values(["wilson_lb","n_unique"], ascending=False).head(5)
        print(f"\n  TOP-5 SEED cells:")
        for _, r in dedup_seed.iterrows():
            rule = (r.shave_rule or "")[:60]
            print(f"    {r.strategy:<35} fam={r.family:<10} sess={r.session_bucket:<11} "
                  f"Seed wr={r.wr:.3f} wlb={r.wilson_lb:.3f} n={int(r.n_unique):>3}  rule={rule}")

    # 5. Today's shadow near-misses for this tuple
    ev = shadow_evidence.get((regime, pair, direction), [])
    near = []
    for r in ev:
        p = parse_violation(r.get("block_reason"))
        if p is None: continue
        feat, op, thr, got, gap = p
        if gap <= 25:
            near.append((gap, r.get("cell_strategy"), r.get("cell_tier"), feat, op, thr, got))
    near.sort()
    print(f"\n  Today's shadow evaluations for this tuple: {len(ev)}  near-misses (gap<=25%): {len(near)}")
    if near:
        seen = set()
        for gap, cs, ct, feat, op, thr, got in near[:5]:
            key = (cs, feat)
            if key in seen: continue
            seen.add(key)
            print(f"    gap={gap:>5.1f}%  cell={cs}/{ct}  clause={feat} {op} {thr} (got {got})")

    # 6. Verdict
    if len(trade) > 0:
        # Honest cells = no hour_utc clause
        honest = trade[~trade.shave_rule.str.contains("hour_utc", na=False)]
        if len(honest) > 0:
            verdict = "DEPLOYABLE"
        else:
            verdict = "TRADE_TIER_BUT_HOUR_FANOUT"
    elif len(seed_only) > 0 and len(near) > 0:
        verdict = "PROMOTE_CANDIDATE"
    elif len(seed_only) > 0:
        verdict = "SEED_ONLY_NO_EVIDENCE"
    else:
        verdict = "NEEDS_FRESH_MINING"
    print(f"\n  >>> VERDICT: {verdict}")
    verdicts.append((slc, regime, pair, direction, blocked, verdict, len(trade), len(seed_only), len(near)))

print()
print("=" * 90)
print("SUMMARY")
print("=" * 90)
print(f"{'slice':<6} {'regime':<6} {'pair':<10} {'dir':<6} {'blocked':>7}  {'verdict':<28} {'trade':>5} {'seed':>5} {'near':>5}")
for slc, rg, pair, d, b, v, t, s, n in verdicts:
    print(f"{slc:<6} {rg:<6} {pair:<10} {d:<6} {b:>7}  {v:<28} {t:>5} {s:>5} {n:>5}")
