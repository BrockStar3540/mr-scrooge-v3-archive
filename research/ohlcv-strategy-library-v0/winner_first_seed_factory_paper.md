# Winner-First Seed Factory

Generated: 2026-05-14

## Abstract

This research program starts from a different premise than standard regime-first quantitative trading research. The usual workflow defines a market regime taxonomy first and then asks which strategies survive inside each regime. Our working thesis is the reverse. We treat each textbook strategy as a micro-bot, run it on each currency pair, sort the resulting winners and losers, and then search inside mixed winner-loser pockets for small factor-defined winner islands. When such an island is found, the island itself becomes the candidate new regime for that micro-bot.

This matters because broad theoretical regimes frequently mix winners and losers together. A regime label such as `technical_regime_53` can still be useful as a rough parent container or skip map, but it is not assumed to be the source of edge. Edge is assumed to live in narrower behavioral neighborhoods that are only visible after strategy-first outcome sorting. The research goal is therefore not to prove that a small number of strategies are globally robust. The goal is to build a large inventory of micro-strategy seeds, each defined by a concrete textbook parent, a pair, a direction, and a local factor pocket where winning behavior concentrates.

## Core Hypothesis

The central hypothesis is that profitable behavior is fragmented. A textbook strategy may fail globally, fail on most pairs, and still contain one or more narrow local pockets where it behaves like a real edge. Those pockets are meaningful even when they are small. A seed such as `10 winners / 0-2 losers` is not a deployable trading rule, but it is a valid micro-strategy nucleus. If enough such nuclei can be harvested across many parents, pairs, and contexts, they can later be expanded, replayed, pruned, clustered, and assembled into a denser inventory that can trade through a larger share of market conditions.

Under this thesis, the relevant unit of discovery is not the textbook rule alone and not the broad regime alone. The relevant unit is the winner island: a context-conditioned descendant of a textbook micro-bot that isolates a small pocket of superior trade outcomes.

## Current Methodology

### 1. Textbook strategy library as parent population

We begin with an explicit OHLCV strategy library containing 63 textbook-style strategy variants across categories such as trend, mean reversion, breakout, false breakout, compression, expansion, range, session, hybrid, and momentum exhaustion. Each strategy is evaluated independently on each FX pair with spread-aware execution and forward outcome scoring. This produces a trade ledger at the row level containing pair, strategy ID, direction, realized R, session, factor values, and broad technical regime labels.

### 2. Strategy-first winner and loser sorting

For each `(strategy_id, pair, direction)` cell, and in some passes each `(strategy_id, pair, direction, technical_regime_53)` cell, we measure how winners and losers distribute across factor space. Existing analysis already established three things.

1. ATR ratio is a frequent discriminator between winners and losers.
2. The 53 broad OHLCV regimes do not cleanly separate winning and losing trades on their own.
3. Mixed cells often contain local sub-pockets where simple factor splits sharply improve purity.

This result is the basis for the winner-first inversion. We do not ask whether old regimes work. We ask whether a broad mixed cell contains a pocket where a specific micro-bot works.

### 3. Targeted winner-island shaving

The first winner-island miner used the mixed-cell map from the prior regime-split analysis and searched only each parent cell's strongest separator factors plus session. It produced 438 raw candidate rule variants, which collapsed to 60 distinct best-parent seeds. These included 6 pure seeds with at least 10 wins and 0 losses, plus 14 holdout-clean seeds with at least 3 holdout wins and 0 holdout losses.

Example seeds illustrate the pattern. A broad mixed parent such as `TF6_ma_ribbon_long / AUD_USD / long / C02` with `399 winners / 1300 losers` can contain a narrow factor shave such as `RSI14` plus `BB_compress` that yields `11 winners / 0 losses`. In this framework, the new candidate regime is not simply `C02`. It is the factor-defined winner island inside that parent.

### 4. Preserving sibling descendants instead of over-collapsing

Collapsing immediately to one best seed per parent discards valuable local structure. To prevent that, we built a diversified sibling bank from the full raw island set. Rather than preserving only 60 best-parent seeds, the sibling-bank pass retained multiple distinct descendants per parent when the factor recipe materially differed. This expanded the inventory to 141 sibling seeds across the same 60 parent cells, including 31 holdout-clean sibling seeds.

This is an important methodological result. It suggests that many mixed parents are not single-seed parents but seed families. One broad parent can spawn several neighboring micro-bots, each with a different factor signature and slightly different outcome profile.

