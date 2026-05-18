"""v10_fast cell-level performance monitor.

Brock 2026-05-18: produce a per-cell snapshot of live evidence on the
v10_fast deployment surface. Joins:

  data/seed-telemetry.jsonl       gate passes/blocks per cell
  data/order-attribution.jsonl    entry LIMIT placements
  data/execution-audit.jsonl      management events / realized exits
  OANDA broker                    current open trades + closed PnL

Emits:
  data/v10_fast_monitor_report.json   current cell stats snapshot
  data/v10_fast_alerts.jsonl          new alerts (append-only)
  data/v10_fast_alerts_state.json     remembered alerts (so we only fire once)

Designed to be cron'd every 5 min. No state in memory between runs.
"""
from __future__ import annotations

import json
import logging
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd
import requests

REPO = Path("/home/ubuntu/mr-scrooge-v3")
V10_FAST = REPO / "data/routing_table_v10_fast_current_regime.parquet"
LEDGER = REPO / "data/seed-telemetry.jsonl"
ORDERS = REPO / "data/order-attribution.jsonl"
AUDIT = REPO / "data/execution-audit.jsonl"
REPORT = REPO / "data/v10_fast_monitor_report.json"
ALERTS = REPO / "data/v10_fast_alerts.jsonl"
ALERT_STATE = REPO / "data/v10_fast_alerts_state.json"
DEPLOY_TIME = "2026-05-18T16:27:13+00:00"  # v10_fast flip moment

log = logging.getLogger("v10_fast_monitor")


def load_env():
    env = {}
    p = REPO / ".env"
    if p.exists():
        for line in p.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k] = v
    return env


def load_jsonl(p: Path) -> list[dict]:
    if not p.exists():
        return []
    out = []
    with open(p) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except Exception:
                pass
    return out


