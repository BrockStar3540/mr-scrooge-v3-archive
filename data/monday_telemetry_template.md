# Monday 2026-05-25 Telemetry Report Template

**Reopen:** Sunday 2026-05-24 22:00 UTC  
**First windows to monitor:** asia (00:00-06:00), london_open (06:00-09:00), ny_mid (13:00-16:00)

---

## A. Asia Window (00:00–06:00 UTC)

### Expected leaves to fire
- C01 EUR_USD asia: RG1_range_bound_scalp_short, MR5_williams_extreme_short
- C02 EUR_USD asia: MTB_S3W0M35P20_long
- C01 USD_JPY asia: BR2_vcb_long
- C02 USD_JPY asia: SS1_asian_range_breakout_long
- MTB_C01_3 EUR_GBP asia: MTB1_pitchfork_long_strict

### Telemetry to check
```bash
# Pull telemetry log
grep "asia" /path/to/telemetry.log | grep "2026-05-25" | head -50

# Check for silence
grep "no_routing_match\|death\|block" /path/to/telemetry.log | grep "2026-05-25 0[0-6]" | head -20
```

### Fill: ___
### Approvals: ___
### Silences: ___
### Family mix: ___
### Anomalies: ___

---

## B. London Open Window (06:00–09:00 UTC)

### Expected leaves to fire
- C02 USD_JPY london_open: MR2_bb_reversion_long
- C02 AUD_JPY london_open: MTB_S4W30M35P20_long
- MTB_C02_6 EUR_GBP london_open: MTB1_pitchfork_short_strict
- MTB_C02_9 EUR_JPY london_open: MTB1_pitchfork_long_strict

### Fill: ___
### Approvals: ___
### Silences: ___
### Family mix: ___
### Anomalies: ___

---

## C. NY Mid Window (13:00–16:00 UTC)

### Expected leaves to fire (v1.11.5 live, will be thin)
- (only 1 cell: MTB_C01_6 USD_MXN ny_mid — this is on the DROP list)

### Note: If TIER1A already flipped, expect:
- C01 EUR_USD ny_mid: MR2_bb_reversion_short
- C01 AUD_USD ny_mid: MR2_bb_reversion_short

### Fill: ___
### Approvals: ___
### Silences: ___
### Family mix: ___
### Anomalies: ___

---

## D. Weak Cell Watch List

These are the 10 cells being dropped in v1.12_TIER1A. Watch if they misbehave before the flip:

| Cell | Why it's on the drop list | What to watch for |
|------|--------------------------|-------------------|
| MTB_C01_6 USD_MXN ny_mid | 0% recent WR, WLB 0.339 | Fills that immediately stop out |
| C01 EUR_CHF asia MTB1_pitchfork_short_strict | WLB 0.337, weakest MTB | Repeated blocks / no fills |
| C02 EUR_USD asia MTB_S2W0M30P20_short | WLB 0.349, WR 36.9% | Stop-out pattern |
| C01 asia EUR_USD CP3_vol_coil_fade_short | WLB 0.347, WR 35.9% | Long losing streaks |

---

## E. Flip Decision Checklist

After Asia + London windows:

- [ ] At least 1 fill in asia window
- [ ] No repeated silence across london_open
- [ ] USD_MXN ny_mid MTB cell does not misbehave (or accept the stop-out and proceed with flip)
- [ ] No bot errors in telemetry log
- [ ] Bot process running normally (check PID, memory)

If all boxes checked: **proceed with v1.12_TIER1A flip**

```bash
# Flip command (update config path, then restart)
# See v1_12_tier1a_flip_package.md for full instructions
```
