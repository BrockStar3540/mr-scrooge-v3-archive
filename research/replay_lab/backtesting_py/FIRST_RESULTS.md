# Replay Lab — First Real Results (USD_JPY canonical_lien_dbb, 30 days)

**Run window:** 2026-04-25 → 2026-05-25 (~5800 M5 bars)
**Strategy family:** canonical_lien_dbb (DBB1/2/3 long + short, 6 variants)
**Routing mode:** bypass (raw strategy edge, slate filter off)
**SL/TP:** 10/12 pips (live config)

---

## Experiment 1: Direction comparison

| direction | n_trades | WR | return | expectancy/trade | max_DD |
|---|---:|---:|---:|---:|---:|
| native (long-biased emissions) | 361 | 62.3% | **−52.6%** | +0.008% | −62.1% |
| reversed (flip every direction) | 349 | 65.0% | **−0.04%** | +0.012% | −33.8% |

Same setups, same window, reversed bleeds ~50% less. **First piece of corpus-level
evidence supporting Brock's long-standing "bot is trading backwards" intuition**
on this specific cell.

Caveat: one pair × one strategy × one month. Don't generalize. But it's a
concrete datapoint we couldn't get from anywhere else.

## Experiment 2: Entry-mode comparison

| entry_mode | n_trades | WR | return | expectancy |
|---|---:|---:|---:|---:|
| signal | 361 | 62.3% | −52.6% | +0.008% |
| pullback_2 | 183 | 57.4% | −38.1% | +0.008% |
| **pullback_4** | **129** | **56.6%** | **−8.1%** | **+0.014%** |
| old_stop_zone (10p pullback) | 0 | — | 0 | — |

**pullback_4 wins on every dimension that matters** (return + expectancy)
despite the lowest WR. Fewer fills, better quality. 10-pip pullback fills
zero — same observation as live earlier this week.

## Experiment 3: Management ablation (entry=signal, native dir)

| management | n_trades | WR | return | expectancy |
|---|---:|---:|---:|---:|
| none (raw 10/12) | 214 | 42.1% | −62.1% | **−0.007%** |
| **tp1_only** | **316** | **60.8%** | **−47.9%** | **+0.010%** |
| tp1_be | 361 | 62.3% | −52.6% | +0.008% |
| tp1_be_ratchet | 364 | 61.5% | −55.5% | +0.008% |

**BE manager and ratchet both hurt expectancy slightly.** TP1 partial harvest
is doing massive work — without it, expectancy goes negative. With it, +0.010.
Adding BE on top pulls trades to scratch that would have continued. Adding
ratchet on top compounds the harm marginally.

## Provisional implications (need cross-validation)

1. **TP1 partial-harvest is the dominant management lever.** Confirmed it
   matters by ~17% WR delta and is the swing factor between negative and
   positive expectancy.
2. **BE manager (0.7R trigger / 0.6R offset) is slightly destructive in
   this regime.** The fix-arc move from 0.5/0.1 → 0.7/0.6 earlier today
   helped reduce scratch frequency, but disabling BE entirely produces a
   better number here. Worth follow-up on whether this generalizes.
3. **pullback_4 entry geometry is a real candidate.** The reverse-arc
   conclusion was that LIMIT-at-signal was best — but that conclusion was
   on a small sample and didn't include this comparison. pullback_4 here
   beats both signal-price entry and 10-pip-deep pullback.
4. **Direction inversion: real but pair/cell specific.** The 6.8-year corpus
   showed long/short symmetric on average across ALL pairs. This 30-day
   USD_JPY DBB cell shows native much worse than reversed. The difference
   between corpus average and this cell is what makes it interesting —
   either USD_JPY DBB specifically has a problem, or the recent 30 days
   were an unfavorable USD_JPY long environment.

## Next experiments worth running

1. **Cross-validate pullback_4 + tp1_only on direction-flipped setups.**
   If reversed + pullback_4 + tp1_only is better than any other combo,
   that's a config change candidate.
2. **Same 4×4×3 sweep on NZD_JPY, CHF_JPY, EUR_JPY DBB cells.** Confirm
   or refute that "native loses" pattern across JPY crosses.
3. **Sweep on box_master_theory + textbook families once their wrappers
   are added** (currently only canonical_lien_dbb is wired).
4. **Run with slate-filtered routing** (exact_strategy_only, not bypass) to
   see what happens when the v1.13 mirror slate filters down to its
   genuinely-promoted cells.

## What this validates about the lab

- End-to-end pipeline correct: feature pipeline, classifier dispatch,
  strategy emission, routing match, backtesting.py execution, summary CSV
- Classifier wiring fix (session_bucket now reads snap.timestamp) works
  for both live AND replay paths
- D-bar pre-extension warmup gives regime53 enough history
- 17 distinct regime53 codes observed, 8 session buckets observed, full
  distribution
- Strategies emit 851/1900 bars (~45% rate, healthy)
- bypass mode lets us test raw strategy edge independent of slate coverage

## Caveats

- Single pair × single family × 30 days — sample is small
- BB compression / OTR warnings persist on some bars (expected — fail-open
  features when zone_detector can't draw)
- Daily ATR warning on early bars (expected — warmup window)
