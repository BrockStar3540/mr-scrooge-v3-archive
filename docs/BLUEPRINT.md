# Mr. Scrooge V3 — Expansion-First Trading Platform Blueprint

> **Governing rule:** Any module can be added, removed, disabled, or put in observe-only mode without breaking the rest of the system.

This applies to: strategies, regimes, gates, indicators, feature builders, execution policies, ML advisors, LLM analysts, dashboard panels, alerts, experiments.

---

## 1. Design Principles

### 1.1 Stability First
Hard-risk and execution safety layers remain deterministic even if a strategy module fails, a gate is disabled, an ML advisor crashes, or an LLM returns nonsense.

### 1.2 Every Capability Is a Module
Each component has: a contract, health status, config, mode, metrics, audit trail.

### 1.3 One Source of Truth per Concern
One state store. One config store. One event bus. One health registry. One audit store.

### 1.4 Composition over Coupling
Modules do not call each other directly unless in the same bounded subsystem. Communication via: shared context, typed results, typed events.

### 1.5 Safe Degradation
If a non-core module is removed: system continues, health light turns gray/red, dashboard explains what is missing, no silent behavior changes.

---

## 2. System Shape

### 2.1 Top-Level Flow

```
Market Data
  -> Feature Engine
  -> Context Builder
  -> Regime Classifiers
  -> Strategy Router
  -> Strategy Modules
  -> Gate Pipeline
  -> Candidate Ranker
  -> Execution Planner
  -> Broker Adapter
  -> Position Management
  -> Telemetry / Dashboard / Audit
```

### 2.2 Core Split — Three Orchestrators

#### A. ScanPipeline
Fetching tradable symbols, building symbol context, running classifiers, routing strategies, evaluating candidates, passing approved candidates to execution.

#### B. PositionPipeline
Open positions, stop updates, harvest logic, break-even logic, reconciliation, close handling.

#### C. StateController
Runtime state, counters, cooldowns, memories, snapshots, persistence, restart recovery.

A tiny `Runtime` object wires these together.

---

## 3. Core Layers

### 3.1 Core Platform (the kernel)
- App bootstrap
- Dependency container
- Event bus
- Config registry
- Module registry
- State store
- Health registry
- Audit logger
- Scheduler

### 3.2 Market Data
- Broker adapter
- Quote stream
- Candle feeder
- Transaction stream
- Spread monitor
- Session classifier

### 3.3 Feature Layer (calculators only)
ATR, Bollinger, OTR, box width, range efficiency, volatility regime, trend slope, wick rejection score, measured move projection, opening-state classifier inputs. These do not trade — they compute reusable facts.

### 3.4 Context Layer
Builds per-symbol context from market data + features + persistent state.

### 3.5 Classification Layer
Regime, BB state, opening state, structure state, volatility state.

### 3.6 Strategy Layer (pluggable engines)
Reversal, trend, gap/opening, measured-move continuation, future engines.

### 3.7 Gate Layer (ordered filters)
Each gate can be: enabled, disabled, observe-only, hard-block, soft-score.

### 3.8 Execution Layer
Entry planner, stop planner, trail planner, broker routing, order reconciliation.

### 3.9 Management Layer
Ratchet, harvester, BE logic, time stop, green exit, emergency close.

### 3.10 Advisory Layer (optional, pluggable)
ML predictors, ML tuners, LLM analysts, heuristics advisors. Never bypass hard risk constraints.

### 3.11 Telemetry Layer
Decision audit, execution audit, health probe results, performance stats, replay logs, dashboard API.

---

## 4. Contracts

### 4.1 Feature Contract
```python
class FeatureModule(Protocol):
    name: str
    def compute(self, symbol: str, snapshot: MarketSnapshot, state: SymbolState) -> FeatureResult: ...
```

### 4.2 Classifier Contract
```python
class ClassifierModule(Protocol):
    name: str
    def classify(self, ctx: SymbolContext) -> ClassificationResult: ...
```

### 4.3 Strategy Contract
```python
class StrategyModule(Protocol):
    name: str
    def eligible(self, ctx: SymbolContext) -> bool: ...
    def evaluate(self, ctx: SymbolContext) -> TradeCandidate | None: ...
```

