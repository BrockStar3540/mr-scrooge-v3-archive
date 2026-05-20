# Tomorrow: Winning-Bank Schedule Map

Per Brock 2026-05-19: stop forcing trades out of bad tuples. Instead,
map where the validated bank actually has edge and check whether the
bot is spending attention there.

The honest framing from tonight's mining pass: "no promotable edge for
the 15 active tuples under the current corpus and current depth-1
mining depth tonight." Not "universally dead." The right next move is
not deeper mining on those tuples -- it's understanding where the
real bank lives.

## Build

For every trade-tier cell (Seed-Pro / Pro / Elite) in v9_observe and
v10_fast_v1.4, generate one row of:

| field | description |
|---|---|
| pair | e.g. EUR_CAD |
| regime53 | C01 / C02 / ... |
| direction | long / short |
| family | direct / dbb_trend / reversal |
| strategy_id | e.g. charlie_compression_breakout |
| tier | Seed-Pro / Pro / Elite |
| wilson_lb | evidence floor |
| n_unique | trade count |
| shave_rule | the rule itself |
| historical_hour_distribution | hour_utc histogram of winning rows |
| typical_session | session_bucket where historical winners fell |
| has_hour_clause | yes/no (flag v9 fan-out artifact) |

## Compare against today's bot attention

For 2026-05-19's full bot session, bucket scan-time spent (or
candidate generation count) per (pair, session, direction). Compare:

- where the bot spent attention today
- where the validated bank actually lights up

## Decision points

1. If bank's hot tuples ARE being scanned but never satisfy shave_rule:
   regime/timing problem, not coverage. Wait or refine entry conditions.
2. If bank's hot tuples are NOT being scanned (pair not in scan list,
   or wrong session): fix coverage/scheduling.
3. If bank's hot tuples cluster in specific hours: schedule bot
   attention there.

## Sources

- data/routing_table_v9_observe.parquet (full bank, 3,073 rows)
- data/routing_table_v10_fast_v1_4.parquet (live, 29 rows)
- research/routing-table-v2-2026-05-14/ml_training_corpus.parquet (1.26M trade rows)
- data/seed-telemetry.jsonl (today bot attention)
- data/routing_rollup_2026-05-19.parquet (today router decisions)

## NOT this

- More mining on dead-tuple traffic
- Promoting fan-out / synthetic-session cells
- Lowering min_tier
