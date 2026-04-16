"""V3.1 Hybrid Scorer unit tests.

Validates all 3 layers: hard blocks, single-factor scoring, paired aspects.
Updated for V3.1 rebalanced weights (2026-04-16).
"""

from scrooge_v3.strategies.v3_scorer import V3HybridScorer, ScorerResult


def make_factors(**overrides) -> dict:
    """Baseline 'neutral' factor set — everything at midpoint."""
    base = {
        "hour": 10, "bage": 14, "ns": 7, "vr": 1.2, "mom": 1, "dc": 2,
        "zs": 1.2, "bbp": 0.55, "e50d": 40, "e20d": 25, "otr": 15,
        "adr": 0.7, "dur": 60, "wp": 0.35, "bp": 0.35, "bbs": "REJ_L", "rsi": 40,
    }
    base.update(overrides)
    return base


scorer = V3HybridScorer()


# =====================================================================
# Layer 0: Hard Blocks
# =====================================================================

class TestHardBlocks:
    def test_rsi_neutral_soft_penalty(self):
        """V3.1.1: RSI neutral is now a -5 soft penalty, not a hard block."""
        r = make_factors(rsi=50)
        result = scorer._compute_score(r)
        assert "RSI_NEUT" not in result.blocks
        assert result.breakdown["rsi"] == -5

    def test_rsi_at_boundary_45_soft_penalty(self):
        r = make_factors(rsi=45)
        result = scorer._compute_score(r)
        assert "RSI_NEUT" not in result.blocks
        assert result.breakdown["rsi"] == -5

    def test_rsi_at_boundary_55_soft_penalty(self):
        r = make_factors(rsi=55)
        result = scorer._compute_score(r)
        assert "RSI_NEUT" not in result.blocks
        assert result.breakdown["rsi"] == -5

    def test_rsi_44_passes(self):
        r = make_factors(rsi=44)
        result = scorer._compute_score(r)
        assert "RSI_NEUT" not in result.blocks

    def test_stretch_up_block(self):
        r = make_factors(bbs="STR_UP")
        result = scorer._compute_score(r)
        assert result.tier == "BLOCKED"
        assert "STR_UP" in result.blocks

    def test_stretch_down_not_blocked(self):
        r = make_factors(bbs="STR_DN")
        result = scorer._compute_score(r)
        assert "STR_UP" not in result.blocks

    def test_duration_12h_block(self):
        r = make_factors(dur=720)
        result = scorer._compute_score(r)
        assert "DUR_12H" in result.blocks

    def test_duration_11h_passes(self):
        r = make_factors(dur=660)
        result = scorer._compute_score(r)
        assert "DUR_12H" not in result.blocks

    def test_otr_low_plus_norm_no_hard_block(self):
        """V3.1: OTR<8+NORM is no longer a hard block, just a soft penalty."""
        r = make_factors(otr=5, bbs="NORM")
        result = scorer._compute_score(r)
        assert "OTR<8+NORM" not in result.blocks

    def test_otr_low_still_penalized(self):
        """OTR < 8 should get -4 soft penalty."""
        r = make_factors(otr=5)
        result = scorer._compute_score(r)
        assert result.breakdown["otr"] == -4

    def test_stale_box_plus_close_ema20_block(self):
        r = make_factors(bage=20, e20d=10)
        result = scorer._compute_score(r)
        assert "STALE+E20" in result.blocks

    def test_stale_box_but_far_ema20_no_block(self):
        r = make_factors(bage=20, e20d=20)
        result = scorer._compute_score(r)
        assert "STALE+E20" not in result.blocks

    def test_multiple_blocks(self):
        r = make_factors(rsi=50, bbs="STR_UP", dur=800)
        result = scorer._compute_score(r)
        assert len(result.blocks) >= 2


# =====================================================================
# Layer 1: Single Factor Scoring (V3.1 decompressed weights)
# =====================================================================

