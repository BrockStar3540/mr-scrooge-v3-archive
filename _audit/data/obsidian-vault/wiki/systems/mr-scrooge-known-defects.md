# Mr. Scrooge Known Defects

type: system
status: active
tags: [scrooge, trading, defects, quality]

trust:
  score: 90
  confidence: high
  evidence:
    - source: code review + production trade analysis 2026-04-07/09
      type: firsthand

## Summary
Tracked defects found during the 2026-04-07 postmortem (Trade 4 GBP_USD -$65 loss on V1, -$2,031 on V2) and 2026-04-09 incident (AUD/CHF SL limit spam). Three HIGH-severity defects remain open. Defects 7-12 found and fixed during the 2026-04-09 scoring recalibration.

## Defect Table

| # | Severity | Status | Summary | File:Line |
|---|----------|--------|---------|-----------|
| 1 | HIGH | OPEN | Counter-trend override has no memory | `gates.py:1620-1631` |
| 2 | HIGH | OPEN | box_contained lookback too short (30min) | `regime/supervisor.py:47,230-236` |
| 3 | HIGH | OPEN | No daily same-zone entry cap | `main.py:1090-1102` |
| 4 | MED | FIXED | SL limit 404 loop / immediate fill spam | `main.py:255-350` |
| 5 | LOW | OBSERVATION | No market-wide caution signal | N/A |
| 6 | MED | FIXED | RegimeAssessment.detail AttributeError | `main.py:1072` |
| 7 | MED | FIXED | P/L calculation wrong for non-USD-quote pairs | V1: `trade_manager.py:721`, V2: `positions/manager.py:360` |
| 8 | LOW | FIXED | Overhead cost in quote currency not USD | V1: `main.py:1331`, V2: `coordinator.py:1045` |
| 9 | MED | FIXED | OANDA 404 on closed trade fetch (V1 live) | V1+V2: `core/oanda_client.py:260` |
| 10 | CRITICAL | FIXED | Scoring inversely correlated with outcomes | V1: `gates.py`, V2: `signals/engine.py` |
| 11 | MED | FIXED | TP2 absurd values from stale box data | V1: `gates.py:2578`, V2: `signals/engine.py` |
| 12 | LOW | FIXED | Duplicate log handler (propagate=True) | V1: `main.py:70`, V2: `main.py:24` |

## Defect Details

### Defect 1 [FIXED 2026-04-13]: Counter-Trend Override No Memory (OPEN)
Tier 1/2 zones unconditionally pass against the trend (`gates.py:1620-1631`). The override has zero memory of how many times the same zone has already failed to reverse. Trade 4 on 2026-04-07 was the 3rd short at PDH in one day — first two only hit TP1 partials (reversal never materialized to TP2), but the bot happily entered a 3rd time.

**Recommended fix:** Decay zone strength after repeated touches. Factor in how many counter-trend entries have failed to reach TP2 today.

**Note:** Partially addressed by scoring Layer 4 (CT penalties reduce re-entry attractiveness at Tier 1 zones).

### Defect 2 [FIXED 2026-04-13]: box_contained Lookback Too Short (OPEN)
`_ACCEPTANCE_LOOKBACK = 6` in `regime/supervisor.py:47` — only 30 minutes of M5 candles. Price dipping briefly inside the box resets the window to +1.0 (minimum to enter). At 17:02 UTC on 2026-04-07, GBP_USD scored +1.0 despite pressing PDH for 9 hours. Post-breakout at 20:02, the score dropped to -5.0. Regime only caught the problem after the SL hit.

**Recommended fix:** Increase lookback or add a daily zone-touch counter that penalizes repeated approaches.

**Note:** Partially addressed by scoring Layer 4 (CT penalties reduce re-entry attractiveness at Tier 1 zones).

### Defect 3 [FIXED 2026-04-13]: No Daily Same-Zone Entry Cap (OPEN)
Zone debounce is 20 minutes, TP cooldown is 15 minutes. The `max_reentries_per_setup` counter in `trade_manager.py:575` only tracks break-even stop re-entries — normal fresh signal entries do NOT increment it. The bot can short the same zone unlimited times per day via normal signal flow.

**Recommended fix:** Add a daily cap on fresh signal entries at the same pair+direction+zone.

**Note:** Partially addressed by scoring Layer 4 (CT penalties reduce re-entry attractiveness at Tier 1 zones).

