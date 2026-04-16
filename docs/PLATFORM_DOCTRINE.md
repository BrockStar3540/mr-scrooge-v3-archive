# Mr. Scrooge V3 — Platform Doctrine

> Mr. Scrooge is no longer a single reversal bot. It is a regime-aware trading
> platform. Market state determines which strategy families are eligible.
> Strategy modules generate candidates. A shared execution and management kernel
> handles all live positions under one audited, replayable, safety-first lifecycle.

---

## 1. Governing Rules

### Rule 1: No strategy may self-activate outside router permission

The strategy router takes classification state (BB state, regime, structure, session,
spread environment) and outputs a set of allowed strategy families. No strategy module
may generate candidates unless the router has explicitly permitted it for the current
symbol context.

### Rule 2: No strategy may own a private management loop

All filled positions return to PositionPipeline for shared management:
harvest, break-even, ratchet, trailing, favorable exit, emergency close.
No strategy may run its own stop management, TP management, or close logic.

### Rule 3: Every strategy must declare a management profile

Entry logic alone is insufficient. Each strategy must specify:
- harvest style (aggressive/patient)
- ratchet parameters (lock %, min pips)
- break-even rules (trigger distance, offset)
- trail style (candle-following, ATR-based, fixed-pip)
- stale timeout (max hold duration before forced review)
- invalidation conditions (when the setup thesis is broken)

---

## 2. Architecture: Strategy-Specific Entry, System-Wide Management

### Strategy modules own:
- Setup recognition
- Eligibility logic (within router permission)
- Entry trigger and order type
- Structural stop proposal
- Target model (TP1, TP2)
- Strategy metadata (management profile, entry context)

