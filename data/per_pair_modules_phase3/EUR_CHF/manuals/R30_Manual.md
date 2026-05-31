# EUR_CHF — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **511**  (W=321 / L=190)  -  WR: **62.8%**

## Session distribution

- asia: n=186  W=115/L=71  WR=61.8%
- ny_mid: n=155  W=96/L=59  WR=61.9%
- ny_open: n=66  W=37/L=29  WR=56.1%
- london_open: n=37  W=23/L=14  WR=62.2%
- asia_late: n=25  W=21/L=4  WR=84.0%
- ny_close: n=21  W=14/L=7  WR=66.7%
- off_hours: n=21  W=15/L=6  WR=71.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60e AND T1=T1c`
- Raw: n=163  W=140/L=23  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 13/23 losers (57%)
- **Final: n=112  W=102/L=10  WR=91.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when session=ny_mid

### W02.  `H20=H20e AND H60=H60e AND T4=T4c`
- Raw: n=163  W=140/L=23  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 13/23 losers (57%)
- **Final: n=112  W=102/L=10  WR=91.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when session=ny_mid

### W03.  `H20=H20e AND H60=H60e AND direction_exec=long`
- Raw: n=163  W=140/L=23  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 13/23 losers (57%)
- **Final: n=112  W=102/L=10  WR=91.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against  •  AVOID when session=ny_mid

### W04.  `H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=163  W=140/L=23  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 13/23 losers (57%)
- **Final: n=112  W=102/L=10  WR=91.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_mid

### W05.  `H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=163  W=140/L=23  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 13/23 losers (57%)
- **Final: n=112  W=102/L=10  WR=91.1%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when session=ny_mid

### W06.  `H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=163  W=140/L=23  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 13/23 losers (57%)
- **Final: n=112  W=102/L=10  WR=91.1%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when session=ny_mid

### W07.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=163  W=140/L=23  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 13/23 losers (57%)
- **Final: n=112  W=102/L=10  WR=91.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_mid

### W08.  `H20=H20e AND H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=163  W=140/L=23  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 13/23 losers (57%)
- **Final: n=112  W=102/L=10  WR=91.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when session=ny_mid

### W09.  `H20=H20e AND H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=163  W=140/L=23  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 13/23 losers (57%)
- **Final: n=112  W=102/L=10  WR=91.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when session=ny_mid

### W10.  `H60=H60e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=163  W=140/L=23  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 13/23 losers (57%)
- **Final: n=112  W=102/L=10  WR=91.1%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_mid

### W11.  `H20=H20e AND H60=H60e AND RSI=RSI1`
- Raw: n=107  W=102/L=5  WR=95.3%
- Refine: exclude ZS=ZS3 drops 3/5 losers (60%)
- **Final: n=97  W=95/L=2  WR=97.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 20-30 oversold  •  AVOID when zscore -1 to +1 neutral

### W12.  `H60=H60e AND T1=T1c AND RSI=RSI1`
- Raw: n=107  W=102/L=5  WR=95.3%
- Refine: exclude ZS=ZS3 drops 3/5 losers (60%)
- **Final: n=97  W=95/L=2  WR=97.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  AVOID when zscore -1 to +1 neutral

### W13.  `H60=H60e AND T4=T4c AND RSI=RSI1`
- Raw: n=107  W=102/L=5  WR=95.3%
- Refine: exclude ZS=ZS3 drops 3/5 losers (60%)
- **Final: n=97  W=95/L=2  WR=97.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  AVOID when zscore -1 to +1 neutral

### W14.  `H60=H60e AND RSI=RSI1 AND direction_exec=long`
- Raw: n=107  W=102/L=5  WR=95.3%
- Refine: exclude ZS=ZS3 drops 3/5 losers (60%)
- **Final: n=97  W=95/L=2  WR=97.9%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 20-30 oversold  •  AVOID when zscore -1 to +1 neutral

### W15.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI1`
- Raw: n=107  W=102/L=5  WR=95.3%
- Refine: exclude ZS=ZS3 drops 3/5 losers (60%)
- **Final: n=97  W=95/L=2  WR=97.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  AVOID when zscore -1 to +1 neutral

