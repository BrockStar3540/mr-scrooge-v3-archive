# mr-scrooge-v2 — Master Notes

## Architecture Overview

```
mr-scrooge-v2/
├── config.py              ← All parameters (typed dataclass, env overrides)
├── alerts.py              ← Claudia + Frank outbox integration
├── coordinator.py         ← Main orchestrator (Phase 6)
├── main.py                ← Boot + systemd entrypoint (Phase 6)
│
├── health/                ← GREEN/YELLOW/RED per component, circuit breakers
│   ├── models.py          ← ComponentHealth, CircuitBreaker, HealthReport
│   └── monitor.py         ← HealthMonitor singleton
│
├── core/                  ← External API wrappers (Phase 2)
│   ├── oanda_client.py    ← REST client (extracted from v1 core/)
│   ├── execution_router.py
│   └── fee_calculator.py
│
├── universe/              ← Pair screening (Phase 3)
│   ├── screener.py        ← ForexUniverseScreener
│   └── session_windows.py ← Session schedule
│
├── zones/                 ← Magic-line zone detection (Phase 3)
│   ├── models.py          ← MagicLine, DailyBox, ZoneMap
│   └── detector.py        ← ZoneDetector
│
├── box/                   ← Box state machine (Phase 3)
│   ├── models.py          ← BoxState, BoxRecord
│   └── state_machine.py   ← BoxStateMachine
│
├── gates/                 ← Signal validation pipeline (Phase 4)
│   ├── models.py          ← BaseGate, GateResult, GatePipelineResult
│   ├── zone_gate/         ← Gate 1: price at magic line?
│   ├── trend_gate/        ← Gate 2: higher-TF trend alignment?
│   ├── atr_gate/          ← Gate 3: volatility adequate?
│   ├── sucker_move_gate/  ← Gate 4: false break detected?
│   ├── pitchfork_gate/    ← Gate 5: named candle signal?
│   └── otr_gate/          ← Gate 6: overhead-to-range ok?
│
├── signals/               ← Signal evaluation + ranking (Phase 5)
│   └── engine.py          ← SignalEngine
│
├── positions/             ← Open position management (Phase 5)
│   ├── models.py          ← Position dataclass
│   └── manager.py         ← PositionManager
│
├── sizing/                ← Position sizing (Phase 5)
│   └── calculator.py      ← margin-based sizing
│
├── experiments/           ← A/B testing framework (Phase 1 ✓)
│   ├── models.py          ← Experiment, VariantStats, TradeOutcome
│   └── tracker.py         ← ABTestingTracker singleton
│
├── dashboard/             ← Flask health + experiments UI (Phase 7)
│   └── templates/
│
├── data/                  ← Runtime state files
└── logs/                  ← Timestamped logs, decisions, trades, experiments
```

## Design Principles
1. **Each component knows its own health** — register + record on every call
2. **Circuit breakers** auto-disable failing components
3. **Gates** run in order; first failure stops pipeline — no silent passes
4. **A/B testing** is opt-in per gate; never influences production until proven
5. **JSONL logs** — append-only, timestamped, machine-parseable
6. **No dead code** — v2 is a clean slate, nothing carried from v1 unless used

## Build Status
| Phase | Contents | Status |
|-------|----------|--------|
| 1 | config, alerts, health, gates/models, experiments | ✅ Complete |
| 2 | core/ (oanda_client, execution_router, fee_calculator) | ✅ Complete |
| 3 | universe/, zones/, box/ | ✅ Complete |
| 4 | All 6 gate subfolders | ✅ Complete |
| 5 | signals/, positions/, sizing/ | ✅ Complete |
| 6 | coordinator.py + main.py | ✅ Complete |
| 7 | dashboard/ | 🔲 Future |

## Change Log
| Date | Phase | Description | Author |
|------|-------|-------------|--------|
| 2026-03-21 | 1 | Initial build — infrastructure + models | Claude Code |

---

## 2026-03-25 — Risk + Exit Architecture Overhaul (synced with V1)

All changes applied to both V1 and V2 simultaneously.

### Changes
1. **TP2 market-price guard** — `signals/engine.py` + `coordinator.py`
   - `_calculate_targets()` receives `current_price` (via `zone_map.current_price`)
   - Rejects if `tp2 <= current_price + 2_pips`
   - Pre-submit guard in `coordinator.py` re-validates before `router.enter_position()`

