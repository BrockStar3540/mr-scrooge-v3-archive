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
