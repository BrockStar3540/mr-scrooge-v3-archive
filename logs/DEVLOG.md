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
