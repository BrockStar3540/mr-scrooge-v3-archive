"""Range state machine — manages runtime range states for all active instruments.

Transitions:
  RANGING -> BREACH_INITIATED: Price closes 1 candle beyond range + buffer
  BREACH_INITIATED -> RANGING: Price returns inside within 2-candle window
  BREACH_INITIATED -> CONFIRMED_BREAK_RECALCULATING: 2 consecutive candles outside, or >1% extension
  CONFIRMED_BREAK_RECALCULATING -> NEW_RANGE_STANDBY: Alternative range drawn and viable
  NEW_RANGE_STANDBY -> SHELVED: If new range not viable
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Optional

import pandas as pd

from scrooge_v3.core.types import FeatureResult, MarketSnapshot
from scrooge_v3.features.models import SessionRange
from scrooge_v3.features.range_models import (
    AlternativeRangeResult,
    RangeState,
    RangeStateRecord,
)

log = logging.getLogger("scrooge_v3.features.range_builder")


class RangeStateMachine:
    """
    Manages runtime range states for all active instruments.

    Implements FeatureModule protocol. Stateful -- tracks range states per symbol.
    """

    name: str = "range_builder"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.breach_buffer_pct = config.get("breach_buffer_pct", 0.002)
        self.breach_confirm_candles = config.get("breach_confirm_candles", 2)
        self.breach_extension_pct = config.get("breach_extension_pct", 0.01)
        self.max_spread_pct_of_half = config.get("max_spread_pct_of_range", 0.15)
        self.new_range_proven_trades = config.get("new_range_proven_trades", 3)
        self.min_efficiency_ratio = config.get("min_efficiency", 2.0)
        self.min_net_profit = config.get("min_net_profit", 0.0)
        self.min_net_profit_pips = config.get("min_net_profit_pips", None)

        # Range age confidence schedule (hours: confidence %)
        self.age_confidence = {
            0: 1.00,
            2: 0.85,
            4: 0.70,
            6: 0.50,
        }

        self.states: dict[str, RangeStateRecord] = {}

    def compute(
        self, symbol: str, snapshot: MarketSnapshot, state: dict
    ) -> FeatureResult:
        """
        FeatureModule interface. Expects state to contain:
          - "current_bar": pd.Series (latest 5m bar)
          - "total_overhead": float
          - "minutes_since_session_start": int
          - "session_range": SessionRange (for initialization if needed)
        """
        record = self.states.get(symbol)

        if record is None:
            session_range: SessionRange | None = state.get("session_range")
            if session_range is None:
                log.warning(f"{symbol}: No session range available for range builder init")
                return FeatureResult(name=self.name, values={}, computed_at=datetime.now())
            record = self.initialize_instrument(symbol, session_range, snapshot.spread)

        current_bar = state.get("current_bar")
        total_overhead = state.get("total_overhead", snapshot.spread * 2)
        minutes = state.get("minutes_since_session_start", 0)

        if current_bar is not None:
            record = self.update(
                symbol, snapshot.mid, current_bar, snapshot.spread, total_overhead, minutes
            )

        return FeatureResult(
            name=self.name,
            values={"range_state_record": record},
            computed_at=datetime.now(),
        )

    # ----------------------------------------------------------
    # INITIALIZE
    # ----------------------------------------------------------

    def _pip_size(self, symbol: str) -> float:
        return 0.01 if "JPY" in symbol else 0.0001

    def _min_net_profit_for_symbol(self, symbol: str) -> float:
        if self.min_net_profit_pips is None:
            return float(self.min_net_profit)
        return float(self.min_net_profit_pips) * self._pip_size(symbol)

    def initialize_instrument(
        self, symbol: str, session_range: SessionRange, current_spread: float
    ) -> RangeStateRecord:
        """Called at boot or when instrument passes screening."""
        spread_threshold = session_range.range_half * self.max_spread_pct_of_half

        record = RangeStateRecord(
            symbol=symbol,
            state=RangeState.RANGING,
            active_range=session_range,
            alternative_range=None,
            using_alternative=False,
            breach_started_at=None,
            breach_price=0.0,
            breach_direction="",
            breach_candles_confirmed=0,
            session_start_time=datetime.now().isoformat(),
            range_age_hours=0.0,
            age_confidence_pct=100.0,
            confirmation_gates_required=2,
            new_range_trades=0,
            new_range_proven=False,
            broken_wall_price=0.0,
            broken_wall_direction="",
            entry_paused=False,
            pause_reason="",
            last_spread=current_spread,
            spread_threshold=spread_threshold,
            last_updated=datetime.now().isoformat(),
        )

        self.states[symbol] = record
        log.info(f"RangeStateMachine initialized: {symbol} | State: RANGING")
        return record

    # ----------------------------------------------------------
    # MAIN UPDATE (called every 5-minute candle close)
    # ----------------------------------------------------------

    def update(
        self,
        symbol: str,
        current_price: float,
        current_bar: pd.Series,
        current_spread: float,
        total_overhead: float,
        minutes_since_session_start: int,
    ) -> RangeStateRecord | None:
        """Master update function. Evaluates all state transitions."""
        if symbol not in self.states:
            log.warning(f"Symbol {symbol} not initialized in state machine")
            return None

        record = self.states[symbol]
        record.last_updated = datetime.now().isoformat()
        record.last_spread = current_spread

        # 1. Update range age and confidence
        record.range_age_hours = minutes_since_session_start / 60
        record.age_confidence_pct = self._get_age_confidence(record.range_age_hours) * 100
        record.confirmation_gates_required = 3 if record.range_age_hours >= 4 else 2

        # 2. Check spread -- require 2 consecutive bad scans before pausing entries
        if current_spread > record.spread_threshold:
            record.spread_bad_count += 1
            if record.spread_bad_count >= 2 and not record.entry_paused:
                record.entry_paused = True
                record.pause_reason = (
                    f"Spread {current_spread:.5f} exceeds threshold "
                    f"{record.spread_threshold:.5f} for {record.spread_bad_count} consecutive scans -- entries paused"
                )
                log.warning(f"{symbol}: {record.pause_reason}")
        else:
            record.spread_bad_count = 0
            if record.entry_paused and "Spread" in record.pause_reason:
                record.entry_paused = False
                record.pause_reason = ""
                log.info(f"{symbol}: Spread normalized -- entries resumed")

        # 3. State machine transitions
        active_range = record.alternative_range if record.using_alternative else record.active_range

        if record.state == RangeState.RANGING:
            self._handle_ranging(record, current_price, current_bar, active_range)
        elif record.state == RangeState.BREACH_INITIATED:
            self._handle_breach_pending(record, current_price, current_bar, active_range)
        elif record.state == RangeState.CONFIRMED_BREAK_RECALCULATING:
            # This state is resolved by calling draw_alternative_range externally
            pass

        return record

    # ----------------------------------------------------------
    # STATE HANDLERS
    # ----------------------------------------------------------

    def _handle_ranging(
        self,
        record: RangeStateRecord,
        current_price: float,
        current_bar: pd.Series,
        session_range: SessionRange,
    ) -> None:
        """Checks for breach conditions from RANGING state."""
        candle_close = float(current_bar["close"])
        breach_up = session_range.PDH * (1 + self.breach_buffer_pct)
        breach_dn = session_range.PDL * (1 - self.breach_buffer_pct)

        if candle_close > breach_up:
            record.state = RangeState.BREACH_INITIATED
            record.breach_started_at = datetime.now().isoformat()
            record.breach_price = candle_close
            record.breach_direction = "up"
            record.breach_candles_confirmed = 1
            record.entry_paused = True
            record.pause_reason = (
                f"Possible upside breach at {candle_close:.5f} "
                f"(PDH {session_range.PDH:.5f}) -- monitoring"
            )
            log.info(f"{record.symbol}: BREACH INITIATED (up) at {candle_close:.5f}")

        elif candle_close < breach_dn:
            record.state = RangeState.BREACH_INITIATED
            record.breach_started_at = datetime.now().isoformat()
            record.breach_price = candle_close
            record.breach_direction = "down"
            record.breach_candles_confirmed = 1
            record.entry_paused = True
            record.pause_reason = (
                f"Possible downside breach at {candle_close:.5f} "
                f"(PDL {session_range.PDL:.5f}) -- monitoring"
            )
            log.info(f"{record.symbol}: BREACH INITIATED (down) at {candle_close:.5f}")

    def _handle_breach_pending(
        self,
        record: RangeStateRecord,
        current_price: float,
        current_bar: pd.Series,
        session_range: SessionRange,
    ) -> None:
        """Determines if breach is false (return to range) or confirmed."""
        candle_close = float(current_bar["close"])

        # False break -- price returned inside range
        if record.breach_direction == "up" and candle_close <= session_range.PDH:
            record.state = RangeState.RANGING
            record.breach_candles_confirmed = 0
            record.breach_started_at = None
            record.entry_paused = False
            record.pause_reason = ""
            log.info(
                f"{record.symbol}: False break confirmed -- returned to range. "
                f"Note: repeated false breaks reinforce zone strength."
            )
            return

        if record.breach_direction == "down" and candle_close >= session_range.PDL:
            record.state = RangeState.RANGING
            record.breach_candles_confirmed = 0
            record.breach_started_at = None
            record.entry_paused = False
            record.pause_reason = ""
            log.info(f"{record.symbol}: False break confirmed -- returned to range.")
            return

        # Still outside -- increment confirmation count
        record.breach_candles_confirmed += 1

        # Check extension confirmation (big move = instant confirm)
        if record.breach_direction == "up":
            extension = (candle_close - session_range.PDH) / session_range.PDH
        else:
            extension = (session_range.PDL - candle_close) / session_range.PDL

        instant_confirm = extension >= self.breach_extension_pct

        # Confirmed breach
        if record.breach_candles_confirmed >= self.breach_confirm_candles or instant_confirm:
            record.state = RangeState.CONFIRMED_BREAK_RECALCULATING
            record.broken_wall_price = (
                session_range.PDH if record.breach_direction == "up" else session_range.PDL
            )
            record.broken_wall_direction = record.breach_direction
            record.pause_reason = (
                f"Range CONFIRMED broken -- {record.breach_direction} "
                f"({record.breach_candles_confirmed} candles, "
                f"extension {extension:.2%}). Recalculating..."
            )
            log.info(
                f"{record.symbol}: RANGE BROKEN ({record.breach_direction}) "
                f"-- drawing alternative range"
            )

    # ----------------------------------------------------------
    # ALTERNATIVE RANGE DRAWING
    # ----------------------------------------------------------

    def draw_alternative_range(
        self,
        symbol: str,
        bars_5m: pd.DataFrame,
        session_high: float,
        session_low: float,
        original_range: SessionRange,
        total_overhead: float,
    ) -> AlternativeRangeResult:
        """
        Alternative range protocol:

        Scenario A (broke up through PDH):
          Option 1: New PDH (session high) -> Original PDH (becomes new PDL)
          Option 2: Session high -> Session low (cheat code)

        Scenario B (broke down through PDL):
          Option 1: Original PDL (becomes new PDH) -> Session low
          Option 2: Session high -> Session low (cheat code)

        Scenario C (both walls broken):
          Cheat code only: Session high -> Session low
        """
        if symbol not in self.states:
            return AlternativeRangeResult(
                success=False,
                new_range=None,
                method="",
                viable=False,
                viability_reason="Symbol not found",
                efficiency_ratio=0,
            )

        record = self.states[symbol]
        direction = record.breach_direction

        candidates: list[tuple[str, float, float]] = []

        if direction == "up":
            new_pdh_a = session_high
            new_pdl_a = original_range.PDH
            if new_pdh_a > new_pdl_a:
                candidates.append(("original_wall_to_new_extreme", new_pdh_a, new_pdl_a))
        elif direction == "down":
            new_pdh_b = original_range.PDL
            new_pdl_b = session_low
            if new_pdh_b > new_pdl_b:
                candidates.append(("original_wall_to_new_extreme", new_pdh_b, new_pdl_b))

        # Always add cheat code as option
        if session_high > session_low:
            candidates.append(("session_cheat_code", session_high, session_low))

        # Evaluate each candidate for viability
        best_result: AlternativeRangeResult | None = None
        best_efficiency = 0.0

        current_price = float(bars_5m["close"].iloc[-1])

        for method, pdh, pdl in candidates:
            box_range = pdh - pdl
            range_half = box_range / 2
            net = range_half - total_overhead

            efficiency = net / total_overhead if total_overhead > 0 else 0

            viable = (
                net >= self._min_net_profit_for_symbol(symbol)
                and efficiency >= self.min_efficiency_ratio
            )

            if efficiency > best_efficiency:
                best_efficiency = efficiency
                new_range = SessionRange(
                    symbol=symbol,
                    PDH=pdh,
                    PDL=pdl,
                    center=pdl + (pdh - pdl) / 2,
                    box_range=box_range,
                    range_half=range_half,
                    box_range_pct=box_range / current_price if current_price > 0 else 0,
                    ATR=original_range.ATR,
                    ATR_60pct=original_range.ATR * 0.60,
                    ATR_80pct=original_range.ATR * 0.80,
                    ATR_20pct=original_range.ATR * 0.20,
                    session_date=datetime.now().date().isoformat(),
                    draw_time=datetime.now().isoformat(),
                )
                viability_reason = (
                    f"Net range_half: {net:.4f} | "
                    f"Efficiency: {efficiency:.2f}x | "
                    f"{'VIABLE' if viable else 'NOT VIABLE'}"
                )
                best_result = AlternativeRangeResult(
                    success=True,
                    new_range=new_range,
                    method=method,
                    viable=viable,
                    viability_reason=viability_reason,
                    efficiency_ratio=efficiency,
                )

        if best_result is None:
            self._shelve_instrument(symbol, "Could not construct valid alternative range")
            return AlternativeRangeResult(
                success=False,
                new_range=None,
                method="",
                viable=False,
                viability_reason="No valid alternative range geometry",
                efficiency_ratio=0,
            )

        if best_result.viable:
            record.alternative_range = best_result.new_range
            record.using_alternative = True
            record.state = RangeState.NEW_RANGE_STANDBY
            record.new_range_trades = 0
            record.new_range_proven = False
            record.entry_paused = False
            record.pause_reason = ""
            log.info(
                f"{symbol}: New range active via {best_result.method} | "
                f"PDH: {best_result.new_range.PDH:.5f} | "
                f"PDL: {best_result.new_range.PDL:.5f} | "
                f"Efficiency: {best_result.efficiency_ratio:.2f}x"
            )
        else:
            self._shelve_instrument(symbol, best_result.viability_reason)

        return best_result

    # ----------------------------------------------------------
    # RETURN-TO-RANGE SETUP
    # ----------------------------------------------------------

    def check_return_to_range(self, symbol: str, current_price: float) -> dict:
        """
        After range is broken, price often returns to test the broken wall.
        Old resistance becomes new support (and vice versa).
        """
        if symbol not in self.states:
            return {"setup_available": False}

        record = self.states[symbol]
        if record.broken_wall_price == 0:
            return {"setup_available": False}

        wall = record.broken_wall_price
        distance = abs(current_price - wall) / wall

        if distance < 0.002:
            if record.broken_wall_direction == "up":
                return {
                    "setup_available": True,
                    "direction": "long",
                    "zone_price": wall,
                    "zone_type": "broken_resistance_now_support",
                    "description": (
                        f"Price returning to test broken PDH {wall:.5f} as new support. "
                        f"Classic return-to-range long setup."
                    ),
                }
            else:
                return {
                    "setup_available": True,
                    "direction": "short",
                    "zone_price": wall,
                    "zone_type": "broken_support_now_resistance",
                    "description": (
                        f"Price returning to test broken PDL {wall:.5f} as new resistance. "
                        f"Classic return-to-range short setup."
                    ),
                }

        return {"setup_available": False}

    # ----------------------------------------------------------
    # NEW RANGE PROVEN TRACKING
    # ----------------------------------------------------------

    def record_new_range_trade_result(self, symbol: str, was_winner: bool) -> None:
        """Track wins in new range to determine when it's proven."""
        if symbol not in self.states:
            return
        record = self.states[symbol]
        if was_winner:
            record.new_range_trades += 1
            if record.new_range_trades >= self.new_range_proven_trades:
                record.new_range_proven = True
                log.info(
                    f"{symbol}: New range PROVEN after "
                    f"{record.new_range_trades} successful trades -- "
                    f"full position sizing restored"
                )

    def get_position_size_multiplier(self, symbol: str) -> float:
        """Returns position size multiplier based on range state."""
        if symbol not in self.states:
            return 1.0
        record = self.states[symbol]

        if record.state == RangeState.NEW_RANGE_STANDBY and not record.new_range_proven:
            return 0.5 + (record.new_range_trades / self.new_range_proven_trades) * 0.5
        elif record.age_confidence_pct < 70:
            return record.age_confidence_pct / 100
        return 1.0

    # ----------------------------------------------------------
    # HELPERS
    # ----------------------------------------------------------

    def _get_age_confidence(self, hours: float) -> float:
        """Interpolates confidence from age schedule."""
        hours_sorted = sorted(self.age_confidence.keys())
        for i in range(len(hours_sorted) - 1):
            h1, h2 = hours_sorted[i], hours_sorted[i + 1]
            if h1 <= hours <= h2:
                c1, c2 = self.age_confidence[h1], self.age_confidence[h2]
                t = (hours - h1) / (h2 - h1)
                return c1 + t * (c2 - c1)
        if hours < hours_sorted[0]:
            return self.age_confidence[hours_sorted[0]]
        return self.age_confidence[hours_sorted[-1]]

    def _shelve_instrument(self, symbol: str, reason: str) -> None:
        if symbol not in self.states:
            return
        record = self.states[symbol]
        record.state = RangeState.SHELVED
        record.entry_paused = True
        record.pause_reason = f"Shelved: {reason}"
        log.info(f"{symbol}: SHELVED -- {reason}")

    def get_state(self, symbol: str) -> Optional[RangeStateRecord]:
        return self.states.get(symbol)

    def is_tradeable(self, symbol: str) -> tuple[bool, str]:
        """Quick check: can we trade this instrument right now?"""
        if symbol not in self.states:
            return False, "Not initialized"
        record = self.states[symbol]
        if record.state == RangeState.SHELVED:
            return False, record.pause_reason
        if record.entry_paused:
            return False, record.pause_reason
        if record.state == RangeState.BREACH_INITIATED:
            return False, "Range breach pending -- monitoring"
        if record.state == RangeState.CONFIRMED_BREAK_RECALCULATING:
            return False, "Range broken -- recalculating"
        return True, "Tradeable"
