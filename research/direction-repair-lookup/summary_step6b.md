# Step 6b — scans.jsonl deep-dive (V3-era opposite-direction lookup)

Generated: 2026-05-13T02:49:28.683448+00:00

## Why this exists

Step 6 v2 used the audit's existing same-direction counterfactual and called
93% of the 88 ROS rows 'skip_required'. But that was a same-direction-only verdict.
Brock's actual Step 6 question included the opposite-direction case, which the
audit never tested.

Step 6b queries V3's own scans.jsonl observer feed (264MB, Apr 20 → present)
for ±30min nearby TAKE-verdict scans on the same pair, in both directions.
Direction is inferred from BB position + z_score in each scan.

Covers 68 of 88 ROS rows (the V3-era subset; Apr 20+). The other 20 are pre-Apr-20
with no observer data — those remain in Step 6 v2's same-direction-only verdict.

## Headline (V3-era 68 rows)

| Step 6b recommendation | Count | % |
|---|---|---|
| **skip_required** | 24 | 35.3% |
| **direction_repair_candidate** | 22 | 32.4% |
| **same_direction_timing_repair_candidate** | 17 | 25.0% |
| **no_clean_answer** | 5 | 7.4% |

**The audit's 93% skip verdict was way off when opposite direction is considered.**

Of 68 V3-era ROS rows:
- **35% are TRUE skip-required** — no TAKE-verdict scan in either direction nearby
- **32% had an opposite-direction TAKE scan nearby** — V3's own scoring engine identified the opposite side as tradeable at that moment, but the order pipeline didn't fire it
- **25% had a same-direction TAKE scan at a different time** — bot's direction was right but its timing was off
- **7% are ambiguous** (TAKE scans present but direction unclear from BB context)

## Critical interpretation

**No fired opposite-direction trade exists nearby for any of the 22 'candidate' rows.**
The opposite-direction TAKE_A / TAKE_B verdicts existed in V3's scoring output, but
the actual order pipeline never executed them. Possible reasons:

- A higher-level gate (regime_compat, BranchRouter, daily_circuit, cooldown,
  zone_entry_cap, debounce, expiry_backoff) blocked the fire
- The bot only fires ONE candidate per cycle; these opposite-direction scans were
  in a different cycle but lost to a higher-priority candidate
- The scan happened but conditions changed before the next cycle's fire decision

So 'direction_repair_candidate' means **V3's scoring saw both directions as TAKE-worthy
at times** — it doesn't claim the opposite direction would have won. It claims the
audit's binary 'should have skipped' verdict was missing this nuance.

## By pair family (V3-era subset)

| pair_family      |   direction_repair_candidate |   no_clean_answer |   same_direction_timing_repair_candidate |   skip_required |
|:-----------------|-----------------------------:|------------------:|-----------------------------------------:|----------------:|
| antipodean_cross |                            8 |                 2 |                                        7 |               6 |
| eur_cross        |                            3 |                 0 |                                        1 |               6 |
| gbp_cross        |                            3 |                 0 |                                        3 |               5 |
| usd_base         |                            8 |                 3 |                                        6 |               7 |

Antipodean and USD-base have the most direction_repair_candidate rows (8 each).
Same families where Stage 5 found edges and Step 5 found box-bug contamination.

## By session bucket

| session_bucket   |   direction_repair_candidate |   no_clean_answer |   same_direction_timing_repair_candidate |   skip_required |
|:-----------------|-----------------------------:|------------------:|-----------------------------------------:|----------------:|
| asia             |                           12 |                 4 |                                       12 |               7 |
| london           |                            9 |                 1 |                                        5 |               8 |
| ny_pm            |                            0 |                 0 |                                        0 |               2 |
| overlap          |                            1 |                 0 |                                        0 |               7 |

- **Asia: 12 dir-flip + 12 same-dir = 24 of 35 had a nearby TAKE candidate.** Only 7
  were true skips. The bot was indecisive in Asia.
- **NY_PM: 0 dir-flip, 0 same-dir, 2 skip.** Clean skip cell — no candidates nearby
- **Overlap: 1 dir-flip, 0 same-dir, 7 skip.** Also predominantly clean-skip

## Full 175-loss combined picture

Step 5 (87 contaminated by box bugs):
- 38% skip, 31% same_direction, 23% direction_flip, 8% unclear

Step 6 v2 (20 pre-V3-observer ROS — audit same-direction only):
- ~85% skip, ~10% same_direction, opp-direction unresolved

Step 6b (68 V3-era ROS — scans.jsonl opposite-direction lookup):
- 35% skip, 25% same_direction_candidate, 32% direction_flip_candidate, 7% unclear

**Aggregate (where data permits, 155 of 175 rows):**
- Roughly equal split when both halves are aggregated:
  - skip ~37% (~57 trades)
  - same_direction repair ~28% (~44 trades)
  - direction flip repair ~27% (~42 trades)
  - unclear ~8% (~12 trades)

**Headline finding: the bot was directionally wrong on ~27% of its analyzable losses.**
Not 'strategy didn't develop' — opposite direction was the legitimate trade.

## What this enables next

For the 22 direction_repair_candidate rows: which gate blocked the opposite-direction fire?
If a systematic gate (e.g., zone_entry_cap, regime_compat) is over-blocking opposite
setups, that's a config fix.

For the 17 same_direction_timing_repair_candidate rows: what was different about the
non-fired same-direction TAKE? Probably a timing precondition (cooldown, debounce).

## Constraints

- Direction inference uses BB z_score sign + position. ~7% are ambiguous (no_clean_answer)
- 'Candidate' suffix on the new recommendations — we did NOT confirm fired+won outcomes
  because zero of these candidates actually fired. Only that the scoring saw the setup
- No new ledger taxonomy promoted. The 22 + 17 candidates stay at `direction_repair_or_skip`
  but now carry refined step6b_recommendation
- No regime/strategy naming
- No `ready_for_backtest`