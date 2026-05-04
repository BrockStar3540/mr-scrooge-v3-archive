"""State recovery — handles trade reconciliation and vanished trade detection.

Extracted from Runtime._run_cycle() (vanished trade detection) and
Runtime._reconcile_pending_orders() to isolate recovery/reconciliation
logic from normal trading flow.
"""

from __future__ import annotations

import json
import logging
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

log = logging.getLogger("scrooge_v3.services.state_recovery")

# --- Harvest LIMIT lifecycle safety (hotfix/stale-harvest-limit) ---------
# 60-day audit found 8 cases of harvest LIMITs surviving parent close and
# later firing as naked positions with no SL/TP. Three independent guards:
#   1. GTD on every harvest LIMIT (hard ceiling at the broker)
#   2. Cancellation on any parent-close path (vanish reconcile)
#   3. Periodic orphan-LIMIT sweep using a persisted harvest ledger
#
# GTD windows are bounded by typical strategy holding profile, NOT pure GTC.
# Hardcoded here because V3 strategy metadata does not currently expose a
# holding/management timeout. If/when it does, switch to that source.
_HARVEST_GTD_HOURS_BY_STRATEGY = {
    "dbb_trend": 12,
    # direct + box-like fallbacks all use 4h
}
_HARVEST_GTD_DEFAULT_HOURS = 4

# Persisted ledger of every harvest order_id we have ever placed. Survives
# restart so we can still cancel orphans even if the tracker entry has been
# removed/corrupted/lost.
_HARVEST_LEDGER_PATH = Path("data/harvest-order-ledger.json")


def _harvest_gtd_hours(strategy: str | None) -> int:
    if not strategy:
        return _HARVEST_GTD_DEFAULT_HOURS
    return _HARVEST_GTD_HOURS_BY_STRATEGY.get(strategy, _HARVEST_GTD_DEFAULT_HOURS)


def _format_gtd(now: datetime, hours: int) -> str:
    """OANDA RFC3339 nano-precision GTD timestamp."""
    expires = now + timedelta(hours=hours)
    return expires.strftime("%Y-%m-%dT%H:%M:%S.000000000Z")


