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
