# features/zone_detector — Dev Log

> Zone detector feature: identifies daily PDH/PDL liquidity zones, applies percentile filtering, and manages zone tiers.

---

## Historical Lessons (V1/V2)

### [2026-03-19] [V1] — Rolling box experiment FAILED — revert to daily PDH/PDL
**Source:** AUDIT.md, SCROOGE.md
**Type:** bug
**Detail:** 30-minute rolling box was too unstable — zones shifted constantly. 23 commits introduced, bot stopped making money. REVERTED to daily PDH/PDL with percentile filter + gap detection. Daily box is the correct model per MASTER_THEORY.

### [2026-03-11] [V2] — Percentile filter: 98th/2nd for spike trimming
**Source:** DAILY_NOTES_2026-03-11
**Type:** rule
**Detail:** Apply 98th percentile for PDH and 2nd percentile for PDL. Original was 95/5 (more aggressive) — 98/2 trims less. Prevents one-candle outliers from distorting the range.

### [2026-03-11] [V2] — Zone width widened from 20% to 30% of range
**Source:** DAILY_NOTES_2026-03-11
**Type:** rule
**Detail:** buy_zone_pct / sell_zone_pct widened from 20% to 30%. Per MASTER_THEORY: "lower part of the box" is the zone.

### [2026-03-12] [V2] — Min level touches lowered from 2 to 1
**Source:** DAILY_NOTES_2026-03-12
**Type:** lesson
**Detail:** One prior high/low is a valid liquidity zone per MASTER_THEORY. Box validation still required 4 combined touches total. Was filtering valid setups.

### [2026-04-12] [V2] — Alternative range (session cheat code) may not have edge
**Source:** NOTES.md
**Type:** warning
**Detail:** Alternative range using session data after breach may not align with MASTER_THEORY. Theory says range = prior day high/low. Need 100+ trades on alternative ranges to evaluate. Track using_alternative=True entries separately.

### [2026-04-09] [V2] — Stale box data caused absurd TP2 values
**Source:** AUDIT_FINDINGS_20260409.md
**Type:** bug
**Detail:** When range boundaries hadn't been refreshed, TP2 calculations produced unreachable targets (300+ pips on 10-pip SL). Fixed by validating TP2 distance against ATR and capping at configurable multiple.
