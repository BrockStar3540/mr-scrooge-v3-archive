"""
SubRegimeFilterGate -- enforce SKIP tier on C01/C02 sub-regime micro-pockets.

The 53-regime classifier puts ~99.6% of trades in C01 + C02. A 40-leaf
decision tree on each splits them into sub-regimes with WR ranging
from 1.5% to 17%. The bottom 8 sub-regimes per parent (C01_q0-q7 and
C02_q0-q7) hold ~22% of all trade volume at 2-5% WR -- pure capital
destruction. This gate vetoes those.

Also vetoes the structurally dead 53-regime tail (T07 directional_drift_flat,
Z01 catch_all, R04 tight_range) where the parent classifier already flagged
zero edge.

Tier definitions (default):
  SKIP : bottom 8 of C01 + bottom 8 of C02 + dead rare regimes
  TAKE : everything else  (the gate is a one-sided veto, not a router)

Sub-regime classification is computed inline from ctx.features. Rule strings
come from data/sub_regime_definitions_v1.csv -- a tree leaf encoding of
(parent_regime + factor band conditions) -> sub_id.
"""
from __future__ import annotations

import csv
import logging
import re
from pathlib import Path
from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate

log = logging.getLogger('scrooge_v3.gate.sub_regime_filter')

# Live feature accessor map (rule grammar -> ctx.features path).
#
# The sub-regime rule corpus was built from features computed by
# TechnicalRegime53Calculator (atr14_M5 / d_atr20_avg semantics, etc.).
# Earlier this map pointed ATR_ratio/BB_compress/ADX14 at non-existent
# features (`atr`/`bb_compress`/`adx`) so 80%+ of sub-regime conditions
# never matched and the gate silently passed through with sub_regime_unmatched.
# 2026-05-18 diagnostic confirmed: snap had only RSI14/bb_position/volume_ratio.
_FEATURE_MAP: dict[str, tuple[str, str]] = {
    'ATR_ratio':    ('technical_regime_53', 'ATR_ratio'),
    'BB_compress':  ('technical_regime_53', 'BB_compress'),
    'ADX14':        ('technical_regime_53', 'ADX14'),
    'RSI14':        ('technical_regime_53', 'RSI14'),
    'bb_position':  ('bollinger',           'bb_position'),
    'volume_ratio': ('volume',              'volume_ratio'),
}

_RULE_RE = re.compile(r'^([\w_]+)\s*(<=|>=|<|>|==|=)\s*(.+?)\s*$')

# Default SKIP set: bottom 8 of each C-parent + structurally dead rare regimes
DEFAULT_SKIP_SUBS = {f'C01_{i}' for i in range(8)} | {f'C02_{i}' for i in range(8)}
DEFAULT_SKIP_RARE = {'T07', 'Z01', 'R04', 'X03', 'S01', 'S05'}


