"""Tests for scrooge_v3.core.clock — session classification, DST, box days, replay.

Includes a golden-path regression proving that under compatibility mode, the
new 9-label clock selects the same threshold profile as the old 5-bucket
hardcoded map (except where old behavior was DST-incorrect by construction).
"""
from __future__ import annotations

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import pytest

from scrooge_v3.core.clock import (
    FixedClock,
    OandaClock,
    SessionLabel,
    box_day_start_utc,
    compat_threshold_profile,
    is_weekly_open,
    session_label_from_utc,
    trading_day_id,
)


def utc(y, m, d, h=0, mm=0):
    return datetime(y, m, d, h, mm, tzinfo=timezone.utc)


# ---------- Session classification ----------

class TestSessionLabels:
    def test_summer_london_ny_overlap(self):
        # 2025-07-15 13:00 UTC: London 14:00 BST, NY 09:00 EDT — both open.
        assert session_label_from_utc(utc(2025, 7, 15, 13, 0)) == SessionLabel.LONDON_NY_OVERLAP

    def test_winter_london_ny_overlap(self):
        # 2025-01-15 14:00 UTC: London 14:00 GMT, NY 09:00 EST.
        assert session_label_from_utc(utc(2025, 1, 15, 14, 0)) == SessionLabel.LONDON_NY_OVERLAP

    def test_summer_london_opens_one_hour_early_in_utc(self):
        # 2025-07-15 07:00 UTC: London 08:00 BST (just opened), Tokyo 16:00 JST (open).
        # Old V3 bucketed 07 UTC as asia_london_open — wrong. New label = TOKYO_LONDON.
        assert session_label_from_utc(utc(2025, 7, 15, 7, 0)) == SessionLabel.TOKYO_LONDON

    def test_winter_london_opens_at_utc_8(self):
        # 2025-01-15 08:00 UTC: London 08:00 GMT (just opened), Tokyo 17:00 JST (open).
        assert session_label_from_utc(utc(2025, 1, 15, 8, 0)) == SessionLabel.TOKYO_LONDON

    def test_summer_ny_only_after_london_close(self):
        # 2025-07-15 16:00 UTC: London 17:00 BST (closed), NY 12:00 EDT (open).
        assert session_label_from_utc(utc(2025, 7, 15, 16, 0)) == SessionLabel.NY_ONLY

    def test_winter_ny_open_past_20_utc(self):
        # Old V3 treated 20-23 UTC as dead_late. Winter 20 UTC: NY 15:00 EST, still open.
        assert session_label_from_utc(utc(2025, 1, 15, 20, 0)) == SessionLabel.NY_ONLY

    def test_sydney_tokyo_overlap_summer(self):
        # Tue 2025-07-15 02:00 UTC: Sydney 12:00 AEST (open), Tokyo 11:00 JST (open).
        assert session_label_from_utc(utc(2025, 7, 15, 2, 0)) == SessionLabel.SYDNEY_TOKYO

    def test_tokyo_only_when_sydney_closed(self):
        # 2025-07-15 06:00 UTC: Sydney 16:00 AEST (just closed), Tokyo 15:00 JST (open).
        assert session_label_from_utc(utc(2025, 7, 15, 6, 0)) == SessionLabel.TOKYO_ONLY

    def test_sydney_only_aedt_after_ny_close(self):
        # Jan is AEDT. 2025-01-15 22:00 UTC Wed: Sydney 09:00 AEDT (open), NY 17:00 EST (just closed).
        assert session_label_from_utc(utc(2025, 1, 15, 22, 0)) == SessionLabel.SYDNEY_ONLY

    def test_weekly_open_sunday_20_utc(self):
        # 2025-07-13 is a Sunday. 20:00 UTC triggers weekly_open.
        assert session_label_from_utc(utc(2025, 7, 13, 20, 0)) == SessionLabel.WEEKLY_OPEN

    def test_weekly_open_not_monday(self):
        # 2025-07-14 is Monday. 20:00 UTC is NY_ONLY, not weekly_open.
        assert session_label_from_utc(utc(2025, 7, 14, 20, 0)) == SessionLabel.NY_ONLY

    def test_rejects_naive_datetime(self):
        with pytest.raises(ValueError):
            session_label_from_utc(datetime(2025, 7, 15, 13, 0))


# ---------- DST transitions ----------

