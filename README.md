# Mr. Scrooge V3 — Plug-in Trading Platform

> Every capability is a module. Every module has a contract. Every contract has health. Every health state is visible. Every decision is replayable.

## What This Is

A modular market behavior engine that routes capital based on context, structure, and execution quality. Not a strategy, not an indicator system, not a signal bot — a plug-in trading platform where any module can be added, removed, disabled, or put in observe-only mode without breaking the rest of the system.

## Repo Structure

```
src/scrooge_v3/
  core/         — kernel: runtime, pipelines, registry, events, state, config
  market/       — broker adapter, screener, spread monitor
  features/     — ATR, Bollinger, OTR, zone detector, range builder
  context/      — context builder (wires features + classifiers)
  classifiers/  — BB state, regime, opening state, structure
  strategies/   — reversal, trend + strategy router
  gates/        — 12 gates + base + pipeline runner
  execution/    — entry planner, stop planner, sizing, order tracker
  management/   — trail, ratchet, BE, partial harvest, favorable exit, emergency
  advisors/     — (future: ML/LLM plug-ins)
  telemetry/    — quality tracker, health monitor, experiments, entry context
  dashboard/    — (future: 5-tab web dashboard)

docs/
  BLUEPRINT.md        — full architecture (layers, contracts, registries, events)
  MASTER_THEORY.md    — Part I source theory + Part II engineering extensions
  THEORY_TO_CODE.md   — maps every theory concept to a V3 module
  V2_MASTER_THEORY.md — reference copy of V2 source theory

logs/
  DEVLOG.md     — main timeline of all changes
  PAIRS.md      — per-pair index with execution profiles
  SESSIONS.md   — per-session index (Sydney, Tokyo, London, New York)
  modules/      — 17 module-specific dev logs with 103 historical lessons
  pairs/        — 8 pair-specific dev logs
  sessions/     — 4 session-specific dev logs

config/
  default.json  — hierarchical config for all modules

tests/
  unit/         — per-module tests with fake context
  integration/  — pipeline tests with mock data
  replay/       — historical event replay
  smoke/        — startup validation
```

## Key Documents

| Document | Purpose |
|----------|---------|
| `docs/BLUEPRINT.md` | Architecture blueprint — layers, contracts, registries, module modes |
| `docs/MASTER_THEORY.md` | Trading theory — Part I (Doug/Sylvia source truth) + Part II (engineering) |
| `docs/THEORY_TO_CODE.md` | Maps every theory section to a V3 module, contract, and config path |
| `logs/DEVLOG.md` | Development timeline — what changed, when, and which module log has details |
| `logs/PAIRS.md` | Pair execution profiles (tight/medium/wide) + per-pair lessons |
| `logs/SESSIONS.md` | Session windows (UTC) + session-specific rules |

## How to Resume Work

1. Read `logs/DEVLOG.md` for the timeline of what's been done
2. Check the **Development Roadmap** below for what's next
3. Read the relevant module log in `logs/modules/` for historical lessons before touching any module
4. Read `logs/PAIRS.md` for pair-specific bugs before touching execution profiles
5. Check `docs/THEORY_TO_CODE.md` Phase checklist for implementation status

---

# Development Roadmap

## Completed Phases

### Phase 1: Foundation (2026-04-14)
- [x] GitHub repo created (`BrockStar3540/mr-scrooge-v3`, private)
- [x] Project structure (11 layers, all packages stubbed)
- [x] Core kernel: types, contracts (7 Protocols), event bus, registry, state store, config store
- [x] Blueprint doc (`docs/BLUEPRINT.md`)
- [x] Master Theory doc (`docs/MASTER_THEORY.md` — Part I source theory + Part II engineering)
- [x] Theory-to-code mapping (`docs/THEORY_TO_CODE.md`)
- [x] Developer log system (DEVLOG.md + per-module logs)
- [x] Default config (`config/default.json`)
- [x] Unit tests for registry + event bus

### Phase 2: V2 Migration — Tier 1 Direct Ports (2026-04-14)
- [x] V2 source staged to `_v2_source/` (62 Python files, reference only)
- [x] Gate system: 12 gates + BaseGate + GatePipeline (all V3 naming applied)
  - [x] 6 ported: zone_proximity, trend_filter, atr_budget, directional_pressure, entry_confirmation, overhead_ratio
  - [x] 6 new (from coordinator): spread, risk_reward, zone_entry_cap, debounce, regime_floor, exhaustion_filter
- [x] Domain models: LiquidityZone, SessionRange, ZoneMap, RangeState, OpenPosition, StrategyEvaluation
- [x] Telemetry: quality tracker, health monitor, experiments, entry context, quality indicators

### Phase 3: V2 Migration — Tier 2 Refactored Ports (2026-04-14)
- [x] Features: ATR, Bollinger, OTR, zone detector (694 LOC), range builder (532 LOC)
- [x] Classifiers: BB state (9 states), regime (7 signals), opening state, structure
- [x] Context builder
- [x] Strategies: reversal, trend
- [x] Strategy router (BB state → strategy mapping)

