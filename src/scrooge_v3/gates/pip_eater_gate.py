"""pip_eater_gate.py v2 — DUAL-SOURCE pip-EV gate.

Mode C (max) blend: takes the more optimistic signal from either pair-module
baseline OR matrix-refined cell. Per Brock 2026-05-31: each source has cells
the other lacks, missing real harvests is worse than disagreement noise.

Lookups:
    pair_lookup:   (pair, strategy, direction, session, regime) -> mean_pip
    matrix_lookup: (pair, strategy, direction, session)         -> exp_optimized_pips

Tiers (floor=4.0p configurable):
    < 0          -> pip_trick    BLOCK
    0 to 4.0     -> empty_plate  BLOCK
    4.0 to 10.0  -> good_plate   PASS
    10.0 to 20.0 -> tasty        PASS
    >= 20.0      -> optimized_meal PASS
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Any, Optional

import pandas as pd

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate
from .base import BaseGate

ML_OBSERVER_DIR = Path("/home/ubuntu/mr-scrooge-v3/src/scrooge_v3/advisors/ml_observer")
if str(ML_OBSERVER_DIR) not in sys.path:
    sys.path.insert(0, str(ML_OBSERVER_DIR))
import per_pair_modules as ppm  # type: ignore  # noqa: E402

FACTOR_BUCKETS_PATH = Path("/home/ubuntu/mr-scrooge-v3/data/per_pair_modules/EUR_USD/lib")
if str(FACTOR_BUCKETS_PATH) not in sys.path:
    sys.path.insert(0, str(FACTOR_BUCKETS_PATH))
import factor_buckets as fb  # type: ignore  # noqa: E402

PAIR_LOOKUP_CSV = Path("/home/ubuntu/mr-scrooge-v3/data/pip_meal_lookup.csv")
MATRIX_LOOKUP_CSV = Path("/home/ubuntu/mr-scrooge-v3/data/matrix_meal_lookup.csv")
# Brock 2026-06-07: 8yr Play Book EV table (NEW single source for the EV check).
# Keyed on the live edge axis (strategy, align[, amplifier bucket]) from
# "Brock's Bot Strategy Book.xlsx -> Per Strategy Play Book". Two tiers:
# tier=amp -> (strategy, align, candidate's bucket in that strategy's amplifier
# factor); tier=spine -> (strategy, align) unconditional fallback.
PLAYBOOK_CSV = Path("/home/ubuntu/mr-scrooge-v3/data/playbook_ev.csv")


def _tag(exp_pips: float, floor: float = 4.0) -> str:
    if exp_pips < 0:        return "pip_trick"
    if exp_pips < floor:    return "empty_plate"
    if exp_pips < 10.0:     return "good_plate"
    if exp_pips < 20.0:     return "tasty"
    return "optimized_meal"


def _normalize_direction(d: Any) -> str:
    s = str(d).lower().replace("tradedirection.", "").strip()
    return "long" if s.startswith("l") else "short" if s.startswith("s") else s


class PipEaterGate(BaseGate):
    """Dual-source pip-EV gate. Mode C (max) blend of pair-module + matrix."""

    name = "pip_eater"

    def __init__(self, config: dict[str, Any] | None = None,
                 mode: GateMode = GateMode.HARD) -> None:
        super().__init__(config or {}, mode)
        self.floor_pips = float(self.config.get("floor_pips", 4.0))
        self.min_n = int(self.config.get("min_n", 30))
        # Brock 2026-06-02: momentum filter. Require align_score (# of H20/H60/
        # T1/T4 aligned with candidate direction) >= align_min. Lab: aligned>=3
        # trades net +0.64p/64% WR vs counter<=1 at -0.30p/59%. 0 = disabled.
        self.align_min = int(self.config.get("align_min", 0))
        # Brock 2026-06-03: per-pair strategy blocklist. strategy_id -> [pairs]
        # where that strategy is a net loser in lab (hard veto, any mode).
        _bl = self.config.get("pair_blocklist", {}) or {}
        self.pair_blocklist = {str(k): set(v or []) for k, v in _bl.items()}
        # Brock 2026-06-07: per-pair align floor + ADR amplifier gate (8yr book).
        self.align_floor_by_pair = {
            str(k): int(v) for k, v in (self.config.get("align_floor_by_pair", {}) or {}).items()
        }
        self.require_adr_min = int(self.config.get("require_adr_min", 0))
        self.adr_exempt_strategies = set(self.config.get("adr_exempt_strategies", []) or [])
        self.blend_mode = str(self.config.get("blend_mode", "max")).lower()  # max | min | avg
        self._pair_lookup: dict[tuple, dict] = {}
        self._coarse_pair_lookup: dict[tuple, dict] = {}  # regime-agnostic fallback
        self._matrix_lookup: dict[tuple, dict] = {}
        # Brock 2026-06-07: 8yr Play Book EV. strategy -> {amp_factor, floor,
        # amp:{(align,bucket):ev}, spine:{align:ev}}. Drives the EV check.
        self._playbook: dict[str, dict] = {}
        self._known_strategies: set[str] = set()  # any strategy present in lab data
        self._missing_logged: set[tuple] = set()
        self._load()

    def _load(self) -> None:
        # Pair-module baseline lookup
        if PAIR_LOOKUP_CSV.exists():
            df = pd.read_csv(PAIR_LOOKUP_CSV)
            full = df.copy()  # unfiltered, for the regime-agnostic aggregate
            df = df[df["n"] >= self.min_n].copy()
            self._pair_lookup = {
                (r["pair"], r["strategy_id"], r["direction_exec"],
                 r["session_bucket"], r["regime_id"]): {
                    "n": int(r["n"]), "mean_pip": float(r["mean_pip"]),
                    "wr": float(r["wr"]), "cohort": str(r["cohort"]),
                }
                for _, r in df.iterrows()
            }
            # Regime-agnostic fallback (Brock 2026-06-01): when neither the
            # regime-specific pair cell NOR the matrix cell exists, collapse the
            # pair-module across ALL regimes (sample-weighted) so we trade on the
            # broader average instead of rejecting. Built from the UNFILTERED rows
            # (thin regime cells combine) but kept only if the combined n>=min_n.
            try:
                full["_wp"] = full["n"] * full["mean_pip"]
                grp = full.groupby(
                    ["pair", "strategy_id", "direction_exec", "session_bucket"],
                    as_index=False,
                ).agg(n=("n", "sum"), _wp=("_wp", "sum"),
                      cohort=("cohort", "first"))
                grp = grp[grp["n"] >= self.min_n]
                self._coarse_pair_lookup = {
                    (r["pair"], r["strategy_id"], r["direction_exec"],
                     r["session_bucket"]): {
                        "n": int(r["n"]),
                        "mean_pip": float(r["_wp"] / r["n"]) if r["n"] else 0.0,
                        "cohort": str(r["cohort"]),
                    }
                    for _, r in grp.iterrows()
                }
                self._known_strategies.update(full["strategy_id"].astype(str).unique())
            except Exception as e:
                self._log.warning("[PIP_EATER] coarse fallback build failed: %s", e)
        # Matrix-refined lookup
        if MATRIX_LOOKUP_CSV.exists():
            mf = pd.read_csv(MATRIX_LOOKUP_CSV)
            self._matrix_lookup = {
                (r["pair"], r["strategy"], r["direction"], r["session"]): {
                    "n_optimized": int(r["n_optimized"]),
                    "exp_optimized_pips": float(r["exp_optimized_pips"]),
                    "exp_baseline_pips": float(r["exp_baseline_pips"]),
                    "lift_pips": float(r["lift_pips"]),
                    "factor_count": int(r.get("factor_count", 0)) if pd.notna(r.get("factor_count")) else 0,
                }
                for _, r in mf.iterrows()
            }
            self._known_strategies.update(mf["strategy"].astype(str).unique())
        pair_n = len(self._pair_lookup)
        mat_n = len(self._matrix_lookup)
        self._log.info(
            "[PIP_EATER] loaded %d pair cells + %d matrix cells + %d coarse(regime-agnostic) cells. Floor=%.1fp blend=%s",
            pair_n, mat_n, len(self._coarse_pair_lookup), self.floor_pips, self.blend_mode,
        )
        # Brock 2026-06-07: load the 8yr Play Book EV table. When present it is
        # the SINGLE source for the EV check (the (pair,session) matrix/pair
        # lookups above stay loaded but no longer drive decisions). The Play Book
        # strategy set also becomes the "covered" set for uncovered_bypass.
        if PLAYBOOK_CSV.exists():
            try:
                pbdf = pd.read_csv(PLAYBOOK_CSV)
                book: dict[str, dict] = {}
                for s, g in pbdf.groupby("strategy"):
                    amp: dict[tuple, float] = {}
                    spine: dict[int, float] = {}
                    for r in g.itertuples():
                        if str(r.tier) == "amp":
                            # min_n guard (parity with the old pair-lookup): thin
                            # amp cells (e.g. n=1 -> 18.5p noise) are dropped so
                            # the candidate falls back to the large-n spine.
                            if int(r.n) >= self.min_n:
                                amp[(int(r.align), str(r.bucket))] = float(r.ev_pips)
                        else:
                            spine[int(r.align)] = float(r.ev_pips)
                    book[str(s)] = {
                        "amp_factor": str(g["amp_factor"].iloc[0]),
                        "floor": int(g["floor"].iloc[0]),
                        "amp": amp, "spine": spine,
                    }
                if book:
                    self._playbook = book
                    # 8yr book defines the covered universe for uncovered_bypass.
                    self._known_strategies = set(book.keys())
                self._log.info(
                    "[PIP_EATER] loaded Play Book EV: %d strategies, %d amp cells, %d spine cells",
                    len(self._playbook),
                    sum(len(v["amp"]) for v in self._playbook.values()),
                    sum(len(v["spine"]) for v in self._playbook.values()),
                )
            except Exception as e:
                self._log.warning("[PIP_EATER] Play Book load failed (%s) — EV check disabled", e)
        else:
            self._log.warning("[PIP_EATER] Play Book CSV missing at %s — EV check has no source", PLAYBOOK_CSV)

    def _compute_buckets(self, candidate: TradeCandidate, ctx: SymbolContext) -> dict[str, str]:
        # Brock 2026-06-02 FIX: the old `ctx.features_dict()` never existed
        # (hasattr False -> feat={}), so ALL 14 factor buckets came back "x" and
        # regime/alignment ran on empty. The real features live in
        # ctx.features[<calc>].values (matrix_features/atr/bollinger/ema/rsi).
        # Merge them so the buckets compute on real data.
        feat = {}
        try:
            for _fr in (getattr(ctx, "features", {}) or {}).values():
                _v = getattr(_fr, "values", None)
                if isinstance(_v, dict):
                    feat.update(_v)
        except Exception:
            pass
        # direction is required by the alignment-aware buckets (H20/H60/T1/T4)
        try:
            feat["direction"] = candidate.direction.value
            feat["direction_exec"] = candidate.direction.value
        except Exception:
            pass
        pip_size = 0.01 if any(j in candidate.symbol for j in ("JPY", "MXN")) else 0.0001
        try:
            stop_pips = abs(candidate.entry_price - candidate.stop_price)
            feat["stop_pips"] = stop_pips / pip_size if pip_size else 0.0
        except Exception:
            feat["stop_pips"] = 7.0
        # SPR factor needs spread in pips; it lives on the snapshot, not a feature calc.
        try:
            if "spread_pips" not in feat:
                _sp = getattr(getattr(ctx, "snapshot", None), "spread", 0.0) or 0.0
                if _sp and pip_size:
                    feat["spread_pips"] = _sp / pip_size
        except Exception:
            pass
        row = {**feat, "pair": candidate.symbol}
        out = {}
        for f in fb.FACTORS:
            try:
                out[f.code] = f.bucket_for(row, {})
            except Exception:
                out[f.code] = f"{f.code}x"
        return out

    def _get_session(self, ctx: SymbolContext) -> str:
        cls = getattr(ctx, "classifications", {}) or {}
        sb = cls.get("session_bucket")
        return getattr(sb, "label", "") if sb else ""

    def _blend(self, pair_ev: Optional[float], matrix_ev: Optional[float]) -> Optional[float]:
        if pair_ev is None and matrix_ev is None:
            return None
        if pair_ev is None:
            return matrix_ev
        if matrix_ev is None:
            return pair_ev
        if self.blend_mode == "max":
            return max(pair_ev, matrix_ev)
        if self.blend_mode == "min":
            return min(pair_ev, matrix_ev)
        return (pair_ev + matrix_ev) / 2.0  # avg

    def evaluate(self, candidate: TradeCandidate, ctx: SymbolContext) -> GateResult:
        try:
            pair = candidate.symbol
            strategy = candidate.strategy or ""
            direction = _normalize_direction(candidate.direction)
            session = self._get_session(ctx)

            # --- per-pair strategy blocklist (Brock 2026-06-03) ---
            _blk = self.pair_blocklist.get(strategy)
            if _blk and pair in _blk:
                return GateResult(
                    gate_name=self.name, passed=False, mode=self.mode,
                    reason=f"PAIR-BLOCKLIST: {strategy} disabled on {pair} (lab net-negative)",
                    metrics={"verdict": "pair_blocked", "pair": pair,
                             "strategy": strategy, "direction": direction},
                )

            mod = ppm.get(pair, strategy)
            if mod is None:
                return GateResult(
                    gate_name=self.name, passed=False, mode=self.mode,
                    reason=f"no per-pair module for {pair}/{strategy}",
                    metrics={"verdict": "no_module"},
                )
            buckets = self._compute_buckets(candidate, ctx)
            regime = mod.assign_regime(buckets)

            # Brock 2026-06-02: MOMENTUM FILTER. Only trade WITH the trend.
            # align_score = # of {H20,H60,T1,T4} aligned with candidate dir.
            # Applies to EVERY candidate (incl. uncovered_bypass strategies) —
            # the lab showed strategy identity barely matters; trade-level
            # alignment is the whole edge (aligned>=3 +0.64p vs counter -0.30p).
            # Brock 2026-06-07: PER-PAIR ALIGN FLOOR + ADR AMPLIFIER GATE.
            # Validated 8yr x per-pair x per-year (Brock's Bot Strategy Book).
            # Per-pair floor (GBP=3, others=2); ADR>=require_adr_min amplifier;
            # calm-regime strategies (TF2) exempt from the ADR gate.
            align_floor = self.align_floor_by_pair.get(pair, self.align_min)
            align_score = (
                (1 if buckets.get("H20") in ("H20a", "H20b") else 0)
                + (1 if buckets.get("H60") in ("H60a", "H60b") else 0)
                + (1 if buckets.get("T1") == "T1a" else 0)
                + (1 if buckets.get("T4") == "T4a" else 0)
            )
            if align_floor > 0 and align_score < align_floor:
                return GateResult(
                    gate_name=self.name, passed=False, mode=self.mode,
                    reason=(f"MOMENTUM filter: align_score={align_score} < floor={align_floor} "
                            f"(pair={pair} H20={buckets.get('H20')} H60={buckets.get('H60')} "
                            f"T1={buckets.get('T1')} T4={buckets.get('T4')} dir={direction})"),
                    metrics={"verdict": "low_align", "align_score": align_score,
                             "align_floor": align_floor, "pair": pair,
                             "strategy": strategy, "direction": direction},
                )
            # ADR amplifier gate: require ADR>=require_adr_min, except calm-exempt (TF2).
            if self.require_adr_min > 0 and strategy not in self.adr_exempt_strategies:
                _adr = buckets.get("ADR", "") or ""
                _adr_lvl = int(_adr[3:]) if _adr.startswith("ADR") and _adr[3:].isdigit() else -1
                if _adr_lvl < self.require_adr_min:
                    return GateResult(
                        gate_name=self.name, passed=False, mode=self.mode,
                        reason=(f"ADR filter: ADR={_adr} < ADR{self.require_adr_min} "
                                f"(pair={pair} strategy={strategy} align={align_score} dir={direction})"),
                        metrics={"verdict": "low_adr", "adr": _adr, "adr_level": _adr_lvl,
                                 "require_adr_min": self.require_adr_min,
                                 "align_score": align_score, "pair": pair,
                                 "strategy": strategy, "direction": direction},
                    )


            # Brock 2026-06-07: EV from the 8yr Play Book, keyed on the live edge
            # axis the gate already computes — (strategy, align[, amplifier
            # bucket]) — retiring the stale (pair,session) matrix/pair lookups
            # from the decision path. Two-tier:
            #   tier 1 (amp_bucket): EV for the candidate's bucket in this
            #     strategy's amplifier factor at this align (richest);
            #   tier 2 (spine): unconditional EV at this align (always present
            #     for align >= the strategy's floor);
            #   neither -> below the per-strategy floor / no cell -> reject
            #     (known strategy) or uncovered_bypass (not in the 8yr book).
            # Spread-cost subtraction below is unchanged.
            pb = self._playbook.get(strategy)
            final_ev = None
            ev_tier = None
            amp_factor = pb["amp_factor"] if pb else None
            amp_bucket = buckets.get(amp_factor) if (pb and amp_factor) else None
            if pb is not None:
                if amp_bucket is not None:
                    final_ev = pb["amp"].get((align_score, amp_bucket))
                    if final_ev is not None:
                        ev_tier = "amp_bucket"
                if final_ev is None:
                    final_ev = pb["spine"].get(align_score)
                    if final_ev is not None:
                        ev_tier = "spine"

            if final_ev is None:
                # Uncovered strategy (absent from the 8yr book) -> pass on the
                # align/ADR + other gates, STAMPED unvalidated for separable PnL.
                if strategy and strategy not in self._known_strategies:
                    try:
                        if candidate.metadata is None:
                            candidate.metadata = {}
                        candidate.metadata["pip_evidence"] = "uncovered_bypass"
                        candidate.metadata["pip_nocell"] = True
                    except Exception:
                        pass
                    return GateResult(
                        gate_name=self.name, passed=True, mode=self.mode,
                        reason=(f"BYPASS uncovered strategy={strategy} — not in 8yr book; "
                                f"passing on align/ADR/other gates (pair={pair} align={align_score})"),
                        metrics={"verdict": "uncovered_bypass", "evidence": "uncovered_bypass",
                                 "uncovered": True, "pair": pair, "strategy": strategy,
                                 "direction": direction, "align_score": align_score},
                    )
                # Known strategy but no cell at this align (below per-strategy
                # floor, or align-cell absent) -> reject. Meaningful: the book
                # says don't trade this strategy at this alignment.
                return GateResult(
                    gate_name=self.name, passed=False, mode=self.mode,
                    reason=(f"no cell evidence (strat={strategy} align={align_score} "
                            f"amp={amp_factor}/{amp_bucket})"),
                    metrics={"verdict": "no_cell", "pair": pair, "strategy": strategy,
                             "direction": direction, "align_score": align_score,
                             "amp_factor": amp_factor, "amp_bucket": amp_bucket},
                )

            # Brock 2026-06-01: NET-of-spread EV. Lab pnl_pips is GROSS; live we
            # pay ~1x round-trip spread (1.8p avg, up to 2.6p on crosses). Gate on
            # the cost-adjusted number so a +4p gross edge on a wide-spread cross
            # does not pass as net-marginal/negative.
            _sp = getattr(getattr(ctx, "snapshot", None), "spread", 0.0) or 0.0
            _pip = 0.01 if any(j in pair for j in ("JPY", "MXN")) else 0.0001
            spread_pips = (_sp / _pip) if _pip else 0.0
            net_ev = final_ev - spread_pips
            tag = _tag(net_ev, floor=self.floor_pips)
            passed = tag in ("good_plate", "tasty", "optimized_meal")
            evidence = f"playbook_{ev_tier}"
            # STAMP: mark the EV source so realized PnL is attributable at close.
            try:
                if candidate.metadata is None:
                    candidate.metadata = {}
                candidate.metadata["pip_evidence"] = evidence
                candidate.metadata["pip_net_ev"] = round(net_ev, 2)
                candidate.metadata["pip_nocell"] = False
            except Exception:
                pass
            metrics = {
                "verdict": tag,
                "final_exp_pips": round(final_ev, 2),
                "net_exp_pips": round(net_ev, 2),
                "spread_pips": round(spread_pips, 2),
                "evidence": evidence,
                "ev_tier": ev_tier,
                "amp_factor": amp_factor,
                "amp_bucket": amp_bucket,
                "align_score": align_score,
                "regime": regime,
                "pair": pair, "strategy": strategy, "direction": direction,
            }
            _amp_s = f"{amp_factor}={amp_bucket}" if ev_tier == "amp_bucket" else "spine"
            if passed:
                reason = (f"HARVEST {tag} net={net_ev:+.2f}p (gross={final_ev:+.2f}p-spr={spread_pips:.1f}p) "
                          f"[playbook {ev_tier} align={align_score} {_amp_s}]")
            elif tag == "pip_trick":
                reason = (f"PIP TRICK detected exp_pips={final_ev:+.2f}p — danger "
                          f"[playbook {ev_tier} align={align_score} {_amp_s}]")
            else:
                reason = (f"empty plate net={net_ev:+.2f}p (gross={final_ev:+.2f}p-spr={spread_pips:.1f}p) < floor={self.floor_pips}p "
                          f"[playbook {ev_tier} align={align_score} {_amp_s}]")
            return GateResult(
                gate_name=self.name, passed=passed, mode=self.mode,
                reason=reason, metrics=metrics,
            )
        except Exception as e:
            self._log.warning("[PIP_EATER] eval error %s/%s: %s",
                              candidate.symbol, candidate.strategy, e)
            return GateResult(
                gate_name=self.name, passed=False, mode=self.mode,
                reason=f"eval error: {type(e).__name__}: {e}",
                metrics={"verdict": "error"},
            )
