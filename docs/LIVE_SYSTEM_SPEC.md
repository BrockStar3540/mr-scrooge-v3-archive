# Live System Specification

> **This is the executable truth.** Not theory, not doctrine — what the system
> actually does right now. Updated 2026-04-16.

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

## Live Gates (bootstrap.py)

Only 3 gates are registered in runtime:

| Gate | Config | Behavior |
|------|--------|----------|
| `RegimeFloorGate` | `min_score: -4` | Blocks if regime score < -4 (BLOCKED state) |
| `DebounceGate` | from config | Prevents re-entry at same zone within 20 min |
| `ZoneEntryCapGate` | from config | Max 3 entries per zone+direction per day |

**Not live (handled by V3 scorer instead):** spread, OTR, RR, exhaustion, nat_stop_validity, spread_vs_stop.

## V3.1 Scorer

### Architecture
- Layer 0: Hard blocks (RSI neutral, STR_UP, duration ≥12h, stale+EMA20)
- Layer 1: 17 single-factor points (decompressed from V3.0)
- Layer 2: 15 paired-aspect bonuses/penalties (halved magnitudes)
- Family overlays: trend candidates get +6/+4/+2/+2/+3/-5 adjustments
- Session-aware thresholds: 5 sessions × 2 families

### Session Rules (default family)

| Session | Hours UTC | Base Floor | B Tier | A Tier | Pair Cap |
|---------|-----------|-----------|--------|--------|----------|
| Asia/London Open | 0-7 | 36 | 50 | 60 | 16 |
| London | 8-11 | 38 | 50 | 60 | 12 |
| NY Active | 12-17 | 36 | 48 | 56 | 12 |
| Late NY | 18-19 | 40 | 50 | 60 | 10 |
| Dead Late | 20-23 | 46 | 58 | 68 | 8 |

### Trend Family Thresholds (lower)

| Session | Base Floor | B Tier | A Tier | Pair Cap |
|---------|-----------|--------|--------|----------|
| Asia/London Open | 34 | 48 | 58 | 16 |
| London | 36 | 48 | 58 | 12 |
| NY Active | 34 | 46 | 54 | 12 |
| Late NY | 38 | 48 | 58 | 10 |
| Dead Late | 44 | 56 | 66 | 8 |

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
