# Mr. Scrooge Parity Harness

type: system
status: active
tags: [trading, scrooge, monitoring, parity, automation]

trust:
  score: 85
  confidence: high
  evidence:
    - source: deployed and verified 2026-04-12
      type: reproducible

## Summary

Continuous alignment monitor that compares V1 and V2 status.json every 90 seconds. Detects session mismatches, regime score drift, signal validity divergence, and market summary discrepancies. Deployed as a systemd service on EC2, independent from both bots.

## Architecture

- Script: ~/parity_harness.py
- Service: parity-harness.service (systemd user unit)
- Log: ~/parity_harness/parity.log
- Snapshots: ~/parity_harness/snapshots/ (saved on drift detection)
- Input: V1 data/status.json + V2 data/status.json
- Interval: 90 seconds

## Severity Levels

| Level | Trigger | Example |
|-------|---------|---------|
| CRITICAL | Validity mismatch (valid=True vs valid=False/None) | One bot classifies a setup as valid, the other doesn't |
| WARNING | Score delta > 1 between V1 and V2 for same pair | BB position near 0.85 threshold causes 4-8 pt swings |
| INFO | All pairs match within tolerance | Normal operation |

## Known Benign Mismatches

- **BB position threshold**: When bb_pos is near 0.85, a 30-second fetch gap can flip the +8/+4 scoring tier. Shows as WARNING with 4-8 point delta. Not actionable.
- **NO_TRADE validity gap**: V2's validity_detail only populates on ENTER signals. NO_TRADE signals have validity=None. Shows as CRITICAL but is cosmetic. Fix planned but low priority.
- **Viable count ±1**: V2's OANDA practice API returns 502s intermittently, causing pair skips despite the bar cache fallback. Shows as SUMMARY DRIFT.

## Key File Paths

| File | Purpose |
|------|---------|
| ~/parity_harness.py | Main script |
| ~/.config/systemd/user/parity-harness.service | Service unit |
| ~/parity_harness/parity.log | Rolling log |
| ~/parity_harness/snapshots/ | Full status.json captures on drift |

## Related

- [[Mr. Scrooge V1 Changelog]]
- [[Mr. Scrooge V2 Changelog]]
- [[Mr. Scrooge Known Defects]]
- [[Mr. Scrooge Architecture]]
