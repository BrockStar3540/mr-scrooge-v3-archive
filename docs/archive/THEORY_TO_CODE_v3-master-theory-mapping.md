> **ARCHIVED 2026-05-30** as part of V4 cutover prep. This doc
> mapped the V1 MASTER_THEORY section numbers to V3 code modules. With
> MASTER_THEORY itself archived at V4 (Box reversal becomes 1 of ~25
> strategies in the encyclopedia, no longer the canonical guide), the
> section-to-code mapping concept loses its anchor.
> 
> The mapping function is absorbed by three V4 docs:
> - `docs/LIVE_SYSTEM_SPEC.md` — current architecture (textual)
> - `docs/ARCHITECTURE_DIAGRAM.md` — current architecture (visual, Mermaid)
> - `docs/STRATEGY_ENCYCLOPEDIA.md` — per-strategy probe code references
> 
> The "V2 problems → V3 solutions" section here is era-specific history;
> the equivalent narrative for V4 lives in `HISTORY.md` and `docs/history/`.
> 
> Preserved as the historical record of how the V3 architecture was
> catalogued during its build phase. For current truth see the three
> V4 docs above.

---

# Theory-to-Code Mapping

> Every theory concept maps to a module, contract, or config path.
> If it doesn't, it's not implemented yet.

---

## Structure: Theory Section -> V3 Layer -> Module -> Contract

| Theory | Section | V3 Layer | Module(s) | Contract | Config Path |
|--------|---------|----------|-----------|----------|-------------|
| Box | 2 | `features/` | `box_builder` | `FeatureModule` | `features.box` |
| Box States | 2.4 | `classifiers/` | `structure_classifier` | `ClassifierModule` | `classifiers.structure` |
| Alternative Box | 2.5 | `features/` | `box_builder` | `FeatureModule` | `features.box.alternative_enabled` |
| Liquidity Zones | 3.1 | `features/` | `zone_detector` | `FeatureModule` | `features.zones` |
| Sucker Move | 3.3 | `features/` | `sucker_move_detector` | `FeatureModule` | `features.sucker_move` |
| Pitchfork Entry | 4 | `strategies/` | `reversal_engine` | `StrategyModule` | `strategies.reversal` |
| ATR | 6 | `features/` | `atr_calculator` | `FeatureModule` | `features.atr` |
| ATR Exhaustion | 6.2 | `features/` | `otr_calculator` | `FeatureModule` | `features.otr` |
| Double BB | 7 | `features/` | `bollinger_calculator` | `FeatureModule` | `features.bollinger` |
| BB States | 7.3 | `classifiers/` | `bb_classifier` | `ClassifierModule` | `classifiers.bb_state` |
| Regime | 13 | `classifiers/` | `regime_classifier` | `ClassifierModule` | `classifiers.regime` |
| Reversal Engine | 8.1 | `strategies/` | `reversal_engine` | `StrategyModule` | `strategies.reversal` |
| Trend Engine (old) | 8.2 | `strategies/` | `trend_engine` | `StrategyModule` | `strategies.trend` | **DISABLED** |
| DBB Trend Engine | 8.2 | `strategies/` | `dbb_trend_engine` | `StrategyModule` | `strategies.dbb_trend` | **ACTIVE** — breakout/pullback continuation |
| Gap Engine | 8.3 | `strategies/` | `gap_engine` | `StrategyModule` | `strategies.gap` |
| Measured Move | 8.3 | `strategies/` | `measured_move_engine` | `StrategyModule` | `strategies.measured_move` |
| Vol Compression | 8.3 | `strategies/` | `vol_breakout_engine` | `StrategyModule` | `strategies.vol_breakout` |
| Spread Gate | 9.2 | `gates/` | `spread_gate` | `GateModule` | `gates.spread` |
| RR Gate | 9.2 | `gates/` | `rr_gate` | `GateModule` | `gates.rr` |
| OTR Gate | 9.2 | `gates/` | `otr_gate` | `GateModule` | `gates.otr` |
| Zone Gate | 9.2 | `gates/` | `zone_gate` | `GateModule` | `gates.zone` |
| Debounce Gate | 9.2 | `gates/` | `debounce_gate` | `GateModule` | `gates.debounce` |
| Regime Gate | 9.2 | `gates/` | `regime_floor_gate` | `GateModule` | `gates.regime_floor` |
| Exhaustion Gate | 9.2 | `gates/` | `exhaustion_gate` | `GateModule` | `gates.exhaustion` |
| Trigger-side SL | 10.4.1 | `execution/` | `stop_planner` | `ExecutionPolicy` | `execution.trigger_side_validation` |
| No-man's-zone | 10.4.2 | `execution/` | `stop_planner` | `ExecutionPolicy` | `execution.no_mans_zone_guard` |
| Spread-aware trail | 10.4.3 | `execution/` | `trail_planner` | `ExecutionPolicy` | `execution.spread_aware_trailing` |
| Order lifecycle | 10.4.4 | `execution/` | `order_tracker` | — | `execution.lifecycle_tracking` |
| Partial TP | 11.2 | `management/` | `harvester` | — | `management.harvest` |
| Break-even | 11.2 | `management/` | `be_manager` | — | `management.break_even` |
| Trailing stop | 11.2 | `management/` | `trail_manager` | — | `management.trail` |
| Ratchet | 11.2 | `management/` | `ratchet_manager` | — | `management.ratchet` |
| Session classifier | 5 | `market/` | `session_classifier` | — | `market.sessions` |
| Spread monitor | — | `market/` | `spread_monitor` | — | `market.spread_monitor` |
| Strategy Router | — | `core/` | `strategy_router` | — | `strategies._router` |
| ML Regime | 12 (advisory) | `advisors/` | `ml_regime_advisor` | `AdvisorModule` | `advisors.ml_regime` |
| ML Trade Scorer | 12 (advisory) | `advisors/` | `ml_trade_scorer` | `AdvisorModule` | `advisors.ml_trade_scorer` |
| LLM Analyst | 12 (advisory) | `advisors/` | `llm_analyst` | `AdvisorModule` | `advisors.llm_analyst` |

