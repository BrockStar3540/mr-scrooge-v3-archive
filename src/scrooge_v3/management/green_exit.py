"""Green Exit ladder — Brock 2026-06-04.

Replaces the single SL10/TP12 scalper exit with a scale-out ladder + a
time-boxed green-harvest. Backtested on the align=4 deployed book: +1.95p/trade
(OOS +1.61p) vs +1.47p single-TP. Edge comes from (a) locking +6 on the runners
after the first tranche and (b) salvaging 4h-stagnant greens — losers unchanged.

Spec
----
Phase 1 (0-4h), price-pips from entry:
  SL -10 ; ladder TP  50% @ +12 ,  25% @ +20 ,  25% @ +30
  When +12 fills (50% out) -> move SL to +6 on the runners (trade now green-locked).

4h checkpoint (whatever is still open):
  >= +7p  -> harvest: limit-close 0.5 pip past the current tick (favorable side)
  <  +7p  -> Phase 2

Phase 2 (re-checked every 30 min):
  keep waiting; once it climbs, arm SL +6 / limit exit +7.5
  (while still below the harvest zone the original -10 SL keeps protecting it)

After any green exit -> NO cooldown (handled by the close-reason tag).

This manager is a pure decision function. It NEVER touches the broker; it returns
one GreenExitDecision per cycle which position_coordinator executes (or, in
observe mode, only logs). All ladder state lives in position.metadata under the
``gx_*`` keys so it survives restarts via the tracker's persisted state.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Optional

from scrooge_v3.core.types import TradeDirection

log = logging.getLogger("scrooge_v3.management.green_exit")


@dataclass
class GreenExitDecision:
    """One ladder action for position_coordinator to execute."""

    position_id: str
    kind: str          # "partial" | "move_sl" | "limit_exit"
    reason: str
    # partial:
    close_fraction: float = 0.0    # fraction of ORIGINAL units to close
    tranche: str = ""              # "tp1" | "tp2"
    move_sl_after: Optional[float] = None  # price to move SL to right after a partial (or None)
    # move_sl:
    new_stop: Optional[float] = None       # absolute price
    # limit_exit:
    limit_price: Optional[float] = None     # absolute price for a closing limit
    green: bool = False            # True => this exit is a "green" exit (no cooldown)
    elapsed_min: float = 0.0       # minutes since open (for scan-tick stamping)
    profit_pips: float = 0.0       # current profit in price-pips (audit)


def _now() -> datetime:
    return datetime.now(timezone.utc)


class GreenExitManager:
    """Drives the Phase-1 ladder + 4h checkpoint + Phase-2 harvest for one position."""

    def __init__(self, config: dict | None = None):
        c = config or {}
        self.enabled = bool(c.get("enabled", False))
        self.observe = bool(c.get("observe", True))   # log-only until proven
        # ladder (price-pips from entry; matches the live scalper_clamp convention)
        self.sl0 = float(c.get("sl_pips", -10.0))
        self.tp1 = float(c.get("tp1_pips", 12.0))
        self.tp2 = float(c.get("tp2_pips", 20.0))
        self.tp3 = float(c.get("tp3_pips", 30.0))
        self.f1 = float(c.get("tp1_fraction", 0.50))
        self.f2 = float(c.get("tp2_fraction", 0.25))
        self.sl_lock = float(c.get("sl_lock_pips", 6.0))
        # phases
        self.p1_minutes = float(c.get("phase1_minutes", 240.0))
        self.harvest_min = float(c.get("harvest_min_pips", 7.0))
        self.p2_limit = float(c.get("phase2_limit_pips", 7.5))
        self.scan_minutes = float(c.get("phase2_scan_minutes", 30.0))
        self.harvest_edge = float(c.get("harvest_past_tick_pips", 0.5))
        # EXIT BRAIN (2026-06-08): live model scores remaining upside each cycle.
        # v1 = TAKE half (harvest faders early). RIDE half (extend runners) = v2.
        _xm = (c.get("exit_model") or {})
        self.exit_model_on = bool(_xm.get("enabled", False))
        self.exit_take_below = float(_xm.get("take_below", 18.0))
        self.exit_ride_above = float(_xm.get("ride_above", 25.0))
        self._xm_path = str(_xm.get("model_path", "/home/ubuntu/mr-scrooge-v3/data/exit-model/exit_model.xgb"))
        self._xm_meta_path = str(_xm.get("meta_path", "/home/ubuntu/mr-scrooge-v3/data/exit-model/exit_model_meta.json"))
        self._xm_booster = None
        self._xm_meta = None
        self._xm_failed = False

    # -- helpers -------------------------------------------------------
    @staticmethod
    def _elapsed_min(position: Any) -> float:
        ts = getattr(position, "opened_at", "") or ""
        if not ts:
            return 0.0
        try:
            t0 = datetime.fromisoformat(ts)
            if t0.tzinfo is None:
                t0 = t0.replace(tzinfo=timezone.utc)
            return (_now() - t0).total_seconds() / 60.0
        except Exception:
            return 0.0

    @staticmethod
    def _meta(position: Any) -> dict:
        m = getattr(position, "metadata", None)
        return m if isinstance(m, dict) else {}

    def _profit_pips(self, direction: TradeDirection, entry: float, price: float, pip: float) -> float:
        if pip <= 0:
            return 0.0
        d = (price - entry) if direction == TradeDirection.LONG else (entry - price)
        return d / pip

    def _price_at(self, direction: TradeDirection, entry: float, pips: float, pip: float) -> float:
        return entry + pips * pip if direction == TradeDirection.LONG else entry - pips * pip

    def _recent_range_pips(self, m5_bars, pip_size):
        """High-low range (pips) over the last ~1h of M5 bars = the last 13 bars,
        matching exit_corpus.py's training window slice(b-12, b+1). The range is
        direction-independent (the short-side mirroring cancels in hi.max-lo.min),
        so raw high/low is faithful for both directions. None on any error."""
        try:
            if m5_bars is None or pip_size <= 0 or len(m5_bars) < 1:
                return None
            w = m5_bars.iloc[-13:]
            hi = float(w["high"].max())
            lo = float(w["low"].min())
            return (hi - lo) / pip_size
        except Exception:
            return None

    def _exit_rem_mfe(self, position, profit, m5_bars, pip_size, elapsed_min):
        """Predicted remaining favorable pips (the exit brain). None on any error."""
        if self._xm_failed:
            return None
        try:
            import json as _json
            from pathlib import Path as _P
            sig = self._meta(position).get("exit_sig")
            if not isinstance(sig, dict):
                return None
            rr = self._recent_range_pips(m5_bars, pip_size)
            if rr is None:
                return None
            if self._xm_booster is None:
                import xgboost as _xgb
                if not _P(self._xm_path).exists():
                    self._xm_failed = True
                    return None
                b = _xgb.Booster(); b.load_model(self._xm_path)
                self._xm_booster = b
                self._xm_meta = _json.loads(_P(self._xm_meta_path).read_text())
            import xgboost as _xgb
            import pandas as _pd
            mt = self._xm_meta
            order = mt["feature_order"]; levels = mt["categorical_levels"]
            adr_lvl = self._meta(position).get("adr_lvl", -1)
            row = {"profit_at": float(profit), "entry_adr": float(adr_lvl),
                   "recent_range": float(rr), "bars_elapsed": float(elapsed_min) / 5.0}
            for c in mt["categorical_features"]:
                row[c] = str(sig.get(c, "NA"))
            df = _pd.DataFrame([[row.get(c) for c in order]], columns=order)
            for c in mt["categorical_features"]:
                cats = levels.get(c) or [str(df[c].iloc[0])]
                df[c] = df[c].astype(str).astype("category").cat.set_categories(cats)
            for c in mt["numeric_features"]:
                df[c] = _pd.to_numeric(df[c], errors="coerce")
            return float(self._xm_booster.predict(_xgb.DMatrix(df, enable_categorical=True))[0])
        except Exception as e:  # noqa: BLE001
            log.warning("[GREEN_EXIT] exit model predict failed (%s) — disabling", e)
            self._xm_failed = True
            return None

    # -- main ----------------------------------------------------------
    def check(
        self,
        position: Any,
        current_price: float,
        pip_size: float,
        bid: float = 0.0,
        ask: float = 0.0,
        hourly_bars: Any = None,
        m5_bars: Any = None,
    ) -> Optional[GreenExitDecision]:
        """Return the next ladder action for this position, or None to hold."""
        if not self.enabled:
            return None

        pos_id = getattr(position, "trade_id", None) or getattr(position, "position_id", str(id(position)))
        direction = TradeDirection(getattr(position, "direction", "long"))
        entry = float(getattr(position, "entry_price", 0.0) or 0.0)
        if entry <= 0 or pip_size <= 0:
            return None

        meta = self._meta(position)
        if meta.get("gx_harvest_armed"):
            return None  # a closing limit is already resting server-side — nothing to do
        tp1_done = bool(meta.get("gx_tp1_done") or getattr(position, "tp1_taken", False))
        tp2_done = bool(meta.get("gx_tp2_done"))
        phase2 = bool(meta.get("gx_phase2"))
        profit = self._profit_pips(direction, entry, current_price, pip_size)
        elapsed = self._elapsed_min(position)

        def mk(**kw):
            kw.setdefault("elapsed_min", elapsed)
            kw.setdefault("profit_pips", round(profit, 2))
            return GreenExitDecision(**kw)

        # exit-side price for closing limits/harvests (sell long on bid, cover short on ask)
        exit_px = bid if direction == TradeDirection.LONG else ask
        if exit_px <= 0:
            exit_px = current_price

        # ---------- PHASE 1 (0 - p1_minutes) ----------
        if elapsed < self.p1_minutes and not phase2:
            # tranche 1: +12, close 50%, then lock SL to +6
            if (not tp1_done) and profit >= self.tp1:
                sl_lock_px = self._price_at(direction, entry, self.sl_lock, pip_size)
                return mk(
                    position_id=pos_id, kind="partial", tranche="tp1",
                    close_fraction=self.f1, move_sl_after=sl_lock_px,
                    reason=f"TP1 +{self.tp1:.0f}p hit (profit={profit:.1f}p) -> close {self.f1:.0%}, lock SL +{self.sl_lock:.0f}p",
                )
            # tranche 2: +20, close 25%
            if tp1_done and (not tp2_done) and profit >= self.tp2:
                return mk(
                    position_id=pos_id, kind="partial", tranche="tp2",
                    close_fraction=self.f2,
                    reason=f"TP2 +{self.tp2:.0f}p hit (profit={profit:.1f}p) -> close {self.f2:.0%} of original",
                )
            # EXIT BRAIN (2026-06-08) — TAKE half: once the runner is active
            # (TP1 done), score remaining upside each cycle; if the model says the
            # move is dying, harvest the green NOW instead of riding it back down.
            if self.exit_model_on and tp1_done and profit >= self.tp1:
                rem = self._exit_rem_mfe(position, profit, m5_bars, pip_size, elapsed)
                if rem is not None and rem < self.exit_take_below:
                    edge = self.harvest_edge * pip_size
                    lim = exit_px + edge if direction == TradeDirection.LONG else exit_px - edge
                    return mk(position_id=pos_id, kind="limit_exit", limit_price=lim, green=True,
                              reason=f"EXIT-BRAIN TAKE: model rem={rem:.1f}p < {self.exit_take_below:.0f}p at +{profit:.1f}p -> harvest green")
            # tranche 3 (+30) rides on the server-side TP; nothing to do here.
            return None

        # ---------- 4h CHECKPOINT (first crossing of p1_minutes) ----------
        if elapsed >= self.p1_minutes and not phase2:
            if profit >= self.harvest_min:
                # EXIT BRAIN — don't harvest a climber at the 4h mark. If the model
                # says room remains, drop to Phase 2 and ride the existing TP3.
                if self.exit_model_on:
                    _rem = self._exit_rem_mfe(position, profit, m5_bars, pip_size, elapsed)
                    if _rem is not None and _rem >= self.exit_ride_above:
                        return mk(position_id=pos_id, kind="enter_phase2",
                                  reason=f"EXIT-BRAIN RIDE: rem={_rem:.1f}p >= {self.exit_ride_above:.0f}p at +{profit:.1f}p -> skip 4h harvest, ride TP3")
                # green harvest: limit 0.5 pip past the tick on the favorable side
                edge = self.harvest_edge * pip_size
                lim = exit_px + edge if direction == TradeDirection.LONG else exit_px - edge
                return mk(
                    position_id=pos_id, kind="limit_exit", limit_price=lim, green=True,
                    reason=f"4h harvest: profit={profit:.1f}p >= +{self.harvest_min:.0f}p -> limit close {self.harvest_edge:.1f}p past tick",
                )
            # under +7p -> drop into Phase 2 (stamped by the executor)
            return mk(
                position_id=pos_id, kind="enter_phase2",
                reason=f"4h checkpoint: profit={profit:.1f}p < +{self.harvest_min:.0f}p -> Phase 2 (scan every {self.scan_minutes:.0f}m)",
            )

        # ---------- PHASE 2 (post-4h, scan every 30 min) ----------
        if phase2:
            last_scan = float(meta.get("gx_last_scan_min", 0.0) or 0.0)
            if (elapsed - last_scan) < self.scan_minutes:
                return None  # not yet time to re-scan
            # it's a scan tick. If it has climbed to the harvest band, limit-exit at +7.5.
            if profit >= self.p2_limit:
                # EXIT BRAIN — don't cap a climber. If the model says room remains,
                # HOLD (scan_tick) and let the existing +30/ADR TP3 ride, instead of
                # salvaging at the current level. Else salvage. Fixes Phase-2
                # amputating late-bloomers (e.g. today's AUD shorts at +8-10).
                if self.exit_model_on:
                    _rem = self._exit_rem_mfe(position, profit, m5_bars, pip_size, elapsed)
                    if _rem is not None and _rem >= self.exit_ride_above:
                        return mk(position_id=pos_id, kind="scan_tick",
                                  reason=f"EXIT-BRAIN RIDE(p2): rem={_rem:.1f}p >= {self.exit_ride_above:.0f}p at +{profit:.1f}p -> hold, ride TP3")
                lim = self._price_at(direction, entry, self.p2_limit, pip_size)
                return mk(
                    position_id=pos_id, kind="limit_exit", limit_price=lim, green=True,
                    reason=f"Phase2 fit: profit={profit:.1f}p >= +{self.p2_limit:.1f}p -> limit exit +{self.p2_limit:.1f}p",
                )
            # not yet — just record the scan tick (executor stamps gx_last_scan_min)
            return mk(
                position_id=pos_id, kind="scan_tick",
                reason=f"Phase2 scan: profit={profit:.1f}p < +{self.p2_limit:.1f}p, keep waiting",
            )

        return None
