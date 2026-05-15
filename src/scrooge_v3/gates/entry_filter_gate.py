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
from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate
from scrooge_v3.strategies.routing_table import RoutingTable

from .base import BaseGate


# Maps rule-grammar feature names (from the offline corpus / shaver) to the
# live bot's (ctx.features[FEAT].values[KEY]) access pattern.
# This is the ONLY place the offline/live name divergence is resolved.
_FEATURE_MAP: dict[str, tuple[str, str]] = {
    'ATR_ratio':    ('atr',          'atr_ratio'),
    'BB_compress':  ('bollinger',    'bb_compress'),
    'RSI14':        ('rsi',          'rsi'),
    'price_pos':    ('zone_detector','price_pos'),
    'volume_ratio': ('volume',       'volume_ratio'),
    'ADX14':        ('adx',          'adx14'),
}

_RULE_RE = re.compile(r'^([\w_]+)\s*(<=|>=|<|>|==|=)\s*(.+?)\s*$')


class EntryFilterGate(BaseGate):
    name = 'entry_filter'

    def __init__(self, routing_table: RoutingTable,
                 config: dict[str, Any] | None = None,
                 mode: GateMode = GateMode.OBSERVE) -> None:
        super().__init__(config=config, mode=mode)
        self._table = routing_table
        self._missing_policy = (config or {}).get('missing_policy', 'allow')

    def evaluate(self, candidate: TradeCandidate, ctx: SymbolContext) -> GateResult:
        regime53 = self._classify(ctx, 'technical_regime_53')
        session  = self._classify(ctx, 'session_bucket')
        if not regime53 or not session:
            return self._pass('cell_key_unavailable')

        decisions = self._table.lookup(
            regime53, ctx.symbol, session,
            direction=candidate.direction.value,
        )
        match = next((d for d in decisions if d.strategy == candidate.strategy), None)
        if match is None:
            return self._pass('no_routing_match_for_strategy')

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

        if verdict:
            return self._pass('shave_rule_satisfied',
                              metrics={'rule': rule, 'cell': cell_label, 'snapshot': snap})
        return self._veto(f'shave_rule_violated: {reason}',
                          metrics={'rule': rule, 'cell': cell_label, 'snapshot': snap})

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
                ts = getattr(ctx.snapshot, 'ts', None)
                snap[n] = ts.hour if ts else None
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
