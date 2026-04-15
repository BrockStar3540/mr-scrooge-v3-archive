# core/events — Developer Log

**File:** `src/scrooge_v3/core/events.py`

---

## 2026-04-14 — Initial creation

**What:** Typed event bus for decoupled module communication.

**Components:**
- `Event` dataclass — type, timestamp, payload dict, source
- `EventBus` — subscribe per type, subscribe_all (global), emit with error isolation
- 19 pre-defined event type constants (MarketSnapshotReceived through ConfigChanged)

**Why:** Blueprint Section 8 — modules communicate through typed events, not direct calls. This eliminates the V2 coordinator star-topology problem where everything imported everything.

**Decisions:**
- Synchronous bus (not async) — trading decisions must be deterministic and ordered. Async introduces non-determinism in event delivery order that could cause replay divergence.
- Handler exceptions are caught and logged, never propagated — a bad telemetry handler must never crash the trading pipeline.
- `subscribe_all()` exists specifically for audit/telemetry — they need every event without subscribing to each type individually.
- Event types are string constants, not enums — allows modules to define custom event types without modifying the core events file.

**Tests:** `tests/unit/test_events.py` — subscribe/emit, global handler, exception isolation.
