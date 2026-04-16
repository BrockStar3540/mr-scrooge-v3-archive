# V3 Developer Log

> Main timeline of all changes. Each entry is a brief with a pointer to the module log for full details.
>
> Format: `[DATE] [MODULE] — one-line summary -> logs/modules/MODULE.md`

---

## 2026-04-14 — Project Bootstrap

- `[2026-04-14] [core/types]` — Initial type definitions: ModuleMode, GateMode, AdvisorMode, HealthColor, MarketSnapshot, SymbolContext, TradeCandidate, GateResult, OrderPlan, StopPlan, PositionState, AdvisorResult -> [logs/modules/core-types.md](modules/core-types.md)
- `[2026-04-14] [core/contracts]` — All 7 Protocol contracts: FeatureModule, ClassifierModule, StrategyModule, GateModule, ExecutionPolicy, AdvisorModule, HealthCheckModule -> [logs/modules/core-contracts.md](modules/core-contracts.md)
- `[2026-04-14] [core/events]` — Typed event bus with 19 pre-defined event types, subscribe/emit pattern, global handlers for audit -> [logs/modules/core-events.md](modules/core-events.md)
- `[2026-04-14] [core/registry]` — Module registry with mode switching, health summary, active/disabled filtering -> [logs/modules/core-registry.md](modules/core-registry.md)
- `[2026-04-14] [core/state]` — Centralized state store: SymbolState, TradePositionState, CooldownState, snapshot/persist/restore -> [logs/modules/core-state.md](modules/core-state.md)
- `[2026-04-14] [core/config]` — Hierarchical config store with dot-path access, JSON-backed persistence -> [logs/modules/core-config.md](modules/core-config.md)
- `[2026-04-14] [docs]` — BLUEPRINT.md, MASTER_THEORY.md (Part I source theory + Part II engineering), THEORY_TO_CODE.md, V2_MASTER_THEORY.md reference copy -> [logs/modules/docs.md](modules/docs.md)

## 2026-04-15 — Historical Lessons Audit

- `[2026-04-15] [gates/entry_confirmation]` — 5 lessons from V1/V2: stop placement, trigger prices, timeframe switching, SL floor, signal type profitability -> [logs/modules/gates-entry-confirmation.md](modules/gates-entry-confirmation.md)
- `[2026-04-15] [gates/directional_pressure]` — 2 lessons: flexible candle window, termination proximity -> [logs/modules/gates-directional-pressure.md](modules/gates-directional-pressure.md)
- `[2026-04-15] [gates/overhead_ratio]` — 1 rule: OTR thresholds with tier interaction -> [logs/modules/gates-overhead-ratio.md](modules/gates-overhead-ratio.md)
- `[2026-04-15] [gates/zone_proximity]` — 1 rule: JPY 2x proximity -> [logs/modules/gates-zone-proximity.md](modules/gates-zone-proximity.md)
- `[2026-04-15] [gates/trend_filter]` — 2 lessons: EMA calibration, tier-aware blocking -> [logs/modules/gates-trend-filter.md](modules/gates-trend-filter.md)
- `[2026-04-15] [gates/atr_budget]` — 1 rule: advisory only -> [logs/modules/gates-atr-budget.md](modules/gates-atr-budget.md)
- `[2026-04-15] [gates/spread]` — 2 lessons: 2-scan consistency, spike definition -> [logs/modules/gates-spread.md](modules/gates-spread.md)
- `[2026-04-15] [features/zone_detector]` — 6 lessons: rolling box failure, percentile filter, zone width, min touches, alt range warning, stale TP2 -> [logs/modules/features-zone-detector.md](modules/features-zone-detector.md)
- `[2026-04-15] [classifiers/regime]` — 6 lessons: score floor, hysteresis, NORMAL=edge, lookback bug, scoring integration, size halving -> [logs/modules/classifiers-regime.md](modules/classifiers-regime.md)
- `[2026-04-15] [strategies/scoring]` — 10 lessons: scoring inversion, ranging killer, CT tier analysis, TP1 predictor, z-score, sub-30min trades, validation rules, score=1 bug, CT memory, zone cap -> [logs/modules/strategies-scoring.md](modules/strategies-scoring.md)
- `[2026-04-15] [execution/stop_planner]` — 3 lessons: hybrid SL, trigger-side bug, dead position spam -> [logs/modules/execution-stop-planner.md](modules/execution-stop-planner.md)
- `[2026-04-15] [execution/entry_planner]` — 4 lessons: TP2 guard, safety gates, fill reconciliation, RR sanity -> [logs/modules/execution-entry-planner.md](modules/execution-entry-planner.md)
- `[2026-04-15] [execution/sizing]` — 3 lessons: JPY formula bug, risk cap, probation removal -> [logs/modules/execution-sizing.md](modules/execution-sizing.md)
- `[2026-04-15] [management/position]` — 8 lessons: BE trigger, ratchet lock, peak tracking, 4-actor race, TP1 persistence, harvester crash, SL-only management, WR asymmetry -> [logs/modules/management-position.md](modules/management-position.md)
- `[2026-04-15] [broker/oanda]` — 4 lessons: P/L currency bug, 404 fallback, 502 cache, margin rates -> [logs/modules/broker-oanda.md](modules/broker-oanda.md)
- `[2026-04-15] [architecture]` — 6 lessons: dual-loop, 4-actor coordination, code isolation, broker-API truth, session freeze, log duplication -> [logs/modules/architecture.md](modules/architecture.md)
- `[2026-04-15] [telemetry/quality]` — 4 lessons: MFE/MAE ratio, follow-through score, entry context fields, quiet trades discovery -> [logs/modules/telemetry-quality.md](modules/telemetry-quality.md)
- `[2026-04-15] [dashboard]` — 9 lessons from V1/V2: market summary 0/0, box states all 26, session frozen, false CRITICALs, no zone re-entry visibility, P/L wrong, silent bug invisible, security posture, status.json contract -> [logs/modules/dashboard.md](modules/dashboard.md)

