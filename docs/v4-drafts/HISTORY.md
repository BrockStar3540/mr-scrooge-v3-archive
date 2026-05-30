# History — Mr. Scrooge V1 → V4

How a single-strategy box-reversal bot in February 2026 became a
25-strategy ML-routed framework by May 2026. This is the public
narrative; the full detail (commit refs, postmortems, bug catalog,
decision records) lives in [`docs/history/`](docs/history/) and
[`docs/decisions/`](docs/decisions/).

---

## Era 1 — Box reversal origin (V1, February 2026)

**What we believed.** The market trades inside a daily box defined by
the previous day's high and low (PDH/PDL). Liquidity sweeps at the box
edges produce reversal opportunities — the *Box Reversal* doctrine.
Combine the sweep with a "sucker move" (3-5 directional candles before
reversal) plus a "pitchfork" entry pattern, and you have a tradable
edge.

**What we built.** A single-strategy bot. One scoring function, six
gates (sucker move, pitchfork, ATR, OTR, RR, BB exhaustion), one
management style (fixed-pip stops, V1 4-stage harvester at TP1/TP2/TP3
+ runner). The full doctrine fit in one Word document
([`v1-exec-summary-feb-2026.md`](docs/history/v1-exec-summary-feb-2026.md))
written by hand.

**What we learned.** The strategy worked on paper. Live, V1 hit ~75%
WR on NORMAL-regime trades but the system fought itself: green-exit
crises (reactive TP-setting fired infinite retry loops on March 12),
percentile-filter bugs that shrank box geometry (B-070), regime
classifier amnesia at UTC midnight (B-072). The *strategy* was
extracting edge; the *infrastructure* was leaking it.

**What changed our minds.** A 4.5-hour silent outage on March 24
(single indentation error, no logs, no alerts, healthy-looking bot)
proved the operational layer needed more than a doctrine document. We
needed instrumentation, gates that didn't fight each other, and a
system that could survive its own bugs.

---

## Era 2 — Modular rewrite (V2, March 2026)

**What we believed.** The strategy was sound; the *architecture* was
the problem. Rewrite into clean modules — a thin runtime conductor with
delegated coordinators for scan, execution, and position management.
Add a dual-loop architecture: a 5-minute scan loop for new entries and
a 3-second loop for SL/TP management. Decommission Mr. Sprite (the
crypto sibling bot) to focus.

**What we built.** A 232-line conductor (`runtime.py`) with eight
extracted modules. Family-aware scoring overlays (trend candidates get
+6/+4/+2 adjustments; reversal candidates use the base scorer). Hybrid
SL trailing with proactive limits backstopped by native broker SL.
Stop validation with four guards (trigger-side, no-man's-zone, spread
kill, buffer minimum) — the
[execution physics](docs/EXECUTION_PHYSICS.md) we still use today.

**What we learned.** Modular rewrite revealed how much of V1's behavior
was *implicit coupling* — small parameter changes broke other
parameters because they shared reference frames. The big
[TRADE_PHYSICS_FIRST_PRINCIPLES](docs/TRADE_PHYSICS_FIRST_PRINCIPLES.md)
analysis (April 15) named this explicitly: the stop must be set by the
market (signal candle extreme), the reward by the structure (box range),
the cost by the broker (spread). Hand-tuned scoring couldn't capture
these relationships.

**What changed our minds.** A 30-minute rolling box experiment (March
19-20) burned 23 commits and broke profitability before we reverted to
daily PDH/PDL — but the discipline of reverting all 23, keeping only
the 17 incidental fixes that survived, became a doctrine in itself.
*"Don't pivot on hot data."*

---

## Era 3 — V3 hybrid scorer (April 2026)

**What we believed.** A WR-Lift hybrid scoring function, calibrated per
strategy family and per trading session, would replace V1's
single-formula approach. Layer 0 hard blocks, Layer 1 single-factor
points (17 factors), Layer 2 paired-aspect bonuses (15 pairs),
session-aware thresholds.

