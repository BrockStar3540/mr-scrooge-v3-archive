"""Session Breakout Continuation — Opening Range break + retest probe.

Defines a per-session Opening Range (OR) at the start of high-liquidity
sessions (London open, NY open). After the OR is established, the strategy
looks for a BREAK + RETEST entry:

  Long  : price has traded above OR_high, then pulls back to OR_high (+/- buffer)
          without printing a new low below OR_low -> long entry on the retest.
  Short : mirror -- price has traded below OR_low, then pulls back to OR_low
          (+/- buffer) without breaking back above OR_high -> short entry on retest.

Only emits during the liquid windows (london_open, london, ny_open, ny_mid
per the session_bucket classifier).

Emits TradeCandidate with:
    strategy_family = 'session_breakout'
    strategy        = 'SB_OR_breakout_long' | 'SB_OR_breakout_short'

Lives under strategies/research_strategies/ -- not routed by default. Bootstrap
must import + register explicitly to enable.
"""
from __future__ import annotations

import logging
from datetime import datetime, time, timezone

from scrooge_v3.core.types import SymbolContext, TradeCandidate, TradeDirection

log = logging.getLogger("scrooge_v3.strategy.session_breakout")


# ---------------------------------------------------------------------------
# Session OR windows (UTC). For each session label we record:
#   session_start_h/m  -- when the session begins
#   or_end_h/m         -- OR ends (bars in [session_start, or_end) are aggregated)
#   session_end_h/m    -- session window cutoff for entries
# ---------------------------------------------------------------------------
_OR_WINDOWS: dict[str, dict[str, int]] = {
    # London open: 07:00-08:00 UTC, OR = 07:00-07:30
    "london_open": {
        "session_start_h": 7,  "session_start_m": 0,
        "or_end_h":        7,  "or_end_m":        30,
        "session_end_h":   8,  "session_end_m":   0,
    },
    # London full session -- carry-forward the London-open OR so retests later
    # in the session can still fire.
    "london": {
        "session_start_h": 7,  "session_start_m": 0,
        "or_end_h":        7,  "or_end_m":        30,
        "session_end_h":   12, "session_end_m":   0,
    },
    # NY open: 12:00-13:00 UTC, OR = 12:00-12:30
    "ny_open": {
        "session_start_h": 12, "session_start_m": 0,
        "or_end_h":        12, "or_end_m":        30,
        "session_end_h":   13, "session_end_m":   0,
    },
    # NY mid -- carry the NY-open OR through the ny_mid window.
    "ny_mid": {
        "session_start_h": 12, "session_start_m": 0,
        "or_end_h":        12, "or_end_m":        30,
        "session_end_h":   17, "session_end_m":   0,
    },
}

_ELIGIBLE_SESSIONS = tuple(_OR_WINDOWS.keys())


