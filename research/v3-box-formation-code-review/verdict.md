# V3 Box-Formation Code Review

Generated: 2026-05-13T03:17:38.848879+00:00

## Verdict: LIVE V3 IS FINE

The 168-428h box_age values in the broker audit were a **forensic measurement
artifact** caused by the audit reconstruction script using cached dukascopy daily
data that ends 2026-04-22. **Live V3 box_age is 0-24h consistently** across 58,152
scan events in scans.jsonl.

**No live-system issue. No code change needed. No ADR.**

## Evidence

### Live V3 scans (58,152 events, Apr 20 → May 12)

box_age_hours distribution across ALL scans:
- 0-24h: 56,937 (97.9%)
- 24-48h: 1,215 (2.1%)
- 48h+: **0 (0.0%)**
- median: 12.4h, max: 27.0h

box_age_hours distribution across TAKE-verdict scans only (the ones that scored):
- 0-24h: 1,606 (100%)
- 24h+: **0**
- median: 6.2h, max: 23.3h

**Live V3 has never operated with a box_age > 48h.**

### Audit reconstruction (the 196 broker rows)

Same single trade comparison (AUD_CAD, 2026-05-04 00:55:54 UTC):

| Source | box_age_hours |
|---|---|
| audit factor_snapshot | **315.93** |
| live scans.jsonl (2026-05-04 00:55:25, same minute) | **3.91** |

**80× discrepancy on the same trade at the same minute.**

## Mechanism — what the audit did wrong

V3's `zone_detector.py` computes box_age as:

```python
last_daily_ts = pd.Timestamp(daily_bars.index[-1])
box_age_hours = (now_utc - last_daily_ts).total_seconds() / 3600
```

Logic: hours since the MOST RECENT daily bar in the feed. In normal operation,
daily_bars.index[-1] is today's date (the bar in progress), so box_age stays 0-24h.

**Audit script** (`Oanda-Bot-Trainer/scripts/live_broker_reverse_engineer.py`
`reconstruct_factor_snapshot`) used the **dukascopy daily cache** at
`/data/oanda-bot-trainer-cache/dukascopy/<pair>/<pair>_D_2019-07-01_2026-04-22.jsonl`.

**The cached daily data ends 2026-04-22.** For any audit entry_ts > 2026-04-22:
- audit's `daily_bars.index[-1]` = 2026-04-22 (the file's last date)
- audit computed box_age = entry_ts - 2026-04-22
- For a May 4 entry: box_age ≈ 12 days = ~288h
- For a May 8 entry: box_age ≈ 16 days = ~384h

This perfectly explains the bimodality:
- Pre-2026-04-22 entries: audit had live daily data, computed normal box_age
- Post-2026-04-22 entries: audit's daily reference froze at Apr 22 → box_age artificially balloons

## V3 code review — production logic

Reading `src/scrooge_v3/features/zone_detector.py` end-to-end:

### Box formation
- `_build_session_range()` searches backward through daily bars for the prior
  trading day (iloc[-2] etc., skipping weekend bars with <0.05% range)
- Builds session range from that prior day's high/low (PDH, PDL)
- Percentile filter applied (98th/2nd percentile from hourly bars)
- Gap detection: if today's open >0.5% outside prior range, range flips
- Sanity check: PDH > PDL or fallback to raw values
- Touch validation: PDH and PDL must have been tested in prior hourly bars

### Box refresh cadence
- Box is recomputed **every scan** (per-cycle, ~60s) using fresh daily_bars
- daily_bars are fetched live from OANDA/data feed each scan
- No box state is persisted across cycles — it's rebuilt each time
- Effectively: V3's 'box' is recalculated continuously based on the latest available daily data

### Why this produces 0-24h box_age in live
- Live OANDA daily feed: today's bar is forming (timestamp = today 00:00 UTC)
- `daily_bars.index[-1]` = today's date
- box_age = now_utc - today_00:00 = current hour of UTC day (0-24h)
- Median 12.4h is consistent with bot scanning throughout the trading day

### Alt-box logic
- `using_alternative` flag exists in `features/range_builder.py` (separate module)
- Triggers when primary range is invalid (e.g., gap-inverted, percentile-rejected)
- Falls back to an alternative range definition
- The B-074 bug (regime vs alt-box mismatch) was specifically that regime classifier
  judged against ORIGINAL box even when signal engine used ALT box
- B-074 was open as of 2026-04-13 per the bug catalog. Status unclear in current code.

## Conclusions per the review-scope checklist

| Question | Answer |
|---|---|
| Where does V3 form/refresh boxes? | `zone_detector.py` per scan cycle (~60s) |
| Expected cadence? | Continuous — recomputed every scan from live daily feed |
| Why box_age 7-18 days? | **AUDIT ARTIFACT.** Dukascopy daily cache ends 2026-04-22. Live is fine. |
| Bug catalog match? | None — this is not B-068-074. Audit script artifact. |
| Stale boxes feeding direct/dbb_trend entries? | NO. Live entries see 0-24h boxes only. |
| Stale boxes in live logs? | NO. scans.jsonl confirms 0-48h ceiling. |

**Verdict: not_a_live_issue.** Forensic measurement artifact. V3 production
operates with fresh box references on the expected cadence.

## Implications for prior research

- **Step 7-8-9 analyses** that used `factor_box_age_hours` from the broker audit are
  **partly contaminated** for post-2026-04-22 trades. The box_age signal in those
  was bot-era-correlated as suspected, but the underlying mechanism is the audit cache
  boundary, not a real V3 box-staleness behavior.

- **The +30 WR gap between fresh and stale** in the prior validation is essentially
  the WR gap between pre- and post-Apr-22 trades. This may still reflect a real era
  effect (different probes, different market regime) but it's NOT mediated by box_age.

- **Other audit-derived factors** that depend on daily bars may have similar artifacts:
  - factor_atr (computed from daily bars in zone_detector — but ATR is a smoothed
    value, less sensitive to one missing day)
  - factor_box_range (zero in audit — separate issue, possibly same root cause)
  - factor_ctx_box_age_hours (zero in audit — separate issue)

- **Future audit reconstructions** must use OANDA-live or fresh dukascopy data, not
  the cached file that ends 2026-04-22.

## What's NOT a concern (despite earlier worry)

- V3 live box_age values are normal (0-24h, median 12.4h)
- V3 box code recomputes per scan from live daily feed — no persistence bug
- The bimodality in audit data does NOT reflect a live system bug

## What IS still worth checking (separately)

- V3's alt-box state (using_alternative flag) — does B-074 (regime vs alt-box
  mismatch) still apply in current V3? Separate code review.
- Audit script's `live_broker_reverse_engineer.py` — should be flagged with a
  data-cache-boundary warning so future re-runs use live-current daily data.

## Next per direction

Item 2: Era-split factor synchrony rerun. With the box_age artifact understood,
re-run Step 8 synchrony WITHIN bot-era to determine which factor patterns are real
and which are era-confounded. Many of the strong factors (volume, BB width, spread,
etc.) may or may not survive an era-split. The bot-era is now well-defined: pre-Apr-22
(audit-comparable) vs post-Apr-22 (audit-cache-degraded).

Honest framing for the rerun:
- Pre-Apr-22 broker trades: audit data is reliable
- Post-Apr-22 broker trades: any daily-derived factor is suspect
- The era-split test will identify which factors hold WITHIN the reliable pre-Apr-22 window