# Replay Lab — 6-Month Universal Sweep Report

**Run:** 2026-05-26 04:34 UTC
**Hardware:** Mac Mini M-series (10 cores, 16 GB RAM), 8 worker processes
**Runtime:** **67 minutes for 108 backtests** (~37 sec/cell)

## Scope

- **27 pairs** (full live universe)
- **2 strategy families:** canonical_lien_dbb (DBB), box_master_theory (MTB)
- **2 direction modes:** native, reversed
- **Held constant:** entry=signal, management=tp1_only, routing=exact_plus_family
- **Window: 2025-11-25 → 2026-05-25 (182 days, 6 months)**
- Captures: BoE/Fed/ECB Q4-Q1 hiking pause, USD pivot Q2, yen post-intervention, Memorial Day quiet

= **108 backtests, 32,247 trades total, 0 errors.**

## TOP-LINE: native wins for BOTH families at 6-month scale

| family | direction | trades | avg WR | avg return | avg expectancy |
|---|---|---:|---:|---:|---:|
| **canonical_lien_dbb** | **native** | 10,930 | 63.8% | **−10.5%** | +0.023% |
| canonical_lien_dbb | reversed | 11,243 | 60.9% | −29.9% | +0.020% |
| **box_master_theory** | **native** | 5,046 | 65.1% | **−6.6%** | +0.027% |
| box_master_theory | reversed | 5,028 | 60.7% | −22.5% | +0.019% |

**This OVERTURNS the 30-day finding** that MTB wanted reversed. At 6-month
scale, both families prefer native by a clear margin. The 30-day "MTB
wants reversed" was sample noise.

**Both families still bleed money on average.** Best aggregate (MTB native)
is −6.6%. But individual cells vary wildly.

## 30-day TOP-10 cells — did they hold at 6 months?

| Pair | Family | Direction | 30d return | 6m return | Verdict |
|---|---|---|---:|---:|:---|
| NZD_JPY | DBB | reversed | +63.6% | **−85.6%** | 💥 **INVERTED** |
| NZD_JPY | MTB | native | +50.6% | **+70.0%** | ✅ HELD + GREW |
| GBP_AUD | DBB | native | +38.3% | **+78.4%** | ✅ HELD + GREW |
| EUR_USD | DBB | native | +36.0% | +17.2% | ✅ held (shrunk) |
| EUR_CHF | MTB | reversed | +35.6% | **−78.9%** | 💥 **INVERTED** |
| AUD_CAD | MTB | native | +32.7% | **+49.7%** | ✅ HELD + GREW |
| AUD_CAD | DBB | reversed | +32.6% | +3.0% | ✅ held (weak) |
| GBP_USD | DBB | native | +28.7% | −5.9% | 💥 turned negative |
| GBP_AUD | MTB | native | +28.3% | +3.2% | ✅ held (weak) |
| AUD_CHF | MTB | reversed | +26.8% | **−29.8%** | 💥 **INVERTED** |

**4 of 10 inverted from winners to losers.** That's a 40% false-positive
rate on 30-day data. Critical validation that **30-day sample alone is
not enough to gate live deployment decisions.**

## Top-10 6-month winners

| Pair | Family | Direction | trades | WR | return | max DD |
|---|---|---|---:|---:|---:|---:|
| AUD_USD | DBB | reversed | 808 | 65.2% | **+94.2%** | −67.5% |
| **GBP_AUD** | **DBB** | **native** | **218** | **69.7%** | **+78.4%** | **−19.6%** |
| NZD_JPY | MTB | native | 228 | 67.1% | +70.0% | −31.9% |
| EUR_JPY | MTB | native | 330 | 66.4% | +56.7% | −35.2% |
| AUD_CAD | MTB | native | 190 | 67.4% | +49.7% | −36.5% |
| NZD_USD | DBB | native | 492 | 68.1% | +40.7% | **−80.2%** |
| EUR_CAD | MTB | native | 371 | 64.7% | +31.6% | −23.2% |
| GBP_CHF | MTB | reversed | 102 | 66.7% | +20.0% | −23.0% |
| AUD_JPY | MTB | reversed | 249 | 65.5% | +19.5% | −47.2% |
| EUR_USD | DBB | native | 485 | 63.9% | +17.2% | −57.6% |

**GBP_AUD DBB native is the standout** — 218 trades, 69.7% WR, +78.4%
return, only −19.6% drawdown. Best risk-adjusted positive cell in the
entire sweep.

