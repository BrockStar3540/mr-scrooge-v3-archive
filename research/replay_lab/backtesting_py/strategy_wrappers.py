"""backtesting.py Strategy wrappers that call live V3 strategy modules.

Architecture: one wrapper class instantiated per backtest. The wrapper
holds a ReplaySpec, a pre-loaded bundle of OHLC data, and a routing table.
In next() it:
  1. Builds a live-shaped SymbolContext at the current bar
  2. Calls the live strategy module (canonical_lien_dbb, etc.) to emit candidates
  3. Runs router_adapter.resolve_cell_match for the configured routing mode
  4. If approved + flat: places an order per entry_mode
  5. For open trades: applies management_adapter per management_mode

The "spec" is passed via class attribute (backtesting.py doesn'\''t support
__init__ overrides cleanly).
"""
from __future__ import annotations
import logging
import sys
from pathlib import Path

import pandas as pd
from backtesting import Strategy

_SRC = Path("/home/ubuntu/mr-scrooge-v3/src")
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from scrooge_v3.core.types import TradeDirection

from .context_factory import build_context
from .router_adapter import load_routing_table, resolve_cell_match
from .management_adapter import (
    apply_management, compute_entry_price, compute_signal_anchored_levels,
)

log = logging.getLogger("replay_lab.strategy_wrappers")


def _pip_size(symbol: str) -> float:
    return 0.01 if any(j in symbol for j in ("JPY", "MXN")) else 0.0001


class BaseReplayStrategy(Strategy):
    """Base class. Subclasses set spec + bundle as class attributes BEFORE
    Backtest.run() — backtesting.py instantiates internally so we can'\''t pass
    via __init__.
    """
    # These get set by the caller (run_single_replay) before Backtest.run()
    _spec = None
    _bundle = None
    _routing_table = None
    _strategy_module = None

    def init(self):
        if self._spec is None:
            raise RuntimeError("BaseReplayStrategy._spec must be set before run()")
        self._pip = _pip_size(self._spec.symbol)
        self._signal_log: list[dict] = []
        self._trade_meta: dict[int, dict] = {}   # bar_index -> meta

    def _build_ctx(self, i):
        return build_context(self._bundle, i, self._spec.symbol)

    def _try_emit(self, ctx):
        """Call the live strategy module and return a candidate (or None).

        Subclasses can override to constrain to a specific variant.
        """
        if self._strategy_module is None:
            return None
        try:
            cand = self._strategy_module.evaluate(ctx)
        except Exception as e:
            log.debug("strategy emit failed: %s", e)
            return None
        return cand

    def _routing_ok(self, ctx, cand) -> tuple[bool, dict]:
        if self._routing_table is None:
            return True, {"match_kind": "no_router"}
        # regime53 is exposed as a FEATURE (values dict), not classifier
        regime53_feat = ctx.classifications.get("regime53") or ctx.features.get("regime53")
        regime_label = None
        if regime53_feat is not None:
            vals = getattr(regime53_feat, "values", None) or {}
            regime_label = vals.get("technical_regime_53") or getattr(regime53_feat, "label", None)
        session = ctx.classifications.get("session_bucket")
        session_label = getattr(session, "label", None) if session else None
        sub_regime = ctx.classifications.get("mtb_sub_regime")
        sub_label = getattr(sub_regime, "label", None) if sub_regime else None
        return resolve_cell_match(
            self._routing_table, regime_label, self._spec.symbol, session_label,
            cand.direction.value, cand.strategy,
            sub_regime=sub_label,
            routing_mode=self._spec.routing_mode,
        )

    def next(self):
        i = len(self.data) - 1   # current bar index in the data slice
        if i < 50:
            return  # warm-up

        # Manage open trades first (apply BE/TP1/ratchet)
        for tr in list(self.trades):
            try:
                direction = "long" if tr.size > 0 else "short"
                actions = apply_management(
                    tr,
                    current_price=float(self.data.Close[-1]),
                    pip_size=self._pip,
                    direction=direction,
                    entry_fill=tr.entry_price,
                    management_mode=self._spec.management_mode,
                )
                if actions:
                    log.debug("mgmt %s: %s", tr, actions)
            except Exception as e:
                log.debug("mgmt failed: %s", e)

        # Only emit new entries when flat (mirror live: one position per symbol)
        if len(self.trades) > 0 or len(self.orders) > 0:
            return

        # Map backtesting bar index i -> bundle["M5"] absolute index.
        # They should be identical since we feed the full M5 frame to Backtest.
        try:
            ctx = self._build_ctx(i)
        except Exception as e:
            log.debug("ctx build failed at %d: %s", i, e)
            return

        cand = self._try_emit(ctx)
        if cand is None:
            return

        ok, info = self._routing_ok(ctx, cand)
        if not ok:
            return

        # Direction-mode handling
        signal_dir = cand.direction.value
        if self._spec.direction_mode == "reversed":
            exec_dir = "short" if signal_dir == "long" else "long"
        else:
            exec_dir = signal_dir

        # Entry geometry
        entry_price = compute_entry_price(
            cand.entry_price, exec_dir, self._pip, self._spec.entry_mode,
        )
        sl_price, tp_price = compute_signal_anchored_levels(
            cand.entry_price, exec_dir,
            sl_pips=self._spec.sl_pips, tp_pips=self._spec.tp_pips,
            pip_size=self._pip,
        )

        # Place LIMIT order
        try:
            if exec_dir == "long":
                self.buy(limit=entry_price, sl=sl_price, tp=tp_price,
                         tag=f"{cand.strategy}|{info.get('match_kind','?')}|{signal_dir}->{exec_dir}")
            else:
                self.sell(limit=entry_price, sl=sl_price, tp=tp_price,
                          tag=f"{cand.strategy}|{info.get('match_kind','?')}|{signal_dir}->{exec_dir}")
            self._signal_log.append({
                "i": i, "ts": self.data.index[-1], "strategy": cand.strategy,
                "signal_dir": signal_dir, "exec_dir": exec_dir,
                "entry_price": entry_price, "sl": sl_price, "tp": tp_price,
                "match_kind": info.get("match_kind"),
            })
        except Exception as e:
            log.debug("order place failed: %s", e)


class CanonicalLienDBBReplay(BaseReplayStrategy):
    """Replays live canonical_lien_dbb module."""
    pass


class BoxMasterTheoryReplay(BaseReplayStrategy):
    """Replays live box_master_theory module."""
    pass


def make_strategy_class(strategy_family: str):
    """Factory: returns a Strategy subclass parametrized by family."""
    if strategy_family == "canonical_lien_dbb":
        return CanonicalLienDBBReplay
    elif strategy_family == "box_master_theory":
        return BoxMasterTheoryReplay
    else:
        return BaseReplayStrategy


def instantiate_live_strategy(strategy_family: str):
    """Returns the live strategy MODULE instance to call inside next()."""
    if strategy_family == "canonical_lien_dbb":
        from scrooge_v3.strategies.canonical_lien_dbb import CanonicalLienDBBStrategy
        return CanonicalLienDBBStrategy({})
    elif strategy_family == "box_master_theory":
        from scrooge_v3.strategies.box_master_theory import BoxMasterTheoryStrategy
        return BoxMasterTheoryStrategy({})
    else:
        raise ValueError(f"unknown strategy_family: {strategy_family}")
