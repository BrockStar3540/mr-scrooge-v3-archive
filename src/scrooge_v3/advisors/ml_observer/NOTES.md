# ML Observer — Scrooge Trade Watcher

Created: 2026-04-13
Author: Claude Code session with Brock

## Purpose

Passive XGBoost-based ML observer that watches both Mr. Scrooge V1 (live)
and V2 (practice) trading bots. Collects signal data, trains a win/loss
classifier after enough trades accumulate, and logs "protests" when its
predictions disagree with bot decisions. Never takes action — read-only.

## Architecture

- Standalone systemd service: `ml-observer.service`
- Reads bot data files only (status.json, entry-context.jsonl, regime-protests.jsonl)
- Writes to its own data/ and logs/ directories
- Shares the `~/mr_scrooge_env` venv (xgboost 3.2.0 installed 2026-04-13)
- 5-minute cycle aligned with bot cycles

## Three Phases (auto-advancing)

1. **Collector** (active now) — records ALL evaluated signals from both bots
   every cycle. Includes rejected setups, not just entries.
2. **Learner** (triggers at 50+ closed trades) — trains XGBoost classifier
   with 5-fold CV, logs feature importance.
3. **Advisor** (triggers at >60% CV accuracy) — logs protests to
   `data/ml-protests.jsonl` when ML disagrees with bot decisions.

## Files

| File | Purpose |
|------|---------|
| observer.py | Main loop — collect, phase-check, learn, advise, sleep |
| features.py | Extracts 24-feature vector from status.json signal objects |
| trainer.py | XGBoost training, cross-validation, feature importance |
| config.py | Paths, thresholds, XGBoost params |

## Data Files

| File | Content |
|------|---------|
| data/observations.jsonl | Every evaluated signal with features + eventual outcome |
| data/ml-protests.jsonl | ML disagreements (Phase 3 only) |
| data/model.xgb | Trained XGBoost model (Phase 2+) |
| data/observer-state.json | Persistent state (phase, counts, file offsets) |

## 24 Features

Score components (9): score, zone, atr, otr, rr, pattern, z_edge, bb_edge, structure
Validity metrics (4): z_score, bb_pos, adr, touch_count
Gate values (2): atr_consumed, otr_ratio
Trade setup (3): risk_reward, regime_score, direction
Temporal (1): hour_utc
Gate pass/fail (5): zone, atr, sucker, pitchfork, otr

## Service Commands

```bash
systemctl --user status ml-observer
systemctl --user restart ml-observer
journalctl --user -u ml-observer -f
tail -f logs/ml-observer.log
wc -l data/observations.jsonl
cat data/observer-state.json
```

## Context

Deployed at the start of the 2026-04-12 beta epoch — fresh data after
major defect-fix and scoring recalibration. Both bots (V1+V2) have clean
logs from this date forward. The observer starts with zero historical data
and learns purely from this new epoch.

---

## 2026-04-16: Rewired for V3 — V1/V2 Decommissioned

V1 and V2 have been fully decommissioned and deleted from EC2. The ML Observer
has been rewired to watch V3 only via its REST API (http://127.0.0.1:8084/api/data).

### Changes
- **config.py**: Replaced V1_DIR/V2_DIR/BOTS dict with V3_API_URL + V3_AUTH.
  No more reading status.json files from disk.
- **features.py**: Complete rewrite. Old 24-feature vector (score_detail + validity + gates)
  replaced with 31-feature vector for V3: 17 scorer breakdown factors (hr, age, stp, vol, etc.),
  v3_score, pairs_total, 9 market features from modules (z_score, bb_position, rsi, etc.),
  regime_score, hour_utc.
- **observer.py**: Fetches from V3 API via requests.get() instead of reading JSON files.
  Deduplicates by V3 cycle_count. Checks recent_closes from API for trade outcomes.
  Advise phase uses V3 verdicts (TAKE_LONG/TAKE_SHORT vs NO_CANDIDATE/V3_REJECT/V3_BLOCKED).
- **State reset**: Old V1/V2 observations archived to observations-v1v2-archive.jsonl.
  Fresh start at phase=1 with 0 observations. Model will retrain from scratch on V3 data.

### What stays the same
- Three-phase system (Collector → Learner → Advisor) unchanged
- XGBoost model and training pipeline unchanged (trainer.py not modified)
- Never takes action — read-only observer, logs protests only
- 5-minute cycle, same thresholds (50 trades for Phase 2, 60% accuracy for Phase 3)
