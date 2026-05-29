# Session-based pair screener — archived 2026-05-28

Archived per Brock directive: "disconnect the screener, the ML doesn't
need it. make sure the ML knows about the 13 strategies lab tested, and
uses them the way they were backtested."

## What lived here

`scrooge_v3/market/screener.get_session_pairs(utc_hour, mode)` — returned
a session-filtered subset of the 26-pair universe based on which forex
sessions were currently open:

```
Sydney  (21:00-06:00 UTC):  6 pairs
Tokyo   (00:00-09:00 UTC): 10 pairs
London  (07:00-16:00 UTC): 16 pairs
NY      (13:00-22:00 UTC): 13 pairs
```

scan_coordinator called this every cycle to decide which pairs to scan.
At Sydney-only hours (22-06 UTC) it returned only 6 pairs, blocking
EUR_USD/GBP_USD/USD_JPY/USD_CHF/USD_CAD entirely until London reopened.

## Why disconnected

The ML rule library already encodes (pair, session, regime) edge in the
14-bucket signatures. The screener was a hardcoded hour filter layered
ON TOP of ML routing — double-gating with zero added value. At
late-NY/Asia-only windows it silently killed 20 pairs/cycle worth of
admit opportunities.

Audit confirmed 25,109 lab rules across 28 pairs are session-stratified
(session_bucket is one of the 14 factors). Letting ml_router decide
admit-per-pair gives finer-grained behavior than any hour-table filter.

## What remained in the live screener.py

These exports were KEPT in `src/scrooge_v3/market/screener.py` because
they have non-screening consumers:

  - `CANDIDATE_PAIRS` — 26-pair universe constant, used by
    scan_coordinator after the disconnect
  - `SESSION_WINDOWS` — session-window data, used by `get_active_sessions`
  - `get_active_sessions(utc_hour)` — used by dashboard_bridge to display
    which sessions are currently open (informational, not gating)
  - `is_weekend()` — utility used by dashboard
  - `BASE_PAIRS`, `PROBATION_PAIRS` — informational classifications

Only `get_session_pairs()` was removed.

## How to revive

If you ever want the session filter back:

1. Read this archive's `screener_original.py` for the `get_session_pairs`
   implementation
2. Paste it back into `src/scrooge_v3/market/screener.py`
3. In `src/scrooge_v3/core/scan_coordinator.py`, replace:
   ```python
   from scrooge_v3.market.screener import CANDIDATE_PAIRS
   pairs = list(CANDIDATE_PAIRS)
   ```
   with:
   ```python
   from scrooge_v3.market.screener import get_session_pairs
   pairs = get_session_pairs(now.hour)
   if not pairs:
       log.debug("[SCAN] No active pairs this session")
       return result
   ```
4. Restart V3.

## Related changes shipped same day

- daily_circuit gate disabled in config (Brock: "daily circuit is supposed
  to be turned off")
- natural_target_floor gate disabled in config (Brock: "drop it entirely
  and let the ML rules be the only quality gate")
- LightGBM v0 promoted from observe→gate with p_win >= 0.55 threshold
- ml_router demoted to shadow (logs admit verdict but doesn't gate)
