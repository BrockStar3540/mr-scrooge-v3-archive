"""Session-bucket classifier — 8 UTC-hour buckets (DST-stable, research-clock).

  asia          22-06 UTC  (Sydney/Tokyo open; wraps midnight UTC)
  asia_late     06-07 UTC  (Tokyo close / pre-London handoff)
  london_open   07-10 UTC
  london        10-12 UTC  (mid-London, pre-NY)
  ny_open       12-14 UTC
  ny_mid        14-17 UTC
  ny_close      17-21 UTC
  off_hours     21-22 UTC  (pre-reopen seam on Sundays; usually empty)

Aligned 2026-05-24 to the boundaries the routing-table corpus was built under
(legacy v1.9 + unified 6m rebuild both use this clock). Previously V3 used
a 4hr asia window 00-04 UTC which dark-windowed hour 22-23 every day —
specifically blocking the Sun 22:00 UTC reopen for ~2 hours.

DST-independent.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone

from scrooge_v3.core.types import ClassificationResult, SymbolContext

log = logging.getLogger("scrooge_v3.classifiers.session_bucket")


def session_bucket_for_hour(hour_utc: int) -> str:
    # research-clock boundaries (aligned 2026-05-24)
    if 22 <= hour_utc or hour_utc < 6: return "asia"
    if 6  <= hour_utc < 7:             return "asia_late"
    if 7  <= hour_utc < 10:            return "london_open"
    if 10 <= hour_utc < 12:            return "london"
    if 12 <= hour_utc < 14:            return "ny_open"
    if 14 <= hour_utc < 17:            return "ny_mid"
    if 17 <= hour_utc < 21:            return "ny_close"
    return "off_hours"   # hour 21 only


class SessionBucketClassifier:
    name = "session_bucket"

    def classify(self, ctx: SymbolContext) -> ClassificationResult:
        snap = getattr(ctx, "snapshot", None)
        ts = getattr(snap, "ts", None) if snap is not None else None
        if ts is None:
            ts = datetime.now(timezone.utc)
        if getattr(ts, "tzinfo", None) is None:
            ts = ts.replace(tzinfo=timezone.utc)
        hour = ts.astimezone(timezone.utc).hour
        bucket = session_bucket_for_hour(hour)
        return ClassificationResult(
            name=self.name,
            label=bucket,
            confidence=1.0,
            metadata={"hour_utc": hour, "bucket": bucket},
        )
