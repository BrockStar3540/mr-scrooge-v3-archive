# Mr. Scrooge

A multi-strategy, ML-routed forex trading bot for the OANDA practice/live
broker. ~25 trading strategies share a single pipeline; per-trade
admission is decided by a lab-mined per-pair / per-regime rule library
and a LightGBM scorer trained on 838k historical setups.

This is a research-grade production system. It is not financial advice
and is not for sale. It is published as a study in how a modest retail
trading system can be built, audited, and evolved transparently.

---

## What it does

For every market cycle (5-minute tick on 26 forex pairs):

1. **Feature extraction.** Compute a 14-bucket signature for the moment
   (Bollinger width + position, ATR at two timeframes, RSI, EMA slopes,
   Z-score, spread, daily-range consumed, four HTF alignment signals).
2. **Strategy emission.** Each of ~25 strategies independently
   evaluates whether its trigger conditions are met; emits a candidate
   with proposed direction, entry, stop, and target if so.
3. **Gate pipeline.** Seven hard gates filter for physical-state
   safety (cooldown, debounce, feature quality, zone caps, etc.).
4. **Matrix-router admission.** Per-pair / per-regime rules from the
   lab corpus determine which (pair × family × direction × session)
   cells are tradable.
5. **LightGBM primary gate.** v0 model (holdout AUC 0.6025) scores
   each surviving candidate; admits only those with `p_win ≥ 0.75` —
   the top ~3% of the lab cohort.
6. **Shadow advisors.** Matrix shadow + `ml_router` shadow record
   their independent verdicts alongside, for ongoing cross-validation.
7. **Best-pick execution.** Highest LightGBM score wins. Atomic LIMIT
   order with stop-loss and partial-harvest take-profit pre-placed.
8. **Position management.** Cheese-slicer ratchet, break-even logic,
   trailing stop, and emergency-close — all guarded by the trigger-side
   spread physics enforced in `StopPlanner`.

Out-of-band: a systemd timer pings Telegram every 5 minutes if daily
P&L crosses thresholds or the service stops.

---

## What's distinctive

- **Lab-mined routing, not hand-tuned scoring.** The admission decision
  comes from a 6-month / 838k-trade lab corpus mined into per-cell
  WIN/LOSE rules and per-factor lift tables. The bot does not consult
  a hardcoded "if RSI < 30 then trade" anywhere.
- **Three parallel observers.** LightGBM gates admission; matrix shadow
  and `ml_router` shadow both score the same candidates and log to
  separate JSONL ledgers. Disagreement between them is the highest-
  information audit signal in the system.
- **Modular strategies.** Strategies are plug-in modules. None has
  privileged status. Adding a strategy means dropping a probe file
  into `src/scrooge/strategies/`, running it through the lab, and
  letting the routing-table assembly decide which (pair × regime)
  cells admit it.
- **Audit-first design.** Every admitted trade carries an attribution
  payload (`OrderAttributionWriter`) that links broker fill back to
  the scoring snapshot. Live broker-truth audits cross-reference
  realized PnL against ML prediction continuously.
- **Decision history in-repo.** `docs/decisions/` contains 20+ ADRs
  going back to V1 (2026-02-15). When you ask "why does it work this
  way," the answer is committed alongside the code.

---

## Status

V4 is the consolidation cut: the architecture stabilized around
ML-routed admission in late May 2026 after the
[ML-routing collapse](docs/history/matrix-integration-era-may-2026.md)
arc. Live since 2026-04-15 (V3 launch) under continuous evolution; V4
freezes the architecture for publication.

