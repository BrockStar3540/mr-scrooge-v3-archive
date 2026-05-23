"""MTB Sub-Regime Classifier — labels C01/C02 events into MTB_-prefixed sub-regimes.

Separate from V3's existing sub_regime_filter_gate which uses sub_regime_definitions_v1.csv
(40-leaf split for SKIP-tier filtering). This classifier uses mtb_sub_regime_definitions.csv
(10-leaf split, Phase 4 decomposition) with MTB_-prefixed IDs to avoid collision.

Output: ctx.classifications["mtb_sub_regime"] = label like "MTB_C01_3" or "MTB_C02_6" or
        "MTB_C01_unmatched" / "MTB_C02_unmatched" for events not covered by any rule, or
        None for events outside C01/C02 parent regimes.

Used by entry_filter_gate to match routing-table cells that have basis['sub_regime']
set (those cells were measured at sub-regime granularity, e.g. v1.11.5 MTB cells).

Feature access mirrors sub_regime_filter_gate's _FEATURE_MAP — same source-of-truth
plumbing.
"""
from __future__ import annotations

import csv
import logging
import re
from pathlib import Path

from scrooge_v3.core.types import ClassificationResult, SymbolContext

log = logging.getLogger("scrooge_v3.classifiers.mtb_sub_regime")

# Reuses sub_regime_filter_gate's _FEATURE_MAP semantics exactly.
_FEATURE_MAP: dict[str, tuple[str, str]] = {
    'ATR_ratio':    ('technical_regime_53', 'ATR_ratio'),
    'BB_compress':  ('technical_regime_53', 'BB_compress'),
    'ADX14':        ('technical_regime_53', 'ADX14'),
    'RSI14':        ('technical_regime_53', 'RSI14'),
    'bb_position':  ('bollinger',           'bb_position'),
    'volume_ratio': ('volume',              'volume_ratio'),
}

_RULE_RE = re.compile(r'^([\w_]+)\s*(<=|>=|<|>|==|=)\s*(.+?)\s*$')

DEFAULT_CSV_PATH = "data/mtb_sub_regime_definitions.csv"


class MTBSubRegimeClassifier:
    """Sub-regime classifier for Master Theory Box cells. NOT used for V3's SKIP-tier
    sub_regime_filter_gate (that gate has its own internal classification using
    sub_regime_definitions_v1.csv). This classifier is a separate, MTB-specific sub_regime
    map for entry_filter routing-table matching at sub-regime granularity."""

    name = "mtb_sub_regime"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.enabled = config.get("enabled", True)
        self.csv_path = Path(config.get("csv_path", DEFAULT_CSV_PATH))
        if not self.csv_path.is_absolute():
            self.csv_path = Path("/home/ubuntu/mr-scrooge-v3") / self.csv_path
        self._definitions = self._load_definitions(self.csv_path)
        n_rules = sum(len(v) for v in self._definitions.values())
        log.info("[CLASSIFIER:mtb_sub_regime] init enabled=%s rules=%d parents=%s",
                 self.enabled, n_rules, sorted(self._definitions.keys()))

    def classify(self, ctx: SymbolContext) -> ClassificationResult:
        if not self.enabled:
            return ClassificationResult(name=self.name, label=None, confidence=0.0,
                                        metadata={"detail": "classifier disabled"})

        parent = self._get_parent_regime(ctx)
        if parent is None:
            return ClassificationResult(name=self.name, label=None, confidence=0.0,
                                        metadata={"detail": "no parent regime"})

        # Only C01/C02 are decomposed; other parents return None
        if parent not in self._definitions:
            return ClassificationResult(name=self.name, label=None, confidence=0.0,
                                        metadata={"parent_regime": parent, "detail": "parent not decomposed"})

        snap = self._snapshot_features(ctx)
        sub_id = self._classify_sub_regime(parent, snap)
        if sub_id is None:
            label = f"MTB_{parent}_unmatched"
            return ClassificationResult(name=self.name, label=label, confidence=0.0,
                                        metadata={"parent_regime": parent, "snap": snap, "detail": "no_rule_matched"})

        return ClassificationResult(name=self.name, label=sub_id, confidence=1.0,
                                    metadata={"parent_regime": parent, "snap": snap})

    # ------------------------------------------------------------------
    # Helpers (mirror sub_regime_filter_gate logic)
    # ------------------------------------------------------------------

    def _load_definitions(self, p: Path) -> dict[str, list[tuple[str, list]]]:
        out: dict[str, list[tuple[str, list]]] = {}
        if not p.exists():
            log.warning("[CLASSIFIER:mtb_sub_regime] definitions not found: %s", p)
            return out
        with open(p) as f:
            for row in csv.DictReader(f):
                parent = row['parent_regime']
                sub_id = row['sub_regime']  # already MTB_-prefixed
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