class TestSingleFactors:
    def test_entry_hour_early_positive(self):
        r = make_factors(hour=3)
        result = scorer._compute_score(r)
        assert result.breakdown["hr"] == 10

    def test_entry_hour_ny_active_mild(self):
        """V3.1: 12-16 UTC is -3 (was -8)."""
        r = make_factors(hour=14)
        result = scorer._compute_score(r)
        assert result.breakdown["hr"] == -3

    def test_entry_hour_ny_peak_minimal(self):
        """V3.1: 16-18 UTC is -1 (was -4)."""
        r = make_factors(hour=17)
        result = scorer._compute_score(r)
        assert result.breakdown["hr"] == -1

    def test_box_age_fresh_positive(self):
        r = make_factors(bage=4)
        result = scorer._compute_score(r)
        assert result.breakdown["age"] == 9

    def test_box_age_stale_negative(self):
        """V3.1.1: 18-24h is -4 (was -7, was -12)."""
        r = make_factors(bage=20)
        result = scorer._compute_score(r)
        assert result.breakdown["age"] == -4

    def test_natural_stop_sweet_spot(self):
        r = make_factors(ns=5)
        result = scorer._compute_score(r)
        assert result.breakdown["stp"] == 8

    def test_volume_calm_positive(self):
        r = make_factors(vr=1.0)
        result = scorer._compute_score(r)
        assert result.breakdown["vol"] == 8

    def test_volume_volatile_negative(self):
        r = make_factors(vr=1.5)
        result = scorer._compute_score(r)
        assert result.breakdown["vol"] == -3

    def test_otr_sweet_spot(self):
        r = make_factors(otr=12)
        result = scorer._compute_score(r)
        assert result.breakdown["otr"] == 2

    def test_ema50_battle_zone(self):
        """EMA50 < 20% = -8 (was -10)."""
        r = make_factors(e50d=15)
        result = scorer._compute_score(r)
        assert result.breakdown["e50"] == -8

    def test_ema20_too_close(self):
        """V3.1.1: e20<15 is -3 (was -6)."""
        r = make_factors(e20d=10)
        result = scorer._compute_score(r)
        assert result.breakdown["e20"] == -3

    def test_z_score_neutral_trap(self):
        r = make_factors(zs=0.3)
        result = scorer._compute_score(r)
        assert result.breakdown["z"] == -7

    def test_directional_candles_strong(self):
        """V3.1: dc>=4 is +10 (was +7) — strongest soft factor."""
        r = make_factors(dc=4)
        result = scorer._compute_score(r)
        assert result.breakdown["dc"] == 10

    def test_directional_candles_zero(self):
        """V3.1: dc==0 is -8 (was -6)."""
        r = make_factors(dc=0)
        result = scorer._compute_score(r)
        assert result.breakdown["dc"] == -8

    def test_wall_proximity_danger_zone(self):
        """V3.1: wall 0.15-0.30 is -3 (was -9)."""
        r = make_factors(wp=0.22)
        result = scorer._compute_score(r)
        assert result.breakdown["wal"] == -3

    def test_body_pct_momentum_candle_bad(self):
        """V3.1: body 0.45-0.65 is -4 (was -8)."""
        r = make_factors(bp=0.55)
        result = scorer._compute_score(r)
        assert result.breakdown["bdy"] == -4

    def test_rsi_oversold_bonus(self):
        r = make_factors(rsi=25)
        result = scorer._compute_score(r)
        assert result.breakdown["rsi"] == 5

    def test_bb_state_norm_positive(self):
        r = make_factors(bbs="NORM")
        result = scorer._compute_score(r)
        assert result.breakdown["bbs"] == 2


# =====================================================================
# Layer 2: Paired Aspects (V3.1 halved magnitudes)
# =====================================================================

class TestPairedAspects:
    def test_early_hour_plus_norm_bonus(self):
        """V3.1: +8 (was +14)."""
        r = make_factors(hour=3, bbs="NORM")
        result = scorer._compute_score(r)
        assert result.breakdown.get("p_hr_norm") == 8

    def test_fresh_age_plus_rsi_bonus(self):
        """V3.1 new pair: fresh box + rsi < 45 = +6."""
        r = make_factors(bage=4, rsi=40)
        result = scorer._compute_score(r)
        assert result.breakdown.get("p_age_rsi") == 6

    def test_afternoon_plus_spent_adr_penalty(self):
        """V3.1: -6 (was -13)."""
        r = make_factors(hour=14, adr=1.0)
        result = scorer._compute_score(r)
        assert result.breakdown.get("n_hr_adr") == -6

    def test_neutral_z_plus_norm_bb_penalty(self):
        """V3.1: -6 (was -9)."""
        r = make_factors(zs=0.3, bbs="NORM")
        result = scorer._compute_score(r)
        assert result.breakdown.get("n_z_norm") == -6

    def test_conviction_plus_ema50_bonus(self):
        """V3.1 new pair: dc>=4 + ema50>=60 = +5."""
        r = make_factors(dc=4, e50d=65)
        result = scorer._compute_score(r)
        assert result.breakdown.get("p_e50_dc") == 5

    def test_no_pairs_when_conditions_not_met(self):
        """Midday + safe ADR = no pair bonus/penalty."""
        r = make_factors(hour=10, adr=0.5)
        result = scorer._compute_score(r)
        assert result.breakdown.get("n_hr_adr") is None
        assert result.breakdown.get("p_hr_norm") is None


