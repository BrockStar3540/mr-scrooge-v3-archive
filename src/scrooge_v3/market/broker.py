"""Broker adapter Protocol — broker-agnostic interface.

Any broker implementation (OANDA, dry-run, replay) must conform to this Protocol.
The runtime and execution layer only interact through this interface.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Protocol

import pandas as pd


@dataclass
class AccountInfo:
    balance: float = 0.0
    equity: float = 0.0
    margin_used: float = 0.0
    margin_available: float = 0.0
    margin_utilization: float = 0.0
    unrealized_pl: float = 0.0
    realized_pl_today: float = 0.0
    currency: str = "USD"


@dataclass
class InstrumentInfo:
    name: str
    pip_size: float
    pip_location: int  # e.g. -4 for EUR_USD, -2 for USD_JPY
    margin_rate: float  # e.g. 0.02 for 50:1 leverage
    min_units: int = 1
    max_units: int = 10_000_000


@dataclass
class PriceQuote:
    symbol: str
    bid: float
    ask: float
    mid: float
    spread: float
    timestamp: datetime | None = None


@dataclass
class OrderResult:
    success: bool
    trade_id: str = ""
    order_id: str = ""  # for pending limit orders
    fill_price: float = 0.0
    units: float = 0.0
    realized_pl: float = 0.0
    error: str = ""
    raw: dict[str, Any] = field(default_factory=dict)


@dataclass
class PendingOrderInfo:
    order_id: str
    symbol: str
    order_type: str  # "LIMIT_ORDER", "STOP_LOSS_ORDER", "TAKE_PROFIT_ORDER", etc.
    units: float
    price: float
    state: str  # "PENDING"
    time_in_force: str = "GTC"
    gtd_time: str = ""
    # Hotfix/orphan-sweep-broker-walk: surface parent + reduce-only flag so
    # state_recovery.reconcile_orphan_harvests can distinguish harvest-style
    # reduce LIMITs from entry LIMITs / SL / TP orders without parsing raw
    # broker payloads.  Empty string when the broker doesn't expose them.
    parent_trade_id: str = ""
    position_fill: str = ""  # "REDUCE_ONLY" | "DEFAULT" | "" (unknown)


@dataclass
class TradeInfo:
    trade_id: str
    symbol: str
    direction: str  # "long" or "short"
    units: float
    entry_price: float
    current_stop: float = 0.0
    current_tp: float = 0.0
    unrealized_pl: float = 0.0
    opened_at: datetime | None = None


class BrokerAdapter(Protocol):
    """Abstract broker interface. All methods may raise or return None on failure."""

    # --- Account ---

    def get_account(self) -> AccountInfo | None: ...

    def get_equity(self) -> float | None: ...

    # --- Instruments ---

    def get_instruments(self) -> dict[str, InstrumentInfo]: ...

    def get_pip_size(self, symbol: str) -> float: ...

    def get_margin_rate(self, symbol: str) -> float: ...

    # --- Pricing ---

    def get_price(self, symbol: str) -> PriceQuote | None: ...

    def get_prices(self, symbols: list[str]) -> dict[str, PriceQuote]: ...

    # --- Candles ---

    def get_candles(
        self,
        symbol: str,
        granularity: str,
        count: int = 50,
    ) -> pd.DataFrame | None: ...

    # --- Positions ---

    def get_open_trades(self) -> list[TradeInfo]: ...

    # --- Orders ---

    def place_market_order(
        self,
        symbol: str,
        units: int,
        stop_loss: float | None = None,
        take_profit: float | None = None,
    ) -> OrderResult: ...

    def modify_stop_loss(self, trade_id: str, new_stop: float) -> bool: ...

    def modify_take_profit(self, trade_id: str, new_tp: float) -> bool: ...

    def close_trade(self, trade_id: str, units: int | None = None) -> OrderResult: ...

    def place_limit_order(
        self,
        symbol: str,
        units: int,
        price: float,
        stop_loss: float | None = None,
        take_profit: float | None = None,
        gtd_time: str | None = None,
        position_fill: str = "DEFAULT",
    ) -> OrderResult: ...

    def get_pending_orders(self, symbol: str | None = None) -> list[PendingOrderInfo]: ...

    def cancel_order(self, order_id: str) -> bool: ...

    # --- Transactions ---

    def get_realized_pl_today(self) -> float: ...

    # --- Health ---

    def ping(self) -> bool: ...