### Defect 4: SL Limit Order Spam (FIXED 2026-04-09)
Three stacking bugs in `_manage_sl_limit()`. See [[SL Limit Order System]] for full details. Fixed via: early return on `sl_limit_filled`, ERROR state handling, return after cancel clear. **Fixed in both V1 (main.py) and V2 (coordinator.py)** — V2 had the same bugs in the same function, just in a different file.

### Defect 5: No Market-Wide Caution Signal (OBSERVATION)
When 0 out of 7+ viable pairs have clean setups (all blocked or RR-rejected), the bot scraped the bottom of the barrel and took the only trade that squeaked through gates. A meta-signal: when every other pair is blocked, conditions are unfavorable.

### Defect 6: RegimeAssessment.detail AttributeError (FIXED 2026-04-07)
`main.py:1072` referenced `regime_assessment.detail` which doesn't exist on `RegimeAssessment`. The correct accessor is `.summary()`. Individual `RegimeSignal` objects have `.detail`, not the top-level assessment. Was causing unhandled errors every 5-min cycle for regime-blocked pairs.

### Defect 7: P/L Calculation Wrong for Non-USD-Quote Pairs (FIXED 2026-04-09)
P/L calculation assumed all pairs had USD as the quote currency. For pairs like EUR_GBP or AUD_CHF, the realized P/L was reported in the quote currency (GBP, CHF) without conversion to USD. Dashboard and logs showed incorrect dollar amounts for these trades.

### Defect 8: Overhead Cost in Quote Currency Not USD (FIXED 2026-04-09)
Spread/commission overhead calculation used raw pip values without converting to USD for non-USD-quote pairs. The effect was minor (cost estimates off by ~5-15%) but compounded over many trades in the quality scoring system.

### Defect 9: OANDA 404 on Closed Trade Fetch (FIXED 2026-04-09)
When fetching a trade that had already been closed by OANDA (SL/TP hit between cycles), the client returned a 404 that bubbled up as an unhandled error. Fixed by catching 404 responses and treating them as "trade closed externally" rather than an error condition.

### Defect 10: Scoring Inversely Correlated with Outcomes (FIXED 2026-04-09)
The original scoring system assigned higher scores to signals that historically lost more money. Analysis of 511 V1 trades and 58 V2 trades revealed the correlation was inverted: top-scored entries had the worst P/L, while low-scored entries performed best. Complete scoring recalibration was required. See [[Mr. Scrooge Scoring Inversion Postmortem]].

### Defect 11: TP2 Absurd Values from Stale Box Data (FIXED 2026-04-09)
When box boundaries hadn't been refreshed (stale PDH/PDL from a prior day or session), TP2 calculations produced unreachable target prices (e.g., 300+ pips away on a 10-pip SL setup). Fixed by validating TP2 distance against ATR and capping at a configurable multiple of SL distance.

### Defect 12: Duplicate Log Handler (FIXED 2026-04-09)
Logger had `propagate=True` which caused every log line to appear twice — once from the handler and once propagated to the root logger. This was a cosmetic issue noted in MEMORY.md as "pre-existing issue with duplicate log handlers." Fixed by setting `propagate=False` on the bot's logger.


### Defect 13: Dead Config Values sl_pips/tp1_pips/tp2_pips (FIXED 2026-04-09, V1 only)
V1's CONFIG dict contained `sl_pips: 10`, `tp1_pips: 10`, `tp2_pips: 30` which were never used — SL/TP are zone-anchored. Removed from V1 CONFIG to eliminate confusion. V2 retained them because the disabled probe system (`probes/engine.py`) references `self.config.sl_pips` at import time — removing them would crash V2 on startup even though probes are disabled.


## Defects Found/Fixed 2026-04-14

### Harvester crash (FIXED)
- trade_state.py mark_dead() used bare `client_id` instead of `"client_id"` string
- Caused 1900+ NameError crashes over 16 hours, zero profit harvesting
- Fixed: quoted string in dict.get()