### 4.4 Gate Contract
```python
class GateModule(Protocol):
    name: str
    def evaluate(self, candidate: TradeCandidate, ctx: SymbolContext) -> GateResult: ...
```

### 4.5 Execution Policy Contract
```python
class ExecutionPolicy(Protocol):
    name: str
    def plan_entry(self, candidate: TradeCandidate, ctx: SymbolContext) -> OrderPlan: ...
    def plan_stop_update(self, position: PositionState, ctx: SymbolContext) -> StopPlan: ...
```

### 4.6 Advisor Contract
```python
class AdvisorModule(Protocol):
    name: str
    def advise(self, ctx: SymbolContext, candidate: TradeCandidate | None) -> AdvisorResult: ...
```

### 4.7 Health Contract
```python
class HealthCheckModule(Protocol):
    name: str
    def probe(self) -> HealthStatus: ...
```

---

## 5. Registries

Modules are discovered, not hard-wired.

### Registries needed:
- Feature registry
- Classifier registry
- Strategy registry
- Gate registry
- Advisor registry
- Health registry
- Dashboard widget registry

Each entry has: name, version, enabled, mode, dependencies, config namespace.

---

## 6. Module Modes

### 6.1 Common modes
- `disabled` / `observe` / `active`

### 6.2 Gate-specific modes
- `hard` / `soft` / `observe`

### 6.3 Advisor-specific modes
- `disabled` / `observe` / `advisory` / `weighted` / `hard_block`

---

## 7. State Store

### 7.1 State Domains
Symbol state, position state, cooldown state, memory state, regime state, execution state, module health state, experiment state.

### 7.2 Required Properties
Typed, snapshotable, replayable, persistent across restart, queryable by dashboard.

### 7.3 Access Pattern
```python
state.symbols["GBP_JPY"].bb_state
state.symbols["GBP_JPY"].cooldowns.zone_debounce_until
state.positions["trade_123"].stop.last_attempt_reason
state.health["trend_engine"].status
```

---

## 8. Event Bus

### 8.1 Event Types
- `MarketSnapshotReceived`, `FeaturesComputed`, `ContextBuilt`
- `ClassificationComputed`, `StrategyEvaluated`
- `CandidateCreated`, `GateEvaluated`, `CandidateRejected`, `CandidateApproved`
- `OrderPlanned`, `OrderSubmitted`, `OrderTriggered`, `OrderFilled`
- `StopUpdateAttempted`, `StopUpdateBlocked`, `StopUpdated`
- `PositionClosed`, `HealthChanged`, `ConfigChanged`

Modules become composable and observable without direct entanglement.

---

## 9. Strategy Router

### 9.1 Inputs
Opening state, BB state, regime, structure, session, spread environment.

### 9.2 Output
A set of allowed strategies.

```python
if bb_state in ["EXTREME_UP", "EXTREME_DOWN", "REJECTION"]:
    allow = ["REVERSAL"]
elif bb_state in ["TREND_UP", "TREND_DOWN", "STRETCH_UP", "STRETCH_DOWN"]:
    allow = ["TREND"]
elif opening_state in ["GAP_UP", "GAP_DOWN"]:
    allow = ["GAP_ENGINE"]
else:
    allow = []
```

No strategy should self-activate outside router permission.

---

## 10. Gate Pipeline

### 10.1 Gate Behavior
Each gate receives candidate, context, state, config. Returns pass/fail, hard/soft, reason, metrics.

### 10.2 Missing Gate Handling
Pipeline continues, marks gate status gray, records gate unavailable, does not crash.

### 10.3 Ordered Gates (example)
1. Spread gate
2. OTR gate
3. RR gate
4. Debounce gate
5. Cap gate
6. Regime floor gate
7. Exhaustion gate

Each is optional.

---

## 11. Feature Engine

### 11.1 Existing/Basic
ATR, BB bands, OTR, spread, box width.

### 11.2 Medium
Volatility regime, trend strength, wick rejection strength, range efficiency, box position, distance to PDH/PDL, measured move unit, gap size, session bias.

### 11.3 Advanced
Correlation regime, volume profile proxies, liquidity sweep score, synthetic macro bias, orderflow approximations, multi-symbol strength meters.

Strategies consume features — they do not recompute them.

---

## 12. Advisory / Intelligence Layer

### 12.1 Rule
ML and LLM are plug-ins, not foundations.

