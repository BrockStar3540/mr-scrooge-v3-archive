# Mr. Scrooge Trading Architecture

type: system
status: active
tags: [scrooge, trading, architecture, forex]

trust:
  score: 90
  confidence: high
  evidence:
    - source: direct codebase review 2026-04-09
      type: firsthand

## Summary
Mr. Scrooge is a box-theory reversal trading system for OANDA forex. V1 (live) is monolithic; V2 (practice) is a modular rewrite. Both share the same core strategy: identify previous-day high/low (PDH/PDL) boxes, wait for price to reach box walls, enter mean-reversion trades with tiered profit extraction.

## Signal Flow Pipeline

Universe Screener (26 pairs → ~8-21 viable)
    ↓
Gates Pipeline (zone → trend → ATR → [sucker_move] → pitchfork → OTR)
    ↓
Signal Engine (rank by score, pick best)
    ↓
Scoring Layer 4 (OANDA truth calibration — ranging, CT combos, signal reweighting)
    ↓
Regime Supervisor (V1+V2: blocks if score < +1, applies +10/-10 scoring adjustment)
    ↓
Execution Router (OANDA market order + native SL/TP)
    ↓
Position Manager (track entry, partials, SL ratchet)
    ↓
SL Limit System [V1 only] (hybrid maker-fill inside native SL)
    ↓
Harvester (30-sec poll, tier-based partial closes)
    ↓
Dashboard (status, decisions, regime visibility)

## V1 vs V2 Module Map

| Component | V1 Location | V2 Location |
|-----------|-------------|-------------|
| Main loop | main.py (~1,700 LOC) | main.py + coordinator.py |
| Config | Inline constants | config.py (40+ typed fields) |
| Gates | gates.py (all-in-one) | gates/ (6 separate dirs) |
| OANDA client | core/oanda_client.py (requests) | core/oanda_client.py (oandapyV20) |
| Execution | core/execution_router.py | core/execution_router.py |
| Regime | regime/supervisor.py (active blocker + scoring input) | regime/supervisor.py (active blocker + scoring input) |
| BB context | regime/bb_context.py | regime/bb_context.py (dual band) |
| Positions | portfolio/trade_manager.py | positions/manager.py + positions/models.py |
| Sizing | Inline in main.py | sizing/calculator.py |
| Quality | quality/ (4 files) | quality/ (4 files) |
| Harvester | harvester/ | harvester/ |
| Box state | Implicit | box/state_machine.py (V2-only) |
| Probes | None | probes/engine.py (V2-only) |
| Health | None | health/monitor.py (V2-only) |
| A/B testing | None | experiments/tracker.py (V2-only) |

## Entry Types
- john_wick — single candle wick rejection at PDH/PDL
- power_of_towers — multi-candle reversal structure at zone
- extreme_reversal — counter-entry on extreme move (added 2026-04-02)

Scoring system recalibrated 2026-04-09 based on 511 V1 + 58 V2 OANDA trades. See [[Mr. Scrooge V1 Scoring System]] and [[Mr. Scrooge V2 Scoring System]].

## Shared Resources
- Venv: ~/mr_scrooge_env symlink → ~/mr_burns_env (both V1 and V2)
- Dashboard: V1's dashboard.py serves both via mr-scrooge-dashboard.service
- Git repos: V1: BrockStar3540/mr-scrooge, V2: BrockStar3540/mr-scrooge-v2 (separate repos since 2026-04-09)

## Copyright Header Requirement
All .py files synced to the Alien Device backup must have the 6-line copyright header.

## Related
- [[Mr. Scrooge V1]]
- [[Mr. Scrooge V2]]
- [[Mr. Scrooge V1 Scoring System]]
- [[Mr. Scrooge V2 Scoring System]]
- [[SL Limit Order System]]
- [[Mr. Scrooge Known Defects]]
- [[OANDA Trading Account]]
