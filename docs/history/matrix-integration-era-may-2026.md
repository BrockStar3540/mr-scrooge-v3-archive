# Matrix integration era — May 2026 (focused retrospective)

The May 11 → May 30 arc as a standalone narrative. Where
`evolution-timeline.md` Era 5 is the chronological log, this is the
"what actually happened and what it meant" version. Written 2026-05-30,
end of era, while context is fresh.

## The setup

Three months of corpus mining (Feb → April 2026) produced an 838k-trade
lab dataset with per-pair / per-strategy WIN/LOSE rules + factor lift
tables + optimized cells across 26 forex pairs × 13+ strategies × 2
directions × 5 sessions. The dataset was correct, mature, and offline —
referenced by hand for strategy promotion decisions, sized into the
matrix factor mining engine, but not part of the live admission path.

Meanwhile the live admission path had grown:
- 14 hand-tuned gates encoding overlapping slices of the same
  per-(pair × family × direction × session) question
- V3HybridScorer as the primary edge call, with session-aware threshold
  tiering tuned on a 50-trade survivor-biased dataset
- 5 strategies, BB-state → strategy hard-coded mapping
- ml_router as observer-only with no enforcement

The gap: the lab dataset had the answer; the live code had seven
approximations of it.

## The forcing function

A 48h losing streak (April 28 → 30): 16 trades, 6.2% WR, 11/11 long
disasters into JPY downtrend, −$5,350. The diagnostic arc surfaced four
distinct issues that had been compounding:

1. **Attribution was broken** (B-078) — 30%+ of trades had
   `strategy=unknown`, masking per-strategy breakdowns.
2. **Harvest LIMITs were going naked** (B-075, B-076) — orphan harvest
   orders firing as standalone positions when parent state desync'd.
3. **Ratchet was costing money** (B-077) — single-line experiment
   underwater $245/trade.
4. **Branched scoring is the right architecture** (47-factor audit) —
   15 factor sign-flips between DBB and Direct families.

The first three were fixed in a coordinated week. The fourth was the
strategic finding: the V3 scorer wasn't merely under-tuned; it was the
wrong architecture for a system with branched signal.

## The pivot

Rather than build a per-branch scorer (the obvious move), the May 11 →
28 work took a different route: collapse the gate stack into a single
matrix-mined routing table, then train a LightGBM model on the full
corpus and use *that* as the primary gate. The matrix encoded per-cell
admission already; LightGBM encoded the per-candidate confidence.
Together they replaced the V3 scorer + 7 gates.

The decision flow:

- **May 14 — MatrixRouter architecture decision (ADR 3008).** One gate,
  one parquet, one log per cell.
- **May 18 — ML observer retrained on cluster serials (ADR 3009).** The
  router's primary key is now the unit of learning.
- **May 22-23 — factor_buckets v3 + decision forest (ADR 3010, 3011).**
  Higher resolution on RSI/BBP/ZS/ADR; pairwise interactions captured
  per cell.
- **May 25 — Three cleanups (ADR 3012, 3013, 3014).** Loser-veto upgrade;
  quality floors (natural-target + feature-quality); family_loose default
  flipped OFF.
- **May 27 — Promotion + retirement day (ADR 3015, 3016).** HTF gate
  promoted observe→hard then retired same day. 6 research strategies
  promoted live. New routing table `v1.14b` (1737 rows / 250 leaves).
  B-1 Patch C (B-079 fix) shipped same day.
- **May 28 — The collapse (ADR 3017, 3018).** V3HybridScorer disabled.
  LightGBM PRIMARY GATE at 0.75. ml_router demoted to shadow.
  DailyCircuit disabled. 4-layer matrix cascade commented out.
- **May 29 — Matrix shadow advisor (ADR 3019).** Raw matrix CSVs wired
  alongside LightGBM as cross-validator. Three parallel observers live.

## What changed in the live system