class TestDSTTransitions:
    def test_us_spring_forward(self):
        # 2025 US spring forward: 2025-03-09. Before: EST (UTC-5). After: EDT (UTC-4).
        # At 14:00 UTC on 2025-03-08 (Saturday is not tradable, use a weekday):
        # 2025-03-07 14:00 UTC (Fri, EST): NY 09:00, London 14:00 GMT → overlap.
        # 2025-03-10 14:00 UTC (Mon, EDT): NY 10:00, London 14:00 GMT → overlap.
        # Both should be LONDON_NY_OVERLAP despite DST shift.
        assert session_label_from_utc(utc(2025, 3, 7, 14, 0)) == SessionLabel.LONDON_NY_OVERLAP
        assert session_label_from_utc(utc(2025, 3, 10, 14, 0)) == SessionLabel.LONDON_NY_OVERLAP

    def test_uk_bst_spring_forward(self):
        # UK spring forward: 2025-03-30. Before: GMT. After: BST.
        # 2025-03-28 07:00 UTC (Fri, GMT): London 07:00 — not open yet (opens 08:00).
        # 2025-03-31 07:00 UTC (Mon, BST): London 08:00 — just opened.
        # So the same UTC hour maps to different labels across UK DST — which is correct.
        before = session_label_from_utc(utc(2025, 3, 28, 7, 0))
        after = session_label_from_utc(utc(2025, 3, 31, 7, 0))
        assert before != after
        assert after == SessionLabel.TOKYO_LONDON

    def test_au_dst_opposite_hemisphere(self):
        # AU DST starts ~Oct (AEDT), ends ~Apr (AEST). Opposite of NH.
        # 2025-02-15 22:00 UTC (AEDT, Sat): Sydney 09:00 AEDT — open.
        # 2025-07-15 22:00 UTC (AEST, Tue): Sydney 08:00 AEST — open.
        # Both should detect Sydney open. Wednesday 22 UTC = weekday, same logic applies.
        assert session_label_from_utc(utc(2025, 2, 19, 22, 0)) == SessionLabel.SYDNEY_ONLY
        assert session_label_from_utc(utc(2025, 7, 15, 22, 0)) == SessionLabel.SYDNEY_ONLY


# ---------- Box day (OANDA NY-17:00 anchor) ----------

class TestBoxDay:
    def test_summer_day_boundary(self):
        # EDT: boundary at 21:00 UTC.
        # 2025-07-15 20:00 UTC is still prev day; 22:00 UTC is new day.
        before = box_day_start_utc(utc(2025, 7, 15, 20, 0))
        after = box_day_start_utc(utc(2025, 7, 15, 22, 0))
        assert before == utc(2025, 7, 14, 21, 0)
        assert after == utc(2025, 7, 15, 21, 0)

    def test_winter_day_boundary(self):
        # EST: boundary at 22:00 UTC.
        before = box_day_start_utc(utc(2025, 1, 15, 21, 0))
        after = box_day_start_utc(utc(2025, 1, 15, 23, 0))
        assert before == utc(2025, 1, 14, 22, 0)
        assert after == utc(2025, 1, 15, 22, 0)

    def test_trading_day_id_stable_across_hour(self):
        # 2025-07-15 22:00 and 23:00 UTC are the same trading day.
        tid1 = trading_day_id(utc(2025, 7, 15, 22, 0))
        tid2 = trading_day_id(utc(2025, 7, 15, 23, 0))
        assert tid1 == tid2 == "2025-07-15"


# ---------- Weekly open flag ----------

class TestWeeklyOpen:
    def test_sunday_evening_utc(self):
        assert is_weekly_open(utc(2025, 7, 13, 20, 0)) is True
        assert is_weekly_open(utc(2025, 7, 13, 23, 59)) is True

    def test_sunday_morning_not_weekly_open(self):
        assert is_weekly_open(utc(2025, 7, 13, 10, 0)) is False

    def test_monday_not_weekly_open(self):
        assert is_weekly_open(utc(2025, 7, 14, 20, 0)) is False


# ---------- Clocks ----------

class TestFixedClock:
    def test_now_utc_is_injected_time(self):
        t = utc(2023, 10, 5, 14, 30)
        clock = FixedClock(t)
        assert clock.now_utc() == t

    def test_session_label_matches_time(self):
        clock = FixedClock(utc(2025, 7, 15, 13, 0))
        assert clock.session_label() == SessionLabel.LONDON_NY_OVERLAP

    def test_set_advances_time(self):
        clock = FixedClock(utc(2025, 7, 15, 10, 0))
        assert clock.session_label() == SessionLabel.LONDON_ONLY
        clock.set(utc(2025, 7, 15, 13, 0))
        assert clock.session_label() == SessionLabel.LONDON_NY_OVERLAP

    def test_rejects_naive(self):
        with pytest.raises(ValueError):
            FixedClock(datetime(2025, 7, 15))


class TestOandaClock:
    def test_returns_tz_aware_utc(self):
        c = OandaClock()
        t = c.now_utc()
        assert t.tzinfo is not None


# ---------- Golden-path regression: compat map matches old behavior ----------

# Old V3 fixed-UTC mapping. Reproduced here so we can verify the compat layer
# produces the same threshold tuple on non-DST-drifted hours.
def _legacy_session_key(utc_hour: int) -> str:
    if utc_hour >= 20:
        return "dead_late"
    if utc_hour >= 18:
        return "late_ny"
    if utc_hour >= 12:
        return "ny_active"
    if utc_hour >= 8:
        return "london"
    return "asia_london_open"


