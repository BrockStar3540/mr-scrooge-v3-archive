# 3001. Regime-aware, not global score

**Status:** Accepted
**Date:** 2026-04-15 (approximate; V3 architecture shipped around this date)
**Version scope:** V3
**Author:** Brock (decision) / research arc (evidence)

## Context

V1 and V2 used a single global scorer: one set of factor weights applied uniformly across all market conditions. Live performance was poor:
- V1 ended at −$993 across 504 trades (44% WR)
- V2 was decommissioned before V1
- V3 inherited the global-score architecture and bled similarly (~−$36k across the 90-day window covered by the live audit)

The 47-factor replay audit and manual tradebook work surfaced the disqualifying problem:

**14 factors flip sign by regime, 15 flip sign by strategy.**

In Echo (BB-rail) tape, wall_proximity is a positive winner factor. In Alpha (trending), wall_proximity is approximately noise. In Charlie (low-vol-trend), it inverts. The manual tradebook also surfaced that Echo × E1 (the only well-powered cluster at the time) had a distinctive factor signature — `wall_proximity↑, regime_confidence↓, ema50_dist_pct↑` — that no global score could fit without contradiction.

A single set of weights forces one number per factor across all regimes. The evidence said that's structurally impossible.

## Decision

**All scoring, strategy selection, factor analysis, and management work in V3 is conditional on regime.** Specifically:

1. The regime classifier is a first-class component, not a feature among many. Its output gates downstream work.
2. Probe / playbook design is per-regime — entry conditions, exits, factor signatures all live inside a `(regime, probe)` cell, not in a global model.
3. No global-rewrite scorer experiments. The existing V3 scorer stays as-is; replacement is regime-aware routing, not better weights.
4. Per-strategy ML experiments are allowed (e.g., the dbb_trend XGBoost filter live since 2026-04-28) but only as **satellite** filters inside an already-regime-gated decision, never as the primary scoring mechanism.

## Alternatives considered

1. **Continue with global score, tune weights.** Rejected — sign flips kill any single-weight model. No amount of optimization fixes a factor whose true sign depends on regime.
2. **Train per-strategy models (one XGBoost per strategy family).** Partially adopted as a satellite layer (dbb_trend AUC 0.774, kept). Rejected as the primary axis because per-strategy slicing leaves regime variance unexplained — direct strategy fires across all 7 v2 regimes with very different outcomes per regime.
3. **Branched scorer (per-family weight set).** Explored deeply in Oanda-Bot-Trainer; produced research deliverables. Paused 2026-04 as a research direction. Closer to right than global score, but regime is the cleaner first-class axis — branched-scorer mixes regime and strategy in one layer, which is harder to reason about.
4. **Train per-pair models.** Rejected — pair-class differences are second-order to regime differences. JPY-cross vs USD-cross matters less than Alpha vs Echo.
5. **Hand-rule filter from the Factor Bible.** Approximately what got adopted, but at the *probe* level (deterministic per-regime probes), not as a global filter. The Factor Bible's insights got encoded into v1/v2 probe definitions rather than a single hand-rule pre-filter.

## Consequences

**Enabled:**
- Per-regime probe libraries with explicit lineage (the v1 and v2 probe arcs).
- Sub-state regime splits (v2 added Alpha-fresh/Alpha-extended and Echo-tight/Echo-explosive on 2026-05-09) — a natural extension of the regime-first principle.
- Live broker forensic audit (2026-05-10) could ask "what regime was this trade in?" as a first-class question, not derive it from features.
- Charlie reintroduction (2026-05-10) — once regime is first-class, "Charlie has no winning playbook in V3 yet" became a falsifiable claim with a clear test, not a guess.

**Closed:**
- No more "global score with better weights" proposals (constraint 3 in scrooge-frozen-constraints).
- No global-rewrite scorer prototype work in production (constraint 2).
- Any future ML proposal must operate inside a regime gate to be considered.

**Costs:**
- Regime classifier becomes a single point of failure. When the v2 Echo discriminator had a methodology bug (timeframe mismatch caught by spread-check, see postmortem 2026-05-08), it stalled the v2 corpus by 5 hours. A global-score architecture wouldn't have had that failure mode.
- Probe library proliferates — 10 active probes in v2 vs. 4 strategies in the original V3 design. More to maintain, more to audit per-cell.

## Cross-references

**Vault:**
- `wiki/systems/scrooge-frozen-constraints.md` — constraints 2, 3, 4, 5 (Charlie SKIP, later superseded)
- `wiki/systems/scrooge-strategy-regime-playbook-matrix.md` — v0.1 and v0.2 matrices
- `wiki/systems/v2-post-audit-state-2026-05-10.md`
- `wiki/systems/scrooge-research-regime-classifier-2026-05-05.md`

**Code:**
- `src/scrooge_v3/classifiers/regime.py` — production V3 regime classifier
- `Oanda-Bot-Trainer/scripts/regime_classifier.py` — frozen trainer-side classifier
- `Oanda-Bot-Trainer/data/replay/v2/audits/regime/regime_classifier_thresholds.json` — frozen v1 thresholds
- `Oanda-Bot-Trainer/data/replay/v3_full_corpus/v2/regime_v2_thresholds.json` — frozen v2 sub-state thresholds

**Evidence:**
- 47-factor replay audit (2026-05-04, `scrooge-research-47-factor-replay-audit-2026-05-04.md`)
- Manual tradebook + Echo × E1 winner pattern (`scrooge-research-playbook-replay-test-2026-05-05.md`)
- Live broker forensic audit (`Oanda-Bot-Trainer/data/replay/v2/audits/live_broker_reverse_engineering_v2.csv`)

**Related ADRs (to be written):**
- 3002 — TBD: branched scorer research paused
- 3003 — TBD: ML observer as satellite filter, not primary
- 3004 — TBD: V1 → V2 probe library refinement with lineage discipline
- 3005 — TBD: Multi-target walker (single-walk, multiple R-targets)
- 3006 — TBD: Live broker forensic audit reframing (tick-alignment → window search)
