# Live System Specification

> **This is the executable truth.** Not theory, not doctrine — what the system
> actually does right now. Updated 2026-05-30.

> **Major shift since the 2026-05-25 revision:** the V3 gate stack
> (14 gates) and V3HybridScorer were retired between 2026-05-27 and
> 2026-05-28. The system is now **ML-routed**: per-pair / per-strategy
> routing decisions come from a matrix-mined parquet table, the LightGBM
> v0 scorer is the primary admission gate, and the V3.1 hybrid scorer is
> disabled. Most of what the May 25 spec described is no longer in the
> live code path.

---

## Strategies — Registered (bootstrap.py)

13 strategies are registered at boot. Eligibility for any given candidate
is decided by the routing table (`routing_table_v10_fast_v1_14b_full_matrix.parquet`),
not by per-strategy BB-state gating.

| Strategy | Family | Source / Status |
|----------|--------|-----------------|
| `reversal` | reversal | Legacy V3 family — still routed by matrix |
| `dbb_trend` | trend | Legacy V3 family — still routed by matrix |
| `direct` | direct | Fallback family — still routed by matrix |
| `trend` | trend | Legacy V3 family (sidelined in routing) |
| `box_master_theory` | box | Promoted 2026-05-27 |
| `canonical_lien_dbb` | trend | Promoted 2026-05-27 |
| `canonical_darvas` | trend | Promoted 2026-05-27 |
| `ifvg` | ifvg | Promoted 2026-05-27 |
| `session_breakout` | breakout | Promoted 2026-05-27 |
| `compression_expansion` | compression | Promoted 2026-05-27 |
| `trend_pullback` | trend | Promoted 2026-05-27 |
| `chaikin_macd_atr` | trend | Promoted 2026-05-27 |
| `compression_reversion` | compression | Promoted 2026-05-27 |

`reversal` + `dbb_trend` + `direct` remain the live-money workhorses by
trade count. The 6 strategies promoted 2026-05-27 (ifvg, session_breakout,
compression_expansion, trend_pullback, chaikin_macd_atr, compression_reversion)
are admitted by the routing table but have low live trade count pending
Phase 3 lab sweep completion.

`compression_reversion` known to be data-poor by design; CE + CR exit
configs deferred to a future routing version (`v1.14c` candidate).

## Routing — `routing_table_v10_fast_v1_14b_full_matrix.parquet`

The router is the only enforcer for which (pair × strategy × direction)
combinations are tradable.

- **1737 rows / 250 leaves** as of the 2026-05-27 promotion.
- Source: matrix mining over the 838k-trade lab corpus, per-pair / per-strategy
  WIN/LOSE rules + factor lifts.
- Replaces: every gate that used to encode this implicitly (RegimeStrategyRouter,
  RegimeCompat, SubRegimeFilter, EntryFilter, HTFTrendFilter).
- Loaded path: `data/routing_table_v10_fast_v1_14b_full_matrix.parquet`
- Shadow path (observe-only comparator): `data/routing_table_v9_observe.parquet`

The old BB-state → strategy mapping that the May 25 spec described
is **DEAD**. Strategies do not self-activate from BB states anymore.

## Gate Pipeline — actual current state