⚠️ Several top-return cells have brutal drawdowns. AUD_USD DBB reversed
returned +94% but had a −67% intermediate drawdown — equity-curve
ulcerative even if it ends positive. NZD_USD DBB native is even worse
(+40% with −80% DD).

## Bottom-10 6-month losers — never run these configs

| Pair | Family | Direction | trades | return | max DD |
|---|---|---|---:|---:|---:|
| AUD_USD | DBB | native | 739 | **−94.0%** | −97.2% |
| NZD_USD | MTB | reversed | 357 | −92.7% | −94.0% |
| EUR_USD | DBB | reversed | 508 | −86.5% | −89.1% |
| NZD_JPY | DBB | reversed | 872 | −85.6% | −94.2% |
| USD_CHF | DBB | reversed | 802 | −84.1% | −94.7% |
| NZD_JPY | MTB | reversed | 222 | −80.0% | −84.1% |
| EUR_CHF | MTB | reversed | 214 | −78.9% | −86.8% |
| USD_CHF | MTB | reversed | 329 | −78.0% | −84.5% |
| GBP_JPY | DBB | reversed | 1484 | −72.2% | −80.4% |
| AUD_CHF | MTB | native | 359 | −71.4% | −79.9% |

**USD_JPY DBB native = −69%** and **USD_JPY DBB reversed = −66%** over
6 months. Both directions of USD_JPY DBB are catastrophic. **The live bot
fires USD_JPY DBB cells frequently** — this is direct evidence those
should be removed from the routing slate.

## Per-pair best config (22 pairs with trades, 1 row per pair)

| pair | best family | best dir | 6m return |
|---|---|---|---:|
| AUD_USD | DBB | reversed | +94.2% |
| GBP_AUD | DBB | native | +78.4% |
| NZD_JPY | MTB | native | +70.0% |
| EUR_JPY | MTB | native | +56.7% |
| AUD_CAD | MTB | native | +49.7% |
| NZD_USD | DBB | native | +40.7% |
| EUR_CAD | MTB | native | +31.6% |
| GBP_CHF | MTB | reversed | +20.0% |
| AUD_JPY | MTB | reversed | +19.5% |
| EUR_USD | DBB | native | +17.2% |
| AUD_NZD | MTB | native | +13.8% |
| EUR_CHF | DBB | reversed | +8.8% |
| GBP_USD | MTB | native | +7.1% (only 4 trades — discard) |
| GBP_JPY | DBB | native | +6.5% |
| EUR_AUD | MTB | reversed | +5.2% |
| USD_CAD | MTB | reversed | +5.2% |
| EUR_GBP | DBB | native | +2.9% |
| USD_JPY | MTB | reversed | −10.7% |
| CHF_JPY | DBB | native | −16.4% |
| USD_CHF | MTB | native | −20.2% |
| CAD_JPY | DBB | native | −28.2% |
| AUD_CHF | MTB | reversed | −29.8% |

**17 of 22 pairs have at least one positive config over 6 months.**
**5 silent pairs** (EUR_NZD, GBP_CAD, GBP_NZD, NZD_CAD, NZD_CHF) — same as 30-day.

## Implications for live deployment

1. **GBP_AUD DBB native is the single most defensible cell** to promote
   to the live slate — strong return, healthy WR, moderate drawdown,
   confirmed across both 30-day and 6-month windows.
2. **Pull USD_JPY DBB cells from the slate.** −69% native, −66% reversed
   over 6 months. The bot fires these cells frequently — every fire is
   negative expectancy.
3. **30-day cell discovery is unreliable.** 40% false-positive rate from
   the 30-day winners list. Always validate 30-day candidates at 6-month
   before live deployment.
4. **Native direction is the consistent winner.** A "reverse all
   directions" experiment (we tried this earlier — flag was rolled back)
   would have been wrong for BOTH families at 6-month scale.
5. **The bot is bleeding even with good cells.** Best aggregate
   config (MTB native) is −6.6% over 6 months. The bot needs cell
   filtering + management improvements to get to positive aggregate.

## Methodology caveats

- Only 2 of 5 strategy families tested (DBB + MTB). canonical_darvas and
  probes/textbook_scalper need separate sweeps.
- Held entry=signal and management=tp1_only constant. Full matrix would
  be 1728 backtests, ~10 hours on Mini.
- Routing mode `exact_plus_family` is inclusive. `exact_strategy_only`
  may produce different per-cell numbers.
- Some pairs have very few trades (GBP_USD MTB n=4); statistical
  significance is limited.
- 6 months is still one regime. Multi-regime validation needs the full
  6.8-year sweep (planned next, requires lab refactor for speed).