class HarvestLedger:
    """Persisted order_id -> trade_id map for harvest LIMITs.

    Used purely for orphan reconciliation. Authoritative tracker state still
    lives on TrackedPosition.harvest_order_id; this is a redundant pointer so
    we can clean up even when the tracker entry is gone.
    """

    def __init__(self, path: Path = _HARVEST_LEDGER_PATH):
        self._path = path
        self._entries: dict[str, dict[str, Any]] = {}
        self._load()

    def _load(self) -> None:
        if not self._path.exists():
            return
        try:
            with open(self._path) as f:
                self._entries = json.load(f)
        except Exception:
            log.exception("[HARVEST-LEDGER] failed to load %s", self._path)
            self._entries = {}

    def _save(self) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "w") as f:
                json.dump(self._entries, f, indent=2)
        except Exception:
            log.exception("[HARVEST-LEDGER] failed to save %s", self._path)

    def add(self, order_id: str, trade_id: str, symbol: str,
            strategy: str, gtd_time: str) -> None:
        if not order_id:
            return
        self._entries[order_id] = {
            "trade_id": trade_id,
            "symbol": symbol,
            "strategy": strategy,
            "gtd_time": gtd_time,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        self._save()

    def remove(self, order_id: str) -> None:
        if order_id in self._entries:
            self._entries.pop(order_id, None)
            self._save()

    def all(self) -> dict[str, dict[str, Any]]:
        return dict(self._entries)


# Module-global ledger instance — single shared file.
_HARVEST_LEDGER = HarvestLedger()


class StateRecovery:
    """Reconciles broker state with local tracker state each cycle."""

    def __init__(self, ctx: Any):
        self.ctx = ctx
        self._ledger = _HARVEST_LEDGER

    # ------------------------------------------------------------------
    # Harvest LIMIT lifecycle safety helpers
    # ------------------------------------------------------------------

    def _audit_harvest(self, etype: str, reason: str,
                       *, trade_id: str = "", order_id: str = "",
                       symbol: str = "", strategy: str = "",
                       gtd_time: str = "", created_at: str = "",
                       management_profile: str = "") -> None:
        """Append a harvest-lifecycle event to data/execution-audit.jsonl.

        Reuses the existing ExecutionAudit channel so dashboards and downstream
        readers don't need a new file. Falls back silently if audit is missing.
        """
        audit = getattr(self.ctx, "execution_audit", None)
        if audit is None:
            return
        try:
            from scrooge_v3.telemetry.execution_audit import AuditEvent
            extra: dict[str, Any] = {}
            if order_id:
                extra["order_id"] = order_id
            if gtd_time:
                extra["gtd_time"] = gtd_time
            if created_at:
                extra["created_at"] = created_at
            if management_profile:
                extra["management_profile"] = management_profile
            if etype.endswith("_cancelled"):
                extra["cancelled_at"] = datetime.now(timezone.utc).isoformat()
            audit.record(AuditEvent(
                type=etype, reason=reason,
                trade_id=trade_id, symbol=symbol,
                strategy=strategy or "",
                extra=extra,
            ))
        except Exception:
            log.exception("[HARVEST-AUDIT] record failed (%s)", etype)

    def _cancel_harvest_for_trade(self, tracked: Any, reason: str) -> None:
        """Cancel a harvest LIMIT for a trade and audit-log it.

        Idempotent: returns silently if the trade has no harvest order.
        Used by all parent-close paths (vanish reconcile, orphan sweep, and
        any explicit close path that wires this in).
        """
        if not tracked:
            return
        order_id = getattr(tracked, "harvest_order_id", "") or ""
        if not order_id:
            return
        ok = False
        try:
            ok = bool(self.ctx.broker.cancel_order(order_id))
        except Exception:
            log.exception("[RECOVERY] cancel_order raised for %s (trade=%s)",
                          order_id, getattr(tracked, "trade_id", ""))
        log.info("[RECOVERY] Harvest LIMIT cancel: order=%s trade=%s ok=%s reason=%s",
                 order_id, getattr(tracked, "trade_id", ""), ok, reason)
        # Always clear local pointer + ledger; if broker rejected (already
        # gone / already filled), GTD will catch any zombie anyway.
        try:
            self.ctx.tracker.clear_harvest_order(getattr(tracked, "trade_id", ""))
        except Exception:
            pass
        self._ledger.remove(order_id)
        self._audit_harvest(
            "harvest_limit_cancelled", reason,
            trade_id=getattr(tracked, "trade_id", ""),
            order_id=order_id,
            symbol=getattr(tracked, "symbol", ""),
            strategy=getattr(tracked, "strategy", ""),
        )

    def detect_vanished_trades(self) -> None:
        """Detect trades closed externally between cycles."""
        ctx = self.ctx
        current_trades = ctx.broker.get_open_trades()
        current_ids = {t.trade_id for t in current_trades}
        vanished = ctx.known_trade_ids - current_ids

        if vanished:
            for tid in vanished:
                log.warning("[RECOVERY] Trade vanished (closed externally): %s", tid)
                ctx.state.decrement_positions()

        ctx.known_trade_ids = current_ids
        ctx.state.position_count = len(current_trades)

    def reconcile_tracker(self) -> None:
        """Reconcile position tracker with broker — detect vanished tracked positions."""
        ctx = self.ctx
        open_trades = ctx.broker.get_open_trades()
        broker_ids = {t.trade_id for t in open_trades}

        # Phase 4: snapshot tracked positions BEFORE reconcile strips
        # them, so signal-discipline can inspect entry/stop/direction.
        pre_snapshot: dict[str, Any] = {}
        try:
            for _tid, _pos in ctx.tracker._positions.items():
                pre_snapshot[_tid] = _pos
        except Exception:
            pre_snapshot = {}

        vanished = ctx.tracker.reconcile_with_broker(broker_ids)

        for tid in vanished:
            tracked = pre_snapshot.get(tid) or ctx.tracker.get(tid)
            if tracked and getattr(tracked, "harvest_order_id", ""):
                # Hotfix: parent vanished (SL hit, manual close, full TP, or
                # any other broker-side exit) -> cancel any outstanding
                # harvest LIMIT and audit-log it. Must run before tracker
                # entry is gone or we lose the order_id pointer.
                self._cancel_harvest_for_trade(tracked, "parent_vanished")

            # Phase 4: classify vanish, book realized PnL, cooldown + blacklist.
            try:
                self._record_vanish_for_signal_discipline(tid, tracked)
            except Exception:
                log.exception("[RECOVERY] signal-discipline hook failed: %s", tid)

            ctx.state.decrement_positions()

        ctx.state.position_count = len(open_trades)
        return open_trades

    def _record_vanish_for_signal_discipline(
        self, trade_id: str, tracked: Any,
    ) -> None:
        """Record cooldown/blacklist and daily PnL on a vanished trade.

        Heuristic for SL-hit: use the broker's realized-PnL-today delta
        since the last sample. A non-positive delta classifies as a
        stop-loss and records a cooldown + zone blacklist. All deltas
        feed the daily circuit breaker.
        """
        ctx = self.ctx
        tracker_obj = getattr(ctx, "cooldown_tracker", None)
        if tracker_obj is None:
            return

        broker = ctx.broker
        # Per-trade close attribution. Previously we used the brokers daily
        # P&L delta to estimate this trades P&L, but if two trades vanish
        # in the same cycle the first consumes the whole delta and the
        # second is wrongly tagged as a stop-loss. Now we ask OANDA for the
        # trades own realizedPL, which is the truthful per-close number.
        pnl_delta = 0.0
        per_trade_pl = None
        try:
            if hasattr(broker, "get_trade"):
                tdata = broker.get_trade(trade_id)
                if tdata is not None:
                    raw_pl = tdata.get("realizedPL")
                    if raw_pl is not None:
                        per_trade_pl = float(raw_pl)
                        # Add financing if present, subtract commission.
                        per_trade_pl += float(tdata.get("financing", 0) or 0)
        except Exception:
            log.exception("[RECOVERY] get_trade(%s) failed; falling back to daily delta", trade_id)

        if per_trade_pl is not None:
            pnl_delta = per_trade_pl
        else:
            # Fallback: legacy daily-aggregate delta heuristic.
            try:
                total_today = 0.0
                if hasattr(broker, "get_realized_pl_today"):
                    total_today = float(broker.get_realized_pl_today() or 0.0)
                last = getattr(ctx, "_last_realized_pl_today", 0.0)
                pnl_delta = total_today - last
                ctx._last_realized_pl_today = total_today
                log.warning("[RECOVERY] using daily-delta fallback for %s pnl=%.2f", trade_id, pnl_delta)
            except Exception:
                log.exception("[RECOVERY] failed to read realized_pl_today")

        acct = None
        try:
            acct = broker.get_account()
        except Exception:
            acct = None
        equity_ref = getattr(acct, "equity", None) if acct else None
        if pnl_delta != 0.0:
            tracker_obj.record_realized_pnl(
                pnl_delta, equity_start=equity_ref,
            )

        if tracked is None:
            return
        if pnl_delta <= 0:
            symbol = getattr(tracked, "symbol", None)
            direction = getattr(tracked, "direction", None)
            entry_price = getattr(tracked, "entry_price", None)
            if symbol and direction:
                tracker_obj.record_stop(
                    symbol=symbol,
                    direction=direction,
                    entry_price=entry_price,
                    reason="stop_loss_or_close",
                )
                log.warning(
                    "[RECOVERY] SL classification: %s %s %s pnl_delta=%.2f "
                    "-> cooldown + blacklist",
                    trade_id, symbol, direction, pnl_delta,
                )

    def reconcile_pending_orders(self) -> None:
        """Reconcile pending entry and harvest limit orders with OANDA."""
        ctx = self.ctx
        pending_on_broker = {o.order_id for o in ctx.broker.get_pending_orders()}
        # Hotfix/harvest-same-cycle-race (2026-04-30):
        # Harvest LIMITs placed by _place_harvest_limit during the entry-fill
        # loop below are not in `pending_on_broker` (snapshot taken before).
        # Track them locally and union before the harvest-reconcile loop so
        # newly-placed orders aren't immediately marked broker_side_gone.
        freshly_placed: set[str] = set()

        # Check pending entries
        for symbol, order_id in list(ctx.tracker.all_pending_entries().items()):
            if order_id in pending_on_broker:
                continue  # Still pending, wait

            # Order gone — check if it filled (new trade appeared)
            open_trades = ctx.broker.get_open_trades()
            new_trade = None
            for t in open_trades:
                if t.symbol == symbol and not ctx.tracker.get(t.trade_id):
                    new_trade = t
                    break

            if new_trade:
                meta = ctx.tracker.get_pending_entry_meta(symbol)
                ctx.tracker.register_entry(
                    trade_id=new_trade.trade_id,
                    symbol=new_trade.symbol,
                    direction=new_trade.direction,
                    units=new_trade.units,
                    entry_price=new_trade.entry_price,
                    stop_price=new_trade.current_stop,
                    tp_price=new_trade.current_tp,
                    tp1_price=meta.get("tp1_price", 0),
                    tp2_price=new_trade.current_tp,
                    strategy=meta.get("strategy", "limit_fill"),
                    v3_score=meta.get("v3_score", 0),
                    metadata=meta.get("metadata", {}),
                )
                ctx.state.position_count += 1
                ctx.state.record_zone_entry(symbol, f"{new_trade.current_stop:.5f}")
                log.info("[RECOVERY] LIMIT ENTRY FILLED: %s %s @ %.5f (order %s)",
                         new_trade.trade_id, symbol, new_trade.entry_price, order_id)
                # Phase 4: fill resets expiry counter.
                tracker_obj = getattr(ctx, "cooldown_tracker", None)
                if tracker_obj is not None:
                    try:
                        tracker_obj.record_fill(
                            symbol, new_trade.direction, new_trade.entry_price,
                        )
                    except Exception:
                        log.exception("[RECOVERY] expiry reset on fill failed")
                ctx.tracker.clear_pending_entry(symbol)
                # Place harvest limit for the new trade
                new_harvest_id = self._place_harvest_limit(
                    ctx.tracker.get(new_trade.trade_id)
                )
                if new_harvest_id:
                    freshly_placed.add(new_harvest_id)
            else:
                # Order expired or was cancelled
                meta = ctx.tracker.get_pending_entry_meta(symbol) or {}
                ctx.tracker.clear_pending_entry_meta(symbol)
                ctx.tracker.clear_pending_entry(symbol)
                log.info("[RECOVERY] LIMIT ENTRY EXPIRED: %s order=%s", symbol, order_id)
                # Phase 4: feed expiry tracker for anti-thrash.
                tracker_obj = getattr(ctx, "cooldown_tracker", None)
                if tracker_obj is not None:
                    try:
                        direction = meta.get("direction")
                        anchor = (
                            meta.get("entry_price")
                            or meta.get("stop_loss")
                            or 0.0
                        )
                        if direction and anchor:
                            tracker_obj.record_expiry(
                                symbol, direction, float(anchor),
                            )
                    except Exception:
                        log.exception("[RECOVERY] expiry tracker hook failed")

        # Check harvest orders
        # Union same-cycle placements into the broker-pending view (see
        # hotfix note above): orders placed earlier in this function call
        # are not in the original snapshot and would otherwise misclassify
        # as broker_side_gone.
        pending_on_broker |= freshly_placed
        for tracked in ctx.tracker.get_positions_with_harvest_orders():
            if tracked.harvest_order_id in pending_on_broker:
                continue  # Still pending

            broker_trade = next(
                (t for t in ctx.broker.get_open_trades() if t.trade_id == tracked.trade_id),
                None,
            )
            order_id = tracked.harvest_order_id
            if broker_trade and broker_trade.units < tracked.units:
                old_units = tracked.units
                # Sync unit truth BEFORE flag — so downstream reads see the
                # correct remaining size if they happen between these calls.
                ctx.tracker.update_units(tracked.trade_id, broker_trade.units)
                ctx.tracker.mark_tp1_taken(tracked.trade_id)
                ctx.tracker.clear_harvest_order(tracked.trade_id)
                self._ledger.remove(order_id)
                log.info("[RECOVERY] HARVEST LIMIT FILLED: %s units %.0f → %.0f",
                         tracked.trade_id, old_units, broker_trade.units)
                # Dust check — if the remaining size is below threshold,
                # flatten the residual so we don't carry orphan units.
                self._maybe_flatten_dust(tracked, broker_trade.units)
            else:
                ctx.tracker.clear_harvest_order(tracked.trade_id)
                self._ledger.remove(order_id)
                log.info("[RECOVERY] HARVEST LIMIT CANCELLED: %s order=%s",
                         tracked.trade_id, order_id)
                self._audit_harvest(
                    "harvest_limit_cancelled", "broker_side_gone",
                    trade_id=tracked.trade_id, order_id=order_id,
                    symbol=getattr(tracked, "symbol", ""),
                    strategy=getattr(tracked, "strategy", ""),
                )

    # ------------------------------------------------------------------
    # Orphan-harvest sweep — broker-first walk
    # ------------------------------------------------------------------
    # Hotfix/orphan-sweep-broker-walk (2026-04-29)
    # The 2026-04-29 (4ad40b3) hotfix caught harvest LIMITs placed AFTER
    # deploy but missed pre-deploy orphans because the original sweep walked
    # only the persisted ledger. Today the user manually closed 7 broker-
    # side orphan LIMITs the ledger never knew about.
    #
    # The fix: walk broker pending orders FIRST. If a pending order looks
    # unambiguously like a harvest-style reduce LIMIT and its parent trade
    # is dead on broker AND not in tracker, cancel it -- ledger entry or no
    # ledger entry. The ledger walk is kept (housekeeping pass to drop
    # dead/filled entries) so behaviour is a strict superset of before.
    #
    # Safety budget: this sweep ONLY ever calls cancel_order on orders that
    # match all four signals below. Any ambiguity -> skip. We would rather
    # leave a real orphan for one cycle than cancel a legitimate entry/SL/TP.
    _HARVEST_LIMIT_TYPES = ("LIMIT_ORDER", "LIMIT")

    @staticmethod
    def _is_harvest_style_reduce_limit(order: Any) -> bool:
        """Tight signature for a V3-placed harvest LIMIT.

        REQUIRED (all must hold):
          1. order_type is a LIMIT (not STOP_LOSS_ORDER, not TAKE_PROFIT_ORDER,
             not MARKET_IF_TOUCHED, not anything else).
          2. position_fill == "REDUCE_ONLY" -- this is what _place_harvest_limit
             stamps onto every harvest LIMIT request and is the cleanest way
             to distinguish from entry LIMITs (which carry "DEFAULT").
          3. parent_trade_id is non-empty -- harvest LIMITs reference the
             trade they're reducing; entry LIMITs do not.

        Anything that fails any of these is left alone.
        """
        order_type = (getattr(order, "order_type", "") or "").upper()
        if order_type not in StateRecovery._HARVEST_LIMIT_TYPES:
            return False
        if (getattr(order, "position_fill", "") or "").upper() != "REDUCE_ONLY":
            return False
        if not (getattr(order, "parent_trade_id", "") or "").strip():
            return False
        return True

    def reconcile_orphan_harvests(self) -> None:
        """Cancel any harvest LIMIT whose parent trade is no longer alive.

        Broker-first walk (covers pre-deploy orphans + state-loss cases):
          1. Pull broker pending orders.
          2. For each one that unambiguously matches the harvest-style
             reduce-LIMIT signature: if the parent trade is dead on broker
             AND absent from tracker -> orphan -> cancel + audit.
          3. Skip (don't cancel) anything that doesn't match the signature
             -- this includes entry LIMITs, SL/TP, and any LIMIT we can't
             identify a parent for.
          4. Then walk the ledger and drop dead/filled ledger entries
             (housekeeping; tracker hooks own the live-trade case).

        Called from Runtime._run_cycle() each cycle alongside the existing
        reconcile_pending_orders() call.
        """
        ctx = self.ctx

        try:
            pending_list = list(ctx.broker.get_pending_orders())
        except Exception:
            log.exception("[RECOVERY] orphan-harvest sweep: get_pending_orders failed")
            return
        try:
            open_trade_ids = {t.trade_id for t in ctx.broker.get_open_trades()}
        except Exception:
            log.exception("[RECOVERY] orphan-harvest sweep: get_open_trades failed")
            return

        ledger = self._ledger.all()
        pending_by_id: dict[str, Any] = {o.order_id: o for o in pending_list}
        orphans_found = 0

        for order in pending_list:
            order_type = (getattr(order, "order_type", "") or "").upper()
            order_id = getattr(order, "order_id", "")
            symbol = getattr(order, "symbol", "")

            # Hard skip everything that isn't a LIMIT order.  STOP_LOSS_ORDER
            # and TAKE_PROFIT_ORDER are managed by OANDA and must never be
            # touched by this sweep regardless of parent state.
            if order_type not in self._HARVEST_LIMIT_TYPES:
                continue

            if not self._is_harvest_style_reduce_limit(order):
                # Entry LIMIT (DEFAULT positionFill, no parent), or a LIMIT
                # we can't classify with confidence -> leave it alone.
                if not (getattr(order, "parent_trade_id", "") or "").strip():
                    log.debug(
                        "[RECOVERY] orphan-harvest sweep: skip non-reduce LIMIT "
                        "order=%s symbol=%s position_fill=%s",
                        order_id, symbol,
                        getattr(order, "position_fill", "") or "",
                    )
                continue

            parent_trade_id = (order.parent_trade_id or "").strip()
            # Critical safety guard: cancel_order is ONLY ever called below
            # this point, and only when parent_trade_id is non-empty.
            assert parent_trade_id, (
                "harvest-style classifier let through an order with no parent "
                "trade_id (order=%s) -- bug, refusing to cancel" % order_id
            )

            parent_alive_on_broker = parent_trade_id in open_trade_ids
            parent_in_tracker = ctx.tracker.get(parent_trade_id) is not None
            if parent_alive_on_broker or parent_in_tracker:
                continue  # legitimate live harvest LIMIT

            # Pull strategy/created_at from ledger if we have a record;
            # otherwise we only know what the broker tells us.
            entry = ledger.get(order_id, {}) or {}
            strategy = entry.get("strategy", "")
            created_at = entry.get("created_at", "")
            gtd_time = entry.get("gtd_time", "") or getattr(order, "gtd_time", "")

            log.warning(
                "[RECOVERY] ORPHAN HARVEST LIMIT (broker-walk): order=%s "
                "trade=%s symbol=%s position_fill=%s -> cancelling",
                order_id, parent_trade_id, symbol,
                getattr(order, "position_fill", ""),
            )
            self._audit_harvest(
                "orphan_harvest_limit_found", "parent_absent",
                trade_id=parent_trade_id, order_id=order_id,
                symbol=symbol, strategy=strategy,
                gtd_time=gtd_time, created_at=created_at,
            )
            ok = False
            try:
                ok = bool(ctx.broker.cancel_order(order_id))
            except Exception:
                log.exception("[RECOVERY] orphan cancel raised: %s", order_id)
            self._ledger.remove(order_id)
            self._audit_harvest(
                "orphan_harvest_limit_cancelled",
                "ok" if ok else "broker_reject",
                trade_id=parent_trade_id, order_id=order_id,
                symbol=symbol, strategy=strategy,
                gtd_time=gtd_time, created_at=created_at,
            )
            orphans_found += 1

        # Housekeeping: drop ledger entries whose order is gone from broker
        # (filled, cancelled by us elsewhere, or GTD-expired). Same logic as
        # the original sweep's tail; preserved verbatim.
        for order_id, entry in list(ledger.items()):
            if order_id in pending_by_id:
                continue
            self._ledger.remove(order_id)

        # Single-line cycle summary -- only when there's something to say,
        # to avoid log spam when the broker has zero pendings (the common
        # case on this account).
        if pending_list:
            log.info(
                "[RECOVERY] orphan-harvest sweep: walked %d pending, %d orphans found",
                len(pending_list), orphans_found,
            )

    def _dust_threshold(self) -> float:
        """Units below which a residual is considered accounting dust."""
        try:
            mgmt = self.ctx.config.section("management") if hasattr(self.ctx, "config") else {}
            if isinstance(mgmt, dict):
                return float(mgmt.get("dust_unit_threshold", 2))
        except Exception:
            pass
        return 2.0

    def _maybe_flatten_dust(self, tracked, remaining_units: float) -> None:
        """If remaining broker units are at/below the dust threshold, flatten.

        After a partial close, tiny residuals (1-2 units) are just accounting
        noise — they can't be meaningfully managed and generate log spam.
        Market-close them and let the normal vanish path clean up the tracker.
        """
        threshold = self._dust_threshold()
        if remaining_units <= 0 or remaining_units > threshold:
            return
        log.warning(
            "[RECOVERY] DUST FLATTEN: %s remaining=%.0f <= threshold=%.0f",
            tracked.trade_id, remaining_units, threshold,
        )
        try:
            result = self.ctx.broker.close_trade(tracked.trade_id)
            if getattr(result, "success", False):
                log.info("[RECOVERY] DUST FLATTENED: %s pl=%.2f",
                         tracked.trade_id, getattr(result, "realized_pl", 0.0))
            else:
                log.warning("[RECOVERY] DUST FLATTEN FAILED: %s error=%s",
                            tracked.trade_id, getattr(result, "error", "?"))
        except Exception:
            log.exception("[RECOVERY] DUST FLATTEN raised: %s", tracked.trade_id)

    def _place_harvest_limit(self, tracked) -> str | None:
        """Pre-place a REDUCE_ONLY limit order at TP1 for partial harvest.

        Returns the new broker order_id on successful placement, or None
        if the call is a no-op / fails. Callers within the same cycle
        (reconcile_pending_orders) use this to union same-cycle placements
        into the broker-pending view before the harvest-reconcile loop.
        """
        if not tracked or not tracked.tp1_price or tracked.tp1_taken:
            return None
        if hasattr(tracked, 'harvest_order_id') and tracked.harvest_order_id:
            return None

        ctx = self.ctx
        harvest_units = int(tracked.units * 0.5)
        if harvest_units <= 0:
            return None

        signed_units = -harvest_units if tracked.direction == "long" else harvest_units

        # Hotfix: bound harvest LIMIT lifetime by strategy holding profile.
        # 4h direct/box / 12h dbb_trend. Pure GTC was the root cause of
        # naked-position orphans when the parent closed and the cancel-on-
        # vanish hook missed.
        now = datetime.now(timezone.utc)
        gtd_hours = _harvest_gtd_hours(getattr(tracked, "strategy", ""))
        gtd_time = _format_gtd(now, gtd_hours)

        result = ctx.broker.place_limit_order(
            symbol=tracked.symbol,
            units=signed_units,
            price=tracked.tp1_price,
            stop_loss=None,
            take_profit=None,
            gtd_time=gtd_time,
            position_fill="REDUCE_ONLY",
        )

        if result.success and result.order_id:
            ctx.tracker.set_harvest_order(tracked.trade_id, result.order_id)
            self._ledger.add(
                order_id=result.order_id,
                trade_id=tracked.trade_id,
                symbol=tracked.symbol,
                strategy=getattr(tracked, "strategy", "") or "",
                gtd_time=gtd_time,
            )
            log.info("[RECOVERY] HARVEST LIMIT PLACED: %s order=%s @ %.5f (%d units) GTD=%s",
                     tracked.trade_id, result.order_id, tracked.tp1_price,
                     harvest_units, gtd_time)
            self._audit_harvest(
                "harvest_limit_created", "tp1_preplaced",
                trade_id=tracked.trade_id,
                order_id=result.order_id,
                symbol=tracked.symbol,
                strategy=getattr(tracked, "strategy", "") or "",
                gtd_time=gtd_time,
                created_at=now.isoformat(),
            )
            return result.order_id
        elif result.success and result.trade_id:
            ctx.tracker.mark_tp1_taken(tracked.trade_id)
            log.info("[RECOVERY] HARVEST LIMIT FILLED IMMEDIATELY: %s @ %.5f",
                     tracked.trade_id, tracked.tp1_price)
            return None
        else:
            log.warning("[RECOVERY] HARVEST LIMIT FAILED: %s error=%s",
                        tracked.trade_id, result.error)
            return None
