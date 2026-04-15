"""Regime classifier -- evaluates market regime from multiple signals.

Ported from V2 RegimeSupervisor. In V3 this is a pure classifier:
it receives all needed data via SymbolContext rather than reaching
out to the coordinator or position manager.

Signals tracked:
  1. box_acceptance     -- closes holding outside PDH/PDL
  2. rejection_decay    -- recent wall touches (exponential decay, 8h half-life)
  3. expansion_pressure -- directional ATR expansion, session-adjusted thresholds
  4. qualified_failures -- gated setups hit SL recently
  5. breadth            -- correlated pairs showing same regime weakness
  6. quality_pressure   -- MFE/MAE follow-through from quality tracker
  7. bb_context         -- Bollinger Band state

Scoring (category-capped):
  - Market Structure (box, rejection, expansion, BB): cap -3
  - Performance (failures, quality): cap -3
  - Corroboration (breadth): cap -1
  Worst case: -7. Best case: +8.
"""

from __future__ import annotations

import logging
from collections import defaultdict, deque
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional

import pandas as pd

from scrooge_v3.core.types import ClassificationResult, SymbolContext

log = logging.getLogger("scrooge_v3.classifiers.regime")


# ---------------------------------------------------------------------------
# Regime state and scoring models
# ---------------------------------------------------------------------------

class RegimeState(Enum):
    NORMAL = "NORMAL"
    CAUTION = "CAUTION"
    RESTRICTED = "RESTRICTED"
    BLOCKED = "BLOCKED"


def classify_score(score: float) -> RegimeState:
    if score >= 0:
        return RegimeState.NORMAL
    if score >= -2:
        return RegimeState.CAUTION
    if score >= -4:
        return RegimeState.RESTRICTED
    return RegimeState.BLOCKED


@dataclass
class RegimeSignal:
    """One piece of evidence contributing to the regime score."""
    name: str
    score_delta: float
    detail: str


# ---------------------------------------------------------------------------
# Category-capped scoring
# ---------------------------------------------------------------------------

_SIGNAL_CATEGORY: dict[str, str] = {
    # Market Structure
    "box_acceptance_above": "market_structure",
    "box_acceptance_below": "market_structure",
    "box_probe_above": "market_structure",
    "box_probe_below": "market_structure",
    "box_contained": "market_structure",
    "rejection_failed": "market_structure",
    "rejection_weak": "market_structure",
    "rejection_clean": "market_structure",
    "expansion_pressure": "market_structure",
    "expansion_mild": "market_structure",
    "compression": "market_structure",
    "bb_breakout_up": "market_structure",
    "bb_breakout_down": "market_structure",
    "bb_rejection_short": "market_structure",
    "bb_rejection_long": "market_structure",
    # Performance
    "qualified_failures": "performance",
    "qualified_failures_mixed": "performance",
    "single_failure": "performance",
    "clean_performance": "performance",
    "quality_pressure_weak": "performance",
    "quality_pressure_strong": "performance",
    # Corroboration
    "breadth_negative": "corroboration",
    "breadth_positive": "corroboration",
}

_CATEGORY_NEG_CAP: dict[str, float] = {
    "market_structure": -3,
    "performance": -3,
    "corroboration": -1,
}


def _compute_capped_score(
    signals: list[RegimeSignal],
) -> tuple[float, float]:
    """
    Sum signal deltas with per-category negative caps.
    Positive contributions are uncapped.
    Returns (total_score, direct_score_excluding_breadth).
    """
    cat_neg: dict[str, float] = defaultdict(float)
    cat_pos: dict[str, float] = defaultdict(float)

    for s in signals:
        cat = _SIGNAL_CATEGORY.get(s.name, "uncategorized")
        if s.score_delta < 0:
            cat_neg[cat] += s.score_delta
        else:
            cat_pos[cat] += s.score_delta

    # Apply negative caps per category
    total_neg = sum(
        max(v, _CATEGORY_NEG_CAP.get(cat, float("-inf")))
        for cat, v in cat_neg.items()
    )
    total_pos = sum(cat_pos.values())
    total_score = total_neg + total_pos

    # Direct score = everything except corroboration (breadth)
    breadth_neg = max(
        cat_neg.get("corroboration", 0.0),
        _CATEGORY_NEG_CAP.get("corroboration", float("-inf")),
    )
    breadth_pos = cat_pos.get("corroboration", 0.0)
    direct_score = total_score - breadth_neg - breadth_pos

    return total_score, direct_score


