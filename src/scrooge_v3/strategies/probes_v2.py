"""Trainer-v2 probes as V3 live strategies.

Ports the 10 v2 probes (Oanda-Bot-Trainer/scripts/playbook_probes_v2.py) into
the V3 live runtime as parametric strategy modules. Each probe becomes a
named V3 strategy that emits TradeCandidates via the standard Protocol.

Architectural decisions:

  - Regime gating moves OUT of the probe and INTO the router.
    Probes originally self-gated on `regime_label` (Alpha-fresh / Bravo /
    Charlie / etc.). Live, that responsibility shifts to
    RegimeStrategyRouterGate (technical_regime_53 allow-list). Each probe
    wrapper declares its `family` (reversal / dbb_trend / direct) so the
    existing 53-cell allow-list applies. The probe's internal regime check
    is satisfied by feeding the probe its expected regime_label sentinel
    — the router has already decided this regime53 cell is OK for this
    probe's family before we ever evaluate.

  - All 10 probes default DISABLED. Enable per-probe via
    config.strategies.probes_v2.<probe_name>.enabled = true.
    This lets Brock fan-in probes one at a time based on ungated-replay
    evidence.

  - Probes consume V3 features. Field mapping:
        ema20      ← features.ema.values["ema20"]
        atr_pips   ← features.atr.values["atr"] / pip_size(symbol)
        rsi        ← features.rsi.values["rsi"]
        bb_position← features.bollinger.values["bb_position"]
        bb_upper   ← features.bollinger.values["upper_a"]
        bb_lower   ← features.bollinger.values["lower_a"]

  - Strategy family mapping (drives router allow-list cells):
        alpha_pullback_v2              → dbb_trend  (continuation)
        alpha_breakout_retest_v2       → direct     (breakout)
        alpha_extended_fade_v2         → reversal   (extension fade)
        echo_box_fade_v2               → reversal   (rail fade)
        echo_failed_breakout_v2        → reversal   (failed-break fade)
        charlie_pullback_continuation_v2 → dbb_trend (continuation)
        charlie_compression_breakout   → direct     (compression breakout)
        bravo_failed_momentum          → reversal   (failed-momentum fade)
        bravo_expansion_continuation   → dbb_trend  (range expansion)
        delta_tag_and_go_v2            → direct     (tag-and-go continuation)
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable

from scrooge_v3.core.types import (
    SymbolContext,
    TradeCandidate,
    TradeDirection,
)

log = logging.getLogger("scrooge_v3.strategy.probes_v2")


# ---------------------------------------------------------------------------
# Probe-internal types (replicated from Oanda-Bot-Trainer/playbook_probes_v2)
# ---------------------------------------------------------------------------

@dataclass
class ProbeContext:
    ts: datetime
    symbol: str
    spread_pips: float
    m5_open: list[float]
    m5_high: list[float]
    m5_low: list[float]
    m5_close: list[float]
    features: dict
    regime_label: str
    atr_pips_mean_20: float | None = None
    r_targets: list[float] = field(default_factory=lambda: [1.5, 2.0])
    bb_state: str | None = None


@dataclass
class ProbeCandidate:
    direction: str
    entry_price: float
    stop_price: float
    r_targets: list[float]
    probe_name: str
    regime_label: str
    structure_ref_price: float
    notes: dict = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Probe helpers
# ---------------------------------------------------------------------------

def pip_size(symbol: str) -> float:
    return 0.01 if symbol.split("_")[-1] == "JPY" else 0.0001


def _stop_distance_pips(entry, struct_ref, atr_pips, spread_pips, symbol):
    pip = pip_size(symbol)
    structure_dist = abs(entry - struct_ref) / pip + 0.25 * atr_pips
    spread_floor = max(spread_pips * 3.0, 3.0)
    return max(structure_dist, spread_floor)


def _build_candidate_multi(direction, entry, struct_ref, ctx, probe_name, notes=None):
    pip = pip_size(ctx.symbol)
    atr_pips = float(ctx.features.get("atr_pips") or 0.0)
    sl_pips = _stop_distance_pips(entry, struct_ref, atr_pips, ctx.spread_pips, ctx.symbol)
    stop_price = entry - sl_pips * pip if direction == "long" else entry + sl_pips * pip
    return ProbeCandidate(
        direction=direction, entry_price=entry, stop_price=stop_price,
        r_targets=list(ctx.r_targets), probe_name=probe_name,
        regime_label=ctx.regime_label, structure_ref_price=struct_ref,
        notes={**(notes or {}), "stop_pips": sl_pips, "atr_pips": atr_pips},
    )


def _bar_body(ctx, idx=-1): return abs(ctx.m5_close[idx] - ctx.m5_open[idx])
def _bar_range(ctx, idx=-1): return ctx.m5_high[idx] - ctx.m5_low[idx]
def _is_bull_bar(ctx, idx=-1): return ctx.m5_close[idx] > ctx.m5_open[idx]
def _mean_range(ctx, lookback):
    rs = [ctx.m5_high[i] - ctx.m5_low[i] for i in range(-lookback - 1, -1)]
    return sum(rs) / max(len(rs), 1)


# ---------------------------------------------------------------------------
# Probe functions (regime gate stripped — router handles via regime53)
# ---------------------------------------------------------------------------

def probe_alpha_pullback_v2(ctx):
    f = ctx.features
    ema20, atr_pips, rsi = f.get("ema20"), f.get("atr_pips"), f.get("rsi")
    if None in (ema20, atr_pips, rsi): return None
    pip = pip_size(ctx.symbol)
    close = ctx.m5_close[-1]
    direction = "long" if close > ema20 else "short"
    if abs(close - ema20) / pip > 0.3 * atr_pips: return None
    if direction == "long":
        if not (_is_bull_bar(ctx) and (close - ctx.m5_low[-1]) >= 0.5 * _bar_range(ctx)): return None
    else:
        if not ((not _is_bull_bar(ctx)) and (ctx.m5_high[-1] - close) >= 0.5 * _bar_range(ctx)): return None
    if rsi <= 30 or rsi >= 70: return None
    struct_ref = min(ctx.m5_low[-5:]) if direction == "long" else max(ctx.m5_high[-5:])
    return _build_candidate_multi(direction, close, struct_ref, ctx, "alpha_pullback_v2", {"rsi": rsi})


def probe_alpha_breakout_retest_v2(ctx):
    f = ctx.features
    ema20, atr_pips = f.get("ema20"), f.get("atr_pips")
    if None in (ema20, atr_pips): return None
    pip = pip_size(ctx.symbol)
    close = ctx.m5_close[-1]
    direction = "long" if close > ema20 else "short"
    prior_window = ctx.m5_close[-16:-4]
    if not prior_window: return None
    if direction == "long":
        broken_level = max(prior_window)
        if max(ctx.m5_high[-4:]) <= broken_level: return None
    else:
        broken_level = min(prior_window)
        if min(ctx.m5_low[-4:]) >= broken_level: return None
    if abs(close - broken_level) / pip > 0.2 * atr_pips: return None
    if direction == "long" and not _is_bull_bar(ctx): return None
    if direction == "short" and _is_bull_bar(ctx): return None
    return _build_candidate_multi(direction, close, broken_level, ctx, "alpha_breakout_retest_v2",
                                  {"broken_level": broken_level})


def probe_alpha_extended_fade_v2(ctx):
    f = ctx.features
    rsi, ema20 = f.get("rsi"), f.get("ema20")
    if None in (rsi, ema20): return None
    if len(ctx.m5_high) < 5: return None
    close = ctx.m5_close[-1]
    if rsi >= 65 and close > ema20:
        direction = "short"; struct_ref = max(ctx.m5_high[-5:])
    elif rsi <= 35 and close < ema20:
        direction = "long"; struct_ref = min(ctx.m5_low[-5:])
    else: return None
    body = _bar_body(ctx)
    if direction == "short":
        upper_wick = ctx.m5_high[-1] - max(ctx.m5_open[-1], ctx.m5_close[-1])
        if upper_wick < body: return None
    else:
        lower_wick = min(ctx.m5_open[-1], ctx.m5_close[-1]) - ctx.m5_low[-1]
        if lower_wick < body: return None
    return _build_candidate_multi(direction, close, struct_ref, ctx, "alpha_extended_fade_v2", {"rsi": rsi})


def probe_echo_box_fade_v2(ctx):
    f = ctx.features
    bb_pos = f.get("bb_position")
    if bb_pos is None: return None
    if bb_pos <= 0.0299: direction = "long"
    elif bb_pos >= 0.8708: direction = "short"
    else: return None
    body = _bar_body(ctx)
    if direction == "long":
        lower_wick = min(ctx.m5_open[-1], ctx.m5_close[-1]) - ctx.m5_low[-1]
        if lower_wick < body: return None
    else:
        upper_wick = ctx.m5_high[-1] - max(ctx.m5_open[-1], ctx.m5_close[-1])
        if upper_wick < body: return None
    close = ctx.m5_close[-1]
    struct_ref = min(ctx.m5_low[-3:]) if direction == "long" else max(ctx.m5_high[-3:])
    return _build_candidate_multi(direction, close, struct_ref, ctx, "echo_box_fade_v2", {"bb_position": bb_pos})


def probe_echo_failed_breakout_v2(ctx):
    f = ctx.features
    bb_upper, bb_lower, atr_pips = f.get("bb_upper"), f.get("bb_lower"), f.get("atr_pips")
    if None in (bb_upper, bb_lower, atr_pips): return None
    pip = pip_size(ctx.symbol)
    prev_low, prev_high, prev_close = ctx.m5_low[-2], ctx.m5_high[-2], ctx.m5_close[-2]
    if prev_low < bb_lower and prev_close > bb_lower and (bb_lower - prev_low) / pip >= 1.0 * atr_pips:
        direction = "long"; struct_ref = prev_low
        pierce = (bb_lower - prev_low) / pip / max(atr_pips, 1e-9)
    elif prev_high > bb_upper and prev_close < bb_upper and (prev_high - bb_upper) / pip >= 1.0 * atr_pips:
        direction = "short"; struct_ref = prev_high
        pierce = (prev_high - bb_upper) / pip / max(atr_pips, 1e-9)
    else: return None
    if direction == "long" and not _is_bull_bar(ctx): return None
    if direction == "short" and _is_bull_bar(ctx): return None
    close = ctx.m5_close[-1]
    return _build_candidate_multi(direction, close, struct_ref, ctx, "echo_failed_breakout_v2",
                                  {"pierce_size_atr_x": pierce})


def probe_charlie_pullback_continuation_v2(ctx):
    f = ctx.features
    ema20, atr_pips, rsi = f.get("ema20"), f.get("atr_pips"), f.get("rsi")
    if None in (ema20, atr_pips, rsi): return None
    if len(ctx.m5_close) < 5: return None
    pip = pip_size(ctx.symbol)
    close = ctx.m5_close[-1]
    direction = "long" if close > ema20 else "short"
    if direction == "long":
        if not (ctx.m5_low[-2] < ctx.m5_low[-3] and ctx.m5_low[-3] < ctx.m5_low[-4]): return None
        if not (close > ctx.m5_close[-2]): return None
    else:
        if not (ctx.m5_high[-2] > ctx.m5_high[-3] and ctx.m5_high[-3] > ctx.m5_high[-4]): return None
        if not (close < ctx.m5_close[-2]): return None
    if abs(close - ema20) / pip > 0.5 * atr_pips: return None
    if rsi <= 35 or rsi >= 65: return None
    struct_ref = min(ctx.m5_low[-5:]) if direction == "long" else max(ctx.m5_high[-5:])
    return _build_candidate_multi(direction, close, struct_ref, ctx, "charlie_pullback_continuation_v2",
                                  {"rsi": rsi})


def probe_charlie_compression_breakout(ctx):
    if len(ctx.m5_high) < 26: return None
    trs = []
    for i in range(1, len(ctx.m5_high)):
        tr = max(ctx.m5_high[i] - ctx.m5_low[i],
                 abs(ctx.m5_high[i] - ctx.m5_close[i - 1]),
                 abs(ctx.m5_low[i] - ctx.m5_close[i - 1]))
        trs.append(tr)
    if len(trs) < 25: return None
    last_6_tr = sum(trs[-6:]) / 6.0
    prior_tr = sum(trs[:-6]) / max(len(trs[:-6]), 1)
    if prior_tr <= 0 or last_6_tr >= 0.85 * prior_tr: return None
    prior_6_high = max(ctx.m5_high[-7:-1])
    prior_6_low = min(ctx.m5_low[-7:-1])
    cur_high, cur_low = ctx.m5_high[-1], ctx.m5_low[-1]
    if cur_high > prior_6_high and _is_bull_bar(ctx):
        direction = "long"; struct_ref = prior_6_low
    elif cur_low < prior_6_low and not _is_bull_bar(ctx):
        direction = "short"; struct_ref = prior_6_high
    else: return None
    close = ctx.m5_close[-1]
    return _build_candidate_multi(direction, close, struct_ref, ctx, "charlie_compression_breakout",
                                  {"tr_compression_ratio": last_6_tr / prior_tr})


def probe_bravo_failed_momentum(ctx):
    if len(ctx.m5_high) < 22: return None
    prev_range = ctx.m5_high[-2] - ctx.m5_low[-2]
    mean_20_range = sum(ctx.m5_high[-22 + i] - ctx.m5_low[-22 + i] for i in range(20)) / 20.0
    if mean_20_range <= 0 or prev_range < 1.5 * mean_20_range: return None
    cur_close = ctx.m5_close[-1]
    if not (ctx.m5_low[-2] < cur_close < ctx.m5_high[-2]): return None
    prev_dir_up = ctx.m5_close[-2] > ctx.m5_open[-2]
    cur_dir_up = ctx.m5_close[-1] > ctx.m5_open[-1]
    if prev_dir_up == cur_dir_up: return None
    direction = "long" if not prev_dir_up else "short"
    struct_ref = ctx.m5_low[-2] if direction == "long" else ctx.m5_high[-2]
    return _build_candidate_multi(direction, cur_close, struct_ref, ctx, "bravo_failed_momentum",
                                  {"prev_range_x_mean20": prev_range / mean_20_range})


def probe_bravo_expansion_continuation(ctx):
    cur_range = _bar_range(ctx)
    mean_20 = _mean_range(ctx, 20)
    if mean_20 <= 0 or cur_range < 1.3 * mean_20: return None
    direction = "long" if _is_bull_bar(ctx) else "short"
    if direction == "long":
        if (ctx.m5_close[-1] - ctx.m5_low[-1]) < 0.67 * cur_range: return None
        struct_ref = ctx.m5_low[-1]
    else:
        if (ctx.m5_high[-1] - ctx.m5_close[-1]) < 0.67 * cur_range: return None
        struct_ref = ctx.m5_high[-1]
    close = ctx.m5_close[-1]
    return _build_candidate_multi(direction, close, struct_ref, ctx, "bravo_expansion_continuation",
                                  {"range_x_mean20": cur_range / mean_20})


def probe_delta_tag_and_go_v2(ctx):
    if len(ctx.m5_high) < 14: return None
    twelve_high = max(ctx.m5_high[-14:-2])
    twelve_low = min(ctx.m5_low[-14:-2])
    prev_high, prev_low, prev_close = ctx.m5_high[-2], ctx.m5_low[-2], ctx.m5_close[-2]
    if prev_high > twelve_high and prev_close > twelve_high:
        direction = "long"; struct_ref = twelve_high
    elif prev_low < twelve_low and prev_close < twelve_low:
        direction = "short"; struct_ref = twelve_low
    else: return None
    if direction == "long" and not _is_bull_bar(ctx): return None
    if direction == "short" and _is_bull_bar(ctx): return None
    close = ctx.m5_close[-1]
    return _build_candidate_multi(direction, close, struct_ref, ctx, "delta_tag_and_go_v2",
                                  {"twelve_high": twelve_high, "twelve_low": twelve_low})


# ---------------------------------------------------------------------------
# Probe registry — name → (probe_fn, family, sentinel_regime, target_hypothesis)
# ---------------------------------------------------------------------------

PROBE_REGISTRY: dict[str, dict[str, Any]] = {
    "alpha_pullback_v2":               {"fn": probe_alpha_pullback_v2,           "family": "dbb_trend", "sentinel": "Alpha-fresh",     "target": 2.0},
    "alpha_breakout_retest_v2":        {"fn": probe_alpha_breakout_retest_v2,    "family": "direct",    "sentinel": "Alpha-fresh",     "target": 1.5},
    "alpha_extended_fade_v2":          {"fn": probe_alpha_extended_fade_v2,      "family": "reversal",  "sentinel": "Alpha-extended",  "target": 2.0},
    "echo_box_fade_v2":                {"fn": probe_echo_box_fade_v2,            "family": "reversal",  "sentinel": "Echo-tight",      "target": 2.0},
    "echo_failed_breakout_v2":         {"fn": probe_echo_failed_breakout_v2,     "family": "reversal",  "sentinel": "Echo-explosive",  "target": 2.0},
    "charlie_pullback_continuation_v2":{"fn": probe_charlie_pullback_continuation_v2,"family":"dbb_trend","sentinel":"Charlie",         "target": 2.0},
    "charlie_compression_breakout":    {"fn": probe_charlie_compression_breakout,"family": "direct",    "sentinel": "Charlie",         "target": 1.5},
    "bravo_failed_momentum":           {"fn": probe_bravo_failed_momentum,       "family": "reversal",  "sentinel": "Bravo",           "target": 2.0},
    "bravo_expansion_continuation":    {"fn": probe_bravo_expansion_continuation,"family": "dbb_trend", "sentinel": "Bravo",           "target": 1.5},
    "delta_tag_and_go_v2":             {"fn": probe_delta_tag_and_go_v2,         "family": "direct",    "sentinel": "Delta",           "target": 1.5},
}


# ---------------------------------------------------------------------------
# V3 strategy wrapper
# ---------------------------------------------------------------------------

_MIN_M5_BARS = 26  # max lookback used by any probe


def _build_probe_ctx(symbol: str, ctx: SymbolContext, sentinel_regime: str,
                     target: float) -> ProbeContext | None:
    """Extract M5 OHLC + V3 features into a ProbeContext shape."""
    m5 = ctx.snapshot.candles.get("5M")
    if m5 is None or len(m5) < _MIN_M5_BARS:
        return None
    try:
        o = m5["open"].astype(float).tolist()
        h = m5["high"].astype(float).tolist()
        lo = m5["low"].astype(float).tolist()
        c = m5["close"].astype(float).tolist()
    except Exception:
        return None
    pip = pip_size(symbol)
    feats: dict[str, Any] = {}
    ema = ctx.features.get("ema")
    if ema is not None:
        feats["ema20"] = (ema.values or {}).get("ema20")
    atr = ctx.features.get("atr")
    if atr is not None:
        atr_val = (atr.values or {}).get("atr")
        if atr_val is not None:
            feats["atr_pips"] = float(atr_val) / pip
    rsi = ctx.features.get("rsi")
    if rsi is not None:
        feats["rsi"] = (rsi.values or {}).get("rsi")
    bb = ctx.features.get("bollinger")
    if bb is not None:
        bbv = bb.values or {}
        feats["bb_position"] = bbv.get("bb_position")
        feats["bb_upper"] = bbv.get("upper_a")
        feats["bb_lower"] = bbv.get("lower_a")
    zone = ctx.features.get("zone_detector")
    if zone is not None:
        zm = (zone.values or {}).get("zone_map")
        sr = getattr(zm, "session_range", None) if zm is not None else None
        if sr is not None:
            feats["pdh"] = getattr(sr, "PDH", None)
            feats["pdl"] = getattr(sr, "PDL", None)
    bb_state = None
    bb_cls = ctx.classifications.get("bb_state")
    if bb_cls is not None:
        bb_state = getattr(bb_cls, "label", None)
    spread_pips = float(ctx.metadata.get("spread_pips", 0.0)) if ctx.metadata else 0.0
    return ProbeContext(
        ts=datetime.now(timezone.utc), symbol=symbol, spread_pips=spread_pips,
        m5_open=o, m5_high=h, m5_low=lo, m5_close=c,
        features=feats, regime_label=sentinel_regime,
        r_targets=[float(target)], bb_state=bb_state,
    )


class ProbeStrategy:
    """Single-probe V3 strategy wrapper.

    Implements StrategyModule Protocol. One instance per probe; the bootstrap
    registers all 10 with `enabled=False` unless explicitly enabled in config.
    """

    def __init__(self, probe_name: str, config: dict | None = None):
        entry = PROBE_REGISTRY.get(probe_name)
        if entry is None:
            raise ValueError(f"unknown probe: {probe_name}")
        cfg = config or {}
        self.name = probe_name
        self._fn: Callable = entry["fn"]
        self._family: str = entry["family"]
        self._sentinel: str = entry["sentinel"]
        self._target: float = float(cfg.get("r_target", entry["target"]))
        self.enabled = bool(cfg.get("enabled", False))

    def eligible(self, ctx: SymbolContext) -> bool:
        if not self.enabled:
            return False
        m5 = ctx.snapshot.candles.get("5M")
        return m5 is not None and len(m5) >= _MIN_M5_BARS

    def evaluate(self, ctx: SymbolContext) -> TradeCandidate | None:
        if not self.enabled:
            return None
        pc = _build_probe_ctx(ctx.symbol, ctx, self._sentinel, self._target)
        if pc is None:
            return None
        try:
            cand = self._fn(pc)
        except Exception as e:
            log.warning("probe %s raised: %s", self.name, e)
            return None
        if cand is None:
            return None

        entry = float(cand.entry_price)
        stop = float(cand.stop_price)
        if stop == entry:
            return None
        risk = abs(entry - stop)
        target_r = self._target
        tp = entry + risk * target_r if cand.direction == "long" else entry - risk * target_r
        direction = TradeDirection.LONG if cand.direction == "long" else TradeDirection.SHORT
        return TradeCandidate(
            symbol=ctx.symbol,
            direction=direction,
            strategy=self.name,
            entry_price=entry,
            stop_price=stop,
            take_profit=tp,
            size=0.0,
            risk_reward=target_r,
            score=1.0,
            metadata={
                "entry_type": "PROBE",
                "probe_name": self.name,
                "probe_family": self._family,
                "probe_sentinel_regime": self._sentinel,
                "structure_ref_price": cand.structure_ref_price,
                "stop_pips": (cand.notes or {}).get("stop_pips"),
                "risk_points": risk,
                "strategy_family": self._family,
                "management_profile": "default",
                **(cand.notes or {}),
            },
            created_at=datetime.now(timezone.utc),
        )


def build_all_probe_strategies(config: dict | None = None) -> list[ProbeStrategy]:
    """Return one ProbeStrategy per registered probe.

    `config` shape:
        config["<probe_name>"] = {"enabled": bool, "r_target": float}
    Missing entries → disabled.
    """
    cfg = config or {}
    out: list[ProbeStrategy] = []
    for name in PROBE_REGISTRY:
        out.append(ProbeStrategy(name, cfg.get(name, {})))
    return out


__all__ = [
    "ProbeStrategy",
    "PROBE_REGISTRY",
    "build_all_probe_strategies",
]
