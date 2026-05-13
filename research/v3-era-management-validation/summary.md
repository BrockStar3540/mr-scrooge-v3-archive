# V3 Broker-Era Directional Management Validation

Generated: 2026-05-13T03:50:31.636807+00:00

## TL;DR — ADR NOT YET JUSTIFIED

The direction asymmetry HOLDS qualitatively (shorts benefit from early BE; longs untouched).
BUT the magnitude collapses on V3-era actual broker data, and the winners-at-risk caveat is
material enough that net benefit could go negative in live production.

**Recommendation: do not draft ADR yet. The validation gate fails at this n.**

## Method

- 98 V3-era broker trades (entry_ts ≥ 2026-04-20, scans.jsonl coverage)
- 92 had usable forward-walk anchor (6 missed scan anchor within ±5min)
- Forward-walk via scan current_close to compute MFE in pips, converted to R using
  V3's actual `natural_stop_pips` (or atr fallback if missing)
- V0 baseline = broker's actual realized_r (real V3 outcome)
- Variants: short BE@{0.5, 0.6, 0.7}R floor at 0 for losers, longs untouched

## Sample

- 92 usable trades: 56 shorts, 36 longs
- Strategy: 27 direct, 16 dbb_trend, 49 unknown (pre-V3-strategy labels)
- MFE distribution: min 0.00, median 0.20, max 2.00R

## Global result

| variant         |   n |   total_R |   mean_R |   winner_rate |   delta_total_R |   delta_per_trade |
|:----------------|----:|----------:|---------:|--------------:|----------------:|------------------:|
| V0_baseline     |  92 |   -39.835 |   -0.433 |         0.293 |           0.000 |             0.000 |
| V_short_BE_0.5R |  92 |   -34.632 |   -0.376 |         0.293 |           5.203 |             0.057 |
| V_short_BE_0.6R |  92 |   -34.632 |   -0.376 |         0.293 |           5.203 |             0.057 |
| V_short_BE_0.7R |  92 |   -34.632 |   -0.376 |         0.293 |           5.203 |             0.057 |

**+5.2R lift** across 92 trades. **+0.057R per trade**. Compared to the 90K sim's +0.235/trade,
the V3-era benefit is **~4× smaller**. Two reasons:
1. V3's existing management already captures more favorable moves before MFE reaches 0.5R
2. With V3's tighter natural_stop_pips, many shorts exit faster — fewer reach MFE 0.5R

## Per-direction

**SHORTS (n=56):**
- baseline: −18.6R (−0.333/trade)
- BE@0.5R: −13.4R (−0.240/trade)  Δ = +5.2R = +0.093/trade
- BE@0.6R: identical to 0.5R
- BE@0.7R: identical to 0.5R

**LONGS (n=36):**
- baseline: −21.2R (−0.589/trade)  Δ = 0 in all variants (rule unchanged for longs)

**All three thresholds (0.5/0.6/0.7) give IDENTICAL lift.** Means no short winner
had mfe between 0.5R and 0.7R that flipped via threshold sensitivity — all the BE
triggers happened well above 0.7R. **No fine-tuning benefit at this n.**

## Per strategy × direction

| strategy   | direction   |   n |   baseline_total_R |   baseline_mean_R |   BE_0.5R_total |   BE_0.7R_total |   delta_BE_0.5 |   delta_BE_0.7 |
|:-----------|:------------|----:|-------------------:|------------------:|----------------:|----------------:|---------------:|---------------:|
| dbb_trend  | long        |   1 |             -1.057 |            -1.057 |          -1.057 |          -1.057 |          0.000 |          0.000 |
| dbb_trend  | short       |  15 |             -5.509 |            -0.367 |          -4.427 |          -4.427 |          1.082 |          1.082 |
| direct     | long        |  20 |            -13.554 |            -0.678 |         -13.554 |         -13.554 |          0.000 |          0.000 |
| direct     | short       |   7 |             -0.522 |            -0.075 |          -0.522 |          -0.522 |          0.000 |          0.000 |
| unknown    | long        |  15 |             -6.579 |            -0.439 |          -6.579 |          -6.579 |          0.000 |          0.000 |
| unknown    | short       |  34 |            -12.615 |            -0.371 |          -8.494 |          -8.494 |          4.121 |          4.121 |

- **dbb_trend/short** (n=15): +1.08R lift
- **direct/short** (n=7): 0 lift (none tripped BE)
- **unknown/short** (n=34, pre-V3-strategy labels): +4.12R lift

Most of the +5.2R global lift comes from the `unknown` strategy bucket — pre-V3 trades
with unlabeled strategy. The named V3 strategies (direct + dbb_trend) only contribute
+1.08R combined from 22 short trades.

## Pocket-level: where the lift concentrates

Top cells by BE@0.5R delta:

