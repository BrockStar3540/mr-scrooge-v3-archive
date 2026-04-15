# core/config — Developer Log

**File:** `src/scrooge_v3/core/config.py`

---

## 2026-04-14 — Initial creation

**What:** Hierarchical config store with dot-path access and JSON persistence.

**Components:**
- `ConfigStore` — load, save, get (dot-path), set (dot-path), section, as_dict

**Why:** Blueprint Section 14 — config must be hierarchical (runtime.broker.strategies.gates...) and hot-reloadable. Every module gets its own config namespace.

**Decisions:**
- Dot-path access (`config.get("strategies.trend_engine.enabled")`) rather than nested dict traversal — cleaner API, matches config file structure.
- JSON-backed, not YAML — zero external dependencies. The default config is `config/default.json`.
- No hot-reload watcher yet — will be added when ConfigChanged events are wired. The `set()` method is ready for it.
- `section()` returns a whole config subtree as a dict — modules can grab their namespace and work with it locally.

**Default config:** `config/default.json` — covers all 11 config groups from the blueprint: runtime, broker, risk, features, classifiers, strategies, gates, execution, advisors, telemetry, dashboard. Every module entry has enabled/mode/parameters.

**TODO:**
- File watcher for hot-reload (emit ConfigChanged event on change)
- Config validation against registered module schemas
- Environment variable overrides (like V2's dataclass approach)