---

## V2 Problems -> V3 Solutions

| V2 Problem | V3 Fix |
|------------|--------|
| coordinator.py (1627-line god object) | Split into `ScanPipeline`, `PositionPipeline`, `StateController` |
| No interface contracts | Every module implements a Protocol (see `core/contracts.py`) |
| Scattered state (dicts on coordinator + ctx) | Centralized `StateStore` with typed domains |
| Cross-cutting imports (star topology) | Modules communicate via `EventBus` + `SymbolContext` |
| regime/ naming confusion | Clean split: `classifiers/bb_classifier`, `classifiers/regime_classifier` |
| No tests | Unit/integration/replay/smoke test layers from day one |
| Adding engine = coordinator surgery | `ModuleRegistry` auto-discovers strategies |
| Gates untogglable without code edits | Config-driven modes: `hard`/`soft`/`observe`/disabled |
| No execution audit | First-class `telemetry/` layer with decision + execution audit |
| Harvester as separate daemon | `PositionPipeline` orchestrates all management (harvest, trail, BE, ratchet) |

---

## Pipeline Flow with Module Names

```
Market Data
  |
  v
[market/broker_adapter]  ->  MarketSnapshot
  |
  v
[market/spread_monitor]  ->  spread state
[market/session_classifier]  ->  session state
  |
  v
[features/*]  ->  FeatureResult per feature
  - atr_calculator
  - bollinger_calculator
  - otr_calculator
  - box_builder
  - zone_detector
  - sucker_move_detector
  - trend_slope
  - wick_rejection
  - range_efficiency
  - measured_move_projection
  |
  v
[context/context_builder]  ->  SymbolContext
  |
  v
[classifiers/*]  ->  ClassificationResult per classifier
  - regime_classifier
  - bb_classifier
  - opening_classifier
  - structure_classifier
  - volatility_classifier
  |
  v
[core/strategy_router]  ->  allowed strategy set
  |
  v
[strategies/*]  ->  TradeCandidate | None
  - reversal_engine (ACTIVE)
  - dbb_trend_engine (ACTIVE — replaces trend_engine)
  - direct_entry (ACTIVE — fallback)
  - trend_engine (DISABLED)
  - gap_engine (DISABLED)
  - measured_move_engine (DISABLED)
  - vol_breakout_engine (DISABLED)
  |
  v
[gates/*]  ->  GateResult per gate (ordered pipeline)
  1. spread_gate
  2. otr_gate
  3. rr_gate
  4. debounce_gate
  5. cap_gate
  6. regime_floor_gate
  7. exhaustion_gate
  |
  v
[advisors/*]  ->  AdvisorResult (optional, never bypasses gates)
  - ml_regime_advisor
  - ml_trade_scorer
  - llm_analyst
  |
  v
[execution/entry_planner]  ->  OrderPlan
[execution/broker_router]  ->  order submitted
  |
  v
[management/*]  (PositionPipeline)
  - stop_manager (trigger-side, no-man's-zone)
  - trail_manager (spread-aware)
  - harvester (partial TP)
  - be_manager (break-even shift)
  - ratchet_manager (lock gains)
  - time_stop
  - green_exit
  - emergency_close
  |
  v
[telemetry/*]
  - decision_audit
  - execution_audit
  - health_probes
  - replay_logger
  - dashboard_api
```

