# ============================================================
# Copyright (c) Carl Brock 2026. All rights reserved.
# ============================================================
"""
ML Observer — OANDA Transactions Poller (read-only)

Pulls ORDER_FILL transactions incrementally via /v3/accounts/.../transactions/sinceid
and returns normalized trade-open / trade-close events for outcome labeling.

We intentionally DO NOT import scrooge_v3.market.oanda_adapter to avoid any risk
of touching live-trading state. This module issues plain HTTP GETs only.
"""

from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Iterable, Optional

import requests

log = logging.getLogger("ml-observer.oanda")

_DEFAULT_TIMEOUT = 20


def load_env(env_path: Path) -> dict:
    """Minimal .env parser — returns dict of KEY=VALUE pairs. Ignores comments."""
    out: dict = {}
    if not env_path.exists():
        return out
    for raw in env_path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip().strip('"').strip("'")
    return out


class OandaPoller:
    """Read-only OANDA transactions poller for outcome labeling."""

    def __init__(self, api_url: str, account_id: str, token: str):
        self.api_url = api_url.rstrip("/")
        self.account_id = account_id
        self._headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    @classmethod
    def from_env(cls, env_path: Path) -> Optional["OandaPoller"]:
        env = load_env(env_path)
        # Also fall back to os.environ (systemd EnvironmentFile support)
        api_url = env.get("OANDA_API_URL") or os.environ.get("OANDA_API_URL")
        account_id = env.get("OANDA_ACCOUNT_ID") or os.environ.get("OANDA_ACCOUNT_ID")
        token = env.get("OANDA_API_TOKEN") or os.environ.get("OANDA_API_TOKEN")
        if not (api_url and account_id and token):
            log.warning("OANDA env missing — outcome polling disabled")
            return None
        return cls(api_url, account_id, token)

    def get_last_transaction_id(self) -> Optional[str]:
        """Return the latest transaction id (for cursor initialization)."""
        url = f"{self.api_url}/v3/accounts/{self.account_id}/transactions"
        try:
            r = requests.get(url, headers=self._headers, timeout=_DEFAULT_TIMEOUT,
                             params={"pageSize": 1})
            r.raise_for_status()
            return str(r.json().get("lastTransactionID", "") or "") or None
        except requests.RequestException as e:
            log.warning("OANDA lastTransactionID fetch failed: %s", e)
            return None

    def fetch_fills_since(self, since_id: str) -> list[dict]:
        """
        Return ORDER_FILL transactions with id > since_id.
        Uses /transactions/sinceid and filters client-side by type (the endpoint
        ignores the type param if we pass it — so we filter here).
        """
        url = f"{self.api_url}/v3/accounts/{self.account_id}/transactions/sinceid"
        try:
            r = requests.get(url, headers=self._headers, timeout=_DEFAULT_TIMEOUT,
                             params={"id": since_id})
            r.raise_for_status()
            data = r.json()
        except requests.RequestException as e:
            log.warning("OANDA fetch_fills_since failed: %s", e)
            return []

        fills: list[dict] = []
        for tx in data.get("transactions", []):
            if tx.get("type") != "ORDER_FILL":
                continue
            fills.append(tx)
        return fills


def classify_fill(tx: dict) -> dict:
    """
    Turn a raw ORDER_FILL transaction into a normalized event dict:

        {
            "tx_id": "1502",
            "time": "2026-04-20T06:08:17.683Z",
            "symbol": "NZD_JPY",
            "kind": "open" | "close" | "reduce",
            "trade_ids_opened": ["1502"],
            "trade_ids_closed": ["1499"],
            "realized_pl_usd": 12.34,
            "price": 93.264,
            "units": 1105104,
        }
    """
    opened = tx.get("tradeOpened") or {}
    reduced = tx.get("tradeReduced") or {}
    closed_list = tx.get("tradesClosed") or []

    trade_ids_opened = [opened["tradeID"]] if opened.get("tradeID") else []
    trade_ids_closed = [t.get("tradeID") for t in closed_list if t.get("tradeID")]
    if reduced.get("tradeID"):
        # partial close — treat as a close event for the fraction
        trade_ids_closed.append(reduced["tradeID"])

    if trade_ids_opened and not trade_ids_closed:
        kind = "open"
    elif trade_ids_closed and not trade_ids_opened:
        kind = "close"
    elif trade_ids_opened and trade_ids_closed:
        # A flip — treat as close-then-open; outcome handler will pick up the close
        kind = "close"
    else:
        kind = "unknown"

    pl = 0.0
    try:
        pl = float(tx.get("pl", 0) or 0)
    except (TypeError, ValueError):
        pl = 0.0
    # Add partial-close pl from tradeReduced if present
    if reduced.get("realizedPL"):
        try:
            pl += float(reduced["realizedPL"])
        except (TypeError, ValueError):
            pass
    # Add per-closed pl
    for t in closed_list:
        try:
            pl += float(t.get("realizedPL", 0) or 0)
        except (TypeError, ValueError):
            pass

    try:
        price = float(tx.get("price", 0) or 0)
    except (TypeError, ValueError):
        price = 0.0
    try:
        units = float(tx.get("units", 0) or 0)
    except (TypeError, ValueError):
        units = 0.0

    return {
        "tx_id": str(tx.get("id", "")),
        "time": tx.get("time", ""),
        "symbol": tx.get("instrument", ""),
        "kind": kind,
        "trade_ids_opened": trade_ids_opened,
        "trade_ids_closed": trade_ids_closed,
        "realized_pl_usd": round(pl, 4),
        "price": price,
        "units": units,
    }
