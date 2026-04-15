# core/contracts — Developer Log

**File:** `src/scrooge_v3/core/contracts.py`

---

## 2026-04-14 — Initial creation

**What:** Defined all 7 module contracts as Python Protocol classes.

**Contracts:**
1. `FeatureModule` — `compute(symbol, snapshot, state) -> FeatureResult`
2. `ClassifierModule` — `classify(ctx) -> ClassificationResult`
3. `StrategyModule` — `eligible(ctx) -> bool` + `evaluate(ctx) -> TradeCandidate | None`
4. `GateModule` — `evaluate(candidate, ctx) -> GateResult`
5. `ExecutionPolicy` — `plan_entry(candidate, ctx) -> OrderPlan` + `plan_stop_update(position, ctx) -> StopPlan`
6. `AdvisorModule` — `advise(ctx, candidate) -> AdvisorResult`
7. `HealthCheckModule` — `probe() -> HealthStatus`

**Why:** Blueprint Section 4 — every module type gets a formal interface. Using Protocol (structural subtyping) rather than ABC so modules don't need to inherit from a base class. Any object with the right methods satisfies the contract.

**Decisions:**
- FeatureModule takes `symbol + snapshot + state` (not SymbolContext) because features compute before the context is built
- StrategyModule has both `eligible()` and `evaluate()` — the router calls `eligible()` first, only calls `evaluate()` if True. This prevents expensive computation for strategies that aren't applicable.
- AdvisorModule receives `candidate | None` because advisors can advise on market conditions even when no candidate exists (e.g., "don't trade right now")
- All contracts have a `name: str` attribute for registry identification
