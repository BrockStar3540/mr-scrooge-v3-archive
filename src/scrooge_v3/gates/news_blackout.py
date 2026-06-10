"""News blackout gate - blocks new entries around scheduled economic releases.

Born 2026-06-10 (May-CPI day): the bot entered fresh AUD shorts at 12:18/12:19
UTC, eleven minutes before the 12:30 UTC CPI print, and had four positions
stopped in the same second. All 14 factor buckets are backward-looking
price/vol measures -- nothing in the model can see a scheduled release coming,
so the calendar veto lives here, outside the model.

Calendar: ``config/econ_calendar.json`` -- static UTC timestamps taken from the
official BLS/OMB/Fed schedules (published ~a year ahead). The file is reloaded
on mtime change so it can be extended without a restart. When the last entry
is within ``stale_warn_days`` of now, evaluations log a warning so the file
gets refilled before it silently runs dry (an empty calendar blocks nothing).
"""

from __future__ import annotations

import json
import os
import time
from datetime import datetime, timezone
from typing import Any

from scrooge_v3.core.types import GateMode, GateResult, SymbolContext, TradeCandidate

from .base import BaseGate

# (pre_minutes, post_minutes) by event impact when config doesn't override
DEFAULT_WINDOWS = {"high": (45, 20), "medium": (30, 15)}


class NewsBlackoutGate(BaseGate):
    """Hard-block new entries inside the window around a scheduled release.

    Only affects NEW entries -- open positions and exits are untouched
    (exits must always be allowed to fire).
    """

    name = "news_blackout"

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        mode: GateMode = GateMode.HARD,
    ) -> None:
        super().__init__(config, mode)
        self.calendar_file = self.config.get(
            "calendar_file", "config/econ_calendar.json"
        )
        raw = self.config.get("windows") or {}
        self.windows: dict[str, tuple[int, int]] = dict(DEFAULT_WINDOWS)
        for impact, pair in raw.items():
            try:
                self.windows[impact] = (int(pair[0]), int(pair[1]))
            except Exception:
                pass
        self.stale_warn_days = int(self.config.get("stale_warn_days", 30))
        self._events: list[dict] = []
        self._mtime: float = -1.0
        self._last_stale_warn: float = 0.0
        self._load()

    # --- calendar loading -------------------------------------------------

    def _load(self) -> None:
        try:
            mtime = os.path.getmtime(self.calendar_file)
        except OSError:
            self._log.error(
                "[NEWS_BLACKOUT] calendar file missing: %s -- gate blocks "
                "nothing until it exists", self.calendar_file,
            )
            self._events = []
            self._mtime = -1.0
            return
        if mtime == self._mtime:
            return
        try:
            with open(self.calendar_file) as f:
                data = json.load(f)
            events = []
            for ev in data.get("events", []):
                ts = datetime.fromisoformat(ev["utc"].replace("Z", "+00:00"))
                events.append({
                    "ts": ts,
                    "name": ev.get("name", "?"),
                    "impact": ev.get("impact", "high"),
                    "currencies": set(ev.get("currencies", ["USD"])),
                })
            events.sort(key=lambda e: e["ts"])
            self._events = events
            self._mtime = mtime
            self._log.info(
                "[NEWS_BLACKOUT] calendar loaded: %d events, last %s",
                len(events), events[-1]["ts"].isoformat() if events else "n/a",
            )
        except Exception:
            # Keep the previously-loaded calendar on a bad edit.
            self._log.exception(
                "[NEWS_BLACKOUT] failed to parse %s -- keeping %d cached "
                "events", self.calendar_file, len(self._events),
            )

    def _now(self) -> datetime:
        return datetime.now(timezone.utc)

    def _warn_if_stale(self, now: datetime) -> None:
        if not self._events:
            return
        horizon = (self._events[-1]["ts"] - now).total_seconds() / 86400.0
        if horizon < self.stale_warn_days and time.time() - self._last_stale_warn > 3600:
            self._last_stale_warn = time.time()
            self._log.warning(
                "[NEWS_BLACKOUT] calendar runs out in %.0f days (last event "
                "%s) -- refill %s from the BLS/OMB/Fed schedules",
                horizon, self._events[-1]["ts"].date(), self.calendar_file,
            )

    # --- evaluation -------------------------------------------------------

    def evaluate(
        self, candidate: TradeCandidate, ctx: SymbolContext
    ) -> GateResult:
        self._load()  # mtime-cached; picks up calendar edits without restart
        now = self._now()
        self._warn_if_stale(now)
        legs = set(candidate.symbol.split("_"))

        nxt = None  # next matching event, for the pass-reason
        for ev in self._events:
            if not (legs & ev["currencies"]):
                continue
            pre, post = self.windows.get(ev["impact"], DEFAULT_WINDOWS["high"])
            delta_min = (ev["ts"] - now).total_seconds() / 60.0
            if -post <= delta_min <= pre:
                when = (
                    f"{delta_min:.0f}m before" if delta_min >= 0
                    else f"{-delta_min:.0f}m after"
                )
                return GateResult(
                    gate_name=self.name,
                    passed=False,
                    reason=(
                        f"BLACKOUT {ev['name']} at "
                        f"{ev['ts'].strftime('%H:%M')}Z ({when} release, "
                        f"window -{pre}m/+{post}m)"
                    ),
                    metrics={
                        "event": ev["name"],
                        "impact": ev["impact"],
                        "minutes_to_release": round(delta_min, 1),
                    },
                )
            if delta_min > pre and nxt is None:
                nxt = (ev, delta_min)

        if nxt:
            reason = (
                f"clear; next: {nxt[0]['name']} in {nxt[1] / 60.0:.1f}h"
            )
        else:
            reason = "clear; no upcoming calendar events"
        return GateResult(
            gate_name=self.name,
            passed=True,
            reason=reason,
            metrics={"score": 1.0},
        )
