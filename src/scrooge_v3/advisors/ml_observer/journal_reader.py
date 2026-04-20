# ============================================================
# Copyright (c) Carl Brock 2026. All rights reserved.
# ============================================================
"""
ML Observer — journald reader.

Pulls new V3 service log entries since a persisted cursor, classifies each
line, and yields (category, record) pairs for the observer to route to
the appropriate output file (scans, actions, bot-logs).

Uses `journalctl --cursor-file=<path> -o json` subprocess — this is the
standard incremental-read pattern. No systemd-python dependency.

Categories emitted:
  - "scorer_line"    : raw V3_SCORER log line → observer merges with API
                       for scans.jsonl
  - "gate"           : [GATE:X] PASSED|FAILED line
  - "sizing"         : [SIZING] units/equity/margin decision
  - "exec"           : ORDER placement / fill / cancellation
  - "tracker"        : [TRACKER] position updates (SL move, BE, TP1, etc.)
  - "recovery"       : [RECOVERY] reconcile events
  - "circuit"        : [CIRCUIT] daily PnL trip / reset events
  - "cooldown"       : cooldown_tracker events
  - "warning"        : WARNING severity — routed to bot-logs
  - "error"          : ERROR severity — routed to bot-logs
  - "other"          : everything else, filtered against a noise list

The classifier is deliberately coarse: if the substring matches a known
tag, we emit the category plus the FULL raw message. Downstream the
observer persists the raw message verbatim so nothing is lost; any future
refinement can re-parse from raw data on disk.
"""

from __future__ import annotations

import json
import logging
import re
import subprocess
from pathlib import Path
from typing import Iterator, Optional

log = logging.getLogger("ml-observer.journal")

# Messages we drop outright — extremely high-frequency lines that would
# swamp bot-logs.jsonl with noise but carry no ML signal.
_NOISE_PATTERNS = (
    re.compile(r"Percentile filter"),
    re.compile(r"Insufficient bars"),
    re.compile(r"502 Bad Gateway"),
    re.compile(r"\[BOOT\] "),
    re.compile(r"Position pipeline initialized"),
    re.compile(r"^\s*$"),
)

# Category regex map (checked in order; first match wins).
# Each pattern is compiled from a substring token for speed.
_CATEGORY_RULES: list[tuple[str, re.Pattern]] = [
    ("scorer_line", re.compile(r"\[V3_SCORER\]")),
    ("gate",       re.compile(r"\[GATE:[A-Za-z_]+\]")),
    ("sizing",     re.compile(r"\[SIZING\]")),
    ("exec",       re.compile(r"\[EXEC\]|ORDER_FILL|ORDER_PLACED|ORDER_CANCEL|"
                              r"ORDER_EXPIRED|tradeOpened|tradeClosed")),
    ("tracker",    re.compile(r"\[TRACKER\]|SL_MOVED|break_even|tp1_taken|"
                              r"harvest|ratchet|trail")),
    ("recovery",   re.compile(r"\[RECOVERY\]|reconcil")),
    ("circuit",    re.compile(r"\[CIRCUIT\]")),
    ("cooldown",   re.compile(r"cooldown_tracker|cooldown_triggered|"
                              r"zone_blacklist")),
    ("positions",  re.compile(r"\[POSITIONS\]")),
    ("scan",       re.compile(r"\[SCAN\]")),
]


def _is_noise(msg: str) -> bool:
    return any(rx.search(msg) for rx in _NOISE_PATTERNS)


def _classify(msg: str, priority: Optional[str]) -> str:
    """Return the category for this message."""
    for cat, rx in _CATEGORY_RULES:
        if rx.search(msg):
            return cat
    # journald priority: 3=ERR, 4=WARNING, 6=INFO
    if priority == "3":
        return "error"
    if priority == "4":
        return "warning"
    return "other"


def iter_journal_events(
    unit: str,
    cursor_file: Path,
    max_entries: int = 5000,
) -> Iterator[tuple[str, dict]]:
    """
    Read new journald entries for `unit` since the persisted cursor.

    Uses `journalctl --cursor-file=<path>` which both reads the cursor
    before running AND writes an updated cursor on exit — so we always
    resume from exactly where we left off.

    Yields (category, record) tuples. Record shape:
        {
            "ts": "2026-04-20T14:46:08.123456+00:00",
            "priority": "6",
            "logger": "scrooge_v3.strategies.v3_scorer",  # best-effort
            "level": "INFO",
            "message": "<full MESSAGE field from journald>",
            "raw": "<original line>",
        }

    If journalctl fails or the unit has no new entries, yields nothing.
    """
    cursor_file.parent.mkdir(parents=True, exist_ok=True)

    # `--cursor-file` is idempotent: reads old cursor, writes new one on exit.
    # `-n <N>` caps how many entries we pull so a first-run catch-up can't OOM.
    # On very first run there's no file yet; journalctl treats that as
    # "start from now". Use `--since=-10m` only if the cursor file is missing.
    args = [
        "journalctl",
        "--user",
        "-u", unit,
        "--cursor-file", str(cursor_file),
        "-n", str(max_entries),
        "-o", "json",
        "--no-pager",
    ]
    if not cursor_file.exists():
        args.extend(["--since", "-5min"])

    try:
        proc = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except FileNotFoundError:
        log.warning("journalctl not available — journal reader disabled")
        return

    assert proc.stdout is not None
    try:
        for line in proc.stdout:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            msg = entry.get("MESSAGE", "")
            if not msg or _is_noise(msg):
                continue
            # __REALTIME_TIMESTAMP is microseconds since epoch
            ts_us = entry.get("__REALTIME_TIMESTAMP")
            try:
                ts_us_i = int(ts_us) if ts_us else None
            except (TypeError, ValueError):
                ts_us_i = None
            from datetime import datetime, timezone
            ts_iso = (
                datetime.fromtimestamp(ts_us_i / 1_000_000, tz=timezone.utc).isoformat()
                if ts_us_i else ""
            )
            priority = entry.get("PRIORITY")
            level = {"3": "ERROR", "4": "WARNING", "6": "INFO"}.get(priority or "", "INFO")
            # Best-effort logger name: our app logs "YYYY-MM-DD HH:MM:SS [LEVEL] logger — message"
            logger_name = ""
            m = re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[[A-Z]+\] ([A-Za-z0-9_.]+)", msg)
            if m:
                logger_name = m.group(1)

            category = _classify(msg, priority)

            yield category, {
                "ts": ts_iso,
                "priority": priority or "",
                "logger": logger_name,
                "level": level,
                "message": msg,
            }
    finally:
        try:
            proc.stdout.close()
        except Exception:
            pass
        proc.wait(timeout=5)
        if proc.returncode not in (0, None):
            stderr = proc.stderr.read() if proc.stderr else ""
            if stderr.strip():
                log.debug("journalctl rc=%s stderr=%s", proc.returncode, stderr.strip())


__all__ = ["iter_journal_events"]
