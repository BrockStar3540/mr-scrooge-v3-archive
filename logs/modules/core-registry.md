# core/registry — Developer Log

**File:** `src/scrooge_v3/core/registry.py`

---

## 2026-04-14 — Initial creation

**What:** Central module registry — modules are discovered, not hard-wired.

**Components:**
- `ModuleEntry` dataclass — name, version, enabled, mode, dependencies, config_namespace, instance, health
- `ModuleRegistry` — register, get, get_active, list_all, set_mode, health_summary

**Why:** Blueprint Section 5 — registries replace hard-wired imports. Adding a new strategy or gate means registering it, not editing pipeline code. This directly fixes V2's biggest problem (coordinator surgery for any new engine).

**Decisions:**
- Single registry class with `registry_name` parameter (e.g., "features", "gates", "strategies") rather than separate FeatureRegistry/GateRegistry classes — less code, same capability.
- `get_active()` returns only enabled modules — pipelines iterate active modules without checking enabled flags.
- `set_mode()` automatically sets `enabled=False` when mode is DISABLED — prevents inconsistency between mode and enabled flag.
- `health_summary()` returns HealthStatus per module grouped by registry — dashboard health tab consumes this directly.
- Modules stored with their instance reference — registry is also the DI container.

**Tests:** `tests/unit/test_registry.py` — register/retrieve, active filtering, mode switching, health summary colors.
