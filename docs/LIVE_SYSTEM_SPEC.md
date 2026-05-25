# Live System Specification

> **This is the executable truth.** Not theory, not doctrine — what the system
> actually does right now. Updated 2026-05-25.

---

## Active Strategies

| Strategy | Name | Status | BB States | Management Profile |
|----------|------|--------|-----------|-------------------|
| Reversal | `reversal` | Active | EXTREME_UP/DOWN, REJECTION_SHORT/LONG | `reversal_core` |
| DBB Trend | `dbb_trend` | Active | TREND_UP/DOWN, BREAKOUT_UP/DOWN, STRETCH_DOWN | `trend_runner` |
| Direct | `direct` | Active | All routed states (fallback) | `default` |
| Trend (old) | `trend` | **Disabled** | — | — |
| Gap | `gap` | **Disabled** | — | — |
| Measured Move | `measured_move` | **Disabled** | — | — |

## Strategy Router (actual code)

```
EXTREME_UP/DOWN       → [reversal, direct]
REJECTION_SHORT/LONG  → [reversal, direct]
TREND_UP/DOWN         → [dbb_trend, direct]
BREAKOUT_UP/DOWN      → [dbb_trend, direct]
STRETCH_UP            → [] (hard blocked)
STRETCH_DOWN          → [dbb_trend, direct]
NORMAL                → [direct]
COMPRESSION           → [direct]
```

No strategy self-activates outside router permission.

## Live Gates (bootstrap.py) — updated 2026-05-25

**14 gates registered** in runtime (was 3 in April spec — major expansion through May).

| # | Gate | Mode | Behavior |
|---|------|------|----------|
| 1 | `DailyCircuitGate` | HARD | Daily P&L circuit breaker |
| 2 | `CooldownGate` | HARD | Per-(pair,dir) cooldown after stops |
| 3 | `DebounceGate` | HARD | Prevent re-entry at same zone within window |
| 4 | `ExpiryBackoffGate` | HARD | Cool down after LIMIT expiries at a zone |
| 5 | `RegimeFloorGate` | HARD | Blocks if regime53 score < -4 |
| 6 | `NaturalTargetFloorGate` | HARD | Block if market projection (M5 ATR*3 vs BB width/2, MIN) < 7 pips |
| 7 | `FeatureQualityFloorGate` | HARD | Block if EMA/RSI/zone_detector returned degraded defaults |
| 8 | `ZoneEntryCapGate` | HARD | Max N entries per zone+direction per day |
| 9 | `RegimeCompatGate` | observe | Per-(regime,family,dir) compatibility classifier (observe-only) |
| 10 | `RegimeStrategyRouterGate` | HARD | (regime53,family,dir_vs_hint) allow-list router |
| 11 | `SubRegimeFilterGate` | HARD | Veto bottom MTB sub-regimes; routing-cell override at trade-tier |
| 12 | `EntryFilterGate` | HARD | Per-strategy routing-cell match (exact_strategy / exact_family); `family_loose_override` config-gated default OFF |
| 13 | `BoxV3ShadowGate` | observe | Box-branch shadow scorer |
| 14 | `EntryFilterShadowGate` | observe | Shadow routing slate (v9_observe) for parallel evaluation |

**HARD = veto on fail. observe = log only, no block.**

**Recent gate additions (2026-05-25):**
- `NaturalTargetFloorGate` — recomputes per-symbol per-cycle market projection from live M5 ticks; blocks ALL strategies on a symbol whose realistic move-potential is below the 7-pip scalp floor.
- `FeatureQualityFloorGate` — blocks candidates on symbols where EMA/RSI/zone_detector returned insufficient-bars defaults (formerly silently consumed by scorer as if real).

**Recent default changes (2026-05-25):**
- `EntryFilter.enable_family_loose_override` defaults `false` — was permitting cross-family cell approvals on live trade-tier entries (P2 audit finding).

See `/data/obsidian-vault/postmortems/scrooge-bug-fix-arc-2026-05-25.md` for the full 2026-05-25 arc.

## V3.1 Scorer