## 2026-04-15 — Trade Math, Recipe Analysis, and V3 Scoring Formula

- `[2026-04-15] [docs/TRADE_MATH]` — First-principles parameter coupling analysis: SL floor tied to wrong reference frame, RR gate using fantasy target, unified viability check proposed
- `[2026-04-15] [docs/TRADE_RECIPE]` — Reverse-engineered winning trade recipe from 50 raw OANDA trades: 10 ingredients scored, 5 new discoveries, 5 confirmed findings
- `[2026-04-15] [docs/SCORING_REVIEW]` — Old vs new scoring: 50 pts of dead weight identified (OTR, RR, ATR consumed), redistribution to conviction, wall proximity, BB middle
- `[2026-04-15] [docs/FACTOR_BIBLE]` — 31 factors with full distribution buckets, win rates, and scoring recommendations from raw OANDA data
- `[2026-04-15] [docs/MASTER_FINDINGS]` — 43 factors in 4 tiers: 10 new discoveries, 6 confirmed, 7 overturned, 4 insufficient data
- `[2026-04-15] [docs/SCORING_FORMULA_V3]` — Complete 5-layer formula specification: hard blocks, base scoring, market state, entry quality, context, regime
- `[2026-04-15] [docs/SCORING_V3_LIVE]` — Live implementation guide: WR-Lift Hybrid with Pair Layer, deployed to V1 and V2
- `[2026-04-15] [data/raw_candles]` — 50 raw OANDA candle JSON files + feature table, fully auditable
- `[2026-04-15] [scripts/*]` — 8 analysis scripts: formula_test, raw_backtest, trade_recipe, scoring_simulator, factor_hunt, full_factor_matrix, ten_formulas, proportional_analysis, export_features, pull_raw_data, hybrid_formula_test, v3_final_formula
- `[2026-04-15] [v3_scorer.py]` — Deployed independently to V1 and V2 (separate copies, no sharing)
- `[2026-04-15] [dashboard]` — Updated to V3 layered breakdown: Market State, Entry Quality, BB/Z/RSI, Cost/Context, Pair Layer

## 2026-04-15 — V1/V2 Live Changes