2. **Risk-capped sizing** — `config.py` + `coordinator.py`
   - New field: `max_risk_per_trade_pct: float = 0.04`
   - Applied in `fire_entry()` after `sizing.calculate()`: `units = min(units, risk_cap_units)`
   - Risk cap computed before regime halving and off-peak reduction

3. **Earlier breakeven** — `positions/manager.py` Stage 1
   - Trigger: +5 pips profit (was 50% of TP1)
   - SL: entry + 1 pip buffer

4. **Harvester tiers + BE-gate** — `harvester/harvester_config.json` + `harvester/main.py`
   - T1: 3%, T2: 5%, T3: removed. Runner = 50% (was 25%)
   - BE-gate: no harvesting until SL >= entry (longs) or SL <= entry (shorts)

5. **Conditional stagnant timeout** — `harvester/main.py`
   - 90 min + profit < T1 (was 6hr blanket)

6. **Adaptive ratchet lock** — `positions/manager.py` `_hybrid_trail()`
   - 55% pre-TP1, 75% post-TP1 (was fixed 80%)

### Updated Change Log
| Date | Phase | Description | Author |
|------|-------|-------------|--------|
| 2026-03-21 | 1 | Initial build — infrastructure + models | Claude Code |
| 2026-03-25 | 5-6 | Risk cap, TP2 guard, BE gate, harvester overhaul, adaptive ratchet | Claude Code |

---

## 2026-03-26 — sl_floor_pct Investigation + Fix

### Problem
V2 went silent for extended periods including the entire NY session on 2026-03-25. V1 showed
the same behaviour. Investigation showed all signal gates were passing — the only blocker was
`RR < 1.6` across every active pair throughout the session.

### Root Cause
`sl_floor_pct = 0.0050` (0.50%) was enforcing a minimum stop of ~54 pips on EUR pairs at 1.08.
This inflated the RR denominator, making 1.6x reward nearly unreachable on normal intraday
setups. Best pairs on the March 25 NY session (USD selloff / tariff news day): EUR_AUD and
EUR_NZD at RR 1.35 — 16% short of the minimum, all session long.

The floor had been raised from 0.30% → 0.50% at some earlier point ("too tight"), but the
overcorrection was the dominant constraint killing trade frequency.

### Fix
Lowered `sl_floor_pct` from 0.50% → 0.25% (`0.0025`) in `config.py`.
At EUR/USD 1.08 = ~27 pip minimum stop (was ~54 pips).

### Immediate Effect (2026-03-26 03:56 UTC)
First cycle after restart at 0.25%:
- **V2**: USD_JPY signal QUALIFIED — all gates passed, RR cleared 1.6 for the first time
- **V2**: REGIME_BLOCKED (score -4.0)
  - `box_acceptance_above(-2)`: 6 consecutive closes above PDH 159.181 — wall not holding
  - `rejection_failed(-2)`: 8.1w failed rejections at that wall in last 24H
  - **This is correct** — regime correctly identified the PDH wall had been failing all day.
    V1 (observer-only regime) took the same trade; V2 enforced the block. Watch V1's outcome
    over next few hours to validate whether the regime call was right.

### Monitoring
Watching next few days to confirm 0.25% floor isn't too loose. If stop-hit rate rises, step
back to 0.30%.

### Logging Bug Fixed (same session)
V2 decisions log was showing `sucker=False fork=False otr=False` even when gates passed and
RR was the only blocker. The `_no_trade()` call at the RR check wasn't forwarding preceding
gate kwargs — a display-only bug, no effect on trade decisions. Fixed in `signals/engine.py`.
Also: `signals/engine.py` was accidentally left as `.bak` from an editing session — bot was
running on stale `.pyc` cache and crashed on next restart. Restored from git HEAD.

### Updated Change Log
| Date | Description | Author |
|------|-------------|--------|
| 2026-03-21 | Initial build | Claude Code |
| 2026-03-25 | Risk cap, TP2 guard, BE gate, harvester overhaul, adaptive ratchet | Claude Code |
| 2026-03-26 | sl_floor_pct 0.50% → 0.25%; fix _no_trade logging bug; restore engine.py | Claude Code |

---

## 2026-03-31 — Data Analysis + Major Config Overhaul

