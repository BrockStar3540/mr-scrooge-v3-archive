# core/state — Developer Log

**File:** `src/scrooge_v3/core/state.py`

---

## 2026-04-14 — Initial creation

**What:** Centralized state store replacing V2's scattered dicts.

**Components:**
- `CooldownState` — zone_debounce_until, entry_cooldown_until, metadata
- `SymbolState` — symbol, bb_state, regime, opening_state, structure_state, volatility_state, cooldowns, features, metadata
- `StopState` — current_stop, last_attempt_reason, last_update
- `TradePositionState` — position_id, symbol, direction, entry_price, size, stop, opened_at, metadata
- `StateStore` — symbols dict, positions dict, health dict, counters dict, memories dict, experiments dict + snapshot/persist/restore

**Why:** Blueprint Section 7 — V2's state was scattered across coordinator dicts, ctx objects, and module-local variables. Made debugging, replay, and dashboard queries nearly impossible. One store, typed domains, snapshotable.

**Decisions:**
- `get_symbol()` auto-creates SymbolState on first access — no need for explicit initialization per symbol.
- `snapshot()` returns a JSON-serializable dict — used for both persistence and dashboard API.
- `persist()` writes to a single JSON file — simple and sufficient for restart recovery. Not a database — the bot doesn't need query performance, it needs reliable save/load.
- `restore()` is a stub — full deserialization logic will be implemented per domain as those domains are built.
- State domains include `experiments` and `memories` — these are for the experiment tracker and pattern memory, not yet implemented but the store is ready.

**TODO:**
- Implement full restore() deserialization
- Add state diffing for event-sourced replay
- Add locking if async scan cycles are ever introduced
