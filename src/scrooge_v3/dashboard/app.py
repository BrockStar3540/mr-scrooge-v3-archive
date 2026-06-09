"""Dashboard Flask app — real-time trading dashboard.

Serves the live trading state as a single JSON endpoint.
HTML renders it into proper cards, badges, and signal panels.
"""

from __future__ import annotations

import functools
import logging
import os
from typing import Any

from flask import Flask, Response, jsonify, render_template, request
from flask.json.provider import DefaultJSONProvider

from .live_state import LiveState

log = logging.getLogger("scrooge_v3.dashboard.app")


class _SafeJSONProvider(DefaultJSONProvider):
    """Never let /api/data 500 on serialization (Brock 2026-06-02).

    A `set` leaking into the snapshot crashed jsonify with
    'Object of type set is not JSON serializable', which 500'd /api/data and
    starved the ml-observer's scorer (acc=0.00). Convert sets/frozensets to
    lists; fall back to str() for any other exotic type so the dashboard — and
    the ML outcome feed that reads it — stay alive.
    """

    @staticmethod
    def default(o: Any) -> Any:
        if isinstance(o, (set, frozenset)):
            try:
                return sorted(o)
            except Exception:
                return list(o)
        try:
            return DefaultJSONProvider.default(o)
        except TypeError:
            return str(o)

_TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")
_STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")

# Global reference set by run_dashboard()
_live_state: LiveState | None = None

_LOG_PATH = "/home/ubuntu/mr-scrooge-v3/logs/scrooge_v3.log"


def _tail(path: str, n: int) -> list:
    try:
        import collections
        with open(path, "rb") as fh:
            return [l.decode("utf-8", "replace") for l in collections.deque(fh, maxlen=n)]
    except Exception:
        return []


def _oanda_open_trades() -> list:
    import os, json, urllib.request
    tok = os.environ.get("OANDA_API_TOKEN") or os.environ.get("OANDA_TOKEN")
    acc = os.environ.get("OANDA_ACCOUNT_ID") or os.environ.get("OANDA_ACCOUNT")
    if not tok or not acc:
        return []
    try:
        req = urllib.request.Request(
            f"https://api-fxpractice.oanda.com/v3/accounts/{acc}/openTrades",
            headers={"Authorization": f"Bearer {tok}"})
        out = []
        for tr in json.load(urllib.request.urlopen(req, timeout=8)).get("trades", []):
            u = float(tr["currentUnits"]); inst = tr["instrument"]
            upl = float(tr.get("unrealizedPL", 0)); op = float(tr.get("price", 0)) or 1
            ps = 0.01 if "JPY" in inst else 0.0001
            if inst.startswith("USD_"):
                pipval = abs(u) * ps / op
            else:
                pipval = abs(u) * ps
            pips = round(upl / pipval, 1) if pipval else 0.0
            out.append({"id": tr["id"], "pair": inst, "units": u,
                        "upl": round(upl, 2), "pips": pips,
                        "dir": "long" if u > 0 else "short",
                        "open": tr["openTime"][11:16]})
        return out
    except Exception:
        return []


def _oanda_account() -> dict:
    import os, json, urllib.request
    tok = os.environ.get("OANDA_API_TOKEN") or os.environ.get("OANDA_TOKEN")
    acc = os.environ.get("OANDA_ACCOUNT_ID") or os.environ.get("OANDA_ACCOUNT")
    if not tok or not acc:
        return {}
    try:
        req = urllib.request.Request(
            f"https://api-fxpractice.oanda.com/v3/accounts/{acc}/summary",
            headers={"Authorization": f"Bearer {tok}"})
        a = json.load(urllib.request.urlopen(req, timeout=8))["account"]
        return {"nav": round(float(a["NAV"]), 2), "balance": round(float(a["balance"]), 2),
                "margin_used": round(float(a.get("marginUsed", 0)), 2),
                "open": int(a.get("openTradeCount", 0))}
    except Exception:
        return {}


def _recent_activity(lines: list) -> dict:
    """Real firing rate: gate decisions + strategy fires in the last ~90s of the log."""
    import re, datetime
    dec, fires = [], []
    for ln in lines:
        m = re.match(r"(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d)", ln)
        if not m:
            continue
        try:
            dt = datetime.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S")
        except Exception:
            continue
        if "pip_eater] PASSED" in ln:
            dec.append((dt, "pass"))
        elif "pip_eater] FAILED" in ln:
            dec.append((dt, "fail"))
        if "[STRATEGY:" in ln:
            sm = re.search(r"STRATEGY:(\w+)", ln)
            if sm:
                fires.append((dt, sm.group(1)))
    allt = [d[0] for d in dec] + [f[0] for f in fires]
    if not allt:
        return {"cand_90s": 0, "pass_90s": 0, "firing": False, "strats": []}
    now = max(allt); cut = now - datetime.timedelta(seconds=90)
    cand = sum(1 for d, k in dec if d >= cut)
    passed = sum(1 for d, k in dec if d >= cut and k == "pass")
    strats = list(dict.fromkeys(s for tt, s in fires if tt >= cut))
    return {"cand_90s": cand, "pass_90s": passed, "firing": cand > 0 or bool(strats), "strats": strats[:6]}