### Background
After collecting trade data from March 29–31, we ran a full analysis of what was working and what
wasn't. Both bots were producing 43% WR with negative expectancy under the prior settings.

### Analysis Findings

**Best day: March 24**
- V2 was REGIME_BLOCKED on all losing setups (GBP_CAD, GBP_AUD, AUD_NZD, EUR_USD — all with
  7–10 week rejection failure chains)
- The one winning trade (AUD_CAD) had `box_contained(+1)` + `compression(+1)` = score +2
  (NORMAL). Price sitting quietly inside box + ATR compressed = highest-quality reversal setup.
- That is the setup the regime filter was designed to protect.

**Worst trades post-March 29**
- USD/MXN (V2): Regime BLOCKED 8+ times in a row (rejection_failed: 10.2 weeks).
  When price briefly touched PDH, box_acceptance cleared for one candle, score moved from -4
  to -2 (no longer BLOCKED under old rules), and V2 entered. Lost.
  Root cause: old threshold only blocked on BLOCKED state (score ≤ -3); RESTRICTED (score -2)
  was allowed through.
- EUR/USD (V2): Entered on regime score = 0 (CAUTION/neutral). EUR was in clear uptrend all
  day. Score 0 means no positive signals at all — nothing actually argued FOR a reversal.
  Root cause: no score floor, CAUTION was treated as acceptable.

**Simulation of fixes (127 trades, March 29–31 window)**
- Current settings: -$163.81 (43.3% WR)
- Regime proxy + balanced universe + original margin (0.50): +$32.04 (48.9% WR)
- Key driver: regime filter blocking the structural losers

### Changes Made

#### 1. Universe Mode → Aggressive (both bots)
- `universe_mode: 'aggressive'` — all 26 CANDIDATE_PAIRS scanned every cycle, all sessions
- Removed: `apply_probation_size`, `probation_size_multiplier` — static probation list replaced
  by dynamic regime scoring. Probation pairs still defined in code but have no special treatment.

#### 2. Harvester Tiers Restored (both V1 + V2 harvesters)
Original ORIGINAL_CONFIG.md tiers restored. Previous tiers (3.0/5.0/7.0%) were too wide —
trades were getting stopped out before ever reaching T1.

| Tier | Old | New | Action |
|------|-----|-----|--------|
| T1 | 3.0% equity | **1.5% equity** | Close 25%, SL stays |
| T2 | 5.0% equity | **3.0% equity** | Close 25%, SL → +1.5% |
| T3 | 7.0% equity | **4.5% equity** | Close 25%, SL → +3.0% |
| Runner | 25% | **25%** | Rides to TP2 (OANDA native) |

Files changed: `harvester/main.py` (V1), `mr-scrooge-v2/harvester/main.py` (V2)

#### 3. Spread Consistency Gate (both bots)
Old: spread exceeding threshold on any single scan → entries immediately paused.
New: spread must exceed threshold on **2 consecutive scans** (10 minutes) before pausing.
Prevents single-candle spread spikes (common in Sydney/Sunday) from blocking valid setups.

Files changed: `gates.py` (V1), `mr-scrooge-v2/box/models.py` + `box/state_machine.py` (V2)

#### 4. Regime Score Floor (both bots)
Old: only BLOCKED state (score ≤ -3) suppressed entries. RESTRICTED and CAUTION allowed through.
New: entry requires **score ≥ +1**. CAUTION (score = 0) = wait. At least one positive signal
must be present.

Log tag: `REGIME_FLOOR` when blocked due to score < +1 with no recent bad history.

#### 5. Regime Hysteresis (both bots)
New: if regime score was ≤ -2 (RESTRICTED or BLOCKED) in either of the last 2 scans (10 min),
entry is still blocked even if current score has improved, until score ≥ +1 is confirmed.

Log tag: `REGIME_HYSTERESIS` distinguishes recoveries from clean floor blocks.
Implemented via `_last_regime_scores` per-symbol deque (maxlen=2).

Addresses the USD/MXN incident where a one-candle improvement in box_acceptance allowed
entry into a 10-week rejection-failure regime.

#### 6. V1 Regime Filter Activated
V1 was observer-only — it logged "protests" but never blocked anything.
V1 regime is now an **active blocker**, using the same logic as V2:
- BLOCKED → suppress entry
- Score < +1 → suppress entry (score floor)
- RESTRICTED → halve position size (trade allowed)

Files changed: `main.py` (V1)