### W16.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI1`
- Raw: n=107  W=102/L=5  WR=95.3%
- Refine: exclude ZS=ZS3 drops 3/5 losers (60%)
- **Final: n=97  W=95/L=2  WR=97.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  AVOID when zscore -1 to +1 neutral

### W17.  `H20=H20e AND H60=H60e AND RSI=RSI1 AND direction_exec=long`
- Raw: n=107  W=102/L=5  WR=95.3%
- Refine: exclude ZS=ZS3 drops 3/5 losers (60%)
- **Final: n=97  W=95/L=2  WR=97.9%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; RSI 20-30 oversold  •  AVOID when zscore -1 to +1 neutral

### W18.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=107  W=102/L=5  WR=95.3%
- Refine: exclude ZS=ZS3 drops 3/5 losers (60%)
- **Final: n=97  W=95/L=2  WR=97.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  AVOID when zscore -1 to +1 neutral

### W19.  `H60=H60e AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=107  W=102/L=5  WR=95.3%
- Refine: exclude ZS=ZS3 drops 3/5 losers (60%)
- **Final: n=97  W=95/L=2  WR=97.9%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  AVOID when zscore -1 to +1 neutral

### W20.  `H60=H60e AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=107  W=102/L=5  WR=95.3%
- Refine: exclude ZS=ZS3 drops 3/5 losers (60%)
- **Final: n=97  W=95/L=2  WR=97.9%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  AVOID when zscore -1 to +1 neutral

### W21.  `H20=H20e AND H60=H60e AND BBP=BBP2`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=ny_mid drops 10/10 losers (100%)
- **Final: n=43  W=43/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third  •  AVOID when session=ny_mid

### W22.  `H60=H60e AND T1=T1c AND BBP=BBP2`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=ny_mid drops 10/10 losers (100%)
- **Final: n=43  W=43/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third  •  AVOID when session=ny_mid

### W23.  `H60=H60e AND T4=T4c AND BBP=BBP2`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=ny_mid drops 10/10 losers (100%)
- **Final: n=43  W=43/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third  •  AVOID when session=ny_mid

### W24.  `H60=H60e AND BBP=BBP2 AND direction_exec=long`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=ny_mid drops 10/10 losers (100%)
- **Final: n=43  W=43/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; lower third  •  AVOID when session=ny_mid

### W25.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP2`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=ny_mid drops 10/10 losers (100%)
- **Final: n=43  W=43/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; lower third  •  AVOID when session=ny_mid

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60a AND T1=T1a`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is RSI=RSI1 (43/67 of losers there)
- **Sharp: n=59  W=16/L=43  WR=27.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when RSI 20-30 oversold

### L02.  `H20=H20a AND H60=H60a AND T4=T4a`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is RSI=RSI1 (43/67 of losers there)
- **Sharp: n=59  W=16/L=43  WR=27.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when RSI 20-30 oversold

### L03.  `H20=H20a AND H60=H60a AND direction_exec=short`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is RSI=RSI1 (43/67 of losers there)
- **Sharp: n=59  W=16/L=43  WR=27.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade  •  ONLY when RSI 20-30 oversold

### L04.  `H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is RSI=RSI1 (43/67 of losers there)
- **Sharp: n=59  W=16/L=43  WR=27.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 20-30 oversold

### L05.  `H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is RSI=RSI1 (43/67 of losers there)
- **Sharp: n=59  W=16/L=43  WR=27.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when RSI 20-30 oversold

### L06.  `H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is RSI=RSI1 (43/67 of losers there)
- **Sharp: n=59  W=16/L=43  WR=27.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when RSI 20-30 oversold

### L07.  `H20=H20a AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is RSI=RSI1 (43/67 of losers there)
- **Sharp: n=59  W=16/L=43  WR=27.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 20-30 oversold

### L08.  `H20=H20a AND H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is RSI=RSI1 (43/67 of losers there)
- **Sharp: n=59  W=16/L=43  WR=27.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when RSI 20-30 oversold

