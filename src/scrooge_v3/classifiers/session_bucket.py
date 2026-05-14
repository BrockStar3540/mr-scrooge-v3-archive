"""Session-bucket classifier — 7 UTC-hour buckets (DST-stable).

  asia          00-04 UTC
  asia_late     04-06 UTC
  london_open   06-09 UTC
  ny_open       09-13 UTC
  ny_mid        13-17 UTC
  ny_close      17-21 UTC
  off_hours     21-24 UTC

Stable wall-clock buckets used by the routing table for per-(pair, session)
strategy attachment. DST-independent.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone

from scrooge_v3.core.types import ClassificationResult, SymbolContext

log = logging.getLogger("scrooge_v3.classifiers.session_bucket")


def session_bucket_for_hour(hour_utc: int) -> str:
    if 0 <= hour_utc < 4:   return "asia"
    if 4 <= hour_utc < 6:   return "asia_late"
    if 6 <= hour_utc < 9:   return "london_open"
    if 9 <= hour_utc < 13:  return "ny_open"
    if 13 <= hour_utc < 17: return "ny_mid"
    if 17 <= hour_utc < 21: return "ny_close"
    return "off_hours"


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
