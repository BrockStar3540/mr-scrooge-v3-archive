# Architecture Diagram

Visual map of how Mr. Scrooge V4 works. All diagrams render in GitHub
markdown via Mermaid.

Companion to [`LIVE_SYSTEM_SPEC.md`](LIVE_SYSTEM_SPEC.md) (the textual
"what it does today") and [`STRATEGY_ENCYCLOPEDIA.md`](STRATEGY_ENCYCLOPEDIA.md)
(per-strategy detail).

---

## 1. System overview

How the major modules talk to each other.

```mermaid
flowchart TB
    subgraph Runtime["runtime.py — conductor (232 lines)"]
        BOOT[bootstrap.py<br/>module loader]
        CTX[runtime_context.py<br/>typed DI container]
    end

    subgraph Coordinators
        SCAN[scan_coordinator<br/>features → strategies → gates → admission]
        EXEC[execution_coordinator<br/>LIMIT order placement<br/>+ SL/TP atomic]
        POS[position_coordinator<br/>management pipeline]
    end

    subgraph Services
        DASH[dashboard_bridge<br/>UI publishing]
        CFG[config_watcher<br/>hot reload]
        RECOV[state_recovery<br/>reconciliation]
    end

    subgraph External
        OANDA[(OANDA REST API<br/>practice or live)]
        TG[Telegram<br/>drawdown alerts]
        TIMER[systemd timer<br/>5-min alerter]
    end

    BOOT --> Coordinators
    BOOT --> Services
    CTX --> Coordinators

    SCAN --> EXEC
    EXEC --> POS
    SCAN <--> OANDA
    EXEC <--> OANDA
    POS <--> OANDA

    POS --> DASH
    SCAN --> DASH
    EXEC --> DASH

    TIMER --> TG
    OANDA -.equity .-> TIMER

    style Runtime fill:#1a3a5c,color:#fff
    style Coordinators fill:#2d5a8c,color:#fff
    style Services fill:#3a6b9e,color:#fff
    style External fill:#4d4d4d,color:#fff
```

**Key:** The 232-line conductor `runtime.py` orchestrates three
coordinators (scan / execution / position) plus three services
(dashboard / config / recovery). All broker I/O routes through OANDA
REST. The Telegram alerter is **out-of-process** — it survives the bot
being sick.

---

## 2. Scan-to-execution sequence

What happens for a single market tick, end-to-end.

```mermaid
sequenceDiagram
    autonumber
    participant OANDA
    participant Scan as scan_coordinator
    participant Features
    participant Strategies as 25 strategies
    participant Gates as 7-gate pipeline
    participant Router as MatrixRouter<br/>(routing_table.parquet)
    participant LGBM as LightGBM v0<br/>(p_win ≥ 0.75)
    participant Shadows as matrix_shadow<br/>+ ml_router_shadow
    participant Exec as execution_coordinator

    OANDA->>Scan: M5 tick (26 pairs)
    Scan->>Features: bucketize 14-signature
    Features-->>Scan: BB/BBP/A5/A1/RSI/E20/E50/ZS/SPR/ADR/H20/H60/T1/T4

    loop for each strategy
        Scan->>Strategies: evaluate(features)
        Strategies-->>Scan: candidate or None
    end

    Scan->>Gates: filter candidates (physical-state)
    Note over Gates: cooldown, debounce, expiry,<br/>feature quality, zone cap
    Gates-->>Scan: surviving candidates

    Scan->>Router: per-cell admission lookup
    Router-->>Scan: admitted candidates

    Scan->>LGBM: score each (p_win)
    LGBM-->>Scan: drop if p_win < 0.75

    par parallel observers
        Scan->>Shadows: observe(picked candidate)
        Shadows-->>Scan: (log only, never blocks)
    end

    Scan->>Scan: rank by p_win → best pick
    Scan->>Exec: best candidate
    Exec->>OANDA: LIMIT order + stopLossOnFill + takeProfitOnFill
    OANDA-->>Exec: fill confirmation
    Exec->>Exec: register with position_coordinator
```

**Key:** Strategies emit; gates filter; router admits; LightGBM
scores; shadows record (never block); best pick wins; LIMIT-only
entries with SL/TP atomic (no naked windows).

---

## 3. Admission stack

Four-layer view of how a single candidate gets from "strategy emitted
it" to "broker fills it."

