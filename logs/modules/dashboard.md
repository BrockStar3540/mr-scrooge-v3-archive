# dashboard — Dev Log

> Modular dashboard: plug-in widget system where each module registers its own panel. Core tabs always present, module panels discovered from registry.

---

## Historical Lessons (V1/V2)

### [2026-04-12] [V2] — V2 market summary always showing 0/0 (Defect 19)
**Source:** known-defects.md
**Type:** bug
**Detail:** Signal engine only populated validity_detail on passing signals. Rejected signals had no validity_detail dict, so status.py's market_summary always reported 0 valid candidates and 0 rejected. Dashboard Signals tab showed "No classified setups." Fix: enforce strict validity_detail schema on ALL signals (pass and reject). V3: every module must return display data regardless of pass/fail outcome.

### [2026-04-12] [V2] — Box states showing all 26 pairs instead of active only (Defect 20)
**Source:** known-defects.md
**Type:** bug
**Detail:** Coordinator iterated box_machine.states.keys() (all tracked) instead of active_instruments (viable only). Dashboard showed 26 cards vs V1's ~11. V3: dashboard widgets must filter to active/relevant data, not dump everything.

### [2026-04-12] [V2] — Session indicator frozen since boot (Defect 17)
**Source:** known-defects.md
**Type:** bug
**Detail:** _update_sessions() defined but never called in run loop. Dashboard permanently showed boot-time session. V3: dashboard data must come from live state, not boot-time snapshots.

### [2026-04-12] [V2] — Parity harness false CRITICALs from cosmetic gaps
**Source:** parity-harness.md
**Type:** lesson
**Detail:** NO_TRADE signals had validity_detail=None, causing parity harness to flag CRITICAL when comparing V1/V2. BB position near 0.85 threshold caused 4-8pt score deltas from timing noise. V3: dashboard monitoring must distinguish real divergence from timing noise. Define severity levels clearly.

### [2026-04-07] [V2] — Dashboard showed healthy status while bot was entering 3rd CT short at same zone
**Source:** known-defects.md, Defect 1
**Type:** bug
**Detail:** Dashboard had no visibility into zone re-entry count or CT failure history. Bot appeared healthy while making the same mistake for the 3rd time. V3: dashboard must show zone hit count, CT failure memory, and entry cap status per symbol.

### [2026-04-09] [BOTH] — Dashboard P/L was wrong for 17/21 pairs
**Source:** scoring-inversion postmortem
**Type:** bug
**Detail:** Dashboard displayed bot-calculated P/L which used quote currency instead of USD for non-USD-quote pairs. Numbers looked plausible but were wrong. V3: dashboard P/L must use broker-reconciled values, not bot calculations. Show both if needed, but flag discrepancies.

### [2026-03-24] [V2] — Silent indentation bug: dashboard showed bot running but zero signals evaluated
**Source:** DAILY_NOTES_2026-03-24.md
**Type:** bug
**Detail:** Bot appeared healthy on dashboard (positions managed, logs flowing) but a return-at-wrong-indent meant zero signals were evaluated for 4.5 hours. V3: dashboard health tab must show "signals evaluated this cycle" count. Zero evaluations = red light, not green.

### [UNDATED] [BOTH] — Dashboard HTTP Basic Auth + Tailscale only
**Source:** dashboard-operations.md (vault)
**Type:** rule
**Detail:** Dashboard binds to 127.0.0.1 only. HTTPS via Tailscale Serve. HTTP Basic Auth (401 on failure). Not publicly routable. V3 must maintain this security posture.

### [UNDATED] [V2] — status.json is the dashboard data contract
**Source:** debugging-workflow.md (vault)
**Type:** rule
**Detail:** V2 dashboard reads from data/status.json written by coordinator every cycle. This is the contract between the bot and the dashboard. V3: define a clear API contract — either status.json or a proper REST endpoint. Widget data should flow through one channel, not scattered file reads.

### [2026-04-16] [V3] — Added BALANCE metric, renamed REALIZED P/L → UNREALIZED P/L
**Source:** Brock request
**Type:** feature
**Detail:** Dashboard metrics bar was showing EQUITY, DAILY PNL, REALIZED P/L. The realized_pl field was actually displaying unrealized_pl data (runtime.py passed acct.unrealized_pl into the realized_pl field). Fixed: renamed field to unrealized_pl throughout live_state.py, runtime.py, and templates/index.html. Added BALANCE as the first metric in the status bar. Balance comes from broker acct.balance, already available in the snapshot.

### [2026-04-16] [V3] — V1 dashboard decommissioned
**Source:** V1 removal
**Type:** cleanup
**Detail:** V1 dashboard (mr-scrooge-dashboard.service, port 8081) stopped, disabled, and service file removed. The old dashboard.html in the V3 dashboard directory is a V1 leftover — only templates/index.html is served by the V3 Flask app via /api/data.

## Dashboard Updates (2026-04-16)

### Execution Tab (new)
- Health lights: SL engine health, spread risk, ratchet efficiency
- Metrics: SL moves vs blocks, avg spread at block/move
- Block reasons breakdown grid
- Scrollable event timeline with color-coded entries

### DBB Trend Tab (new)
- Approved / rejected / blocked counts with health lights
- Breakout vs pullback candidate counts
- Average base and final scores
- Breakdown by session bucket and box age
- Scrollable candidate table

### Winner-Path Fix (CRITICAL)
scan_symbol_full() was taking candidates[0] — first registered strategy,
not the actual V3 scorer winner. Fixed to mirror live scan_symbol() path:
- Run gates on ALL candidates
- Score ALL gate-approved candidates
- Pick winner via max(score) — same as live
- Report includes candidates_by_strategy for transparency

### Scorer Audit Payload
Every scored pair now shows raw box-derived inputs in the log:
px, ema20, ema50, box_range, box_age — fully verifiable.