---

## Implementation Priority

### Phase 1 — Contracts + Core (DONE)
- [x] `core/types.py`
- [x] `core/contracts.py`
- [x] `core/events.py`
- [x] `core/registry.py`
- [x] `core/state.py`
- [x] `core/config.py`

### Phase 2 — Market + Features
- [ ] `market/broker_adapter.py` (OANDA)
- [ ] `market/spread_monitor.py`
- [ ] `market/session_classifier.py`
- [ ] `features/atr.py`
- [ ] `features/bollinger.py`
- [ ] `features/otr.py`
- [ ] `features/box_builder.py`
- [ ] `features/zone_detector.py`
- [ ] `features/sucker_move.py`

### Phase 3 — Classifiers + Context
- [ ] `context/context_builder.py`
- [ ] `classifiers/regime.py`
- [ ] `classifiers/bb_state.py`
- [ ] `classifiers/opening.py`
- [ ] `classifiers/structure.py`

### Phase 4 — Strategies + Router
- [ ] `core/strategy_router.py`
- [ ] `strategies/reversal.py`
- [ ] `strategies/trend.py`

### Phase 5 — Gates
- [ ] `gates/spread.py`
- [ ] `gates/rr.py`
- [ ] `gates/otr.py`
- [ ] `gates/debounce.py`
- [ ] `gates/cap.py`
- [ ] `gates/regime_floor.py`
- [ ] `gates/exhaustion.py`

### Phase 6 — Pipelines + Execution
- [ ] `core/scan_pipeline.py`
- [ ] `core/position_pipeline.py`
- [ ] `execution/entry_planner.py`
- [ ] `execution/stop_planner.py`
- [ ] `execution/trail_planner.py`
- [ ] `execution/broker_router.py`

### Phase 7 — Management
- [ ] `management/harvester.py`
- [ ] `management/be_manager.py`
- [ ] `management/ratchet.py`
- [ ] `management/trail.py`
- [ ] `management/time_stop.py`
- [ ] `management/green_exit.py`
- [ ] `management/emergency_close.py`

### Phase 8 — Telemetry + Dashboard
- [ ] `telemetry/decision_audit.py`
- [ ] `telemetry/execution_audit.py`
- [ ] `telemetry/replay_logger.py`
- [ ] `dashboard/health_tab.py`
- [ ] `dashboard/modules_tab.py`
- [ ] `dashboard/features_tab.py`
- [ ] `dashboard/execution_tab.py`
- [ ] `dashboard/replay_tab.py`

### Phase 9 — Advisors (optional)
- [ ] `advisors/ml_regime.py`
- [ ] `advisors/ml_trade_scorer.py`
- [ ] `advisors/llm_analyst.py`


---

## Runtime Extraction (2026-04-16)

The V2 coordinator split (`ScanPipeline`, `PositionPipeline`, `StateController`) has been
further extracted into dedicated modules:

| Module | Responsibility | Lines |
|--------|---------------|-------|
| `core/runtime.py` | Conductor — boot, loop, shutdown | 232 |
| `core/bootstrap.py` | Module registration, config, broker init | 262 |
| `core/runtime_context.py` | Typed dependency container | 43 |
| `core/scan_coordinator.py` | Market data, scan pipeline, candidate filtering | 125 |
| `core/execution_coordinator.py` | Sizing, SL validation, order placement | 131 |
| `core/position_coordinator.py` | Management pipeline, SL physics, harvest/exit | 185 |
| `services/dashboard_bridge.py` | Dashboard live_state publishing | 97 |
| `services/config_watcher.py` | Hot-reload handling | 53 |
| `services/state_recovery.py` | Vanished trades, pending orders, harvest limits | 155 |

## Strategy-Family-Aware Scoring (2026-04-16)

| Concept | Module | Config Path |
|---------|--------|-------------|
| Family overlays (trend/reversal) | `strategies/v3_scorer.py` | `scoring` |
| Family-aware RR gate | `gates/risk_reward.py` | `gates.rr.trend_min_rr` |
| Management profiles | `core/position_pipeline.py` | `management.exit_manager` |
| Candidate family helper | `gates/risk_reward.py::_candidate_family()` | — |