### 12.2 ML Should Do
Classify regimes better, predict trade quality, tune parameters, optimize stops, suggest risk modifiers.

### 12.3 LLM Should Do
Analyze logs, explain failures, propose experiments, summarize module performance, generate configuration suggestions.

### 12.4 ML/LLM Must NOT
Bypass hard risk controls, place orders directly without deterministic validation, replace the broker/execution safety chain.

### 12.5 Placement
After strategy candidate generation, before final execution planning.

---

## 13. Dashboard Design — Modular Widget System

The dashboard follows the same plug-in architecture as the trading system. Modules are not hard-wired into tabs — they register their own dashboard widgets. When a module is added, its panel appears. When disabled, its panel goes gray. No dashboard code changes required to add visibility for a new module.

### 13.1 Widget Contract

Every module can optionally implement a dashboard widget:

```python
class DashboardWidget(Protocol):
    widget_name: str
    widget_category: str  # "health", "features", "execution", "strategy", "advisory"
    def render_data(self) -> dict: ...
```

The dashboard discovers widgets from the module registry's `dashboard_widget_registry`. Core tabs are always present. Module-specific panels appear/disappear based on what's registered.

### 13.2 Core Tabs (Always Present)

**Health tab** — module status lights, auto-populated from health registry:
- Every registered module gets a status light (green/yellow/red/gray/blue)
- Grouped by layer: core, broker, features, classifiers, strategies, gates, execution, management, advisors
- Must show "signals evaluated this cycle" count — zero evaluations = red light
- Must show zone hit count, CT failure memory, entry cap status per symbol

**Status colors:** green=healthy, yellow=degraded, red=failed, gray=disabled, blue=observe-only.

**System tab** — runtime info:
- Cycle count, uptime, equity, daily P&L, position count
- Active sessions (must update live, not freeze at boot)
- Daily loss limit status
- Last scan timestamp

### 13.3 Module-Registered Panels

Each module registers its own panel data. Examples:

**From feature modules:**
- Zone detector → per-symbol zone map, PDH/PDL, tier counts
- Bollinger → band levels, BB state per symbol
- ATR → ATR values, consumption percentage
- Range builder → range state per symbol (RANGING/BREACH/CONFIRMED_BREAK)

**From classifiers:**
- Regime → regime score timeline, signal breakdown, state per symbol
- BB state → current BB classification per symbol
- Opening → gap detection status

**From strategies:**
- Reversal → candidate count, last candidate details, win/loss stats
- Trend → pullback detection count, entry stats

**From gates:**
- Each gate → pass/fail counts, rejection reasons, latency
- Pipeline → aggregate gate results per symbol

**From execution:**
- Entry planner → recent entries, staleness rejections, TP2 guard blocks
- Stop planner → stop update attempts, blocked reasons, trigger-side adjustments
- Order tracker → active orders, lifecycle states, fill timeline

**From management:**
- Trail → trailing stop movements, spread-pause events
- Ratchet → lock events, current lock levels
- Harvester → tier hits, partial close events
- BE → breakeven transitions

**From telemetry:**
- Quality tracker → MFE/MAE ratios, follow-through scores
- Experiments → active A/B tests, variant stats

### 13.4 Pair View

Per-pair dashboard accessible from any tab:
- All features for that symbol
- All classifications for that symbol
- All gate results for that symbol
- Current position (if any) with management state
- Zone entry count / CT failure count / cooldown status
- Historical trade outcomes

### 13.5 Replay View

For a trade ID or symbol + time range:
- All events in chronological order
- All module decisions with pass/fail/reason
- Why the trade was blocked or fired
- Entry → management → exit timeline with P&L

### 13.6 Data Contract

Dashboard reads from a single API, not scattered files:
- REST endpoint at `/api/status` returns full system state
- REST endpoint at `/api/widgets` returns all registered widget data
- REST endpoint at `/api/pair/{symbol}` returns pair-specific view
- REST endpoint at `/api/trade/{trade_id}` returns trade replay
- WebSocket at `/ws/live` for real-time updates (optional, Phase H)

P&L displayed on dashboard must use broker-reconciled values, not bot calculations. Show both if they differ and flag the discrepancy.

### 13.7 Live Configuration Panel