### Shared platform owns:
- Spread validation and spread monitor
- Executable stop validation (trigger-side, no-man's-zone)
- Order lifecycle (limit entry, GTD, fill reconciliation)
- Position state tracking (TrackedPosition persistence)
- Profit-phase management (EARLY_HOLD / LOCK / HARVEST)
- Partial harvest (TP1)
- Break-even management
- Ratchet stop (profit locking)
- Trailing stop (candle structure following)
- Favorable exit (limit order for better fill)
- Emergency close (circuit breaker)
- Execution audit (JSONL + dashboard)
- Replay and telemetry

---

## 3. Classification Layer

Market state is determined by multiple independent classifiers, not a single scalar.

### Structure state
Ranging / breach / confirmed break / alt-box / invalid

### Behavior state (BB classifier)
NORMAL / EXTREME / REJECTION / STRETCH / BREAKOUT / COMPRESSION

### Regime hostility
NORMAL (>=0) / CAUTION (>=-2) / RESTRICTED (>=-4) / BLOCKED (<-4)

Regime signals: box acceptance, rejection decay, expansion pressure, qualified
failures, breadth, quality pressure, BB context.

### Session state
Asia-London open (0-7 UTC) / London (8-11) / NY active (12-17) / Late NY (18-19) / Dead late (20-23)

### Execution environment
Spread normal / elevated / hostile. Rolling mean from SpreadMonitor.

---

## 4. Router: Sets Not Winners

The router outputs **a set of allowed strategy families**, not a single trade.

Current routing (from strategy_router.py + BB state):

| BB State | Allowed Strategies |
|----------|-------------------|
| EXTREME_UP, EXTREME_DOWN | reversal, direct |
| REJECTION_SHORT, REJECTION_LONG | reversal, direct |
| TREND_UP, TREND_DOWN | dbb_trend, direct |
| BREAKOUT_UP, BREAKOUT_DOWN | dbb_trend, direct |
| NORMAL | direct |
| COMPRESSION | direct |
| STRETCH_UP | (none — hard blocked) |
| STRETCH_DOWN | dbb_trend, direct |

Old TrendStrategy (SMA20 pullback) disabled as of 2026-04-16. DBB Trend owns
the continuation lane exclusively.

Future: router should also incorporate regime state for strategy-regime
compatibility (e.g., RESTRICTED regime + reversal = reject or heavy penalty).

---

## 5. Strategy Menu (Current + Planned)

| Strategy | Status | Entry Logic | Management Profile |
|----------|--------|-------------|-------------------|
| Reversal | Active | Box boundary rejection, pitchfork entry | Harvest early, ratchet fast, tight trail |
| Trend (FULL) | Active | Trend continuation with 50% size | Patient harvest, wider ratchet, candle trail |
| Trend (STRETCH) | Active | Trend extension with 30% size | Very patient, wide trail, time-limited |
| Direct | Active | Score-driven entry without specific pattern | Default management profile |
| Gap/Opening | Planned | Session open dislocation | Quick harvest, tight management |
| Measured Move | Planned | AB=CD continuation pattern | Target-driven, less trailing |
| Vol Breakout | Planned | Compression → expansion entry | Hold through expansion, wide initial stop |

---

## 6. Management Profiles

Shared PositionPipeline uses strategy metadata to parameterize behavior:

```
management_profile: reversal_scalp
  harvest_fraction: 0.50
  harvest_at: tp1 (box center)
  be_trigger_pips: 5
  ratchet_lock_pct: 0.50
  ratchet_min_pips: 6
  trail_style: hourly_candle
  max_hold_hours: 48

management_profile: trend_runner
  harvest_fraction: 0.50
  harvest_at: tp1 (1R target)
  early_hold_threshold_r: 0.6 (more patience than reversal)
  min_sl_step_pips: 4.0 (wider steps, less thrashing)
  be_trigger_pips: 8
  ratchet_lock_pct: 0.40
  ratchet_min_pips: 10
  trail_style: hourly_candle_wide
  max_hold_hours: 96

management_profile: default
  harvest_fraction: 0.50
  harvest_at: tp1
  be_trigger_pips: 5
  ratchet_lock_pct: 0.50
  ratchet_min_pips: 6
  trail_style: hourly_candle
  max_hold_hours: 48
```

---

## 7. Scoring: V3.1 Rebalanced Engine

The V3 scorer evaluates candidates after router permission and gate passage.

Key V3.1 changes (2026-04-16):
- 5 session buckets with independent thresholds
- Hour/age penalties decompressed (NY no longer starved)
- Directional candles = strongest soft factor
- Weak factors (wall, ADR, OTR) reduced
- Pair layer halved (confirmation not rescue)
- Correlated-negative caps prevent triple-dipping
- OTR<8+NORM hard block removed (soft penalty only)

See docs/SCORING_V3_LIVE.md for full formula specification.

V3.1.1 addition: scorer is now **strategy-family-aware**:
- Trend candidates get +6 structure break, +4 pullback/breakout mode, +2 dc conviction
- Trend candidates get softened NY/stale penalties (+2 hr, +3 age for continuation)
- Trend candidates get separate session thresholds (lower floors)
- Exhausted chase penalty: -5 if z>=1.5 and ema20<15
- Reversal candidates: unchanged (no family overlays applied)

---

## 8. Future: Regime-Strategy Compatibility Layer

The missing middle layer between regime classification and strategy scoring.

**Not yet implemented.** When added, it should:

- Score regime-strategy FIT, not just regime hostility
- Use regime reason decomposition (acceptance, expansion, failures, breadth)
- Apply differently per strategy family:
  - Reversal + expansion_pressure = strong negative
  - Trend + expansion_pressure = possibly positive
  - Reversal + compression = positive
  - Reversal + failed_rejections = strong negative
- Live as a pre-scorer filter or scorer modifier, not a hard gate

This avoids the old mistake of one scalar regime score blocking everything.

---

## 9. What This Doctrine Replaces

The old V1/V2 model was:
- One reversal strategy trying to do everything
- Regime as a blunt global gate (score < -1 = no trades)
- Separate harvester daemon with conflicting stop logic
- No strategy-specific management parameters
- No execution audit or replay capability

The V3 model is:
- Multiple strategy families, each with defined scope
- Regime as a routing input and compatibility signal
- One PositionPipeline for all management
- Strategy-declared management profiles
- Full execution audit with JSONL + dashboard
