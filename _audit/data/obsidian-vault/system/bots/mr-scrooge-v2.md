# Bot: Mr. Scrooge V2

type: system
status: active
tags: [scrooge, trading, bot, forex, oanda, v2]

trust:
  score: 95
  confidence: high
  evidence:
    - source: live production system on practice account, OANDA audit 2026-04-09
      type: firsthand

## Summary
Mr. Scrooge V2 — modular rewrite of the trading bot running on OANDA practice account (~$87K equity as of 2026-04-09). Coordinator architecture with 85 tracked files. Adds box state machine, liquidity probes, health monitoring, A/B testing, and dual Bollinger Band regime analysis. Scoring system recalibrated 2026-04-09 from OANDA trade data (Layer 4 OANDA-truth adjustments). Regime supervisor is an ACTIVE entry blocker (since 2026-03-31).

## WARNING: Position Sizing
V2 sizes positions at ~27x V1 (530K-3.28M units vs 19K-77K). A single SL hit can lose $1,000-6,000+ on V2 vs $50-80 on V1. This is by design — the strategy trades large and uses the ratchet/harvest/limit system to manage risk post-entry.

## Location
- **Code:** EC2 `~/.openclaw/workspace/agents/mr-scrooge-v2/`
- **GitHub:** `BrockStar3540/mr-scrooge-v2` (own repo, fine-grained token `GITHUB_TOKEN_SCROOGE_V2`)
- **Alien Device:** `/Volumes/Alien Device/mr-scrooge-v2/` — `alien` remote configured, `receive.denyCurrentBranch=updateInstead`
- **Deploy:** EC2 is truth. `git push origin main` (GitHub) + `git push alien main` (Alien Device)

## Systemd Services (EC2, user mode)

| Service | Purpose |
|---------|---------|
| `mr-scrooge-v2.service` | Main trading bot (5-min cycle + 3-sec fast execution thread) |
| `mr-scrooge-v2-harvester.service` | Profit harvester (30-sec poll) |
| Dashboard: uses V1's `mr-scrooge-dashboard.service` | SHARED — see [[Mr. Scrooge Dashboard Operations]] |

## Scoring System (Recalibrated 2026-04-09)

Calibrated from 58 V2 + 511 V1 OANDA trades. See [[Mr. Scrooge V2 Scoring System]] for full details.

| Layer | Purpose |
|-------|---------|
| Layer 1 | Validity pre-filter (z-direction, ADR ceiling, low extreme) |
| Layer 2 | Base scoring (tier, ATR, OTR, R:R, signal type: john_wick +15, power_of_towers +5) |
| Layer 3 | Contextual modifiers (z-score, BB position, touches, gap) |
| Layer 4 | OANDA truth: ranging -20, CT+PoT -15, CT+JW -5, CT T1 -10, CT T2 +5, z-align +5 |
| Regime | NORMAL +10, CAUTION -5, RESTRICTED -10 (rebalanced 2026-04-13, category-capped) |

R:R: Hard gate uses TP2 (min 1.35 (lowered from 1.60 on 2026-04-13)). Scoring uses TP1 (realistic target).

## Architecture (vs V1)

| Aspect | V1 | V2 |
|--------|----|----|
| Structure | Monolithic main.py (~1,800 LOC) | Coordinator + 14 subsystems (85 files) |
| Gates | All in gates.py | 6 separate dirs: zone, trend, atr, sucker_move, pitchfork, otr |
| Box tracking | Implicit | Explicit BoxStateMachine (IN_BOX, BREACH_PENDING, BROKEN, SHELVED) |
| Probes | None | Liquidity sweep pre-confirmation limit orders (disabled) |
| Health | None | Per-component GREEN/YELLOW/RED + circuit breakers |
| A/B testing | None | Experiments framework (opt-in per gate) |
| Regime | Score-based blocker | ACTIVE blocker (since 2026-03-31) + scoring input (+10/-10). See [[Mr. Scrooge V2 Regime System]] |
| SL limit | In main.py | In coordinator.py (same logic, different location) |
| Git | Isolated repo (BrockStar3540/mr-scrooge) | Isolated repo (BrockStar3540/mr-scrooge-v2) |

## Module Structure

| Directory | Contents |
|-----------|----------|
| `main.py` | Entrypoint, boots Coordinator, logging setup |
| `config.py` | 40+ typed fields, SCROOGE_* env overrides |
| `coordinator.py` | Master orchestrator, owns all runtime state, fast execution thread |
| `core/` | oanda_client.py, execution_router.py, fee_calculator.py |
| `gates/` | 6 gate dirs: zone_gate/, trend_gate/, atr_gate/, sucker_move_gate/, pitchfork_gate/, otr_gate/ |
| `signals/` | engine.py (scoring + gate orchestration), models.py, extreme_reversal.py |
| `positions/` | models.py (OpenPosition with pip_value_per_unit), manager.py |
| `sizing/` | calculator.py (margin-based, risk-capped) |
| `box/` | models.py, state_machine.py — box breach tracking |
| `probes/` | models.py, engine.py — liquidity sweep orders (disabled) |
| `regime/` | supervisor.py (ACTIVE), models.py, bb_context.py (dual BB) |
| `health/` | models.py, monitor.py — component health + circuit breakers |
| `quality/` | tracker.py, indicators.py, models.py, entry_context.py |
| `experiments/` | models.py, tracker.py — A/B testing |
| `harvester/` | main.py, start.sh, harvester_config.json, harvester_state.json |
| `data/` | status.json, entry-context.jsonl, regime-protests.jsonl |
| `data/audit/` | OANDA trade exports from 2026-04-09 audit |
| `.gitignore` | Excludes .env, logs, pycache, runtime state |