class SubRegimeFilterGate(BaseGate):
    name = 'sub_regime_filter'

    def __init__(self,
                 definitions_path: str | Path,
                 config: dict[str, Any] | None = None,
                 mode: GateMode = GateMode.OBSERVE) -> None:
        super().__init__(config=config, mode=mode)
        cfg = config or {}
        self._skip_subs: set[str] = set(cfg.get('skip_subs', DEFAULT_SKIP_SUBS))
        self._skip_rare: set[str] = set(cfg.get('skip_rare', DEFAULT_SKIP_RARE))
        self._definitions = self._load_definitions(Path(definitions_path))
        log.info('[SUB_REGIME_FILTER] loaded %d sub-regime rules; SKIP=%d sub + %d rare',
                 sum(len(v) for v in self._definitions.values()),
                 len(self._skip_subs), len(self._skip_rare))

    def _load_definitions(self, p: Path) -> dict[str, list[tuple[str, list]]]:
        """Parse CSV into {parent_regime: [(sub_regime_id, clauses), ...]}."""
        out: dict[str, list[tuple[str, list]]] = {}
        if not p.exists():
            log.warning('[SUB_REGIME_FILTER] definitions not found: %s', p)
            return out
        with open(p) as f:
            for row in csv.DictReader(f):
                parent = row['parent_regime']
                sub_id = row['sub_regime']
                clauses = self._parse_rule(row.get('rule', ''))
                out.setdefault(parent, []).append((sub_id, clauses))
        return out

    @staticmethod
    def _parse_rule(rule: str) -> list[tuple[str, str, float]]:
        out = []
        if not rule:
            return out
        for raw in rule.split(' AND '):
            m = _RULE_RE.match(raw.strip())
            if not m:
                continue
            feat, op, val = m.group(1), m.group(2), m.group(3)
            op = '==' if op == '=' else op
            try:
                out.append((feat, op, float(val)))
            except ValueError:
                continue
        return out

    def _get_parent_regime(self, ctx: SymbolContext) -> str | None:
        feat = ctx.features.get('technical_regime_53')
        if feat is None:
            return None
        vals = getattr(feat, 'values', {}) or {}
        v = vals.get('technical_regime_53')
        return str(v).upper() if v else None

    def _snapshot_features(self, ctx: SymbolContext) -> dict[str, float]:
        snap: dict[str, float] = {}
        for name, (feat_key, val_key) in _FEATURE_MAP.items():
            f = ctx.features.get(feat_key)
            if f is None:
                continue
            v = getattr(f, 'values', {}).get(val_key) if f else None
            if v is None:
                continue
            try:
                snap[name] = float(v)
            except (TypeError, ValueError):
                continue
        # MarketSnapshot exposes `timestamp`, not `ts`. The earlier `ts`
        # lookup always returned None and emitted hour_utc=nan, which broke
        # every C01/C02 rule that conditions on hour_utc (151 of 81 rules).
        ts = getattr(ctx.snapshot, 'timestamp', None)
        snap['hour_utc'] = float(ts.hour) if ts is not None else float('nan')
        return snap

    def _classify_sub_regime(self, parent: str, snap: dict[str, float]) -> str | None:
        rules = self._definitions.get(parent)
        if not rules:
            return None
        for sub_id, clauses in rules:
            ok = True
            for feat, op, thr in clauses:
                v = snap.get(feat)
                if v is None or v != v:  # NaN check
                    ok = False; break
                if   op == '<=': cond = v <= thr
                elif op == '>=': cond = v >= thr
                elif op == '<':  cond = v <  thr
                elif op == '>':  cond = v >  thr
                elif op == '==': cond = v == thr
                else: cond = False
                if not cond:
                    ok = False; break
            if ok:
                return sub_id
        return None

    def evaluate(self, candidate: TradeCandidate, ctx: SymbolContext) -> GateResult:
        parent = self._get_parent_regime(ctx)
        if not parent:
            return self._pass('parent_regime_unknown')

        # Skip dead rare regimes immediately
        if parent in self._skip_rare:
            return self._veto(f'dead_regime:{parent}', metrics={'parent': parent})

        # Non-C regimes: pass through (let other gates decide)
        if parent not in ('C01', 'C02'):
            return self._pass(f'non_c_parent:{parent}', metrics={'parent': parent})

        snap = self._snapshot_features(ctx)
        sub_id = self._classify_sub_regime(parent, snap)
        if sub_id is None:
            try:
                hour = int(snap.get('hour_utc', -1))
            except Exception:
                hour = -1
            key = (parent, hour)
            if not hasattr(self, '_unmatched_seen'):
                self._unmatched_seen = set()
            if key not in self._unmatched_seen:
                self._unmatched_seen.add(key)
                log.info('[SUB_REGIME_FILTER] unmatched diag parent=%s hour=%d snap=%s',
                         parent, hour,
                         {k: (round(v, 6) if isinstance(v, float) else v)
                          for k, v in snap.items()})
            return self._pass(f'sub_regime_unmatched:{parent}',
                              metrics={'parent': parent, 'snapshot': snap})

        if sub_id in self._skip_subs:
            return self._veto(f'sub_regime_skip:{sub_id}',
                              metrics={'parent': parent, 'sub_regime': sub_id, 'snapshot': snap})

        return self._pass(f'sub_regime_take:{sub_id}',
                          metrics={'parent': parent, 'sub_regime': sub_id})

    def _pass(self, reason: str, metrics: dict | None = None) -> GateResult:
        return GateResult(gate_name=self.name, passed=True, mode=self.mode,
                          reason=reason, metrics=metrics or {})

    def _veto(self, reason: str, metrics: dict | None = None) -> GateResult:
        return GateResult(gate_name=self.name, passed=False, mode=self.mode,
                          reason=reason, metrics=metrics or {})
