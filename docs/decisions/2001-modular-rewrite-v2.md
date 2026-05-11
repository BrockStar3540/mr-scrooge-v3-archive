# 2001. V2 modular rewrite (38/38 modules clean)

**Status:** Accepted (V2 active Mar 21 - Apr 15; effectively decommissioned with V3 transition)
**Date:** 2026-03-21 (commit `d28e98b`)
**Version scope:** V2
**Backfilled:** 2026-05-11

## Context

By late March 2026, V1's monolithic structure was straining:
- `gates.py` was 139 KB
- `main.py` was 97 KB
- `dashboard.html` was 1063 lines + 311 lines of dashboard.py
- Strategy/execution/management/UI all entangled in main.py
- AUDIT.md fixes were accumulating in a flat list because there was nowhere clean to put them

A modular rewrite was attempted in parallel: V2.

## Decision

Build V2 as a parallel codebase with strict modular separation:

- **`box/`** — box state machine, models
- **`experiments/`** — research-stage features, isolated from production paths
- **`coordinator.py`** (632 lines) — replaces large chunks of main.py
- **`alerts.py`** — alerting separated from main loop
- **`positions/`** — position models, manager
- **`core/`** — broker client, execution router, fee calculator (preserved from V1, refactored)

Stated outcome: **"38/38 modules clean."** Single commit (`d28e98b`).

Removed in the rewrite:
- Monolithic `dashboard.html` / `dashboard.py` (consolidated)
- Old `AUDIT.md`, `README.md`, `SCROOGE.md` (replaced with `NOTES.md` running log)

## Alternatives considered

- **Incremental refactor of V1** — rejected. The entanglement was deep; one-at-a-time refactors would have churned for months. Big-bang was faster but riskier.
- **Skip V2 entirely; go directly to V3** — not yet conceived in March; V3 emerged later.
- **Keep V1 monolithic and add modules around it** — rejected. New code would just inherit the entanglement.

## Consequences

**Enabled:**
- Clean module boundaries for the Fast Execution Loop (ADR 2002) and TradeCoordinator (ADR 1010 — implemented in both V1 and V2 simultaneously after the rewrite).
- The V2 architecture became the conceptual base for V3 (`mr-scrooge-v3` repo's runtime.py + bootstrap.py + coordinator pattern).

**Closed:**
- Monolithic V1 structure. Future development happens on modular surfaces.

**Costs:**
- V2 inherited V1's strategy logic but not its battle-testing. Bug B-054 (4.5-hour silent skip from `return None` indentation in coordinator.py) shipped within 3 days of V2 build. **The clean module structure didn't prevent dumb bugs.**
- Maintaining V1 + V2 in parallel doubled the surface area for ~3 weeks until V3 took over.

## Survival into V3

V3's architecture (in `mr-scrooge-v3` repo) is structurally V2's children:
- `runtime.py` (232 lines) = thin conductor (like V2's main.py minus coordinator)
- `bootstrap.py` (262 lines) = module registration
- `scan_coordinator.py` / `execution_coordinator.py` / `position_coordinator.py` = direct descendants of V2's coordinator.py split into responsibility-focused chunks

V2 was the bridge. Not bad code; just temporary.

## Cross-references

- `BrockStar3540/mr-scrooge` commit `d28e98b`
- `[[scrooge-bug-catalog]]` B-054 (V2 silent skip — clean modules don't prevent dumb bugs)
- V3 runtime architecture: `[[mr-scrooge-architecture]]`
