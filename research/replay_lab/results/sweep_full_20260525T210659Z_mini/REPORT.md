# Replay Lab — Universal Sweep Report

**Run:** 2026-05-25 21:06 UTC
**Hardware:** Mac Mini M-series (10 cores, 16 GB RAM), 8 worker processes
**Runtime:** **10.7 minutes for 108 backtests** (~6 sec/cell, 80× faster than EC2)

## Scope

- **27 pairs** (full live universe)
- **2 strategy families:** canonical_lien_dbb (DBB), box_master_theory (MTB)
- **2 direction modes:** native, reversed
- **Held constant:** entry=signal, management=tp1_only, routing=exact_plus_family,
  window=2026-04-25 → 2026-05-25 (30 days)

= **108 backtests, all completed, 0 errors.**

## Top-line aggregate

| family | direction | pairs | trades | avg WR | avg return | avg expectancy |
|---|---|---:|---:|---:|---:|---:|
| **canonical_lien_dbb** | **native** | 27 | 1871 | 64.9% | **−0.1%** | +0.025% |
| canonical_lien_dbb | reversed | 27 | 1958 | 62.5% | −4.0% | +0.021% |
| **box_master_theory** | **reversed** | 27 | 741 | 60.5% | **−1.6%** | +0.019% |
| box_master_theory | native | 27 | 745 | 62.4% | −4.3% | +0.019% |

**Headline finding: the two families have MIRROR-OPPOSITE direction preferences.**
- canonical_lien_dbb: native wins by ~4% absolute return
- box_master_theory: reversed wins by ~3% absolute return

A global "reverse all directions" flag would help MTB and hurt DBB by
roughly equal amounts. **The earlier "bot is trading backwards" intuition
applies only to MTB pitchforks, not to DBB zone-touches.**

## Top 10 winning cells (positive return)

| pair | family | direction | trades | WR | return |
|---|---|---|---:|---:|---:|
| NZD_JPY | DBB | reversed | 126 | 69.8% | **+63.6%** |
| NZD_JPY | MTB | native | 41 | 73.2% | **+50.6%** |
| GBP_AUD | DBB | native | 42 | 78.6% | **+38.3%** |
| EUR_USD | DBB | native | 75 | 68.0% | **+36.0%** |
| EUR_CHF | MTB | reversed | 34 | 76.5% | **+35.6%** |
| AUD_CAD | MTB | native | 34 | 76.5% | **+32.7%** |
| AUD_CAD | DBB | reversed | 55 | 72.7% | **+32.6%** |
| GBP_USD | DBB | native | 55 | 67.3% | **+28.7%** |
| GBP_AUD | MTB | native | 89 | 69.7% | **+28.3%** |
| AUD_CHF | MTB | reversed | 51 | 70.6% | **+26.8%** |

## Bottom 5 (worst losses, configs to NEVER run)

| pair | family | direction | trades | WR | return |
|---|---|---|---:|---:|---:|
| AUD_JPY | DBB | reversed | 189 | 57.1% | −60.2% |
| NZD_USD | DBB | reversed | 81 | 60.5% | −43.6% |
| NZD_JPY | MTB | reversed | 36 | 55.6% | −42.4% |
| USD_JPY | DBB | native | 204 | 60.8% | −37.4% |
| EUR_USD | MTB | native | 49 | 53.1% | −34.1% |

## Per-pair best config (22 pairs with trades, 1 row per pair)