### Current Settings Summary (both bots)

| Parameter | V1 | V2 |
|-----------|----|----|
| margin_utilization_pct | 0.80 | 0.80 |
| max_concurrent_positions | 1 | 1 |
| universe_mode | aggressive | aggressive |
| probation_size_multiplier | removed | removed |
| regime filter | **ACTIVE** (was observer-only) | active |
| regime entry threshold | score ≥ +1 | score ≥ +1 |
| regime hysteresis | 2-scan lookback | 2-scan lookback |
| spread gate | 2 consecutive scans | 2 consecutive scans |
| T1 harvester | 1.5% equity | 1.5% equity |
| T2 harvester | 3.0% equity | 3.0% equity |
| T3 harvester | 4.5% equity | 4.5% equity |

### What to Watch
- Regime log tags: `REGIME_BLOCKED`, `REGIME_RESTRICTED`, `REGIME_FLOOR`, `REGIME_HYSTERESIS`
  in `logs/decisions.log` — confirm they're firing on the expected pairs
- Trade frequency may drop initially as the score floor filters CAUTION setups
- If WR improves but frequency drops too much, consider whether score ≥ 0 is sufficient
  (removing the floor) while keeping hysteresis
- Harvester: T1 at 1.5% should trigger much earlier — watch `harvester/logs/harvests.log`

## 2026-04-03 — Fast Execution Loop + Dashboard Regime Visibility

### Changes Made

#### 1. Pair Execution Profiles (both bots)
Added `_PAIR_PROFILE` dict with per-pair tuned parameters for the hybrid SL limit and green exit
systems. Three tiers based on observed spread/wick behaviour:

| Tier | Pairs | Trig (pips) | Offset | Fallback | Fast Mult | Green Offset |
|------|-------|-------------|--------|----------|-----------|--------------|
| tight | EUR_USD, AUD_USD, EUR_CAD | 2 | 1.0 | 3.0 | 2.5x | 0.5 |
| medium | GBP_USD, USD_JPY, NZD_USD, USD_CHF, USD_CAD, EUR_JPY | 4 | 1.5 | 5.0 | 2.0x | 1.0 |
| wide | GBP_JPY, CHF_JPY, NZD_JPY, AUD_JPY, AUD_CHF | 6 | 2.0 | 7.0 | 1.8x | 1.5 |

Files changed: `coordinator.py` (V2), `main.py` (V1)

#### 2. Hybrid SL Limit System (both bots)
Proactive REDUCE_ONLY limit order placed when price approaches stop within `trigger_buffer` pips.
OANDA native SL kept as hard backstop. Full lifecycle: fill check, ratchet cancel, fallback,
placement. Fast market detection skips limit placement when candle range ≥ `fast_mult × avg`.

Key fields added to `OpenPosition`:
`sl_limit_order_id`, `sl_limit_price`, `sl_limit_active`, `sl_limit_attempted`,
`sl_limit_filled`, `sl_limit_pips_saved`, `sl_fallback_used`, `last_sl_price`

Files changed: `positions/models.py` (V2), `portfolio/trade_manager.py` (V1),
`coordinator.py` (V2), `main.py` (V1)

#### 3. Green Exit → Limit Order (both bots)
Hourly green exit now places a REDUCE_ONLY limit at `bid - green_offset_pips` (long) or
`ask + green_offset_pips` (short) with 300s expiry. Falls back to market on failure or
fast market. Green exit guard: skips if `sl_limit_active = True`. Only fires when no
stop-ratchet action pending this cycle (move_stops take priority).

Files changed: `positions/manager.py` (V2), `portfolio/trade_manager.py` (V1),
`coordinator.py` (V2), `main.py` (V1)

#### 4. Fast Execution Loop — 3-second daemon thread (both bots)
Dual-loop architecture: 5-min loop handles decisions, 3-sec loop handles SL limit
placement and fill monitoring (`manage_open_positions_fast` / `_fast_loop_body`).

Implementation:
- `threading.Lock` (`_exec_lock`) prevents race conditions between loops
- `_cached_bars` dict stores latest `bars_5m` from slow loop; fast loop reuses without refetch
- Fast loop fetches live prices via single batch `get_prices(symbols)` call per cycle
- Position loop in slow loop wrapped with `with _exec_lock:`
- Dead position guard: existence check before `_manage_sl_limit` in fast loop
- Log tag: `[FAST_LOOP]` on thread start and errors