class SessionBreakoutStrategy:
    """Opening-Range break + retest continuation. Long & short variants.

    Implements StrategyModule Protocol (`name`, `eligible`, `evaluate`).
    Stateless -- recomputes OR on each evaluate() call by scanning the M5 bars
    of the current UTC day for bars inside the OR window of the active
    session.
    """

    name = "session_breakout"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.enabled = config.get("enabled", True)
        # Retest tolerance, in pips, applied symmetrically around the OR boundary.
        self.retest_buffer_pips = config.get("retest_buffer_pips", 1.5)
        # Spread cap: reject when spread > spread_cap_frac * stop_distance.
        self.spread_cap_frac = config.get("spread_cap_frac", 0.15)
        # Minimum projected pips beyond entry before first structure level.
        self.min_projected_pips = config.get("min_projected_pips", 7.0)
        # Stop / target floors (pips).
        self.sl_pip_floor = config.get("sl_pip_floor", 10.0)
        self.tp_pip_floor = config.get("tp_pip_floor", 12.0)
        # Default SL = sl_or_frac * OR_range. Default TP = OR_range projected.
        self.sl_or_frac = config.get("sl_or_frac", 0.5)
        # Minimum required bars inside the OR window to consider the OR valid.
        self.min_or_bars = config.get("min_or_bars", 3)
        # Score emitted on candidates (router consumers may rescore).
        self.fixed_score = config.get("fixed_score", 28)
        log.info(
            "[STRATEGY:session_breakout] init enabled=%s retest_buf_pips=%.2f "
            "spread_cap_frac=%.2f min_proj_pips=%.1f",
            self.enabled, self.retest_buffer_pips,
            self.spread_cap_frac, self.min_projected_pips,
        )

    # -----------------------------------------------------------------------
    # Module interface
    # -----------------------------------------------------------------------
    def eligible(self, ctx: SymbolContext) -> bool:
        if not self.enabled:
            return False
        sb = ctx.classifications.get("session_bucket")
        if sb is None or sb.label not in _ELIGIBLE_SESSIONS:
            return False
        bars = ctx.snapshot.candles.get("5M")
        if bars is None or len(bars) < 12:
            return False
        return True

    def evaluate(self, ctx: SymbolContext) -> TradeCandidate | None:
        try:
            return self._evaluate_inner(ctx)
        except Exception as e:  # noqa: BLE001 -- strategies must never crash
            log.warning(
                "[STRATEGY:session_breakout] evaluate raised on %s: %s",
                ctx.symbol, e,
            )
            return None

    # -----------------------------------------------------------------------
    # Core logic
    # -----------------------------------------------------------------------
    def _evaluate_inner(self, ctx: SymbolContext) -> TradeCandidate | None:
        sb = ctx.classifications.get("session_bucket")
        if sb is None or sb.label not in _ELIGIBLE_SESSIONS:
            return None
        window = _OR_WINDOWS[sb.label]

        bars = ctx.snapshot.candles.get("5M")
        if bars is None or len(bars) < 12:
            return None

        try:
            idx = bars.index
            highs = bars["high"].astype(float).values
            lows = bars["low"].astype(float).values
            closes = bars["close"].astype(float).values
        except Exception:  # noqa: BLE001
            return None

        now = ctx.snapshot.timestamp
        if now is None:
            return None
        if now.tzinfo is None:
            now = now.replace(tzinfo=timezone.utc)

        # Build OR window boundaries on the current UTC day.
        day = now.date()
        or_start = datetime.combine(
            day, time(window["session_start_h"], window["session_start_m"]),
            tzinfo=timezone.utc,
        )
        or_end = datetime.combine(
            day, time(window["or_end_h"], window["or_end_m"]),
            tzinfo=timezone.utc,
        )
        sess_end = datetime.combine(
            day, time(window["session_end_h"], window["session_end_m"]),
            tzinfo=timezone.utc,
        )

        # OR must be complete before we can scan for break/retest.
        if now < or_end:
            return None
        # And we must still be inside the entry window for this session.
        if now > sess_end:
            return None

        # Collect bar indices within the OR window and after-OR (post-OR, current).
        or_idx: list[int] = []
        post_or_idx: list[int] = []
        for i in range(len(idx)):
            ts = self._coerce_utc(idx[i])
            if ts is None:
                continue
            if or_start <= ts < or_end:
                or_idx.append(i)
            elif or_end <= ts <= now:
                post_or_idx.append(i)

        if len(or_idx) < self.min_or_bars or len(post_or_idx) < 2:
            return None

        or_high = max(highs[i] for i in or_idx)
        or_low = min(lows[i] for i in or_idx)
        or_range = or_high - or_low
        if or_range <= 0:
            return None

        pip = 0.01 if "JPY" in ctx.symbol else 0.0001
        retest_buf = self.retest_buffer_pips * pip

        current_close = closes[-1]
        current_low = lows[-1]
        current_high = highs[-1]

        post_or_highs = [highs[i] for i in post_or_idx]
        post_or_lows = [lows[i] for i in post_or_idx]
        post_or_closes = [closes[i] for i in post_or_idx]

        broke_above = max(post_or_highs) > or_high
        broke_below = min(post_or_lows) < or_low

        candidate: TradeCandidate | None = None

        # -------- LONG: break above, retest at OR_high, holds above OR_low --
        if broke_above and not broke_below:
            retested = (
                (or_high - retest_buf) <= current_low <= (or_high + retest_buf)
                and current_close > or_low
            )
            if not retested:
                # Accept a recent pullback (last 4 post-OR bars) + current close
                # reclaiming above OR_high.
                k0 = max(0, len(post_or_lows) - 4)
                pulled_back = any(
                    (or_high - retest_buf) <= post_or_lows[k] <= (or_high + retest_buf)
                    for k in range(k0, len(post_or_lows))
                )
                pulled_back_no_break = min(post_or_closes[k0:]) > or_low
                retested = (
                    pulled_back
                    and pulled_back_no_break
                    and current_close > or_high
                )

            if retested:
                candidate = self._build_long(
                    ctx, current_close, or_high, or_low, or_range, pip,
                )

        # -------- SHORT: break below, retest at OR_low, holds below OR_high --
        elif broke_below and not broke_above:
            retested = (
                (or_low - retest_buf) <= current_high <= (or_low + retest_buf)
                and current_close < or_high
            )
            if not retested:
                k0 = max(0, len(post_or_highs) - 4)
                pulled_back = any(
                    (or_low - retest_buf) <= post_or_highs[k] <= (or_low + retest_buf)
                    for k in range(k0, len(post_or_highs))
                )
                pulled_back_no_break = max(post_or_closes[k0:]) < or_high
                retested = (
                    pulled_back
                    and pulled_back_no_break
                    and current_close < or_low
                )

            if retested:
                candidate = self._build_short(
                    ctx, current_close, or_high, or_low, or_range, pip,
                )

        if candidate is None:
            return None

        # Spread gate.
        stop_distance_pips = abs(candidate.entry_price - candidate.stop_price) / pip
        spread = getattr(ctx.snapshot, "spread", 0.0) or 0.0
        spread_pips = spread / pip
        if stop_distance_pips > 0 and spread_pips > self.spread_cap_frac * stop_distance_pips:
            log.debug(
                "[STRATEGY:session_breakout] %s spread_gate spread_pips=%.2f "
                "stop_pips=%.2f cap=%.2f", ctx.symbol, spread_pips,
                stop_distance_pips, self.spread_cap_frac * stop_distance_pips,
            )
            return None

        # Projection-to-structure gate.
        projected_pips = candidate.metadata.get("projected_tp_pips", 0.0)
        if projected_pips < self.min_projected_pips:
            log.debug(
                "[STRATEGY:session_breakout] %s projection_gate proj_pips=%.2f "
                "min=%.2f", ctx.symbol, projected_pips, self.min_projected_pips,
            )
            return None

        log.info(
            "[STRATEGY:session_breakout] %s symbol=%s dir=%s entry=%.5f "
            "stop=%.5f tp=%.5f proj_pips=%.1f or_range_pips=%.1f session=%s",
            candidate.strategy, ctx.symbol, candidate.direction.value,
            candidate.entry_price, candidate.stop_price, candidate.take_profit or 0.0,
            projected_pips, or_range / pip, sb.label,
        )
        return candidate

    # -----------------------------------------------------------------------
    # Builders
    # -----------------------------------------------------------------------
    def _build_long(
        self,
        ctx: SymbolContext,
        entry: float,
        or_high: float,
        or_low: float,
        or_range: float,
        pip: float,
    ) -> TradeCandidate:
        sl_floor = self.sl_pip_floor * pip
        tp_floor = self.tp_pip_floor * pip
        sl_distance = max(self.sl_or_frac * or_range, sl_floor)
        tp_distance = max(or_range, tp_floor)
        stop_price = entry - sl_distance
        take_profit = entry + tp_distance
        projected_pips = tp_distance / pip
        risk = entry - stop_price
        reward = take_profit - entry
        rr = (reward / risk) if risk > 0 else 0.0
        return TradeCandidate(
            symbol=ctx.symbol,
            direction=TradeDirection.LONG,
            strategy="SB_OR_breakout_long",
            entry_price=entry,
            stop_price=stop_price,
            take_profit=take_profit,
            size=0.0,
            risk_reward=rr,
            score=self.fixed_score,
            metadata={
                "entry_type": "SESSION_BREAKOUT_RETEST",
                "strategy_family": "session_breakout",
                "or_high": or_high,
                "or_low": or_low,
                "or_range_pips": or_range / pip,
                "projected_tp_pips": projected_pips,
                "risk_points": risk,
                "reward_points": reward,
            },
            created_at=datetime.now(timezone.utc),
        )

    def _build_short(
        self,
        ctx: SymbolContext,
        entry: float,
        or_high: float,
        or_low: float,
        or_range: float,
        pip: float,
    ) -> TradeCandidate:
        sl_floor = self.sl_pip_floor * pip
        tp_floor = self.tp_pip_floor * pip
        sl_distance = max(self.sl_or_frac * or_range, sl_floor)
        tp_distance = max(or_range, tp_floor)
        stop_price = entry + sl_distance
        take_profit = entry - tp_distance
        projected_pips = tp_distance / pip
        risk = stop_price - entry
        reward = entry - take_profit
        rr = (reward / risk) if risk > 0 else 0.0
        return TradeCandidate(
            symbol=ctx.symbol,
            direction=TradeDirection.SHORT,
            strategy="SB_OR_breakout_short",
            entry_price=entry,
            stop_price=stop_price,
            take_profit=take_profit,
            size=0.0,
            risk_reward=rr,
            score=self.fixed_score,
            metadata={
                "entry_type": "SESSION_BREAKOUT_RETEST",
                "strategy_family": "session_breakout",
                "or_high": or_high,
                "or_low": or_low,
                "or_range_pips": or_range / pip,
                "projected_tp_pips": projected_pips,
                "risk_points": risk,
                "reward_points": reward,
            },
            created_at=datetime.now(timezone.utc),
        )

    # -----------------------------------------------------------------------
    # Helpers
    # -----------------------------------------------------------------------
    @staticmethod
    def _coerce_utc(ts):
        """Coerce a bar-index value into a UTC-aware datetime, or None."""
        try:
            if hasattr(ts, "to_pydatetime"):
                dt = ts.to_pydatetime()
            elif isinstance(ts, datetime):
                dt = ts
            else:
                return None
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except Exception:  # noqa: BLE001
            return None


__all__ = ["SessionBreakoutStrategy"]
