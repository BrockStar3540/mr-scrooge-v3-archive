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


def _capture_feature_snapshot(ctx) -> dict:
    """Flatten SymbolContext into per-trade feature dict (Brock spec 2026-05-26).
    Required 14 + 'also add' factors + diagnostics."""
    snap = {}
    s = ctx.snapshot
    pip = 0.01 if any(j in ctx.symbol for j in ("JPY","MXN")) else 0.0001
    snap["pair"] = ctx.symbol
    snap["signal_time"] = s.timestamp.isoformat() if s.timestamp else None
    snap["hour_utc"] = s.timestamp.hour if s.timestamp else None
    snap["dow_utc"] = s.timestamp.weekday() if s.timestamp else None
    snap["mid"] = s.mid
    snap["bid"] = s.bid
    snap["ask"] = s.ask
    snap["spread_pips"] = (s.spread / pip) if s.spread else 0.0

    # Bollinger
    f = ctx.features
    boll = (f.get("bollinger") or {}).values if f.get("bollinger") else {}
    for k in ("upper_a","lower_a","sma_a","z_score","bb_position",
              "upper_b","lower_b","sma_b"):
        snap[f"bb_{k}"] = boll.get(k)
    if boll.get("upper_a") is not None and boll.get("lower_a") is not None:
        snap["bb_width_pips"] = (boll["upper_a"] - boll["lower_a"]) / pip
    snap["zscore"] = boll.get("z_score")
    snap["bb_position"] = boll.get("bb_position")

    # ATR — daily from feature + compute M5 + H1 from candles
    atr_d = (f.get("atr") or {}).values if f.get("atr") else {}
    snap["atr_daily"] = atr_d.get("atr")
    snap["adr_consumed"] = atr_d.get("adr_consumed")

    def _atr_pips(bars, n, p_pip):
        if bars is None or len(bars) < n+1: return None
        try:
            h = bars["high"].astype(float).tail(n+1).values
            l = bars["low"].astype(float).tail(n+1).values
            c = bars["close"].astype(float).tail(n+1).values
            trs = []
            for i in range(1, len(h)):
                trs.append(max(h[i]-l[i], abs(h[i]-c[i-1]), abs(l[i]-c[i-1])))
            return (sum(trs)/len(trs)) / p_pip if trs else None
        except Exception: return None

    m5 = ctx.snapshot.candles.get("M5")
    if m5 is None or len(m5) == 0: m5 = ctx.snapshot.candles.get("5M")
    h1 = ctx.snapshot.candles.get("1H")
    if h1 is None or len(h1) == 0: h1 = ctx.snapshot.candles.get("H1")
    d  = ctx.snapshot.candles.get("D")

    snap["atr_5m_pips"] = _atr_pips(m5, 14, pip)
    snap["atr_1h_pips"] = _atr_pips(h1, 14, pip)
    snap["atr_d_pips"]  = _atr_pips(d,  14, pip) if d is not None and len(d) > 14 else None

    # Realized volatility — stddev of last 20 M5 returns, annualized rough proxy
    if m5 is not None and len(m5) >= 21:
        try:
            closes = m5["close"].astype(float).tail(21).values
            import math
            rets = [(closes[i]/closes[i-1] - 1) for i in range(1, len(closes))]
            mean = sum(rets)/len(rets)
            var = sum((r-mean)**2 for r in rets)/len(rets)
            snap["realized_vol"] = math.sqrt(var)
        except Exception: snap["realized_vol"] = None

    # EMA + slopes
    ema_f = (f.get("ema") or {}).values if f.get("ema") else {}
    snap["ema20"] = ema_f.get("ema20")
    snap["ema50"] = ema_f.get("ema50")
    snap["ema20_dist_pct"] = ema_f.get("ema20_dist_pct")
    snap["ema50_dist_pct"] = ema_f.get("ema50_dist_pct")
    # Slope: re-compute from H1 closes
    if h1 is not None and len(h1) >= 22:
        try:
            closes_h1 = h1["close"].astype(float)
            def _ema(series, n):
                k = 2/(n+1); e = series.iloc[:n].mean()
                for v in series.iloc[n:]: e = v*k + e*(1-k)
                return e
            e20_now = _ema(closes_h1, 20)
            e20_prev = _ema(closes_h1.iloc[:-2], 20)
            e50_now = _ema(closes_h1, 50) if len(closes_h1) >= 50 else None
            e50_prev = _ema(closes_h1.iloc[:-2], 50) if len(closes_h1) >= 52 else None
            snap["ema20_slope"] = (e20_now - e20_prev) / pip if e20_prev else 0.0
            snap["ema50_slope"] = (e50_now - e50_prev) / pip if (e50_now and e50_prev) else None
        except Exception:
            snap["ema20_slope"] = snap["ema50_slope"] = None

    # RSI
    rsi = (f.get("rsi") or {}).values if f.get("rsi") else {}
    snap["rsi14"] = rsi.get("rsi")

    # OTR
    otr = (f.get("otr") or {}).values if f.get("otr") else {}
    snap["otr_ratio"] = otr.get("otr_ratio")

    # Regime53 features
    r53 = (f.get("regime53") or {}).values if f.get("regime53") else {}
    for k in ("technical_regime_53","ATR14","BB_width","ADX14","EMA_slope",
              "RSI14","close_pos","ATR_ratio","BB_compress"):
        snap[f"r53_{k}"] = r53.get(k)
    snap["regime53"] = r53.get("technical_regime_53")

    # Classifications
    c = ctx.classifications
    snap["bb_state"] = getattr(c.get("bb_state"), "label", None)
    snap["regime_label"] = getattr(c.get("regime"), "label", None)
    regime_md = getattr(c.get("regime"), "metadata", {}) or {}
    snap["regime_score"] = regime_md.get("score")
    snap["session_bucket"] = getattr(c.get("session_bucket"), "label", None)
    snap["sub_regime"] = getattr(c.get("mtb_sub_regime"), "label", None)
    snap["opening_state"] = getattr(c.get("opening_state"), "label", None)
    snap["structure"] = getattr(c.get("structure"), "label", None)

    # HTF bias at 4 lookbacks
    if d is not None and len(d) > 0:
        try:
            closes_d = d["close"].astype(float)
            for lb in (5, 20, 60, 120):
                if len(closes_d) > lb:
                    c_now = float(closes_d.iloc[-1]); c_then = float(closes_d.iloc[-1-lb])
                    pct = ((c_now - c_then)/c_then) if c_then else 0.0
                    snap[f"htf_pct_{lb}"] = pct
                    snap[f"htf_bias_{lb}"] = "long" if c_now>c_then else ("short" if c_now<c_then else "neutral")
        except Exception: pass

    # H1/H4 trend (sign of close change)
    if h1 is not None and len(h1) > 20:
        try:
            c1 = float(h1["close"].iloc[-1]); c1p = float(h1["close"].iloc[-21])
            snap["trend_1h_pct"] = (c1-c1p)/c1p if c1p else 0.0
            snap["trend_1h"] = "long" if c1>c1p else ("short" if c1<c1p else "neutral")
            if len(h1) > 80:
                c4 = float(h1["close"].iloc[-1]); c4p = float(h1["close"].iloc[-81])
                snap["trend_4h_pct"] = (c4-c4p)/c4p if c4p else 0.0
                snap["trend_4h"] = "long" if c4>c4p else ("short" if c4<c4p else "neutral")
        except Exception: pass

    # Range percentile (M5 bar range vs last 50)
    if m5 is not None and len(m5) >= 51:
        try:
            highs = m5["high"].astype(float).tail(50).values
            lows  = m5["low"].astype(float).tail(50).values
            ranges = [(highs[i]-lows[i])/pip for i in range(len(highs))]
            now_rng = ranges[-1]
            sorted_rngs = sorted(ranges)
            rank = sorted_rngs.index(now_rng) if now_rng in sorted_rngs else 0
            snap["range_percentile"] = rank / max(len(ranges)-1, 1)
            snap["range_pips_now"] = now_rng
        except Exception: pass

    # Distance to structure (nearest recent swing hi/lo within 50 M5 bars)
    if m5 is not None and len(m5) >= 50:
        try:
            highs = m5["high"].astype(float).tail(50).values
            lows  = m5["low"].astype(float).tail(50).values
            close = float(m5["close"].iloc[-1])
            swing_hi = max(highs[:-1])
            swing_lo = min(lows[:-1])
            snap["dist_to_swing_high_pips"] = (swing_hi - close) / pip
            snap["dist_to_swing_low_pips"]  = (close - swing_lo) / pip
            snap["distance_to_structure_pips"] = min(abs(snap["dist_to_swing_high_pips"]),
                                                      abs(snap["dist_to_swing_low_pips"]))
        except Exception: pass

    # Pullback depth: how far has price retraced from the recent extreme in trend direction
    if m5 is not None and len(m5) >= 20 and snap.get("trend_1h"):
        try:
            highs = m5["high"].astype(float).tail(20).values
            lows  = m5["low"].astype(float).tail(20).values
            close = float(m5["close"].iloc[-1])
            if snap["trend_1h"] == "long":
                # Uptrend: measure pullback from swing high to current close
                hi = max(highs); lo = min(lows)
                rng = hi - lo
                snap["pullback_depth_pct"] = (hi - close) / rng if rng > 0 else 0.0
            elif snap["trend_1h"] == "short":
                hi = max(highs); lo = min(lows)
                rng = hi - lo
                snap["pullback_depth_pct"] = (close - lo) / rng if rng > 0 else 0.0
        except Exception: pass

    return snap


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
        # Per-trade feature snapshots, written to a per-run JSONL sidecar.
        # Bypasses backtesting.py's instance-shuffling issues entirely.
        import tempfile, os
        sidecar = os.path.join(
            tempfile.gettempdir(),
            f"feature_log_{self._spec.symbol}_{self._spec.label or 'run'}_"
            f"{os.getpid()}.jsonl",
        )
        # Clear any previous file from a prior run with same name
        try:
            if os.path.exists(sidecar):
                os.remove(sidecar)
        except Exception: pass
        type(self)._feature_sidecar_path = sidecar
        type(self)._feature_log = {}  # kept for back-compat

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
        # no_router-bypass-honored (Brock 2026-05-28 Phase 3): honor the
        # spec's routing_mode BEFORE testing _routing_table. load_routing_table
        # auto-loads the live parquet when path is None, so _routing_table is
        # never None — the old check was dead. Probes that aren't in the slate
        # (BR2_vcb_short, etc.) were silently routed-blocked on every emit.
        if self._spec.routing_mode in ("no_router", "bypass"):
            return True, {"match_kind": self._spec.routing_mode}
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

        # Capture feature snapshot at entry bar for factor analysis
        snap = _capture_feature_snapshot(ctx)
        snap["strategy"] = cand.strategy
        snap["signal_dir"] = signal_dir
        snap["exec_dir"] = exec_dir
        snap["match_kind"] = info.get("match_kind")
        snap["entry_price_set"] = entry_price
        snap["sl_set"] = sl_price
        snap["tp_set"] = tp_price
        snap["candidate_rr"] = cand.risk_reward
        snap["candidate_score"] = cand.score
        type(self)._feature_log[i] = snap
        # Also write to sidecar JSONL — primary persistence path
        try:
            import json
            sidecar = getattr(type(self), "_feature_sidecar_path", None)
            if sidecar:
                with open(sidecar, "a") as _f:
                    _f.write(json.dumps({"bar": i, **{k: (v if not hasattr(v, 'isoformat') else v.isoformat()) for k, v in snap.items()}}, default=str) + "\n")
        except Exception:
            pass

        # Place entry order.
        # 2026-05-28 Brock Phase 3 fix: entry_mode="signal" was placing LIMIT
        # at the signal price. backtesting.py rejects LIMIT SELL whose
        # limit == current close (and LIMIT BUY at/above market), which
        # silently dropped 100% of probes_v2 orders (entry_price == close
        # for every emit). Match live-broker semantics: signal-mode fills at
        # next-bar market; offset modes (pullback_*, old_stop_zone) keep
        # LIMIT because their entry_price is intentionally offset from price.
        try:
            use_market = (self._spec.entry_mode == "signal")
            _tag = f"{cand.strategy}|{info.get('match_kind','?')}|{signal_dir}->{exec_dir}|i={i}"
            if exec_dir == "long":
                if use_market:
                    self.buy(sl=sl_price, tp=tp_price, tag=_tag)
                else:
                    self.buy(limit=entry_price, sl=sl_price, tp=tp_price, tag=_tag)
            else:
                if use_market:
                    self.sell(sl=sl_price, tp=tp_price, tag=_tag)
                else:
                    self.sell(limit=entry_price, sl=sl_price, tp=tp_price, tag=_tag)
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