Files changed: `coordinator.py` (V2), `main.py` (V1)

#### 5. Regime Visibility on Dashboard (V1 dashboard + both bots)
Before: regime blocked entries silently — dashboard showed `ENTER_SHORT`/`ENTER_LONG` with
no indicator. Signal card had blue glow, box card had no banner.

After: at all three regime block points (BLOCKED, FLOOR, HYSTERESIS), the bot now:
- Sets `signal.action` to `'REGIME_BLOCKED'`, `'REGIME_FLOOR'`/`'REGIME_HYSTERESIS'`
- Sets `signal.wait_for` with score + reason detail
- Writes to `_blockers[symbol]` with full message (feeds both signal card and box card banners)

Dashboard changes:
- `actionCls` = `'fail'` (red) for any `action.startsWith('REGIME_')`
- Blue `ready-card` glow suppressed for regime-blocked cards
- Badge shows `REGIME_BLOCKED` directly (no `READY —` prefix)
- Red blocker banner shown on both signal card and box card

Files changed: `main.py` (V1), `coordinator.py` (V2), `dashboard.html` (V1 only — V2 has no
separate dashboard UI)

### Architecture Note
System is now dual-loop: candle-based decisions (5 min) + real-time execution (3 sec).
This is the same pattern used in professional trading systems. The lock prevents simultaneous
`_manage_sl_limit` calls from both loops on the same position.

### What to Watch
- `[FAST_LOOP] Execution thread started` in logs on each restart ✓
- `[FAST_LOOP] error:` lines — indicates API issues in the fast loop
- Dashboard: regime-blocked pairs now show red `REGIME_BLOCKED` badge and blocker banner
- SL limit events: `SL limit placed`, `fallback triggered`, `skipped (fast market)` in logs
- Lock contention: if slow loop feels sluggish, fast loop may be holding lock too long


### Session 2026-04-03 — Cleanup Pass
- `alerts.py`: Already routed to Frank outbox (done in prior session). Confirmed clean.
- `harvester/start.sh`: hardcoded `mr_burns_env` path replaced with `mr_scrooge_env` symlink.
- Ghost agent references (Burns, Wonderful, Sprite) purged from workspace-wide docs.
- No logic changes. V2 confirmed active.

---

## 2026-04-09 — OANDA Audit + Scoring Recalibration

### What happened
Two independent OANDA API audits pulled all trade data and cross-referenced with
H1 candle context. Found: scoring system inversely correlated with outcomes,
ranging markets (not counter-trend) are the #1 killer, P/L calculation wrong
for non-USD-quote pairs.

### Changes applied
- **Scoring Layer 4**: ranging -20, CT+PoT -15, CT+JW -5, CT T1 -10, CT T2 +5, z-align +5
- **Signal reweighting**: john_wick +15 (was +10), power_of_towers +5 (was +10)
- **Regime scoring**: NORMAL +10, CAUTION/RESTRICTED -10 (in coordinator.py)
- **R:R scoring**: Uses TP1 (realistic target). Hard gate still uses TP2.
- **Score floor**: min=1 for gate-passed signals (prevents regime penalty from zeroing)

### Bug fixes
- _calc_pnl: quote currency → USD conversion via pip_value_per_unit
- overhead_cost_usd: same conversion
- OANDA 404 fallback: transactions API for closed trade P/L recovery
- TP2 clamped to 3x ATR
- RotatingFileHandler (10MB, 5 backups) + propagate=False on child loggers

### Files modified
signals/engine.py, signals/models.py, gates/trend_gate/gate.py, coordinator.py,
positions/manager.py, positions/models.py, core/oanda_client.py, config.py, main.py

### Data
Audit data saved to data/audit/. Full findings in data/audit/AUDIT_FINDINGS_20260409.md

## 2026-04-09 — Dashboard Integration

### What happened
V2 dashboard created as independent service on port 8084 (V1 on 8081).
Dashboard was empty because V2's data pipeline wasn't feeding the HTML
the same data format V1 produces.

