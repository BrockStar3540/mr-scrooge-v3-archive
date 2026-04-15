# core/types — Developer Log

**File:** `src/scrooge_v3/core/types.py`

---

## 2026-04-14 — Initial creation

**What:** Created all core type definitions used across V3 modules.

**Types defined:**
- `ModuleMode` (disabled/observe/active)
- `GateMode` (hard/soft/observe)
- `AdvisorMode` (disabled/observe/advisory/weighted/hard_block)
- `HealthColor` (green/yellow/red/gray/blue)
- `HealthStatus` — name, color, reason, last_run, last_success, avg_latency_ms, error_count, mode
- `MarketSnapshot` — symbol, bid, ask, mid, spread, timestamp, candles dict
- `FeatureResult` — name, values dict, computed_at
- `ClassificationResult` — name, label, confidence, metadata
- `SymbolContext` — the single object passed through the pipeline (symbol, snapshot, features, classifications, state, metadata)
- `TradeCandidate` — symbol, direction, strategy, entry/stop/tp prices, size, risk_reward, score, metadata
- `TradeDirection` (long/short)
- `GateResult` — gate_name, passed, mode, reason, metrics
- `OrderState` (created/acknowledged/triggered/filled/cancelled/rejected)
- `OrderPlan` — symbol, direction, entry/stop/tp, size, order_type, metadata
- `StopPlan` — position_id, new_stop, reason, metadata
- `PositionState` — position_id, symbol, direction, entry_price, current_stop, size, unrealized_pnl, opened_at
- `AdvisorResult` — advisor_name, recommendation, confidence, adjustments, metadata

**Why:** Blueprint Section 4 requires formal typed results for all contracts. Everything uses `from __future__ import annotations` for forward-ref support.

**Decisions:**
- Used dataclasses over Pydantic — lighter, no external dependency for core types
- SymbolContext carries features/classifications as dicts keyed by module name — allows dynamic module discovery without hardcoded fields
- TradeCandidate includes both `score` (composite quality) and `risk_reward` (raw RR) — gates and ranker use different ones
