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


class _MultiProbeStrategy:
    """Wraps the PROBE_REGISTRY: tries every enabled probe + textbook probe
    on each ctx, returns the highest-RR candidate (mirrors the live bot's
    ProbeStrategy registration that bootstrap enables individually)."""
    def __init__(self, enabled: list[str] | None = None):
        # Make sure textbook_scalper probes are registered into PROBE_REGISTRY
        import scrooge_v3.strategies.textbook_scalper  # noqa: F401 — side-effect register
        from scrooge_v3.strategies.probes_v2 import PROBE_REGISTRY, ProbeStrategy
        self._probes = []
        names = enabled if enabled is not None else list(PROBE_REGISTRY.keys())
        for name in names:
            try:
                ps = ProbeStrategy(name, {"enabled": True})
                self._probes.append(ps)
            except ValueError:
                pass  # unknown probe — skip

    def evaluate(self, ctx):
        best = None
        best_rr = 0.0
        for p in self._probes:
            try:
                if not p.eligible(ctx):
                    continue
                cand = p.evaluate(ctx)
                if cand is None:
                    continue
                if cand.risk_reward > best_rr:
                    best, best_rr = cand, cand.risk_reward
            except Exception:
                continue
        return best




# ============================================================
# Higher-TF Trend Filter (Brock 2026-05-26): meta-filter that gates
# strategy emissions by daily / 4H directional bias.
# Per spec: bias = sign(close_now - close_N_periods_ago)
#   bias > 0  -> long-only
#   bias < 0  -> short-only
#   |bias| ~ 0 -> no trade
# ============================================================

class HTFTrendFilter:
    """Wraps a live strategy module; gates its emissions by HTF bias."""

    def __init__(self, strategy_module, htf="D", lookback_periods=20, neutral_pct=0.0):
        """
        Args:
            strategy_module: instance of live strategy (CanonicalLienDBBStrategy etc.)
            htf: "D" (daily) or "H4" (4H) — which timeframe to read bias from
            lookback_periods: number of HTF bars back to compare (5=1wk for D, 20=4wk, 60=12wk, 120=24wk)
            neutral_pct: if |close_change / close_prior| < this, treat as neutral (no trade)
                         0.0 = always trade in bias direction
        """
        self._mod = strategy_module
        self._htf = htf
        self._lookback = int(lookback_periods)
        self._neutral_pct = float(neutral_pct)
        self.enabled = True

    def _compute_bias(self, ctx) -> str | None:
        """Return 'long', 'short', or 'neutral'."""
        bars = ctx.snapshot.candles.get(self._htf)
        if bars is None or len(bars) == 0:
            bars = ctx.snapshot.candles.get("D")
        if bars is None or len(bars) <= self._lookback:
            return None
        try:
            close_now = float(bars["close"].iloc[-1])
            close_then = float(bars["close"].iloc[-1 - self._lookback])
            pct_change = (close_now - close_then) / close_then if close_then else 0.0
            if abs(pct_change) < self._neutral_pct:
                return "neutral"
            return "long" if pct_change > 0 else "short"
        except Exception:
            return None

    def evaluate(self, ctx):
        bias = self._compute_bias(ctx)
        if bias is None or bias == "neutral":
            return None
        try:
            cand = self._mod.evaluate(ctx)
        except Exception:
            return None
        if cand is None:
            return None
        # Only allow candidates aligned with HTF bias
        if cand.direction.value != bias:
            return None
        # Annotate metadata for telemetry
        if cand.metadata is None:
            cand.metadata = {}
        cand.metadata["htf_bias"] = bias
        cand.metadata["htf_lookback"] = self._lookback
        return cand




