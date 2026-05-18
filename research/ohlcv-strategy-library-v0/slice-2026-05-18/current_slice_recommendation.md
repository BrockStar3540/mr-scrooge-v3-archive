# Current-slice war-room — 2026-05-18T17:41:16.504774+00:00

## Slice snapshot
- UTC hour: 17 | session: **ny_close** | dominant regime: **C02**
- Top live pairs (60min): USD_CHF, EUR_CAD
- Family mix: {'direct': 38}
- Direction mix: {'long': 19, 'short': 19}
- Shadow shave-passes in slice window: 0

## Fast-candidate inventory
- live_validated_parent in slice: 5 (session_match=0)
- boundary_sibling in slice:      12 (session_match=0)
- v9_observe_seed in slice:       42
- probe_seed_child in slice:      339
- ranked candidates (dedup deploy): **59**
- fast candidates (in-session, in-pair, sibling+ parent): **0**

## Top-10 candidates for current slice

| rank | regime | pair | family | strategy | dir | session | source | n | wr | shadow_pass | score |
|---:|---|---|---|---|---|---|---|---:|---:|---:|---:|
| 1 | C02 | USD_CHF | dbb_trend | alpha_pullback_v2 | long | ny_close | v9_observe_seed | 10 | 1.000 | 0 | 9.14 |
| 2 | C02 | EUR_CAD | direct | charlie_compression_breakout | long | ny_close | v9_observe_seed | 13 | 0.923 | 0 | 8.76 |
| 3 | C02 | USD_CHF | direct | alpha_breakout_retest_v2 | long | ny_close | v9_observe_seed | 17 | 0.882 | 0 | 8.70 |
| 4 | C02 | EUR_CAD | dbb_trend | TF6_ma_ribbon_short | short | ny_close | v9_observe_seed | 21 | 0.857 | 0 | 8.69 |
| 5 | C02 | USD_CHF | reversal | alpha_extended_fade_v2 | short | ny_close | v9_observe_seed | 16 | 0.875 | 0 | 8.60 |
| 6 | C02 | USD_CHF | dbb_trend | TF6_ma_ribbon_long | long | ny_close | v9_observe_seed | 11 | 0.909 | 0 | 8.52 |
| 7 | C02 | EUR_CAD | dbb_trend | charlie_pullback_continuation_v2 | long | ny_close | v9_observe_seed | 11 | 0.909 | 0 | 8.52 |
| 8 | C02 | USD_CHF | dbb_trend | TF6_ma_ribbon_short | short | ny_close | v9_observe_seed | 15 | 0.867 | 0 | 8.49 |
| 9 | C02 | EUR_CAD | dbb_trend | TF6_ma_ribbon_long | long | ny_close | v9_observe_seed | 15 | 0.867 | 0 | 8.49 |
| 10 | C02 | EUR_CAD | dbb_trend | TF3_supertrend_long | long | ny_close | v9_observe_seed | 10 | 0.900 | 0 | 8.37 |

## Fallback ladder by pair

| pair | direction | tier | source | strategy | session | n | wr | reason |
|---|---|---|---|---|---|---:|---:|---|
| USD_CHF | long | alt_family | v9_observe_seed | alpha_pullback_v2 | ny_close | 10 | 1.0 | v9_observe Seed in regime+pair |
| USD_CHF | short | alt_family | v9_observe_seed | alpha_extended_fade_v2 | ny_close | 16 | 0.875 | v9_observe Seed in regime+pair |
| EUR_CAD | long | alt_family | v9_observe_seed | charlie_compression_breakout | ny_close | 13 | 0.923 | v9_observe Seed in regime+pair |
| EUR_CAD | short | alt_family | v9_observe_seed | TF6_ma_ribbon_short | ny_close | 21 | 0.857 | v9_observe Seed in regime+pair |

## Direct answer: what should fire now?

**No cell currently in the live trade table OR among widened siblings matches the current session.**
All live-validated parents are for ny_open or ny_mid; current session is **ny_close**.

Fix options:
- Promote boundary siblings whose session_bucket clause was widened to include current session.
- Mine new cells for the active session by re-running strike pass with current slice as target.
- Accept no-trade for this session.

## Recommendation
- **4 of 4 pair×direction tuples have an honest fit.**
- Tier breakdown: alt_family=4

Build `v10_fast_v1.1` from `current_slice_fast_candidates.csv` and flip.
This is a session-and-slice-aware narrow surface, not a universal table.