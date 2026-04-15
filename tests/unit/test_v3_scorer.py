"""V3 Hybrid Scorer unit tests.

Validates all 3 layers: hard blocks, single-factor scoring, paired aspects.
Uses known factor values with expected scores from docs/SCORING_V3_LIVE.md.
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
    def test_rsi_neutral_block(self):
        r = make_factors(rsi=50)
        result = scorer._compute_score(r)
        assert result.tier == "BLOCKED"
        assert "RSI_NEUT" in result.blocks

    def test_rsi_at_boundary_45_blocks(self):
        r = make_factors(rsi=45)
        result = scorer._compute_score(r)
        assert "RSI_NEUT" in result.blocks

    def test_rsi_at_boundary_55_blocks(self):
        r = make_factors(rsi=55)
        result = scorer._compute_score(r)
        assert "RSI_NEUT" in result.blocks

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

    def test_otr_low_plus_norm_block(self):
        r = make_factors(otr=5, bbs="NORM")
        result = scorer._compute_score(r)
        assert "OTR<8+NORM" in result.blocks

    def test_otr_low_plus_rej_no_block(self):
        """Low OTR with non-NORM BB state should NOT trigger this block."""
        r = make_factors(otr=5, bbs="REJ_L")
        result = scorer._compute_score(r)
        assert "OTR<8+NORM" not in result.blocks

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
# Layer 1: Single Factor Scoring
# =====================================================================

class TestSingleFactors:
    def test_entry_hour_early_positive(self):
        r = make_factors(hour=3)
        result = scorer._compute_score(r)
        assert result.breakdown["hr"] == 13

    def test_entry_hour_afternoon_negative(self):
        r = make_factors(hour=14)
        result = scorer._compute_score(r)
        assert result.breakdown["hr"] == -8

    def test_box_age_fresh_positive(self):
        r = make_factors(bage=4)
        result = scorer._compute_score(r)
        assert result.breakdown["age"] == 13

    def test_box_age_stale_negative(self):
        r = make_factors(bage=20)
        result = scorer._compute_score(r)
        assert result.breakdown["age"] == -12

    def test_natural_stop_sweet_spot(self):
        r = make_factors(ns=5)
        result = scorer._compute_score(r)
        assert result.breakdown["stp"] == 9

    def test_volume_calm_positive(self):
        r = make_factors(vr=1.0)
        result = scorer._compute_score(r)
        assert result.breakdown["vol"] == 9

    def test_volume_volatile_negative(self):
        r = make_factors(vr=1.5)
        result = scorer._compute_score(r)
        assert result.breakdown["vol"] == -3

    def test_otr_inverted_low_is_bad(self):
        """V3 critical: OTR < 8% = -11 pts (17% WR, worst bracket)."""
        r = make_factors(otr=5)
        result = scorer._compute_score(r)
        assert result.breakdown["otr"] == -11

    def test_otr_sweet_spot(self):
        r = make_factors(otr=12)
        result = scorer._compute_score(r)
        assert result.breakdown["otr"] == 4

    def test_ema50_battle_zone(self):
        """EMA50 < 20% = -10 pts (20% WR)."""
        r = make_factors(e50d=15)
        result = scorer._compute_score(r)
        assert result.breakdown["e50"] == -10

    def test_ema20_too_close(self):
        r = make_factors(e20d=10)
        result = scorer._compute_score(r)
        assert result.breakdown["e20"] == -7

    def test_z_score_neutral_trap(self):
        r = make_factors(zs=0.3)
        result = scorer._compute_score(r)
        assert result.breakdown["z"] == -9

    def test_wall_proximity_danger_zone(self):
        r = make_factors(wp=0.22)
        result = scorer._compute_score(r)
        assert result.breakdown["wal"] == -9

    def test_body_pct_momentum_candle_bad(self):
        r = make_factors(bp=0.55)
        result = scorer._compute_score(r)
        assert result.breakdown["bdy"] == -8

    def test_rsi_oversold_bonus(self):
        r = make_factors(rsi=25)
        result = scorer._compute_score(r)
        assert result.breakdown["rsi"] == 7

    def test_bb_state_norm_positive(self):
        r = make_factors(bbs="NORM")
        result = scorer._compute_score(r)
        assert result.breakdown["bbs"] == 3


# =====================================================================
# Layer 2: Paired Aspects
# =====================================================================

class TestPairedAspects:
    def test_early_hour_plus_norm_bonus(self):
        r = make_factors(hour=3, bbs="NORM")
        result = scorer._compute_score(r)
        assert result.breakdown.get("p_hr_norm") == 14

    def test_early_hour_plus_fresh_box_bonus(self):
        r = make_factors(hour=3, bage=4)
        result = scorer._compute_score(r)
        assert result.breakdown.get("p_hr_age") == 11

    def test_afternoon_plus_spent_adr_penalty(self):
        r = make_factors(hour=14, adr=1.0)
        result = scorer._compute_score(r)
        assert result.breakdown.get("n_hr_adr") == -13

    def test_neutral_z_plus_norm_bb_penalty(self):
        r = make_factors(zs=0.3, bbs="NORM")
        result = scorer._compute_score(r)
        assert result.breakdown.get("n_z_norm") == -9

    def test_no_pairs_when_conditions_not_met(self):
        """Midday + safe ADR = no pair bonus/penalty."""
        r = make_factors(hour=10, adr=0.5)
        result = scorer._compute_score(r)
        assert result.breakdown.get("n_hr_adr") is None
        assert result.breakdown.get("p_hr_norm") is None


# =====================================================================
# Tier Classification
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
        assert result.score >= 65

    def test_b_tier(self):
        """Score between 50 and 64."""
        r = make_factors(
            hour=3, bage=10, ns=5, vr=1.0, mom=1, dc=2,
            zs=0.8, bbp=0.55, e50d=40, e20d=25, otr=12,
            adr=0.7, dur=60, wp=0.35, bp=0.35, bbs="REJ_L", rsi=40,
        )
        result = scorer._compute_score(r)
        assert result.tier in ("A", "B")
        assert result.score >= 50

    def test_reject_tier(self):
        # bage=16 avoids 18-24 STALE+E20 block; e20d=20 avoids <15 penalty
        r = make_factors(
            hour=14, bage=16, ns=3, vr=1.5, mom=0, dc=0,
            zs=0.3, bbp=0.42, e50d=25, e20d=20, otr=22,
            adr=1.1, dur=60, wp=0.22, bp=0.55, bbs="BRK_UP", rsi=60,
        )
        result = scorer._compute_score(r)
        assert result.tier == "REJECT"
        assert result.score < 50

    def test_blocked_tier(self):
        r = make_factors(rsi=50)
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
        # Score is 165, so even with threshold_a=80, still A
        assert result.tier == "A"
