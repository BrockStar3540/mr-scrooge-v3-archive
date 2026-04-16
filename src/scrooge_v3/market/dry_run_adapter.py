"""Dry-run broker adapter — shadow-trades without real orders.

Implements BrokerAdapter Protocol. Reads real prices from OANDA
but simulates order execution locally. Used for testing and
shadow-trading before going live.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any

import pandas as pd

from .broker import (
    AccountInfo,
    InstrumentInfo,
    OrderResult,
    PendingOrderInfo,
    PriceQuote,
    TradeInfo,
)
from .oanda_adapter import OANDAAdapter

log = logging.getLogger("scrooge_v3.market.dry_run_adapter")


class DryRunAdapter:
    """Shadow-trading adapter — real prices, simulated orders.

    Wraps an OANDAAdapter for market data but intercepts all
    order operations with local simulation.
    """

    def __init__(self, oanda: OANDAAdapter, config: dict | None = None):
        config = config or {}
        self._oanda = oanda
        self._virtual_balance = config.get("virtual_balance", 10_000.0)
        self._virtual_trades: dict[str, TradeInfo] = {}
        self._next_trade_id = 1
        self._realized_pl_today = 0.0
        self._pending_orders: dict[str, dict] = {}

    # --- Delegate market data to OANDA ---

    def get_account(self) -> AccountInfo:
        return AccountInfo(
            balance=self._virtual_balance,
            equity=self._virtual_balance,
            margin_used=0.0,
            margin_available=self._virtual_balance,
            margin_utilization=0.0,
            unrealized_pl=0.0,
            realized_pl_today=self._realized_pl_today,
            currency="USD",
        )

    def get_equity(self) -> float:
        return self._virtual_balance

    def get_instruments(self) -> dict[str, InstrumentInfo]:
        return self._oanda.get_instruments()

    def get_pip_size(self, symbol: str) -> float:
        return self._oanda.get_pip_size(symbol)

    def get_margin_rate(self, symbol: str) -> float:
        return self._oanda.get_margin_rate(symbol)

    def get_price(self, symbol: str) -> PriceQuote | None:
        return self._oanda.get_price(symbol)

    def get_prices(self, symbols: list[str]) -> dict[str, PriceQuote]:
        return self._oanda.get_prices(symbols)

    def get_candles(self, symbol: str, granularity: str, count: int = 50) -> pd.DataFrame | None:
        return self._oanda.get_candles(symbol, granularity, count)

    # --- Simulated positions ---

    def get_open_trades(self) -> list[TradeInfo]:
        return list(self._virtual_trades.values())

    # --- Simulated orders ---

    def place_market_order(
        self,
        symbol: str,
        units: int,
        stop_loss: float | None = None,
        take_profit: float | None = None,
    ) -> OrderResult:
        quote = self._oanda.get_price(symbol)
        if not quote:
            return OrderResult(success=False, error="No price available")

        fill_price = quote.ask if units > 0 else quote.bid
        trade_id = f"DRY-{self._next_trade_id}"
        self._next_trade_id += 1

        self._virtual_trades[trade_id] = TradeInfo(
            trade_id=trade_id,
            symbol=symbol,
            direction="long" if units > 0 else "short",
            units=abs(units),
            entry_price=fill_price,
            current_stop=stop_loss or 0.0,
            current_tp=take_profit or 0.0,
            unrealized_pl=0.0,
            opened_at=datetime.now(timezone.utc),
        )

        log.info(
            "[DRY_RUN] FILLED %s %s %d units @ %.5f SL=%.5f TP=%.5f",
            trade_id, symbol, units, fill_price,
            stop_loss or 0, take_profit or 0,
        )
        return OrderResult(success=True, trade_id=trade_id, fill_price=fill_price, units=abs(units))

    def modify_stop_loss(self, trade_id: str, new_stop: float) -> bool:
        trade = self._virtual_trades.get(trade_id)
        if not trade:
            return False
        trade.current_stop = new_stop
        log.debug("[DRY_RUN] SL modified %s → %.5f", trade_id, new_stop)
        return True

    def modify_take_profit(self, trade_id: str, new_tp: float) -> bool:
        trade = self._virtual_trades.get(trade_id)
        if not trade:
            return False
        trade.current_tp = new_tp
        return True

    def close_trade(self, trade_id: str, units: int | None = None) -> OrderResult:
        trade = self._virtual_trades.pop(trade_id, None)
        if not trade:
            return OrderResult(success=False, error=f"Trade {trade_id} not found")

        quote = self._oanda.get_price(trade.symbol)
        if not quote:
            return OrderResult(success=False, error="No price for close")

        exit_price = quote.bid if trade.direction == "long" else quote.ask
        pip = 0.01 if "JPY" in trade.symbol else 0.0001
        if trade.direction == "long":
            pl_pips = (exit_price - trade.entry_price) / pip
        else:
            pl_pips = (trade.entry_price - exit_price) / pip

        log.info("[DRY_RUN] CLOSED %s @ %.5f (%.1f pips)", trade_id, exit_price, pl_pips)
        return OrderResult(success=True, trade_id=trade_id, fill_price=exit_price, realized_pl=pl_pips)

    def place_limit_order(
        self,
        symbol: str,
        units: int,
        price: float,
        stop_loss: float | None = None,
        take_profit: float | None = None,
        gtd_time: str | None = None,
        position_fill: str = "DEFAULT",
    ) -> OrderResult:
        quote = self._oanda.get_price(symbol)
        if not quote:
            return OrderResult(success=False, error="No price available")

        # Check if limit would fill immediately (at-or-better)
        if units > 0 and quote.ask <= price:
            # Buy limit at or above ask = immediate fill
            return self.place_market_order(symbol, units, stop_loss, take_profit)
        if units < 0 and quote.bid >= price:
            # Sell limit at or below bid = immediate fill
            return self.place_market_order(symbol, units, stop_loss, take_profit)

        # Pending — store for later
        order_id = f"DRY-ORD-{self._next_trade_id}"
        self._next_trade_id += 1
        self._pending_orders[order_id] = {
            "symbol": symbol, "units": units, "price": price,
            "stop_loss": stop_loss, "take_profit": take_profit,
            "gtd_time": gtd_time, "position_fill": position_fill,
        }
        log.info("[DRY_RUN] LIMIT ORDER PLACED %s %s %d units @ %.5f",
                 order_id, symbol, units, price)
        return OrderResult(success=True, order_id=order_id)

    def get_pending_orders(self, symbol: str | None = None) -> list[PendingOrderInfo]:
        orders = []
        for oid, o in list(self._pending_orders.items()):
            if symbol and o["symbol"] != symbol:
                continue
            orders.append(PendingOrderInfo(
                order_id=oid, symbol=o["symbol"], order_type="LIMIT",
                units=abs(o["units"]), price=o["price"], state="PENDING",
            ))
        return orders

    def cancel_order(self, order_id: str) -> bool:
        if order_id in self._pending_orders:
            del self._pending_orders[order_id]
            log.info("[DRY_RUN] Cancelled order %s", order_id)
            return True
        return False

    # --- Transactions ---

    def get_realized_pl_today(self) -> float:
        return self._realized_pl_today

    # --- Health ---

    def ping(self) -> bool:
        return self._oanda.ping()