The bot trades on a small OANDA practice account. It is not
recommended for live capital you cannot afford to lose. Forward
performance is not guaranteed by lab results — see the
[honest limitations](docs/RESEARCH_METHODOLOGY.md#known-limitations)
section of the methodology doc.

---

## Repo tour

```
mr-scrooge-v4/
├── README.md                 # you are here
├── HISTORY.md                # V1 → V4 narrative
├── LICENSE                   # MIT
│
├── docs/
│   ├── LIVE_SYSTEM_SPEC.md   # what the system does today (executable truth)
│   ├── ARCHITECTURE_DIAGRAM.md  # visual maps + flow diagrams
│   ├── STRATEGY_ENCYCLOPEDIA.md # all 25 strategies, equal footing
│   ├── TRADE_PHYSICS_FIRST_PRINCIPLES.md
│   ├── EXECUTION_PHYSICS.md
│   ├── RESEARCH_METHODOLOGY.md   # how the corpus was built
│   ├── LAB_REPRODUCTION_GUIDE.md # how to reproduce
│   ├── decisions/                # ADRs (20+, V1 → V4)
│   ├── history/                  # era timelines, bug catalog, retros
│   └── archive/                  # superseded docs with deprecation headers
│
├── src/scrooge/             # bot code (no version suffix — repo carries the version)
│   ├── strategies/          # ~25 strategy modules
│   ├── gates/               # 7-gate active pipeline
│   ├── advisors/            # LightGBM + matrix shadow + ml_router shadow
│   ├── execution/           # StopPlanner, order placement
│   ├── management/          # ratchet, BE, trail, harvest, emergency
│   ├── telemetry/           # audit ledgers, attribution
│   └── core/                # runtime, bootstrap, scan coordinator
│
├── data/
│   ├── routing_table.parquet         # live routing table
│   ├── matrix/                       # 3 lab-mined matrix CSVs
│   ├── models/lgbm_v0/               # LightGBM model + metadata
│   └── per_pair_modules/             # 27 pair modules with regime rules
│
├── research/                # reference samples + scripts (not full lab)
│   ├── sample_corpus/       # 1-pair / 1-month slice for examples
│   ├── harness/             # backtesting.py wrapper + dispatch
│   ├── matrix_mining/       # scripts that build factor_lift_table
│   ├── lightgbm_training/   # train script + reproducible recipe
│   └── notebooks/           # exploratory analysis
│
├── ops/                     # deploy / run / monitor
│   ├── systemd/             # systemd unit examples (sanitized)
│   ├── telegram_alerter/    # drawdown alert script + setup
│   ├── dashboard/           # 3-tab UI (Signals / Execution / DBB)
│   └── deploy/              # EC2-first workflow guide
│
└── tests/
```

---

## Getting started

Three reading orders depending on what you came for:

**Operator / deployer:**
`README.md` → `docs/LIVE_SYSTEM_SPEC.md` → `ops/deploy/` →
`docs/EXECUTION_PHYSICS.md` → `ops/systemd/` → run

**Researcher / reproducer:**
`README.md` → `HISTORY.md` → `docs/RESEARCH_METHODOLOGY.md` →
`docs/LAB_REPRODUCTION_GUIDE.md` → `research/notebooks/` → fork

**Understander (no deployment intent):**
`README.md` → `HISTORY.md` → `docs/STRATEGY_ENCYCLOPEDIA.md` →
`docs/ARCHITECTURE_DIAGRAM.md` → `docs/decisions/` (the "why we
believe what we believe" trail)

The bot **does not run** without OANDA credentials and a configured
practice or live account; see `.env.template` for what you need. We
keep no broker integrations besides OANDA (deliberate scope choice).

---

## License

MIT. See `LICENSE`.

---

## Acknowledgements

This work owes intellectual debt to:

- The wider ICT / smart-money trading community (Fair Value Gaps,
  Power of Three, liquidity sweeps), which inspired several
  strategies in the encyclopedia even where we ultimately measured
  their effectiveness differently from the original claims.
- The `backtesting.py` Python library, which underlies the lab harness.
- The `LightGBM` project for the primary admission scorer.
- The OANDA REST API as the broker integration layer.

No third-party signal services, no proprietary indicator licenses, no
external strategy purchases. All strategy logic, lab tooling, and
ML infrastructure built in-house and documented here.

---

## What this isn't

- Not financial advice. Not a recommendation. Not for sale.
- Not a multi-broker framework — OANDA only.
- Not a strategy you can drop into your platform of choice — it's
  a complete bot, not a signal generator.
- Not curve-fit-then-frozen — the lab corpus is open methodology,
  the routing table is regenerated on rebuild, and edges decay; this
  is documented openly rather than oversold.
- Not "the YouTube backtest of EMA20 said 60% so here it is."
  The lab tests every strategy across 27 pairs × 20 regimes × 5
  sessions and reports what actually held up.
