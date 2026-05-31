"""per_pair_modules.py — runtime loader for the 28 currency module folders.

Each currency module (EUR_USD, GBP_USD, ...) lives at:
    data/per_pair_modules/<PAIR>/
        master_rules.csv (in manuals/master_rules.csv per the lab build)
        regime_centroids.csv
        lib/factor_buckets.py

This module discovers them on boot, loads each pair's rules and KMeans
centroids, and exposes a clean API for the rest of the ML observer:

    PairModule.assign_regime(buckets_dict) -> "R##"
    PairModule.match_rules(regime, session, buckets, strategy, direction)
        -> {"win_rules": [...], "lose_rules": [...]}

The matched rule list is what the rest of the ML observer (and later the bot
gate) consume to make pass/block decisions.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

MODULES_DIR = Path("/home/ubuntu/mr-scrooge-v3/data/per_pair_modules")
REGIME_FACTORS = ["BB", "A5", "A1", "E20", "E50", "ADR", "SPR"]

log = logging.getLogger("scrooge_v3.ml_observer.per_pair_modules")


def _find_master_rules(pair_dir: Path) -> Optional[Path]:
    for p in [pair_dir / "master_rules.csv",
              pair_dir / "manuals" / "master_rules.csv"]:
        if p.exists():
            return p
    return None


@dataclass
class PairModule:
    pair: str
    rules: pd.DataFrame                       # master_rules.csv contents
    centroids: pd.DataFrame                   # 20 regime centroids (mode buckets)
    centroid_vectors: np.ndarray              # one-hot encoded centroids
    centroid_columns: list[str]               # columns used for encoding

    @classmethod
    def load(cls, pair_dir: Path) -> Optional["PairModule"]:
        pair = pair_dir.name
        rules_path = _find_master_rules(pair_dir)
        cent_path = pair_dir / "regime_centroids.csv"
        if not rules_path or not cent_path.exists():
            log.warning("[PER_PAIR] %s: missing rules or centroids, skipping", pair)
            return None
        try:
            rules = pd.read_csv(rules_path)
        except pd.errors.EmptyDataError:
            rules = pd.DataFrame(columns=[
                "pair","regime","rule_type","raw_rule","raw_n","raw_w","raw_l","raw_wr",
                "refine_axis","refine_bucket","refine_op",
                "refined_n","refined_w","refined_l","refined_wr","plain_english",
            ])
        cent = pd.read_csv(cent_path)
        # One-hot encode the regime factor mode-buckets so we can assign by
        # nearest centroid using simple Hamming distance.
        cent_factors = cent[REGIME_FACTORS].copy()
        cent_vec = pd.get_dummies(cent_factors, prefix=REGIME_FACTORS).astype(float)
        return cls(
            pair=pair, rules=rules, centroids=cent,
            centroid_vectors=cent_vec.values,
            centroid_columns=cent_vec.columns.tolist(),
        )

    # ----------------------------------------------------------------
    # Regime assignment — given a candidate's 14 buckets, nearest centroid
    # ----------------------------------------------------------------
    def assign_regime(self, buckets: dict[str, str]) -> str:
        # Build a one-hot vector in the centroid's column-space
        vec = np.zeros(len(self.centroid_columns), dtype=float)
        for f in REGIME_FACTORS:
            col = f"{f}_{buckets.get(f, '')}"
            if col in self.centroid_columns:
                vec[self.centroid_columns.index(col)] = 1.0
        # Hamming-like distance: sum of squared differences (works for one-hot)
        dists = ((self.centroid_vectors - vec) ** 2).sum(axis=1)
        idx = int(np.argmin(dists))
        return self.centroids.iloc[idx]["regime"]

    # ----------------------------------------------------------------
    # Rule matching — find every rule whose conditions are satisfied
    # ----------------------------------------------------------------
    def match_rules(self, regime: str, session: str, buckets: dict[str, str],
                    strategy: str, direction: str) -> dict[str, list[dict]]:
        # Filter to this regime's rules
        sub = self.rules[self.rules["regime"] == regime]
        if sub.empty:
            return {"win_rules": [], "lose_rules": []}

        # Build the candidate's full condition map used by rules
        cand: dict[str, str] = dict(buckets)
        cand["session_bucket"] = session or ""
        cand["strategy_id"] = strategy or ""
        cand["direction_exec"] = direction or ""

        win_hits, lose_hits = [], []
        for _, r in sub.iterrows():
            raw_rule = str(r.get("raw_rule", "") or "")
            if not raw_rule:
                continue
            # Parse "AX=VX AND AY=VY"
            conditions = [c.strip() for c in raw_rule.split("AND") if "=" in c]
            ok = True
            for c in conditions:
                ax, _, bv = c.partition("=")
                ax, bv = ax.strip(), bv.strip()
                if cand.get(ax) != bv:
                    ok = False
                    break
            if not ok:
                continue
            # Optional refinement
            ref_op = str(r.get("refine_op", "") or "")
            ref_ax = str(r.get("refine_axis", "") or "")
            ref_b = str(r.get("refine_bucket", "") or "")
            if ref_op == "exclude" and ref_ax and ref_b:
                # Rule was 'WIN with this exclusion' — candidate must NOT have ref_b
                if cand.get(ref_ax) == ref_b:
                    continue
            elif ref_op == "include" and ref_ax and ref_b:
                # Rule was 'LOSE sharpened to this single bucket' — candidate
                # must HAVE ref_b for the loss-veto to apply.
                if cand.get(ref_ax) != ref_b:
                    continue

            hit = {
                "rule_type": str(r.get("rule_type", "")),
                "raw_rule": raw_rule,
                "refine_op": ref_op, "refine_axis": ref_ax, "refine_bucket": ref_b,
                "lab_n": int(r.get("refined_n", 0) or 0),
                "lab_w": int(r.get("refined_w", 0) or 0),
                "lab_l": int(r.get("refined_l", 0) or 0),
                "lab_wr": float(r.get("refined_wr", 0.0) or 0.0),
                "plain_english": str(r.get("plain_english", "") or ""),
            }
            if hit["rule_type"] == "WIN":
                win_hits.append(hit)
            elif hit["rule_type"] == "LOSE":
                lose_hits.append(hit)
        return {"win_rules": win_hits, "lose_rules": lose_hits}


# ---------------------------------------------------------------------------
# Registry — singleton at module level
# ---------------------------------------------------------------------------
_MODULES: dict[str, PairModule] = {}
_LOADED = False


def load_all() -> dict[str, PairModule]:
    global _LOADED, _MODULES
    if _LOADED:
        return _MODULES
    if not MODULES_DIR.exists():
        log.error("[PER_PAIR] modules dir does not exist: %s", MODULES_DIR)
        _LOADED = True
        return _MODULES
    for pair_dir in sorted(p for p in MODULES_DIR.iterdir() if p.is_dir()):
        m = PairModule.load(pair_dir)
        if m:
            _MODULES[m.pair] = m
    _LOADED = True
    log.info(
        "[PER_PAIR] loaded %d pair modules: %s",
        len(_MODULES),
        ", ".join(sorted(_MODULES.keys())),
    )
    # Quick rule-count audit
    for p in sorted(_MODULES):
        m = _MODULES[p]
        n_wins = (m.rules["rule_type"] == "WIN").sum()
        n_loses = (m.rules["rule_type"] == "LOSE").sum()
        log.info("[PER_PAIR]   %s: %d WIN rules, %d LOSE rules, %d centroids",
                 p, n_wins, n_loses, len(m.centroids))
    return _MODULES


def get(pair: str) -> Optional[PairModule]:
    if not _LOADED:
        load_all()
    return _MODULES.get(pair)


def pairs() -> list[str]:
    if not _LOADED:
        load_all()
    return sorted(_MODULES.keys())
