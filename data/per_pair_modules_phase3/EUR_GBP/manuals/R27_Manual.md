# EUR_GBP — R27 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **875**  (W=583 / L=292)  -  WR: **66.6%**

## Session distribution

- ny_mid: n=209  W=138/L=71  WR=66.0%
- london: n=150  W=100/L=50  WR=66.7%
- london_open: n=127  W=83/L=44  WR=65.4%
- ny_open: n=119  W=78/L=41  WR=65.5%
- ny_close: n=118  W=81/L=37  WR=68.6%
- asia: n=77  W=57/L=20  WR=74.0%
- off_hours: n=53  W=32/L=21  WR=60.4%
- asia_late: n=22  W=14/L=8  WR=63.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60b AND T1=T1a AND T4=T4a`
- Raw: n=86  W=82/L=4  WR=95.3%
- Refine: exclude ZS=ZS3 drops 3/4 losers (75%)
- **Final: n=83  W=82/L=1  WR=98.8%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when zscore -1 to +1 neutral

### W02.  `H60=H60b AND T1=T1a AND direction_exec=long`
- Raw: n=86  W=82/L=4  WR=95.3%
- Refine: exclude ZS=ZS3 drops 3/4 losers (75%)
- **Final: n=83  W=82/L=1  WR=98.8%**
- **Dir: LONG**  •  HTF60 slightly aligned; 1h trend WITH trade  •  AVOID when zscore -1 to +1 neutral

### W03.  `H60=H60b AND T4=T4a AND direction_exec=long`
- Raw: n=86  W=82/L=4  WR=95.3%
- Refine: exclude ZS=ZS3 drops 3/4 losers (75%)
- **Final: n=83  W=82/L=1  WR=98.8%**
- **Dir: LONG**  •  HTF60 slightly aligned; 4h trend WITH trade  •  AVOID when zscore -1 to +1 neutral

### W04.  `H60=H60b AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=86  W=82/L=4  WR=95.3%
- Refine: exclude ZS=ZS3 drops 3/4 losers (75%)
- **Final: n=83  W=82/L=1  WR=98.8%**
- **Dir: LONG**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when zscore -1 to +1 neutral