# ============================================================
# P1 #2 (Brock 2026-05-26): Regime-Filtered Session Momentum Filter.
# Meta-wrapper — gates emissions by session + volatility + spread.
# ============================================================
class SessionMomentumFilter:
    """Allow emissions only when session/vol/spread conditions all favor
    momentum continuation. Wraps any strategy module.

    Defaults match the dev brief's 'active sessions, volatility above
    median, spread acceptable relative to stop':
      - active sessions: london_open, london, ny_open, ny_mid
      - atr_median_lookback: 20 M5 bars
      - atr_min_multiple: 1.0 (current ATR >= rolling median)
      - max_spread_to_stop_pct: 0.15 (spread must be < 15%% of stop distance)
    """
    ACTIVE_SESSIONS = {"london_open", "london", "ny_open", "ny_mid"}

    def __init__(
        self,
        strategy_module,
        atr_median_lookback: int = 20,
        atr_min_multiple: float = 1.0,
        max_spread_to_stop_pct: float = 0.15,
        active_sessions: set | None = None,
    ):
        self._mod = strategy_module
        self._atr_lookback = int(atr_median_lookback)
        self._atr_min = float(atr_min_multiple)
        self._max_spread_pct = float(max_spread_to_stop_pct)
        self._active = set(active_sessions) if active_sessions else self.ACTIVE_SESSIONS
        self.enabled = True

    def _session_ok(self, ctx) -> bool:
        sb = ctx.classifications.get("session_bucket")
        label = getattr(sb, "label", None) if sb else None
        return label in self._active

    def _volatility_ok(self, ctx) -> tuple[bool, float, float]:
        """Returns (ok, atr_pips, median_pips)."""
        m5 = ctx.snapshot.candles.get("M5")
        if m5 is None or len(m5) == 0:
            m5 = ctx.snapshot.candles.get("5M")
        if m5 is None or len(m5) < self._atr_lookback + 1:
            return False, 0.0, 0.0
        try:
            pip = 0.01 if any(j in ctx.symbol for j in ("JPY","MXN")) else 0.0001
            # True range over last N bars
            highs = m5["high"].tail(self._atr_lookback + 1).astype(float).values
            lows  = m5["low"].tail(self._atr_lookback + 1).astype(float).values
            closes = m5["close"].tail(self._atr_lookback + 1).astype(float).values
            trs = []
            for i in range(1, len(highs)):
                tr = max(highs[i] - lows[i],
                         abs(highs[i] - closes[i-1]),
                         abs(lows[i] - closes[i-1]))
                trs.append(tr / pip)
            if not trs:
                return False, 0.0, 0.0
            atr_now = trs[-1]
            atr_median = sorted(trs)[len(trs)//2]
            return atr_now >= atr_median * self._atr_min, atr_now, atr_median
        except Exception:
            return False, 0.0, 0.0

    def _spread_ok(self, ctx, candidate) -> tuple[bool, float, float]:
        """Returns (ok, spread_pips, stop_pips)."""
        try:
            pip = 0.01 if any(j in ctx.symbol for j in ("JPY","MXN")) else 0.0001
            spread_pips = ctx.snapshot.spread / pip if ctx.snapshot.spread else 0.0
            stop_pips = abs(candidate.entry_price - candidate.stop_price) / pip
            if stop_pips <= 0:
                return False, spread_pips, 0.0
            ratio = spread_pips / stop_pips
            return ratio <= self._max_spread_pct, spread_pips, stop_pips
        except Exception:
            return False, 0.0, 0.0

    def evaluate(self, ctx):
        if not self._session_ok(ctx):
            return None
        try:
            cand = self._mod.evaluate(ctx)
        except Exception:
            return None
        if cand is None:
            return None
        vol_ok, atr, med = self._volatility_ok(ctx)
        if not vol_ok:
            return None
        sp_ok, sp_p, st_p = self._spread_ok(ctx, cand)
        if not sp_ok:
            return None
        # Annotate
        if cand.metadata is None: cand.metadata = {}
        cand.metadata["sm_session"] = getattr(ctx.classifications.get("session_bucket"), "label", "?")
        cand.metadata["sm_atr_pips"] = atr
        cand.metadata["sm_atr_median"] = med
        cand.metadata["sm_spread_pips"] = sp_p
        cand.metadata["sm_spread_to_stop"] = (sp_p / st_p) if st_p > 0 else 0
        return cand


def instantiate_live_strategy(strategy_family: str):
    """Returns the live strategy MODULE instance to call inside next().

    Supported families:
      - canonical_lien_dbb (class-based, 6 variants)
      - box_master_theory (class-based, 21+ MTB variants)
      - canonical_darvas (class-based, 5 DRV variants)
      - probes (PROBE_REGISTRY + textbook_scalper probes, 22 functions)
      - all (every family combined; returns highest-RR per bar)
    """
    if strategy_family == "canonical_lien_dbb":
        from scrooge_v3.strategies.canonical_lien_dbb import CanonicalLienDBBStrategy
        return CanonicalLienDBBStrategy({})
    elif strategy_family == "box_master_theory":
        from scrooge_v3.strategies.box_master_theory import BoxMasterTheoryStrategy
        return BoxMasterTheoryStrategy({})
    elif strategy_family == "canonical_darvas":
        from scrooge_v3.strategies.canonical_darvas import CanonicalDarvasStrategy
        return CanonicalDarvasStrategy({})
    elif strategy_family == "probes" or strategy_family == "textbook_scalper":
        return _MultiProbeStrategy()
    elif strategy_family == "all":
        return _AllFamiliesStrategy()
    else:
        raise ValueError(f"unknown strategy_family: {strategy_family}")


class _AllFamiliesStrategy:
    """Tries every family; returns highest-RR candidate across all."""
    def __init__(self):
        self._modules = [
            instantiate_live_strategy(f)
            for f in ("canonical_lien_dbb", "box_master_theory",
                       "canonical_darvas", "probes")
        ]

    def evaluate(self, ctx):
        best, best_rr = None, 0.0
        for m in self._modules:
            try:
                cand = m.evaluate(ctx)
                if cand is None: continue
                if cand.risk_reward > best_rr:
                    best, best_rr = cand, cand.risk_reward
            except Exception:
                continue
        return best
