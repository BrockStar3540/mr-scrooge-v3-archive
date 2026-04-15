# Bot: Mr. Scrooge V1

type: system
status: active
tags: [scrooge, trading, bot, forex, oanda, v1]

trust:
  score: 95
  confidence: high
  evidence:
    - source: live production system, OANDA audit 2026-04-09
      type: firsthand

## Summary
OANDA forex trading bot — live account. Monolithic Python architecture. Box-theory reversal entries with OANDA-truth-calibrated scoring (2026-04-09), hybrid SL limit exits, harvester profit extraction, and regime-based trade filtering. Runs 24/5 on EC2.

## Location
- **Code (truth):** EC2 `~/.openclaw/workspace/agents/mr-scrooge/`
- **GitHub:** `BrockStar3540/mr-scrooge` (private, token: GITHUB_TOKEN_SCROOGE)
- **Alien Device backup:** `/Volumes/Alien Device/mr-scrooge/`
- **Git:** Isolated `.git` inside `agents/mr-scrooge/` (not workspace root)
- **Remotes:** `origin` (GitHub), `alien` (Alien Device via Tailscale SSH)
- **Sync flow:** EC2 → GitHub + EC2 → Alien Device (one-way push)

## Systemd Services (EC2, user mode)

| Service | Purpose |
|---------|---------|
| `mr-scrooge.service` | Main trading bot — 5-min cycle loop |
| `mr-scrooge-harvester.service` | Profit harvester — 30-sec poll |
| `mr-scrooge-dashboard.service` | Web dashboard — port 8081 (SHARED with V2) |

All: `Restart=always`, auto-start on EC2 reboot.

## Module Structure

| Path | Contents |
|------|----------|
| `main.py` | Main loop, entry ranking, regime scoring injection (~84KB) |
| `gates.py` | All signal gates + `_calculate_score()` (~132KB) |
| `core/` | oanda_client.py, execution_router.py, fee_calculator.py |
| `regime/` | supervisor.py, models.py, bb_context.py |
| `portfolio/` | trade_manager.py — position lifecycle, P/L calculation |
| `quality/` | tracker.py, indicators.py, models.py, entry_context.py |
| `harvester/` | main.py, harvester_config.json, harvester_state.json |
| `data/` | status.json, entry-context.jsonl, regime-protests.jsonl |
| `data/audit/` | OANDA audit CSVs and raw API exports |
| `dashboard.py` + `dashboard.html` | Flask dashboard |
| `.gitignore` | Excludes .env, pycache, logs, .bak files |

## Configuration
- **Credentials:** `.env` in bot dir (LEVEL 4 — never in vault, never in git)
- **Config:** `main.py` CONFIG dict (inline constants)
- **Account:** LIVE (real money)
- margin_utilization: 0.80
- max_concurrent_positions: 1
- min_risk_reward: 1.35 (lowered from 1.60 on 2026-04-13, hard gate uses TP2)
- SL/TP: zone-anchored (box-derived), not fixed pips
- Scans up to 21 instruments per cycle

## Scoring System (recalibrated 2026-04-09)

See [[Mr. Scrooge V1 Scoring System]] for full details.

Key points:
- Three layers + OANDA truth modifiers (Layer 3b)
- john_wick: +15 pts (preferred). power_of_towers: +5 pts (deprioritized)
- Ranging market: -20 pts. CT + power_of_towers: -15 pts. CT Tier 1: -10 pts
- Regime (rebalanced 2026-04-13): NORMAL +10, CAUTION -5, RESTRICTED -10
- Regime scoring uses category caps: market structure -3 max, performance -3 max, breadth -1 max
- Regime state thresholds: NORMAL >= 0, CAUTION >= -2, RESTRICTED >= -4, BLOCKED < -4
- Entry gating: only BLOCKED suppresses entry (score floor and hysteresis removed)
- R:R scoring uses TP1 (realistic target). Hard gate uses TP2.
- Calibrated from 511 OANDA trades — see audit data in `data/audit/`

## Signal Types
- `john_wick` — wick rejection at zone (+15 scoring bonus)
- `power_of_towers` — multi-candle reversal (+5 scoring bonus)
- `extreme_reversal` — Bollinger Band spike counter-entry

## Key Systems
- **SL Limit System:** Hybrid maker-fill exit inside native SL — see [[SL Limit Order System]]
- **Green Exit:** Hourly limit exit at maker-fee spread
- **Fast Execution Loop:** 3-second sub-cycle for SL limit management
- **Harvester:** Separate daemon, tier-based partial closes (1.5%/3.0%/4.5% equity)

## Logs

All in `logs/`:

| File | Content | Rotation |
|------|---------|----------|
| `mrscrooge.log` | Main bot output | Daily logrotate, gzip, 20 days |
| `decisions.log` | Entry/exit decisions, scoring | RotatingFileHandler 10MB, 5 backups |
| `trades.log` | Trade executions | RotatingFileHandler 10MB, 5 backups |
| `launchd.log` | Startup/shutdown | Daily logrotate |

Child loggers have `propagate=False` — no duplicate lines.
See [[Mr. Scrooge V1 Log Systems]] for grep recipes and audit methodology.

## Monitoring
- [[Frank Agent]] watches via HEARTBEAT.md (30-min silent health check)
- Alert triggers: bot down, equity drop >3%, errors

## DANGER ZONE
- **Before editing:** Read [[Mr. Scrooge V1 Pre-Edit Briefing]]
- **Known defects:** See [[Mr. Scrooge Known Defects]] — 3 HIGH open + 7 fixed (2026-04-09)
- **Edit procedure:** Follow [[Mr. Scrooge Edit and Deploy Workflow]]
- **Scoring recalibrated 2026-04-09** — don't change point values without OANDA data audit
- **Dashboard is SHARED** with V2 — restart affects both
- **Copyright headers** on all .py files synced to Alien Device
- **Clear pycache** after any edit: `find . -name '*.pyc' -delete`
- **Never use nohup** — systemd owns the process


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
- [[Mr. Scrooge V2]]
- [[OANDA Trading Account]]
- [[Mr. Scrooge Architecture]]
- [[Mr. Scrooge V1 Scoring System]]
- [[Mr. Scrooge V1 Pre-Edit Briefing]]
- [[Mr. Scrooge V1 Log Systems]]
- [[Mr. Scrooge V1 Changelog]]
- [[Mr. Scrooge Edit and Deploy Workflow]]
- [[Mr. Scrooge Known Defects]]
- [[SL Limit Order System]]