### Fixes applied
- Signal serialization: rich gate objects (zone.tier/details, atr.consumed_pct, otr.ratio, pitchfork.type)
- Score detail: _sd dict tracking in _score(), stored on SignalResult
- Signal evaluation: runs even at max_positions (for dashboard visibility)
- Box states: expanded to all initialized instruments, not just viable
- Sessions: initialized at boot (not just on hour change)
- Screen results: all 12 fields serialized (was 7)
- Market summary: built from validity_detail (V1-compatible)
- Stale screen cache: _update_sessions now updates _last_screen

### V1 bug found
_update_sessions() rescanned universe but forgot to update _last_screen.
Dashboard showed stale Sydney spreads even after bot found 10+ viable instruments.
Fixed with one line: ctx['_last_screen'] = _serialize_screen(screen_results)

### Key lesson
V1 and V2 share NO code, NO services. Separate dashboards, separate git repos,
separate GitHub tokens, separate Alien Device remotes. The only shared resource
is the Python venv symlink.

## 2026-04-10 — 4-Actor Trade Coordination (Phase 1)

### What changed
- New core/trade_state.py: TradeCoordinator class for cross-process state
- coordinator.py: Register trades, mark dead, alive gate in fast loop, sl_owner check, tiers_hit sync, no_position fix
- harvester/main.py: Alive gate, tier updates to coordination file, SL ownership handoff
- oanda_client.py: Detect NO_POSITION_TO_REDUCE (fixes spam bug)

### Why
4 actors modifying same OANDA trade with no shared state. Same issues as V1.

### Watch for
- Same as V1. Coordination file: data/trade_coordination.json

## 2026-04-10 — Phase 3A: Entry Safety Gates

### What changed
- coordinator.py: Added 4 hard gates before entry candidate ranking
- config.py: Added min_entry_score=20, spread_hard_block_ratio=3.0, stale_trigger_atr_fraction=0.3
- Same gates as V1: score, spread, freshness, distance

### Watch for
- Same as V1. Grep decision logs for SCORE_BLOCKED, SPREAD_BLOCKED, TRIGGER_STALE, TRIGGER_FAR

## 2026-04-12 — V1/V2 Convergence + Beta Epoch

### What changed
- coordinator.py: Fixed session indicator frozen since boot (added _update_sessions call). Added bar cache fallback for OANDA 502s. Filtered box_states to active_instruments only. Added _bar_cache init.
- signals/engine.py: Enforced validity_detail schema on ALL signals (pass and reject). Added _store_validity method. Added setup_type classification. Fixed RR rejection message format.
- signals/extreme_reversal.py: Fixed logger from mr-scrooge to mr-scrooge-v2.
- zones/detector.py: Deleted dead stub code block (lines 695-721) with leaked V1 logger.
- regime/supervisor.py: Merged correlation map — full 26-pair universe with _MAX_BREADTH_PEERS=4 cap.

### Why
Dashboard comparison revealed 6 code-level divergences between V1 and V2:
1. Session indicator frozen at boot value (New York shown on Sunday night)
2. Correlation map only covered AUD/NZD/JPY — missing EUR/GBP/USD majors
3. Market summary always 0/0 — validity_detail not populated on rejected signals
4. Box States showed all 26 pairs instead of viable only
5. Two V1 logger names leaking into V2 logs
6. OANDA 502 errors caused pair skipping with no fallback

### Context from investigation
- Manual USD/JPY deep-dive exposed that the alternative box (session_cheat_code) may not align with the Master Theory. The theory says box = prior day high/low. The alt box uses session range after breach. Not enough post-fix data to judge — jury is out.
- V2 practice API (api-fxpractice.oanda.com) returns 502s intermittently. Bar cache fallback prevents pair skipping but uses stale data. Monitor for accuracy impact.
- Parity harness running as systemd service. Known benign mismatches: BB position near 0.85 threshold causes 4-8 point score deltas, NO_TRADE signals still have validity_detail=None (only ENTER signals populate it).
- Pre-beta data archived. Beta epoch: 2026-04-13 02:41 UTC.

### Open questions (same as V1)
1. Alternative box edge — needs 100+ clean trades
2. USD_MXN — choked, observe during beta
3. Win/loss asymmetry — need 75%+ win rate for net positive
4. NO_TRADE validity_detail gap — parity harness flags these as CRITICAL but they're harmless. Fix later if it creates noise.

### Watch for
- Parity harness: ~/parity_harness/parity.log
- OANDA 502s: grep for using cached bars — if frequent, practice API may need monitoring
- Validity mismatch on NO_TRADE signals (known gap, not urgent)