Every module's dashboard widget includes an adjustable configuration panel:

- Module ships with default config values (from `config/default.json`)
- Dashboard displays current config for each module with editable fields
- Changes apply immediately via hot-reload (emit `ConfigChanged` event)
- Changes persist to config file (survive restart)
- Config history: track what changed, when, and by whom
- Rollback: revert to previous config or defaults with one click
- Validation: module defines valid ranges/types for its parameters — dashboard enforces them before applying

Example: the RR gate widget shows:
```
reversal_min_rr: [1.35] (default: 1.35, range: 0.5-5.0)
trend_min_rr:    [1.10] (default: 1.10, range: 0.5-5.0)
mode:            [hard ▾] (options: hard, soft, observe)
enabled:         [✓]
```

Adjusting `mode` from `hard` to `observe` takes effect next scan cycle — no restart, no code edit, no SSH.

### 13.8 Security

- Bind to `127.0.0.1` only (not 0.0.0.0)
- HTTP Basic Auth (401 on failure)
- HTTPS via Tailscale Serve
- Not publicly routable
- Config changes require auth (same Basic Auth)
- Config change audit log (who changed what, when)

---

## 14. Configuration System

### 14.1 Config Groups
Runtime, broker, sessions, features, classifiers, strategies, gates, execution, risk, advisors, telemetry, dashboard.

### 14.2 Per-Module Config
Every module gets: enabled, mode, parameters, thresholds, version tag.

```yaml
strategies:
  trend_engine:
    enabled: true
    mode: active
    stretch_enabled: true
    size_full: 0.50
    size_stretch: 0.30

gates:
  rr_gate:
    enabled: true
    mode: hard
    reversal_min_rr: 1.35
    trend_min_rr: 1.10

advisors:
  ml_regime_advisor:
    enabled: false
    mode: observe
```

---

## 15. Testing Architecture

### 15.1 Unit Tests
Every module testable with fake context.

### 15.2 Integration Tests
Scan pipeline, position pipeline, state persistence, broker adapter.

### 15.3 Replay Tests
Feed historical events and verify outcomes.

### 15.4 Smoke Tests
At startup: load config, register modules, broker ping, one dry scan cycle, dashboard health check. If smoke fails, system does not start trading.

---

## 16. Observability Requirements

Every module reports: status, reason, last run, last success, avg latency, error count, current mode.
Optional: input hash, output summary, recent event count.

---

## 17. Execution Doctrine

### 17.1 Trigger-Side Aware Stops
Short stops validated against ask. Long stops validated against bid.

### 17.2 No-Man's-Zone Guard
Never place stops inside executable spread.

### 17.3 Spread-Aware Trailing
Trail logic must pause or loosen in hostile spread environments.

### 17.4 Trigger/Fill Distinction
Track: created, acknowledged, triggered, filled.

### 17.5 Execution Audit Is First-Class
Not optional, not patchwork.

---

## 18. Migration Path from V2

1. Define contracts and typed results
2. Split coordinator into ScanPipeline, PositionPipeline, StateController
3. Introduce registries and module loading
4. Centralize state
5. Build health registry and dashboard health tab
6. Add replay harness
7. Add optional advisors / ML / LLM

---

## 19. Acceptance Criteria

V3 is successful when:
- Removing any non-core module does not crash the bot
- Every module has visible health on the dashboard
- Every strategy is independently measurable
- Every gate can be toggled without code edits
- Every trade can be replayed from logs
- Every stop update can be audited
- Strategies can be added without pipeline surgery
- Advisors can be enabled/disabled without changing core logic

---

## 20. Final Doctrine

```
Every capability is a module.
Every module has a contract.
Every contract has health.
Every health state is visible.
Every decision is replayable.
```

---

## Appendix: Platform Doctrine (2026-04-16)

See [PLATFORM_DOCTRINE.md](PLATFORM_DOCTRINE.md) for the governing rules:

1. **No strategy may self-activate outside router permission**
2. **No strategy may own a private management loop**
3. **Every strategy must declare a management profile**

Key evolution: Mr. Scrooge is now defined as a **regime-aware trading platform**
with strategy-specific entry and system-wide management. Box reversal remains a
first-class strategy but is no longer the only lens through which markets are
evaluated. Multiple strategy families coexist under one shared execution kernel.