## What the Current Results Mean

The current results do not prove deployable robustness. They do prove something else that is strategically important: the seed factory is real. The textbook library is not behaving like a static menu of fixed strategies. It is behaving like a parent population from which conditional descendants can be mined.

Three conclusions follow.

1. Broad regime labels are not sufficient. They can organize search, but they do not explain the edge by themselves.
2. Textbook strategies do not need to survive globally to be useful. They only need to generate localized winner islands.
3. The discovery space branches. Once one winner island is found, nearby sibling islands often exist and should be preserved rather than discarded.

In other words, the research is no longer about identifying a handful of survivors. It is about constructing a growing ecology of micro-bot descendants.

## Planned Expansion Into a Larger Seed Set

The next phase is to turn the current island inventory into a repeatable seed factory capable of producing many more candidate micro-bots.

### A. Mutate textbook parents deliberately

Textbook strategies should not remain fixed. Each parent can be varied along dimensions such as entry trigger strictness, volatility filters, session filters, time-of-day windows, compression or expansion thresholds, momentum stretch thresholds, and stop/target geometry. The point is not to search blindly across all possible formulas. The point is to create plausible descendants that change the winner-loser mix enough to reveal new islands.

### B. Expand from seed families, not just raw parents

The most promising expansion route is to mutate around the existing winner-island families themselves. A parent that already produced one or more seeds is much more likely to produce additional useful descendants than a parent starting from zero. This means future passes should branch around the 141-sibling inventory: widen or narrow factor bands, swap adjacent session filters, relax or tighten RSI and ATR pockets, and test nearby behavioral neighborhoods.

### C. Preserve multiple descendants when they are meaningfully distinct

The inventory should not collapse too early. If one micro-bot parent yields several siblings with distinct factor signatures, those siblings should remain separate seeds. A large tradeable inventory will likely require many overlapping but non-identical context-conditioned descendants rather than one canonical rule per parent.

### D. Build toward condition coverage

The end goal is not a small elite club of seeds. The end goal is a sufficiently broad and dense inventory that at least some seeds are active and valid through most market conditions. This implies explicit coverage work across trend, reversal, compression, expansion, session transitions, high-volatility environments, low-volatility environments, majors, crosses, and distinct liquidity windows.

## Validation Philosophy

Validation remains necessary, but it comes after seed creation rather than before it. A small seed is meaningful if it isolates real winner concentration. That seed should then move through stricter stages.

1. Row-level seed discovery.
2. Sibling preservation and family expansion.
3. Bar-by-bar replay and path-true execution checks.
4. Cost and spread realism.
5. Blind forward validation.
6. Portfolio assembly and condition-coverage testing.

This ordering is deliberate. If strict deployment filters are imposed too early, the research collapses back into broad survivor logic and misses the actual discovery task, which is to generate enough promising nuclei in the first place.

## Research Claim

The main claim being tested is that useful regimes should be derived from winner islands found inside strategy-first outcome cells, rather than imposed as the primary explanatory object upfront. In this design, regimes are not the starting taxonomy. They are the byproduct of successful local behavior.

If that claim continues to hold as the seed bank grows, then the project will have demonstrated a practical methodology for transforming a finite textbook strategy library into a much larger, context-conditioned micro-bot inventory. That would create a path toward an adaptive trading system whose breadth comes not from a few universal rules, but from many narrowly specialized descendants that collectively span a wider share of market behavior.

## Immediate Next Steps

1. Treat the 141 sibling-bank seeds as the first seed inventory, not the final output.
2. Generate neighborhood mutations around each seed family rather than only around raw textbook parents.
3. Re-run the winner-island miner on the expanded descendants and append new sibling families.
4. Start measuring coverage by condition type so seed count is translated into expected market-condition reach.
5. Only after the inventory is materially larger should the project shift emphasis toward bar-by-bar replay, execution realism, and deployment selection.

The program is therefore best described as a winner-first seed factory. Its success criterion is not whether one strategy survives everywhere. Its success criterion is whether repeated mining, mutation, and sibling preservation can manufacture a large enough population of micro-bot seeds to trade through most market conditions with continual specialization rather than broad universal rules.


---

## 2026-05-14 Addendum — Parser-Tree Architecture + Ungated Replay Validation

This addendum extends the original paper with two developments from 2026-05-14:

1. A new architectural pattern for the live trading runtime: the **parser tree** (dispatch-only, veto-by-absence at the leaf).
2. An ungated 26-pair / 6-month replay that validates the core inversion claim with direct cell-level evidence.