### L09.  `H20=H20a AND H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is RSI=RSI1 (43/67 of losers there)
- **Sharp: n=59  W=16/L=43  WR=27.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when RSI 20-30 oversold

### L10.  `H60=H60a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is RSI=RSI1 (43/67 of losers there)
- **Sharp: n=59  W=16/L=43  WR=27.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 20-30 oversold

### L11.  `H20=H20e AND H60=H60c AND T1=T1c`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_open (24/43 of losers there)
- **Sharp: n=34  W=10/L=24  WR=29.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 neutral; 1h trend AGAINST trade  •  ONLY when session=ny_open

### L12.  `H20=H20e AND H60=H60c AND T4=T4c`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_open (24/43 of losers there)
- **Sharp: n=34  W=10/L=24  WR=29.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 neutral; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L13.  `H20=H20e AND H60=H60c AND direction_exec=long`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_open (24/43 of losers there)
- **Sharp: n=34  W=10/L=24  WR=29.4%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 neutral  •  ONLY when session=ny_open

### L14.  `H60=H60c AND T1=T1c AND T4=T4c`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_open (24/43 of losers there)
- **Sharp: n=34  W=10/L=24  WR=29.4%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L15.  `H60=H60c AND T1=T1c AND direction_exec=long`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_open (24/43 of losers there)
- **Sharp: n=34  W=10/L=24  WR=29.4%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend AGAINST trade  •  ONLY when session=ny_open

### L16.  `H60=H60c AND T4=T4c AND direction_exec=long`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_open (24/43 of losers there)
- **Sharp: n=34  W=10/L=24  WR=29.4%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L17.  `H20=H20e AND H60=H60c AND T1=T1c AND T4=T4c`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_open (24/43 of losers there)
- **Sharp: n=34  W=10/L=24  WR=29.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L18.  `H20=H20e AND H60=H60c AND T1=T1c AND direction_exec=long`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_open (24/43 of losers there)
- **Sharp: n=34  W=10/L=24  WR=29.4%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 neutral; 1h trend AGAINST trade  •  ONLY when session=ny_open

### L19.  `H20=H20e AND H60=H60c AND T4=T4c AND direction_exec=long`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_open (24/43 of losers there)
- **Sharp: n=34  W=10/L=24  WR=29.4%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 neutral; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L20.  `H60=H60c AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_open (24/43 of losers there)
- **Sharp: n=34  W=10/L=24  WR=29.4%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L21.  `H20=H20a AND H60=H60a AND RSI=RSI1`
- Raw: n=59  W=16/L=43  WR=27.1%
- Sharpen: sharpest is session_bucket=asia (14/43 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 20-30 oversold  •  ONLY when session=asia

### L22.  `H60=H60a AND T1=T1a AND RSI=RSI1`
- Raw: n=59  W=16/L=43  WR=27.1%
- Sharpen: sharpest is session_bucket=asia (14/43 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 20-30 oversold  •  ONLY when session=asia

### L23.  `H60=H60a AND T4=T4a AND RSI=RSI1`
- Raw: n=59  W=16/L=43  WR=27.1%
- Sharpen: sharpest is session_bucket=asia (14/43 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 20-30 oversold  •  ONLY when session=asia

### L24.  `H60=H60a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=59  W=16/L=43  WR=27.1%
- Sharpen: sharpest is session_bucket=asia (14/43 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 20-30 oversold  •  ONLY when session=asia

### L25.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI1`
- Raw: n=59  W=16/L=43  WR=27.1%
- Sharpen: sharpest is session_bucket=asia (14/43 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 20-30 oversold  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(63/44) | H20a(37/56) |
| H60 | H60e(44/12) | H60a(13/35), H60b(5/12) |
| T1 | T1c(63/44) | T1a(37/56) |
| T4 | T4c(63/44) | T4a(37/56) |
| BBP | BBP2(53/46) | — |
| RSI | RSI1(55/42) | RSI0(35/47) |
| ZS | ZS2(49/43) | — |
| strategy_id | — | — |
| direction_exec | long(63/44) | short(37/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
