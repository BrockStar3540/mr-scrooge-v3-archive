"""V3 Hybrid Scorer — rebalanced scoring engine.

V3.1 reconfig (2026-04-16):
  - Decompressed hour/box-age penalties so NY session is not starved
  - Split session rules: asia_london / london / ny_active / late_ny / dead_late
  - Shrunk weak factors (wall proximity, BB position, ADR, OTR)
  - Strengthened directional conviction (dc)
  - Halved pair layer magnitudes, removed hour-dependent positive pairs
  - Added correlated-negative caps (hour+age, neutral cluster)
  - Removed OTR<8+NORM hard block (kept as soft penalty)
  - Lowered decision thresholds for NY-active

Architecture:
  Layer 0 — Hard blocks (automatic reject, before scoring)
  Layer 1 — 17 single-factor points (decompressed)
  Layer 2 — 15 paired-aspect bonuses/penalties (halved magnitudes)
  Decision — Session-aware A/B/REJECT/BLOCKED
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from scrooge_v3.core.clock import (
    Clock,
    OandaClock,
    SessionLabel,
    compat_threshold_profile,
)
from scrooge_v3.core.types import SymbolContext, TradeCandidate, TradeDirection

log = logging.getLogger("scrooge_v3.strategies.v3_scorer")


@dataclass
class ScorerResult:
    score: int = 0
    base_score: int = 0
    blocks: list[str] = field(default_factory=list)
    breakdown: dict[str, int] = field(default_factory=dict)
    tier: str = "REJECT"  # "A", "B", "REJECT", "BLOCKED"
    pairs_total: int = 0


# Session thresholds now live in scrooge_v3/core/clock.py under the 9-label
# SessionThresholdProfile system with a compat map back to the legacy 5-bucket
# values (same calibration, just accessed through the DST-aware clock).

# Correlated-negative caps — prevent triple-dipping
_MAX_HOUR_PLUS_AGE = -10
_MAX_NEUTRAL_CLUSTER = -10


class V3HybridScorer:
    """Scores trade candidates using V3.1 rebalanced formula.

    Key changes from V3.0:
      - NY active session (12-17 UTC) has its own thresholds
      - Hour/age penalties decompressed so they don't kill NY
      - Directional conviction (dc) is the strongest soft factor
      - Weak factors (wall, ADR, OTR) reduced
      - Pair bonuses halved — confirmation not rescue
    """

    name = "v3_scorer"

    def __init__(self, config: dict | None = None, clock: Clock | None = None):
        config = config or {}
        self.threshold_a = config.get("threshold_a", 60)
        self.threshold_b = config.get("threshold_b", 50)
        # Clock is injected. Production passes OandaClock; replay passes FixedClock.
        self.clock: Clock = clock or OandaClock()

    def score(self, ctx: SymbolContext, candidate: TradeCandidate) -> ScorerResult:
        """Score a trade candidate using V3.1 Hybrid formula."""
        f = self._extract_factors(ctx, candidate)
        return self._compute_score(f, candidate)

    # ------------------------------------------------------------------
    # Factor extraction
    # ------------------------------------------------------------------

    def _extract_factors(self, ctx: SymbolContext, candidate: TradeCandidate) -> dict[str, Any]:
        """Build flat factor dict from SymbolContext features."""
        now = self.clock.now_utc()

        bb_cls = ctx.classifications.get("bb_state")
        bbs = bb_cls.label if bb_cls else "NORM"
        _bb_map = {
            "NORMAL": "NORM", "EXTREME_UP": "EXT_U", "EXTREME_DOWN": "EXT_D",
            "REJECTION_SHORT": "REJ_S", "REJECTION_LONG": "REJ_L",
            "STRETCH_UP": "STR_UP", "STRETCH_DOWN": "STR_DN",
            "BREAKOUT_UP": "BRK_UP", "BREAKOUT_DOWN": "BRK_DN",
            "COMPRESSION": "COMP",
        }
        bbs = _bb_map.get(bbs, bbs)

        rsi_feat = ctx.features.get("rsi")
        rsi = rsi_feat.values.get("rsi", 50.0) if rsi_feat else 50.0

        bb_feat = ctx.features.get("bollinger")
        zs = bb_feat.values.get("z_score", 0.0) if bb_feat else 0.0
        bbp = bb_feat.values.get("bb_position", 0.5) if bb_feat else 0.5

        zd_feat = ctx.features.get("zone_detector")
        box_age = zd_feat.values.get("box_age_hours", 0.0) if zd_feat else 0.0
        wall_prox = zd_feat.values.get("wall_proximity", 0.5) if zd_feat else 0.5

        ema_feat = ctx.features.get("ema")
        e50d = ema_feat.values.get("ema50_dist_pct", 30.0) if ema_feat else 30.0
        e20d = ema_feat.values.get("ema20_dist_pct", 20.0) if ema_feat else 20.0

        otr_feat = ctx.features.get("otr")
        otr = otr_feat.values.get("otr_ratio", 0.15) * 100 if otr_feat else 15.0

        atr_feat = ctx.features.get("atr")
        adr = atr_feat.values.get("adr_consumed", 0.5) if atr_feat else 0.5

        vol_feat = ctx.features.get("volume")
        vr = vol_feat.values.get("volume_ratio", 1.0) if vol_feat else 1.0

        risk_points = candidate.metadata.get("risk_points", 0.0)
        pip = 0.01 if "JPY" in ctx.symbol else 0.0001
        ns = risk_points / pip if pip > 0 else 0.0

        mom, dc, bp = self._candle_features(ctx, candidate.direction)

        dur = 60.0

        # Raw audit values — box-derived inputs for score verification
        ema20_raw = ema_feat.values.get("ema20", 0.0) if ema_feat else 0.0
        ema50_raw = ema_feat.values.get("ema50", 0.0) if ema_feat else 0.0
        box_range = 0.0
        pdh = pdl = 0.0
        if zd_feat and zd_feat.values.get("zone_map"):
            zm = zd_feat.values["zone_map"]
            sr = getattr(zm, "session_range", None)
            if sr:
                pdh = getattr(sr, "PDH", 0.0)
                pdl = getattr(sr, "PDL", 0.0)
                box_range = pdh - pdl
            elif isinstance(zm, dict) and "session_range" in zm:
                sr = zm["session_range"]
                pdh = sr.get("PDH", 0.0) if isinstance(sr, dict) else 0.0
                pdl = sr.get("PDL", 0.0) if isinstance(sr, dict) else 0.0
                box_range = pdh - pdl

        return {
            "hour": now.hour,
            "bage": box_age,
            "ns": ns,
            "vr": vr,
            "mom": mom,
            "dc": dc,
            "zs": zs,
            "bbp": bbp,
            "e50d": e50d,
            "e20d": e20d,
            "otr": otr,
            "adr": adr,
            "dur": dur,
            "wp": wall_prox,
            "bp": bp,
            "bbs": bbs,
            "rsi": rsi,
            # Raw audit inputs (not scored, just for verification)
            "_price": ctx.snapshot.mid,
            "_ema20": ema20_raw,
            "_ema50": ema50_raw,
            "_box_range": box_range,
            "_pdh": pdh,
            "_pdl": pdl,
            "_box_age_h": box_age,
            "_spread": ctx.snapshot.spread,
        }

    def _candle_features(self, ctx: SymbolContext, direction: TradeDirection = TradeDirection.LONG) -> tuple[float, float, float]:
        """Extract momentum candles, directional candles, and body% from 5m bars.

        dc_count is trade-direction-relative:
          - LONG: counts bullish (green) candles as aligned
          - SHORT: counts bearish (red) candles as aligned
        """
        bars = ctx.snapshot.candles.get("5M") if ctx.snapshot.candles else None
        if bars is None or len(bars) < 6:
            return 0.0, 0.0, 0.3

        closes = bars["close"].astype(float).values
        opens = bars["open"].astype(float).values
        highs = bars["high"].astype(float).values
        lows = bars["low"].astype(float).values

        mom_count = 0
        dc_count = 0
        for i in range(-5, 0):
            candle_range = highs[i] - lows[i]
            body = abs(closes[i] - opens[i])
            if candle_range > 0 and body / candle_range > 0.6:
                mom_count += 1
            if direction == TradeDirection.LONG:
                if closes[i] > opens[i]:
                    dc_count += 1
            else:
                if closes[i] < opens[i]:
                    dc_count += 1

        entry_range = highs[-1] - lows[-1]
        entry_body = abs(closes[-1] - opens[-1])
        body_pct = entry_body / entry_range if entry_range > 0 else 0.3

        return float(mom_count), float(dc_count), body_pct

    # ------------------------------------------------------------------
    # Scoring engine — V3.1 rebalanced
    # ------------------------------------------------------------------

    def _compute_score(self, r: dict[str, Any], candidate: TradeCandidate | None = None) -> ScorerResult:
        """Compute the V3.1 rebalanced score."""
        blocks: list[str] = []
        bd: dict[str, int] = {}

        # === LAYER 0: HARD BLOCKS ===
        # RSI_NEUT moved to soft penalty (was hard block)
        # Backtest: 6 winners were hard-blocked by RSI 45-55, including $17.48 winner
        if r["bbs"] == "STR_UP":
            blocks.append("STR_UP")
        if r["dur"] >= 720:
            blocks.append("DUR_12H")
        # OTR<8+NORM removed as hard block — kept as soft penalty via OTR factor
        if 18 <= r["bage"] <= 24 and r["e20d"] < 15:
            blocks.append("STALE+E20")

        if blocks:
            log.info("[V3_SCORER] BLOCKED: %s", ", ".join(blocks))
            return ScorerResult(score=0, blocks=blocks, breakdown=bd, tier="BLOCKED")

        s = 0

        # === LAYER 1: SINGLE FACTOR BASE (17 factors — decompressed) ===

        # Entry hour — decompressed, NY not killed
        h = r["hour"]
        if h < 8: p = 10
        elif h < 12: p = 2
        elif h < 16: p = -3
        elif h < 18: p = -1
        elif h < 20: p = -3
        else: p = -7
        s += p; bd["hr"] = p

        # Box age (18-24h softened from -7 to -4, backtest-justified)
        a = r["bage"]
        if a < 8: p = 9
        elif a < 12: p = 5
        elif a < 18: p = 0
        elif a < 24: p = -4
        else: p = -4
        s += p; bd["age"] = p

        # Natural stop
        ns = r["ns"]
        if 4 <= ns <= 6: p = 8
        elif 6 < ns <= 8: p = 3
        elif ns < 4: p = -3
        else: p = -2
        s += p; bd["stp"] = p

        # Volume ratio
        v = r["vr"]
        if 0.9 <= v <= 1.1: p = 8
        elif 1.1 < v <= 1.3: p = 2
        elif 0.7 <= v < 0.9: p = -3
        elif v > 1.3: p = -3
        else: p = -1
        s += p; bd["vol"] = p

        # Momentum candles
        m = r["mom"]
        if 2 <= m <= 3: p = 6
        elif m == 1: p = 1
        elif m == 0: p = -4
        elif m >= 4: p = 2
        else: p = 0
        s += p; bd["mom"] = p

        # Directional candles — strongest soft factor
        dc = r["dc"]
        if dc >= 4: p = 10
        elif 2 <= dc <= 3: p = 4
        elif dc == 1: p = 0
        else: p = -8
        s += p; bd["dc"] = p

        # Z-score magnitude
        az = abs(r["zs"])
        if 0.5 <= az < 1.0: p = 5
        elif 1.0 <= az < 1.5: p = 4
        elif az >= 1.5: p = 2
        else: p = -7
        s += p; bd["z"] = p

        # BB position — reduced, weak factor
        bb = r["bbp"]
        if 0.65 <= bb <= 0.85: p = 3
        elif 0.50 <= bb < 0.65: p = 1
        elif 0.35 <= bb < 0.50: p = -2
        elif bb > 0.85: p = -2
        else: p = -1
        s += p; bd["bb"] = p

        # EMA50 distance — keep strong
        if r["e50d"] >= 60: p = 4
        elif r["e50d"] < 20: p = -8
        else: p = 0
        s += p; bd["e50"] = p

        # EMA20 distance — keep strong
        # EMA20 distance (e20<15 softened from -6 to -3, backtest-justified)
        if 15 <= r["e20d"] <= 30: p = 4
        elif r["e20d"] >= 30: p = 1
        elif r["e20d"] < 15: p = -3
        else: p = 0
        s += p; bd["e20"] = p

        # OTR — reduced, weak factor
        o = r["otr"]
        if 8 <= o <= 18: p = 2
        elif o < 8: p = -4
        elif o > 30: p = -1
        else: p = 0
        s += p; bd["otr"] = p

        # ADR consumed — token-sized, barely matters
        if r["adr"] < 0.8: p = 2
        elif 0.8 <= r["adr"] <= 1.2: p = -1
        else: p = -1
        s += p; bd["adr"] = p

        # Duration
        d = r["dur"]
        if 30 <= d <= 120: p = 5
        elif 120 < d <= 360: p = 2
        elif d < 30: p = -2
        elif 360 < d <= 720: p = -4
        else: p = 0
        s += p; bd["dur"] = p

        # Wall proximity — reduced, inconsistent
        wp = r["wp"]
        if wp < 0.15: p = 1
        elif 0.15 <= wp < 0.30: p = -3
        elif 0.30 <= wp < 0.50: p = 1
        else: p = -1
        s += p; bd["wal"] = p

        # Body %
        bp = r["bp"]
        if bp < 0.25: p = 1
        elif 0.25 <= bp < 0.45: p = 0
        elif 0.45 <= bp <= 0.65: p = -4
        else: p = -1
        s += p; bd["bdy"] = p

        # BB state
        bbs = r["bbs"]
        if bbs == "NORM": p = 2
        elif bbs in ("REJ_L", "REJ_S"): p = 3
        elif bbs in ("BRK_UP", "BRK_DN"): p = -2
        elif bbs == "STR_DN": p = -2
        else: p = 0
        s += p; bd["bbs"] = p

        # RSI (neutral zone is now soft penalty, not hard block)
        rsi = r["rsi"]
        if rsi < 30: p = 5
        elif 30 <= rsi < 45: p = 2
        elif 45 <= rsi <= 55: p = -5  # Was hard block, now soft penalty
        elif 55 < rsi < 70: p = -3
        elif rsi >= 70: p = -4
        else: p = 0
        s += p; bd["rsi"] = p

        # === CORRELATED-NEGATIVE CAPS ===
        # Prevent hour+age from triple-dipping with session thresholds
        hr_age_total = bd["hr"] + bd["age"]
        if hr_age_total < _MAX_HOUR_PLUS_AGE:
            cap_adj = _MAX_HOUR_PLUS_AGE - hr_age_total
            s += cap_adj
            bd["hr_age_cap"] = cap_adj

        # === FAMILY OVERLAYS ===
        family = ""
        if candidate and hasattr(candidate, "metadata") and candidate.metadata:
            family = candidate.metadata.get("strategy_family", "")

        if family == "trend":
            md = candidate.metadata or {}
            if md.get("structure_break_confirmed"):
                s += 6; bd["fam_struct"] = 6
            em = md.get("entry_type", "")
            if em == "DBB_PULLBACK" and md.get("pullback_depth_pct", 1.0) <= 0.55:
                s += 4; bd["fam_pb"] = 4
            elif em == "DBB_BREAKOUT":
                s += 4; bd["fam_brk"] = 4
            if dc >= 4:
                s += 2; bd["fam_dc"] = 2
            # Soften NY/stale for continuation trades
            if 16 <= r["hour"] < 20:
                s += 2; bd["fam_hr"] = 2
            if 18 <= r["bage"] < 24:
                s += 3; bd["fam_age"] = 3
            # Penalize exhausted chases
            if az >= 1.5 and r["e20d"] < 15:
                s -= 5; bd["fam_chase"] = -5

        # === LAYER 2: PAIRED ASPECT BONUSES (halved magnitudes) ===
        pairs = 0

        # Positive pairs
        if r["hour"] < 8 and bbs == "NORM":
            pairs += 8; bd["p_hr_norm"] = 8
        if r["hour"] < 8 and 0.5 <= az < 1.0:
            pairs += 6; bd["p_hr_z"] = 6
        if r["bage"] < 12 and rsi < 45:
            pairs += 6; bd["p_age_rsi"] = 6
        if r["bage"] < 12 and bbs == "NORM":
            pairs += 5; bd["p_age_norm"] = 5
        if r["bage"] < 12 and 8 <= r["otr"] <= 18:
            pairs += 4; bd["p_age_otr"] = 4
        if r["e50d"] >= 60 and dc >= 4:
            pairs += 5; bd["p_e50_dc"] = 5
        if 4 <= ns <= 6 and dc >= 4:
            pairs += 5; bd["p_ns_dc"] = 5
        if 1.0 <= az < 1.5 and bbs == "NORM":
            pairs += 5; bd["p_z_norm"] = 5

        # Negative pairs
        if 12 <= r["hour"] < 16 and 0.8 <= r["adr"] <= 1.2:
            pairs -= 6; bd["n_hr_adr"] = -6
        if 12 <= r["hour"] < 16 and dc == 0:
            pairs -= 6; bd["n_hr_dc0"] = -6
        if az < 0.5 and bbs == "NORM":
            pairs -= 6; bd["n_z_norm"] = -6
        if az < 0.5 and 0.8 <= r["adr"] <= 1.2:
            pairs -= 5; bd["n_z_adr"] = -5
        if r["mom"] == 0 and bb > 0.85:
            pairs -= 5; bd["n_mom_bb"] = -5
        if ns < 4 and 0.7 <= v < 0.9:
            pairs -= 4; bd["n_ns_vr"] = -4
        if dc == 0 and r["otr"] < 8:
            pairs -= 4; bd["n_dc_otr"] = -4

        # Neutral cluster cap
        neutral_pairs = sum(v for k, v in bd.items() if k.startswith("n_z_"))
        if neutral_pairs < _MAX_NEUTRAL_CLUSTER:
            cap_adj = _MAX_NEUTRAL_CLUSTER - neutral_pairs
            pairs += cap_adj
            bd["neutral_cap"] = cap_adj

        # === SESSION-AWARE PAIR CAPPING ===
        # Session detection now goes through the centralized clock (DST-aware,
        # Sydney-aware, 9 semantic labels). Threshold selection goes through a
        # compatibility map so production scoring behavior stays near-identical
        # while we ship the clock foundation. See scrooge_v3/core/clock.py.
        session_label: SessionLabel = self.clock.session_label()
        weekly_open_flag = self.clock.is_weekly_open()
        profile = compat_threshold_profile(session_label, family=family or "default")
        base_floor, final_min_b, final_min_a, pair_cap = profile.as_tuple()
        # Expose both the new semantic label and the compat key for audit.
        session = session_label.value

        # Cap positive pair bonuses (negative pairs always apply in full)
        positive_pairs = max(0, pairs)
        negative_pairs = min(0, pairs)
        if positive_pairs > pair_cap:
            bd["pair_cap_applied"] = pair_cap - positive_pairs
            positive_pairs = pair_cap
        capped_pairs = positive_pairs + negative_pairs

        base_score = s
        final_score = s + capped_pairs
        bd["pairs_total"] = capped_pairs
        bd["base_score"] = base_score

        # === SESSION-AWARE DECISION ===
        if base_score < base_floor:
            tier = "REJECT"
        elif final_score >= final_min_a:
            tier = "A"
        elif final_score >= final_min_b:
            tier = "B"
        else:
            tier = "REJECT"

        # Build raw audit string for verifiability
        raw_audit = ""
        if r.get("_price"):
            raw_audit = f" || px={r['_price']:.5f} ema20={r['_ema20']:.5f} ema50={r['_ema50']:.5f} box={r['_box_range']:.5f} age={r['_box_age_h']:.1f}h"

        log.info(
            "[V3_SCORER] base=%d final=%d tier=%s fam=%s session=%s (floor=%d b=%d a=%d cap=%d) pairs_raw=%+d capped=%+d | %s%s",
            base_score, final_score, tier, family or "default", session, base_floor, final_min_b, final_min_a, pair_cap,
            pairs, capped_pairs,
            " ".join(f"{k}={v:+d}" for k, v in bd.items() if k not in ("pairs_total", "base_score", "pair_cap_applied", "hr_age_cap", "neutral_cap")),
            raw_audit,
        )

        return ScorerResult(score=final_score, base_score=base_score, blocks=[], breakdown=bd, tier=tier, pairs_total=capped_pairs)