```mermaid
flowchart LR
    C[candidate] --> G{7 physical<br/>gates}
    G -->|fail| X1[blocked]
    G -->|pass| R{MatrixRouter<br/>cell lookup}
    R -->|no rule| X2[blocked]
    R -->|admit| L{LightGBM<br/>p_win ≥ 0.75}
    L -->|< 0.75| X3[blocked]
    L -->|≥ 0.75| RANK[rank by p_win]

    R -.also.-> MS[matrix_shadow<br/>observe-only]
    L -.also.-> MLR[ml_router_shadow<br/>observe-only]

    MS --> JSONL1[(matrix_shadow.jsonl)]
    MLR --> JSONL2[(ml_router_shadow.jsonl)]
    L --> JSONL3[(lightgbm_shadow.jsonl)]

    RANK --> BEST[best pick → execute]

    style X1 fill:#5c1a1a,color:#fff
    style X2 fill:#5c1a1a,color:#fff
    style X3 fill:#5c1a1a,color:#fff
    style BEST fill:#1a5c1a,color:#fff
    style MS fill:#5c5c1a,color:#fff
    style MLR fill:#5c5c1a,color:#fff
```

**Key:** Three parallel observers log to three JSONL ledgers.
Disagreement between LightGBM (gate) and the two shadows is the
highest-information audit signal in the system.

---

## 4. Strategy taxonomy

The ~25 strategies grouped by family. No strategy has privileged
status; the routing table decides which fires for which (pair × regime
× session) cell.

```mermaid
flowchart TB
    ROOT[scrooge.strategies — ~25 modules]

    ROOT --> CONT[Continuation family]
    ROOT --> REV[Reversion family]
    ROOT --> BOX[Box family]
    ROOT --> BREAK[Breakout family]
    ROOT --> OTHER[Other]

    CONT --> dbb_trend
    CONT --> trend_pullback
    CONT --> chaikin_macd_atr
    CONT --> canonical_lien_dbb
    CONT --> trend_aligned_breakout
    CONT --> session_momentum_all

    REV --> reversal
    REV --> compression_reversion
    REV --> MR2[MR2_bb_reversion]
    REV --> MR4[MR4_zscore_extreme]
    REV --> MR5[MR5_williams_extreme]
    REV --> RG1[RG1_range_bound_scalp]
    REV --> CP3[CP3_vol_coil_fade]

    BOX --> box_master_theory
    BOX --> canonical_darvas

    BREAK --> BR2[BR2_vcb<br/>volume compression breakout]
    BREAK --> BR5[BR5_opening_range_breakout]
    BREAK --> CP1[CP1_coil_breakout]
    BREAK --> CP2[CP2_squeeze_momentum]
    BREAK --> session_breakout
    BREAK --> compression_expansion

    OTHER --> ifvg[ifvg — inverse fair value gap]
    OTHER --> direct[direct — fallback]
    OTHER --> TF2[TF2_pullback_EMA20]

    style ROOT fill:#1a3a5c,color:#fff
    style CONT fill:#1a5c3a,color:#fff
    style REV fill:#5c3a1a,color:#fff
    style BOX fill:#5c1a5c,color:#fff
    style BREAK fill:#3a5c1a,color:#fff
    style OTHER fill:#5c5c5c,color:#fff
```

**Note:** Box reversal (`box_master_theory`) — originally the V1
flagship strategy — is now one entry of ~25, same template as every
other. Its detailed historical doctrine is preserved at
[`docs/archive/MASTER_THEORY_v1-box-reversal-origin-2025.md`](archive/MASTER_THEORY_v1-box-reversal-origin-2025.md).

---

## 5. Data flow — corpus to admission

How market data becomes admission decisions, end-to-end.

```mermaid
flowchart TB
    subgraph DataAcquisition[1. Data acquisition]
        CANDLES[OANDA REST<br/>M5 + H1 + D1 candles<br/>27 pairs × 6mo]
        CACHE[(parquet cache)]
        CANDLES --> CACHE
    end

    subgraph FeatureEng[2. Feature engineering]
        CACHE --> BUCKETS[factor_buckets v3<br/>14-bucket signature]
        BUCKETS --> SIGS[trade signatures]
    end

    subgraph LabHarness[3. Lab harness]
        SIGS --> HARNESS[backtesting.py wrapper<br/>per strategy × pair × direction]
        HARNESS --> OUTCOMES[per-trade outcomes<br/>~838k trades]
    end

    subgraph Mining[4. Mining]
        OUTCOMES --> MATRIX[factor_lift_table.csv<br/>+ optimized_matrix.csv]
        OUTCOMES --> KMEANS[KMeans 20 regimes/pair]
        KMEANS --> CENTROIDS[regime_centroids.csv]
        OUTCOMES --> RULES[master_rules.csv<br/>WIN/LOSE per cell]
        CENTROIDS --> RULES
    end

    subgraph Models[5. Models]
        OUTCOMES --> LGBM_TRAIN[LightGBM training<br/>holdout 80/20]
        LGBM_TRAIN --> LGBM_MODEL[lgbm_v0/model.txt]
    end

    subgraph Assembly[6. Routing table assembly]
        MATRIX --> ROUTING[routing_table.parquet<br/>1737 rows / 250 leaves]
        RULES --> ROUTING
    end

    subgraph Live[7. Live admission]
        ROUTING --> ADMIT[MatrixRouter at scan time]
        LGBM_MODEL --> SCORE[LightGBM at scan time]
        ADMIT --> DECISION[admit / reject / shadow log]
        SCORE --> DECISION
    end

    style DataAcquisition fill:#1a3a5c,color:#fff
    style FeatureEng fill:#2d5a8c,color:#fff
    style LabHarness fill:#3a6b9e,color:#fff
    style Mining fill:#5c3a1a,color:#fff
    style Models fill:#5c5c1a,color:#fff
    style Assembly fill:#1a5c3a,color:#fff
    style Live fill:#1a5c5c,color:#fff
```