# ============================================================
# 7-pip realistic-slice filter (Brock 2026-05-26 hard rule).
# available_slice_pips = projected_tp_pips - spread - slippage
# Reject if < min_pips (default 7).
# ============================================================
class SliceFloorFilter:
    """Meta-wrapper that rejects candidates whose realistic move-to-TP
    after costs is below min_pips."""

    def __init__(self, strategy_module, min_pips: float = 7.0,
                 slippage_pips: float = 0.5):
        self._mod = strategy_module
        self._min = float(min_pips)
        self._slip = float(slippage_pips)
        self.enabled = True

    def evaluate(self, ctx):
        try:
            cand = self._mod.evaluate(ctx)
        except Exception:
            return None
        if cand is None:
            return None
        try:
            pip = 0.01 if any(j in ctx.symbol for j in ("JPY","MXN")) else 0.0001
            # Projected TP distance in pips
            md = cand.metadata or {}
            projected = md.get("projected_tp_pips")
            if projected is None:
                # Compute from candidate entry/tp
                projected = abs(cand.take_profit - cand.entry_price) / pip if cand.take_profit else 0
            spread_pips = (ctx.snapshot.spread / pip) if ctx.snapshot.spread else 0.0
            available = float(projected) - float(spread_pips) - self._slip
            if available < self._min:
                return None
            # Annotate
            cand.metadata = {**(cand.metadata or {}),
                              "slice_projected_pips": float(projected),
                              "slice_spread_pips": float(spread_pips),
                              "slice_slip_pips": self._slip,
                              "slice_available_pips": available}
            return cand
        except Exception:
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
    elif strategy_family == "dbb_trend":
        from scrooge_v3.strategies.dbb_trend import DBBTrendStrategy
        return DBBTrendStrategy({"enabled": True})
    elif strategy_family == "reversal":
        from scrooge_v3.strategies.reversal import ReversalStrategy
        return ReversalStrategy({"enabled": True})
    elif strategy_family == "trend":
        from scrooge_v3.strategies.trend import TrendStrategy
        return TrendStrategy({"enabled": True})
    elif strategy_family == "direct":
        from scrooge_v3.strategies.direct_entry import DirectEntryStrategy
        return DirectEntryStrategy({"enabled": True})
    elif strategy_family == "ifvg":
        from scrooge_v3.strategies.research_strategies.ifvg_imbalance import IFVGStrategy
        return IFVGStrategy()
    elif strategy_family == "session_breakout":
        from scrooge_v3.strategies.research_strategies.session_breakout import SessionBreakoutStrategy
        return SessionBreakoutStrategy()
    elif strategy_family == "compression_expansion":
        from scrooge_v3.strategies.research_strategies.compression_expansion import CompressionExpansionStrategy
        return CompressionExpansionStrategy({"enabled": True})
    elif strategy_family == "trend_pullback":
        from scrooge_v3.strategies.research_strategies.intraday_trend_pullback import IntradayTrendPullbackStrategy
        return IntradayTrendPullbackStrategy()
    elif strategy_family == "chaikin_macd_atr":
        from scrooge_v3.strategies.research_strategies.chaikin_macd_atr import ChaikinMACDATRStrategy
        return ChaikinMACDATRStrategy()
    elif strategy_family == "compression_reversion":
        from scrooge_v3.strategies.research_strategies.compression_mean_reversion import CompressionMeanReversionStrategy
        return CompressionMeanReversionStrategy()
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
