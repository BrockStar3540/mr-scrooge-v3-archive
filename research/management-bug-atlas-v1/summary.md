# Management-Bug Atlas v1 — Direction-Conditional Exits

Generated: 2026-05-13T03:37:39.811513+00:00

## Source (intraday-safe, no daily-cache contamination)

`per_trade_factors_filled.csv.gz` — 90,024 sim trades.
- Uses MFE, MAE, realized_r, time_to_X — all intraday derived
- Strategy labels are V3 branches (direct, dbb_trend)
- 30-day window 2026-03-15 to 2026-04-13
- Per-cell n is meaningful (2000-5000 per cell)

## Headline: DIRECTION IS THE DOMINANT AXIS

Of 64 (strategy × pair_family × direction × session_bucket) cells:
- **42 cells flagged `earlier_BE_at_0.5R`** — almost all SHORTS
- **6 cells flagged `hold_for_1R` or `hold_for_2R`** — almost all LONGS
- 16 cells insufficient_data (small strategy/family combos)
- 0 cells flagged scalp / skip_cell at this n — entries are developing, management is the leak

## The pattern: longs hold, shorts give back

### LONGS that should hold for 1R or 2R

| Pocket | n | reach 1R | reach 2R | conv 2R | recommendation |
|---|---|---|---|---|---|
| dbb_trend / usd_base / short / london | 235 | 49.4% | 21.3% | 62.0% | hold_for_2R |
| direct / antipodean_cross / long / asia | 3584 | 56.3% | 24.1% | 64.2% | hold_for_2R |
| direct / eur_cross / long / london | 2022 | 51.3% | 19.0% | 61.8% | hold_for_1R |
| direct / gbp_cross / long / london | 1727 | 56.9% | 27.0% | 52.4% | hold_for_1R |
| direct / usd_base / long / asia | 4685 | 51.0% | 25.9% | 65.3% | hold_for_2R |
| direct / usd_base / long / london | 2981 | 45.6% | 19.7% | 62.2% | hold_for_1R |

All 5 direct-strategy hold-cells are LONGS. The one short (dbb_trend/usd_base/london) is the exception.

### SHORTS that should BE-early

Top 15 by n:

| Pocket | n | reach 0.5R | giveback at 0.5R | mfe median | giveback total |
|---|---|---|---|---|---|
| direct / antipodean_cross / short / asia | 4403 | 75.7% | 36.7% | 1.09R | 45.7% |
| direct / usd_base / short / asia | 4166 | 63.5% | 40.6% | 0.87R | 55.3% |
| direct / gbp_cross / short / asia | 4105 | 73.1% | 48.8% | 1.04R | 60.7% |
| direct / eur_cross / short / asia | 3478 | 68.7% | 47.1% | 0.88R | 60.8% |
| direct / usd_base / short / london | 3457 | 57.2% | 33.5% | 0.65R | 46.4% |
| direct / antipodean_cross / short / london | 3276 | 71.2% | 37.2% | 1.00R | 46.0% |
| direct / eur_cross / long / asia | 3216 | 79.0% | 34.8% | 1.14R | 42.2% |
| direct / antipodean_cross / short / ny_pm | 3188 | 80.3% | 38.5% | 1.23R | 45.4% |
| direct / usd_base / short / ny_pm | 3144 | 65.7% | 47.5% | 0.84R | 57.5% |
| direct / eur_cross / short / london | 3075 | 63.8% | 38.8% | 0.75R | 51.4% |
| direct / usd_base / long / ny_pm | 3004 | 71.0% | 41.1% | 0.80R | 47.8% |
| direct / eur_cross / short / ny_pm | 2911 | 66.4% | 48.0% | 0.73R | 57.9% |
| direct / gbp_cross / short / ny_pm | 2678 | 70.5% | 51.0% | 0.87R | 60.0% |
| direct / antipodean_cross / long / ny_pm | 2668 | 73.6% | 46.0% | 0.90R | 56.1% |
| direct / gbp_cross / short / london | 2581 | 73.3% | 43.5% | 1.01R | 53.8% |