## Configuration
- **Credentials:** `.env` in bot dir — OANDA_ENVIRONMENT=practice (see [[OANDA Trading Account]])
- **Config:** `config.py` dataclass with 40+ fields, overridable via `SCROOGE_*` env vars
- **SL/TP:** Zone-anchored (NOT fixed pips). Config values sl_pips/tp1_pips/tp2_pips only used by disabled probe system.
- Probes: disabled by default (probe_enabled=false)
- Green exit: enabled (hourly_green_exit_min_pnl=0.2%)

## Shared Resources
- **Venv:** `~/mr_scrooge_env` symlink to `~/mr_burns_env` — shared with V1
- **Dashboard:** V1's `mr-scrooge-dashboard.service` serves both

## Logs
All in `~/.openclaw/workspace/agents/mr-scrooge-v2/logs/`:
- `mrscroogev2.log` — main output (daily logrotate)
- `decisions.log` — entry/exit decisions (RotatingFileHandler 10MB, 5 backups)
- `trades.log` — trade events (RotatingFileHandler 10MB, 5 backups)
- `launchd.log` — startup/shutdown
- Child loggers: propagate=False (no duplicate lines)

See [[Mr. Scrooge V2 Log Systems]] for grep recipes and audit methodology.

## DANGER ZONE
- **27x position sizing** — V2 SL losses are extreme in dollar terms
- **Shares dashboard** — restarting dashboard service affects V1 visibility too
- **Scoring was recalibrated 2026-04-09** — don't change point values without re-running the OANDA audit. See [[Mr. Scrooge V2 Scoring System]]
- **SL limit is in coordinator.py** (not main.py like V1) — bugs fixed 2026-04-09. See [[SL Limit Order System]]
- **Edit procedure:** Follow [[Mr. Scrooge Edit and Deploy Workflow]] and read [[Mr. Scrooge V2 Pre-Change Checklist]] first


## 2026-04-14 Session Changes (major overhaul)

### Regime & Entry
- Regime scoring: category-capped (market structure -3 max, performance -3 max, breadth -1 max)
- Breadth feedback loop broken (uses direct_score)
- Direction-aware rejection decay (aligned = -1 instead of -2)
- box_acceptance restored to -2 for all directions (structural, not directional)
- Entry floor: regime score >= -1 required for reversals
- BB exhaustion gate: reversals require EXTREME or REJECTION BB state
- min_risk_reward: 1.35 (was 1.60)

### Defect Fixes
- CT failure memory: 2 SL hits at same zone blocks CT entries (CT_ZONE_EXHAUSTED)
- box_contained lookback: 24 candles / 2 hours (was 6 / 30 min)
- Daily zone entry cap: 3 per zone+direction
- Harvester crash: trade_state.py client_id NameError fixed
- TP1 persistence: saved in trade_coordination.json, survives restarts
- V2 engine.py _result typo fix

### New: Trend Participation Engine
- Fires when BB state = TREND or STRETCH (reversal blocked)
- Enters with-trend on pullback to BB20 midline (SMA20)
- TREND_FULL: 50% position size, 1-candle confirmation
- TREND_STRETCH: 30% position size, 2-candle confirmation
- SL: 1.0 × ATR(14) on 5M bars
- Fixed score: 30. All existing trade management unchanged.

### Execution Timing (SL guardrails)
- Trigger-side validation: check SL against ask (shorts) / bid (longs) + buffer
- Spread kill switch: skip trailing when spread > 5p (JPY) / 2p (default)
- No-man's zone: never place SL where bid < sl < ask
- Audit logging: every SL move writes to data/execution-audit.jsonl

### Dashboard
- New Execution tab: SL guard stats, block reasons, engine performance, event timeline
- Dashboard tab handler JS fix (this->tab in arrow function)

## Related
- [[Mr. Scrooge V1]]
- [[OANDA Trading Account]]
- [[Mr. Scrooge Architecture]]
- [[Mr. Scrooge V2 Scoring System]]
- [[Mr. Scrooge V2 Regime System]]
- [[Mr. Scrooge V2 Pre-Change Checklist]]
- [[Mr. Scrooge Edit and Deploy Workflow]]
- [[Mr. Scrooge Harvester Operations]]
- [[Mr. Scrooge V2 Log Systems]]
- [[Mr. Scrooge Known Defects]]
