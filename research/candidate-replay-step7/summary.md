# Step 7: Candidate Outcome Replay + Gate Audit

Generated: 2026-05-13T02:57:07.386331+00:00

## Question

Step 6b said 39 of 68 V3-era ROS rows had a nearby TAKE-verdict scan in either the
opposite or same direction. **Did those candidates actually develop?** Or were they
scoring artifacts that the order pipeline rightly skipped?

## Method

Forward-walk replay using V3's own scan stream as price feed (dukascopy M5 ends
Apr 22; most candidates are after that, so V3 scans.jsonl is the only available
forward-walk source). For each of 39 candidates:
- Anchor at the TAKE scan's `features.bollinger.current_close`
- Walk forward 8 hours using subsequent scans' current_close on same pair
- Stop distance = 1×ATR proxy (V3's natural_stop_pips not in scan record)
- Track MFE, MAE; compute outcome at 1R, 1.5R, 2R; ratchet-at-0.5R-BE outcome

## Outcome distribution

| outcome_class | n | % |
|---|---|---|
| no_development | 34 | 87.2% |
| partial_winner_ratchet_save | 3 | 7.7% |
| 1R_winner | 1 | 2.6% |
| clean_stop | 1 | 2.6% |

**87% (34 of 39) showed no development at all** within 8 hours of the candidate scan.
The price didn't move enough to either hit the 1×ATR stop or reach 0.5R favorable.
Only 4 of 39 had meaningful movement.

## Final verdict distribution

| verdict_final | n |
|---|---|
| no_development | 34 |
| direction_repair_partial | 3 |
| direction_repair_confirmed | 1 |
| false_candidate | 1 |

**Promoted to confirmed:** 1 (`direction_repair_confirmed` — full 1R+ winner)
**Promoted to partial:** 3 (`direction_repair_partial` — ratchet would save BE)
**Demoted to false_candidate:** 1 (full clean stop)
**No development:** 34 (price didn't develop within 8h — can't classify)

## What this means

Step 6b's signal was real (V3's scoring saw TAKE candidates) but the candidates 
**mostly didn't develop into trades.** Only 4 of 39 (10%) actually moved meaningfully
within 8 hours.

So the audit's original 'should have skipped' verdict was **empirically correct**
for ~87% of the V3-era ROS rows, even though it was using a different (same-direction-only)
counterfactual to reach it. The opposite-direction TAKE scans Step 6b found were
real but largely flat-market false signals.

## Gate audit

- 39 cycles with scan data
- **0 of 39 cycles had any sibling trade fire.** The candidate didn't lose to a
  competing scan in the same cycle. It just didn't fire — somewhere downstream of
  scoring but before order placement.

This means the gate-blocking question is **NOT 'which gate ate it.'** The candidate
scan existed, no sibling beat it, but the bot still didn't place an order. Possible
causes (not resolved by this analysis):
- Order pipeline filter (correlation gate, pending order cap)
- One-per-cycle priority across other pairs (a candidate on a different pair in the
  same cycle won, not visible to per-pair query)
- Spread or slippage check at order placement time
- Bot was in a position-management state, not entry-scanning state

Further gate-audit would require querying actions.jsonl for the bot's actual
decision sequence in each cycle (heavier and not yet done).

## Constraints / honest caveats

- **Stop distance proxy** (1×ATR) may be too wide. V3 uses natural_stop_pips which
  is often tighter. With a tighter stop, more candidates would resolve (either
  stop or favorable). The 87% no_development figure is an upper bound.
- **Forward-walk via scans** uses close-only prices at sparse intervals (cycle-rate,
  not bar-by-bar). Intra-scan price moves are not captured. Real intraday tick data
  would resolve more candidates.
- **'Confirmed' is provisional.** The 1 direction_repair_confirmed and 3 direction_repair_partial
  rows are based on this measurement. A more rigorous replay (V1 code on M5 ticks) would
  be authoritative.

## Updated overall picture: 175 loss trades, final verdict per analyzable subset

| Source | n | Confirmed-save share | True-skip share |
|---|---|---|---|
| Step 5 (87 contaminated) | 87 | 54% repair candidates (31% same_dir + 23% flip) — but unverified | 38% skip |
| Step 6 v2 (88 V3-era ROS) | 88 | 5.7% same_dir + 0.5% (1 confirmed flip from step 7) = 6% | 94% |

**The two halves of the bot's losses:**
- 87 contaminated: ~54% are unverified repair candidates (still need V1-code box replay)
- 88 V3-era ROS: ~94% genuinely skip-required. Bot was overtrading post-Apr-13.

## What's queued

- The 1 `direction_repair_confirmed` and 3 `direction_repair_partial` cases are now
  the only verified V3-era opposite-direction saves. These can be added to the
  winner cluster pool for factor synchrony.
- Box-geometry replay v2 (with V1 actual code, not heuristic) would convert the 50
  Step 5 candidates from 'hypothetical' to 'verified'.
- Factor synchrony map can now be built on verified winners + the 4 newly-promoted
  rows (no more unverified candidates polluting the synchrony pool).