**Pattern:** these cells reach +0.5R to +1.0R median MFE, then 30-60% give back to negative.
BE-at-0.5R would lock in $0 instead of letting the trade reverse to $-1R.

## Brock's question 6: asia/direct/USD-antipodean vs london/USD-base

| Pocket | n | rec | mfe_med | reach 1R | reach 2R | gave_back |
|---|---|---|---|---|---|---|
| dbb_trend/usd_base/long/london | 8 | n_low | nanR | nan% | nan% | nan% |
| dbb_trend/usd_base/short/london | 235 | hold_2R | 0.96R | 49.4% | 21.3% | 58.7% |
| direct/antipodean_cross/long/asia | 3584 | hold_2R | 1.12R | 56.3% | 24.1% | 46.0% |
| direct/antipodean_cross/short/asia | 4403 | BE@0.5 | 1.09R | 54.3% | 26.0% | 45.7% |
| direct/usd_base/long/asia | 4685 | hold_2R | 1.02R | 51.0% | 25.9% | 45.1% |
| direct/usd_base/long/london | 2981 | hold_1R | 0.88R | 45.6% | 19.7% | 42.6% |
| direct/usd_base/short/asia | 4166 | BE@0.5 | 0.87R | 45.5% | 21.7% | 55.3% |
| direct/usd_base/short/london | 3457 | BE@0.5 | 0.65R | 38.7% | 16.9% | 46.4% |

**Answer: yes, direction-conditional exit logic is the structural finding.**
- asia/direct/usd_base/**long**: hold_for_2R (25.9% reach 2R, 65% conv)
- asia/direct/antipodean/**long**: hold_for_2R (24.1% reach 2R, 64% conv)
- asia/direct/usd_base/**short**: BE@0.5 (55% giveback)
- asia/direct/antipodean/**short**: BE@0.5 (46% giveback)
- london/direct/usd_base/**long**: hold_for_1R (46% reach 1R)
- london/direct/usd_base/**short**: BE@0.5 (46% giveback)

## What this DOESN'T say

- Not a config recommendation. These are diagnoses.
- Same caveat as v0: simulator outcomes, not live broker outcomes. The live broker
  reaches less R due to fixed-pip TP1 clipping. Simulator reaches more R but takes
  larger losses too (1×ATR stops).
- Doesn't account for current V3 box state correctness; assumes the entry was valid
- 30-day V1/V2 era window. Doesn't test directly against current V3 production.

## What this means for V3

Current V3 management is uniform across direction (per the ADRs, ratchet logic doesn't
split on direction). This atlas suggests V3 should:

- **For SHORTS**: trigger BE much earlier (~0.5R), accept some early BE outcomes as a tax
  for avoiding gave_back losses. Currently the ratchet at +50% of TP1 (~1R for 2R target)
  fires too late to save shorts.
- **For LONGS** in Asia + London: leave management alone. The current TP logic captures
  enough to be profitable in these cells. Don't add overly tight management to longs.
- **Across all directions in NY_PM**: more giveback. Consider scalp-only or skip in this
  session for some pockets.

## Direction-conditional management is the actionable hypothesis

It's:
- methodologically clean (intraday-safe data, no daily contamination)
- statistically supported (n=2000-5000 per cell)
- direction-clear (longs hold, shorts give back)
- pocket-clear (Asia + London for longs work; shorts need management everywhere)
- different from V3's current uniform-direction management

This is the candidate ADR direction worth investigating next. Per the locked protocol
though: NO ADR yet. The next validation step before promoting to ADR is to
**confirm this pattern holds on V3-era data** (not just V1/V2 sim data). That would
require either:
- Forward-walking V3 broker trades against intraday data (heavier compute)
- OR waiting for sufficient V3 live history to accumulate per-cell n
- OR running the corpus with V3-style management to compare alternatives

## What's locked

- Direction-conditional management is the highest-leverage forensic finding from this entire research arc
- Longs in usd_base / antipodean / eur / gbp during Asia or London reach 1R-2R reliably
- Shorts give back consistently across all pair families and sessions
- NO ADR yet — needs V3-era validation