### SL execution timing (FIXED)
- Hybrid trail calculated SL from mid-price, OANDA triggers shorts on ask
- During wide spreads (13-16p on JPY), SL placed inside spread → instant fill
- Fixed: 4 guardrails in execution_router.move_stop (trigger-side, spread kill, no-man's zone, side-aware)

### TP1 lost on restart (FIXED)
- Reconciliation set TP1=0.0 because OANDA doesn't store TP1 natively
- Ratchet/BE ran blind without TP1 anchor (5-pip fallback only)
- Fixed: TP1 persisted in trade_coordination.json, recovered on reconcile

## Related
- [[Mr. Scrooge V1]]
- [[Mr. Scrooge V2]]
- [[SL Limit Order System]]
- [[Mr. Scrooge Architecture]]
- [[Mr. Scrooge Scoring Inversion Postmortem]]

### Defect 14: SL Limit Spam on Dead Positions (FIXED 2026-04-10)
After the harvester closed a position's final partial, the SL-limit fast loop (3-sec thread) continued placing opposing limit orders for the dead trade. OANDA rejected each with NO_POSITION_TO_REDUCE but the bot retried every 3 seconds for up to 5 minutes (46+ wasted API calls per dead trade). Root cause: place_opposing_limit returned success=True even on immediate cancel. Fixed in oanda_client.py (detect orderCancelTransaction) and main.py/_manage_sl_limit (mark position done on no_position). Also added cross-process TradeCoordinator with alive gate. See [[Trade Coordination Protocol]].

### Defect 15: Score=1 Entries With Full Position Sizing (FIXED 2026-04-10)
Regime CAUTION penalty (-10) pushed scores to the floor (1) but the bot still entered with full margin-based position sizing. Trade audit: score=1 USD/MXN lost -$40.41 (V1) and -$940.54 (V2). Fixed with Phase 3A safety gates: minimum score >= 20, spread hard-block (ratio > 3.0), trigger freshness (already broken), stale trigger distance (> 0.3 ATR_5m).

### Defect 16: Ratchet/Harvester SL Race Condition (FIXED 2026-04-10)
Ratchet (5-min loop) and harvester (30-sec daemon) both modified the same trade's stop loss independently, with different target prices. Result: contradictory stop movements and hidden P/L distortion. Fixed via TradeCoordinator sl_owner protocol — harvester owns SL during T1-T3 partial phase, ratchet takes over after handoff. See [[Trade Coordination Protocol]].

### Defect 17: V2 Session Indicator Frozen Since Boot (FIXED 2026-04-12)
V2's coordinator.py defined _update_sessions() but never called it in the run loop. Sessions were set once at boot time and never updated. If the bot booted during New York hours, the dashboard permanently showed New York as active regardless of actual time. Fixed by adding self._update_sessions(now) call in the main loop before universe rescan.

### Defect 18: V1/V2 Correlation Map Divergence (FIXED 2026-04-12)
V1's regime breadth signal only covered EUR/GBP/USD majors. V2 only covered AUD/NZD/JPY crosses. Since both bots scan the same 26-pair universe, breadth_negative fired on V1 for EUR_USD but never on V2 (and vice versa for AUD pairs), causing consistent 1-point regime score differences. Fixed by merging both maps into a unified 17-pair correlation map in both bots, with _MAX_BREADTH_PEERS=4 cap to control trigger frequency.

### Defect 19: V2 Market Summary Always Showing 0/0 (FIXED 2026-04-12)
V2's signal engine only populated validity_detail on passing signals. Rejected signals had no validity_detail dict, so status.py's market_summary always reported 0 valid candidates and 0 rejected. Dashboard Signals tab showed No classified setups. Fixed by enforcing a strict validity_detail schema contract on ALL signals (pass and reject), including setup_type classification, invalid_reasons list, and per-check boolean status.

### Defect 20: V2 Box States Showing All 26 Pairs (FIXED 2026-04-12)
V2's coordinator iterated self.box_machine.states.keys() (all tracked boxes) instead of self.active_instruments (viable pairs only). Dashboard Box States tab showed 26 cards vs V1's ~11. Fixed by matching V1's pattern — only render boxes for active/viable instruments.

### Defect 21: V1 Logger Names Leaking Into V2 Logs (FIXED 2026-04-12)
Two V2 files used V1's logger namespace: zones/detector.py had a dead code stub with getLogger('mr-scrooge'), and signals/extreme_reversal.py used getLogger('mr-scrooge.extreme_reversal'). Fixed by deleting the dead stub block and renaming the extreme_reversal logger to 'mr-scrooge-v2.extreme_reversal'.

---

## Beta Epoch — 2026-04-13 02:41 UTC

All pre-beta data archived. Defects 17-21 are fixed. Logs cleared for clean data collection on the converged codebase (Phase 3A + 4-actor coordination + V1/V2 convergence fixes). The parity harness (parity-harness.service) now continuously monitors for regression.

Open items carried forward into beta observation:
- Alternative box (session_cheat_code) alignment with Master Theory — see [[Mr. Scrooge Alternative Box Analysis]]
- USD_MXN effectively choked by spread/OTR/score gates — observe whether it should be removed from universe entirely
- NO_TRADE validity_detail gap in V2 (cosmetic, causes parity harness false CRITICALs)