| Dimension | Era 4 end (April spec) | Era 5 end (May 30) |
|---|---|---|
| Gates registered | 14 | 7 active (5 retired, 6 commented out) |
| Primary edge call | V3HybridScorer (session × family thresholds) | LightGBM v0 @ 0.75 |
| Routing | BB-state → strategy hard-coded | parquet table, 1737 cells × 250 leaves |
| Strategies registered | 5 | 13 |
| Strategies routed | 3 (reversal, dbb_trend, direct) | 7+ (+box, ifvg, session_breakout, compression_expansion, trend_pullback, chaikin_macd_atr, compression_reversion) |
| Audit ledgers | 1 (execution-audit.jsonl) | 7 (incl. 3 parallel ML observer streams) |
| Attribution | inferred at journal-write from log scan | dedicated `OrderAttributionWriter` with `order_id` lookup |
| Drawdown protection | DailyCircuitGate (in-process) | Telegram 5-min timer (out-of-band) + DailyCircuit config-flippable |

## What stayed the same

Management is essentially unchanged from Era 4:
- Cheese-slicer ratchet at 0.5 (after the 0.7 experiment failure)
- 4-stage TP1 / TP2 / TP3 + runner harvest
- LIMIT-only entries with GTD
- SL-advancement-only (no market exits since Era 2)
- 26 candidate pairs (down from 27 with screener disconnect)

## Open questions at end of era

1. **Does matrix + LightGBM agreement actually predict realized WR?** —
   needs ~30-50 closed trades at the new threshold to baseline. Live
   trade count was 0 on 2026-05-30 (weekend, fresh reboot post-streak).
2. **Do the 6 promoted strategies hold up live?** — Phase 3 lab sweep
   still running on Mini; per-strategy validation pending. CE + CR
   matrix rebuild deferred to a `v1.14c` candidate.
3. **Does the matrix shadow disagree with LightGBM often enough to
   matter?** — first agreement/disagreement curves expected after
   ~100 picked candidates.
4. **Is loser-veto still the right policy when matrix is shadow not
   gate?** — ADR 3012 superseded by ADR 3019; revisit if disagreement
   logs show LightGBM admitting matrix-vetoed candidates that lose.

## Lessons recorded

- **The right architecture beats better tuning.** The V3 scorer was
  being tuned for months; the LightGBM gate was trained once and
  outperformed because the architecture (per-candidate confidence over
  the full feature space) was right for the problem.
- **Lab-mined truth eventually has to enter the live path.** The matrix
  was correct and offline for months while the gates approximated it
  in production. The cost of duplication was hidden but real (gate
  audit overhead, divergent verdicts, 14-gate cognitive load).
- **Observe → HARD via three-way confirmation.** HTF gate was confirmed
  three ways (matrix, modules, LightGBM) before promotion; promotion
  was right; same-day retirement once the router subsumed it was also
  right. Both moves were cheap.
- **Magnitude-based early stop is fine when the prior is "current is
  working".** Ratchet 0.7 was rolled back at 27 trades — well below any
  statistical floor — because the loss magnitude said "this is going the
  wrong way, don't pay to prove it." Pre-registered stop rules now
  required for any new live experiment.
- **Out-of-band alerting beats in-process safety nets.** The drawdown
  alerter survived multiple bot states (down, paused, circuit-tripped,
  healthy) where DailyCircuitGate would have either silently passed or
  noisily failed. Both layers exist now; only the alerter is load-bearing.

## What comes next (the V4 cutover)

The system at end of Era 5 is recognizably a different architecture
from the V3 launch state. The plan is to formalize this as a V4 cutover
once Phase 3 sweep finishes and the bot has baked a week or two on the
new corpus. The cutover doc will live separately when it's ready; this
retrospective stands as the bridge.

## Cross-references

- ADRs 3002 through 3019 — full decision trail
- `LIVE_SYSTEM_SPEC.md` — current executable truth (2026-05-30 rev)
- `evolution-timeline.md` Era 5 — chronological log
- `bug-catalog.md` B-075 through B-079 — bugs surfaced this era
- Vault: `wiki/projects/scrooge-v3-*` for per-project arcs
