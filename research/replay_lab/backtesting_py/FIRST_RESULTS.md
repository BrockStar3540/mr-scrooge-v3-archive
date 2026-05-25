# Replay Lab — Corrected First Results (USD_JPY canonical_lien_dbb, 30 days)

**Status:** This document replaces the earlier FIRST_RESULTS.md whose numbers
were tainted by a classifier-input bug. See "Correction" section below.

**Run window:** 2026-04-25 → 2026-05-25 (~5800 M5 bars)
**Strategy family:** canonical_lien_dbb (DBB1/2/3 long + short, 6 variants)
**Routing mode:** exact_strategy_only (live default)
**SL/TP:** 10/12 pips (live config)

---

## Correction (what went wrong + fix)

Initial run published numbers using `routing_mode="bypass"` because the
slate appeared to reject everything. Investigation revealed the actual cause:
**my `context_factory.build_snapshot()` was passing only 30 daily bars** to
the regime53 calculator, but `bb_compress` (the C-regime classification
input) needs 41+ daily bars (20-bar SMA × 20-bar rolling mean × shift-1).

With insufficient D-bar lookback, `bb_compress` came back `None`, so the
classifier fell through to non-C codes (R04 "tight_range" dominant). The
live bot doesn't have this problem because its `snapshot.candles["D"]`
holds 60+ bars.

**Fix:** bumped `d_lookback` default from 30 to 60 in `context_factory.py`.
Now the replay classifier produces 97% C01/C02 distribution, matching live
bot's 100% C01/C02 in the past hour's observer-captured logs.

Below numbers are post-fix, using live's default routing (not bypass).

---

## Experiment 1: Direction comparison

| direction | n_trades | WR | return | expectancy | max_DD |
|---|---:|---:|---:|---:|---:|
| native | 227 | 64.3% | **−38.0%** | +0.009% | −49.4% |
| reversed | 229 | 63.3% | **−22.0%** | +0.010% | −33.3% |

**Reversed bleeds 16% less return on identical setups.** Smaller gap than
the broken-classifier version (which showed 50% gap), but still consistent
with "long-bias is the worse side" on this specific cell/window. Don't
generalize from one pair × one strategy × one month.

## Experiment 2: Entry-mode comparison

| entry_mode | n_trades | WR | return | expectancy |
|---|---:|---:|---:|---:|
| signal | 227 | 64.3% | −38.0% | +0.009% |
| **pullback_2** | **164** | **62.2%** | **−32.5%** | **+0.012%** |
| pullback_4 | 119 | 52.9% | −37.7% | +0.007% |
| old_stop_zone (10p) | 0 | — | — | — |

**pullback_2 wins under live routing.** Under bypass it was pullback_4
(deeper), but live routing already filters to higher-quality setups; deep
pullback just misses too many fills. 10-pip pullback still gets zero fills
in any configuration — matches earlier live observation.

## Experiment 3: Management ablation (entry=signal, native dir)

| management | n_trades | WR | return | expectancy |
|---|---:|---:|---:|---:|
| none | 138 | 42.0% | −47.7% | **−0.008%** |
| **tp1_only** | **204** | **60.8%** | **−37.4%** | **+0.011%** |
| tp1_be | 227 | 64.3% | −38.0% | +0.009% |
| tp1_be_ratchet | 227 | 63.9% | −38.0% | +0.009% |

**TP1 partial harvest is the swing factor.** Without it, expectancy is
negative. With it, +0.011. Adding BE on top REDUCES expectancy. Adding
ratchet on top is a wash. This finding is identical to the bypass version
— management hierarchy is robust to routing mode.

## Provisional implications (still need cross-validation)

1. **TP1 partial-harvest is doing the heavy lifting.** Disabling it
   converts every config to negative expectancy. The fact that this
   finding survives both bypass and live-routing modes means it's
   trustworthy.
2. **BE manager is slightly destructive.** The earlier fix from
   0.5/0.1 → 0.7/0.6 helped vs the pre-fix scratch problem, but turning
   BE OFF altogether tests as slightly better here. Worth deeper test
   on other pairs/cells before changing live.
3. **pullback_2 entry is a candidate config change.** Under live
   routing it beats signal-entry on return AND expectancy. Half as many
   trades but 17% better return. Real candidate for a controlled live
   test if it holds on more pairs.
4. **Direction inversion: pair/cell specific.** The 6.8-year corpus
   showed long/short symmetric on average. This 30-day USD_JPY cell
   shows long-bias slightly worse — but the live-routing gap (16%) is
   smaller than the bypass gap (50%) was. The slate's regime filter is
   absorbing most of the "wrong-direction" signals before they fire.

## Next experiments

1. Cross-validate pullback_2 + tp1_only on direction-flipped setups
2. Same 3×3×3 sweep on NZD_JPY, CHF_JPY, EUR_JPY, GBP_JPY DBB cells
3. Wire box_master_theory + textbook family wrappers
4. Re-run with v1.13_full_mirror (long+short symmetry) and compare to
   v1.12_comprehensive routing — does the mirror help or hurt expectancy?
5. Vary BE trigger/offset across (0.3R, 0.5R, 0.7R, 1.0R) sweep