### Architecture
- Layer 0: Hard blocks (RSI neutral, STR_UP, duration ≥12h, stale+EMA20)
- Layer 1: 17 single-factor points (decompressed from V3.0)
- Layer 2: 15 paired-aspect bonuses/penalties (halved magnitudes)
- Family overlays: trend candidates get +6/+4/+2/+2/+3/-5 adjustments
- Session-aware thresholds: 5 sessions × 2 families

### Score Scale Warning

V3.1.1 uses a **lower operating score scale** than the original V3.0 documented
in SCORING_V3_LIVE.md. Scores like 42, 50, 56 are meaningful under the current
system. Do NOT compare live scores to the old V3.0 documentation which used
floors of 40-50 and final thresholds of 60-75.

**Calibration status:** Current thresholds were calibrated on a 50-trade
executed-trade dataset (survivor-biased). Full calibration requires a
candidate-level replay dataset. Current thresholds are a live hypothesis
under forward validation, not a proven optimum.

### Session Rules (default family) — V3.1.1 recalibrated

| Session | Hours UTC | Base Floor | B Tier | A Tier | Pair Cap |
|---------|-----------|-----------|--------|--------|----------|
| Asia/London Open | 0-7 | 30 | 44 | 54 | 16 |
| London | 8-11 | 32 | 44 | 54 | 12 |
| NY Active | 12-17 | 30 | 42 | 50 | 12 |
| Late NY | 18-19 | 34 | 44 | 54 | 10 |
| Dead Late | 20-23 | 40 | 52 | 62 | 8 |

### Trend Family Thresholds (lower)

| Session | Base Floor | B Tier | A Tier | Pair Cap |
|---------|-----------|--------|--------|----------|
| Asia/London Open | 28 | 42 | 52 | 16 |
| London | 30 | 42 | 52 | 12 |
| NY Active | 28 | 40 | 48 | 12 |
| Late NY | 32 | 42 | 52 | 10 |
| Dead Late | 38 | 50 | 60 | 8 |

### Trend Family Overlays
- Structure break confirmed: +6
- DBB_PULLBACK with depth ≤55%: +4
- DBB_BREAKOUT: +4
- Directional candles ≥4: +2
- Hour 16-19 UTC softening: +2
- Box age 18-24h softening: +3
- Exhausted chase (z≥1.5 + ema20<15): -5

## Management Profiles (position_pipeline.py)

| Profile | early_hold_r | min_sl_step_pips | Used by |
|---------|-------------|------------------|---------|
| `trend_runner` | 0.6 | 4.0 | dbb_trend |
| `reversal_core` | 0.5 (default) | 3.0 (default) | reversal |
| `default` | 0.5 | 3.0 | direct |

Shared management for all profiles: harvest, BE, ratchet, trail, favorable exit, emergency close.

## Execution

- Entry: LIMIT orders with GTD (5 min expiry), maker-side pricing
- SL validation: trigger-side + no-man's-zone + spread kill switch
- Harvest: pre-placed REDUCE_ONLY limit at TP1 (50% close)
- Spread monitor: rolling mean, skip entry if spread > 1.5x mean

## Runtime Architecture (post-extraction)

```
runtime.py (232 lines) — conductor
├── bootstrap.py (262) — boot all modules
├── runtime_context.py (43) — typed dependency container
├── scan_coordinator.py (125) — market data + scan pipeline
├── execution_coordinator.py (131) — order placement
├── position_coordinator.py (185) — management pipeline
├── services/dashboard_bridge.py (97) — UI publishing
├── services/config_watcher.py (53) — hot reload
└── services/state_recovery.py (155) — reconciliation
```

## Dashboard

3 tabs:
- **Signals**: per-pair cards with V3 scorer breakdown
- **Execution**: SL health lights, block reasons, event timeline
- **DBB Trend**: candidate audit table, session/age breakdown

API endpoints: `/api/data`, `/api/execution`

## Telemetry

- `data/execution-audit.jsonl` — every SL move/block/hold/harvest
- `data/dbb-candidate-audit.jsonl` — every dbb_trend candidate with score/tier
- `data/positions.json` — persisted position tracker
- `data/state.json` — persisted runtime state
- `data/replay/` — session replay JSONL files