| pair | best family | best direction | return |
|---|---|---|---:|
| NZD_JPY | DBB | reversed | +63.6% |
| GBP_AUD | DBB | native | +38.3% |
| EUR_USD | DBB | native | +36.0% |
| EUR_CHF | MTB | reversed | +35.6% |
| AUD_CAD | MTB | native | +32.7% |
| GBP_USD | DBB | native | +28.7% |
| AUD_CHF | MTB | reversed | +26.8% |
| AUD_JPY | DBB | native | +26.1% |
| EUR_JPY | MTB | native | +25.4% |
| AUD_USD | DBB | native | +23.0% |
| NZD_USD | DBB | native | +17.5% |
| EUR_GBP | DBB | native | +15.7% |
| CAD_JPY | MTB | reversed | +13.5% |
| AUD_NZD | MTB | reversed | +10.0% |
| USD_CAD | DBB | native | +7.5% |
| USD_JPY | MTB | reversed | +5.9% |
| EUR_CAD | MTB | reversed | +5.5% |
| CHF_JPY | DBB | reversed | +5.2% |
| EUR_AUD | DBB | reversed | +4.5% |
| GBP_CHF | MTB | native | +2.2% |
| USD_CHF | MTB | reversed | +0.0% |
| GBP_JPY | DBB | reversed | **−7.8%** ← only pair with no positive config |

## Silent pairs (0 trades on any config)
`EUR_NZD, GBP_CAD, GBP_NZD, NZD_CAD, NZD_CHF` — 5 pairs where neither DBB
nor MTB emitted any signals in the 30-day window. Likely combination of
low volatility on minor crosses + routing-table coverage gaps.

## Per-family direction-preference pattern

**DBB prefers NATIVE on:** GBP_AUD, EUR_USD, GBP_USD, AUD_JPY, AUD_USD,
NZD_USD, EUR_GBP, USD_CAD, EUR_CHF (USD-base + AUD-base mostly)

**DBB prefers REVERSED on:** NZD_JPY, AUD_CAD, CHF_JPY, EUR_AUD, GBP_JPY
(several JPY crosses)

**MTB prefers NATIVE on:** NZD_JPY, AUD_CAD, EUR_JPY, GBP_AUD, GBP_CHF

**MTB prefers REVERSED on:** EUR_CHF, AUD_CHF, CAD_JPY, AUD_NZD, USD_JPY,
EUR_CAD, USD_CHF (many CHF crosses + select JPY crosses)

There's NOT a single clean pattern. Each (pair, family) is its own cell
with its own direction preference. **Configuring direction per-(pair,family)
not globally is the actionable signal.**

## Implications

1. **NO single-flag fix works.** Reverse-all helps half the cells and
   hurts the other half. A "directional override map" indexed by
   (pair, family) would.
2. **Top cells are dramatically positive.** NZD_JPY DBB reversed +63.6%
   in 30 days. These are real candidate cells for the routing slate.
3. **Bottom cells are dramatically negative.** AUD_JPY DBB reversed −60%
   in 30 days. These should be EXPLICITLY EXCLUDED from the slate.
4. **22 of 27 pairs have at least one positive config.** Only GBP_JPY
   has all four negative — drop it from the slate entirely?
5. **DBB fires ~2.5× more often than MTB.** DBB is the dominant signal
   producer; tuning DBB cells will have ~2.5× the throughput impact of
   tuning MTB cells.

## Methodology caveats

- 30-day window only. May not be regime-representative — re-run on
  a 180-day window to validate.
- Routing mode `exact_plus_family` is the loosest "live-realistic"
  option. `exact_strategy_only` is the live default; results may
  differ.
- Entry=signal, management=tp1_only held constant. The earlier 1-pair
  experiment showed pullback_2 + tp1_only outperformed signal + tp1_be
  by margin on USD_JPY DBB; full sweep should re-validate that on the
  same 27-pair universe.
- canonical_darvas + textbook_scalper (probes) NOT included in this
  sweep. Probes especially are slow per-bar (22 sub-iterations). Worth
  a separate sweep if they matter.

## What ought to come next

1. **Tighter sweep:** re-run with both `entry_mode` × `management_mode`
   to identify the best (pair, family, direction, entry, management)
   per cell. 27 × 2 × 2 × 4 × 4 = 1728 backtests — should be ~2.5 hr on Mini.
2. **180-day sweep** on the same dimensions to test 30-day stability.
3. **Cell-level slate audit:** cross-reference current v1.13_mirror
   slate against this sweep's top-25 cells. How many are already
   promoted? How many promoted cells are in the bottom-15?
4. **Directional override config:** prototype a (pair, family) →
   direction map in the live bot, gate by config flag.
