# Replay Lab — Regime-Gated vs Regime-Free 6m Comparison

**Run:** 2026-05-26 06:37 UTC
**Both sweeps:** 27 pairs × 2 families × 2 directions = 108 backtests each
**Window:** 2025-11-25 → 2026-05-25 (6 months)
**Only difference:** `routing_mode`
- Gated = `exact_plus_family` (current live config: slate filters to C01/C02 cells)
- Free  = `bypass` (no slate, strategies emit freely on every bar)

## TOP-LINE: regime filter is a double-edged sword

| family | direction | GATED return | FREE return | trades gated | trades free |
|---|---|---:|---:|---:|---:|
| canonical_lien_dbb | native | **−10.5%** | −17.5% | 10,930 | 27,573 |
| **canonical_lien_dbb** | **reversed** | **−29.9%** | **+18.5%** | 11,243 | 32,106 |
| **box_master_theory** | **native** | **−6.6%** | −24.0% | 5,046 | 30,777 |
| box_master_theory | reversed | −22.5% | −40.2% | 5,028 | 37,516 |

**Three things this exposes:**

1. **3x more emissions when slate is removed.** Strategies fire constantly; slate filters out 2/3.
2. **DBB reversed flips from −30% to +18% without the slate.** The slate is actively SELECTING the cells where reversed DBB loses — broader universe has reversed DBB winning. **This is the most actionable finding of the entire lab so far.**
3. **MTB native still wins vs reversed in BOTH modes.** That preference is robust.

## TOP 10 cells (regime-FREE, where the slate is missing edge)

| pair | family | direction | trades | WR | return | max DD |
|---|---|---|---:|---:|---:|---:|
| NZD_CHF | MTB | native | 562 | 68.7% | **+326.3%** | −78.6% |
| NZD_CHF | DBB | reversed | 549 | 68.9% | **+301.8%** | −92.8% |
| EUR_CAD | DBB | reversed | 1878 | 65.1% | **+177.9%** | −51.6% |
| AUD_NZD | DBB | native | 1192 | 63.0% | **+747.4%** *(see caveat)* | −? |
| GBP_CHF | MTB | native | 318 | 67.6% | +112.2% | −42.2% |
| EUR_GBP | DBB | reversed | 433 | 63.7% | +609.9% *(see caveat)* | −? |
| EUR_CHF | DBB | reversed | 516 | 64.2% | +421.6% *(see caveat)* | −? |
| GBP_CAD | MTB | native | 796 | 64.8% | +90.0% | −33.2% |
| AUD_JPY | DBB | native | 2550 | 63.4% | +145.1% | −? |
| GBP_CHF | DBB | reversed | 1295 | 64.9% | +70.1% | −77.0% |

⚠️ The +747% / +609% / +421% numbers should be treated cautiously — at
those return levels in a 6-month window we're likely seeing compounding
artifacts or signal-collision quirks. The mid-tier (+70 to +180%) cells
are more credible.

## The 5 "silent" pairs from gated mode WERE producing strong signal

These 5 pairs had ZERO trades in the gated sweep — slate has no cells
for them. In regime-free mode they're all firing, several positive:

| Pair | Best regime-free config | Return |
|---|---|---:|
| **NZD_CHF** | MTB native | **+326.3%** (562 trades) |
| **EUR_CAD** | DBB reversed | **+177.9%** (1878 trades) |
| **GBP_CAD** | MTB native | **+90.0%** (796 trades) |
| **GBP_CHF** | MTB native | **+112.2%** (318 trades) |
| GBP_NZD | none clean | best is DBB native −20% |
| EUR_NZD | DBB reversed | +24% but huge DD |
| NZD_CAD | MTB native | +34% |

**The slate is leaving real money on the table for at least 4 of these
5 pairs.** They were silent in our 6m gated sweep purely because the
slate didn't have cells for them — not because the market wasn't moving.

## Cells where REGIME GATE HELPS (slate IS removing losers)

| Cell | Gated return | Free return | Gate saves |
|---|---:|---:|---:|
| AUD_USD DBB reversed | +94.2% | −86.6% | **+181 points** |
| EUR_JPY MTB native | +56.7% | −85.0% | +142 |
| GBP_AUD DBB native | +78.4% | −58.2% | +137 |
| GBP_CHF MTB reversed | +20.0% | −97.9% | +118 |
| NZD_USD DBB native | +40.7% | −60.5% | +101 |
| EUR_AUD MTB reversed | +5.2% | −94.6% | +100 |
| NZD_JPY MTB native | +70.0% | −22.5% | +93 |

These cells are confirmed by the gate doing what it's supposed to do —
filter signals to favorable regime windows. The slate is genuinely
helping on these.

## Cells where REGIME GATE HURTS (slate IS removing winners)

| Cell | Gated return | Free return | Gate destroys |
|---|---:|---:|---:|
| AUD_NZD DBB native | −16.7% | +747.4% | **−764 points** |
| EUR_GBP DBB reversed | −2.7% | +609.9% | −613 |
| EUR_CHF DBB reversed | +8.8% | +421.6% | −413 |
| GBP_USD MTB reversed | −4.1% | +374.6% | −379 |
| GBP_CHF MTB native | −41.0% | +112.2% | −153 |
| AUD_JPY DBB native | −5.1% | +145.1% | −150 |
| GBP_AUD DBB reversed | −62.8% | +26.8% | −90 |
| USD_CHF DBB reversed | −84.1% | +0.6% | −85 |
| EUR_GBP MTB native | +0.6% | +77.2% | −77 |
| AUD_CAD MTB reversed | −19.3% | +57.3% | −77 |

**Take this with a grain of salt** — return-pct numbers in the +400 to
+700% range may have backtesting.py compounding artifacts. But the
direction of effect (gate filters out winners) is unambiguous.

## What this means for the slate

The current v1.13_mirror slate is **a mixed-signal filter**: removes
real bleeders (good) AND removes real winners (bad). Net effect over
6 months: aggregate return moved from −10/-30% on DBB to a more uniform
−6 to −24% across families. Slightly less variance, similar bleed.

**The slate is not strictly an improvement over no-slate.** It's a
filter that happens to remove both extremes.

## Three possible directions

1. **Rebuild slate from regime-free findings** — promote the cells with
   strong regime-free edge AND survived 6m, retire cells where regime-free
   is worse than gated. Half-day of slate-build work.

2. **Redefine regimes** — current C01/C02 (tight-coil low/high ADX) may
   not be the right cut. The fact that the slate misses real signal
   suggests the regime definition itself is too narrow. Could try
   alternate classifications: ADR-position, trend strength, session-vol.

3. **Both** — rebuild slate AND refine regime definitions. Multi-day.

## What this enables for new strategy testing

When we add the new strategies from `scrooge-strategy-backlog.md`:
- We can test them BOTH ways (gated + bypass) and see if they have
  intrinsic edge OR require regime filtering to work
- The Higher-TF Trend Filter is itself a "regime" by another name
  (just bullish/bearish bias, not C01/C02). Worth testing as the
  PRIMARY filter before adding any other regime.

## Methodology caveats (same as before)

- Single-asset model; no portfolio correlation
- No intrabar simulation
- Fixed per-pair spread
- 6-month window only — multi-regime validation still needs 6.8yr (lab refactor first)
- 5 of 9 strategy families NOT yet tested in any sweep (darvas, probes, future new strategies)