### W05.  `H60=H60a AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=71  W=66/L=5  WR=93.0%
- Refine: exclude session_bucket=ny_close drops 3/5 losers (60%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=ny_close

### W06.  `H60=H60a AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude session_bucket=ny_close drops 3/5 losers (60%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W07.  `H60=H60a AND BBP=BBP4 AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude session_bucket=ny_close drops 3/5 losers (60%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 70-80 overbought; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W08.  `H20=H20b AND H60=H60a AND BBP=BBP4`
- Raw: n=65  W=61/L=4  WR=93.8%
- Refine: no further refinement
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; upper third

### W09.  `H20=H20b AND H60=H60a AND T1=T1a`
- Raw: n=64  W=55/L=9  WR=85.9%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=56  W=51/L=5  WR=91.1%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when zscore -1 to +1 neutral

### W10.  `H20=H20b AND H60=H60a AND direction_exec=long`
- Raw: n=64  W=55/L=9  WR=85.9%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=56  W=51/L=5  WR=91.1%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade  •  AVOID when zscore -1 to +1 neutral

### W11.  `H20=H20b AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=64  W=55/L=9  WR=85.9%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=56  W=51/L=5  WR=91.1%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when zscore -1 to +1 neutral

### W12.  `H20=H20b AND H60=H60a AND ZS=ZS4`
- Raw: n=61  W=57/L=4  WR=93.4%
- Refine: no further refinement
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; zscore +1 to +2 overbought

### W13.  `H20=H20b AND H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=61  W=57/L=4  WR=93.4%
- Refine: no further refinement
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought

### W14.  `H60=H60a AND T1=T1c AND RSI=RSI6`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude H20=H20a drops 5/6 losers (83%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought  •  AVOID when HTF20 aligned WITH trade

### W15.  `H60=H60a AND T4=T4c AND RSI=RSI6`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude H20=H20a drops 5/6 losers (83%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  AVOID when HTF20 aligned WITH trade

### W16.  `H60=H60a AND RSI=RSI6 AND direction_exec=short`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude H20=H20a drops 5/6 losers (83%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 70-80 overbought  •  AVOID when HTF20 aligned WITH trade

### W17.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude H20=H20a drops 5/6 losers (83%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  AVOID when HTF20 aligned WITH trade

### W18.  `H60=H60a AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude H20=H20a drops 5/6 losers (83%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought  •  AVOID when HTF20 aligned WITH trade

### W19.  `H60=H60a AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude H20=H20a drops 5/6 losers (83%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  AVOID when HTF20 aligned WITH trade

### W20.  `H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude H20=H20a drops 4/8 losers (50%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W21.  `H60=H60a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude H20=H20a drops 4/8 losers (50%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W22.  `H60=H60a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude H20=H20a drops 4/8 losers (50%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W23.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude H20=H20a drops 4/8 losers (50%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W24.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude H20=H20a drops 4/8 losers (50%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W25.  `H60=H60a AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude H20=H20a drops 4/8 losers (50%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60d AND T1=T1c AND T4=T4c`
- Raw: n=61  W=13/L=48  WR=21.3%
- Sharpen: sharpest is ZS=ZS5 (19/48 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L02.  `H60=H60d AND T1=T1c AND direction_exec=short`
- Raw: n=61  W=13/L=48  WR=21.3%
- Sharpen: sharpest is ZS=ZS5 (19/48 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L03.  `H60=H60d AND T4=T4c AND direction_exec=short`
- Raw: n=61  W=13/L=48  WR=21.3%
- Sharpen: sharpest is ZS=ZS5 (19/48 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L04.  `H60=H60d AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=61  W=13/L=48  WR=21.3%
- Sharpen: sharpest is ZS=ZS5 (19/48 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L05.  `H20=H20d AND H60=H60e AND T4=T4a`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is ZS=ZS4 (9/25 of losers there)
- **Sharp: n=10  W=1/L=9  WR=10.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when zscore +1 to +2 overbought

### L06.  `H20=H20d AND T1=T1a AND RSI=RSI6`
- Raw: n=38  W=14/L=24  WR=36.8%
- Sharpen: sharpest is session_bucket=ny_open (12/24 of losers there)
- **Sharp: n=15  W=3/L=12  WR=20.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; RSI 70-80 overbought  •  ONLY when session=ny_open

### L07.  `H20=H20d AND T4=T4a AND RSI=RSI6`
- Raw: n=38  W=14/L=24  WR=36.8%
- Sharpen: sharpest is session_bucket=ny_open (12/24 of losers there)
- **Sharp: n=15  W=3/L=12  WR=20.0%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; RSI 70-80 overbought  •  ONLY when session=ny_open

### L08.  `H20=H20d AND RSI=RSI6 AND direction_exec=long`
- Raw: n=38  W=14/L=24  WR=36.8%
- Sharpen: sharpest is session_bucket=ny_open (12/24 of losers there)
- **Sharp: n=15  W=3/L=12  WR=20.0%**
- **Dir: LONG**  •  HTF20 mildly against; RSI 70-80 overbought  •  ONLY when session=ny_open

### L09.  `H20=H20d AND T1=T1a AND T4=T4a AND RSI=RSI6`
- Raw: n=38  W=14/L=24  WR=36.8%
- Sharpen: sharpest is session_bucket=ny_open (12/24 of losers there)
- **Sharp: n=15  W=3/L=12  WR=20.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  ONLY when session=ny_open

### L10.  `H20=H20d AND T1=T1a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=38  W=14/L=24  WR=36.8%
- Sharpen: sharpest is session_bucket=ny_open (12/24 of losers there)
- **Sharp: n=15  W=3/L=12  WR=20.0%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend WITH trade; RSI 70-80 overbought  •  ONLY when session=ny_open

### L11.  `H20=H20d AND T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=38  W=14/L=24  WR=36.8%
- Sharpen: sharpest is session_bucket=ny_open (12/24 of losers there)
- **Sharp: n=15  W=3/L=12  WR=20.0%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend WITH trade; RSI 70-80 overbought  •  ONLY when session=ny_open

### L12.  `H20=H20e AND H60=H60d AND T4=T4c`
- Raw: n=31  W=4/L=27  WR=12.9%
- Sharpen: sharpest is ZS=ZS5 (18/27 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L13.  `H20=H20b AND H60=H60d AND T1=T1c`
- Raw: n=31  W=9/L=22  WR=29.0%
- Sharpen: sharpest is RSI=RSI4 (16/22 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L14.  `H20=H20b AND H60=H60d AND T4=T4c`
- Raw: n=31  W=9/L=22  WR=29.0%
- Sharpen: sharpest is RSI=RSI4 (16/22 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L15.  `H20=H20b AND H60=H60d AND direction_exec=short`
- Raw: n=31  W=9/L=22  WR=29.0%
- Sharpen: sharpest is RSI=RSI4 (16/22 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 mildly against  •  ONLY when RSI 50-60 upper neutral

### L16.  `H20=H20b AND H60=H60d AND T1=T1c AND T4=T4c`
- Raw: n=31  W=9/L=22  WR=29.0%
- Sharpen: sharpest is RSI=RSI4 (16/22 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L17.  `H20=H20b AND H60=H60d AND T1=T1c AND direction_exec=short`
- Raw: n=31  W=9/L=22  WR=29.0%
- Sharpen: sharpest is RSI=RSI4 (16/22 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L18.  `H20=H20b AND H60=H60d AND T4=T4c AND direction_exec=short`
- Raw: n=31  W=9/L=22  WR=29.0%
- Sharpen: sharpest is RSI=RSI4 (16/22 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L19.  `H60=H60d AND T1=T1c AND RSI=RSI4`
- Raw: n=31  W=12/L=19  WR=38.7%
- Sharpen: sharpest is H20=H20b (16/19 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF20 slightly aligned

### L20.  `H20=H20e AND H60=H60d AND T1=T1c`
- Raw: n=30  W=4/L=26  WR=13.3%
- Sharpen: sharpest is ZS=ZS5 (18/26 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L21.  `H20=H20e AND H60=H60d AND direction_exec=short`
- Raw: n=30  W=4/L=26  WR=13.3%
- Sharpen: sharpest is ZS=ZS5 (18/26 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 mildly against  •  ONLY when zscore +2 to +3 deep overbought

### L22.  `H20=H20e AND H60=H60d AND T1=T1c AND T4=T4c`
- Raw: n=30  W=4/L=26  WR=13.3%
- Sharpen: sharpest is ZS=ZS5 (18/26 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `H20=H20e AND H60=H60d AND T1=T1c AND direction_exec=short`
- Raw: n=30  W=4/L=26  WR=13.3%
- Sharpen: sharpest is ZS=ZS5 (18/26 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `H20=H20e AND H60=H60d AND T4=T4c AND direction_exec=short`
- Raw: n=30  W=4/L=26  WR=13.3%
- Sharpen: sharpest is ZS=ZS5 (18/26 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `H60=H60d AND T1=T1c AND RSI=RSI5`
- Raw: n=30  W=7/L=23  WR=23.3%
- Sharpen: sharpest is H20=H20e (17/23 of losers there)
- **Sharp: n=18  W=1/L=17  WR=5.6%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(14/8) | H20e(9/17) |
| H60 | H60b(24/11), H60a(35/23) | H60d(9/28), H60e(27/32) |
| T1 | — | — |
| T4 | — | — |
| BBP | BBP4(52/46) | — |
| RSI | — | — |
| ZS | ZS4(49/40) | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
