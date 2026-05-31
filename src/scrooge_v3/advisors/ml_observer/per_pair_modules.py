"""per_pair_modules.py — runtime loader for per-cohort currency module folders.

Each currency module (EUR_USD, GBP_USD, ...) lives under ONE of the cohort dirs:

    data/per_pair_modules/<PAIR>/          <- LEGACY cohort (V3-family strategies, R00-R19)
    data/per_pair_modules_phase3/<PAIR>/   <- PHASE 3 cohort (probes_v2 + textbook_scalper, R20-R39)

A cohort represents a corpus of trades fitted with its own KMeans regimes.
Regime IDs are namespaced per cohort (legacy=R00-R19, phase3=R20-R39, etc.)
so they never collide. At lookup-time we dispatch by (pair, strategy):
the strategy's parent cohort owns the routing decision.

Future Phase 4+ just drop a new per_pair_modules_phaseN/ dir and restart;
the loader auto-discovers it via COHORT_DIRS.

Public API:
    load_all()                                 — boot-time, idempotent
    get(pair, strategy="") -> Optional[PairModule]
                                              — module owning (pair, strategy);
                                                falls back to legacy if no match
    get_all(pair) -> list[PairModule]         — every cohort's module for a pair
                                                (used by ml_router which iterates
                                                ALL cohorts' rules to compute
                                                the allowed-strategies set)
    pairs() -> list[str]                      — union of pairs known to any cohort
    cohorts() -> list[str]                    — names of registered cohorts
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

# Ordered list of (cohort_name, dir_path). On strategy collisions (same strategy
# appears in multiple cohorts), the LATER cohort wins — so newer corpora override
# older ones. Add new phases at the END.
COHORT_DIRS: list[tuple[str, Path]] = [
    ("legacy", Path("/home/ubuntu/mr-scrooge-v3/data/per_pair_modules")),
    ("phase3", Path("/home/ubuntu/mr-scrooge-v3/data/per_pair_modules_phase3")),
]

REGIME_FACTORS = ["BB", "A5", "A1", "E20", "E50", "ADR", "SPR"]

log = logging.getLogger("scrooge_v3.ml_observer.per_pair_modules")


def _find_master_rules(pair_dir: Path) -> Optional[Path]:
    for p in [pair_dir / "master_rules.csv",
              pair_dir / "manuals" / "master_rules.csv"]:
        if p.exists():
            return p
    return None


def _discover_strategies(pair_dir: Path) -> set[str]:
    """Discover which strategies this cohort's corpus covers.

    Reads strategies.json (lightweight, shipped with the module) first;
    falls back to trade_serials.csv (the full corpus, used at build-time
    if strategies.json hasn't been precomputed)."""
    sj = pair_dir / "strategies.json"
    if sj.exists():
        try:
            data = json.loads(sj.read_text())
            return set(data.get("strategies", []))
        except Exception as e:
            log.warning("[PER_PAIR] %s: strategies.json parse failed: %s", pair_dir.name, e)
    # Fallback: scan trade_serials.csv
    ts = pair_dir / "trade_serials.csv"
    if not ts.exists():
        return set()
    try:
        ser = pd.read_csv(ts, usecols=["strategy_id"], low_memory=False)
        return set(ser["strategy_id"].dropna().astype(str).unique())
    except Exception as e:
        log.warning("[PER_PAIR] %s: trade_serials read failed: %s", pair_dir.name, e)
        return set()


@dataclass
class PairModule:
    pair: str
    cohort: str                               # which cohort dir this came from
    rules: pd.DataFrame                       # master_rules.csv contents
    centroids: pd.DataFrame                   # 20 regime centroids (mode buckets)
    centroid_vectors: np.ndarray              # one-hot encoded centroids
    centroid_columns: list[str]               # columns used for encoding
    strategies: set[str] = field(default_factory=set)
                                              # strategies this cohort's corpus covers

    @classmethod
    def load(cls, pair_dir: Path, cohort: str) -> Optional["PairModule"]:
        pair = pair_dir.name
        rules_path = _find_master_rules(pair_dir)
        cent_path = pair_dir / "regime_centroids.csv"
        if not rules_path or not cent_path.exists():
            log.warning("[PER_PAIR:%s] %s: missing rules or centroids, skipping",
                        cohort, pair)
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
        strategies = _discover_strategies(pair_dir)
        return cls(
            pair=pair, cohort=cohort, rules=rules, centroids=cent,
            centroid_vectors=cent_vec.values,
            centroid_columns=cent_vec.columns.tolist(),
            strategies=strategies,
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
                if cand.get(ref_ax) == ref_b:
                    continue
            elif ref_op == "include" and ref_ax and ref_b:
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
                "cohort": self.cohort,
                "regime": regime,
            }
            if hit["rule_type"] == "WIN":
                win_hits.append(hit)
            elif hit["rule_type"] == "LOSE":
                lose_hits.append(hit)
        return {"win_rules": win_hits, "lose_rules": lose_hits}


# ---------------------------------------------------------------------------
# Registry — singletons at module level
# ---------------------------------------------------------------------------

# Per-cohort: cohort_name -> {pair: PairModule}
_MODULES_BY_COHORT: dict[str, dict[str, PairModule]] = {}

# Lookup by (pair, strategy) -> PairModule (later cohort wins on collision)
_STRATEGY_INDEX: dict[tuple[str, str], PairModule] = {}

# Loaded flag — load_all() is idempotent
_LOADED = False


def load_all() -> None:
    """Discover and load every cohort dir listed in COHORT_DIRS. Idempotent."""
    global _LOADED
    if _LOADED:
        return
    for cohort_name, src_dir in COHORT_DIRS:
        if not src_dir.exists():
            log.warning("[PER_PAIR] cohort=%s dir missing: %s (skipping)",
                        cohort_name, src_dir)
            continue
        _MODULES_BY_COHORT[cohort_name] = {}
        for pair_dir in sorted(p for p in src_dir.iterdir() if p.is_dir()):
            m = PairModule.load(pair_dir, cohort_name)
            if m is None:
                continue
            _MODULES_BY_COHORT[cohort_name][m.pair] = m
            # Index every (pair, strategy) tuple this module covers
            for strat in m.strategies:
                key = (m.pair, strat)
                if key in _STRATEGY_INDEX:
                    prev = _STRATEGY_INDEX[key]
                    log.warning(
                        "[PER_PAIR] strategy collision %s/%s: previously cohort=%s, "
                        "now cohort=%s — later wins", m.pair, strat, prev.cohort, cohort_name)
                _STRATEGY_INDEX[key] = m
        log.info("[PER_PAIR] cohort=%s loaded %d pair modules: %s",
                 cohort_name, len(_MODULES_BY_COHORT[cohort_name]),
                 ", ".join(sorted(_MODULES_BY_COHORT[cohort_name].keys())))
        # Per-cohort rule + strategy audit
        for p in sorted(_MODULES_BY_COHORT[cohort_name]):
            m = _MODULES_BY_COHORT[cohort_name][p]
            n_wins = (m.rules["rule_type"] == "WIN").sum()
            n_loses = (m.rules["rule_type"] == "LOSE").sum()
            log.info("[PER_PAIR:%s]   %s: %d WIN rules, %d LOSE rules, %d centroids, %d strategies",
                     cohort_name, p, n_wins, n_loses, len(m.centroids), len(m.strategies))
    _LOADED = True
    # Final summary
    all_pairs = set()
    for mods in _MODULES_BY_COHORT.values():
        all_pairs.update(mods.keys())
    log.info("[PER_PAIR] UNION: %d pairs × %d cohorts -> %d (pair,strategy) routes",
             len(all_pairs), len(_MODULES_BY_COHORT), len(_STRATEGY_INDEX))


def get(pair: str, strategy: str = "") -> Optional[PairModule]:
    """Return the module owning (pair, strategy).

    Dispatch: (pair, strategy) → cohort that has that strategy in its corpus.
    If strategy is empty/unknown, falls back to the LEGACY cohort by pair
    (preserves backwards-compat for callers that haven't yet wired in strategy).
    """
    if not _LOADED:
        load_all()
    if strategy:
        m = _STRATEGY_INDEX.get((pair, strategy))
        if m is not None:
            return m
    return _MODULES_BY_COHORT.get("legacy", {}).get(pair)


def get_all(pair: str) -> list[PairModule]:
    """Return every cohort's module for this pair.

    Used by ml_router which iterates ALL cohorts' rule tables to compute the
    full allowed-strategy set for a candidate state.
    """
    if not _LOADED:
        load_all()
    out: list[PairModule] = []
    for _cohort, mods in _MODULES_BY_COHORT.items():
        m = mods.get(pair)
        if m is not None:
            out.append(m)
    return out


def pairs() -> list[str]:
    """Union of pairs known to any cohort."""
    if not _LOADED:
        load_all()
    all_pairs: set[str] = set()
    for mods in _MODULES_BY_COHORT.values():
        all_pairs.update(mods.keys())
    return sorted(all_pairs)


def cohorts() -> list[str]:
    """Names of cohorts that loaded successfully."""
    if not _LOADED:
        load_all()
    return list(_MODULES_BY_COHORT.keys())
