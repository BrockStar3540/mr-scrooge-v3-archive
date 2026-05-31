# Backtest Results

Headline lab numbers for every strategy in the V4 roster. This is the
**entry point to the 3-document evaluation workflow:**

```
1. BACKTEST_RESULTS.md            (you are here)
   ↓ "this strategy looks interesting"
2. STRATEGY_ENCYCLOPEDIA.md       (per-strategy formula)
   ↓ "I want to run my own test"
3. LAB_REPRODUCTION_GUIDE.md      (step-by-step harness)
```

All numbers below come from the 6-month Phase 3 lab sweep (Nov 25,
2025 → May 25, 2026) on 27 OANDA forex pairs unless explicitly noted
as matrix-mined. **Lab numbers are not a forecast.** See
[`RESEARCH_METHODOLOGY.md#known-limitations`](RESEARCH_METHODOLOGY.md#known-limitations)
for the honest caveats — regime-dependence, compound-sizing inflation,
no walk-forward validation, no slippage modeling.

---

## How to read this doc

Each strategy gets one row in the master table with:

- **n_trades** — lab firings (sum across pairs × directions where applicable)
- **WR** — corpus win rate
- **PnL** — lab dollar accumulation from $50k seed equity under compound sizing
- **Pairs+** — pairs with positive PnL (of 27)
- **Direction edge** — `native`, `reversed`, or `symmetric` based on which side won
- **Status** — live/sidelined/conditional + any flags

Flags worth knowing:
- 🟢 **promotable** — clean Phase 3 winner, ready for routing-table inclusion via Task #41
- 🚨 **outlier — needs forensic** — compound-growth signature (>$100M PnL)
- ⚠️ **wrong-direction** — Phase 3 shows reversed side wins; trade in regime-aligned direction
- 🔴 **drop candidate** — net-negative or near-zero edge
- 🔵 **data-thin** — insufficient corpus data to evaluate confidently
- ⚫ **never fires** — probe code may be broken

---

## Master summary

### V3 family + promoted (matrix-mined, 6mo corpus)

| Strategy | Family | n (matrix) | WR (matrix) | Exp pips | Pairs | Direction | Status |
|---|---|---|---|---|---|---|---|
| `box_master_theory` | box | 13,558 | 81% | 6.5 | 27/27 | symmetric | LIVE — V1 origin, equal footing now |
| `dbb_trend` | continuation | 6,925 | 77% | 6.0 | 27/27 | symmetric | LIVE — V3 workhorse |
| `direct` | direct | 11,933 | 82% | 7.0 | 27/27 | symmetric | LIVE (fallback) — highest matrix WR |
| `reversal` | reversion | n/a | n/a | n/a | **0/27** | — | LIVE 🔵 coverage gap (not in matrix) |
| `canonical_lien_dbb` | continuation | 8,374 | 78% | 5.9 | 25/27 | symmetric | LIVE |
| `canonical_darvas` | box | n/a | n/a | n/a | **0/27** | — | conditional 🔵 coverage gap |
| `chaikin_macd_atr` | continuation | 10,888 | 81% | 6.5 | 27/27 | symmetric | LIVE (promoted 2026-05-27) |
| `compression_expansion` | breakout | 10,040 | 80% | 6.2 | 27/27 | symmetric | LIVE (promoted 2026-05-27) |
| `trend_pullback` | continuation | 10,414 | 81% | 6.3 | 27/27 | symmetric | LIVE (promoted 2026-05-27) |
| `ifvg` | other | 11,674 | 81% | 6.6 | 27/27 | symmetric | LIVE (promoted 2026-05-27) |
| `session_breakout` | breakout | 1,556 | 80% | 6.0 | **8/27** | long-edge | LIVE (narrow coverage) |
| `trend` | continuation | 10,582 | 80% | 6.3 | 27/27 | symmetric | sidelined (legacy) |
| `trend_aligned_breakout` | breakout | 2,802 | 72% | 5.9 | 20/27 | 60S/30L cells | conditional |
| `compression_reversion` | reversion | 1,354 (long only) | n/a | n/a | partial | — | LIVE 🔵 data-thin |

### probes_v2 family (Phase 3 lab — none in matrix yet)

10 NATO-phonetic probes from `probes_v2.py`, all default DISABLED.
Entered the lab corpus only via Phase 3 sweep.

| Probe | Family routing | n | WR | PnL | Pairs+ | Direction | Status |
|---|---|---|---|---|---|---|---|
| `alpha_pullback_v2` | dbb_trend | 134,836 | 61% | +$34.8M | 20/27 | ⚠️ reversed | sidelined |
| `alpha_breakout_retest_v2` | direct | 145,998 | 61% | +$60.6M | 17/27 | ⚠️ reversed | sidelined |
| `alpha_extended_fade_v2` | reversal | 44,685 | 61% | **+$584M** | 27/27 | ⚠️ reversed | 🚨 outlier — needs forensic |
| `bravo_failed_momentum` | reversal | 81,918 | 62% | **−$1.1M** | **4/27** | native | 🔴 drop candidate |
| `bravo_expansion_continuation` | dbb_trend | 136,155 | 61% | +$61.6M | 17/27 | ⚠️ reversed | sidelined |
| `charlie_pullback_continuation_v2` | dbb_trend | 86,462 | 62% | **+$297.7M** | 26/27 | ⚠️ reversed | 🚨 outlier — needs forensic |
| `charlie_compression_breakout` | direct | 62,464 | 63% | +$1.7M | 10/27 | ⚠️ reversed | sidelined (narrow) |
| `delta_tag_and_go_v2` | direct | 85,956 | 62% | +$2.0M | 12/27 | ⚠️ reversed | sidelined (narrow) |
| `echo_box_fade_v2` | reversal | 69,346 | 62% | +$0.7M | 13/27 | native | sidelined (rare exception — native preferred) |
| `echo_failed_breakout_v2` | reversal | — | — | — | — | — | pending (Phase 3 variant 34/34) |

### textbook_scalper family (Phase 3 lab — none in matrix yet)

22 variants from `textbook_scalper.py` (TF/BR/CP/MR/RG families). All
default DISABLED. Entered the lab corpus only via Phase 3 sweep.

| Variant | Family routing | n | WR | PnL | Pairs+ | Direction | Status |
|---|---|---|---|---|---|---|---|
| `TF2_pullback_EMA20_long` | direct | 80,061 | 61% | **+$126M** | 27/27 | ⚠️ reversed | 🚨 outlier — forensic done (real compound growth) |
| `TF2_pullback_EMA20_short` | direct | 80,668 | 61% | — | 27/27 | mirror | sidelined |
| `TF4_sar_long` | direct | — | — | — | — | — | sidelined |
| `BR2_vcb_long` | direct | 59,306 | 62% | +$1.6M | 14/27 | symmetric | 🟢 sidelined → strong promote candidate |
| `BR2_vcb_short` | direct | 57,622 | 61% | **+$4.9M** | 19/27 | symmetric | 🟢 strong promote candidate |
| `BR3_inside_bar_long` | direct | 23,695 | 63% | +$115k | 9/27 | weak | sidelined |
| `BR3_inside_bar_short` | direct | 22,076 | 62% | **−$37k** | 6/27 | LOSER | 🔴 only consistent loser — DROP |
| `BR5_opening_range_breakout_long` | direct | 53,527 | 62% | +$2.3M | 12/27 | symmetric | sidelined |
| `BR5_opening_range_breakout_short` | direct | 51,733 | 61% | **+$4.5M** | 18/27 | symmetric | 🟢 strong promote candidate |
| `CP1_coil_breakout_long` | direct | 54,298 | 62% | **+$7.3M** | 18/27 | symmetric | 🟢 top winner |
| `CP1_coil_breakout_short` | direct | 53,393 | 61% | +$2.0M | 18/27 | symmetric | sidelined |
| `CP2_squeeze_momentum_long` | direct | 36,428 | 62% | **+$3.8M** | 16/27 | (no short) | 🟢 strong promote candidate |
| `CP3_vol_coil_fade_long` | reversal | 7,742 | 61% | +$380k | 20/27 | ⚠️ reversed | sidelined |
| `CP3_vol_coil_fade_short` | reversal | 8,799 | 62% | +$814k | 20/27 | ⚠️ reversed | sidelined |
| `MR2_bb_reversion_short` | reversal | 26,121 | 62% | **+$4.0M** | 24/27 | ⚠️ reversed | sidelined |
| `MR4_zscore_extreme_long` | reversal | 4,150 | 62% | +$25k | 15/27 | ⚠️ reversed (weakest case) | sidelined |
| `MR4_zscore_extreme_short` | reversal | 4,570 | 62% | +$100k | 16/27 | ⚠️ reversed (weakest case) | sidelined |
| `MR5_williams_extreme_long` | reversal | 2,875 | 59% | +$420k | 18/27 | ⚠️ reversed + temporally narrow | sidelined (risky) |
| `MR5_williams_extreme_short` | reversal | 2,686 | 62% | +$561k | 22/27 | ⚠️ reversed + temporally narrow | sidelined (risky) |
| `RG1_range_bound_scalp_long` | reversal | 17,909 | 61% | +$2.3M | 23/27 | ⚠️ reversed | sidelined |
| `RG1_range_bound_scalp_short` | reversal | 19,346 | 62% | **+$3.2M** | 25/27 | ⚠️ reversed | sidelined |
| `RG2_range_support_bounce_long` | reversal | **0** | n/a | n/a | 0/27 | — | ⚫ never fires (possibly broken) |

---

## Notable findings — start here if you want the headlines

### 🟢 Strong promote candidates (continuation/breakout, symmetric)

Five textbook_scalper variants stand out as clean direction-aligned
winners with broad pair coverage. None require any direction flip — they
won in their coded direction. These are the first-round Task #41
promotion candidates:

| Variant | PnL | Pairs+ | Why |
|---|---|---|---|
| `CP1_coil_breakout_long` | **+$7.3M** | 18/27 | Top winner. Coil + breakout + bull bar formula validated. |
| `BR2_vcb_short` | +$4.9M | 19/27 | VCB + RSI 22-50 + close < 5-bar low + bearish bar. |
| `BR5_opening_range_breakout_short` | +$4.5M | 18/27 | 20-bar low break + bearish bar + RSI < 50. |
| `CP2_squeeze_momentum_long` | +$3.8M | 16/27 | Squeeze + ADX + 3-bar expanding closes. Long-only by design. |
| `BR2_vcb_long` | +$1.6M | 14/27 | Mirror of BR2_short. Solid but less robust. |

### ⚠️ Wrong-direction probes (run reversed = trade with regime trend)

Eleven probes showed reversed direction winning more than native — the
Phase 3 wrong-direction finding, validated across 21-27/27 pairs and
26/26 weeks. The actionable read is **not** "flip these probes" but
"trade in the direction of the regime trend" (the HTF gate already does
this at the system level since 2026-05-27).

| Probe | Reversed PnL | Pairs preferring reversed |
|---|---|---|
| `RG1_range_bound_scalp` | +$7.6M | 27/27 |
| `MR2_bb_reversion` (short) | +$5.1M | 27/27 |
| `MR5_williams_extreme` | +$2.0M | 27/27 |
| `CP3_vol_coil_fade` | +$2.6M | 26/27 |
| `MR4_zscore_extreme` | +$1.0M | 23/27 |
| `alpha_pullback_v2` | $34.8M | 20/27 |
| `alpha_breakout_retest_v2` | $60.6M | 17/27 |
| `bravo_expansion_continuation` | $61.6M | 17/27 |
| `charlie_compression_breakout` | $1.7M | 10/27 |
| `delta_tag_and_go_v2` | $2.0M | 12/27 |
| `TF2_pullback_EMA20_long` | +$127M | 27/27 |

### 🚨 Compound-growth outliers (forensic before promotion)

Three variants surfaced PnL in the $100M+ range — almost certainly real
edge × compound growth on $50k seed equity, not artifact. TF2 was
forensically verified 2026-05-30 (200 EMA filter test, cross-calibrated
against TraderDale + TradePro external sources). The other two need the
same forensic before any promotion:

| Variant | n | PnL | Verified? |
|---|---|---|---|
| `TF2_pullback_EMA20_long` | 80k | +$126M | ✓ verified — real compound growth at 70% WR reversed |
| `charlie_pullback_continuation_v2` | 86k | **+$297M** | ⏳ pending forensic |
| `alpha_extended_fade_v2` | 45k | **+$584M** | ⏳ pending forensic |

Forensic procedure for both: add the 200 EMA filter to a re-run on 3
sample pairs, check whether WR moves up (real edge) or down (methodology
inflation). Compare against external calibration sources for similar
strategy archetypes.

### 🔴 Drop candidates (net-negative or broken)

| Variant | n | PnL / status | Why drop |
|---|---|---|---|
| `BR3_inside_bar_short` | 22k | −$37k | Only consistently net-negative variant; 6/27 pair coverage |
| `bravo_failed_momentum` | 82k | **−$1.1M** | 4/27 pair coverage — works in <15% of universe |
| `RG2_range_support_bounce_long` | **0** | never fires | Probe may be broken (conditions never aligned across 6mo) |

### 🔵 Coverage gaps (V3-registered, not in lab corpus)

| Strategy | Status | Gap fixed by |
|---|---|---|
| `reversal` | LIVE but no matrix data | Task #41 module rebuild |
| `canonical_darvas` | conditional, no matrix data | Task #41 module rebuild |
| `compression_reversion` | LIVE, partial data only | Task #41 module rebuild |

These three V3 strategies are admitted live but don't have lab-mined
rule coverage. The router falls back to either LightGBM-only gating
(`reversal`) or near-zero firing (`compression_reversion`). Task #41
brings them into the matrix.

---

## By-family deep dives

### Continuation family
**Phase 3 winners:** CP1 (long), CP2 (long), BR2 (long+short), BR5 (long+short)
**Matrix-validated:** dbb_trend, canonical_lien_dbb, chaikin_macd_atr, trend_pullback, trend, compression_expansion
**Direction-asymmetric (reversed wins):** alpha_pullback_v2, bravo_expansion_continuation, charlie_pullback_continuation_v2

The dominant story is that **direction-coded continuation probes (BR/CP)
win in their native direction**, while **probes_v2 continuation-flavored variants prefer reversed**. The
discrepancy maps to whether the probe code has its own implicit trend filter
(BR/CP all check RSI + breakout structure; probes_v2 alpha/charlie use simpler EMA20 proximity).

### Reversion family
**ALL wrong-direction in this corpus:** MR2, MR4, MR5, RG1, CP3, alpha_extended_fade_v2
**Exception:** echo_box_fade_v2 (native preferred)
**Drop candidate:** bravo_failed_momentum (only net-negative reversion variant)

The 6mo corpus regime structurally punished mean-reversion plays at
extremes — every reversion-flavored probe except echo_box_fade_v2 wins
reversed. The bot's `reversal` and `compression_reversion` live strategies
fall in this family but had near-zero live volume in the 27d post-promotion
broker truth (so the live evidence is inconclusive yet).

### Breakout family
**Promote candidates:** BR2, BR5, CP1, CP2 (all long+short or single-direction winners)
**Matrix data:** session_breakout (8/27), compression_expansion (27/27), trend_aligned_breakout (20/27)
**Drop candidate:** BR3_inside_bar_short

Breakout family is the cleanest direction-aligned story in Phase 3 —
multiple variants won handsomely without needing inversion. CP1 + BR5 are
top-tier promote candidates.

### Box family
**V3 only:** box_master_theory (matrix-validated, 81% WR), canonical_darvas (coverage gap)
**No textbook/probes_v2 in this family** — box strategies are a smaller niche in V4.

### Other / fallback
**direct** is the matrix-mined fallback (82% WR aggregated). It's not a
strategy in the traditional sense — it admits any candidate whose bucket
signature lands in a high-WR matrix cell. Highest live volume per
broker-truth audit; net-negative live so far because the bearish-regime
LONG bias dragged it down.

---

## Caveats (the honest disclaimer)

Numbers in this doc come from a **6-month in-sample lab** with these
specific limitations (mirroring the
[`RESEARCH_METHODOLOGY.md` known-limitations section](RESEARCH_METHODOLOGY.md#known-limitations)):

1. **Regime-dependent.** Nov 2025 → May 2026 was bearish-friendly.
   Reversion-family findings are conditional on this regime.
2. **Compound sizing inflates dollar magnitudes.** A 70%-WR variant
   grows $50k → $8.6M over 6mo. The dollars are correct accounting,
   but reading them as per-pip edge is wrong. Use **WR + pair breadth**
   for cross-variant ranking.
3. **No walk-forward / temporal OOS validation.** All numbers are
   in-sample by construction. Promote any winner only after walk-forward
   confirms it generalizes — see Step 8 of `LAB_REPRODUCTION_GUIDE.md`.
4. **No realistic slippage.** Lab assumes fills at quoted prices. Live
   OANDA slippage is ~0.3 pips on majors, more on exotics. Live WR
   will be lower than lab by some friction.
5. **3 outliers ($100M+ PnL) need forensic before promotion.** TF2 was
   forensically verified; charlie_pullback_continuation_v2 and
   alpha_extended_fade_v2 are pending.
6. **textbook_scalper + probes_v2 are NOT in matrix yet** — they enter
   via Task #41 module rebuild. Until then, even promotable variants
   cannot be routed live.

---

## Cross-references

- **[`STRATEGY_ENCYCLOPEDIA.md`](STRATEGY_ENCYCLOPEDIA.md)** — per-strategy probe formula (the trigger conditions a strategy uses to fire)
- **[`LAB_REPRODUCTION_GUIDE.md`](LAB_REPRODUCTION_GUIDE.md)** — step-by-step harness for running your own backtest
- **[`RESEARCH_METHODOLOGY.md`](RESEARCH_METHODOLOGY.md)** — how the lab corpus + matrix + LightGBM were built
- **[`LIVE_SYSTEM_SPEC.md`](LIVE_SYSTEM_SPEC.md)** — what the production bot does today
- **[`decisions/`](decisions/)** — ADRs covering individual promotion + retirement decisions per strategy
- Raw lab data: `research/replay_lab/results/spec_sweep_phase3_*/per_variant_*.csv`


---

## Full-corpus aggregates (2026-05-31 sync, post Phase 3 wire-in)

These are the **raw 6-month trade_serials.csv aggregates** across all 27 pairs.
Different lens than the matrix-mined numbers above — matrix is the optimizer's
filtered subset; this is the unfiltered universe. **Both are valid; matrix is
cleaner signal, full-corpus is the population.**

### V3-family (legacy R00-R19 cohort)

| Strategy | Trades | Wins | Losses | WR | Sum pips | Exp pips | Pairs |
|---|---:|---:|---:|---:|---:|---:|---:|
| `box_master_theory` | 91,158 | 56,972 | 34,186 | 62.5% | 225,554 | +2.47 | 28 |
| `direct` | 85,334 | 52,896 | 32,438 | 62.0% | 207,945 | +2.44 | 28 |
| `ifvg` | 77,718 | 47,972 | 29,746 | 61.7% | 184,455 | +2.37 | 27 |
| `trend` | 54,844 | 34,211 | 20,633 | 62.4% | 131,993 | +2.41 | 27 |
| `trend_pullback` | 52,637 | 33,177 | 19,460 | 63.0% | 130,339 | +2.48 | 27 |
| `canonical_lien_dbb` | 50,964 | 31,564 | 19,400 | 61.9% | 124,168 | +2.44 | 27 |
| `chaikin_macd_atr` | 49,809 | 31,102 | 18,707 | 62.4% | 120,598 | +2.42 | 27 |
| `compression_expansion` | 49,181 | 30,974 | 18,207 | 63.0% | 120,481 | +2.45 | 27 |
| `dbb_trend` | 26,906 | 16,875 | 10,031 | 62.7% | 67,473 | +2.51 | 28 |
| `session_breakout` | 6,003 | 3,740 | 2,263 | 62.3% | 14,106 | +2.35 | 24 |
| `compression_reversion` | 1,858 | 1,139 | 719 | 61.3% | 4,155 | +2.24 | 16 |
| `reversal` | 331 | 206 | 125 | 62.2% | 691 | +2.09 | 25 |
| `canonical_darvas` | 113 | 80 | 33 | **70.8%** | 588 | **+5.21** | 12 |
| **V3-family TOTAL** | **838,182** | **519,128** | **319,054** | **~62%** | **1,532,546** | **+1.83 avg** | **28** |

### Phase 3 (probes_v2 + textbook_scalper, phase3 R20-R39 cohort)

Live since 2026-05-31. All 30 enabled in config + bootstrap registers them via PROBE_REGISTRY.

| Strategy | Trades | Wins | Losses | WR | Sum pips | Exp pips | Pairs |
|---|---:|---:|---:|---:|---:|---:|---:|
| `alpha_breakout_retest_v2` | 145,998 | 89,368 | 56,630 | 61.2% | 317,946 | +2.18 | 27 |
| `bravo_expansion_continuation` | 136,155 | 82,934 | 53,221 | 60.9% | 289,867 | +2.13 | 27 |
| `alpha_pullback_v2` | 134,836 | 82,588 | 52,248 | 61.3% | 292,609 | +2.17 | 27 |
| `charlie_pullback_continuation_v2` | 86,462 | 53,633 | 32,829 | 62.0% | 195,497 | +2.26 | 27 |
| `delta_tag_and_go_v2` | 85,956 | 53,240 | 32,716 | 61.9% | 193,520 | +2.25 | 27 |
| `bravo_failed_momentum` | 81,918 | 50,425 | 31,493 | 61.6% | 179,308 | +2.19 | 27 |
| `TF2_pullback_EMA20_short` | 80,668 | 49,502 | 31,166 | 61.4% | 177,600 | +2.20 | 27 |
| `TF2_pullback_EMA20_long` | 80,061 | 49,166 | 30,895 | 61.4% | 175,531 | +2.19 | 27 |
| `echo_box_fade_v2` | 69,346 | 43,065 | 26,281 | 62.1% | 157,796 | +2.28 | 27 |
| `charlie_compression_breakout` | 62,464 | 39,126 | 23,338 | 62.6% | 143,740 | +2.30 | 27 |
| `BR2_vcb_long` | 59,306 | 36,531 | 22,775 | 61.6% | 130,297 | +2.20 | 27 |
| `BR2_vcb_short` | 57,622 | 35,267 | 22,355 | 61.2% | 124,325 | +2.16 | 27 |
| `CP1_coil_breakout_long` | 54,298 | 33,549 | 20,749 | 61.8% | 121,417 | +2.24 | 27 |
| `BR5_opening_range_breakout_long` | 53,527 | 33,059 | 20,468 | 61.8% | 119,654 | +2.24 | 27 |
| `CP1_coil_breakout_short` | 53,393 | 32,679 | 20,714 | 61.2% | 115,071 | +2.16 | 27 |
| `BR5_opening_range_breakout_short` | 51,733 | 31,511 | 20,222 | 60.9% | 109,151 | +2.11 | 27 |
| `alpha_extended_fade_v2` | 44,685 | 27,316 | 17,369 | 61.1% | 96,571 | +2.16 | 27 |
| `TF4_sar_long` | 39,747 | 24,639 | 15,108 | 62.0% | 89,243 | +2.25 | 27 |
| `CP2_squeeze_momentum_long` | 36,428 | 22,585 | 13,843 | 62.0% | 81,877 | +2.25 | 27 |
| `MR2_bb_reversion_short` | 26,121 | 16,280 | 9,841 | 62.3% | 60,430 | +2.31 | 27 |
| `BR3_inside_bar_long` | 23,695 | 14,884 | 8,811 | **62.8%** | 54,806 | +2.31 | 27 |
| `BR3_inside_bar_short` | 22,076 | 13,756 | 8,320 | 62.3% | 49,892 | +2.26 | 27 |
| `RG1_range_bound_scalp_short` | 19,346 | 12,026 | 7,320 | 62.2% | 44,205 | +2.28 | 27 |
| `RG1_range_bound_scalp_long` | 17,909 | 10,998 | 6,911 | 61.4% | 39,003 | +2.18 | 27 |
| `CP3_vol_coil_fade_short` | 8,799 | 5,481 | 3,318 | 62.3% | 20,397 | **+2.32** | 27 |
| `CP3_vol_coil_fade_long` | 7,742 | 4,751 | 2,991 | 61.4% | 16,906 | +2.18 | 27 |
| `MR4_zscore_extreme_short` | 4,570 | 2,838 | 1,732 | 62.1% | 10,304 | +2.25 | 27 |
| `MR4_zscore_extreme_long` | 4,150 | 2,562 | 1,588 | 61.7% | 9,221 | +2.22 | 27 |
| `MR5_williams_extreme_long` | 2,875 | 1,690 | 1,185 | 58.8% | 5,281 | +1.84 | 27 |
| `MR5_williams_extreme_short` | 2,686 | 1,658 | 1,028 | 61.7% | 6,195 | +2.31 | 27 |
| **Phase 3 TOTAL** | **1,554,572** | **956,617** | **597,955** | **~61.5%** | **3,455,659** | **+2.22 avg** | **27** |

### Combined
| Cohort | Strategies | Trades | Blended WR | Regimes |
|---|---:|---:|---:|---|
| V3-family (legacy) | 13 active | 838,182 | ~62% | R00-R19 |
| Phase 3 | 30 active | 1,554,572 | ~61.5% | R20-R39 |
| **Combined** | **43 live** | **2,392,754** | **~62%** | **R00-R39 (40 regimes)** |

For per-regime breakdown per strategy: see
`research/per_pair_phase3/<PAIR>/manuals/master_rules.csv` (Phase 3) and
`research/per_pair/<PAIR>/manuals/master_rules.csv` (legacy).

---

## Appendix: Strategy lifecycle + historical artifacts

This section documents strategy IDs that appear in legacy lab data or
in PROBE_REGISTRY but **do not correspond to a current live strategy
with full lab backing**. Listed for forensic completeness.

### Lab-only meta-strategies (ghost names in legacy data)

These names appear in `research/per_pair/<PAIR>/trade_serials.csv` (legacy
modules built 2026-05-28) but have **zero references in current
`src/scrooge_v3/` code**. They were emitted by older lab wrappers that
have since been deleted. Their trade counts contributed to per-regime
aggregate WR in the legacy modules, but no live strategy can be matched
to a rule pinned to these strategy_ids.

| Name | Legacy lab N | Legacy WR | Verdict |
|---|---:|---:|---|
| `htf_all` | 107,412 | 61.9% | Ghost — older HTF-trend wrapper, code deleted. Likely replaced by `htf_trend_filter` gate (now MatrixRouter F40 universal pre-filter, ADR 3008). |
| `probes` | 99,764 | 61.7% | Lab wrapper alias for "run all probes_v2 NATO together." Live equivalent: the 10 individual probes_v2 NATO strategies (`alpha_*`, `bravo_*`, `charlie_*`, `delta_*`, `echo_*`) which ARE live with proper attribution. |
| `session_momentum_all` | 69,753 | 62.1% | Ghost — older session-momentum wrapper, code deleted. No live equivalent. |
| `trend_aligned_breakout` | 14,397 | 56.6% | Ghost — older variant, code deleted. Not in current registry. |

**Action**: No live code change needed. These rows in legacy
`trade_serials.csv` are historical exhaust; they boosted per-regime
sample counts but no rule pins to them as `strategy_id`. Leave as-is
for forensic continuity.

### PROBE_REGISTRY entries that are disabled or removed

| Probe | PROBE_REGISTRY status | Config status | Reason |
|---|---|---|---|
| `canonical_lien_dbb_long` | present in `canonical_lien_dbb.py` | disabled (no config entry) | Brock 2026-05-28: V3-family `canonical_lien_dbb` STRATEGY (50,964 lab trades) is the preferred entry. Probe variants kept registered but disabled — net edge was negative across 12 live trades. |
| `canonical_lien_dbb_short` | same | disabled | same |
| `echo_failed_breakout_v2` | **REMOVED 2026-05-31** from `probes_v2.py` PROBE_REGISTRY | n/a | 0 trades in Phase 3 lab corpus — formula never produced a setup, probable broken probe. Function body kept for archival; only registry entry stripped. |
| `RG2_range_support_bounce_long` | **REMOVED 2026-05-31** from `textbook_scalper.py` PROBE_REGISTRY | n/a | Same as above — 0 lab trades, broken probe. |

### V3-family formula-parity fix (2026-05-31)

`research_strategies/compression_expansion.py` had drifted between Mini
(lab) and EC2 (live):
- Mini lab build: `compression_percentile = 0.50` (Brock's correction with
  explanatory comment that 0.80 is mathematically infeasible)
- EC2 live: `compression_percentile = 0.80` (reverted to the buggy value)

This meant the legacy lab module for `compression_expansion` (49,181 trades
at 63% WR) was mined assuming pct=0.50, but the live bot was firing with
pct=0.80 — far fewer (near-zero) live candidates would emit, and the lab's
W/L rules wouldn't transfer cleanly.

**Patched on EC2 2026-05-31**: pct now matches Mini at 0.50. Live now
fires the same conditions that built the legacy rules.

Other minor diffs (cosmetic only, no live-vs-lab divergence):
- `trend.py`: Mini has defensive `_get()` helper; EC2 uses direct `.get()`.
  Behaviorally equivalent in current data paths.
- `research_strategies/{ifvg_imbalance, session_breakout, intraday_trend_pullback,
  chaikin_macd_atr, compression_mean_reversion}.py`: EC2 adds `_family`
  class attribute for dashboard metadata. Mini lacks it. Not behavior-
  affecting — only used by dashboard's `routing_cell_family` display field.