### Parser-Tree Architecture

The earlier production design used a stack of veto gates — each gate decided whether a candidate trade should pass or fail. The new design replaces the gate stack with a routing tree where every node is a parser/dispatcher:

```
tick → regime parser  (label: technical_regime_53)
     → pair parser    (label: symbol)
     → session parser (label: session_bucket, 7 UTC-stable wall-clock buckets)
     → routing table lookup
        → list of attached strategies + per-cell parameter overrides
        → empty list = nothing fires = "death by absence"
```

Three properties make this pattern materially different from the gate stack.

**1. No intermediate veto.** The regime parser does not kill any tick; it labels it. The pair parser does not kill; it dispatches. Only at the leaf — the (regime, pair, session) cell — does enforcement happen, and it happens implicitly through the absence of an attached strategy. This is a strict generalization of the gate stack because any gate veto can be expressed as "no strategy is attached at this leaf for this family / direction."

**2. The routing table is data, not code.** Cells are rows in a parquet file, hot-loaded at boot. Each row carries: strategy, family, direction-constraint, r_target, score_boost, and basis evidence (n, wins, sum_R, mean_R, WR). Adding a new (cell × strategy) attachment requires no code change — only a new row.

**3. The dispatch tree generates death-point telemetry as a first-class signal.** Every tick that fails to fire records its terminal node `(regime, pair, session, decision_state)`. Aggregated over time this is a heatmap of unmet structural demand. If a cell that historically had attached strategies starts producing many "no-fire" outcomes, it is an early signal that the strategy is decoupling from the underlying microstructure. If a previously empty cell begins to accumulate dense traffic, it is an early signal that the seed factory has a new target. Under a stable gate stack, both of these signals are invisible by construction.

### Implementation Snapshot

The parser tree is live in the V3 runtime in observe mode as of the commits below:

| Layer | Mechanism | Status |
|---|---|---|
| Regime parser | `TechnicalRegime53Calculator` feature (V3 port of the research classifier) | live |
| Pair parser | Symbol is already known per tick | inherent |
| Session parser | `SessionBucketClassifier` (7 UTC buckets, DST-stable) | live |
| Lookup | `RoutingTable` class, hot-loaded from `data/routing_table_v1.parquet` | live (observe) |
| Veto-by-absence enforcement | Routing-table `lookup()` returning empty list | observe-mode (flips with `routing_table_mode: hard`) |
| Telemetry | `RoutingTelemetryRollup` with two tiers (~10KB/day rollup + 1-in-N sampled deaths) | shipped disabled |

Initial routing table v1: **2,804 attached cells across 613 unique (regime, pair, session) leaves**, mined from 1.26M trades (textbook + V3 trainer probes, last 6 months). Cells require n ≥ 10 AND sum_R > 0 AND WR ≥ 0.30 to be attached. **1,553 cells with historical traffic remain unattached** — these are the next seed-factory targets, surfaced automatically by the build.

### Ungated 26-Pair Replay — Direct Evidence

To answer the open question "what does V3 look like without any regime gating," we ran the full V3 probe library against all 26 pairs over the last 6 months with the regime filter disabled. The result is 90,015 filled trades at r_target = 1.5.

**Headline.** Without gating, the bot is mildly red: WR 40.6%, mean R −0.027, sum R −2,415 over 6 months. This sets the unfiltered baseline.

**The decisive finding for the parser-tree thesis.** When trades are split by whether they land in "dead" regimes (R04, T07, Z01 — the ones the previous gate vetoed) versus "alive" regimes, the per-trade economics are *identical*:

| Bucket | n | WR | mean R |
|---|---:|---:|---:|
| DEAD regimes (R04 + T07 + Z01) | 86,420 | 40.3% | −0.028 |
| ALIVE regimes | 3,595 | 40.0% | −0.028 |

The dead regimes are not structurally worse on a per-trade basis. They are merely where 96% of trade volume happens to land. The previous gate-based design, which vetoed dead regimes wholesale, was throwing out productive cells along with the losing ones.

**The throwaway cost.** Eight (probe × regime53) cells inside the so-called "dead" regimes were positive across the full 6-month corpus and would have been vetoed by the existing gate. They total +366 R of forgone edge:

