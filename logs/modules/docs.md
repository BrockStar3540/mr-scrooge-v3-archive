# docs — Developer Log

**Files:** `docs/BLUEPRINT.md`, `docs/MASTER_THEORY.md`, `docs/THEORY_TO_CODE.md`, `docs/V2_MASTER_THEORY.md`

---

## 2026-04-14 — Initial creation

**BLUEPRINT.md** — Full V3 architecture: 20 sections covering design principles, system shape (3 orchestrators), 11 core layers, 7 contracts, registries, module modes, state store, event bus, strategy router, gate pipeline, feature engine, advisory layer, dashboard design (5 tabs, status colors), configuration system, testing architecture, observability, execution doctrine, migration path, acceptance criteria, final doctrine.

**MASTER_THEORY.md** — Two-part structure:
- Part I (Sections 1-23): Doug/Sylvia source theory preserved verbatim from V2. Ground truth. Covers: core philosophy, market model, sucker move (including "messy" variant), levels-first rule, liquidity zones, never-trade-middle, buy-lows-sell-highs, daily chart first, box/range framework (with fakeout vs true break, alternative box, transition rules, multi-box priority, validity decay), two-timeframe model, pitchfork entry, John Wick candle quality, falling knife rule, entry execution, opening/gap behavior, daily bias, trade management (partials, BE, hourly trailing, exit signals), re-entry logic, sideways consolidation, volume evidence, measured moves, complete trade flow, theory boundary declaration.
- Part II (Sections 24-37): Engineering extensions with source cross-references. Covers: three core behaviors, box lifecycle state machine (6 states, trade permissions, creation algorithm, decay parameters, gap cases, double trap), BB classification (double band), ATR/OTR, strategy stack, regime theory, gate theory, execution doctrine (trigger-side, no-man's-zone, spread trailing, lifecycle tracking), management extensions (ratchet, time stop, green exit, emergency close), re-entry engineering, timing physics, system philosophy, edge summary.

**THEORY_TO_CODE.md** — Bridge doc: 35-row mapping table (theory section -> V3 layer/module/contract/config path), V2 problems -> V3 fixes table, full pipeline flow diagram with module names, 9-phase implementation checklist.

**V2_MASTER_THEORY.md** — Reference copy of the V2 source theory file, kept for comparison.

**Decisions:**
- Two-part theory structure ensures source truth is never diluted by engineering additions
- "When Part I and Part II conflict, Part I wins" — explicit hierarchy
- V2 reference copy kept alongside V3 version for audit trail
