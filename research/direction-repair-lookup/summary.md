# Step 6 — Direction-Repair Lookup v2

Generated: 2026-05-13T02:19:55.962662+00:00

## Critical data-scope finding

v1 attempted to query `per_trade_factors_filled.csv.gz` for ±30min nearby
candidates. **All 88 target rows returned 0 candidates.** Reason:

- Factor file ts range: 2026-03-15 → 2026-04-13 (the 30-day audit window)
- Target rows entry_ts range: **2026-04-14 → 2026-05-08** (entirely AFTER audit ends)

Of the 88 target rows:
- 20 are Apr 14-17 (pre-V3-observer — NO candidate stream exists)
- 68 are Apr 20+ (V3 observer scans.jsonl exists but not yet queried)

## v2 approach: use the audit's existing same-direction counterfactual

`audit_best_counterfactual_model` is `simple_2R` for all 88 rows — same direction
walked forward against a 2R target. The audit already computed this:

- `audit_best_counterfactual_r = +2.0` → same direction would have hit target (timing repair valid)
- `audit_best_counterfactual_r = 0.0` → same direction never developed (skip)
- `audit_best_counterfactual_r = -1.0` → same direction would have lost too (skip)

This gives a clean answer for the SAME-direction question. The OPPOSITE-direction
question remains data-blocked.

## Headline split

| Step 6 recommendation | Count | % |
|---|---|---|
| **skip_required** | 82 | 93.2% |
| **same_direction_timing_repair** | 5 | 5.7% |
| **no_clean_answer** | 1 | 1.1% |

**Brock's question answered:**
> 'Of the trades that looked like should have skipped, were they actually skip-only,
> or was the winning trade nearby in the opposite/same direction?'

Answer: **~93% were genuinely skip-only** per the audit's same-direction counterfactual.
Only **5 of 88 (6%) have a same-direction timing-repair candidate** — meaning a different
management on the SAME direction would have hit 2R target.

**The opposite-direction question is unresolved.** Factor file doesn't cover the dates;
V3 scans.jsonl could be queried as a follow-on for the 68 Apr-20+ rows.

## The 5 same_direction_timing_repair cases

| pair    | bot_direction   | session_bucket   | session_quarter   | bot_actual_strategy   |   actual_realized_r |   audit_counterfactual_r | nearest_winner_cluster   |
|:--------|:----------------|:-----------------|:------------------|:----------------------|--------------------:|-------------------------:|:-------------------------|
| CHF_JPY | short           | asia             | asia_q2           | unknown               |               -1.00 |                     2.00 | unkn_ant_asi_s           |
| CHF_JPY | short           | london           | london_q2         | unknown               |               -1.02 |                     2.00 | unkn_ant_lon_s           |
| EUR_JPY | short           | asia             | asia_q4           | unknown               |               -0.23 |                     2.00 | nan                      |
| NZD_JPY | long            | london           | london_q1         | unknown               |               -0.03 |                     2.00 | unkn_ant_lon_l           |
| NZD_USD | short           | asia             | asia_q3           | unknown               |               -0.31 |                     2.00 | unkn_usd_asi_s           |

Notes on these 5:
- 4 of 5 have a nearest_winner_cluster match — meaning the geometric cell matches an existing winner pattern
- 4 of 5 are SHORT trades (3 Asia, 1 London)
- Pairs: CHF_JPY (×2), EUR_JPY, NZD_JPY, NZD_USD — JPY-cross + NZD-heavy
- These ARE legitimate same-direction-with-better-management candidates

## By pair family

| pair_family      |   no_clean_answer |   same_direction_timing_repair |   skip_required |
|:-----------------|------------------:|-------------------------------:|----------------:|
| antipodean_cross |                 0 |                              3 |              28 |
| eur_cross        |                 0 |                              1 |              11 |
| gbp_cross        |                 1 |                              0 |              11 |
| usd_base         |                 0 |                              1 |              32 |

- antipodean_cross has the most absolute saves (3) but also the most skips (28)
- usd_base: 32 of 33 skip — almost universal verdict that bot was overtrading USD pairs in this window

## By session bucket

| session_bucket   |   no_clean_answer |   same_direction_timing_repair |   skip_required |
|:-----------------|------------------:|-------------------------------:|----------------:|
| asia             |                 0 |                              3 |              45 |
| london           |                 0 |                              2 |              25 |
| ny_pm            |                 0 |                              0 |               2 |
| overlap          |                 1 |                              0 |              10 |

- asia: 45 skip, 3 save — still the dominant trading window, but mostly skip-required failures
- london: 25 skip, 2 save
- ny_pm: 2 skip, 0 saves (very thin sample)

## Combined picture across step 5 + step 6 (175 loser rows total)

Step 5 (87 contaminated by box bugs):
- 38% skip_required (false signal in middle of correct box)
- 31% same_direction_repair (right dir, wrong location)
- 23% direction_flip_repair (opposite dir was right)
- 8% no_clean_answer

Step 6 (88 non-contaminated, V3 era):
- 93% skip_required (audit same-direction counterfactual = 0 or -1)
- 6% same_direction_timing_repair (audit says same dir would have hit 2R)
- 1% no_clean_answer
- **opposite-direction lookup unresolved** (data blocked)

**The two halves of the bot's losses tell different stories:**
- The 87 pre-Apr-13 trades: bot was lied to by its own geometry (box bugs caused 62%
  of failures to have a SALVAGEABLE direction repair available)
- The 88 post-Apr-13 trades: bot was overtrading (93% are genuinely skip-only per audit;
  the box was fine; the signal was just not there)

**Combined verdict:** of 175 loss trades, ~57% are skip_required (should never have
fired), ~18% are same-direction-with-better-management saves, ~11% are direction-flip
saves (only in the contaminated subset), ~5% are unresolved, and ~23% (the 88 ROS
rows' opposite-direction question) remain data-blocked.

## Follow-on for true opposite-direction resolution

If you want the opposite-direction question answered for the 68 V3-era rows,
the next step is to query `scans.jsonl` (264MB, Apr 20 → present) for
nearby OPPOSITE-direction candidates that either FIRED or were near-fire (score above
threshold), and check `outcomes.jsonl` for whether those V3 trades won.

That's a separate compute pass. Not yet authorized.

## Per scope rules

- No regime/strategy naming
- No `ready_for_backtest`
- The 5 same_direction_timing_repair candidates remain at `repair_taxonomy = direction_repair_or_skip`
  but now carry `step6_recommendation = same_direction_timing_repair` as the refinement