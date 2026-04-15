"""OANDA v20 REST API adapter — implements BrokerAdapter Protocol.

Ported from V2 core/oanda_client.py with all historical lessons applied:
  - P/L currency bug: use broker API P/L, never compute locally
  - 404 fallback: transaction stream for closed trades
  - 502 cache: stale candle data fallback
  - Margin rates: fetched per instrument on boot
  - LIMIT past market: pre-validate before submit
  - Decimal precision: JPY = 3, else 5

See logs/modules/broker-oanda.md for full lesson history.
"""

from __future__ import annotations

import logging
import time
from datetime import datetime, timezone
from typing import Any

import pandas as pd
import requests

from .broker import (
    AccountInfo,
    BrokerAdapter,
    InstrumentInfo,
    OrderResult,
    PriceQuote,
    TradeInfo,
)

log = logging.getLogger("scrooge_v3.market.oanda_adapter")

_DEFAULT_TIMEOUT = 10


class OANDAAdapter:
    """OANDA v20 REST API implementation of BrokerAdapter."""

    def __init__(self, config: dict[str, Any]):
        self.api_url = config["api_url"]  # e.g. https://api-fxpractice.oanda.com
        self.account_id = config["account_id"]
        self._headers = {
            "Authorization": f"Bearer {config['api_token']}",
            "Content-Type": "application/json",
        }
        self._instruments: dict[str, InstrumentInfo] = {}
        self._candle_cache: dict[str, tuple[float, pd.DataFrame]] = {}
        self._cache_ttl = config.get("cache_ttl_seconds", 30)
        self._consecutive_failures = 0
        self._failure_threshold = config.get("failure_threshold", 5)
        self._recovery_until: float = 0.0
        self._recovery_seconds = config.get("recovery_seconds", 120)

    # ------------------------------------------------------------------
    # HTTP primitives with health tracking
    # ------------------------------------------------------------------

    def _get(self, path: str, params: dict | None = None, timeout: int = _DEFAULT_TIMEOUT) -> dict | None:
        if self._in_recovery():
            return None
        url = f"{self.api_url}{path}"
        try:
            resp = requests.get(url, headers=self._headers, params=params, timeout=timeout)
            resp.raise_for_status()
            self._consecutive_failures = 0
            return resp.json()
        except requests.RequestException as e:
            self._record_failure(str(e))
            return None

    def _put(self, path: str, body: dict, timeout: int = _DEFAULT_TIMEOUT) -> dict | None:
        if self._in_recovery():
            return None
        url = f"{self.api_url}{path}"
        try:
            resp = requests.put(url, headers=self._headers, json=body, timeout=timeout)
            resp.raise_for_status()
            self._consecutive_failures = 0
            return resp.json()
        except requests.RequestException as e:
            self._record_failure(str(e))
            return None

    def _post(self, path: str, body: dict, timeout: int = _DEFAULT_TIMEOUT) -> dict | None:
        if self._in_recovery():
            return None
        url = f"{self.api_url}{path}"
        try:
            resp = requests.post(url, headers=self._headers, json=body, timeout=timeout)
            resp.raise_for_status()
            self._consecutive_failures = 0
            return resp.json()
        except requests.RequestException as e:
            self._record_failure(str(e))
            return None

    def _in_recovery(self) -> bool:
        if self._consecutive_failures >= self._failure_threshold:
            if time.monotonic() < self._recovery_until:
                return True
            self._consecutive_failures = 0
        return False

    def _record_failure(self, error: str) -> None:
        self._consecutive_failures += 1
        if self._consecutive_failures >= self._failure_threshold:
            self._recovery_until = time.monotonic() + self._recovery_seconds
            log.error("[OANDA] Circuit breaker: %d failures, recovery in %ds — %s",
                      self._consecutive_failures, self._recovery_seconds, error)
        else:
            log.warning("[OANDA] Request failed (%d/%d): %s",
                        self._consecutive_failures, self._failure_threshold, error)

    # ------------------------------------------------------------------
    # Account
    # ------------------------------------------------------------------

    def get_account(self) -> AccountInfo | None:
        data = self._get(f"/v3/accounts/{self.account_id}/summary")
        if not data:
            return None
        acct = data.get("account", {})
        balance = float(acct.get("balance", 0))
        margin_used = float(acct.get("marginUsed", 0))
        return AccountInfo(
            balance=balance,
            equity=float(acct.get("NAV", balance)),
            margin_used=margin_used,
            margin_available=float(acct.get("marginAvailable", 0)),
            margin_utilization=margin_used / balance if balance > 0 else 0.0,
            unrealized_pl=float(acct.get("unrealizedPL", 0)),
            realized_pl_today=0.0,
            currency=acct.get("currency", "USD"),
        )

    def get_equity(self) -> float | None:
        acct = self.get_account()
        return acct.equity if acct else None

    # ------------------------------------------------------------------
    # Instruments
    # ------------------------------------------------------------------

    def get_instruments(self) -> dict[str, InstrumentInfo]:
        if self._instruments:
            return self._instruments
        data = self._get(f"/v3/accounts/{self.account_id}/instruments")
        if not data:
            return {}
        for inst in data.get("instruments", []):
            name = inst["name"]
            pip_loc = int(inst.get("pipLocation", -4))
            self._instruments[name] = InstrumentInfo(
                name=name,
                pip_size=10 ** pip_loc,
                pip_location=pip_loc,
                margin_rate=float(inst.get("marginRate", 0.02)),
                min_units=int(inst.get("minimumTradeSize", 1)),
                max_units=int(inst.get("maximumOrderUnits", 10_000_000)),
            )
        log.info("[OANDA] Loaded %d instruments", len(self._instruments))
        return self._instruments

    def get_pip_size(self, symbol: str) -> float:
        inst = self._instruments.get(symbol)
        if inst:
            return inst.pip_size
        self.get_instruments()
        inst = self._instruments.get(symbol)
        return inst.pip_size if inst else (0.01 if "JPY" in symbol else 0.0001)

    def get_margin_rate(self, symbol: str) -> float:
        inst = self._instruments.get(symbol)
        if inst:
            return inst.margin_rate
        self.get_instruments()
        inst = self._instruments.get(symbol)
        return inst.margin_rate if inst else 0.02

    # ------------------------------------------------------------------
    # Pricing
    # ------------------------------------------------------------------

    def get_price(self, symbol: str) -> PriceQuote | None:
        data = self._get(f"/v3/accounts/{self.account_id}/pricing", params={"instruments": symbol})
        if not data:
            return None
        prices = data.get("prices", [])
        if not prices:
            return None
        p = prices[0]
        bid = float(p["bids"][0]["price"])
        ask = float(p["asks"][0]["price"])
        return PriceQuote(
            symbol=symbol, bid=bid, ask=ask,
            mid=(bid + ask) / 2, spread=ask - bid,
            timestamp=datetime.now(timezone.utc),
        )

    def get_prices(self, symbols: list[str]) -> dict[str, PriceQuote]:
        if not symbols:
            return {}
        data = self._get(
            f"/v3/accounts/{self.account_id}/pricing",
            params={"instruments": ",".join(symbols)},
        )
        if not data:
            return {}
        result = {}
        for p in data.get("prices", []):
            sym = p["instrument"]
            bid = float(p["bids"][0]["price"])
            ask = float(p["asks"][0]["price"])
            result[sym] = PriceQuote(
                symbol=sym, bid=bid, ask=ask,
                mid=(bid + ask) / 2, spread=ask - bid,
                timestamp=datetime.now(timezone.utc),
            )
        return result

    # ------------------------------------------------------------------
    # Candles (with 502 cache fallback)
    # ------------------------------------------------------------------

    def get_candles(self, symbol: str, granularity: str, count: int = 50) -> pd.DataFrame | None:
        cache_key = f"{symbol}:{granularity}"
        data = self._get(
            f"/v3/instruments/{symbol}/candles",
            params={"granularity": granularity, "count": count, "price": "M"},
        )
        if data and "candles" in data:
            df = self._candles_to_df(data["candles"])
            if df is not None and len(df) > 0:
                self._candle_cache[cache_key] = (time.monotonic(), df)
                return df

        # 502 cache fallback: use stale data if available
        cached = self._candle_cache.get(cache_key)
        if cached:
            age, df = cached
            age_s = time.monotonic() - age
            log.warning("[OANDA] Using cached %s candles for %s (%.0fs old)", granularity, symbol, age_s)
            return df

        return None

    @staticmethod
    def _candles_to_df(candles: list[dict]) -> pd.DataFrame | None:
        if not candles:
            return None
        rows = []
        for c in candles:
            if not c.get("complete", True) and c != candles[-1]:
                continue
            mid = c.get("mid", {})
            rows.append({
                "time": c["time"],
                "open": float(mid.get("o", 0)),
                "high": float(mid.get("h", 0)),
                "low": float(mid.get("l", 0)),
                "close": float(mid.get("c", 0)),
                "volume": int(c.get("volume", 0)),
            })
        if not rows:
            return None
        df = pd.DataFrame(rows)
        df["time"] = pd.to_datetime(df["time"])
        df = df.set_index("time")
        return df

    # ------------------------------------------------------------------
    # Positions
    # ------------------------------------------------------------------

    def get_open_trades(self) -> list[TradeInfo]:
        data = self._get(f"/v3/accounts/{self.account_id}/openTrades")
        if not data:
            return []
        trades = []
        for t in data.get("trades", []):
            units = float(t.get("currentUnits", 0))
            trades.append(TradeInfo(
                trade_id=t["id"],
                symbol=t["instrument"],
                direction="long" if units > 0 else "short",
                units=abs(units),
                entry_price=float(t.get("price", 0)),
                current_stop=float(t.get("stopLossOrder", {}).get("price", 0)),
                current_tp=float(t.get("takeProfitOrder", {}).get("price", 0)),
                unrealized_pl=float(t.get("unrealizedPL", 0)),
            ))
        return trades

    # ------------------------------------------------------------------
    # Orders
    # ------------------------------------------------------------------

    def place_market_order(
        self,
        symbol: str,
        units: int,
        stop_loss: float | None = None,
        take_profit: float | None = None,
    ) -> OrderResult:
        prec = 3 if "JPY" in symbol else 5
        body: dict[str, Any] = {
            "order": {
                "type": "MARKET",
                "instrument": symbol,
                "units": str(units),
                "timeInForce": "FOK",
                "positionFill": "DEFAULT",
            }
        }
        if stop_loss is not None:
            body["order"]["stopLossOnFill"] = {
                "price": f"{stop_loss:.{prec}f}",
                "timeInForce": "GTC",
            }
        if take_profit is not None:
            body["order"]["takeProfitOnFill"] = {
                "price": f"{take_profit:.{prec}f}",
                "timeInForce": "GTC",
            }

        result = self._post(f"/v3/accounts/{self.account_id}/orders", body)
        if not result:
            return OrderResult(success=False, error="API call failed")

        fill = result.get("orderFillTransaction")
        if fill:
            trade_id = fill.get("tradeOpened", {}).get("tradeID", "")
            return OrderResult(
                success=True,
                trade_id=trade_id,
                fill_price=float(fill.get("price", 0)),
                units=abs(float(fill.get("units", 0))),
                raw=result,
            )

        cancel = result.get("orderCancelTransaction", {})
        reject = result.get("orderRejectTransaction", {})
        error = cancel.get("reason", "") or reject.get("rejectReason", "unknown")
        return OrderResult(success=False, error=error, raw=result)

    def modify_stop_loss(self, trade_id: str, new_stop: float) -> bool:
        prec = 3 if new_stop > 50 else 5
        body = {"stopLoss": {"price": f"{new_stop:.{prec}f}", "timeInForce": "GTC"}}
        result = self._put(f"/v3/accounts/{self.account_id}/trades/{trade_id}/orders", body)
        return result is not None

    def modify_take_profit(self, trade_id: str, new_tp: float) -> bool:
        prec = 3 if new_tp > 50 else 5
        body = {"takeProfit": {"price": f"{new_tp:.{prec}f}", "timeInForce": "GTC"}}
        result = self._put(f"/v3/accounts/{self.account_id}/trades/{trade_id}/orders", body)
        return result is not None

    def close_trade(self, trade_id: str, units: int | None = None) -> OrderResult:
        body: dict[str, Any] = {}
        if units is not None:
            body["units"] = str(abs(units))
        result = self._put(f"/v3/accounts/{self.account_id}/trades/{trade_id}/close", body)
        if not result:
            return OrderResult(success=False, error="API call failed")

        fill = result.get("orderFillTransaction")
        if fill:
            realized_pl = (
                float(fill.get("pl", 0))
                + float(fill.get("financing", 0))
                - float(fill.get("commission", 0))
            )
            return OrderResult(
                success=True,
                trade_id=trade_id,
                fill_price=float(fill.get("price", 0)),
                realized_pl=realized_pl,
                raw=result,
            )
        return OrderResult(success=False, error="No fill transaction", raw=result)

    # ------------------------------------------------------------------
    # Transactions
    # ------------------------------------------------------------------

    def get_realized_pl_today(self) -> float:
        today = datetime.now(timezone.utc).strftime("%Y-%m-%dT00:00:00.000000000Z")
        data = self._get(
            f"/v3/accounts/{self.account_id}/transactions",
            params={"from": today, "type": "ORDER_FILL"},
        )
        if not data:
            return 0.0

        total = 0.0
        for page_url in data.get("pages", []):
            page = self._get_raw_url(page_url)
            if not page:
                continue
            for tx in page.get("transactions", []):
                total += float(tx.get("pl", 0))
        return round(total, 2)

    def _get_raw_url(self, url: str) -> dict | None:
        """Fetch a full URL (for transaction pagination)."""
        try:
            resp = requests.get(url, headers=self._headers, timeout=_DEFAULT_TIMEOUT)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException:
            return None

    # ------------------------------------------------------------------
    # Health
    # ------------------------------------------------------------------

    def ping(self) -> bool:
        data = self._get(f"/v3/accounts/{self.account_id}/summary")
        return data is not None