| pair_family      | direction   | session_bucket   |   n |   baseline_total_R |   BE_0.5R_total |   BE_0.7R_total |   delta_BE_0.5 |   delta_BE_0.7 |
|:-----------------|:------------|:-----------------|----:|-------------------:|----------------:|----------------:|---------------:|---------------:|
| gbp_cross        | short       | asia             |   5 |             -2.887 |          -1.805 |          -1.805 |          1.082 |          1.082 |
| eur_cross        | short       | asia             |   4 |              1.683 |           2.724 |           2.724 |          1.041 |          1.041 |
| eur_cross        | short       | overlap          |   2 |             -2.076 |          -1.036 |          -1.036 |          1.040 |          1.040 |
| eur_cross        | short       | london           |   4 |             -3.006 |          -1.968 |          -1.968 |          1.038 |          1.038 |
| antipodean_cross | short       | london           |   3 |              1.991 |           2.994 |           2.994 |          1.003 |          1.003 |
| antipodean_cross | long        | london           |   4 |             -2.483 |          -2.483 |          -2.483 |          0.000 |          0.000 |
| antipodean_cross | long        | asia             |  10 |             -8.258 |          -8.258 |          -8.258 |          0.000 |          0.000 |
| eur_cross        | long        | london           |   5 |             -0.163 |          -0.163 |          -0.163 |          0.000 |          0.000 |
| eur_cross        | long        | asia             |   3 |              0.780 |           0.780 |           0.780 |          0.000 |          0.000 |
| antipodean_cross | short       | asia             |   9 |             -4.903 |          -4.903 |          -4.903 |          0.000 |          0.000 |

Pattern: lift is concentrated in **eur_cross and gbp_cross shorts**. The biggest
V3-era short pocket — **usd_base/short/asia (n=12)** — shows ZERO benefit. That directly
contradicts the sim's strongest pocket finding (sim said usd_base shorts in Asia had
highest lift).

## The CRITICAL CAVEAT: short winners at risk

- 19 V3-era short winners total
- **7 (37%) have MFE >= 0.5R** — these are the winners that REACHED the BE trip level
- Total R from those at-risk winners: **+8.20R**

**In live production**, the BE@0.5R rule could be tripped by retracement on a winning
short before it reaches TP. Some fraction of those 8.20R would be lost as winners get
stopped at BE instead of running to TP.

**Net math (conservative live model):**
- Gain from BE catching losers: +5.20R
- Loss from BE stopping winners early: up to −8.20R (worst case, all retrace)
- **Realistic live net: between −3R and +5R**
- Possibly NEGATIVE depending on retracement rate

## Compared to the 90K-sim result

| Metric | 90K sim | V3-era actual |
|---|---|---|
| Per-trade short lift | +0.41R | +0.09R (4× smaller) |
| Total short R lift | +21,140 | +5.2 |
| Strongest cell | usd_base/short/asia | usd_base/short/asia = 0 |
| Winners-at-risk warning | implicit | 37% of short winners |
| ADR justified | yes (per sim) | NO (per live data) |

**The sim was too generous.** V3's actual management is already doing more work than the
walker's 1×ATR-stop / 2R-target assumption modeled. The marginal benefit of BE@0.5R on
top of V3's existing logic is small.

## Why the validation gate matters here

Without this V3-era pass, we would have:
1. Drafted ADR for BE@0.5R for shorts
2. Promoted to production
3. Realized in live trading that the benefit is +0.09R/trade not +0.24
4. AND lost some short winners to premature BE
5. Net: marginal-to-negative outcome, with the cost of changing production behavior

The Brock protocol's '1 live-contract validation pass' caught this. Cost: 1 forward-walk
pass on the 90K dataset's V3-era subset. Saved: a half-baked config change.

## What's TRUE

- Direction asymmetry is real (shorts give back more than longs)
- LONGS don't need capping. The 90K-sim 'long cap is catastrophic' finding holds.
- BE@0.5R for shorts DOES help in some cells (cross-pair shorts)
- The qualitative thesis is correct

## What's NOT TRUE at V3 scale

- +0.24R/trade lift for BE@0.5R-on-shorts (only +0.09 in V3-era)
- usd_base/short is the biggest beneficiary (it shows 0 lift in V3-era)
- 0.5/0.6/0.7 threshold optimization (all identical at this n)
- Single-rule deployment justified by the sim alone

## What's needed before ADR

1. **Larger V3-era sample**: 56 shorts is too few to estimate winners-at-risk reliably
2. **Threshold separation**: 0.5/0.6/0.7 need enough n to show meaningful difference
3. **Live-or-shadow A/B**: simulate BE rule against more V3 trades to see realistic retrace haircut
4. **Pocket targeting**: if the rule works only in cross-pair shorts (not usd_base), it
   should be pocket-conditional, not global

## Honest verdict

- **Direction-asymmetric management thesis: VALIDATED qualitatively.** Longs and shorts are
  not the same trade. This part of Brock's framing is correct.
- **'BE@0.5R for shorts' as the deployable rule: NOT VALIDATED at V3 scale.** The benefit
  is small, the winners-at-risk is real, the pocket-specificity is unclear.
- **ADR draft: not yet justified.** Need more V3-era data or a tighter pocket-conditional
  formulation.

## What's queued

1. **Continue V3 live observation**: accumulate more V3-era trades over time, re-run this
   validation in a few weeks with bigger n
2. **Per-pocket validation**: if cross-pair shorts in london/asia really do benefit (the
   tiny but consistent +1R deltas), that might justify a pocket-conditional rule
3. **Move research budget elsewhere**: direction asymmetry is logged as a research finding
   but is not currently a deployable lever
4. **Track Brock's framing as the methodology principle**: 'longs and shorts are not the
   same trade' is the conceptual anchor going forward, not a specific config rule yet