| probe | regime53 | n | sum R | WR |
|---|---|---:|---:|---:|
| echo_box_fade_v2 | T07 | 6,740 | +167.6 | 42.0% |
| alpha_breakout_retest_v2 | Z01 | 3,024 | +96.3 | 42.5% |
| alpha_breakout_retest_v2 | T07 | 3,831 | +43.0 | 41.9% |
| bravo_failed_momentum | R04 | 1,491 | +23.5 | 42.2% |
| alpha_pullback_v2 | Z01 | 3,416 | +20.4 | 42.1% |
| bravo_expansion_continuation | T07 | 2,971 | +4.4 | 41.7% |
| bravo_expansion_continuation | R04 | 2,607 | +3.1 | 42.0% |
| delta_tag_and_go_v2 | T07 | 273 | +2.5 | 41.0% |

**Confirmed bleeders.** Twenty-six (probe × regime53) cells lost more than 10 R over the 6-month corpus. The worst was `charlie_pullback_continuation_v2 × R04` at −566.7 R across 7,478 trades; the same probe also lost −430.9 R in Z01 and −334.5 R in T07. `alpha_extended_fade_v2` similarly bleeds in T07 (−223.6 R), Z01 (−178.7 R), and R04 (−80.3 R). Under the parser-tree, these are non-attached cells; under the gate stack, they were vetoed as a side effect of a coarser rule.

**Same-probe-different-cell signal.** A specific probe can be globally negative and yet contain strongly positive cells. `alpha_extended_fade_v2` averages −0.125 R across the full corpus but its `T06 × off_hours` slice is +0.434 R / 58.6% WR over 29 trades, and its `O06 × off_hours` slice is +0.413 R / 56.5% WR over 23 trades. No global filter on `alpha_extended_fade_v2` would have caught this. Only per-cell routing surfaces it.

### What This Means for the Methodology

The ungated evidence reinforces — and sharpens — the central claim of this paper. Useful structure is fragmented across narrow context cells. Coarse classifications (regime taxonomies, family-level routes, BB-state heuristics) are valuable as dispatch labels but are too blunt to be used as enforcement layers. The seed factory's role is to mine these narrow cells; the parser tree's role is to enforce them in production.

Three concrete updates to the methodology:

1. **Routing-table population is now a primary research deliverable.** Each seed in the seed bank carries its (strategy, regime, pair, session) cell. The routing table is the union of attached seeds, refreshed periodically.
2. **Death-point telemetry replaces "filter accuracy" as the key live metric.** Instead of asking "did the gate correctly filter?" we ask "which cells produce traffic with no attached strategy?" and "which previously-attached cells are losing their fire rate?"
3. **Regime taxonomy is downgraded from enforcement device to context label.** It still organizes the dispatch tree, but it no longer controls the kill decision directly.

### Today's Commits (mr-scrooge-v3)

| commit | content |
|---|---|
| daa5377 | Port `technical_regime_53` as V3 live feature |
| 04507d8 | Ungated 26-pair replay analysis — validates parser-tree |
| 0b2e3cc | Routing telemetry: tiered rollup + sampled death writer |
| 6c7bbc4 | Routing table v1 + session bucket classifier + observe hook |
| bc06c4e | Moving-regime loser bank extended to all 4 buckets |
| 1a03cec | Trainer-v2 probes ported as V3 live strategies (10, disabled) |
| a88edb5 | `RegimeStrategyRouterGate` v2: 53-regime allow-list (to be retired in Phase D) |
| 7570e1c | 91 last-6mo moving-regime seeds + initial loser bank |

### Open Items (Phase D and Beyond)

1. **Phase D — regime gate → label-only.** Stop vetoing the eight in-dead-regime winning cells. The current `RegimeStrategyRouterGate v2` should pass-through always and record its label; the routing table is the only enforcer.
2. **Routing table v2.** Rebuild from the ungated evidence (not the narrower seed-factory lens). Attach the eight throwaway cells, explicitly kill the 26 bleeders. Add per-cell `r_target` and `score_boost` overrides for the "same probe, different cell" signal.
3. **Mode flip.** Move `routing_table_mode` from `observe` to `hard` once v2 lands. Enable `routing_telemetry`. Begin accumulating the death-point heatmap.
4. **Death-point dashboard widget.** A live heatmap of `(regime, pair, session, decision_state)` over a rolling window, surfacing the unfilled-demand cells the seed factory should target next.

The seed factory and the parser tree are now coupled. The factory mines new cells; the tree enforces and observes them; the telemetry feeds back the next mining target. This is the expansion loop the doctrine originally specified, now operating on the live runtime rather than the research corpus alone.
