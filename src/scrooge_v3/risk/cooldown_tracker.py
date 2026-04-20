"""Cooldown, zone-blacklist, limit-expiry, and daily-circuit tracking.

Phase 4 - Signal Discipline. Single tracker that owns four related pieces
of state that keep the bot from revenge-trading, thrashing, or blowing
through the daily risk budget:

  1. Post-stopout cooldowns        -> data/cooldowns.json
  2. Zone-loss blacklist           -> data/zone_blacklist.json
  3. Consecutive limit expiries    -> data/limit_expiry_tracker.json
  4. Daily realized loss / circuit -> data/daily_circuit.json

All persist to disk so state survives restarts.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

log = logging.getLogger("scrooge_v3.risk.cooldown_tracker")


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _parse(ts: str | None) -> datetime | None:
    if not ts:
        return None
    try:
        dt = datetime.fromisoformat(ts)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except (ValueError, TypeError):
        return None


def zone_key_for(symbol: str, direction: str, price: float, pips: int = 20) -> str:
    """Bucket an entry price into a zone key rounded to N pips.

    JPY pairs use 0.01 per pip; others use 0.0001. The bucket width is
    ``pips * pip_size``; entries within the same bucket share a zone.
    """
    pip_size = 0.01 if "_JPY" in symbol else 0.0001
    bucket_width = pips * pip_size
    if bucket_width <= 0:
        bucket_width = 0.0020
    bucket = round(price / bucket_width) * bucket_width
    return f"{symbol}:{direction}:{bucket:.5f}"


@dataclass
class CooldownEntry:
    symbol: str
    direction: str
    stopped_at: datetime
    reason: str = "stop_loss"

    def to_dict(self) -> dict:
        return {
            "symbol": self.symbol,
            "direction": self.direction,
            "stopped_at": self.stopped_at.isoformat(),
            "reason": self.reason,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "CooldownEntry":
        return cls(
            symbol=d["symbol"],
            direction=d["direction"],
            stopped_at=_parse(d["stopped_at"]) or _now(),
            reason=d.get("reason", "stop_loss"),
        )


class CooldownTracker:
    """Aggregate risk-discipline state with persistence."""

    def __init__(
        self,
        config: dict | None = None,
        data_dir: Path | None = None,
    ) -> None:
        config = config or {}
        self.cooldown_minutes: int = int(config.get("cooldown_after_stop_minutes", 60))
        self.zone_blacklist_hours: float = float(config.get("zone_blacklist_hours", 4))
        self.zone_bucket_pips: int = int(config.get("zone_bucket_pips", 20))
        self.max_consecutive_expiries: int = int(
            config.get("max_consecutive_expiries", 3)
        )
        self.backoff_minutes: int = int(config.get("backoff_minutes", 30))
        self.max_daily_loss_pct: float = float(config.get("max_daily_loss_pct", 3.0))

        self._data_dir = data_dir or Path("data")
        self._data_dir.mkdir(parents=True, exist_ok=True)

        self._cooldown_path = self._data_dir / "cooldowns.json"
        self._blacklist_path = self._data_dir / "zone_blacklist.json"
        self._expiry_path = self._data_dir / "limit_expiry_tracker.json"
        self._circuit_path = self._data_dir / "daily_circuit.json"

        self._cooldowns: dict[str, CooldownEntry] = {}
        self._zone_blacklist: dict[str, datetime] = {}
        self._expiry_counts: dict[str, dict] = {}
        self._circuit: dict = {
            "utc_date": _now().strftime("%Y-%m-%d"),
            "equity_start": 0.0,
            "realized_pnl": 0.0,
            "tripped": False,
            "tripped_at": None,
        }

        self._load()

    # ------------------------------------------------------------------
    # Keys
    # ------------------------------------------------------------------
    @staticmethod
    def cooldown_key(symbol: str, direction: str) -> str:
        return f"{symbol}:{direction}"

    # ------------------------------------------------------------------
    # Cooldown API (Bug K)
    # ------------------------------------------------------------------
    def record_stop(
        self,
        symbol: str,
        direction: str,
        entry_price: float | None = None,
        when: datetime | None = None,
        reason: str = "stop_loss",
    ) -> None:
        """Record a stop-loss hit. Adds cooldown + zone blacklist."""
        ts = when or _now()
        key = self.cooldown_key(symbol, direction)
        self._cooldowns[key] = CooldownEntry(
            symbol=symbol, direction=direction, stopped_at=ts, reason=reason,
        )
        log.warning(
            "[COOLDOWN] Stop recorded: %s %s at %s - cooldown %dm",
            symbol, direction, ts.isoformat(), self.cooldown_minutes,
        )
        if entry_price is not None:
            self.blacklist_zone(symbol, direction, entry_price, when=ts)
        self._persist_cooldowns()

    def is_in_cooldown(
        self,
        symbol: str,
        direction: str,
        now: datetime | None = None,
    ) -> bool:
        now = now or _now()
        entry = self._cooldowns.get(self.cooldown_key(symbol, direction))
        if entry is None:
            return False
        elapsed = (now - entry.stopped_at).total_seconds() / 60.0
        if elapsed >= self.cooldown_minutes:
            self._cooldowns.pop(self.cooldown_key(symbol, direction), None)
            self._persist_cooldowns()
            return False
        return True

    def cooldown_remaining_minutes(
        self, symbol: str, direction: str, now: datetime | None = None,
    ) -> float:
        now = now or _now()
        entry = self._cooldowns.get(self.cooldown_key(symbol, direction))
        if entry is None:
            return 0.0
        elapsed = (now - entry.stopped_at).total_seconds() / 60.0
        return max(0.0, self.cooldown_minutes - elapsed)

    # ------------------------------------------------------------------
    # Zone blacklist API (Bug L)
    # ------------------------------------------------------------------
    def blacklist_zone(
        self,
        symbol: str,
        direction: str,
        price: float,
        when: datetime | None = None,
    ) -> str:
        ts = when or _now()
        key = zone_key_for(symbol, direction, price, self.zone_bucket_pips)
        self._zone_blacklist[key] = ts
        log.warning(
            "[ZONE_BLACKLIST] %s added (%.1fh window)", key, self.zone_blacklist_hours,
        )
        self._persist_blacklist()
        return key

    def is_zone_blacklisted(
        self,
        symbol: str,
        direction: str,
        price: float,
        now: datetime | None = None,
    ) -> bool:
        now = now or _now()
        key = zone_key_for(symbol, direction, price, self.zone_bucket_pips)
        ts = self._zone_blacklist.get(key)
        if ts is None:
            return False
        elapsed_hours = (now - ts).total_seconds() / 3600.0
        if elapsed_hours >= self.zone_blacklist_hours:
            self._zone_blacklist.pop(key, None)
            self._persist_blacklist()
            return False
        return True

    # ------------------------------------------------------------------
    # Limit expiry anti-thrash (Bug M)
    # ------------------------------------------------------------------
    def _expiry_key(self, symbol: str, direction: str, price: float) -> str:
        return zone_key_for(symbol, direction, price, self.zone_bucket_pips)

    def record_expiry(self, symbol: str, direction: str, price: float) -> int:
        key = self._expiry_key(symbol, direction, price)
        entry = self._expiry_counts.get(key, {"count": 0, "backoff_until": None})
        entry["count"] += 1
        if entry["count"] >= self.max_consecutive_expiries:
            entry["backoff_until"] = (
                _now() + timedelta(minutes=self.backoff_minutes)
            ).isoformat()
            log.warning(
                "[EXPIRY] %s consecutive=%d >= %d - backoff until %s",
                key, entry["count"], self.max_consecutive_expiries,
                entry["backoff_until"],
            )
        self._expiry_counts[key] = entry
        self._persist_expiry()
        return entry["count"]

    def record_fill(self, symbol: str, direction: str, price: float) -> None:
        """A fill resets the consecutive-expiry counter for that zone."""
        key = self._expiry_key(symbol, direction, price)
        if key in self._expiry_counts:
            del self._expiry_counts[key]
            log.info("[EXPIRY] reset on fill: %s", key)
            self._persist_expiry()

    def record_direction_flip(self, symbol: str, new_direction: str) -> None:
        """If the bot flips direction in this symbol, reset opposite keys."""
        opposite = "short" if new_direction == "long" else "long"
        prefix = f"{symbol}:{opposite}:"
        dropped = [k for k in self._expiry_counts if k.startswith(prefix)]
        for k in dropped:
            del self._expiry_counts[k]
        if dropped:
            log.info(
                "[EXPIRY] reset on direction flip: %s->%s (%d keys)",
                symbol, new_direction, len(dropped),
            )
            self._persist_expiry()

    def is_in_expiry_backoff(
        self,
        symbol: str,
        direction: str,
        price: float,
        now: datetime | None = None,
    ) -> bool:
        now = now or _now()
        key = self._expiry_key(symbol, direction, price)
        entry = self._expiry_counts.get(key)
        if not entry:
            return False
        until = _parse(entry.get("backoff_until"))
        if until is None:
            return False
        if now >= until:
            del self._expiry_counts[key]
            self._persist_expiry()
            return False
        return True

    def expiry_count(self, symbol: str, direction: str, price: float) -> int:
        key = self._expiry_key(symbol, direction, price)
        entry = self._expiry_counts.get(key)
        return int(entry.get("count", 0)) if entry else 0

    # ------------------------------------------------------------------
    # Daily circuit breaker (Bug N)
    # ------------------------------------------------------------------
    def start_day(self, equity: float, when: datetime | None = None) -> None:
        ts = when or _now()
        self._circuit = {
            "utc_date": ts.strftime("%Y-%m-%d"),
            "equity_start": float(equity),
            "realized_pnl": 0.0,
            "tripped": False,
            "tripped_at": None,
        }
        self._persist_circuit()
        log.info(
            "[CIRCUIT] Day start: equity=%.2f date=%s",
            equity, self._circuit["utc_date"],
        )

    def maybe_roll_day(self, now: datetime | None = None) -> bool:
        """If UTC date changed, reset the circuit. Returns True if rolled."""
        now = now or _now()
        today = now.strftime("%Y-%m-%d")
        if self._circuit.get("utc_date") != today:
            self._circuit = {
                "utc_date": today,
                "equity_start": self._circuit.get("equity_start", 0.0),
                "realized_pnl": 0.0,
                "tripped": False,
                "tripped_at": None,
            }
            self._persist_circuit()
            log.info("[CIRCUIT] UTC day rolled to %s - resets", today)
            return True
        return False

    def record_realized_pnl(
        self,
        pnl: float,
        equity_start: float | None = None,
        now: datetime | None = None,
    ) -> None:
        now = now or _now()
        self.maybe_roll_day(now)
        if equity_start and self._circuit.get("equity_start", 0.0) <= 0:
            self._circuit["equity_start"] = float(equity_start)
        self._circuit["realized_pnl"] = (
            float(self._circuit.get("realized_pnl", 0.0)) + float(pnl)
        )
        eq = self._circuit.get("equity_start", 0.0)
        if eq > 0:
            pct = (self._circuit["realized_pnl"] / eq) * 100.0
            if pct <= -self.max_daily_loss_pct and not self._circuit.get("tripped"):
                self._circuit["tripped"] = True
                self._circuit["tripped_at"] = now.isoformat()
                tomorrow = (now + timedelta(days=1)).strftime("%Y-%m-%d")
                log.error(
                    "[CIRCUIT] Daily loss limit hit: %.2f%% (%.2f) - "
                    "halting new entries until %s 00:00 UTC",
                    pct, self._circuit["realized_pnl"], tomorrow,
                )
        self._persist_circuit()

    def is_circuit_tripped(self, now: datetime | None = None) -> bool:
        now = now or _now()
        self.maybe_roll_day(now)
        return bool(self._circuit.get("tripped"))

    def circuit_snapshot(self) -> dict:
        return dict(self._circuit)

    # ------------------------------------------------------------------
    # Context helpers (for gate plumbing)
    # ------------------------------------------------------------------
    def to_state_dict(self) -> dict:
        """Produce a dict that gates can read from ``ctx.state``."""
        return {
            "cooldowns": {k: v.to_dict() for k, v in self._cooldowns.items()},
            "zone_blacklist": {
                k: v.isoformat() for k, v in self._zone_blacklist.items()
            },
            "limit_expiry": {
                k: {
                    "count": v.get("count", 0),
                    "backoff_until": v.get("backoff_until"),
                }
                for k, v in self._expiry_counts.items()
            },
            "daily_circuit": dict(self._circuit),
            "risk_config": {
                "cooldown_after_stop_minutes": self.cooldown_minutes,
                "zone_blacklist_hours": self.zone_blacklist_hours,
                "zone_bucket_pips": self.zone_bucket_pips,
                "max_consecutive_expiries": self.max_consecutive_expiries,
                "backoff_minutes": self.backoff_minutes,
                "max_daily_loss_pct": self.max_daily_loss_pct,
            },
        }

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------
    def _persist_cooldowns(self) -> None:
        data = {k: v.to_dict() for k, v in self._cooldowns.items()}
        self._write(self._cooldown_path, data)

    def _persist_blacklist(self) -> None:
        data = {k: v.isoformat() for k, v in self._zone_blacklist.items()}
        self._write(self._blacklist_path, data)

    def _persist_expiry(self) -> None:
        self._write(self._expiry_path, self._expiry_counts)

    def _persist_circuit(self) -> None:
        self._write(self._circuit_path, self._circuit)

    @staticmethod
    def _write(path: Path, data: Any) -> None:
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, "w") as f:
                json.dump(data, f, indent=2, default=str)
        except Exception:
            log.exception("[COOLDOWN] Failed to persist %s", path)

    def _load(self) -> None:
        if self._cooldown_path.exists():
            try:
                with open(self._cooldown_path) as f:
                    data = json.load(f)
                self._cooldowns = {
                    k: CooldownEntry.from_dict(v) for k, v in data.items()
                }
            except Exception:
                log.exception("[COOLDOWN] Failed to load cooldowns")

        if self._blacklist_path.exists():
            try:
                with open(self._blacklist_path) as f:
                    data = json.load(f)
                self._zone_blacklist = {}
                for k, v in data.items():
                    ts = _parse(v)
                    if ts:
                        self._zone_blacklist[k] = ts
            except Exception:
                log.exception("[COOLDOWN] Failed to load zone blacklist")

        if self._expiry_path.exists():
            try:
                with open(self._expiry_path) as f:
                    self._expiry_counts = json.load(f)
            except Exception:
                log.exception("[COOLDOWN] Failed to load expiry tracker")

        if self._circuit_path.exists():
            try:
                with open(self._circuit_path) as f:
                    self._circuit = json.load(f)
            except Exception:
                log.exception("[COOLDOWN] Failed to load daily circuit")
