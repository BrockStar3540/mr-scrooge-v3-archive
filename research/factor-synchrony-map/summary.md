# Raw Factor Synchrony Map v0

Generated: 2026-05-13T03:02:04.482615+00:00

## Per locked direction 2026-05-13: synchrony, not scoring

Question per pocket: **In this pair_family × direction (× session) pocket, what
raw factor states did verified winners share, and which did losers lack?**

NOT a score. NOT a 'this factor is good' claim. Each finding is locally conditional.

## Inputs (honest pool)

**Winners (broker-only, 68 rows):**
- 64 bot_actual_winner rows from live broker truth
- 4 step7 promoted (1 confirmed direction_repair, 3 partial)
- Manual rows (46) excluded — lack the 79-factor data, only have 3 factors

**Losers (broker non-contaminated, 91 rows):**
- All bot_actual_loser rows where repair_taxonomy != correct_box_replay_required
- Excludes 87 box-bug contaminated rows (pending Step 5 correct-box replay)

**Factors analyzed:** 26 priority raw factors (BB position, wall_proximity,
EMA distances, ATR/OTR/ADR consumed, RSI, z-score, spread, rr_ratio, volume,
box_age_hours, regime_confidence as metadata, etc.)

## Grain levels

**Coarse (pair_family × direction):** 8 pockets, 208 rows. Most robust given n.
**Mid (+ session_bucket):** 29 pockets, 754 rows. Mostly unstable at n<3 per cell.

## Coarse-grain sign distribution

| sign                    |   count |
|:------------------------|--------:|
| neutral                 |     150 |
| ambiguous               |      41 |
| loser_contrast          |      10 |
| shared_winner_condition |       7 |

- 7 shared_winner_condition findings (factor higher in winners, CI excludes 0)
- 10 loser_contrast findings (factor higher in losers)
- 150 neutral
- 41 ambiguous (n<3 one side or no variance)

## Cross-pocket consensus per factor

| consensus                |   count |
|:-------------------------|--------:|
| neutral_or_unstable_only |      13 |
| loser_contrast_universal |       7 |
| shared_winner_universal  |       6 |

**Zero factors INVERT across coarse pockets.** At this grain, factors that matter
matter consistently in the same direction. (This differs from the live-epoch atlas,
which had strategy + finer cells adding noise.)

## Strongest pockets (best sample size)

- **usd_base × short**: 18 winners, 21 losers (most robust)
- **usd_base × long**: 10 winners, 12 losers
- **antipodean_cross × long**: 6 winners, 15 losers
- Others: thinner (3-6 winners per side)

## SHARED WINNER CONDITIONS (what winners had that losers didn't)

- **usd_base × long** — winners had **MORE bb_band_width_a_bps** 
  (winner median 17.747 vs loser 9.269, d=+1.29, n_w=10, n_l=12)
- **antipodean_cross × long** — winners had **MORE current_volume** 
  (winner median 9376.500 vs loser 5626.000, d=+1.28, n_w=6, n_l=15)
- **usd_base × long** — winners had **MORE current_volume** 
  (winner median 13156.000 vs loser 7791.000, d=+1.13, n_w=10, n_l=12)
- **eur_cross × short** — winners had **MORE atr** 
  (winner median 0.852 vs loser 0.008, d=+1.10, n_w=6, n_l=9)
- **usd_base × long** — winners had **MORE bb_band_width_b_bps** 
  (winner median 17.266 vs loser 11.643, d=+1.02, n_w=10, n_l=12)
- **usd_base × long** — winners had **MORE volume_ratio** 
  (winner median 1.002 vs loser 0.681, d=+1.00, n_w=10, n_l=12)
- **usd_base × short** — winners had **MORE avg_volume** 
  (winner median 11095.600 vs loser 9125.250, d=+0.83, n_w=18, n_l=21)

**Patterns visible:**
- `current_volume` and `volume_ratio` are winner-shared in usd_base/long AND antipodean/long → real volume matters for longs
- `bb_band_width_a_bps` and `bb_band_width_b_bps` are winner-shared in usd_base/long → winners entered during higher volatility
- `avg_volume` higher in usd_base/short winners → activity matters
- (`atr` finding in eur_cross/short flagged as data-suspect: winner_median 0.85 vs loser 0.008 — magnitude difference suggests unit mixup or measurement artifact)

## LOSER CONTRAST (what losers had that winners didn't)

- **eur_cross × long** — losers had **MORE box_age_hours** 
  (loser median 348.060 vs winner 25.795, d=-1.41, n_w=6, n_l=5)
- **antipodean_cross × long** — losers had **MORE ema50_dist_pct** 
  (loser median 63.830 vs winner 23.950, d=-1.13, n_w=6, n_l=15)
