"""Feature models — liquidity zones, session ranges, and zone maps."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class LiquidityZone:
    """
    A single horizontal liquidity zone drawn on the hourly chart.
    These are the primary reference levels for all trade decisions.
    """
    price: float
    zone_type: str          # 'resistance', 'support', 'breakout_flip'
    tier: int               # 1=highest (hourly+daily align), 2, 3, 4
    test_count: int         # How many times price has tested this level
    last_tested: str        # ISO datetime of most recent test
    daily_aligned: bool     # Does this level match a daily high/low?
    is_breakout_flip: bool  # Was this a breakout level that flipped polarity?
    strength_score: float   # Composite score 0-100
    source_timeframe: str   # '1H', 'D', 'pre_market'
    symbol: str
    created_at: str


@dataclass
class SessionRange:
    """
    The primary PDH/PDL range drawn from the prior day's range.
    Foundation of the entire system.
    """
    symbol: str
    PDH: float              # Prior day high
    PDL: float              # Prior day low
    center: float           # Midpoint — do not trade here
    box_range: float        # PDH - PDL
    range_half: float       # Half the range
    box_range_pct: float    # Range as % of price
    ATR: float              # Daily ATR(14)
    ATR_60pct: float        # 60% of ATR — directional pressure threshold
    ATR_80pct: float        # 80% of ATR — strong reversal threshold
    ATR_20pct: float        # 20% of ATR — minimum threshold
    session_date: str
    draw_time: str
    # Validation fields (percentile filtering + touch validation)
    pdh_touches: int = 0
    pdl_touches: int = 0
    percentile_filtered: bool = False
    validated: bool = True
    raw_PDH: float = 0.0
    raw_PDL: float = 0.0
    gap_detected: bool = False
    gap_direction: str = ''   # 'up' | 'down' | ''


@dataclass
class ZoneMap:
    """
    Complete zone picture for one instrument at one point in time.
    This is what the strategy engine queries.
    """
    symbol: str
    exchange: str
    session_range: SessionRange
    prior_hour_high: float          # Prior completed hour high — secondary zone
    prior_hour_low: float           # Prior completed hour low — secondary zone
    prior_hour_mid: float           # Prior hour midpoint
    liquidity_zones: list[LiquidityZone]
    tier1_zones: list[LiquidityZone]    # Hourly + daily aligned
    tier2_zones: list[LiquidityZone]    # Multiple hourly tests
    tier3_zones: list[LiquidityZone]    # Single hourly pivot
    sell_zones: list[LiquidityZone]     # Near PDH and upper zones
    buy_zones: list[LiquidityZone]      # Near PDL and lower zones
    current_price: float
    current_zone: str               # 'buy_zone', 'sell_zone', 'middle', 'above_range', 'below_range'
    nearest_buy_zone: Optional[LiquidityZone] = None
    nearest_sell_zone: Optional[LiquidityZone] = None
    built_at: str = ''
