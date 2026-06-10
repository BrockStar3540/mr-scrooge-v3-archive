# ATR-collapse emergency exit + the runner investigation — 2026-06-09

## The problem
12h audit: ~half of all losers (48% peaked >=+4p) were trades that went GREEN then
bled to the full -12 SL. The green-exit ladder only arms protection at TP1 (+12),
so a trade peaking +8 had ZERO protection (the "sub-+12 dead zone").

## What we tested (order-resolved M5 replay, green_exit_bt engine, per_pair_lab 6mo)
All on align==4 (the runners) — the real test, since trails must not choke them:
| exit | align-4 net/trade | vs baseline |
|---|---|---|
| baseline ladder | +1.255 | — |
| fixed give-back trail | +1.224 | -0.031 (chokes) |
| volatility-scaled trail | +1.017 | -0.237 (chokes more) |
| **ATR-collapse take-green** | **+1.266** | **+0.012 (only winner)** |

Trails cut on PRICE pullback -> choke runners (runners pull back). ATR-collapse cuts
on VOLATILITY death -> runners keep ATR high so they're spared; only stalled trades cut.

## Key findings
1. **Runners are a VOLATILITY phenomenon, not alignment.** Align is flat across MFE
   tiers (1.89-2.05); higher align slightly REDUCES 30+ odds. The run-size predictors
   are the ATR factors: A5=atr_5m_pips, A1=atr_1h_pips, ADR (30+ signature: A1_2 3.71x,
   A5_3 2.95x, ADR5 2.05x).
2. **align-immunity is redundant.** Making align-4 immune to the exit: +0.007 vs +0.009
   (no help). 30+ runners realize +13.64p whether the exit is active or immune -
   IDENTICAL. The ATR-collapse is self-immune to runners by construction (a runner keeps
   its ATR, so a collapse trigger physically can't fire on it).
3. **The give-back bleed is an ENTRY problem** (low-align trades). The only thing that
   "helps" broadly (the blunt trail, +0.27 on all-aligns) does so by amputating low-align
   trades mid-flight = an align-filter in disguise; on good trades it loses. Not taking
   them (entry gate) beats any mid-trade cut.

## What shipped
`green_exit.py`: `_recent_atr_pips()` (mean per-bar 5m range, last 12 bars = the validated
signal) + ATR-collapse rule in check() Phase-1 dead zone: if not tp1_done and profit>=6
and recent 5m ATR < 1.5p -> harvest the green. Behind `management.green_exit.atr_collapse_exit`
(enabled, arm_pips 6, atr_thresh_pips 1.5). Verified: fires on 0.8p vol, spares 4.0p runner.
Small (~+0.01p/trade) but free: never chokes a runner, nudges WR up, instantly reversible.

## Entry lever -- RESOLVED (already pulled by the gate fixes)
Profiled the low-align x low-vol cells (corpus_8yr, 1.6M signals): align<=1 & ADR<=2 = 15%
of the raw candidate pool at ~-2p net; align<=2 & ADR<=2 = 26%. Net-positive EV exists ONLY
in the high-align x high-vol corner (align 3-4 x ADR 4-5); everything low-align OR low-vol
is net-negative, far below the +1.25 floor. So the corrected EV gate ALREADY excludes the
low-align x low-vol bleeders by selecting +EV -- the bot doesn't take them.

The give-back bleed was a BROKEN-gate symptom: frozen align + pooled direction made those
cells look up a WRONG, sometimes-passing EV. The htf-unfreeze (6964295) + direction-key
(9cc79b1) fixes made them read their true -2p and get rejected. No explicit entry filter
needed -- the lever was real, and we already pulled it when we unfroze align and keyed
direction. (Profile: giveback_volume.py.)
