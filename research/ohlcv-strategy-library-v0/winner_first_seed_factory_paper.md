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