# ---------------------------------------------------------------------------
# Regime classifier
# ---------------------------------------------------------------------------

class RegimeClassifier:
    """
    Evaluates market regime from multiple signals.

    All data comes via SymbolContext:
      - ctx.features["zone_detector"] for zone_map / session range
      - ctx.features["bollinger"] (via bb_classifier classification)
      - ctx.classifications["bb_classifier"] for BB state
      - ctx.state for bars, outcomes, direction, quality pressure, peer assessments

    Implements ClassifierModule protocol.
    """

    name: str = "regime"

    # How many recent candles to examine for each signal
    _ACCEPTANCE_LOOKBACK = 24
    _DECAY_LOOKBACK = 24
    _EXPANSION_LOOKBACK = 12
    _FAILURE_WINDOW_HOURS = 6
    _DECAY_HALF_LIFE_HOURS = 8.0
    _MAX_BREADTH_PEERS = 4

    # Full universe -- majors + crosses (ordered by correlation strength)
    _CORRELATION_BLOCKS: dict[str, list[str]] = {
        "EUR_USD": ["GBP_USD", "USD_CHF", "EUR_JPY", "EUR_CAD"],
        "GBP_USD": ["EUR_USD", "USD_CHF", "GBP_CAD"],
        "USD_CAD": ["CAD_JPY", "EUR_CAD", "GBP_CAD"],
        "USD_CHF": ["EUR_USD", "GBP_USD"],
        "EUR_CAD": ["EUR_USD", "USD_CAD", "GBP_CAD"],
        "GBP_CAD": ["GBP_USD", "USD_CAD", "EUR_CAD"],
        "AUD_USD": ["AUD_NZD", "AUD_CAD", "AUD_JPY", "NZD_USD"],
        "NZD_USD": ["AUD_USD", "AUD_NZD", "NZD_JPY"],
        "AUD_NZD": ["AUD_USD", "NZD_USD", "AUD_JPY", "NZD_JPY"],
        "AUD_CAD": ["AUD_USD", "AUD_JPY"],
        "USD_JPY": ["EUR_JPY", "GBP_JPY", "CAD_JPY", "CHF_JPY", "AUD_JPY"],
        "EUR_JPY": ["USD_JPY", "GBP_JPY", "CAD_JPY", "CHF_JPY", "EUR_USD"],
        "GBP_JPY": ["USD_JPY", "EUR_JPY", "CAD_JPY", "CHF_JPY"],
        "CAD_JPY": ["USD_JPY", "EUR_JPY", "GBP_JPY", "CHF_JPY", "USD_CAD"],
        "CHF_JPY": ["USD_JPY", "EUR_JPY", "GBP_JPY", "CAD_JPY"],
        "AUD_JPY": ["AUD_USD", "AUD_NZD", "USD_JPY", "EUR_JPY", "GBP_JPY", "CAD_JPY", "CHF_JPY"],
        "NZD_JPY": ["NZD_USD", "AUD_NZD", "USD_JPY"],
    }

    def __init__(self, config: dict | None = None):
        config = config or {}
        # Per-symbol: deque of recent qualified trade outcomes
        self._outcomes: dict[str, deque] = defaultdict(lambda: deque(maxlen=10))
        # Per-symbol: last assessment direct_score (for breadth cross-check)
        self._last_direct_scores: dict[str, float] = {}

    def classify(self, ctx: SymbolContext) -> ClassificationResult:
        symbol = ctx.symbol

        # Extract data from context
        zone_map = self._get_zone_map(ctx)
        bars_5m: pd.DataFrame | None = ctx.snapshot.candles.get("5m")
        bars_1h: pd.DataFrame | None = ctx.snapshot.candles.get("1H")
        direction: str | None = ctx.state.get("direction")
        quality_pressure = ctx.state.get("quality_pressure")

        # Ingest any new outcomes passed in state
        new_outcomes = ctx.state.get("regime_outcomes", [])
        for outcome in new_outcomes:
            self._outcomes[symbol].append(outcome)

        # Evaluate all signals
        signals: list[RegimeSignal] = []

        signals.extend(self._check_box_acceptance(symbol, zone_map, bars_5m, direction))
        signals.extend(self._check_rejection_decay(symbol, zone_map, bars_1h, direction))
        signals.extend(self._check_expansion_pressure(symbol, bars_5m, zone_map))
        signals.extend(self._check_qualified_failures(symbol))
        signals.extend(self._check_breadth(symbol))
        signals.extend(self._check_quality_pressure(symbol, quality_pressure))
        signals.extend(self._check_bb_context(ctx))

        score, direct_score = _compute_capped_score(signals)
        state = classify_score(score)

        # Cache direct score for breadth
        self._last_direct_scores[symbol] = direct_score

        return ClassificationResult(
            name=self.name,
            label=state.value,
            confidence=abs(score),
            metadata={
                "regime_state": state.value,
                "score": score,
                "direct_score": direct_score,
                "signals": [
                    {"name": s.name, "delta": s.score_delta, "detail": s.detail}
                    for s in signals
                ],
                "would_have_intervened": state != RegimeState.NORMAL,
            },
        )

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _get_zone_map(ctx: SymbolContext):
        zd = ctx.features.get("zone_detector")
        if zd is None or not zd.values:
            return None
        return zd.values.get("zone_map")

    def record_outcome(
        self,
        trade_id: str,
        symbol: str,
        pnl: float,
        hit_sl: bool,
        entry_time: str,
    ) -> None:
        """Called when a trade closes to feed the qualified_failures signal."""
        self._outcomes[symbol].append({
            "trade_id": trade_id,
            "symbol": symbol,
            "hit_sl": hit_sl,
            "pnl": pnl,
            "entry_time": entry_time,
            "closed_at": datetime.now(timezone.utc).isoformat(),
        })

    # ------------------------------------------------------------------
    # Signal 1: Box Acceptance
    # ------------------------------------------------------------------

    def _check_box_acceptance(
        self,
        symbol: str,
        zone_map,
        bars_5m: pd.DataFrame | None,
        direction: str | None = None,
    ) -> list[RegimeSignal]:
        """Is price holding outside PDH/PDL?"""
        signals: list[RegimeSignal] = []
        if zone_map is None or bars_5m is None or len(bars_5m) < self._ACCEPTANCE_LOOKBACK:
            return signals

        pdh = zone_map.session_range.PDH
        pdl = zone_map.session_range.PDL
        recent = bars_5m.iloc[-self._ACCEPTANCE_LOOKBACK:]
        closes = recent["close"].values

        # Count consecutive closes above PDH
        above_streak = 0
        for c in reversed(closes):
            if c > pdh:
                above_streak += 1
            else:
                break

        # Count consecutive closes below PDL
        below_streak = 0
        for c in reversed(closes):
            if c < pdl:
                below_streak += 1
            else:
                break

        if above_streak >= 2:
            signals.append(RegimeSignal(
                name="box_acceptance_above",
                score_delta=-2,
                detail=(
                    f"{above_streak} consecutive closes above PDH {pdh:.5f} -- "
                    f"{'shorting back (aligned, structural penalty kept)' if direction == 'short' else 'price holding outside range'}"
                ),
            ))
        elif above_streak == 1:
            signals.append(RegimeSignal(
                name="box_probe_above",
                score_delta=-1,
                detail=f"1 close above PDH {pdh:.5f} -- watching for acceptance",
            ))

        if below_streak >= 2:
            signals.append(RegimeSignal(
                name="box_acceptance_below",
                score_delta=-2,
                detail=(
                    f"{below_streak} consecutive closes below PDL {pdl:.5f} -- "
                    f"{'longing back (aligned, structural penalty kept)' if direction == 'long' else 'price holding outside range'}"
                ),
            ))
        elif below_streak == 1:
            signals.append(RegimeSignal(
                name="box_probe_below",
                score_delta=-1,
                detail=f"1 close below PDL {pdl:.5f} -- watching for acceptance",
            ))

        # Bonus: clean containment
        current = float(closes[-1])
        if pdl < current < pdh:
            outside_count = sum(1 for c in closes if c > pdh or c < pdl)
            if outside_count == 0:
                signals.append(RegimeSignal(
                    name="box_contained",
                    score_delta=+1,
                    detail=f"Price fully contained within range for last {self._ACCEPTANCE_LOOKBACK} candles",
                ))

        return signals

    # ------------------------------------------------------------------
    # Signal 2: Rejection Quality Decay
    # ------------------------------------------------------------------

    def _check_rejection_decay(
        self,
        symbol: str,
        zone_map,
        bars_1h: pd.DataFrame | None,
        direction: str | None = None,
    ) -> list[RegimeSignal]:
        """Have recent wall touches produced clean rejections or weak ones?"""
        signals: list[RegimeSignal] = []
        if zone_map is None or bars_1h is None or len(bars_1h) < self._DECAY_LOOKBACK:
            return signals

        pdh = zone_map.session_range.PDH
        pdl = zone_map.session_range.PDL
        box_range = zone_map.session_range.box_range
        if box_range <= 0:
            return signals

        proximity = box_range * 0.08
        recent = bars_1h.iloc[-self._DECAY_LOOKBACK:]

        clean_rejections = 0.0
        weak_rejections = 0.0
        failed_above = 0.0
        failed_below = 0.0

        n_bars = len(recent)
        for i, (_, bar) in enumerate(recent.iterrows()):
            high = float(bar["high"])
            low = float(bar["low"])
            close = float(bar["close"])

            age_hours = n_bars - 1 - i
            weight = 0.5 ** (age_hours / self._DECAY_HALF_LIFE_HOURS)

            if high >= pdh - proximity:
                if close < pdh - proximity:
                    clean_rejections += weight
                elif close < pdh:
                    weak_rejections += weight
                else:
                    failed_above += weight

            if low <= pdl + proximity:
                if close > pdl + proximity:
                    clean_rejections += weight
                elif close > pdl:
                    weak_rejections += weight
                else:
                    failed_below += weight

        failed_rejections = failed_above + failed_below
        total_touches = clean_rejections + weak_rejections + failed_rejections
        if total_touches == 0:
            return signals

        if failed_rejections >= 2:
            aligned = (
                (direction == "short" and failed_above > failed_below)
                or (direction == "long" and failed_below > failed_above)
            )
            delta = -1 if aligned else -2
            suffix = " (direction-aligned, reduced penalty)" if aligned else ""
            signals.append(RegimeSignal(
                name="rejection_failed",
                score_delta=delta,
                detail=(
                    f"{failed_rejections:.1f}w failed rejections at walls in last {self._DECAY_LOOKBACK}H -- "
                    f"wall not holding (clean={clean_rejections:.1f}w weak={weak_rejections:.1f}w "
                    f"above={failed_above:.1f}w below={failed_below:.1f}w){suffix}"
                ),
            ))
        elif weak_rejections >= 3 and clean_rejections == 0:
            signals.append(RegimeSignal(
                name="rejection_weak",
                score_delta=-1,
                detail=(
                    f"{weak_rejections:.1f}w weak rejections, 0 clean in last {self._DECAY_LOOKBACK}H -- "
                    f"reversal quality degrading"
                ),
            ))
        elif clean_rejections >= 2 and failed_rejections == 0:
            signals.append(RegimeSignal(
                name="rejection_clean",
                score_delta=+2,
                detail=(
                    f"{clean_rejections:.1f}w clean rejections at walls in last {self._DECAY_LOOKBACK}H -- "
                    f"reversal framework working well"
                ),
            ))

        return signals

    # ------------------------------------------------------------------
    # Signal 3: Expansion Pressure
    # ------------------------------------------------------------------

    def _check_expansion_pressure(
        self, symbol: str, bars_5m: pd.DataFrame | None, zone_map
    ) -> list[RegimeSignal]:
        """Is ATR expanding directionally without mean reversion?"""
        signals: list[RegimeSignal] = []
        if bars_5m is None or len(bars_5m) < self._EXPANSION_LOOKBACK + 20:
            return signals

        recent = bars_5m.iloc[-self._EXPANSION_LOOKBACK:]
        baseline = bars_5m.iloc[-(self._EXPANSION_LOOKBACK + 20) : -self._EXPANSION_LOOKBACK]

        def true_range(df: pd.DataFrame) -> float:
            hl = df["high"] - df["low"]
            return float(hl.mean())

        recent_atr = true_range(recent)
        baseline_atr = true_range(baseline)
        if baseline_atr <= 0:
            return signals

        expansion_ratio = recent_atr / baseline_atr

        # Directional persistence
        directions = []
        for _, bar in recent.iterrows():
            directions.append(1 if float(bar["close"]) > float(bar["open"]) else -1)

        same_direction = sum(1 for d in directions if d == directions[-1])
        directionality = same_direction / len(directions)

        # Session-adjusted thresholds
        utc_hour = datetime.now(timezone.utc).hour
        if 12 <= utc_hour <= 16:
            thresh_hard, thresh_mild = 2.2, 1.7
        elif utc_hour in range(7, 13) or utc_hour in range(17, 22):
            thresh_hard, thresh_mild = 1.8, 1.4
        else:
            thresh_hard, thresh_mild = 1.4, 1.2

        if expansion_ratio > thresh_hard and directionality > 0.65:
            signals.append(RegimeSignal(
                name="expansion_pressure",
                score_delta=-2,
                detail=(
                    f"ATR {expansion_ratio:.1f}x baseline + {directionality:.0%} directional candles -- "
                    f"persistent expansion, poor fading conditions"
                ),
            ))
        elif expansion_ratio > thresh_mild and directionality > 0.60:
            signals.append(RegimeSignal(
                name="expansion_mild",
                score_delta=-1,
                detail=(
                    f"ATR {expansion_ratio:.1f}x baseline + {directionality:.0%} directional -- "
                    f"mild expansion pressure"
                ),
            ))
        elif expansion_ratio < 0.8:
            signals.append(RegimeSignal(
                name="compression",
                score_delta=+1,
                detail=f"ATR {expansion_ratio:.1f}x baseline -- compression, reversal conditions favorable",
            ))

        return signals

    # ------------------------------------------------------------------
    # Signal 4: Qualified Trade Failures
    # ------------------------------------------------------------------

    def _check_qualified_failures(self, symbol: str) -> list[RegimeSignal]:
        """Have our own gated setups been failing recently?"""
        signals: list[RegimeSignal] = []
        outcomes = list(self._outcomes[symbol])
        if not outcomes:
            return signals

        now = datetime.now(timezone.utc)
        recent_failures: list[dict] = []
        recent_wins: list[dict] = []

        for o in outcomes:
            try:
                closed_at = datetime.fromisoformat(o["closed_at"])
                if closed_at.tzinfo is None:
                    closed_at = closed_at.replace(tzinfo=timezone.utc)
                hours_ago = (now - closed_at).total_seconds() / 3600
                if hours_ago <= self._FAILURE_WINDOW_HOURS:
                    if o["hit_sl"]:
                        recent_failures.append(o)
                    else:
                        recent_wins.append(o)
            except Exception:
                continue

        n_fail = len(recent_failures)
        n_win = len(recent_wins)

        if n_fail >= 2 and n_win == 0:
            signals.append(RegimeSignal(
                name="qualified_failures",
                score_delta=-3,
                detail=(
                    f"{n_fail} qualified setups hit SL in last {self._FAILURE_WINDOW_HOURS}h, 0 winners -- "
                    f"market not honoring reversal framework"
                ),
            ))
        elif n_fail >= 2:
            signals.append(RegimeSignal(
                name="qualified_failures_mixed",
                score_delta=-2,
                detail=(
                    f"{n_fail} SL hits, {n_win} winners in last {self._FAILURE_WINDOW_HOURS}h -- "
                    f"elevated failure rate"
                ),
            ))
        elif n_fail == 1 and n_win == 0:
            signals.append(RegimeSignal(
                name="single_failure",
                score_delta=-1,
                detail=f"1 qualified setup hit SL, no winners in last {self._FAILURE_WINDOW_HOURS}h",
            ))
        elif n_win >= 2 and n_fail == 0:
            signals.append(RegimeSignal(
                name="clean_performance",
                score_delta=+1,
                detail=f"{n_win} winners, 0 SL hits in last {self._FAILURE_WINDOW_HOURS}h",
            ))

        return signals

    # ------------------------------------------------------------------
    # Signal 5: Breadth (correlated symbol regime scores)
    # ------------------------------------------------------------------

    def _check_breadth(self, symbol: str) -> list[RegimeSignal]:
        """Are correlated pairs also in poor regime state?"""
        signals: list[RegimeSignal] = []
        peers = self._CORRELATION_BLOCKS.get(symbol)
        if not peers:
            return signals

        peer_scores = [
            self._last_direct_scores[p]
            for p in peers[: self._MAX_BREADTH_PEERS]
            if p in self._last_direct_scores
        ]
        if len(peer_scores) < 2:
            return signals

        avg = sum(peer_scores) / len(peer_scores)

        if avg <= -2.0:
            signals.append(RegimeSignal(
                name="breadth_negative",
                score_delta=-1,
                detail=(
                    f"{len(peer_scores)} correlated pairs avg direct regime score {avg:+.1f} -- "
                    f"broad weakness, not pair-specific"
                ),
            ))
        elif avg >= 2.0:
            signals.append(RegimeSignal(
                name="breadth_positive",
                score_delta=+1,
                detail=(
                    f"{len(peer_scores)} correlated pairs avg direct regime score {avg:+.1f} -- "
                    f"broad strength confirms reversal conditions"
                ),
            ))

        return signals

    # ------------------------------------------------------------------
    # Signal 6: Trade Quality Pressure
    # ------------------------------------------------------------------

    def _check_quality_pressure(self, symbol: str, quality_pressure) -> list[RegimeSignal]:
        """Are recent trades showing poor follow-through?"""
        signals: list[RegimeSignal] = []
        if quality_pressure is None:
            return signals
        if getattr(quality_pressure, "pressure", "unknown") == "unknown":
            return signals
        if getattr(quality_pressure, "n_trades", 0) < 3:
            return signals

        if quality_pressure.pressure == "weak":
            signals.append(RegimeSignal(
                name="quality_pressure_weak",
                score_delta=-1,
                detail=(
                    f"Last {quality_pressure.n_trades} trades: avg F/T={quality_pressure.avg_ft_score:.0f} "
                    f"MFE/MAE={quality_pressure.avg_mfe_mae:.1f}x -- slow follow-through"
                ),
            ))
        elif quality_pressure.pressure == "strong":
            signals.append(RegimeSignal(
                name="quality_pressure_strong",
                score_delta=+1,
                detail=(
                    f"Last {quality_pressure.n_trades} trades: avg F/T={quality_pressure.avg_ft_score:.0f} "
                    f"MFE/MAE={quality_pressure.avg_mfe_mae:.1f}x -- clean follow-through"
                ),
            ))

        return signals

    # ------------------------------------------------------------------
    # Signal 7: Bollinger Band Context
    # ------------------------------------------------------------------

    def _check_bb_context(self, ctx: SymbolContext) -> list[RegimeSignal]:
        """Uses the BB classifier result from the pipeline."""
        bb = ctx.classifications.get("bb_classifier")
        if bb is None:
            return []

        score_delta = bb.metadata.get("score_delta", 0)
        if score_delta == 0:
            return []

        return [
            RegimeSignal(
                name=f"bb_{bb.label.lower()}",
                score_delta=score_delta,
                detail=bb.metadata.get("detail", bb.label),
            )
        ]
