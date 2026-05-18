"""
EntryFilterGate -- per-cell shave-rule enforcement.

DRAFT — not yet wired into the gate pipeline. Reviewed by Brock 2026-05-15.

After RegimeStrategyRouterGate confirms a candidate's cell is allowed, this
gate looks up the matching RoutingDecision and, if the decision carries a
non-null shave_rule (from routing_table_v4+), parses the rule against the
current SymbolContext features. The rule is the per-cell entry filter the
shaver validated (e.g. ATR14>0.0005 AND RSI14<=70.6).

Live deployment plan:
  1. Routing table builder writes shave_rule per cell into the parquet.
  2. RoutingTable.load() stores it in RoutingDecision.basis['shave_rule'].
  3. This gate evaluates the rule against ctx.features and ctx.classifications.
  4. Mode = OBSERVE for first 24-48h to verify rule-firing rate is sane.
  5. Flip to HARD via config when telemetry looks clean.

Missing-feature policy:
  Default 'allow' (fail-open) -- if a rule needs a feature the live bot
  doesn't compute, allow the trade and log telemetry. Flip to 'veto' once
  the feature map is verified comprehensive.
"""

from __future__ import annotations

import re
import logging

log = logging.getLogger("scrooge_v3.gate.entry_filter")
from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate
from scrooge_v3.strategies.routing_table import RoutingTable

from .base import BaseGate


# Maps rule-grammar feature names (from the offline corpus / shaver) to the
# live bot's (ctx.features[FEAT].values[KEY]) access pattern.
# This is the ONLY place the offline/live name divergence is resolved.
#
# 2026-05-18 audit: ATR_ratio/BB_compress/ADX14/RSI14 were pointing at
# non-existent features (`atr`/`bollinger.bb_compress`/`adx`/`rsi.rsi`).
# Live values for these live on the technical_regime_53 feature with
# matching key names. Without this fix shave_rule clauses on those
# features fell through to `missing_feature:<name>` and (under the default
# `missing_policy: allow`) silently passed the candidate.
_FEATURE_MAP: dict[str, tuple[str, str]] = {
    'ATR_ratio':    ('technical_regime_53', 'ATR_ratio'),
    'BB_compress':  ('technical_regime_53', 'BB_compress'),
    'ADX14':        ('technical_regime_53', 'ADX14'),
    'RSI14':        ('technical_regime_53', 'RSI14'),
    'bb_position':  ('bollinger',           'bb_position'),
    'price_pos':    ('zone_detector',       'price_pos'),
    'volume_ratio': ('volume',              'volume_ratio'),
}

_RULE_RE = re.compile(r'^([\w_]+)\s*(<=|>=|<|>|==|=)\s*(.+?)\s*$')