### Phase 4: Coordinator Decomposition (2026-04-14)
- [x] ScanPipeline (features → context → classify → route → evaluate → gate)
- [x] PositionPipeline (manage → trail → ratchet → BE → harvest → exit)
- [x] StateController (zone caps, CT memory, debounce, cooldowns, daily loss)
- [x] Runtime (130-line main loop, was 1,627 in V2)

### Phase 5: Execution + Management Layers (2026-04-14)
- [x] Entry planner (sizing adjustments, staleness/TP2 guards)
- [x] Stop planner (trigger-side validation, no-man's-zone, spread-aware trailing)
- [x] Order tracker (CREATED → SENT → ACK → TRIGGERED → FILLED lifecycle)
- [x] Sizing calculator (margin-utilization, broker-agnostic)
- [x] Trail manager (hourly candle structure)
- [x] Ratchet manager (lock % of unrealized gains)
- [x] Break-even manager (move to BE after partial TP or pip threshold)
- [x] Partial harvest manager (take 50% at TP1)
- [x] Favorable exit manager (limit-order exit with fast-market fallback)
- [x] Emergency close manager (circuit breaker for drawdown/margin/disconnect)

### Phase 6: Market Layer (2026-04-14)
- [x] Universe screener (session-aware pair selection, 3 modes)
- [x] Spread monitor (rolling stats, hostile detection)

### Phase 7: Historical Lessons Audit (2026-04-15)
- [x] Audited 57 workspace/vault markdown files
- [x] Audited 21 known defects from vault defect tracker
- [x] Audited 2 postmortem files (scoring inversion, OANDA audit)
- [x] Audited 9 Dropbox files (1.4MB session transcripts, Feb-Apr 2026)
- [x] 103 findings categorized into 17 module dev logs
- [x] 8 pair-specific dev logs with execution profiles
- [x] 4 session-specific dev logs (Sydney, Tokyo, London, New York)
- [x] USDJPY runaway re-entry bug (2026-03-02) — foundational incident documented

---

## Remaining Phases

### Phase A: Broker Adapter (CRITICAL PATH)
- [ ] Define broker-agnostic interface (`market/broker.py` Protocol)
- [ ] Port OANDA client (`market/oanda_adapter.py`) — V2 `core/oanda_client.py` (600 LOC)
- [ ] Port fee calculator (`market/fee_calculator.py`) — V2 `core/fee_calculator.py` (194 LOC)
- [ ] Quote stream / candle feeder integration
- [ ] Transaction stream (detect native closes between cycles)
- [ ] Account info (equity, margin, positions) on boot
- [ ] Instrument cache (pip size, margin rate per pair)
- [ ] API error handling: 404 fallback, 502 cache, rate limiting
- [ ] Dry-run mode (shadow-trade without real orders)

### Phase B: Wire Runtime.boot()
- [ ] Register all feature modules into registry
- [ ] Register all classifier modules into registry
- [ ] Register all strategy modules into registry
- [ ] Register all gate modules into registry (ordered)
- [ ] Connect broker adapter
- [ ] Initialize state controller from config
- [ ] Reconcile open positions from broker on boot
- [ ] Run smoke test: broker ping, one dry scan cycle, health check
- [ ] If smoke fails → do not start trading
- [ ] Wire gate pipeline to scan pipeline

### Phase C: Modular Dashboard
- [ ] Define `DashboardWidget` Protocol (widget_name, widget_category, render_data())
- [ ] Dashboard widget registry in ModuleRegistry
- [ ] Core infrastructure:
  - [ ] Flask app (port 8084, bind 127.0.0.1, HTTP Basic Auth)
  - [ ] REST API: `/api/status`, `/api/widgets`, `/api/pair/{symbol}`, `/api/trade/{trade_id}`
  - [ ] Tailscale Serve HTTPS exposure
  - [ ] Widget auto-discovery from registry (modules register their own panels)
- [ ] Core tabs (always present):
  - [ ] Health tab: auto-populated status lights from health registry, per-layer grouping
  - [ ] System tab: cycle count, uptime, equity, daily P&L, active sessions, loss limit status
- [ ] Module-registered panels (appear/disappear with module registration):
  - [ ] Feature widgets: zone map, BB bands, ATR values, range state
  - [ ] Classifier widgets: regime score timeline, BB state, opening state
  - [ ] Strategy widgets: candidate counts, win/loss stats
  - [ ] Gate widgets: pass/fail counts, rejection reasons, latency
  - [ ] Execution widgets: entry log, stop movements, order lifecycle
  - [ ] Management widgets: trail events, ratchet locks, harvest tiers, BE transitions
  - [ ] Telemetry widgets: MFE/MAE, follow-through scores, experiment results
- [ ] Pair view: per-symbol deep dive (all features, classifications, gates, position state)
- [ ] Replay view: per-trade event timeline with all module decisions
- [ ] P&L display: broker-reconciled values, flag discrepancies with bot calculations
- [ ] "Signals evaluated this cycle" counter — zero = red light (catches silent bugs)
- [ ] Zone hit count, CT failure memory, entry cap status per symbol visible
- [ ] Live config panel per module:
  - [ ] Display current config values with editable fields
  - [ ] Module defines valid ranges/types — dashboard enforces before applying
  - [ ] Changes apply immediately via hot-reload (ConfigChanged event)
  - [ ] Changes persist to config file (survive restart)
  - [ ] Config change history (what changed, when)
  - [ ] Rollback to previous config or defaults with one click
  - [ ] Config changes require auth + audit log
- [ ] Dev log: `logs/modules/dashboard.md` (9 historical V1/V2 lessons already captured)

### Phase D: Tests
- [ ] Unit tests: every gate with fake context (verify pass/fail logic)
- [ ] Unit tests: every feature with mock bars (verify calculations)
- [ ] Unit tests: every classifier with mock features (verify labels)
- [ ] Unit tests: strategy router (BB state → allowed strategies)
- [ ] Unit tests: state controller (zone caps, cooldowns, daily reset)
- [ ] Unit tests: entry planner (staleness, TP2 guard, sizing adjustments)
- [ ] Unit tests: stop planner (trigger-side, no-man's-zone, spread-aware)
- [ ] Integration test: ScanPipeline with mock market data → produces candidates
- [ ] Integration test: PositionPipeline with mock positions → produces management actions
- [ ] Smoke test: boot Runtime with dry_run=true → completes one cycle without crash
- [ ] Regression: V2 gate logic produces identical results given identical inputs
- [ ] Regression: V2 zone detector produces identical zones given identical bars

### Phase E: Config Validation + Hot Reload
- [ ] Validate config against registered module schemas on boot
- [ ] File watcher for `config/default.json` changes
- [ ] Emit `ConfigChanged` event on reload
- [ ] Module mode switching via config (disabled/observe/active) without restart
- [ ] Gate mode switching (hard/soft/observe) without restart
- [ ] Environment variable overrides (like V2's `SCROOGE_{FIELD}=value`)

### Phase F: Replay Harness
- [ ] Event recording: log all events to replay JSONL
- [ ] Event replay: feed historical events → verify outcomes
- [ ] Decision comparison: same inputs → same outputs as V2
- [ ] Parity harness: continuous V2 vs V3 comparison (like V1/V2 parity harness)
- [ ] Trade replay: for any trade, show all events + all module decisions + why blocked/fired

### Phase G: Deployment
- [ ] systemd service unit (`mr-scrooge-v3.service`)
- [ ] `.env` setup on EC2 (OANDA keys, separate from V1/V2)
- [ ] Fine-grained GitHub PAT: `GITHUB_TOKEN_SCROOGE_V3` (done)
- [ ] Alien Device backup (`git push alien main`)
- [ ] Log rotation (RotatingFileHandler, 10MB, 5 backups)
- [ ] Process singleton enforcement (file lock)
- [ ] Graceful shutdown (SIGTERM handler, persist state, close positions if configured)
- [ ] Frank monitoring integration (heartbeat, equity alerts)

### Phase H: Advisors (Optional, Post-Launch)
- [ ] ML regime advisor (observe mode first)
- [ ] ML trade scorer (observe mode first)
- [ ] LLM log analyst (on-demand, not real-time)
- [ ] Parameter tuner (suggest config changes based on performance data)

---

## Historical Lessons (Quick Reference)

The full audit is in `logs/modules/`. Here are the top 5 lessons that V3 must never violate:

1. **Scoring inversion** (2026-04-09): Higher scores predicted worse outcomes. V3 scoring must be validated against broker trade data, never bot logs. Bot P/L was wrong for 17/21 pairs.

2. **Runaway re-entry** (2026-03-02): 20 identical USD_JPY losses in 3 hours with zero circuit breakers. V3 has zone entry cap (3/day), cooldown after stop, daily loss limit, and pre-entry price validation from day one.

3. **Trigger-side SL** (2026-04-14): SL calculated from mid-price, OANDA triggers shorts on ask. During wide spreads, SL placed inside spread → instant fill. V3 validates all stops against the trigger side.

4. **4-actor race condition** (2026-04-10): Bot, ratchet, SL-limit, and harvester all modified the same trade's SL independently. V3 uses a single PositionPipeline with explicit ownership protocol.

5. **Rolling box failed** (2026-03-19): 30-minute rolling box experiment destroyed profitability (23 commits). Daily PDH/PDL is the correct model per MASTER_THEORY. Do not re-introduce rolling boxes.

---

## Tech Stack

- Python 3.9+ (3.11+ preferred)
- OANDA v20 REST API (broker adapter)
- Flask (dashboard)
- pandas, numpy (features/classifiers)
- pytest (tests)
- systemd (deployment)

## Getting Started

```bash
# Clone
git clone https://github.com/BrockStar3540/mr-scrooge-v3.git
cd mr-scrooge-v3

# Install
pip install -e ".[dev]"

# Run tests
pytest tests/

# Start (dry run)
python -m scrooge_v3 --dry-run
```