The `GatePipeline.register_many([...])` block in `bootstrap.py` now
registers a much smaller set than the May 25 spec described. Five gates
were retired 2026-05-27 (collapsed into the matrix router), and a 4-layer
matrix cascade was commented out 2026-05-28 ("ML router supersedes —
strategies pre-filtered by per-pair rules"). The active pipeline is:

| # | Gate | Mode | Behavior |
|---|------|------|----------|
| 1 | `DailyCircuitGate` | (HARD when enabled — **currently DISABLED via config**) | Daily P&L circuit breaker |
| 2 | `CooldownGate` | HARD | Per-(pair,dir) cooldown after stops |
| 3 | `DebounceGate` | HARD | Prevent re-entry at same zone within window |
| 4 | `ExpiryBackoffGate` | HARD | Cool down after LIMIT expiries at a zone |
| 5 | `NaturalTargetFloorGate` | (HARD when enabled — **currently DISABLED via config**) | M5 ATR×3 vs BB-width/2 floor |
| 6 | `FeatureQualityFloorGate` | HARD | Block on degraded EMA / RSI / zone_detector |
| 7 | `ZoneEntryCapGate` | HARD | Max N entries per zone+direction per day |

**Retired 2026-05-27 — replaced by MatrixRouter / routing table:**
`HTFTrendFilterGate`, `RegimeCompatGate`, `RegimeStrategyRouterGate`,
`SubRegimeFilterGate`, `EntryFilterGate`, `EntryFilterShadowGate`.

**Commented out 2026-05-28 — superseded by per-pair-rule pre-filtering at the router:**
`SessionFilterGate`, `PairFilterGate`, `MatrixComboFilterGate`,
`MatrixSignatureFilterGate`, monolith `MatrixRouterGate`, `BoxV3ShadowGate`.
(Kept in the file as commented one-line rollback options.)

**Why DailyCircuit + NaturalTargetFloor are disabled:**
- `DailyCircuit` was disabled 2026-05-28 to break a stuck circuit-trip
  state during the $5,350 losing-streak recovery. Telegram drawdown
  alerts (every 5 min on −2.7% daily / −6.5% cumulative / circuit trip
  / service pause) provide the same protection without the false-trip
  failure mode.
- `NaturalTargetFloor` was disabled 2026-05-28 because the lab-mined
  per-pair WIN/LOSE rules now encode the same quality bar implicitly.
  Both gates are config-flippable for revival.

## Admission Stack (post-router)

The V3HybridScorer was disabled 2026-05-28: `scan_pipeline.scorer = None`.
Strategy admission is now a three-layer ML stack, all wired in
`bootstrap.py`:

| Layer | Role | Mode | Threshold |
|-------|------|------|-----------|
| 1. Routing table | Per-cell (pair × family × direction × session) allow-list | HARD | (matrix WIN/LOSE rules) |
| 2. LightGBM v0 scorer | Primary admission gate — `p_win` over the candidate | HARD | **0.75** |
| 3. Matrix shadow advisor | Cross-validation against lab matrix + factor_lift | OBSERVE | logs only |
| 4. ml_router | Demoted to shadow after 2026-05-28 | OBSERVE | logs only |

**Model details:**
- LightGBM v0 — version `vv0_2026-05-28`, holdout AUC `0.6025`, threshold
  `0.75` (top ~3% of lab cohort = ~75% sim WR).
- Matrix shadow — loads `data/matrix/optimized_matrix_by_session.csv`
  (3,879 cells) + `data/matrix/factor_lift_table.csv` (162
  pair×strat×dir keys). Verdicts: `MATRIX_PASS` / `MATRIX_NEG_CELL` /
  `NO_CELL_FACTOR_ONLY` / `MATRIX_BLIND`.
- ml_router — previously primary gate, now records its decision to
  `data/ml_router_shadow.jsonl` for cross-comparison only.
- MLStrategyFilter and BranchRouter advisors are conditional loads
  (off by default) — re-enabled via `config.scoring.ml_filter` /
  `config.scoring.branch_router`.

## Management Profiles (position_pipeline.py)

| Profile | early_hold_r | min_sl_step_pips | Used by |
|---------|-------------|------------------|---------|
| `trend_runner` | 0.6 | 4.0 | `dbb_trend` |
| `reversal_core` | 0.5 (default) | 3.0 (default) | `reversal` |
| `default` | 0.5 | 3.0 | all others (incl. promoted strategies) |

Shared across all profiles: `PartialHarvestManager` (TP1 50% close,
pre-placed REDUCE_ONLY limit with GTD), `BreakEvenManager`, `RatchetManager`
(50% lock at 0.5 — reverted from 0.7 experiment 2026-04-30 after
$245/trade degradation), `TrailManager`, `FavorableExitManager`
(conditional), `EmergencyCloseManager`, `StopPlanner`.

## Execution

- Entry: LIMIT orders with GTD (5 min expiry), maker-side pricing
- SL validation: trigger-side + no-man's-zone + spread kill switch
- Harvest: pre-placed REDUCE_ONLY limit at TP1 (50% close), 2-pass orphan
  sweep (`harvest-order-ledger.json` + broker pending walk — hotfix
  2026-04-29 + 2026-04-30)
- Spread monitor: rolling mean, skip entry if spread > 1.5x mean
- Order attribution: `OrderAttributionWriter` keeps a
  `order_id → strategy / candidate / scoring payload` map at
  `data/order-attribution.jsonl`, used by the ML observer + broker-truth
  audit. Patches A + B.right (2026-05-04) — see ADR 3006.

## Runtime Architecture (post-extraction, post-scorer-removal)

```
runtime.py — conductor
├── bootstrap.py — boot all modules + load:
│       routing_table_v10_fast_v1_14b_full_matrix.parquet
│       LightGBM v0 model (advisors/lightgbm_shadow)
│       Matrix shadow advisor (advisors/matrix_shadow)
│       MLStrategyFilter (conditional)
│       BranchRouter (conditional)
├── runtime_context.py — typed dependency container
├── scan_coordinator.py — market data + scan pipeline
│       gate_pipeline (7 gates above, scorer=None)
│       observe() calls for lightgbm_shadow + matrix_shadow + ml_router
├── execution_coordinator.py — order placement
├── position_coordinator.py — management pipeline
├── services/dashboard_bridge.py — UI publishing
├── services/config_watcher.py — hot reload
└── services/state_recovery.py — reconciliation
```

The universe screener was disconnected 2026-05-28 (archived under
`archived/screener_session_filter_2026-05-28/`). A pass-through stub
returns the full 26-pair `CANDIDATE_PAIRS` list — session filtering is
now the routing table's job.

## Dashboard

3 tabs (unchanged):
- **Signals**: per-pair cards — note that the V3 scorer breakdown panel
  shown here is informational only; LightGBM `p_win` is the gating value.
- **Execution**: SL health lights, block reasons, event timeline
- **DBB Trend**: candidate audit table, session/age breakdown

API endpoints: `/api/data`, `/api/execution`

## Telemetry — actual current JSONL ledgers

| File | Purpose |
|------|---------|
| `data/execution-audit.jsonl` | Every SL move / block / hold / harvest |
| `data/dbb-candidate-audit.jsonl` | Every dbb_trend candidate (score, tier, session) |
| `data/lightgbm_shadow.jsonl` | LightGBM `p_win` per scored candidate (gating value) |
| `data/matrix_shadow.jsonl` | Matrix verdict per picked candidate (cross-val) |
| `data/ml_router_shadow.jsonl` | Demoted ml_router decision per candidate |
| `data/order-attribution.jsonl` | order_id → strategy / candidate / scoring payload |
| `data/seed-telemetry.jsonl` | Seed-tier candidate ledger (offline expansion mining) |
| `data/positions.json` | Persisted position tracker |
| `data/cooldowns.json` | Per-(pair,dir) cooldown state |
| `data/daily_circuit.json` | Day-start equity baseline + trip state |
| `data/harvest-order-ledger.json` | Pre-placed harvest LIMIT bookkeeping |
| `data/state.json` | Persisted runtime state |
| `data/alert_state.json` | Telegram drawdown alert dedup state |

## Drawdown Alerting (Telegram)

`scrooge-drawdown-alert.timer` fires every 5 min. Triggers:
- Daily P&L ≤ −2.7%
- Cumulative drawdown ≤ −6.5%
- Service paused or circuit trip
- Service down

State persisted in `data/alert_state.json` (dedup window). See
`/data/obsidian-vault/postmortems/fixes/scrooge-bug-fix-arc-2026-05-25.md`
and the DBB-loser-audit project page for the rationale.

## Universe

26 forex pairs (was 27 in the May 25 spec — one was retired with the
screener disconnect). Pairs: EUR_USD, GBP_USD, USD_JPY, AUD_USD,
USD_CHF, USD_CAD, NZD_USD, USD_MXN, EUR_JPY, GBP_JPY, AUD_JPY, CAD_JPY,
CHF_JPY, NZD_JPY, EUR_GBP, EUR_CAD, EUR_AUD, EUR_NZD, EUR_CHF, GBP_CAD,
GBP_AUD, GBP_NZD, GBP_CHF, AUD_CAD, AUD_NZD, AUD_CHF.

EUR_GBP confirmed data-poor in the matrix (0 factor_lift rows). Routing
table inherits that exclusion implicitly.

## What's NOT live right now (clearing up the May 25 spec)

The May 25 spec described a 14-gate stack and a V3.1 scorer with
session-aware tiering. Both are gone. Specifically retired or disabled:

- V3HybridScorer (`scan_pipeline.scorer = None` since 2026-05-28)
- Session/family threshold tables (no longer the admission gate)
- 5-strategy router with hard-coded BB-state mapping
- HTFTrendFilterGate (HTF alignment is now encoded in the routing table's
  per-cell rules + the LightGBM model's learned weights)
- RegimeCompatGate / RegimeStrategyRouterGate / SubRegimeFilterGate /
  EntryFilterGate / EntryFilterShadowGate
- BoxV3ShadowGate
- 4-layer matrix cascade (SessionFilter / PairFilter / MatrixComboFilter /
  MatrixSignatureFilter)
- Monolith MatrixRouterGate
- Universe screener session filtering

Anything from the May 25 spec not listed under "Active Strategies",
"Routing", "Gate Pipeline", "Admission Stack", "Management",
"Execution", "Runtime Architecture", "Dashboard", or "Telemetry" above
is **not live** as of 2026-05-30.

## Cross-references

- **Architecture decisions:** `docs/decisions/` (ADRs 3010+ cover the
  May 2026 collapse to ML routing — to be backfilled)
- **History:** `docs/history/` (matrix-integration-era retrospective
  pending — to be backfilled)
- **Vault state-of-union:**
  `/data/obsidian-vault/wiki/systems/scrooge-current-state-2026-05-05.md`
  → frozen constraints in `scrooge-frozen-constraints.md`
- **Vault project pages:**
  - `wiki/projects/scrooge-v3-attribution-brokertruth-factors.md`
  - `wiki/projects/scrooge-v3-branch-scorer-research.md`
  - `wiki/projects/scrooge-v3-dbb-loser-audit.md`
  - `wiki/projects/scrooge-v3-harvest-same-cycle-race.md`
  - `wiki/projects/scrooge-v3-stale-harvest-hotfix.md`
- **Strategy promotion postmortem:**
  `wiki/postmortems/fixes/scrooge-v3-strategy-promotion-2026-05-27.md`
