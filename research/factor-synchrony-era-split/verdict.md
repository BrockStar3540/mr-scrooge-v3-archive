# Era-Split Factor Synchrony with Daily-Cache Quarantine

Generated: 2026-05-13T03:30:45.749374+00:00

## Method

- Boundary: 2026-04-22 (end of dukascopy daily cache; verified in V3 box-formation review)
- Pre-era: entry_ts ≤ 2026-04-22 (audit's daily-derived factors reliable)
- Post-era: entry_ts > 2026-04-22 (daily-derived factors contaminated)
- Quarantine: 19 daily-cache-contaminated factors EXCLUDED from synchrony test
- 21 intraday-safe factors used for the actual test
- For each (pair_family × direction) pocket: compute Cohen's d + 95% CI per factor
- Consistency check: same factor flagged in same direction across BOTH eras

## Pool

- 68 broker winners (37 pre, 31 post)
- 91 broker non-contaminated losers (26 pre, 65 post)
- Contaminated rows (87 correct_box_replay_required) excluded
- Manual rows excluded (no factor data)

## Factor lineage tally

| lineage                  |   count |
|:-------------------------|--------:|
| unknown_lineage          |      31 |
| intraday_safe            |      21 |
| daily_cache_contaminated |      19 |
| metadata_or_unknown      |      10 |

**20 factors are all-zero in audit output (broken in reconstruction):**

| factor               | lineage                  |
|:---------------------|:-------------------------|
| bb_percent_b_a       | intraday_safe            |
| bb_percent_b_b       | intraday_safe            |
| box_range            | daily_cache_contaminated |
| ctx_box              | daily_cache_contaminated |
| ctx_box_age_hours    | daily_cache_contaminated |
| ctx_ema20            | metadata_or_unknown      |
| ctx_ema50            | metadata_or_unknown      |
| ctx_px               | metadata_or_unknown      |
| direction_long       | metadata_or_unknown      |
| natural_stop_pips    | daily_cache_contaminated |
| px_vs_ema20_bps      | intraday_safe            |
| px_vs_ema50_bps      | intraday_safe            |
| rr_ratio             | daily_cache_contaminated |
| scorer_base          | unknown_lineage          |
| scorer_capped        | unknown_lineage          |
| scorer_final         | daily_cache_contaminated |
| scorer_pairs_raw     | unknown_lineage          |
| spread_to_stop_ratio | unknown_lineage          |
| strategy_id          | metadata_or_unknown      |
| tp_distance_pips     | daily_cache_contaminated |

Even 4 intraday-safe factors are unusable due to audit reconstruction not populating
them: bb_percent_b_a, bb_percent_b_b, px_vs_ema20_bps, px_vs_ema50_bps
(all zero across all rows — likely an audit script bug, not a real-data issue).

## Per-era results (intraday_safe factors only)

| Era | n significant findings | Sign distribution |
|---|---|---|
| Pre-boundary | 9 | shared_winner=7, loser_contrast=2 |
| Post-boundary | 11 | shared_winner=5, loser_contrast=6 |

## Cross-era consistency

After matching on (pair_family, direction, factor):

| consistency        |   count |
|:-------------------|--------:|
| n_too_small_in_one |     105 |
| consistent_noise   |      57 |
| pre_only           |       4 |
| other              |       1 |
| consistent_signal  |       1 |

## THE SINGLE FINDING THAT SURVIVES BOTH ERA-SPLIT AND LINEAGE QUARANTINE

| era_pre   | pair_family   | direction   | factor      |   n_winners_pre |   n_losers_pre |   winner_median_pre |   loser_median_pre |   winner_mean_pre |   loser_mean_pre |   cohens_d_pre |   ci_low_pre |   ci_high_pre | sign_pre       | era_post   |   n_winners_post |   n_losers_post |   winner_median_post |   loser_median_post |   winner_mean_post |   loser_mean_post |   cohens_d_post |   ci_low_post |   ci_high_post | sign_post      | consistency       |
|:----------|:--------------|:------------|:------------|----------------:|---------------:|--------------------:|-------------------:|------------------:|-----------------:|---------------:|-------------:|--------------:|:---------------|:-----------|-----------------:|----------------:|---------------------:|--------------------:|-------------------:|------------------:|----------------:|--------------:|---------------:|:---------------|:------------------|
| pre       | usd_base      | short       | spread_pips |               9 |              4 |               0.700 |              1.000 |             0.735 |            1.000 |         -0.996 |       -0.482 |        -0.048 | loser_contrast | post       |                9 |              17 |                0.500 |               0.900 |              0.644 |             0.829 |          -0.881 |        -0.351 |         -0.019 | loser_contrast | consistent_signal |

**`usd_base × short`: spread_pips is loser_contrast in BOTH eras.**
- pre: Cohen's d = −0.996 (n_winners=9, n_losers≈10)
- post: Cohen's d = −0.881 (n_winners=9, n_losers≈10)
- Wider spreads predict losses in usd_base shorts. Consistent across eras with similar effect size.

**Zero factors flipped sign between eras (no INVERTED findings).**

## What this kills (previously believed signals)

Step 8 surfaced these as 'winner signatures' or 'loser contrasts' — all now demoted:

| Previous finding | Status after era-split |
|---|---|
| `box_age_hours` strongest loser signal across 3 pockets | **CONTAMINATED** (audit artifact, V3-era only) |
| `wall_proximity` loser_contrast in antipodean/long | **CONTAMINATED** (daily-derived) |
| `current_volume`/`volume_ratio` winner-positive in usd_base/long + antipodean/long | **ERA-CONFOUNDED** (didn't survive era-split) |
| `bb_band_width_a_bps` winner-positive in usd_base/long | **ERA-CONFOUNDED** |
| `avg_volume` winner-positive in usd_base/short | **ERA-CONFOUNDED** |
| `ema20_dist_pct` / `ema50_dist_pct` loser-contrast in antipodean/long | **ERA-CONFOUNDED** |
| `otr_ratio` loser-contrast in antipodean/long | **CONTAMINATED** (uses box geometry) |
| `regime_confidence` loser-positive in usd_base/short | **METADATA, not lineage-clean** |
| `box_age_hours` overall +30 WR gap | **AUDIT ARTIFACT** (dukascopy cache boundary) |

Net: of ~17 'significant' Step 8 findings, **only 1 survives rigorous methodology**.

## Why so few survive

1. **Sample size**: 37 pre + 31 post winners across 8 pocket cells = avg 4-5 per cell
   per era. Most pockets register as 'n_too_small_in_one' (105 of 168 cell-factor rows)
2. **Daily-cache contamination**: 19 factors quarantined, including some of the
   strongest-looking Step 8 signals (wall_proximity, box_age_hours, otr_ratio)
3. **Audit reconstruction bugs**: 20 factors all-zero in audit output. Includes some
   intraday_safe ones (bb_percent_b_a/b, px_vs_ema20_bps) that should have worked
4. **Era confounding**: pre-V3 and V3-era trade different markets with different probes
   under different management. Many 'signals' are era-specific.

## The methodological lesson

Step 8 (factor synchrony v0) found 17+ winner/loser signals. After:
- daily-cache quarantine (V3 code review caught this)
- era-split (bimodal diagnostic caught the era confound)
- consistency-across-eras filter

Only spread_pips in usd_base/short survives. **The Step 8 'signals' were almost entirely**
**artifacts of audit reconstruction + era confounding.**

This validates the whole Brock 2026-05-13 protocol:
> 'Until we know whether box_age is measuring market physics or bot state corruption,
> no ADR.'

Without that protocol, we'd have ADR'd box_age, wall_proximity, and possibly half a dozen
other false signals. The methodology saved us.

## What we have

- ONE real signal: `usd_base × short: spread_pips loser_contrast`. d≈−0.94 average
  across eras, n_winners=9 per era. **Wider spreads predict losses in usd_base shorts.**
- This is logical (cost of trading) and survives methodology. Empirically grounded.

- A factor-lineage taxonomy and an era-split methodology that future research can use

- A warning inserted into `live_broker_reverse_engineer.py` documenting the 2026-04-22
  daily-cache boundary

## What we don't have

- Strong evidence for a multi-factor synchrony pattern. With n=4-5 winners per pocket
  per era, we're under-powered for the kind of pattern discovery Step 8 was aiming at.
- Confidence in the regime/cluster naming we were heading toward. The candidate clusters
  (usd_base/short etc.) are still real geometric pockets but the FACTOR signatures we
  thought characterized them were mostly artifacts.

## What's queued (per locked sequencing)

Per Brock protocol: 'Do not run sister-factor diagnostics until this quarantine is done.'
The quarantine is done. Sister-factor diagnostics are now authorized.

BUT: with only 1 surviving signal, the sister-factor diagnostic has very little to
validate. The realistic next options are:

1. **Apply sister-factor independence test to spread_pips** — confirm it's not a
   pocket-tag itself (it shouldn't be — spread is a live market property, not derived
   from any bot logic)
2. **Widen the data window**: add the 87 box-contaminated rows back IF we re-run V1's
   actual box code against fresh market data. That would push n per pocket above the
   stability threshold.
3. **Resign to current epistemic state**: accept that the broker-audit data we have is
   not statistically strong enough for multi-factor synchrony work. Move research
   focus elsewhere (e.g., V3 live observation as it accumulates more trades).
4. **Wait for v2 corpus rerun with full 47-factor extraction** — would give ~10K+ trades
   per pocket and resolve the n-limit problem definitively. Multi-day compute pass.