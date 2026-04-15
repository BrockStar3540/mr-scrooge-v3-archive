# Mr. Scrooge V1 Changelog

type: system
status: active
tags: [scrooge, trading, changelog, v1]

trust:
  score: 90
  confidence: high
  evidence:
    - source: git history and production deployment records
      type: firsthand

## Summary
Dated log of all significant V1 changes. For the process/rules on when and how to document changes, see [[Mr. Scrooge Changelog Process]]. For code-level session notes, see EC2 `NOTES.md` in the bot directory.

---

### 2026-04-12 — Correlation Map Expansion + Peer Cap

**Author:** Claude Code
**Commit:** 27571cd
**Files:** regime/supervisor.py

**What:** Merged V2's AUD/NZD/JPY correlation pairs into breadth signal map. Added _MAX_BREADTH_PEERS=4 cap to control trigger frequency with larger map. Lists ordered by correlation strength so cap takes strongest peers first.

**Why:** Both bots scan same 26-pair universe. V1 was only evaluating EUR/GBP/USD majors for breadth signal, causing regime score divergence (breadth_negative fired on V1 but never on V2 for the same pairs).

**Verification:** Regime logs now show breadth_negative/positive on USD_CHF and other newly covered pairs. Trigger frequency consistent with pre-merge behavior (capped at 4 peers).

### 2026-04-09 — OANDA Audit + Scoring Recalibration + Bug Fixes

**Author:** V1 Auditor (Claude Code session)
**Files:** `gates.py`, `main.py`, `portfolio/trade_manager.py`, `core/oanda_client.py`, `dashboard.py`, `dashboard.html`

**What:**
- Scoring recalibration: Layer 3b OANDA truth modifiers (ranging -20, CT+PoT -15, CT+JW -5, CT T1 -10, CT T2 +5, z-align +5)
- Signal reweighting: john_wick +15 (was +10), power_of_towers +5 (was +10)
- Regime scoring: NORMAL +10, CAUTION -10 applied in main.py
- R:R scoring uses TP1 (buckets recalibrated: >=2.0/1.5/1.0), TP2 hard gate unchanged
- Score floor: min=1 for gate-passed signals
- P/L currency conversion for non-USD-quote pairs (pip_value_per_unit on OpenPosition)
- Overhead cost USD conversion using pip_value
- OANDA 404 fallback: transactions API when trade endpoint returns 404
- TP sanity clamp: 3x ATR maximum
- Dead config removed: sl_pips, tp1_pips, tp2_pips
- Entry-context patch_outcome moved outside quality_rec guard
- Log duplicate fix: propagate=False on child loggers
- Log rotation: RotatingFileHandler 10MB, 5 backups
- Dashboard: new scoring keys display, negative value coloring, credentials to env vars
- Git repo isolated: own .git in agents/mr-scrooge/ (was workspace-level)
- Alien Device cleaned: V2 strays removed, proper rsync from EC2
- .gitignore created, .bak files deleted

**Why:** Two independent OANDA API audits (511 V1 trades, 58 V2 trades) found scoring system had zero predictive power (r≈0 with P/L). Ranging markets = PF 0.33 (#1 profit killer). CT Tier 1 = worst category. Bot P/L logs wrong for 17 of 21 instruments.

**Verification:**
- V1 restarted at 18:54 UTC, clean boot, 21/26 instruments viable
- RANKING line confirmed: scores 1-44 range (new penalties firing)
- AUD_CAD position reconciled correctly (existing trade preserved)
- Zero errors/tracebacks in post-restart logs
- Dashboard restarted, serving new scoring keys

---

### 2026-04-09 — SL Limit Order Spam Fix

**Author:** Prior session
**Files:** `main.py`

**What:** Three stacking bugs in `_manage_sl_limit()`: early return on sl_limit_filled, ERROR state handling, prevent re-placement after cancel.

**Why:** Bot was rapidly placing/canceling SL limit orders in a loop, burning API rate limits.

**Verification:** No repeat of spam behavior after fix.

---

### 2026-04-07 — RegimeAssessment.detail AttributeError Fix

**Author:** Prior session
**Files:** `main.py:1072`

**What:** Changed `regime_assessment.detail` → `.summary()`. Individual RegimeSignal objects have `.detail`, not the top-level assessment.

**Why:** Unhandled error every 5-min cycle for regime-blocked pairs.

**Verification:** No AttributeError in logs after fix.

---

## Related
- [[Mr. Scrooge V1]]
- [[Mr. Scrooge V1 Scoring System]]
- [[Mr. Scrooge Known Defects]]
- [[Mr. Scrooge Changelog Process]]