- **gbp_cross × short** — losers had **MORE box_age_hours** 
  (loser median 373.940 vs winner 124.590, d=-1.10, n_w=4, n_l=7)
- **eur_cross × short** — losers had **MORE spread_pips** 
  (loser median 1.000 vs winner 0.700, d=-1.09, n_w=6, n_l=9)
- **antipodean_cross × long** — losers had **MORE box_age_hours** 
  (loser median 344.850 vs winner 105.910, d=-1.07, n_w=6, n_l=15)
- **antipodean_cross × long** — losers had **MORE otr_ratio** 
  (loser median 0.110 vs winner 0.058, d=-0.83, n_w=6, n_l=15)
- **usd_base × short** — losers had **MORE regime_confidence** 
  (loser median 2.000 vs winner 0.000, d=-0.82, n_w=18, n_l=21)
- **antipodean_cross × long** — losers had **MORE ema20_dist_pct** 
  (loser median 38.620 vs winner 20.465, d=-0.80, n_w=6, n_l=15)
- **antipodean_cross × long** — losers had **MORE wall_proximity** 
  (loser median 0.335 vs winner 0.058, d=-0.79, n_w=6, n_l=15)
- **usd_base × short** — losers had **MORE spread_pips** 
  (loser median 0.900 vs winner 0.600, d=-0.75, n_w=18, n_l=21)

**Patterns visible:**
- **`box_age_hours` is the strongest loser signal** — appears in antipodean/long (d=-1.07), gbp_cross/short (d=-1.10), eur_cross/long (d=-1.41). Winners enter on FRESH boxes (25-125h), losers on STALE boxes (344-373h). Three pockets, consistent direction.
- `spread_pips` is loser-shared in usd_base/short (d=-0.75) and eur_cross/short (d=-1.09). Wider spreads → losses. Expected, but quantified.
- `wall_proximity` is loser-shared in antipodean/long (d=-0.79). Winners entered closer to wall (~0.06), losers entered further (~0.34).
- `ema20_dist_pct` + `ema50_dist_pct` are loser-shared in antipodean/long. Winners entered with smaller EMA distance, losers with bigger.
- **`regime_confidence` is loser-shared in usd_base/short (d=-0.82)** — HIGH regime_confidence trades LOSE in this pocket. Same counter-intuitive pattern as the older atlas surfaced.
- `otr_ratio` is loser-shared in antipodean/long.

## Cross-pocket inversion: ZERO

At coarse grain (pair_family × direction), no factor flips sign across pockets.
Each non-neutral factor stays directionally consistent. **This is a finding:** when
you condition on pair_family + direction, the factor physics is more stable than at
the previous strategy-level grain (where 19-29 factors inverted in the live-epoch atlas).

## What the synchrony map suggests (NOT yet validated)

For the strongest cell (usd_base × short, n_w=18 n_l=21):
- Winning signature: tight spread + low regime_confidence + higher avg_volume
- Losing signature: wide spread + high regime_confidence + lower avg_volume

For antipodean × long (n_w=6 n_l=15):
- Winning signature: closer to wall + smaller EMA distances + younger box + lower OTR + higher current_volume
- Losing signature: further from wall + larger EMA distances + older box + higher OTR

**These are hypotheses ready for forward testing**, not deployable rules.

## Sample-size caveats (loud)

- Best pocket has 18 winners. Most have 3-6. Statistical power is weak.
- 'shared_winner_condition' at n_w=6 means Cohen's d CI excluded 0 — but the effect
  size estimate is itself noisy at small n.
- Mid-grain (+ session) has 572 of 754 rows as 'unstable' (n<3). Not usable yet.
- Cannot extend to fine grain (+ session_quarter + strategy) until winner pool is
  significantly larger (likely requires V1-code box replay to add the 87 contaminated rows back).

## What this DOES NOT say

- 'volume is good' or 'box_age is bad' globally. **All findings are pocket-conditional.**
- Any single factor wins or loses absolutely. The map says: IN THIS POCKET, this factor
  state was associated with winning/losing. Different pocket may have different pattern.
- These should become rules. Rules need bigger n and out-of-sample validation.

## What comes next (per direction)

1. **Step 8 candidate regime naming** — Brock's call. The synchrony patterns suggest
   candidate names like 'usd_base short with tight spread + low regime_confidence'.
   Not yet named.
2. **Step 9 validation** — once regimes are named, test on holdout (post-Apr-13 V3 era)
3. **V1-code box replay** for the 87 contaminated rows would significantly widen the
   winner+loser pool (more like 145+90 rows) and make mid-grain stable.