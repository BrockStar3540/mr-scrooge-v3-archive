# execution/stop_planner — Dev Log

> Stop planner: manages stop-loss placement, hybrid SL strategy (native + proactive limit), and trigger-side validation.

---

## Historical Lessons (V1/V2)

### [2026-04-03] [V2] — Hybrid SL: native SL + proactive limit for better fill
**Source:** NOTES.md
**Type:** lesson
**Detail:** Hybrid system keeps OANDA native SL as hard backstop. Proactive REDUCE_ONLY limit placed when price approaches stop within trigger_buffer pips. Pair-specific profiles: tight (2p trigger, 1.0 offset), medium (4p, 1.5), wide (6p, 2.0). Fast market detection skips limit.

### [2026-04-14] [V2] — Hybrid trail calculated SL from mid-price, OANDA triggers shorts on ask
**Source:** known-defects.md
**Type:** bug
**Detail:** During wide spreads (13-16p on JPY), SL placed inside spread -> instant fill (dead on arrival). Fixed: 4 guardrails — trigger-side validation, spread kill switch, no-man's zone, side-aware.

### [2026-04-10] [BOTH] — SL limit spam on dead positions (46+ API calls)
**Source:** known-defects.md, Defect 14
**Type:** bug
**Detail:** After harvester closed position, SL-limit fast loop continued placing limits. OANDA rejected with NO_POSITION_TO_REDUCE but bot retried every 3 seconds. Fixed: detect orderCancelTransaction, mark position done, add alive gate.

### [2026-04-14] [BOTH] — Spread kill switch: skip trailing when spread hostile
**Source:** system/bots/mr-scrooge.md, mr-scrooge-v2.md
**Type:** rule
**Detail:** Spread kill switch: skip trailing stop updates when spread > 5p (JPY pairs) / 2p (default pairs). Part of the 4 guardrails in execution_router.move_stop. Prevents stops from being placed inside spread during hostile conditions.

### [2026-03-11] [V1] — ATR = 0 on reconciled positions after restart
**Source:** DAILY_NOTES_2026-03-11.md
**Type:** bug
**Detail:** Positions loaded from OANDA on restart have atr_at_entry = 0.0 because OANDA doesn't store this value. Hybrid trail's ATR component falls back to candle-only trail for these positions. V3 must persist atr_at_entry in its own state file (not rely on broker).

### [2026-04-16] [V3] — validate_stop() can loosen stops — caller must guard
**Source:** Ratchet bypass bug investigation
**Type:** lesson
**Detail:** validate_stop() adjusts proposed stops for trigger-side safety and no-man's-zone. The adjusted value depends on live bid/ask/spread, which change every tick. This means validate_stop() can return a value that is WORSE than current_stop. The stop planner itself doesn't know what current_stop is — it only validates a proposed value. Callers (runtime.py position management loop) must compare the validated output against current_stop and reject loosening moves. This is now enforced in runtime.py with a final guard after validate_stop().