def _brain_snapshot() -> dict:
    import re
    lines = _tail(_LOG_PATH, 1500)
    funnel = {"passed": 0, "ev_veto": 0, "below_floor": 0, "adr": 0, "cooldown": 0, "other": 0}
    passed_evs, factor, exit_feed, pos_dec = [], {}, [], {}
    strat_fires, strat_tally, last_size = [], {}, None
    for ln in lines:
        if "pip_eater] PASSED" in ln:
            funnel["passed"] += 1
            m = re.search(r"net=\+?(-?[\d.]+)p", ln)
            if m: passed_evs.append(float(m.group(1)))
        elif "pip_eater] FAILED" in ln or "empty_plate" in ln:
            low = ln.lower()
            if "ml_ev" in low or "ev_veto" in low or "neg ev" in low or "ev=" in low and "veto" in low: funnel["ev_veto"] += 1
            elif "floor" in low or "empty_plate" in low: funnel["below_floor"] += 1
            elif "adr" in low: funnel["adr"] += 1
            elif "cooldown" in low: funnel["cooldown"] += 1
            else: funnel["other"] += 1
        ps = re.search(r"symbol=([A-Z]{3}_[A-Z]{3})", ln)
        if ps:
            al = re.search(r"align=(\d)", ln); ad = re.search(r"ADR=(ADR\d)", ln)
            if al or ad:
                f = factor.setdefault(ps.group(1), {"pair": ps.group(1)})
                if al: f["align"] = int(al.group(1))
                if ad: f["adr"] = ad.group(1)
        if "GREEN_EXIT LIVE" in ln or "EXIT-BRAIN" in ln:
            tid = re.search(r"\] (\d{3,})", ln); kind = re.search(r"kind=(\w+)", ln)
            act = "RIDE" if "RIDE" in ln else ("TAKE" if "TAKE" in ln else (kind.group(1) if kind else "?"))
            rem = re.search(r"rem=(-?[\d.]+)p", ln)
            pf = re.search(r"profit=(-?[\d.]+)p", ln) or re.search(r"at \+?(-?[\d.]+)p", ln)
            el = re.search(r"elapsed=(\d+)m", ln)
            ev = {"t": ln[11:16], "trade": tid.group(1) if tid else "?", "action": act,
                  "rem": float(rem.group(1)) if rem else None,
                  "profit": float(pf.group(1)) if pf else None,
                  "elapsed": int(el.group(1)) if el else None}
            exit_feed.append(ev)
            if tid: pos_dec[tid.group(1)] = ev
        ms = re.search(r"\[STRATEGY:(\w+)\]\s+([A-Z_]+)\s+symbol=([A-Z]{3}_[A-Z]{3})", ln)
        if ms:
            strat_tally[ms.group(1)] = strat_tally.get(ms.group(1), 0) + 1
            strat_fires.append({"s": ms.group(1), "sig": ms.group(2), "pair": ms.group(3), "t": ln[11:16]})
        sz = re.search(r"\[SIZING\] ([A-Z]{3}_[A-Z]{3}): risk-capped \d+ -> (\d+)", ln)
        if sz:
            last_size = {"pair": sz.group(1), "units": int(sz.group(2)), "t": ln[11:16]}
    positions = _oanda_open_trades()
    for p in positions:
        p["brain"] = pos_dec.get(p["id"])
    return {
        "brains": {"entry_ev": "armed", "adr_tp": "live", "exit_brain": "live", "sizing": "parked"},
        "exit_brain": positions,
        "exit_feed": exit_feed[-30:][::-1],
        "funnel": funnel,
        "funnel_pass_ev_avg": round(sum(passed_evs) / len(passed_evs), 2) if passed_evs else None,
        "factor_state": sorted(factor.values(), key=lambda x: x["pair"]),
        "strategies": {"fires": strat_fires[-14:][::-1], "tally": strat_tally},
        "sizing": last_size,
        "activity": _recent_activity(lines),
        "account": _oanda_account(),
    }



def create_app(
    live_state: LiveState | None = None,
    config: dict | None = None,
) -> Flask:
    global _live_state
    _live_state = live_state or LiveState()

    config = config or {}
    app = Flask(__name__, template_folder=_TEMPLATE_DIR, static_folder=_STATIC_DIR)
    app.json = _SafeJSONProvider(app)  # set-safe serialization (fixes /api/data 500)

    auth_user = config.get("auth_user", os.environ.get("DASHBOARD_USER", "admin"))
    auth_pass = config.get("auth_pass", os.environ.get("DASHBOARD_PASS", "scrooge"))

    def check_auth(u: str, p: str) -> bool:
        return u == auth_user and p == auth_pass

    def requires_auth(f):
        @functools.wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if auth and check_auth(auth.username, auth.password):
                resp = f(*args, **kwargs)
                if isinstance(resp, Response):
                    resp.set_cookie("sa", "1", httponly=True, samesite="Strict")
                return resp
            if request.cookies.get("sa") == "1":
                return f(*args, **kwargs)
            return Response("Auth required", 401, {"WWW-Authenticate": 'Basic realm="V3"'})
        return decorated

    @app.route("/")
    @requires_auth
    def index():
        return render_template("index.html")

    @app.route("/api/data")
    @requires_auth
    def api_data():
        return jsonify(_live_state.snapshot())

    @app.route("/arcade")
    @requires_auth
    def arcade():
        return render_template("arcade.html")

    @app.route("/api/brain")
    @requires_auth
    def api_brain():
        try:
            return jsonify(_brain_snapshot())
        except Exception as e:  # noqa: BLE001
            log.exception("brain endpoint failed")
            return jsonify({"error": str(e), "exit_brain": [], "exit_feed": [],
                            "funnel": {}, "factor_state": [], "brains": {}})

    @app.route("/api/execution")
    @requires_auth
    def api_execution():
        snap = _live_state.snapshot()
        return jsonify(snap.get("execution", {}))

    return app


def run_dashboard(
    live_state: LiveState | None = None,
    config: dict | None = None,
) -> None:
    config = config or {}
    app = create_app(live_state, config)
    port = config.get("port", 8084)
    log.info("[DASHBOARD] Starting on 127.0.0.1:%d", port)
    app.run(host="127.0.0.1", port=port, debug=False)
