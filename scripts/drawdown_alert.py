#!/usr/bin/env python3
"""Scrooge V3 drawdown alert daemon.

Fires Telegram alerts to Brock when:
  1. Daily P/L crosses -2.7% (early warning, once per UTC day)
  2. Daily circuit trips                     (once per UTC day)
  3. Service is inactive / failed             (once per outage)
  4. Cumulative DD from rollback baseline crosses -6.5% (once until recovery)

Run via openclaw cron every 5 min. Dedupes via data/alert_state.json.
Authorized 2026-05-04 by Brock.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

ROOT = Path("/home/ubuntu/mr-scrooge-v3")
STATE_PATH = ROOT / "data" / "alert_state.json"
CIRCUIT_PATH = ROOT / "data" / "daily_circuit.json"
ENV_PATH = ROOT / ".env"

ROLLBACK_BASELINE_EQUITY = 73211.0907
ROLLBACK_TS_UTC = "2026-04-30T18:43:42Z"

DAILY_WARN_PCT = -0.027
CUM_WARN_PCT = -0.065
CUM_RECOVER_PCT = -0.04  # arm next cumulative warn only after recovering above this

TG_CHANNEL = "telegram"
TG_ACCOUNT = "lestat"
TG_TARGET = "5611717594"  # Brock


def _load_env(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    if not path.exists():
        return out
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def _load_state() -> dict:
    if STATE_PATH.exists():
        try:
            return json.loads(STATE_PATH.read_text())
        except Exception:
            return {}
    return {}


def _save_state(s: dict) -> None:
    STATE_PATH.write_text(json.dumps(s, indent=2))


def _today_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _fetch_oanda_equity(env: dict[str, str]) -> tuple[float | None, float | None]:
    """Return (NAV, balance) or (None, None) on failure."""
    base = env.get("OANDA_API_URL", "").rstrip("/")
    acct = env.get("OANDA_ACCOUNT_ID")
    tok = env.get("OANDA_API_TOKEN")
    if not (base and acct and tok):
        return None, None
    try:
        r = requests.get(
            f"{base}/v3/accounts/{acct}/summary",
            headers={"Authorization": f"Bearer {tok}"},
            timeout=10,
        )
        r.raise_for_status()
        d = r.json().get("account", {})
        return float(d.get("NAV", 0.0)), float(d.get("balance", 0.0))
    except Exception as e:
        print(f"[ALERT] oanda fetch failed: {e}", file=sys.stderr)
        return None, None


def _service_state() -> str:
    try:
        r = subprocess.run(
            ["systemctl", "--user", "is-active", "mr-scrooge-v3.service"],
            capture_output=True, text=True, timeout=5,
        )
        return r.stdout.strip() or "unknown"
    except Exception as e:
        return f"error:{e}"


def _send(msg: str) -> bool:
    try:
        r = subprocess.run(
            [
                "openclaw", "message", "send",
                "--channel", TG_CHANNEL,
                "--account", TG_ACCOUNT,
                "--target", TG_TARGET,
                "--message", msg,
                "--json",
            ],
            capture_output=True, text=True, timeout=20,
        )
        ok = r.returncode == 0
        if not ok:
            print(f"[ALERT] send failed rc={r.returncode}: {r.stderr[:200]}", file=sys.stderr)
        return ok
    except Exception as e:
        print(f"[ALERT] send raised: {e}", file=sys.stderr)
        return False


def main() -> int:
    env = _load_env(ENV_PATH)
    state = _load_state()
    today = _today_utc()
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # --- Pull live data ---
    nav, balance = _fetch_oanda_equity(env)
    circuit = {}
    if CIRCUIT_PATH.exists():
        try:
            circuit = json.loads(CIRCUIT_PATH.read_text())
        except Exception:
            circuit = {}
    svc = _service_state()

    equity_start = float(circuit.get("equity_start", 0.0)) or None
    realized_pnl = float(circuit.get("realized_pnl", 0.0))
    tripped = bool(circuit.get("tripped"))
    daily_pct = (realized_pnl / equity_start) if equity_start else None

    cum_pct = ((nav - ROLLBACK_BASELINE_EQUITY) / ROLLBACK_BASELINE_EQUITY) if nav else None

    fired: list[str] = []

    # 1) Daily P/L early warning
    if daily_pct is not None and daily_pct <= DAILY_WARN_PCT:
        key = f"daily_warn:{today}"
        if not state.get(key):
            msg = (
                f"⚠️ Scrooge daily P/L early warning\n"
                f"Daily: {daily_pct:.2%}  (threshold {DAILY_WARN_PCT:.1%})\n"
                f"Realized: ${realized_pnl:,.2f} on start ${equity_start:,.2f}\n"
                f"NAV now: ${nav:,.2f}" + (f"  cum-since-rollback: {cum_pct:.2%}" if cum_pct is not None else "") + "\n"
                f"{now_iso}"
            )
            if _send(msg):
                state[key] = now_iso
                fired.append("daily_warn")

    # 2) Daily circuit tripped
    if tripped:
        key = f"circuit_trip:{today}"
        if not state.get(key):
            msg = (
                f"🛑 Scrooge daily circuit TRIPPED\n"
                f"Daily: {daily_pct:.2%}  realized ${realized_pnl:,.2f} on ${equity_start:,.2f}\n"
                f"Tripped at: {circuit.get('tripped_at')}\n"
                f"NAV now: ${nav:,.2f}" + (f"  cum-since-rollback: {cum_pct:.2%}" if cum_pct is not None else "") + "\n"
                f"Bot is frozen until next UTC day.\n"
                f"{now_iso}"
            )
            if _send(msg):
                state[key] = now_iso
                fired.append("circuit_trip")

    # 3) Service paused / failed
    if svc not in ("active", "activating"):
        key = "service_paused"
        prev = state.get(key)
        if prev != svc:
            msg = (
                f"❗ Scrooge service state: {svc}\n"
                f"systemctl --user is-active mr-scrooge-v3.service = {svc}\n"
                f"{now_iso}"
            )
            if _send(msg):
                state[key] = svc
                fired.append("service_paused")
    else:
        if state.get("service_paused") and state["service_paused"] != "active":
            msg = f"✅ Scrooge service recovered: active\n{now_iso}"
            if _send(msg):
                state["service_paused"] = "active"
                fired.append("service_recovered")

    # 4) Cumulative drawdown from rollback baseline
    if cum_pct is not None:
        armed = state.get("cum_warn_armed", True)  # default armed
        last_key = "cum_warn_last"
        if cum_pct <= CUM_WARN_PCT and armed:
            msg = (
                f"📉 Scrooge cumulative DD warning\n"
                f"Cum since rollback ({ROLLBACK_TS_UTC}): {cum_pct:.2%}\n"
                f"Baseline ${ROLLBACK_BASELINE_EQUITY:,.2f}  →  NAV ${nav:,.2f}\n"
                f"Daily: {daily_pct:.2%}  Service: {svc}\n"
                f"{now_iso}"
            )
            if _send(msg):
                state["cum_warn_armed"] = False
                state[last_key] = now_iso
                fired.append("cum_warn")
        elif cum_pct > CUM_RECOVER_PCT and not armed:
            state["cum_warn_armed"] = True
            fired.append("cum_warn_rearmed")

    # Heartbeat (no send) for telemetry
    state["last_check"] = {
        "ts": now_iso, "nav": nav, "daily_pct": daily_pct,
        "cum_pct": cum_pct, "tripped": tripped, "svc": svc,
        "fired": fired,
    }
    _save_state(state)

    if fired:
        print(f"[ALERT] fired: {fired}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