- `[2026-04-15] [V1+V2]` — SL floor 0.25% to 0.10%, min RR 1.35 to 1.0, spread threshold 30% to 10%
- `[2026-04-15] [V1+V2]` — Regime floor REMOVED (was blocking at score < -1), only BLOCKED suppresses
- `[2026-04-15] [V1+V2]` — BB exhaustion gate REMOVED, V3 scorer handles BB state scoring
- `[2026-04-15] [V1+V2]` — V3 Hybrid Scorer deployed as scoring override
- `[2026-04-15] [V1+V2]` — Dashboard updated with V3 layered breakdown
- `[2026-04-15] [V1+V2]` — Git pushed to GitHub + Alien Device

## 2026-04-15 — Architecture Updates

- `[2026-04-15] [docs/BLUEPRINT]` — Dashboard redesigned as modular widget system: DashboardWidget Protocol, widget registry, auto-discovery, module-registered panels, pair view, replay view, REST API contract
- `[2026-04-15] [README]` — Phase C updated to modular dashboard with detailed checklist

## 2026-04-15 — V3 Scorer Integration + Module Build-out + Dashboard

### Module Audit & Reconciliation
- `[2026-04-15] [core/strategy_router]` — STRETCH_UP route changed from ["trend"] to [] (0% WR on V1 live data, hard block). All other modules verified aligned with V3 scoring.
- `[2026-04-15] [all dev logs]` — Verified all 7 module logs already had Apr 15 corrections (OTR inversion, regime floor removal, ATR dead weight, wall proximity inconsistency, spread vs natural stop, box age discovery).

