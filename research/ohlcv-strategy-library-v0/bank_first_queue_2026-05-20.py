"""Phase 1 deliverables: current_session_bank_priority.csv +
bank_first_strategy_queue.json

For each active session, list the cells the bot SHOULD prioritize -- i.e.,
cells that are NOT GHOSTs (fire >= 0.25/wk historically).
The bot can use this queue to actively hunt these slices instead of waiting
for generic direct-family generation to stumble into them.
"""
import json
import pandas as pd

FREQ_CSV = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/deployable_bank_with_frequency.csv"
PRI_CSV = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/current_session_bank_priority.csv"
QUEUE_JSON = "/home/ubuntu/mr-scrooge-v3/data/bank_first_strategy_queue.json"

df = pd.read_csv(FREQ_CSV)

# Drop GHOSTS — anything < 0.25 fires/week is not worth prioritizing
tradable = df[df.freq_class != "GHOST"].copy().sort_values("fires_per_week", ascending=False)
print(f"Non-GHOST cells: {len(tradable)} (of {len(df)} total)")

# Determine each cell's active session from shave_rule's session_bucket==X clause
import re
SESSION_CLAUSE = re.compile(r"session_bucket\s*==\s*([\w_]+)")
def get_active_sessions(rule):
    m = SESSION_CLAUSE.search(rule or "")
    if m: return [m.group(1)]
    # if rule has hour clauses, derive session
    return ["any"]   # session-agnostic, can fire any session

tradable["active_sessions"] = tradable.shave_rule.fillna("").map(get_active_sessions)

# Priority CSV: one row per (cell, session)
rows = []
for _, r in tradable.iterrows():
    for sess in r.active_sessions:
        rows.append({
            "session_bucket": sess,
            "pair": r.pair, "regime": r.regime, "direction": r.direction,
            "strategy": r.strategy, "family": r.family, "tier": r.tier,
            "freq_class": r.freq_class,
            "fires_per_week": r.fires_per_week,
            "fires_per_month": r.fires_per_month,
            "corpus_wr_after_rule": r.corpus_wr_after_rule,
            "v9_wr": r.v9_wr,
            "shave_rule": r.shave_rule,
            "priority_score": r.fires_per_week * max(0, r.corpus_wr_after_rule - 0.40),
        })
pri = pd.DataFrame(rows).sort_values(["session_bucket","priority_score"],
                                      ascending=[True, False])
pri.to_csv(PRI_CSV, index=False)
print(f"wrote {PRI_CSV}  ({len(pri)} rows)")

# Print top cells per session
for sess in ("london_open","ny_open","ny_mid","ny_close","asia","asia_late","any"):
    s = pri[pri.session_bucket == sess]
    if not len(s): continue
    print(f"\n=== Priority queue: {sess} ({len(s)} cells) ===")
    print(s[["pair","regime","direction","family","strategy","freq_class",
             "fires_per_week","corpus_wr_after_rule","priority_score"]].to_string(index=False))

# JSON queue: bot can read this to drive bank-first generation
queue = {
    "version": 1,
    "created_at": "2026-05-20T23:30:00Z",
    "description": (
        "Bank-first priority queue. For the active session, the bot should "
        "evaluate these (pair, regime, direction, strategy) tuples FIRST "
        "by directly invoking the named strategy instead of relying on "
        "BB->direct generation to find them. session_bucket=='any' cells "
        "are session-agnostic and apply in every session."
    ),
    "min_freq_per_week": 0.25,
    "sessions": {},
}
for sess in pri.session_bucket.unique():
    s = pri[pri.session_bucket == sess]
    queue["sessions"][sess] = [
        {
            "pair": r.pair, "regime53": r.regime, "direction": r.direction,
            "strategy": r.strategy, "family": r.family, "tier": r.tier,
            "shave_rule": r.shave_rule,
            "fires_per_week": float(r.fires_per_week),
            "corpus_wr": float(r.corpus_wr_after_rule),
            "priority_score": float(r.priority_score),
        }
        for _, r in s.iterrows()
    ]
with open(QUEUE_JSON, "w") as f:
    json.dump(queue, f, indent=2)
print(f"\nwrote {QUEUE_JSON}")