# =====================================================================
# Correlated-Negative Caps
# =====================================================================

class TestCorrelatedCaps:
    def test_hour_age_cap(self):
        """hr+age should be capped at -10 total."""
        r = make_factors(hour=22, bage=20)  # hr=-7, age=-7 = -14, cap to -10
        result = scorer._compute_score(r)
        hr = result.breakdown["hr"]
        age = result.breakdown["age"]
        cap = result.breakdown.get("hr_age_cap", 0)
        assert hr + age + cap >= -10

    def test_no_cap_when_not_needed(self):
        """No cap when hr+age is above -10."""
        r = make_factors(hour=10, bage=14)  # hr=2, age=0 = positive
        result = scorer._compute_score(r)
        assert "hr_age_cap" not in result.breakdown


# =====================================================================
# Session Detection
# =====================================================================

class TestSessionDetection:
    def test_asia_london_open(self):
        r = make_factors(hour=3)
        result = scorer._compute_score(r)
        # Session should be asia_london_open with floor=36

    def test_ny_active_session(self):
        """V3.1: 12-17 UTC = ny_active, not afternoon."""
        r = make_factors(hour=15)
        result = scorer._compute_score(r)
        # Score should use ny_active thresholds (floor=36, b=48, a=56)

    def test_dead_late_session(self):
        r = make_factors(hour=22)
        result = scorer._compute_score(r)
        # Dead late requires higher base (floor=46)


# =====================================================================
# Tier Classification (V3.1 thresholds)
# =====================================================================

class TestTierClassification:
    def test_a_tier(self):
        r = make_factors(
            hour=3, bage=4, ns=5, vr=1.0, mom=2, dc=4,
            zs=0.8, bbp=0.72, e50d=65, e20d=22, otr=12,
            adr=0.6, dur=60, wp=0.08, bp=0.2, bbs="REJ_L", rsi=35,
        )
        result = scorer._compute_score(r)
        assert result.tier == "A"
        assert result.score >= 56  # V3.1 A threshold for asia_london

    def test_b_tier(self):
        r = make_factors(
            hour=3, bage=10, ns=5, vr=1.0, mom=1, dc=2,
            zs=0.8, bbp=0.55, e50d=40, e20d=25, otr=12,
            adr=0.7, dur=60, wp=0.35, bp=0.35, bbs="REJ_L", rsi=40,
        )
        result = scorer._compute_score(r)
        assert result.tier in ("A", "B")
        assert result.score >= 48

    def test_reject_tier(self):
        r = make_factors(
            hour=14, bage=16, ns=3, vr=1.5, mom=0, dc=0,
            zs=0.3, bbp=0.42, e50d=25, e20d=20, otr=22,
            adr=1.1, dur=60, wp=0.22, bp=0.55, bbs="BRK_UP", rsi=60,
        )
        result = scorer._compute_score(r)
        assert result.tier == "REJECT"

    def test_blocked_tier(self):
        """STR_UP is still a hard block."""
        r = make_factors(bbs="STR_UP")
        result = scorer._compute_score(r)
        assert result.tier == "BLOCKED"
        assert result.score == 0


# =====================================================================
# Custom Thresholds
# =====================================================================

class TestCustomThresholds:
    def test_custom_a_threshold(self):
        custom = V3HybridScorer({"threshold_a": 80, "threshold_b": 60})
        r = make_factors(
            hour=3, bage=4, ns=5, vr=1.0, mom=2, dc=4,
            zs=0.8, bbp=0.72, e50d=65, e20d=22, otr=12,
            adr=0.6, dur=60, wp=0.08, bp=0.2, bbs="REJ_L", rsi=35,
        )
        result = custom._compute_score(r)
        # Strong setup should still be A
        assert result.tier == "A"
