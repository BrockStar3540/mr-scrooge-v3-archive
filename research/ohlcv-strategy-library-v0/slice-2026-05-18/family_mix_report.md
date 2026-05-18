# Family-generation-vs-best-fit report — 2026-05-18

## Headline finding

The bot's live candidate generator is **98% direct family**, and the
entry-filter gate **strict-matches generator family to cell family**.
Result: in 11 hours of live flow with 4,101 candidates that found a
v9_observe cell match, **0 of them were cross-family matches**.

| metric | n |
|---|---:|
| Live candidates (entry_filter rows) | 4,832 |
| Direct-family candidates | 4,734 (98.0%) |
| dbb_trend-family candidates | 98 (2.0%) |
| reversal-family candidates | 0 |
| Candidates that found a v9 cell match | 4,101 |
| direct candidate → direct cell match | 4,008 |
| direct candidate → dbb_trend cell match | **0** |
| direct candidate → reversal cell match | **0** |

## What this means

For a slice like `C02 / ny_close / USD_CHF`, even if v9_observe has a
**dbb_trend** cell (`alpha_pullback_v2 long`, n=10, wr=1.00) that would
be the best historical fit for the slice, the bot **never exercises it**
because the gate filters by candidate-family.

The bot generates a `direct` candidate for USD_CHF, the gate looks only
for direct cells, and the dbb_trend cell sits unused even though it has
strong in-sample evidence.

## Two bottlenecks (not one)

1. **Tier bottleneck**: cells exist in v9_observe at Seed tier, blocked
   by `min_tier=Seed-Pro`. Fix: per-slice promotion (what v10_fast_v1.1
   does).
2. **Family-generation bottleneck**: 98% of candidates are direct. Even
   with the tier fix, dbb_trend/reversal alternates rarely get exercised.

## Implication for v10_fast_v1.1

The surgical v10_fast_v1.1 has 14 cells:
- 10 originals (9 direct + 1 dbb_trend) — fire on direct-heavy live flow
- 4 slice fallbacks for ny_close:
  - 1 direct (EUR_CAD charlie_compression_breakout long) — **will fire**
  - 3 dbb_trend/reversal — **will rarely fire** because bot doesn't
    generate those families enough

So v10_fast_v1.1 effectively adds 1 active ny_close cell
(`C02|EUR_CAD|charlie_compression_breakout|long|ny_close`). The 3
dbb_trend/reversal cells will accumulate live-shadow evidence over time
but won't fire until the generator produces more of those families.

## Strategic next moves

Three levers ranked by impact:

1. **Promiscuous-match mode in entry_filter.** When the candidate's
   exact family has no cell in the (regime, pair, session) leaf, try
   ANY cell at that leaf regardless of family. Risk: a direct candidate
   firing against a dbb_trend cell's shave_rule might not have the
   right entry/stop/TP setup. Mitigation: only promiscuous-match when
   the candidate's family has 0 cells AND the alternate family's cell
   has live-shadow validation.

2. **Boost dbb_trend / reversal generator weights.** The V3 scorer
   currently produces direct 98% of the time. Tune the scorer to
   produce more diverse families when the slice supports them.

3. **Build per-slice generator overrides.** For `C02/ny_close/USD_CHF`,
   force the generator to evaluate dbb_trend and reversal strategies
   even if they're not the default. This is regime-specific scoring.

## Recommended order
1. Option 2 is the cleanest -- scorer tuning. But requires regression
   testing to avoid breaking direct-heavy slices.
2. Option 1 is the fastest fix but introduces cross-family risk.
3. Option 3 is the most surgical but requires per-slice config.

## What v10_fast_v1.1 does in the meantime

- Adds 1 active ny_close cell (EUR_CAD direct long) — will fire if
  ADX14, RSI14, BB_compress etc. land in the cell's bands
- Adds 3 silent cells (dbb_trend/reversal alternates) — will accumulate
  shadow evidence but rarely fire
- Keeps the 10 original ny_open/ny_mid cells active for tomorrow's
  London/NY session

Net effect for tonight: minor (1 extra direct cell active).
Net effect for tomorrow: full active set of 14 cells available.