### Phase 3: V3 Scorer Module + New Features
- `[2026-04-15] [strategies/v3_scorer]` — V3HybridScorer module: 43-factor scoring engine ported from scripts/hybrid_formula_test.py. Layer 0 hard blocks (5), Layer 1 single-factor scoring (17 factors), Layer 2 paired aspects (18 bonuses/penalties). ScorerResult dataclass with score, blocks, breakdown, tier. -> [logs/modules/strategies-scoring.md](modules/strategies-scoring.md)
- `[2026-04-15] [features/ema]` — EMACalculator: EMA20/EMA50 from hourly bars with range-relative distance percentages.
- `[2026-04-15] [features/volume]` — VolumeCalculator: current/average volume ratio from hourly bars.
- `[2026-04-15] [features/rsi]` — RSICalculator: RSI(14) from hourly close prices.
- `[2026-04-15] [features/bollinger]` — Enriched with z_score and bb_position outputs.
- `[2026-04-15] [features/atr]` — Enriched with adr_consumed output (today's range / ATR).
- `[2026-04-15] [features/zone_detector]` — Enriched with box_age_hours and wall_proximity outputs.
- `[2026-04-15] [core/scan_pipeline]` — V3 scorer integrated as step 7: re-scores gate-approved candidates, rejects < 50 or hard-blocked, replaces strategy fixed scores.

### Phase 4: Broker Adapter
- `[2026-04-15] [market/broker]` — BrokerAdapter Protocol: 15-method interface (account, instruments, pricing, candles, positions, orders, transactions, health). Supporting dataclasses: AccountInfo, InstrumentInfo, PriceQuote, OrderResult, TradeInfo.
- `[2026-04-15] [market/oanda_adapter]` — OANDAAdapter: full OANDA v20 REST implementation with circuit breaker (5 failures → 120s recovery), candle cache fallback for 502s, 404 transaction stream fallback for closed trades, instrument cache on boot.
- `[2026-04-15] [market/fee_calculator]` — FeeCalculator with V3 OTR categories (inverted: <8% = too_low, 8-18% = sweet_spot), spike detection, session spread estimation.
- `[2026-04-15] [market/dry_run_adapter]` — DryRunAdapter: shadow-trading with real OANDA prices, simulated order execution, virtual positions.

### Phase 5: Wire Runtime.boot()
- `[2026-04-15] [core/runtime]` — boot() fully wired: initializes OANDA or dry-run broker, registers 7 features, 4 classifiers, 2 strategies, 12 gates (ordered pipeline), V3 scorer. _run_cycle() fully wired: session-aware screener, market snapshot fetching, scan_pipeline.scan_universe(), entry planning + sizing + order execution.

### Phase 6: Modular Dashboard
- `[2026-04-15] [dashboard/widget_registry]` — WidgetRegistry with DashboardWidget Protocol, category grouping, render_all() for API.
- `[2026-04-15] [dashboard/app]` — Flask app (port 8084, 127.0.0.1): HTTP Basic Auth + session cookie for JS fetch, REST API (/api/status, /api/widgets, /api/widgets/<category>), auto-refresh HTML template.
- `[2026-04-15] [dashboard/widgets]` — 5 widgets: HealthWidget (module registry status), SystemWidget (equity, P&L, uptime, cycles), ScoringWidget (V3 scorer breakdowns), GateWidget (pass/fail counts, rejection reasons), ExecutionWidget (entries, SL moves, closes).
- `[2026-04-15] [dashboard/templates]` — Dark theme HTML with tab navigation, 10s auto-refresh, UTC clock, category filtering.
- `[2026-04-15] [dashboard/static]` — CSS: dark GitHub-style theme with sticky header, widget cards, category sections.

### Phase D: Tests (2026-04-15)
- `[2026-04-15] [tests/unit/test_v3_scorer]` — 42 tests: all 5 hard blocks, all 17 single-factor weights, 5 paired aspects, 4 tier classifications, custom thresholds.
- `[2026-04-15] [tests/unit/test_features]` — 14 tests: EMA (3), Volume (2), RSI (2), Bollinger enrichment (2), ATR enrichment (1), Strategy Router (3).
- `[2026-04-15] [tests/unit/test_gates]` — 16 tests: Spread (5), OTR inverted (3), R:R (3), Exhaustion (2), Regime floor (2), Stop planner trigger-side (4).
- `[2026-04-15] [tests/integration/test_scan_pipeline]` — 3 tests: features compute, universe scan, event emission.
- `[2026-04-15] [tests/smoke/test_boot]` — 5 tests: all imports, config loads, scorer deterministic, OTR inversion, widget registry.

### Phase E: Config Validation + Hot Reload (2026-04-15)
- `[2026-04-15] [core/config]` — Schema validation (types, ranges, required fields), env var overrides (SCROOGE_SECTION_KEY=value), file watcher with hot reload, change history tracking, rollback on invalid reload, ConfigChanged events for module mode switching.
- `[2026-04-15] [core/runtime]` — Config validation on boot, env overrides applied before validation, config watcher started on boot, _handle_config_change for module/gate mode switching and scan interval updates.
- `[2026-04-15] [tests/unit/test_config]` — 13 tests: schema validation (7), dot-path + history (3), env overrides (2), callbacks (1), file watcher with change detection + rollback on invalid (2), diff detection (2).

### Phase F: Replay Harness (2026-04-15)
- `[2026-04-15] [telemetry/replay]` — EventRecorder (subscribe_all → JSONL), EventReplayer (load, filter, extract candidates/rejections/approvals), replay_through_scorer for decision comparison, build_trade_timeline per symbol, session summary stats.
- `[2026-04-15] [tests/replay/test_replay]` — 7 tests: recording to JSONL, stop prevents further recording, load events, filter by type, summary stats, trade timeline, full round-trip record-then-replay.

### Session: 2026-04-16 — Dashboard, Ratchet Fix, Stop Persistence
- `[2026-04-16] [dashboard/templates]` — Added BALANCE metric to dashboard status bar (first position), renamed REALIZED P/L → UNREALIZED P/L. Updated live_state.py field from realized_pl to unrealized_pl. Updated runtime.py to pass unrealized_pl.
- `[2026-04-16] [management/position]` — Fixed ratchet bypass bug: validate_stop() spread adjustment could loosen the stop past current_stop, defeating the ratchet's "never loosen" guarantee. Added final guard in runtime.py: after validate_stop(), reject any adjusted stop that would move backwards (lower for longs, higher for shorts).
- `[2026-04-16] [execution/position_tracker]` — Fixed stop persistence bug: update_stop() updated in-memory state but never called persist(). SL changes were lost on restart, reverting to the original stop from positions.json. Added self.persist() call.
- `[2026-04-16] [management/position]` — Tuned ratchet and break-even thresholds via config/default.json: ratchet_min_profit_pips 10→6 (locks 50% at +6 pips), be_trigger_pips 15→5 (breakeven at +5 pips). Old defaults left a gap where green trades could revert to red.
- `[2026-04-16] [infrastructure]` — Decommissioned Mr. Scrooge V1: stopped and disabled 3 systemd services (mr-scrooge, mr-scrooge-dashboard, mr-scrooge-harvester), removed service files, deleted ~/.openclaw/workspace/agents/mr-scrooge/. OANDA live credentials preserved in Obsidian vault. V3 is now the only active Scrooge version.

## 2026-04-16 — Exit Manager, Execution Audit, V3.1 Scorer Rebalance

### Exit Manager + Execution Audit
- `[2026-04-16] [core/position_pipeline]` — Added profit-phase gating: EARLY_HOLD (<0.5R skips ratchet/trail), LOCK (0.5-0.8R normal), HARVEST (>=0.8R aggressive). Added spread guard on ratchet moves (was only on trail). Added min-step filter (3 pip default) to prevent SL thrashing seen in OANDA logs.
- `[2026-04-16] [core/runtime]` — Fixed indentation bug: favorable_exit and emergency_close handlers were dead code (nested inside harvest elif branch since initial implementation, never reachable). Now properly wired as sibling elif blocks.
- `[2026-04-16] [telemetry/execution_audit]` — New module: JSONL audit logger + in-memory ring buffer (200 events). Records every SL move/block/hold/harvest/exit with full context (trade_id, symbol, profit_r, spread, reason). Computes live summary: SL efficiency %, block reason breakdown, avg spread at block vs move.
- `[2026-04-16] [core/runtime]` — Wired execution audit into position management loop. Every decision logged with audit_base context. Pushed to LiveState each cycle for dashboard consumption.
- `[2026-04-16] [dashboard]` — Added Execution tab: health lights (SL engine / spread risk / ratchet efficiency), metrics row (moves/blocks/holds/harvests), block reasons breakdown grid, scrollable event timeline with color-coded entries. Added /api/execution endpoint.
- `[2026-04-16] [config/default.json]` — Added management.exit_manager section: early_hold_threshold_r=0.5, lock_threshold_r=0.8, min_sl_step_pips=3.0.

### V3.1 Scorer Rebalance (MAJOR)
- `[2026-04-16] [strategies/v3_scorer]` — Fixed directional candle bug: dc_count was always counting green (bullish) candles regardless of trade direction. For shorts, bearish candles now count as aligned. Was skewing dc factor and paired penalties (n_hr_dc0, n_dc_otr) for all short trades.
- `[2026-04-16] [strategies/v3_scorer]` — V3.1 rebalance: complete reconfig of scoring engine.
  - **5 session buckets** instead of 3: asia_london_open (0-7), london (8-11), ny_active (12-17), late_ny (18-19), dead_late (20-23). NY active session gets own thresholds (floor=36, B=48, A=56) — was being killed by "afternoon" bucket (45/65).
  - **Hour decompressed**: 12-16 UTC from -8 to -3, 16-18 UTC from -4 to -1. NY session no longer structurally starved.
  - **Box age decompressed**: 18-24h from -12 to -7.
  - **Directional candles strengthened**: dc>=4 from +7 to +10, dc==0 from -6 to -8 — strongest soft factor per data.
  - **Weak factors shrunk**: wall proximity -3 (was -9), body% -4 (was -8), OTR -4 (was -11), ADR -1 (was -3).
  - **OTR<8+NORM hard block removed** — kept as soft penalty only.
  - **Pair layer halved**: all magnitudes ~50% of V3.0. Confirmation not rescue.
  - **Correlated-negative caps**: hr+age capped at -10 total (prevents triple-dipping with session thresholds), neutral cluster capped at -10.
  - **Decision thresholds lowered** for NY active session.
- `[2026-04-16] [tests/unit/test_v3_scorer]` — Updated all 47 tests for V3.1 weights: new factor values, new pair magnitudes, new session detection tests, correlated-cap tests.

### Platform Doctrine
- `[2026-04-16] [docs/PLATFORM_DOCTRINE]` — New document: formalizes Mr. Scrooge as a regime-aware trading platform. Strategy-specific entry with system-wide management. Three sacred rules: no self-activation outside router, no private management loops, every strategy declares management profile. Defines strategy menu, routing table, and management profiles.