_LEGACY_TUPLES = {
    "asia_london_open": (30, 44, 54, 16),
    "london":           (32, 44, 54, 12),
    "ny_active":        (30, 42, 50, 12),
    "late_ny":          (34, 44, 54, 10),
    "dead_late":        (40, 52, 62, 8),
}


class TestCompatRegression:
    """Compat mode must match old thresholds on every hour that wasn't already wrong.

    The drift set differs between winter and summer because the old 5-bucket
    map was DST-naive. Each drift represents a case where old V3 applied the
    wrong threshold because it misidentified the session.

    Winter (EST/GMT) drifts:
      - 12 UTC: old=ny_active, new=LONDON_ONLY→london (NY opens at 13 UTC in EST)
      - 18-19 UTC: old=late_ny, new=NY_ONLY→ny_active (late_ny bucket folded in)
      - 20-21 UTC: old=dead_late, new=NY_ONLY→ny_active (NY still open until 22 UTC EST)

    Summer (EDT/BST) drifts:
      - 7 UTC: old=asia_london_open, new=TOKYO_LONDON→london (London opens at 7 UTC BST)
      - 18-19 UTC: old=late_ny, new=NY_ONLY→ny_active
      - 20 UTC: old=dead_late, new=NY_ONLY→ny_active (NY still open until 21 UTC EDT)
    """

    WINTER_DRIFTS = {12, 18, 19, 20, 21}
    SUMMER_DRIFTS = {7, 18, 19, 20}

    _TREND_LEGACY = {
        "asia_london_open": (28, 42, 52, 16),
        "london":           (30, 42, 52, 12),
        "ny_active":        (28, 40, 48, 12),
        "late_ny":          (32, 42, 52, 10),
        "dead_late":        (38, 50, 60, 8),
    }

    def _check(self, ts_base_fn, drifts, family, legacy_map):
        for h in range(24):
            if h in drifts:
                continue
            ts = ts_base_fn(h)
            label = session_label_from_utc(ts)
            new_profile = compat_threshold_profile(label, family=family)
            old_key = _legacy_session_key(h)
            old_tuple = legacy_map[old_key]
            assert new_profile.as_tuple() == old_tuple, (
                f"{family} h={h} label={label} new={new_profile.as_tuple()} old={old_tuple}"
            )

    def test_winter_non_drift_hours_match_default(self):
        self._check(lambda h: utc(2025, 1, 15, h, 0), self.WINTER_DRIFTS, "default", _LEGACY_TUPLES)

    def test_winter_non_drift_hours_match_trend(self):
        self._check(lambda h: utc(2025, 1, 15, h, 0), self.WINTER_DRIFTS, "trend", self._TREND_LEGACY)

    def test_summer_non_drift_hours_match_default(self):
        self._check(lambda h: utc(2025, 7, 15, h, 0), self.SUMMER_DRIFTS, "default", _LEGACY_TUPLES)

    def test_summer_non_drift_hours_match_trend(self):
        self._check(lambda h: utc(2025, 7, 15, h, 0), self.SUMMER_DRIFTS, "trend", self._TREND_LEGACY)

    def test_winter_12_utc_drift_documented(self):
        # In winter, 12 UTC is London-only, not NY overlap. Old V3 incorrectly
        # applied ny_active thresholds here.
        ts = utc(2025, 1, 15, 12, 0)
        assert session_label_from_utc(ts) == SessionLabel.LONDON_ONLY
        new = compat_threshold_profile(session_label_from_utc(ts)).as_tuple()
        assert new == _LEGACY_TUPLES["london"]
        assert new != _LEGACY_TUPLES["ny_active"]

    def test_summer_7_utc_drift_documented(self):
        # In summer (BST), London opens at 7 UTC. Old V3 bucketed 7 UTC as asia_london_open.
        ts = utc(2025, 7, 15, 7, 0)
        assert session_label_from_utc(ts) == SessionLabel.TOKYO_LONDON
        new = compat_threshold_profile(session_label_from_utc(ts)).as_tuple()
        assert new == _LEGACY_TUPLES["london"]
        assert new != _LEGACY_TUPLES["asia_london_open"]

    def test_late_ny_hours_now_use_ny_active_thresholds(self):
        # Document the known drift: 18-19 UTC was late_ny, now folds into NY_ONLY/ny_active.
        label = session_label_from_utc(utc(2025, 1, 15, 18, 0))
        assert label == SessionLabel.NY_ONLY
        new = compat_threshold_profile(label).as_tuple()
        assert new == _LEGACY_TUPLES["ny_active"]
        # Different from old:
        assert new != _LEGACY_TUPLES["late_ny"]

    def test_weekly_open_keeps_dead_late_thresholds(self):
        # Compat: weekly_open maps to dead_late thresholds, but flag is separate.
        ts = utc(2025, 7, 13, 22, 0)  # Sunday
        label = session_label_from_utc(ts)
        assert label == SessionLabel.WEEKLY_OPEN
        assert is_weekly_open(ts) is True
        assert compat_threshold_profile(label).as_tuple() == _LEGACY_TUPLES["dead_late"]