**Key:** Steps 1-6 are the lab pipeline (offline, periodic rebuilds).
Step 7 is live admission (continuous, runs every scan cycle). The lab
artifacts (`routing_table.parquet`, `lgbm_v0/model.txt`, per-pair
modules, matrix CSVs) are the bridge.

---

## 6. Evolution — V1 to V4

The chronology of how the architecture got here. Each era's
[history doc](history/) and [ADR set](decisions/) carries the detail.

```mermaid
timeline
    title Mr. Scrooge architectural evolution
    section V1 (Feb 2026)
        Box reversal doctrine : Single strategy
                              : 6 hand-tuned gates
                              : MASTER_THEORY canonical
    section V2 (Mar 2026)
        Modular rewrite       : 232-line conductor
                              : Dual-loop (5min + 3sec)
                              : 4-guard StopPlanner
                              : Mr Sprite removed
    section V3 (Apr 2026)
        Hybrid scorer         : V3HybridScorer
                              : Family-aware overlays
                              : 14-gate pipeline
                              : 3 active strategies
    section V3.5 (May 2026)
        Regime + routing      : MatrixRouter
                              : factor_buckets v3
                              : LightGBM v0 shadow
                              : 6 strategies promoted
    section V3.6 (late May 2026)
        ML routing collapse   : V3HybridScorer DISABLED
                              : LightGBM PRIMARY @ 0.75
                              : Matrix shadow added
                              : 13 strategies live
    section V4 (publish)
        Consolidation         : 25 strategies equal footing
                              : MASTER_THEORY demoted
                              : MIT license, public
                              : src/scrooge/ (no version suffix)
```

**Key:** V1 → V4 is a 4-month arc. The dominant move was *from
hand-tuned scoring to lab-mined routing* — V3HybridScorer's death
(ADR 3017, May 28) was the watershed. V4 freezes this architecture
for publication; future iteration happens *within* this frame, not
*replacing* it.

---

## 7. Telemetry — what gets logged where

Every admitted trade leaves a trail across multiple ledgers.

```mermaid
flowchart LR
    SCAN[scan cycle] --> AUDIT[(execution-audit.jsonl<br/>SL moves, blocks, holds)]
    SCAN --> DBB[(dbb-candidate-audit.jsonl<br/>per-strategy candidates)]
    SCAN --> LSHADOW[(lightgbm_shadow.jsonl<br/>p_win per candidate)]
    SCAN --> MSHADOW[(matrix_shadow.jsonl<br/>matrix verdict per pick)]
    SCAN --> ROUTERSHADOW[(ml_router_shadow.jsonl<br/>demoted router decision)]
    SCAN --> SEED[(seed-telemetry.jsonl<br/>seed-tier ledger)]

    EXEC[execution] --> ATTRIB[(order-attribution.jsonl<br/>order_id → strategy)]
    EXEC --> POS[(positions.json<br/>persistent state)]

    POS --> COOLDOWN[(cooldowns.json)]
    POS --> CIRCUIT[(daily_circuit.json)]
    POS --> HARVEST[(harvest-order-ledger.json)]
    POS --> STATE[(state.json)]

    TIMER[systemd 5min] --> ALERT[(alert_state.json)]

    style AUDIT fill:#1a3a5c,color:#fff
    style ATTRIB fill:#5c3a1a,color:#fff
    style ALERT fill:#5c1a1a,color:#fff
```

**Key:** `order-attribution.jsonl` is the load-bearing audit artifact
— it links every broker fill back to its scoring snapshot (Patches A
+ B.right + C, [ADR 3006](decisions/3006-b1-attribution-architecture.md)).
Without it, broker-truth audits can't reliably split outcomes by
strategy.

---

## Diagram-rendering notes

All diagrams use Mermaid syntax and render natively in GitHub
markdown — no external tooling required. To regenerate as standalone
images (for slide decks or documentation outside this repo), use
either the [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli) or
the official [Mermaid Live Editor](https://mermaid.live).

Diagrams are kept deliberately *coarse-grained*. Per-module detail
lives in [`LIVE_SYSTEM_SPEC.md`](LIVE_SYSTEM_SPEC.md); per-strategy
detail lives in [`STRATEGY_ENCYCLOPEDIA.md`](STRATEGY_ENCYCLOPEDIA.md);
per-decision detail lives in [`decisions/`](decisions/). These
diagrams are for orientation, not specification.