class EntryFilterGate(BaseGate):
    name = 'entry_filter'

    def __init__(self, routing_table: RoutingTable,
                 config: dict[str, Any] | None = None,
                 mode: GateMode = GateMode.OBSERVE,
                 ledger: Any = None) -> None:
        super().__init__(config=config, mode=mode)
        self._table = routing_table
        self._ledger = ledger
        cfg = config or {}
        self._missing_policy = cfg.get('missing_policy', 'allow')
        # Tier-gating: only accept candidates whose cell tier >= min_tier
        # Tier order: Probationary < Standard < Pro < Elite
        # Tier hierarchy aligned with build_routing_table_v9.tier_for():
        #   Probationary  (weak)     < Seed (small-but-pure, unvalidated) <
        #   Standard      (broad, mid evidence) < Seed-Pro (small-but-very-pure) <
        #   Pro           (strong evidence) < Elite (very strong evidence)
        # Unknown tier names raise rather than silently return 0 — the
        # 2026-05-18 bleed pattern was a `min_tier="Pro"` with the gate
        # silently passing because nothing matched the rank map.
        self._tier_rank = {
            'Probationary': 0, 'Seed': 1, 'Standard': 2,
            'Seed-Pro': 3, 'Pro': 4, 'Elite': 5,
        }
        _raw_min = cfg.get('min_tier', 'Probationary')
        if _raw_min not in self._tier_rank:
            raise ValueError(
                f"min_tier={_raw_min!r} not in known tiers "
                f"{list(self._tier_rank)} — config typo? "
                "Default to 'Probationary' explicitly to disable tier-gating."
            )
        self._min_tier_rank = self._tier_rank[_raw_min]
        log.info('[ENTRY_FILTER] min_tier=%s (rank=%d)',
                 cfg.get('min_tier', 'Probationary'), self._min_tier_rank)

    def evaluate(self, candidate: TradeCandidate, ctx: SymbolContext) -> GateResult:
        regime53 = self._classify(ctx, 'technical_regime_53')
        session  = self._classify(ctx, 'session_bucket')
        if not regime53 or not session:
            # When tier-gating is active, we cannot verify the candidate is in a
            # qualifying cell — fail closed. Without min_tier we keep the original
            # observe-friendly pass.
            if self._min_tier_rank > 0:
                return self._veto('cell_key_unavailable_tier_gated',
                                  metrics={'regime53': regime53, 'session': session})
            return self._pass('cell_key_unavailable')

        decisions = self._table.lookup(
            regime53, ctx.symbol, session,
            direction=candidate.direction.value,
        )
        # Try exact strategy match first (offline replay strategy IDs).
        # Fall back to family match — the live bot's candidate.strategy is
        # the FAMILY name (dbb_trend/direct/reversal/trend), not the specific
        # strategy_id (echo_box_fade_v2, TF4_sar_long, etc.). Without this
        # fallback the gate pass-through-ed every candidate.
        # Among multiple family matches, prefer highest tier.
        match = next((d for d in decisions if d.strategy == candidate.strategy), None)
        if match is None:
            family_matches = [d for d in decisions if d.family == candidate.strategy]
            if family_matches:
                # Sort by tier (Elite > Pro > Standard > Probationary), then by score_boost
                family_matches.sort(
                    key=lambda d: (
                        self._tier_rank.get((d.basis or {}).get('tier', 'Probationary'), 0),
                        d.score_boost,
                    ),
                    reverse=True,
                )
                match = family_matches[0]
        if match is None:
            # No cell in the routing table covers this (regime, pair, session,
            # direction, family). Under tier-gating that means the candidate is
            # NOT in a qualifying tier — fail closed. Bug discovered 2026-05-18
            # after a Sunday-open bleed where the fail-open path bypassed
            # min_tier=Pro and let direct-counter trades fire.
            if self._min_tier_rank > 0:
                return self._veto('no_routing_match_for_strategy_tier_gated',
                                  metrics={'strategy': candidate.strategy,
                                           'direction': candidate.direction.value,
                                           'regime53': regime53,
                                           'session': session})
            return self._pass('no_routing_match_for_strategy')

        # Tier check: read tier from RoutingDecision.basis
        cell_tier = (match.basis or {}).get('tier', 'Probationary')
        cell_tier_rank = self._tier_rank.get(cell_tier, 0)
        if cell_tier_rank < self._min_tier_rank:
            return self._veto(f'below_min_tier:{cell_tier}_rank{cell_tier_rank}<{self._min_tier_rank}',
                              metrics={'cell_tier': cell_tier})
        rule = (match.basis or {}).get('shave_rule') or ''
        if not rule.strip():
            return self._pass('no_shave_rule_in_cell')

        try:
            clauses = self._parse_rule(rule)
        except Exception as exc:
            return self._pass(f'rule_parse_error:{exc}')

        snap = self._extract_features(ctx, [c[0] for c in clauses])
        verdict, reason = self._evaluate_clauses(clauses, snap)
        cell_label = f'{regime53}|{ctx.symbol}|{session}'

        if verdict is None:
            if self._missing_policy == 'veto':
                return self._veto(reason, metrics={'rule': rule, 'cell': cell_label})
            return self._pass(reason, metrics={'rule': rule, 'cell': cell_label, 'snapshot': snap})

        # carry the cell's strategy_id + family so downstream telemetry
        # can filter the corpus to the exact strategy this rule was fit on
        # (rather than the broader family). Required for sane offline
        # expansion -- see Brock 2026-05-18 telemetry diagnostic.
        cell_strategy = match.strategy
        cell_family = match.family
        if verdict:
            return self._pass('shave_rule_satisfied',
                              metrics={'rule': rule, 'cell': cell_label,
                                       'snapshot': snap,
                                       'cell_strategy': cell_strategy,
                                       'cell_family': cell_family,
                                       'cell_tier': cell_tier})
        return self._veto(f'shave_rule_violated: {reason}',
                          metrics={'rule': rule, 'cell': cell_label,
                                   'snapshot': snap,
                                   'cell_strategy': cell_strategy,
                                   'cell_family': cell_family,
                                   'cell_tier': cell_tier})

    # ---- helpers ---------------------------------------------------------

    def _classify(self, ctx: SymbolContext, key: str) -> str | None:
        # session_bucket lives in ctx.classifications; technical_regime_53
        # lives in ctx.features[...].values[key] (it is a feature in V3,
        # not a classifier). Try both.
        c = ctx.classifications.get(key)
        if c is not None:
            return c.label
        feat = ctx.features.get(key)
        if feat is None:
            return None
        vals = getattr(feat, "values", {}) or {}
        v = vals.get(key)
        return str(v) if v is not None else None

    def _parse_rule(self, rule: str) -> list[tuple[str, str, Any]]:
        out = []
        for raw in rule.split(' AND '):
            m = _RULE_RE.match(raw.strip())
            if not m:
                raise ValueError(f'bad clause: {raw!r}')
            feat, op, val = m.group(1), m.group(2), m.group(3)
            op = '==' if op == '=' else op
            if feat == 'session_bucket':
                out.append((feat, op, val))
            elif feat == 'hour_utc':
                out.append((feat, op, int(float(val))))
            else:
                out.append((feat, op, float(val)))
        return out

    def _extract_features(self, ctx: SymbolContext, names: list[str]) -> dict[str, Any]:
        snap: dict[str, Any] = {}
        for n in set(names):
            if n == 'hour_utc':
                # MarketSnapshot exposes `timestamp`, not `ts`. Same bug as
                # SubRegimeFilterGate — hour_utc shave clauses silently never
                # matched, falling through to `missing_feature:hour_utc`.
                ts = getattr(ctx.snapshot, 'timestamp', None)
                snap[n] = ts.hour if ts is not None else None
            elif n == 'session_bucket':
                snap[n] = self._classify(ctx, 'session_bucket')
            elif n in _FEATURE_MAP:
                feat_name, key = _FEATURE_MAP[n]
                feat = ctx.features.get(feat_name)
                snap[n] = feat.values.get(key) if feat else None
            else:
                snap[n] = None
        return snap

    def _evaluate_clauses(self, clauses, snap) -> tuple[bool | None, str]:
        for feat, op, val in clauses:
            v = snap.get(feat)
            if v is None:
                return None, f'missing_feature:{feat}'
            if isinstance(val, str):
                ok = (str(v) == val) if op == '==' else (str(v) != val)
            else:
                try:
                    vf = float(v)
                except (TypeError, ValueError):
                    return None, f'non_numeric_feature:{feat}={v!r}'
                if   op == '<=': ok = vf <= val
                elif op == '>=': ok = vf >= val
                elif op == '<':  ok = vf <  val
                elif op == '>':  ok = vf >  val
                elif op == '==': ok = vf == val
                else: ok = False
            if not ok:
                return False, f'{feat} {op} {val} (got {v})'
        return True, 'all_clauses_satisfied'

    def _pass(self, reason: str, metrics: dict | None = None) -> GateResult:
        return GateResult(gate_name=self.name, passed=True, mode=self.mode,
                          reason=reason, metrics=metrics or {})

    def _veto(self, reason: str, metrics: dict | None = None) -> GateResult:
        return GateResult(gate_name=self.name, passed=False, mode=self.mode,
                          reason=reason, metrics=metrics or {})

    # Brock 2026-05-18: write structured row per candidate so the offline
    # expansion pipeline can drive sibling/seed mining off live telemetry.
    def safe_evaluate(self, candidate, ctx):  # type: ignore[override]
        result = super().safe_evaluate(candidate, ctx)
        if self._ledger is not None:
            try:
                m = result.metrics or {}
                regime53 = m.get('regime53') or self._classify(ctx, 'technical_regime_53')
                session = m.get('session') or self._classify(ctx, 'session_bucket')
                self._ledger.record(
                    gate=self.name,
                    symbol=ctx.symbol,
                    regime53=regime53,
                    session_bucket=session,
                    direction=candidate.direction.value,
                    candidate_strategy=candidate.strategy,
                    block_reason=result.reason,
                    passed=bool(result.passed),
                    mode=result.mode.value if hasattr(result.mode, 'value') else str(result.mode),
                    cell_tier=m.get('cell_tier'),
                    cell_label=m.get('cell'),
                    cell_strategy=m.get('cell_strategy'),
                    cell_family=m.get('cell_family'),
                    shave_rule=m.get('rule'),
                    factors=m.get('snapshot'),
                )
            except Exception:
                log.exception("[%s] ledger write failed", self.name)
        return result
