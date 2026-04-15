"""Zone detector — builds the complete zone map for an instrument.

Uses:
- Daily chart for PDH/PDL and ATR
- Hourly chart for liquidity zones (pivot highs/lows)
- Cross-timeframe validation for tier assignment

Workflow:
1. Fetch daily OHLC -> draw session range, calculate ATR
2. Fetch hourly OHLC -> detect pivot highs/lows
3. Identify breakout flip levels
4. Cross-validate: hourly level near daily level -> Tier 1
5. Rank all zones by tier and test count
6. Determine current price location
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Optional

import numpy as np
import pandas as pd

from scrooge_v3.core.types import FeatureResult, MarketSnapshot
from scrooge_v3.features.models import LiquidityZone, SessionRange, ZoneMap

log = logging.getLogger("scrooge_v3.features.zone_detector")


class ZoneDetector:
    """
    Builds the complete zone map for an instrument using daily and hourly bars.

    Implements FeatureModule protocol.
    """

    name: str = "zone_detector"

    def __init__(self, config: dict | None = None):
        config = config or {}
        self.pivot_lookback = config.get("pivot_lookback_bars", 5)
        self.zone_merge_pct = config.get("zone_merge_pct", 0.0015)
        self.daily_align_pct = config.get("daily_align_pct", 0.002)
        self.buy_zone_pct = config.get("buy_zone_pct", 0.30)
        self.sell_zone_pct = config.get("sell_zone_pct", 0.30)
        self.atr_period = config.get("atr_period", 14)
        self.hourly_bars_back = config.get("hourly_bars_back", 48)
        # Percentile filtering
        self.use_percentile_filter = config.get("use_percentile_filter", True)
        self.pdh_percentile = config.get("pdh_percentile", 98)
        self.pdl_percentile = config.get("pdl_percentile", 2)
        # Touch validation
        self.min_level_touches = config.get("min_level_touches", 1)
        self.touch_buffer_pct = config.get("touch_buffer_pct", 0.001)
        self.reject_unvalidated = config.get("reject_unvalidated_boxes", False)

    def compute(
        self, symbol: str, snapshot: MarketSnapshot, state: dict
    ) -> FeatureResult:
        daily_bars: pd.DataFrame | None = snapshot.candles.get("D")
        hourly_bars: pd.DataFrame | None = snapshot.candles.get("1H")
        current_price = snapshot.mid
        exchange = state.get("exchange", "")

        if daily_bars is None or hourly_bars is None:
            log.warning(f"{symbol}: Missing daily or hourly bars for zone detection")
            return FeatureResult(name=self.name, values={}, computed_at=datetime.now())

        zone_map = self.build_zone_map(symbol, exchange, daily_bars, hourly_bars, current_price)

        if zone_map is None:
            return FeatureResult(name=self.name, values={}, computed_at=datetime.now())

        # Box age: hours since the session range was established (prior day close)
        box_age_hours = 0.0
        sr = zone_map.session_range
        if sr is not None:
            try:
                last_daily_ts = pd.Timestamp(daily_bars.index[-1]) if hasattr(daily_bars.index[-1], 'hour') else pd.Timestamp(daily_bars.iloc[-1].get("time", datetime.now()))
                box_age_hours = (datetime.now() - last_daily_ts.to_pydatetime().replace(tzinfo=None)).total_seconds() / 3600
            except Exception:
                box_age_hours = 0.0

        # Wall proximity: distance from current price to nearest range boundary as fraction of range
        wall_proximity = 0.5
        if sr is not None:
            box_range = sr.PDH - sr.PDL
            if box_range > 0:
                dist_to_high = abs(current_price - sr.PDH)
                dist_to_low = abs(current_price - sr.PDL)
                wall_proximity = min(dist_to_high, dist_to_low) / box_range

        return FeatureResult(
            name=self.name,
            values={
                "zone_map": zone_map,
                "box_age_hours": round(box_age_hours, 2),
                "wall_proximity": round(wall_proximity, 4),
            },
            computed_at=datetime.now(),
        )

    # ----------------------------------------------------------
    # MASTER BUILD FUNCTION
    # ----------------------------------------------------------

    def build_zone_map(
        self,
        symbol: str,
        exchange: str,
        daily_bars: pd.DataFrame,
        hourly_bars: pd.DataFrame,
        current_price: float,
    ) -> Optional[ZoneMap]:
        """
        Builds complete ZoneMap for one instrument.

        Args:
            daily_bars: DataFrame with OHLCV, at least 15 rows
            hourly_bars: DataFrame with OHLCV, at least 48 rows
            current_price: Latest price tick

        Returns:
            ZoneMap or None if insufficient data
        """
        if len(daily_bars) < 3 or len(hourly_bars) < 10:
            log.warning(f"Insufficient bar data for {symbol}")
            return None

        # 1. Build session range
        session_range = self._build_session_range(symbol, daily_bars, hourly_bars)
        if session_range is None:
            return None

        # 1b. Prior completed hour high/low -- additional liquidity zone
        prior_hour_high = float(hourly_bars["high"].iloc[-2]) if len(hourly_bars) >= 2 else session_range.PDH
        prior_hour_low = float(hourly_bars["low"].iloc[-2]) if len(hourly_bars) >= 2 else session_range.PDL
        prior_hour_mid = (prior_hour_high + prior_hour_low) / 2

        # 2. Detect hourly liquidity zones
        liquidity_zones = self._detect_liquidity_zones(
            symbol, hourly_bars, daily_bars, session_range
        )

        # 3. Tier all zones
        self._assign_tiers(liquidity_zones, session_range)

        # 4. Sort into buy/sell zones
        sell_zones, buy_zones = self._classify_directional_zones(
            liquidity_zones, session_range
        )

        # 5. Determine current price location
        current_zone = self._identify_current_zone(
            current_price, session_range, liquidity_zones
        )

        # 6. Find nearest actionable zones
        nearest_buy = self._nearest_zone(current_price, buy_zones, direction="above")
        nearest_sell = self._nearest_zone(current_price, sell_zones, direction="below")

        return ZoneMap(
            symbol=symbol,
            exchange=exchange,
            session_range=session_range,
            prior_hour_high=prior_hour_high,
            prior_hour_low=prior_hour_low,
            prior_hour_mid=prior_hour_mid,
            liquidity_zones=liquidity_zones,
            tier1_zones=[z for z in liquidity_zones if z.tier == 1],
            tier2_zones=[z for z in liquidity_zones if z.tier == 2],
            tier3_zones=[z for z in liquidity_zones if z.tier == 3],
            sell_zones=sell_zones,
            buy_zones=buy_zones,
            current_price=current_price,
            current_zone=current_zone,
            nearest_buy_zone=nearest_buy,
            nearest_sell_zone=nearest_sell,
            built_at=datetime.now().isoformat(),
        )

    # ----------------------------------------------------------
    # SESSION RANGE (was _build_daily_box)
    # ----------------------------------------------------------

    def _build_session_range(
        self,
        symbol: str,
        daily_bars: pd.DataFrame,
        hourly_bars: pd.DataFrame | None = None,
    ) -> Optional[SessionRange]:
        """
        Builds the PDH/PDL session range from prior completed day.
        Also calculates ATR for directional pressure thresholds.
        """
        try:
            # Find the most recent completed bar with a meaningful range.
            # Weekend bars (Sat/Sun) have near-zero movement and produce invalid tiny ranges.
            prior = None
            for i in range(2, min(len(daily_bars) + 1, 10)):
                candidate = daily_bars.iloc[-i]
                cand_high = float(candidate["high"])
                cand_low = float(candidate["low"])
                cand_close = float(candidate["close"]) if candidate["close"] else cand_high
                cand_range_pct = (cand_high - cand_low) / cand_close if cand_close > 0 else 0
                if cand_range_pct >= 0.0005:  # At least 0.05% range = real trading session
                    prior = candidate
                    break
            if prior is None:
                prior = daily_bars.iloc[-2]  # fallback

            raw_PDH = float(prior["high"])
            raw_PDL = float(prior["low"])
            PDH = raw_PDH
            PDL = raw_PDL
            percentile_filtered = False

            # -- Percentile filtering: use hourly bar distribution to remove spike wicks --
            prior_hourly = None
            if self.use_percentile_filter and hourly_bars is not None and len(hourly_bars) >= 24:
                prior_hourly = self._get_prior_day_hourly(hourly_bars)
                if len(prior_hourly) >= 6:
                    clean_high = float(np.percentile(prior_hourly["high"].values, self.pdh_percentile))
                    clean_low = float(np.percentile(prior_hourly["low"].values, self.pdl_percentile))
                    if clean_high < raw_PDH:
                        PDH = clean_high
                        percentile_filtered = True
                        log.info(
                            f"{symbol}: Percentile filter -- PDH {raw_PDH:.5f} -> {PDH:.5f} "
                            f"(spike of {((raw_PDH - PDH) / PDH) * 100:.2f}% removed)"
                        )
                    if clean_low > raw_PDL:
                        PDL = clean_low
                        percentile_filtered = True
                        log.info(
                            f"{symbol}: Percentile filter -- PDL {raw_PDL:.5f} -> {PDL:.5f} "
                            f"(spike of {((PDL - raw_PDL) / raw_PDL) * 100:.2f}% removed)"
                        )

            today = daily_bars.iloc[-1]
            today_open = float(today["open"])
            today_high = float(today["high"])
            today_low = float(today["low"])
            current_close = float(today["close"])

            # Gap detection -- if today's open is >0.5% outside the prior day range,
            # redraw using the gap protocol:
            #   Gap up: new ceiling = session high, new floor = prior PDH (flipped)
            #   Gap down: new ceiling = prior PDL (flipped), new floor = session low
            is_gap = False
            gap_direction = ""
            GAP_THRESHOLD = 0.005  # 0.5%
            if today_open > PDH * (1 + GAP_THRESHOLD):
                is_gap = True
                gap_direction = "up"
                old_PDH = PDH
                PDH = today_high
                PDL = old_PDH
                log.info(
                    f"{symbol}: Gap UP detected -- open {today_open:.5f} > PDH {old_PDH:.5f} "
                    f"| New range: {PDL:.5f} -> {PDH:.5f}"
                )
            elif today_open < PDL * (1 - GAP_THRESHOLD):
                is_gap = True
                gap_direction = "down"
                old_PDL = PDL
                PDH = old_PDL
                PDL = today_low
                log.info(
                    f"{symbol}: Gap DOWN detected -- open {today_open:.5f} < PDL {old_PDL:.5f} "
                    f"| New range: {PDL:.5f} -> {PDH:.5f}"
                )

            box_range = PDH - PDL

            # -- Sanity check: PDH must be above PDL --
            if box_range <= 0:
                log.error(
                    f"{symbol}: Inverted range after filtering -- "
                    f"PDL {PDL:.5f} >= PDH {PDH:.5f} | "
                    f"raw PDH={raw_PDH:.5f} PDL={raw_PDL:.5f} -- falling back to raw values"
                )
                PDH = raw_PDH
                PDL = raw_PDL
                percentile_filtered = False
                box_range = PDH - PDL
                if box_range <= 0:
                    log.error(f"{symbol}: Raw range also inverted -- discarding instrument")
                    return None

            range_half = box_range / 2
            center = PDL + range_half
            box_range_pct = box_range / current_close if current_close > 0 else 0

            # -- Touch validation: count hourly candles that tested each level --
            pdh_touches = 0
            pdl_touches = 0
            validated = True

            if not is_gap:
                if prior_hourly is None and hourly_bars is not None and len(hourly_bars) >= 24:
                    prior_hourly = self._get_prior_day_hourly(hourly_bars)
                if prior_hourly is not None and len(prior_hourly) >= 6:
                    pdh_touches = self._count_level_touches(PDH, prior_hourly, "high")
                    pdl_touches = self._count_level_touches(PDL, prior_hourly, "low")

                validated = (
                    pdh_touches >= self.min_level_touches
                    and pdl_touches >= self.min_level_touches
                )

                if not validated:
                    log.info(
                        f"{symbol}: Range touch validation "
                        f"{'FAILED' if self.reject_unvalidated else 'WARNING'} "
                        f"-- PDH touches: {pdh_touches}/{self.min_level_touches}, "
                        f"PDL touches: {pdl_touches}/{self.min_level_touches}"
                    )
                    if self.reject_unvalidated:
                        return None

            # ATR calculation
            atr = self._calculate_atr(daily_bars, self.atr_period)

            return SessionRange(
                symbol=symbol,
                PDH=PDH,
                PDL=PDL,
                center=center,
                box_range=box_range,
                range_half=range_half,
                box_range_pct=box_range_pct,
                ATR=atr,
                ATR_60pct=atr * 0.60,
                ATR_80pct=atr * 0.80,
                ATR_20pct=atr * 0.20,
                session_date=datetime.now().date().isoformat(),
                draw_time=datetime.now().isoformat(),
                pdh_touches=pdh_touches,
                pdl_touches=pdl_touches,
                percentile_filtered=percentile_filtered,
                validated=validated,
                raw_PDH=raw_PDH,
                raw_PDL=raw_PDL,
                gap_detected=is_gap,
                gap_direction=gap_direction,
            )
        except Exception as e:
            log.error(f"Session range build failed {symbol}: {e}")
            return None

    @staticmethod
    def _calculate_atr(bars: pd.DataFrame, period: int) -> float:
        """Standard ATR calculation."""
        highs = bars["high"].values
        lows = bars["low"].values
        closes = bars["close"].values

        tr_list = []
        for i in range(1, len(bars)):
            tr = max(
                highs[i] - lows[i],
                abs(highs[i] - closes[i - 1]),
                abs(lows[i] - closes[i - 1]),
            )
            tr_list.append(tr)

        tr_series = pd.Series(tr_list)
        atr = tr_series.ewm(span=period, adjust=False).mean().iloc[-1]
        return float(atr)

    # ----------------------------------------------------------
    # PERCENTILE FILTERING & TOUCH VALIDATION
    # ----------------------------------------------------------

    @staticmethod
    def _get_prior_day_hourly(hourly_bars: pd.DataFrame) -> pd.DataFrame:
        """
        Extract approximately the prior day's hourly bars from the lookback window.
        Bars are chronologically ordered (oldest first, newest last).

        With n bars: the last 24 bars = today's session, so iloc[-48:-24] = yesterday.
        """
        n = len(hourly_bars)
        if n >= 48:
            return hourly_bars.iloc[-48:-24]
        elif n >= 24:
            return hourly_bars.iloc[: n - 12]
        return hourly_bars

    def _count_level_touches(self, level: float, bars: pd.DataFrame, col: str) -> int:
        """
        Count candles whose extreme came within touch_buffer_pct of a price level.
        More touches = stronger, more validated level.
        """
        count = 0
        buffer = level * self.touch_buffer_pct
        values = bars[col].astype(float).values
        for val in values:
            if abs(val - level) <= buffer:
                count += 1
        return count

    # ----------------------------------------------------------
    # HOURLY LIQUIDITY ZONES (was _detect_magic_lines)
    # ----------------------------------------------------------

    def _detect_liquidity_zones(
        self,
        symbol: str,
        hourly_bars: pd.DataFrame,
        daily_bars: pd.DataFrame,
        session_range: SessionRange,
    ) -> list[LiquidityZone]:
        """
        Detects all significant horizontal levels on the hourly chart:
        - Pivot highs and lows
        - Breakout areas that have flipped polarity
        """
        zones: list[LiquidityZone] = []

        # 1. Pivot highs -> resistance / sell zones
        pivot_highs = self._find_pivots(hourly_bars, "high")
        for price, test_count, last_tested in pivot_highs:
            flip = self._is_breakout_flip(price, hourly_bars, "resistance")
            zones.append(LiquidityZone(
                price=price,
                zone_type="resistance" if not flip else "breakout_flip",
                tier=4,
                test_count=test_count,
                last_tested=last_tested,
                daily_aligned=False,
                is_breakout_flip=flip,
                strength_score=0,
                source_timeframe="1H",
                symbol=symbol,
                created_at=datetime.now().isoformat(),
            ))

        # 2. Pivot lows -> support / buy zones
        pivot_lows = self._find_pivots(hourly_bars, "low")
        for price, test_count, last_tested in pivot_lows:
            flip = self._is_breakout_flip(price, hourly_bars, "support")
            zones.append(LiquidityZone(
                price=price,
                zone_type="support" if not flip else "breakout_flip",
                tier=4,
                test_count=test_count,
                last_tested=last_tested,
                daily_aligned=False,
                is_breakout_flip=flip,
                strength_score=0,
                source_timeframe="1H",
                symbol=symbol,
                created_at=datetime.now().isoformat(),
            ))

        # 3. Add PDH and PDL explicitly as liquidity zones
        zones.append(LiquidityZone(
            price=session_range.PDH,
            zone_type="resistance",
            tier=2,
            test_count=1,
            last_tested=session_range.draw_time,
            daily_aligned=True,
            is_breakout_flip=False,
            strength_score=0,
            source_timeframe="D",
            symbol=symbol,
            created_at=datetime.now().isoformat(),
        ))
        zones.append(LiquidityZone(
            price=session_range.PDL,
            zone_type="support",
            tier=2,
            test_count=1,
            last_tested=session_range.draw_time,
            daily_aligned=True,
            is_breakout_flip=False,
            strength_score=0,
            source_timeframe="D",
            symbol=symbol,
            created_at=datetime.now().isoformat(),
        ))

        # 4. Merge nearby levels (within zone_merge_pct)
        zones = self._merge_nearby_zones(zones)

        return zones

    def _find_pivots(
        self,
        bars: pd.DataFrame,
        price_col: str,
    ) -> list[tuple[float, int, str]]:
        """
        Finds significant pivot points on the hourly chart.
        Returns list of (price, test_count, last_tested_iso).
        """
        n = self.pivot_lookback
        prices = bars[price_col].values
        times = bars.index if hasattr(bars.index, "__iter__") else range(len(bars))
        found_levels: list[tuple[float, int, str]] = []

        for i in range(n, len(bars) - n):
            val = prices[i]

            if price_col == "high":
                is_pivot = all(val >= prices[i - j] for j in range(1, n + 1)) and all(
                    val >= prices[i + j] for j in range(1, n + 1)
                )
            else:
                is_pivot = all(val <= prices[i - j] for j in range(1, n + 1)) and all(
                    val <= prices[i + j] for j in range(1, n + 1)
                )

            if is_pivot:
                merged = False
                for k, (existing_price, count, _) in enumerate(found_levels):
                    if abs(val - existing_price) / existing_price < self.zone_merge_pct:
                        found_levels[k] = (
                            (existing_price * count + val) / (count + 1),
                            count + 1,
                            str(times[i]) if hasattr(times[i], "__str__") else datetime.now().isoformat(),
                        )
                        merged = True
                        break

                if not merged:
                    found_levels.append((
                        val,
                        1,
                        str(times[i]) if hasattr(times[i], "__str__") else datetime.now().isoformat(),
                    ))

        return found_levels

    def _is_breakout_flip(
        self, price: float, bars: pd.DataFrame, original_type: str
    ) -> bool:
        """
        Detects if a level has flipped polarity:
        - Was resistance, got broken, now acting as support
        - Was support, got broken, now acting as resistance
        """
        closes = bars["close"].values
        tolerance = price * self.zone_merge_pct * 2

        broke_through = False
        returned_and_held = False

        for i in range(1, len(closes)):
            if original_type == "resistance":
                if closes[i] > price + tolerance and not broke_through:
                    broke_through = True
                if broke_through and abs(closes[i] - price) < tolerance:
                    returned_and_held = True
            else:
                if closes[i] < price - tolerance and not broke_through:
                    broke_through = True
                if broke_through and abs(closes[i] - price) < tolerance:
                    returned_and_held = True

        return broke_through and returned_and_held

    def _merge_nearby_zones(
        self, zones: list[LiquidityZone]
    ) -> list[LiquidityZone]:
        """Merges liquidity zones that are within zone_merge_pct of each other."""
        if not zones:
            return zones

        zones_sorted = sorted(zones, key=lambda x: x.price)
        merged: list[LiquidityZone] = []

        i = 0
        while i < len(zones_sorted):
            current = zones_sorted[i]
            group = [current]

            j = i + 1
            while j < len(zones_sorted):
                if abs(zones_sorted[j].price - current.price) / current.price < self.zone_merge_pct:
                    group.append(zones_sorted[j])
                    j += 1
                else:
                    break

            if len(group) == 1:
                merged.append(current)
            else:
                avg_price = sum(z.price for z in group) / len(group)
                total_tests = sum(z.test_count for z in group)
                any_daily = any(z.daily_aligned for z in group)
                any_flip = any(z.is_breakout_flip for z in group)
                best_source = "D" if any_daily else "1H"

                merged.append(LiquidityZone(
                    price=avg_price,
                    zone_type="breakout_flip" if any_flip else group[0].zone_type,
                    tier=4,
                    test_count=total_tests,
                    last_tested=group[-1].last_tested,
                    daily_aligned=any_daily,
                    is_breakout_flip=any_flip,
                    strength_score=0,
                    source_timeframe=best_source,
                    symbol=current.symbol,
                    created_at=datetime.now().isoformat(),
                ))

            i = j

        return merged

    # ----------------------------------------------------------
    # TIER ASSIGNMENT
    # ----------------------------------------------------------

    def _assign_tiers(
        self,
        liquidity_zones: list[LiquidityZone],
        session_range: SessionRange,
    ) -> None:
        """
        Assigns tier and strength score to each liquidity zone.

        Tier 1: Hourly level aligns with daily level (strongest)
        Tier 2: Breakout flip OR multiple tests (3+)
        Tier 3: 2 tests
        Tier 4: Single test, no special properties
        """
        daily_levels = [session_range.PDH, session_range.PDL]

        for zone in liquidity_zones:
            # Check daily alignment
            for dl in daily_levels:
                if abs(zone.price - dl) / dl < self.daily_align_pct:
                    zone.daily_aligned = True
                    break

            # Assign tier
            if zone.daily_aligned:
                zone.tier = 1
            elif zone.is_breakout_flip or zone.test_count >= 3:
                zone.tier = 2
            elif zone.test_count >= 2:
                zone.tier = 3
            else:
                zone.tier = 4

            # Strength score (0-100)
            score = 0
            score += min(zone.test_count * 15, 45)
            score += 25 if zone.daily_aligned else 0
            score += 20 if zone.is_breakout_flip else 0
            score += 10 if zone.source_timeframe == "D" else 0
            zone.strength_score = min(score, 100)

    # ----------------------------------------------------------
    # ZONE CLASSIFICATION
    # ----------------------------------------------------------

    def _classify_directional_zones(
        self,
        liquidity_zones: list[LiquidityZone],
        session_range: SessionRange,
    ) -> tuple[list[LiquidityZone], list[LiquidityZone]]:
        """Separates liquidity zones into sell zones (upper) and buy zones (lower)."""
        sell_zones = [z for z in liquidity_zones if z.price >= session_range.center]
        buy_zones = [z for z in liquidity_zones if z.price < session_range.center]

        sell_zones.sort(key=lambda x: x.price, reverse=True)
        buy_zones.sort(key=lambda x: x.price)

        return sell_zones, buy_zones

    def _identify_current_zone(
        self,
        current_price: float,
        session_range: SessionRange,
        liquidity_zones: list[LiquidityZone],
    ) -> str:
        """Determines where current price sits relative to the session range."""
        sell_threshold = session_range.PDL + (session_range.box_range * (1 - self.sell_zone_pct))
        buy_threshold = session_range.PDL + (session_range.box_range * self.buy_zone_pct)

        if current_price > session_range.PDH * 1.002:
            return "above_range"
        elif current_price < session_range.PDL * 0.998:
            return "below_range"
        elif current_price >= sell_threshold:
            return "sell_zone"
        elif current_price <= buy_threshold:
            return "buy_zone"
        else:
            return "middle"

    @staticmethod
    def _nearest_zone(
        current_price: float,
        zones: list[LiquidityZone],
        direction: str,
    ) -> Optional[LiquidityZone]:
        """Finds the nearest zone in a given direction (above or below)."""
        if not zones:
            return None

        if direction == "above":
            candidates = [z for z in zones if z.price >= current_price]
            if not candidates:
                return None
            return min(candidates, key=lambda z: z.price - current_price)
        else:
            candidates = [z for z in zones if z.price <= current_price]
            if not candidates:
                return None
            return min(candidates, key=lambda z: current_price - z.price)
