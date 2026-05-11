# Box-drawing bugs (chronological)

## 2026-03-09 — Inverted boxes from 8-day-stale hourly slice
- session: 2026-03-09_77af2792.md (lines 12347-12950)
- failure: `zone_detector._get_prior_day_hourly()` used `iloc[:24]` (OLDEST 24 of 200 bars passed in by main.py), pulling data from 8+ days prior. Percentile filter then "cleaned" yesterday's PDH/PDL using ancient bars, producing wildly wrong levels and, on several pairs, fully inverted boxes (PDL > PDH).
- root cause: function written assuming 48-bar input; main.py passes 200. No validation that PDH > PDL after percentile filtering. Inverted boxes broke zone direction logic — bot took longs in clear EUR downtrend (EUR/USD, EUR/CAD) and counter-trend across the EUR complex.
- affected: USD_CAD, EUR_NZD, GBP_CAD confirmed inverted on 03-09; EUR/USD PDH inflated 1.16672 → 1.17570 (+900 pips of contamination). EUR pairs (EUR/CAD, EUR/USD, EUR/AUD, EUR/NZD) all had wrong-direction entries during the window.
- fix: `iloc[:24]` → `iloc[-48:-24]` (anchor to end of array = yesterday's 24 bars). Added PDH>PDL sanity guard falling back to raw OANDA values + clear error log. Trend filter also tightened (10-bar lookback, 0.0005 slope vs 5-bar 0.001). Dashboard fix to show `alternative_box` when `using_alternative=True`. No commit hash captured in session.
- contaminated window: unknown start (whenever 200-bar fetch was introduced) through 2026-03-09 fix. All EUR-pair longs in the lead-up are suspect — Brock manually closed everything except EUR/CHF and USD/CHF after the fix.

## 2026-03-19 — 30m rolling box experiment (broke profitability)
- session: 2026-03-19_4ac1dfc3.md (lines 3563-3770, 5286-5381, 6393)
- failure: Replaced daily PDH/PDL with `_build_30m_box()` using last 24 × 30m bars (12hr window). Box now shifted every cycle. Coupled with zone-anchored entries (entry = zone_price × 1.0001, stop = PDH × 1.001) — a complete strategy rewrite, not a parameter tweak. Bot bled money the entire window.
- root cause: 30m box updates ~48x/day so the "level" the bot was fading was never a true overnight liquidity wall. ATR/OTR/sucker-move gates were all calibrated against daily-box geometry — incompatible with 12hr shifting walls. Old log entries from daily-box code intermixed during transition, masking the regression.
- affected: All pairs traded during the experiment.
- fix: Commit `59e83b9` on 2026-03-20 — "Revert to profitable daily box strategy. Reverts 30m rolling box experiment and zone-anchored entries that broke profitability." Full revert of zone_detector.py, box_state_machine.py, CONFIG back to daily mode, 50% margin, sizing/decompressors restored, green exit restored, volatility gate restored.
- contaminated window: 2026-03-19 evening (~commit b96fe77 push) through 2026-03-20 afternoon (commit 59e83b9). Roughly 18-24 hours of live trades on the experimental box — EXCLUDE this window entirely from any live-truth backtest.

## 2026-03-20 — Box shrinking from percentile filter + gap handling
- session: 2026-03-20_1c92abef.md (lines 244, 289, 5143)
- failure: Percentile filtering removed spike wicks aggressively; combined with gap-handling logic this made daily boxes artificially narrow. Half-box geometry shrank → TPs (midline) moved closer to entry → tighter R:R. Separately, crypto path used a 24h fixed UTC session in `_build_session_box()` with a 1% minimum-box-size floor that often rejected the box entirely on low-vol days (causing no-trade days that LOOKED like a "bot off" bug).
- root cause: percentile filter (`raw_PDH` → filtered PDH) was clipping 0.33-0.39% on USD/CHF type pairs and similar elsewhere. No floor between "filter spike wicks" and "delete real range."
- affected: All forex pairs (narrower boxes); all crypto pairs on low-vol days (rejected boxes).
- fix: Discussion-only in this session — flagged as audit item #3 ("Box shrinking") and #12 ("Crypto wrong session"). Filter not removed; the 03-20 revert kept the filter behavior. Later (03-25) Brock and Claude observed the same percentile clipping causing the USD/CHF LONG TP-below-market rejection cascade.
- contaminated window: ongoing — percentile filter never fully removed in V1/V2. Every long that hit TP1=filtered_PDH had a slightly compressed target. Magnitude: ~5-15 pips per pair per day, varies by pair.

## 2026-03-25 — Filtered PDH below market → 5 OANDA 400 rejections on USD/CHF
- session: 2026-03-25_559a3c94.md (lines 630-720)
- failure: Percentile filter clipped USD/CHF PDH from 0.79248 → 0.78939. Long signal fired with TP2 = filtered PDH. Current market was 0.790+, ABOVE the clipped TP. OANDA rejected 5 market orders (tickets 304, 305, 306 on V2 + 2 on V1) because BUY TP price must be > current market.
- root cause: `_calculate_targets()` only validated `tp2 > entry_price` (the signal's pitchfork trigger), not `tp2 > current_market`. Market orders fill above the trigger; the gap exposed the bad TP.
- affected: USD/CHF LONG on 2026-03-25 (5 rejections). Any LONG with filtered PDH < current market would hit the same wall.
- fix: Not fully fixed in this session — diagnosis written; the structural fix is "validate TP vs current market before submit" plus the broader "remove or cap percentile filter." V1's behavior was masked previously by a separate copy-paste bug (`new_stop` undefined in `place_entry_order`, fixed by commit `3f14762e` on 03-24); pre-fix V1 had zero entries because of the NameError, then started entering and immediately exposed this.
- contaminated window: 03-24 (3f14762e deployed) through 03-25 (rejections discovered). Any long with filtered-PDH TP below market is suspect across V1's life after 3f14762e; volume small (only 5 attempts in this snapshot but pattern is structural).

## 2026-03-29 — Box-reset amnesia at midnight UTC
- session: 2026-03-29_606b6ebc.md (lines 3585-3760, 6879-6946)
- failure: At 00:00 UTC the daily box recomputes. Any pair that had been BLOCKED for hours/days (score -4 to -6 from rejection_failed, expansion_pressure, price-outside-box) instantly resets: new PDH/PDL → price now "inside" new box → `box_contained(+1)` fires, prior negative signals all forget themselves → score jumps from -6 to +1 → entry permitted. Bot takes the trade. Bot loses.
- root cause: Negative regime signals were computed against the OLD box and not carried over the boundary. Hysteresis as coded required score ≥ +1 after BLOCKED — but the new-box +1 score trivially satisfied this. Floor and hysteresis used the same threshold = no real protection.
- affected: USD/MXN (loss -$1,197), EUR/CHF (bad entry at 14:02 UTC after 06:31 UTC BLOCKED-score=-6), confirmed pattern. Likely contaminated other pairs across many UTC midnights. NZD/JPY 3/31 8:31 AM re-entry (-$53.30) is in the same family.
- fix: Hysteresis tightened — after BLOCKED (score ≤ -3), recovery requires score ≥ +2 (NORMAL with at least two positive signals), not ≥ +1. Tagged `REGIME_HYSTERESIS` in logs. Applied in V2 coordinator.py and V1 once regime activated. Also added regime score floor.
- contaminated window: every UTC-midnight transition where a pair was BLOCKED in the hours before, from regime activation (around 2026-03-22 to 03-23 V2 / 03-31 V1) through fix on 2026-03-29 to 2026-04-01. EXCLUDE all entries within the first ~2 hours of UTC day for pairs that were BLOCKED in the prior 24h on that window.

## 2026-04-09 — Stale-box TP2 at 7,883 pips
- session: 2026-04-09_3b97eb1c.md (lines 1994-2340, 2913-2973) and 2026-04-09_86bbfcec.md (lines 664-1849)
- failure: Two USD/CHF entries and one GBP/CAD entry showed TP1/TP2 distances of 7,883 pips (USD/CHF) and ~18,400 pips (GBP/CAD) in the sizing log. Absurd target values from stale box data — pip-distance calculation pulled wrong PDH/PDL from a previous day's snapshot.
- root cause: Defect #11 in V2 audit. Box snapshot used in `_calculate_targets()` was not refreshed for these pairs; old box (likely from a prior alternative-box build or a session that hadn't rolled) was carried into target math. Underlying box build is suspect — but the immediate symptom is unbounded TPs.
- affected: USD/CHF (2 entries), GBP/CAD (1 entry), 2026-04-09. Practically the absurd TP was unreachable, so the trades behaved like "no TP" — they ran to SL or partial harvest exit rather than hitting target.
- fix: 3x daily-ATR clamp added in `_calculate_targets()` (B.4 patch). If TP2 distance > 3x ATR, clamp to 3x ATR and log warning. This is a guard, not a root-cause fix to the stale box. Logged in DEFECTS as fixed 2026-04-09.
- contaminated window: unknown earlier extent — the bug surfaced 04-09 but the staleness mechanism could have produced silent contamination on any prior day. Conservative: treat every USD/CHF and GBP/CAD entry from 03-31 (V1 regime activation) through 04-09 fix as potentially contaminated, especially long trades.

## 2026-04-13 — Regime supervisor judges against original box when bot uses alternative box
- session: 2026-04-13_31367b51.md (lines 1723-2116)
- failure: When `using_alternative=True`, the signal engine trades against the new alternative box's PDH/PDL, but the regime supervisor still evaluates rejection-failed / box-acceptance against the ORIGINAL (broken) box. Result: regime double-counts risk and over-blocks legitimate alt-box trades, OR under-blocks bad ones because the wrong walls are being assessed.
- root cause: Architectural — regime module wasn't updated when alternative-box logic was added to the signal engine. Two different "boxes of truth" for the same instrument.
- affected: Any instrument in NEW_BOX_STANDBY / alternative-box state. USD_CHF, AUD_CAD, USD_MXN score=1 trades on V1 and V2 were all alternative-box trades — they got fake-valid scores near the floor.
- fix: Not fully applied in this session — diagnosis recorded. The score=1 floor pathway (Phase 3A) was the immediate band-aid; the structural fix (regime reads alternative_box when active) was flagged for follow-up.
- contaminated window: open as of 2026-04-13. Any alternative-box trade through this date should be treated as having scored against the wrong reference frame.

# Winning sessions / streaks (chronological)

## 2026-03-23 — V2 RESTRICTED-tagged winners: AUD_CAD and GBP_CAD / CAD_JPY
- session: 2026-03-23_fdc5d1f8.md → carried into 2026-03-24_2766c2e9.md (lines 3783, 4101, 4509)
- pair(s): AUD/CAD (+$2,564), GBP/CAD (+$463), CAD_JPY (+$2,627) on V2
- trades: 2-3 wins explicitly cited, no losses recorded for this window. AUD/CAD was the headline single-trade winner of the V1/V2 era.
- config context: V2 ~$88K practice account, post-3f14762e fix (new_stop bug repaired 03-24 evening, but these winners are 03-23 V2 which never had that bug). Regime supervisor live in observe-then-half-size mode. RESTRICTED entries still permitted at half size. Box drawing post-03-09 fix (anchored hourly slice, sanity guard active). Daily box mode (post-59e83b9 revert).
- backtest replay potential: HIGH — these are the canonical "the system works when boxes are right and regime is observant" trades. Replay AUD/CAD and CAD/JPY around 2026-03-23 15:00-18:00 UTC. Any candidate config should reproduce these or it's regressing. CAD-cross strength + USD weakness on 03-23 is the macro setup; the bot caught it three times.

## 2026-03-24 — V2 RESTRICTED net +$1,493 day despite AUD_JPY loss
- session: 2026-03-24_2766c2e9.md (line 3783)
- pair(s): AUD/CAD big winner from prior day still resolving + new V2 entries; AUD/JPY half-size loss -$1,071
- trades: 1 large winner +$2,564 vs 1 sized-down loser -$1,071 = net +$1,493
- config context: Same as 03-23. The "RESTRICTED saved $1,071" framing — regime sized AUD/JPY down to half because it was protesting; trade still lost but only half-bad. Demonstrates regime working AS INTENDED in observe-half-size mode.
- backtest replay potential: MEDIUM — single-trade outcome, not representative of a streak. Useful as a "regime sizing actually helps" validation point. A candidate config that turns AUD/JPY into a full-size loss here is worse.

## 2026-04-07 — V1 net +$74.17 / 5 winners + 1 SL hit
- session: 2026-04-07_d9c27471.md (lines 2250-2290)
- pair(s): AUD_JPY long +$27.98, NZD_USD short +$4.08, AUD_USD long +$5.09, NZD_USD short +$4.29, AUD_USD long +$46.92, AUD_CHF long -$14.19, GBP_USD short open at session end
- trades: 5 wins, 1 loss, 1 open. Net closed +$74.17 on ~$1,669 equity (~+4.4% day on closed P/L).
- config context: V1 live, 21 instruments scanned, harvester taking partials (AUD_USD #6 +$46.92 was harvester-driven through progressively higher sells). Power_of_towers signal dominant (5 of 7 trades). John_wick on 1. Post-3f14762e (new_stop fixed). Pre-04-09 TP clamp (so any absurd-TP bug would have shown up here — it didn't, suggesting these pairs had clean boxes that day). Box drawing on standard daily PDH/PDL.
- backtest replay potential: HIGH — best documented "good day" of the V1 era. The pair concentration (AUD, NZD, JPY antipodean complex) suggests this is a regime-fit day: clear directional flow in JPY-crosses + risk-on antipodean strength, both fading to the box edge. Replay 2026-04-07 04:00-22:00 UTC across these pairs. Any candidate config that doesn't also turn green here is worse than current.

## 2026-04-10 — V1 score>1 trades all winners (+$42.89 incl. open)
- session: 2026-04-10_54314085.md (lines 678-720, 2746)
- pair(s): GBP/USD +$8.52 (score 44), NZD/JPY +$2.14 (score 51), NZD/JPY open +$32.23 (score 31), AUD/CAD +$4.22 (score 1), USD/MXN -$40.41 (score 1)
- trades: 3 of 3 score>1 trades won; the 2 score=1 trades split (1 win, 1 large loss = -$36.19 net on score=1 subgroup). Net all = +$6.70 closed.
- config context: V1 live, post-04-09 TP clamp. Score floor of 1 in place. Regime active. The score=1 trades were ALL alternative-box trades (per 04-13 audit) — flagged as the contamination subset.
- backtest replay potential: HIGH for the "score is informative" hypothesis. The Score>1 cohort being clean wins and Score=1 being mixed-to-bad is a directly testable threshold. Replay with `signal.score >= 20` filter and confirm only the +$42.89 cohort enters. Don't replay USD/MXN — it's the contamination case, not a config signal.

## 2026-03-09 evening — All 4 open positions green (anecdotal, not closed)
- session: 2026-03-09_77af2792.md (line 3300, 2923-2937)
- pair(s): EUR/USD long, USD/JPY short, CAD/JPY short, CHF/JPY short
- trades: 4 open, all green simultaneously. Not a "closed wins" record, but a snapshot of correctly-aligned positioning AFTER the inverted-box fix. EUR/USD long was a pre-existing reconciled position.
- config context: Same evening as the iloc[:24] → iloc[-48:-24] fix. Trend filter tightened. Sanity guard live. Boxes now correctly drawn for the first time in the corpus.
- backtest replay potential: LOW — not enough closed-P/L data to anchor a backtest. Useful only as the "first clean post-bug state" boundary marker. Anything BEFORE this is in the contamination zone for inverted-box trades.

(Note: only ~5 strong winning-day records found in the corpus. Brock's recollection of "every trade won" sessions partially matches 03-23 V2 and 04-07 V1, but the corpus doesn't contain a true 100%-win day with >3 trades. The corpus is heavier on bug-fix narrative than on "good day" celebration. If more all-win days existed, they were either too uneventful to be discussed at length, or live in the V3 era / dashboard rather than session transcripts.)

# Synthesis

Two patterns dominate. **Box contamination is multi-vector**: the box can be (a) inverted from a stale-hourly-slice bug (03-09), (b) replaced by an experimental 12-hour rolling window (03-19/20), (c) shrunk too aggressively by the percentile filter (03-25 USD/CHF rejections), (d) reset at UTC midnight wiping accumulated negative signal (03-29 amnesia), (e) stale-snapshot-carried producing absurd TPs (04-09 7,883 pips), or (f) judged against the wrong reference frame when the alt-box is active (04-13). Each has a distinct contaminated window and distinct trade-pattern fingerprint.

**(a) EXCLUDE from any "live truth" backtest comparison:**
- Pre-2026-03-09: all EUR-pair longs (inverted-box era, unknown start).
- 2026-03-19 evening → 2026-03-20 afternoon (commit 59e83b9): all trades (30m experiment era).
- First ~2 hours of every UTC day from regime activation (~03-22 V2, ~03-31 V1) through 2026-03-29 hysteresis fix: any pair that was BLOCKED in prior 24h (amnesia window).
- 2026-03-31 → 2026-04-09: USD/CHF and GBP/CAD entries especially (stale-box absurd-TP era).
- Through 2026-04-13: all alternative-box trades, particularly score=1 entries (regime vs. alt-box mismatch).

**(b) BEST validation targets for proposed config changes:**
- **2026-04-07 (V1)** — the canonical good day. 5 winners on AUD/NZD/JPY antipodean complex. Any new config that doesn't also win here is worse.
- **2026-03-23 (V2)** — AUD/CAD +$2,564 and CAD/JPY +$2,627 on RESTRICTED tagging. Validates regime-sizing logic. Any config that turns these into losses or blocks them entirely is worse.
- **2026-04-10 (V1)** — score>1 cohort all winners. Validates score-as-filter hypothesis. Test that a minimum-score filter (≥20) preserves these wins while killing the score=1 USD/MXN -$40 loser.