**What we built.** [`V3HybridScorer`](docs/decisions/2003-v3-scoring-system.md)
plus a 14-gate pipeline: regime floor, regime-strategy router,
sub-regime filter, entry filter, HTF trend filter, plus all the
physical-state gates from V2. The strategies modularized into
families: `reversal`, `dbb_trend`, `direct`. Per-pair management
profiles (`trend_runner` for DBB; `reversal_core` for reversal).
[Live on 2026-04-15.](https://github.com/BrockStar3540/mr-scrooge-v3)

**What we learned.** A 48-hour losing streak (April 28-30: 16 trades,
6.2% WR, 11/11 long disasters into JPY downtrend, −$5,350) forced an
honest diagnosis. Per-strategy ML observer audits found `dbb_trend` had
clean separability (AUC 0.774, 71.8% WR at p≥0.5) but `direct` was
near-noise. Three independent investigations (manual tradebook,
EUR_CAD #1918 post-mortem, offline v2 scorer build) all reached the
same finding: the V3 scorer ranked candidates well by *maximum
favorable excursion* potential but had near-zero correlation with
*realized R*. The architecture was wrong; better tuning wouldn't fix
it.

**What changed our minds.** A 60-day broker-truth pull (May 4: 152
trades, 39.6% WR, −$30,958) closed the question. WR matched replay —
entry quality wasn't the problem. The dollar mean was wildly
different — execution friction, management, and regime drift were.
And critically: the 47-factor audit found 15 factor sign-flips between
DBB and Direct families. *Branched signal needs branched scoring; a
global scorer averages it away.*

---

## Era 4 — Matrix collapse + ML routing (V3.5, May 2026)

**What we believed.** The lab corpus we'd been mining offline (838k
trades, 6 months, 27 pairs, 14-bucket signature) had the answer the
V3 scorer was missing — per-cell admission rules learned from data,
not hand-tuned. Bring the matrix into the live admission path.

**What we built.** A two-week structural collapse:

- **MatrixRouter** ([ADR 3008](docs/decisions/3008-matrix-router-replaces-regime-and-routing-stack.md))
  replaced seven gates with one parquet lookup
  (`routing_table_v10_fast_v1_14b_full_matrix.parquet`, 1737 rows / 250
  leaves). The seven gates had been encoding overlapping slices of the
  same per-(pair × family × direction × session) question in seven
  divergent formats. Now: one parquet, one log per cell.
- [**factor_buckets v3**](docs/decisions/3010-factor-buckets-v3-expansion.md)
  expanded RSI/BBP/ZS/ADR bucket resolution per
  empirical neighbor-WR analysis. 20 KMeans regimes per pair, 540
  (pair × regime) cells across 27 pairs, ~25k WIN/LOSE rules total.
- [**LightGBM v0**](docs/decisions/3017-v3-hybrid-scorer-disabled-lightgbm-primary.md)
  trained on the full 838k corpus (holdout AUC 0.6025). Promoted to
  PRIMARY GATE at threshold 0.75 — the top ~3% of lab cohort, ~75% sim
  WR. **V3HybridScorer disabled.**
- **Matrix shadow advisor** ([ADR 3019](docs/decisions/3019-matrix-wiring-as-shadow-advisor.md))
  wired the raw matrix CSVs alongside LightGBM as a parallel
  cross-validator. `ml_router` demoted from primary gate to shadow.
- [**Six new strategies promoted**](docs/decisions/3016-six-strategy-promotion-and-routing-v1-14b.md)
  to live (ifvg, session_breakout, compression_expansion, trend_pullback,
  chaikin_macd_atr, compression_reversion), bringing the live strategy
  roster from 3 to 13.
- The **out-of-band drawdown alerter** ([ADR 3007](docs/decisions/3007-drawdown-alerting-telegram-timer.md))
  shipped during the May 4 diagnosis arc — a 5-minute systemd timer
  pinging Telegram if daily P&L crosses thresholds. Survives the bot
  being sick.

**What we learned.** The lab-mined approach didn't merely outperform
hand-tuned scoring — it changed what *kind* of question we were
asking. V3.0 asked "what's a good trade signature today?" The matrix
answered "in this regime, on this pair, in this session, with this
bucket signature, what's actually worked over 838k historical trades?"
The shift from hypothesis-driven scoring to data-mined admission was
the move.

**What changed our minds.** Within the first 48 hours of LightGBM at
0.75 plus matrix routing, the bot didn't suddenly become profitable
— the regime was bearish-friendly and the bot was structurally
long-biased, [a separate concern still under investigation](docs/decisions/3015-htf-trend-filter-observe-to-hard.md).
But the *failure modes* shifted from "scorer made a bad call" to
"the regime doesn't favor what our strategies emit." That's a more
tractable question.

---

## Era 5 — Consolidation (V4, what you're reading)

**What we believe.** The architecture that crystallized in late May
2026 — matrix-routed admission, LightGBM primary gate, three parallel
observer ledgers, ~25 modular strategies with no privileged status,
out-of-band alerting — is *the* architecture. Future work iterates
within this frame; it doesn't replace it.

**What V4 represents.** A clean cut. New repo, new top-level package
(`scrooge`, no version suffix), MIT license, public documentation,
no internal references to V1/V2/V3 in code or comments. The
[Box Reversal master theory](docs/archive/MASTER_THEORY_v1-box-reversal-origin-2025.md)
that started V1 is preserved in `docs/archive/` as historical context
— it became one of 25 strategies in the encyclopedia, no longer the
guiding doctrine.

The lab corpus continues to grow. The matrix gets re-mined when new
strategies are promoted. The LightGBM model gets retrained as the
corpus accumulates. The routing table version bumps on each rebuild.
The bot evolves; the architecture stabilizes.

**What's deliberately NOT in V4.**

- No broker abstraction layer. OANDA only.
- No hardcoded master theory. All strategies plug into the same
  scoring + routing framework.
- No "this is V3..." comments in code. The lineage lives in
  `docs/history/` and the ADR trail, not in the source.
- No live position state, broker credentials, or runtime ledgers in
  the repo. Those are operational, not architectural.
- No promise of forward profitability. Lab-validated edges decay;
  the regime that produced the 838k corpus may not be the regime
  the next quarter produces. We measure honestly and document the
  decay openly.

---

## Threads that died along the way

Documented in `docs/history/dead-ends-graveyard.md` for the curious;
summarized here:

| Idea | Tried | Why dropped |
|---|---|---|
| Mr. Sprite (crypto) | V1 era | Removed March 25 — crypto-specific bugs distracted from forex focus |
| 30-minute rolling box | March 19-20 | Two-day experiment broke profitability; reverted to daily PDH/PDL |
| Reactive market-order exits | March 12 | Green-exit crisis — infinite retry loop in production; SL-advancement-only since |
| Global scoring (single weights for all families) | V1 → V3 | Closed by [ADR 3001](docs/decisions/3001-regime-aware-not-global-score.md) |
| Strict ATR + OTR hard gates | March 11 | Demoted to advisory; MASTER_THEORY audit found transcripts had no such requirement |
| Reverse-every-strategy experiment | May 25 | 2hr live test, inconclusive; surfaced 2 integration bugs preserved in code for regime-conditional revival |
| Ratchet 0.7 (vs 0.5) | April 29 | 27-trade live experiment, −$245/trade, rolled back per [ADR 3004](docs/decisions/3004-harvest-same-cycle-race-and-ratchet-rollback.md) |
| Universal "flip the probe" framing | May 30 | Reframed correctly as "trade in the direction of the regime trend" — same insight, durable expression via the HTF hard gate |

---

## Pivots worth video-series treatment

For anyone (Brock-future, Claude-future, or a reader) wanting to walk
the highest-narrative moments:

1. **The 30m box experiment failure (March 19-20)** — 23 commits in 2
   days breaking profitability, the discipline of reverting all 23
2. **MASTER_THEORY realignment (March 11)** — discovering the code had
   invented rules not in the source transcripts; deleting BOX_THEORY.md
3. **Green-exit crisis (March 12)** — infinite retry loop in
   production; the move to SL-advancement-only
4. **4.5-hour silent V2 outage (March 24)** — single indentation
   error, no logs, no alerts, healthy-looking bot
5. **4-actor coordination revelation (April 10)** — bot, ratchet,
   SL-limit, harvester all modifying the same OANDA trade with no
   shared state; the 46-order API spam that revealed it
6. **The \$5,350 losing streak (April 28 → May 4)** — 48h, 16 trades,
   11/11 long disasters into JPY downtrend; the diagnostic arc that
   pulled out B-1 attribution, harvest race, ratchet rollback,
   drawdown alerter, and the matrix integration thesis in a single
   coordinated response
7. **MatrixRouter collapse (May 14 → May 28)** — 14 gates to 7, the
   moment lab-mined truth entered the live admission path
8. **LightGBM PRIMARY GATE (May 28)** — single config commit ending a
   year of hand-tuned scoring
9. **The reframing (May 30)** — "wrong direction" finding becomes
   "trade in the direction of the regime trend" — same insight, much
   more durable expression

---

## What V4 is, in one paragraph

A modular forex trading framework where 25 strategies share a common
scan/admit/execute/manage pipeline, with admission decided by
lab-mined per-cell rules and a LightGBM scorer trained on six months of
labeled outcomes, with parallel shadow advisors that cross-validate
every live decision and out-of-band alerting that survives bot
failure. It started as one person's hand-coded box-reversal hypothesis
and became — through a year of measured iteration, recorded mistakes,
and the discipline of letting data overturn theory — something
considerably more honest about what it knows and doesn't know.

That's the system. The rest of this repo shows you how it works, why
it works the way it does, how it got there, and how you could verify
or reproduce any claim it makes.
