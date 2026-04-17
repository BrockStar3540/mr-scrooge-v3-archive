# architecture — Dev Log

> System architecture: loop design, multi-actor coordination, logging, and cross-version lessons.

---

## Historical Lessons (V1/V2)

### [2026-04-03] [V2] — Dual-loop: 5-min decisions + 3-sec execution
**Source:** NOTES.md
**Type:** lesson
**Detail:** Professional pattern. Slow loop: candle decisions, universe scan, regime. Fast loop: SL limit placement, fill monitoring. Threading.Lock prevents simultaneous _manage_sl_limit calls. Dead position guard in fast loop.

### [2026-04-10] [V2] — Four-actor coordination via TradeCoordinator
**Source:** NOTES.md
**Type:** bug
**Detail:** Bot, ratchet, SL-limit, and harvester modified same OANDA trade independently. 46+ wasted API calls on dead positions. Solution: TradeCoordinator class for cross-process state via coordination file.

### [2026-04-09] [BOTH] — No code sharing between V1 and V2
**Source:** NOTES.md
**Type:** lesson
**Detail:** Separate dashboards, git repos, GitHub tokens, Alien Device remotes. Isolation prevented bug infection between versions.

### [2026-04-09] [BOTH] — Never trust bot logs for P&L — use broker API
**Source:** scoring-inversion postmortem
**Type:** rule
**Detail:** Bot P&L was wrong for 17/21 pairs. Log-based analysis would have reached wrong conclusions. Always pull closed trades from broker API for truth.

### [2026-04-12] [V2] — Session indicator frozen since boot (Defect 17)
**Source:** known-defects.md
**Type:** bug
**Detail:** _update_sessions() defined but never called in run loop. Sessions were set once at boot and never updated. Dashboard permanently showed boot-time session.

### [2026-04-12] [V2] — Duplicate log handler (propagate=True)
**Source:** known-defects.md, Defect 12
**Type:** bug
**Detail:** propagate=True on child loggers caused every line to appear twice. Fixed with propagate=False. Added RotatingFileHandler (10MB, 5 backups).

### [2026-03-24] [V2] — Silent indentation bug skipped ALL signals for 4.5 hours
**Source:** DAILY_NOTES_2026-03-24.md
**Type:** bug
**Detail:** A `return None` at 8-space indent (should have been 12-space) in process_instrument() caused immediate return after tradeable check for every symbol. No errors raised, bot appeared healthy, logs continued, positions managed. Zero signals evaluated for ~4.5 hours. V3 MUST have integration tests verifying at least one signal evaluation per cycle.

### [2026-03-26] [V2] — engine.py renamed to .bak, bot ran on stale .pyc
**Source:** AUDIT.md, V2 NOTES.md
**Type:** bug
**Detail:** signals/engine.py was renamed to .bak during editing. Bot survived on stale .pyc cache and only crashed on next restart with ModuleNotFoundError. Lesson: never rename files to .bak — use git branches. Always verify .py files exist after editing.

### [2026-03-05] [V1] — Multiple live bot instances running concurrently
**Source:** AUDIT.md
**Type:** bug
**Detail:** Confirmed by duplicate log lines. Fix: non-blocking file lock (logs/mr-scrooge.lock) prevents second instance. start.sh has startup lock + orphan process sweep. V3 MUST have process-level singleton enforcement.

### [2026-03-19] [V1] — Never use pkill+Popen for restart, use systemctl
**Source:** AUDIT.md
**Type:** lesson
**Detail:** pkill followed by Popen to restart created rogue duplicate processes. systemd owns the process lifecycle — nohup and manual process management fight with it.

### [2026-04-03] [V1] — Alert routing to non-existent Slack channel caused syslog flooding
**Source:** AUDIT.md
**Type:** bug
**Detail:** _send_scrooge_alert() routed to non-existent #mr-scrooge Slack channel, causing syslog flooding. Fixed to route via Telegram. V3 alert routing must target valid channels.

### [2026-02-14] [V1] — OANDA server latency: NYC region is critical
**Source:** Dropbox: 2026-02-14_Building a forex trading agent with OAND.md
**Type:** lesson
**Detail:** OANDA primary servers in NYC/NJ. VPS in NYC: 1-3ms latency. San Francisco: 60-70ms. London: 70-80ms. Home WiFi: 30-50ms + jitter. For live trading with aggressive entries, NYC region deployment is critical. Affects fill quality and slippage on limit orders, especially harvester partials.

## Runtime Extraction (2026-04-16)

### Phase 1-4 Complete
runtime.py went from **877 lines** (god-file) to **232 lines** (thin conductor).

Eight modules extracted:

| Module | Lines | Responsibility |
|--------|-------|----------------|
| `core/bootstrap.py` | 262 | All module registration, config, broker init |
| `core/runtime_context.py` | 43 | Typed RuntimeContext dataclass |
| `core/scan_coordinator.py` | 125 | Market data fetch, scan pipeline, candidate filter |
| `core/execution_coordinator.py` | 131 | Sizing, SL validation, order placement |
| `core/position_coordinator.py` | 185 | Management pipeline, SL physics, harvest/exit |
| `services/dashboard_bridge.py` | 97 | Dashboard live_state publishing (crash-safe) |
| `services/config_watcher.py` | 53 | Hot-reload handling |
| `services/state_recovery.py` | 155 | Vanished trades, pending orders, harvest limits |

### Conductor Pattern
_run_cycle() is now pure orchestration:
```
detect_vanished → scan → execute → reconcile → manage → publish
```
Each step delegates to a dedicated module. No execution or management
logic remains in runtime.py.

## Safety Fixes (2026-04-17)

### Order Throttles
- Max 2 pending limit orders at a time
- Currency correlation gate: no new trade if base or quote currency already in open/pending position
- Prevents correlated burst at session open (was placing 6 JPY/AUD orders in 10 min)

### Margin Cap
- margin_utilization reduced from 0.80 to 0.40
- Looser scorer + near-max sizing = blow-up risk

### Metadata Persistence
- Pending entry metadata (strategy, family, profile, tp1, v3_score) now persisted to positions.json
- Survives restarts — no more generic "limit_fill" positions with empty metadata
