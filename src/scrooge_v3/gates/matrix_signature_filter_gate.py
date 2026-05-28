"""matrix_signature_filter_gate — Gate #4 of the 4-layer matrix cascade.

The actual bucket-level decision:
  * Compute candidate's 14-factor bucket signature from live features.
  * Universal HTF20 pre-filter: any H20 in {H20d, H20e} -> BLOCK.
  * Loser veto: ANY (factor, bucket) classified LOSER for this combo -> BLOCK.
  * Winner allow: at least N WINNER hits (default 1) AND zero LOSER hits -> PASS.
  * Else (all NEUTRAL/INSUFFICIENT) -> BLOCK as no_signal.

Reads matrix_combo from candidate.metadata (set by matrix_combo_filter).
Stamps matrix_cluster_serial + matrix_winners_hit + matrix_losers_hit on
PASS so the ML observer + outcome ledger get the full fingerprint.
"""

from __future__ import annotations

import logging

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate
from .base import BaseGate
from . import matrix_engine as me

log = logging.getLogger("scrooge_v3.gate.matrix_signature_filter")


class MatrixSignatureFilterGate(BaseGate):
    name = "matrix_signature_filter"

    def __init__(self, config: dict | None = None, mode: GateMode = GateMode.HARD):
        super().__init__(config or {}, mode)
        self._stop_pips = float(self.config.get("stop_pips", 7.0))
        self._min_winner_hits = int(self.config.get("min_winner_hits", 1))
        self._allow_no_signal = bool(self.config.get("allow_no_signal", False))
        try:
            me.load()
            log.info(
                "[MATRIX_SIGNATURE_FILTER] ready — min_winner_hits=%d allow_no_signal=%s",
                self._min_winner_hits, self._allow_no_signal,
            )
        except Exception:
            log.exception("[MATRIX_SIGNATURE_FILTER] engine load failed; gate fails-open")

    def evaluate(self, candidate: TradeCandidate, ctx: SymbolContext) -> GateResult:
        combo = (candidate.metadata or {}).get("matrix_combo")
        if not combo:
            # Earlier gate didn't stamp combo (or gate registered out-of-order).
            # Recompute defensively rather than fail-closed silently.
            sym = candidate.symbol or "?"
            family = me.candidate_family(candidate)
            direction = me.candidate_direction(candidate)
            session = me.candidate_session(ctx)
            combo = me.combo_key(sym, family, direction, session)

        row = me.row_from_ctx(candidate, ctx)
        buckets = me.compute_buckets(row, stop_pips=self._stop_pips)

        sig = "|".join(f"{f.code}={buckets.get(f.code, '?')}" for f in me.factors())
        degraded = row.get("_matrix_features_degraded") or []
        log.info(
            "[MATRIX_SIGNATURE_FILTER] combo=%s sig=[%s]%s",
            combo, sig,
            f" degraded=[{','.join(degraded)}]" if degraded else "",
        )
        candidate.metadata["matrix_candidate_buckets"] = buckets
        candidate.metadata["matrix_bucket_signature"] = sig

        h20 = buckets.get("H20", "")
        if h20 in me.HTF20_MISMATCH_BUCKETS:
            return GateResult(
                gate_name=self.name, passed=False,
                reason=f"htf20_mismatch:h20_bucket={h20}",
                metrics={"blocked_by": "htf20_universal_pre_filter", "h20_bucket": h20},
            )

        rules = me.wlf_index().get(combo, {})
        winners_hit, losers_hit = [], []
        for f in me.factors():
            b = buckets.get(f.code, "")
            tier = rules.get(f.code, {}).get(b)
            if not tier:
                continue
            cls, wr, n = tier
            if cls == "WINNER":
                winners_hit.append((f.code, b, wr, n))
            elif cls == "LOSER":
                losers_hit.append((f.code, b, wr, n))

        candidate.metadata["matrix_winners_hit"] = [
            {"factor": f, "bucket": b, "wr": w, "n": n} for f, b, w, n in winners_hit
        ]
        candidate.metadata["matrix_losers_hit"] = [
            {"factor": f, "bucket": b, "wr": w, "n": n} for f, b, w, n in losers_hit
        ]

        if losers_hit:
            detail = ",".join(f"{f}={b}(wr={w:.0%},n={n})" for f, b, w, n in losers_hit)
            return GateResult(
                gate_name=self.name, passed=False,
                reason=f"loser_veto:{combo}:{detail}",
                metrics={
                    "blocked_by": "loser_veto",
                    "combo": combo,
                    "losers_hit": len(losers_hit),
                    "winners_hit": len(winners_hit),
                },
            )

        if len(winners_hit) >= self._min_winner_hits:
            detail = ",".join(f"{f}={b}(wr={w:.0%},n={n})" for f, b, w, n in winners_hit)
            serial = "|".join([combo] + [buckets.get(f.code, "?") for f in me.factors()])
            candidate.metadata["matrix_cluster_serial"] = serial
            candidate.metadata["matrix_schema"] = "v3_wlf_layered"
            best_wr = max(w for _, _, w, _ in winners_hit)
            return GateResult(
                gate_name=self.name, passed=True,
                reason=f"winner_allow:{combo}:winners={len(winners_hit)}:best_wr={best_wr:.0%}:{detail}",
                metrics={
                    "combo": combo,
                    "winners_hit": len(winners_hit),
                    "best_wr": best_wr,
                    "score": float(best_wr),
                },
            )

        if self._allow_no_signal:
            serial = "|".join([combo] + [buckets.get(f.code, "?") for f in me.factors()])
            candidate.metadata["matrix_cluster_serial"] = serial
            candidate.metadata["matrix_schema"] = "v3_wlf_no_signal_allowed"
            return GateResult(
                gate_name=self.name, passed=True,
                reason=f"no_signal_allowed:{combo}",
                metrics={"combo": combo, "winners_hit": 0, "losers_hit": 0},
            )

        return GateResult(
            gate_name=self.name, passed=False,
            reason=f"no_signal:{combo}:winners={len(winners_hit)}<min{self._min_winner_hits},losers=0",
            metrics={
                "combo": combo,
                "winners_hit": len(winners_hit),
                "losers_hit": 0,
            },
        )
