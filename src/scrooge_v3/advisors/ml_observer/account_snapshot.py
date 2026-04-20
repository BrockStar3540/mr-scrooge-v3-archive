# ============================================================
# Copyright (c) Carl Brock 2026. All rights reserved.
# ============================================================
"""
ML Observer — Account + risk-tracker snapshot.

Called each cycle to capture:
  - V3 /api/data `account` section: balance, equity, margin, daily PnL, positions
  - OANDA /v3/accounts/{id}/summary (authoritative margin/equity — the V3
    dashboard value is cached and can lag)
  - Risk-tracker state files in mr-scrooge-v3/data/:
      * cooldowns.json        (per-symbol cooldown registry)
      * zone_blacklist.json   (entry-zone blacklist)
      * daily_circuit.json    (daily PnL circuit state)
      * limit_expiry_tracker.json (pending-order expiry counter)
      * positions.json        (live position state — info-only)

One row per cycle is appended to account.jsonl. Missing files are noted
as `null` in the row rather than suppressed, so downstream can tell the
difference between "no cooldowns" (`{}`) and "file missing" (`null`).
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests

log = logging.getLogger("ml-observer.account")

_DEFAULT_TIMEOUT = 15


def _read_json_safe(path: Path):
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text() or "null")
    except (OSError, json.JSONDecodeError) as e:
        log.warning("Failed to read %s: %s", path, e)
        return None


def fetch_oanda_summary(api_url: str, account_id: str, token: str) -> Optional[dict]:
    """Pull authoritative account summary straight from OANDA."""
    try:
        url = f"{api_url.rstrip('/')}/v3/accounts/{account_id}/summary"
        r = requests.get(
            url,
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
            timeout=_DEFAULT_TIMEOUT,
        )
        if r.status_code != 200:
            log.debug("OANDA summary returned %s", r.status_code)
            return None
        return r.json().get("account", {}) or {}
    except requests.RequestException as e:
        log.debug("OANDA summary fetch failed: %s", e)
        return None


def build_snapshot(
    v3_data: Optional[dict],
    v3_data_root: Path,
    oanda_api_url: Optional[str] = None,
    oanda_account_id: Optional[str] = None,
    oanda_token: Optional[str] = None,
) -> dict:
    """Assemble a single account.jsonl row.

    `v3_data_root` is the mr-scrooge-v3/data/ directory holding tracker
    state files.
    """
    ts = datetime.now(timezone.utc).isoformat()
    v3_account = (v3_data or {}).get("account", {}) if v3_data else {}
    v3_system = (v3_data or {}).get("system", {}) if v3_data else {}

    oanda_summary = None
    if oanda_api_url and oanda_account_id and oanda_token:
        oanda_summary = fetch_oanda_summary(oanda_api_url, oanda_account_id, oanda_token)

    # Normalize OANDA numeric strings
    def _f(d: Optional[dict], key: str) -> Optional[float]:
        if not d:
            return None
        v = d.get(key)
        if v is None:
            return None
        try:
            return float(v)
        except (TypeError, ValueError):
            return None

    return {
        "ts": ts,
        "cycle": v3_system.get("cycle_count"),
        "v3_account": v3_account,   # raw V3 dashboard account block
        "oanda": {
            "balance":         _f(oanda_summary, "balance"),
            "equity":          _f(oanda_summary, "NAV"),
            "margin_used":     _f(oanda_summary, "marginUsed"),
            "margin_available": _f(oanda_summary, "marginAvailable"),
            "unrealized_pl":   _f(oanda_summary, "unrealizedPL"),
            "realized_pl":     _f(oanda_summary, "pl"),
            "open_position_count": oanda_summary.get("openPositionCount") if oanda_summary else None,
            "open_trade_count":    oanda_summary.get("openTradeCount") if oanda_summary else None,
            "last_transaction_id": oanda_summary.get("lastTransactionID") if oanda_summary else None,
        },
        "cooldowns":        _read_json_safe(v3_data_root / "cooldowns.json"),
        "zone_blacklist":   _read_json_safe(v3_data_root / "zone_blacklist.json"),
        "daily_circuit":    _read_json_safe(v3_data_root / "daily_circuit.json"),
        "limit_expiry_tracker": _read_json_safe(v3_data_root / "limit_expiry_tracker.json"),
        "positions":        _read_json_safe(v3_data_root / "positions.json"),
    }


__all__ = ["build_snapshot", "fetch_oanda_summary"]