def oanda_account_state(env):
    """Return (balance, NAV, open_trades, recent_closed_since_deploy)."""
    url = env.get("OANDA_API_URL", "https://api-fxpractice.oanda.com")
    acct = env["OANDA_ACCOUNT_ID"]
    headers = {"Authorization": f"Bearer {env['OANDA_API_TOKEN']}"}
    out = {"balance": None, "NAV": None, "open_trades": [], "closed_since_deploy": []}
    try:
        r = requests.get(f"{url}/v3/accounts/{acct}/summary",
                         headers=headers, timeout=10)
        if r.ok:
            d = r.json().get("account", {})
            out["balance"] = float(d.get("balance", 0))
            out["NAV"] = float(d.get("NAV", 0))
        r = requests.get(f"{url}/v3/accounts/{acct}/openTrades",
                         headers=headers, timeout=10)
        if r.ok:
            out["open_trades"] = r.json().get("trades", [])
        # Closed trades since deploy
        r = requests.get(f"{url}/v3/accounts/{acct}/trades",
                         params={"state": "CLOSED", "count": 50},
                         headers=headers, timeout=10)
        if r.ok:
            for t in r.json().get("trades", []):
                close_time = t.get("closeTime", "")
                if close_time and close_time >= DEPLOY_TIME:
                    out["closed_since_deploy"].append(t)
    except Exception as exc:
        log.warning("OANDA query failed: %s", exc)
    return out


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    now = datetime.now(timezone.utc).isoformat()
    log.info("v10_fast monitor run @ %s", now)

    # 1. Load v10_fast cells
    if not V10_FAST.exists():
        log.error("v10_fast parquet missing: %s", V10_FAST)
        return
    v10 = pd.read_parquet(V10_FAST)
    cells = v10.drop_duplicates(subset=["parent_regime","pair","strategy","direction","session_bucket"]).copy()
    cells["cell_label"] = (cells.parent_regime + "|" + cells.pair + "|" +
                            cells.strategy + "|" + cells.direction + "|" +
                            cells.session_bucket)
    log.info("v10_fast cells: %d", len(cells))

    # 2. Telemetry: passes + blocks per cell since deploy
    ledger = load_jsonl(LEDGER)
    tel_df = pd.DataFrame(ledger) if ledger else pd.DataFrame()
    if not tel_df.empty:
        tel_df["ts"] = pd.to_datetime(tel_df["ts"], errors="coerce", utc=True)
        tel_df = tel_df[tel_df["ts"] >= DEPLOY_TIME]
    log.info("telemetry rows since deploy: %d", len(tel_df))

    def cell_key(r):
        cs = r.get("cell_strategy")
        if cs is None or (isinstance(cs, float) and pd.isna(cs)):
            return None
        return f"{r.get('regime53')}|{r.get('symbol')}|{cs}|{r.get('direction')}|{r.get('session_bucket')}"

    if not tel_df.empty:
        tel_df["cell_key"] = tel_df.apply(cell_key, axis=1)
    # Per cell: shadow passes / blocks + live approved / blocked
    shadow_pass = tel_df[(tel_df.get("gate") == "entry_filter_shadow") &
                         (tel_df.get("block_reason") == "shave_rule_satisfied")] if not tel_df.empty else pd.DataFrame()
    shadow_block = tel_df[(tel_df.get("gate") == "entry_filter_shadow") &
                          (tel_df.get("block_reason", "").map(lambda s: isinstance(s,str) and s.startswith("shave_rule_violated")))] if not tel_df.empty else pd.DataFrame()
    live_approved = tel_df[(tel_df.get("gate") == "entry_filter") &
                           (tel_df.get("passed") == True)] if not tel_df.empty else pd.DataFrame()
    live_blocked = tel_df[(tel_df.get("gate") == "entry_filter") &
                          (tel_df.get("passed") == False)] if not tel_df.empty else pd.DataFrame()

    def per_cell_count(frame):
        if frame.empty or "cell_key" not in frame.columns:
            return {}
        return frame.dropna(subset=["cell_key"]).cell_key.value_counts().to_dict()

    shadow_pass_c = per_cell_count(shadow_pass)
    shadow_block_c = per_cell_count(shadow_block)
    live_approved_c = per_cell_count(live_approved)
    live_blocked_c = per_cell_count(live_blocked)

    # 3. Orders placed since deploy (order-attribution)
    orders = load_jsonl(ORDERS)
    orders_df = pd.DataFrame(orders) if orders else pd.DataFrame()
    if not orders_df.empty:
        orders_df["placed_at"] = pd.to_datetime(orders_df["placed_at"], errors="coerce", utc=True)
        orders_df = orders_df[orders_df["placed_at"] >= DEPLOY_TIME]
    log.info("orders placed since deploy: %d", len(orders_df))

    # Attribute orders to cells via (symbol, direction). For multi-cell-per-pair
    # we cannot disambiguate without joining the matching telemetry approval --
    # do that for new orders only.
    def attribute_order_to_cell(o):
        if tel_df.empty:
            return None
        # Find the live_approved telemetry row closest in time to the order
        sym, direction = o.get("symbol"), o.get("direction")
        placed = pd.to_datetime(o["placed_at"], utc=True)
        window_lo = placed - pd.Timedelta(seconds=10)
        window_hi = placed + pd.Timedelta(seconds=2)
        cand = live_approved[
            (live_approved.get("symbol") == sym)
            & (live_approved.get("direction") == direction)
            & (live_approved.get("ts") >= window_lo)
            & (live_approved.get("ts") <= window_hi)
        ]
        if cand.empty:
            return None
        return cand.iloc[0]["cell_key"]

    order_by_cell: dict[str, int] = {}
    if not orders_df.empty:
        for _, o in orders_df.iterrows():
            key = attribute_order_to_cell(o)
            if key:
                order_by_cell[key] = order_by_cell.get(key, 0) + 1

    # 4. Fills + exits from OANDA
    env = load_env()
    oanda_state = oanda_account_state(env)
    log.info("OANDA: balance=%s NAV=%s open=%d closed_since_deploy=%d",
             oanda_state["balance"], oanda_state["NAV"],
             len(oanda_state["open_trades"]),
             len(oanda_state["closed_since_deploy"]))

    fills_by_cell: dict[str, int] = {}
    realized_by_cell: dict[str, float] = {}
    unrealized_by_cell: dict[str, float] = {}

    # Map OANDA trade -> cell via order-attribution + telemetry
    # For closed trades: trade.id matches order_id in attribution
    for trade in oanda_state["closed_since_deploy"]:
        oid = trade.get("id", "")
        match = orders_df[orders_df.get("order_id", "").astype(str) == oid]
        if not match.empty:
            o = match.iloc[0]
            cell = attribute_order_to_cell(o.to_dict()) if not tel_df.empty else None
            if cell:
                fills_by_cell[cell] = fills_by_cell.get(cell, 0) + 1
                realized_by_cell[cell] = realized_by_cell.get(cell, 0.0) + float(trade.get("realizedPL", 0) or 0)

    for trade in oanda_state["open_trades"]:
        oid = trade.get("id", "")
        match = orders_df[orders_df.get("order_id", "").astype(str) == oid]
        if not match.empty:
            o = match.iloc[0]
            cell = attribute_order_to_cell(o.to_dict()) if not tel_df.empty else None
            if cell:
                fills_by_cell[cell] = fills_by_cell.get(cell, 0) + 1
                unrealized_by_cell[cell] = unrealized_by_cell.get(cell, 0.0) + float(trade.get("unrealizedPL", 0) or 0)

    # 5. Build per-cell rows
    rows = []
    for _, c in cells.iterrows():
        key = c.cell_label
        rows.append({
            "cell_label": key,
            "strategy_id": c.strategy,
            "pair": c.pair,
            "direction": c.direction,
            "session_bucket": c.session_bucket,
            "regime53": c.parent_regime,
            "tier": c.tier,
            "approved_count": int(live_approved_c.get(key, 0)),
            "live_blocked_count": int(live_blocked_c.get(key, 0)),
            "order_count": int(order_by_cell.get(key, 0)),
            "fill_count": int(fills_by_cell.get(key, 0)),
            "realized_pnl": round(realized_by_cell.get(key, 0.0), 2),
            "unrealized_pnl": round(unrealized_by_cell.get(key, 0.0), 2),
            "shadow_pass_count": int(shadow_pass_c.get(key, 0)),
            "shadow_block_count": int(shadow_block_c.get(key, 0)),
        })

    # Also: shadow passes on NON-v10_fast cells (the v10_fast_v2 candidate stream)
    v10_keys = set(cells["cell_label"])
    extra_passes = {k: v for k, v in shadow_pass_c.items() if k not in v10_keys}

    report = {
        "generated_at": now,
        "deploy_time": DEPLOY_TIME,
        "account": {
            "balance": oanda_state["balance"],
            "NAV": oanda_state["NAV"],
            "open_trade_count": len(oanda_state["open_trades"]),
            "closed_since_deploy": len(oanda_state["closed_since_deploy"]),
        },
        "v10_fast_cells": rows,
        "totals": {
            "approved": sum(r["approved_count"] for r in rows),
            "orders":   sum(r["order_count"] for r in rows),
            "fills":    sum(r["fill_count"] for r in rows),
            "realized": round(sum(r["realized_pnl"] for r in rows), 2),
            "unrealized": round(sum(r["unrealized_pnl"] for r in rows), 2),
        },
        "non_v10_fast_shadow_passes": dict(sorted(
            extra_passes.items(), key=lambda kv: -kv[1])[:25]),
    }
    REPORT.write_text(json.dumps(report, indent=2, default=str))
    log.info("report -> %s", REPORT)

    # 6. Alerts (first order / first fill / first loss per cell)
    state = json.loads(ALERT_STATE.read_text()) if ALERT_STATE.exists() else {}
    new_alerts = []
    for r in rows:
        key = r["cell_label"]
        s = state.setdefault(key, {})
        if r["order_count"] > 0 and not s.get("first_order"):
            s["first_order"] = now
            new_alerts.append({"ts": now, "type": "first_order", "cell": key,
                               "count": r["order_count"]})
        if r["fill_count"] > 0 and not s.get("first_fill"):
            s["first_fill"] = now
            new_alerts.append({"ts": now, "type": "first_fill", "cell": key,
                               "count": r["fill_count"]})
        if r["realized_pnl"] < 0 and not s.get("first_loss"):
            s["first_loss"] = now
            new_alerts.append({"ts": now, "type": "first_loss", "cell": key,
                               "realized": r["realized_pnl"]})
    ALERT_STATE.write_text(json.dumps(state, indent=2, default=str))
    if new_alerts:
        with open(ALERTS, "a") as f:
            for a in new_alerts:
                f.write(json.dumps(a, default=str) + "\n")
        log.info("emitted %d new alerts", len(new_alerts))
        for a in new_alerts:
            log.info("ALERT: %s %s", a["type"], a)
    else:
        log.info("no new alerts")


if __name__ == "__main__":
    main()
