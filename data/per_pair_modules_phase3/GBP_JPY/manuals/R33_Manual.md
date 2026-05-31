# GBP_JPY — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **6,460**  (W=3,930 / L=2,530)  -  WR: **60.8%**

## Session distribution

- asia: n=2433  W=1517/L=916  WR=62.4%
- ny_close: n=1296  W=794/L=502  WR=61.3%
- london_open: n=760  W=458/L=302  WR=60.3%
- ny_mid: n=715  W=410/L=305  WR=57.3%
- asia_late: n=407  W=245/L=162  WR=60.2%
- off_hours: n=356  W=230/L=126  WR=64.6%
- ny_open: n=342  W=188/L=154  WR=55.0%
- london: n=151  W=88/L=63  WR=58.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60e AND T4=T4c`
- Raw: n=162  W=153/L=9  WR=94.4%
- Refine: exclude session_bucket=asia_late drops 6/9 losers (67%)
- **Final: n=148  W=145/L=3  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when session=asia_late

### W02.  `H20=H20a AND T1=T1c AND T4=T4c`
- Raw: n=162  W=153/L=9  WR=94.4%
- Refine: exclude session_bucket=asia_late drops 6/9 losers (67%)
- **Final: n=148  W=145/L=3  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=asia_late

### W03.  `H20=H20a AND T4=T4c AND direction_exec=short`
- Raw: n=162  W=153/L=9  WR=94.4%
- Refine: exclude session_bucket=asia_late drops 6/9 losers (67%)
- **Final: n=148  W=145/L=3  WR=98.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when session=asia_late

### W04.  `H20=H20a AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=162  W=153/L=9  WR=94.4%
- Refine: exclude session_bucket=asia_late drops 6/9 losers (67%)
- **Final: n=148  W=145/L=3  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=asia_late

### W05.  `H20=H20a AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=162  W=153/L=9  WR=94.4%
- Refine: exclude session_bucket=asia_late drops 6/9 losers (67%)
- **Final: n=148  W=145/L=3  WR=98.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when session=asia_late

### W06.  `H20=H20a AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=162  W=153/L=9  WR=94.4%
- Refine: exclude session_bucket=asia_late drops 6/9 losers (67%)
- **Final: n=148  W=145/L=3  WR=98.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=asia_late

### W07.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=130  W=115/L=15  WR=88.5%
- Refine: exclude session_bucket=asia_late drops 9/15 losers (60%)
- **Final: n=121  W=115/L=6  WR=95.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=asia_late

### W08.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=130  W=115/L=15  WR=88.5%
- Refine: exclude session_bucket=asia_late drops 9/15 losers (60%)
- **Final: n=121  W=115/L=6  WR=95.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=asia_late

### W09.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude H20=H20e drops 17/17 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third; session=asia  •  AVOID when HTF20 strongly against

### W10.  `T1=T1a AND T4=T4c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude H20=H20e drops 16/16 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 strongly against

### W11.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=105  W=92/L=13  WR=87.6%
- Refine: exclude session_bucket=asia_late drops 8/13 losers (62%)
- **Final: n=97  W=92/L=5  WR=94.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia_late

### W12.  `T4=T4c AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=105  W=92/L=13  WR=87.6%
- Refine: exclude session_bucket=asia_late drops 8/13 losers (62%)
- **Final: n=97  W=92/L=5  WR=94.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia_late

### W13.  `H60=H60e AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude session_bucket=ny_close drops 7/15 losers (47%)
- **Final: n=85  W=77/L=8  WR=90.6%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W14.  `RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude session_bucket=ny_close drops 7/15 losers (47%)
- **Final: n=85  W=77/L=8  WR=90.6%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W15.  `H60=H60e AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude session_bucket=ny_close drops 7/15 losers (47%)
- **Final: n=85  W=77/L=8  WR=90.6%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W16.  `H20=H20a AND T4=T4c AND session_bucket=asia`
- Raw: n=98  W=90/L=8  WR=91.8%
- Refine: exclude ZS=ZS2 drops 6/8 losers (75%)
- **Final: n=90  W=88/L=2  WR=97.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W17.  `H20=H20a AND H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=97  W=94/L=3  WR=96.9%
- Refine: exclude BBP=BBP1 drops 2/3 losers (67%)
- **Final: n=93  W=92/L=1  WR=98.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when just touched lower band

### W18.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=97  W=94/L=3  WR=96.9%
- Refine: exclude BBP=BBP1 drops 2/3 losers (67%)
- **Final: n=93  W=92/L=1  WR=98.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when just touched lower band

### W19.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=97  W=94/L=3  WR=96.9%
- Refine: exclude BBP=BBP1 drops 2/3 losers (67%)
- **Final: n=93  W=92/L=1  WR=98.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when just touched lower band

### W20.  `H60=H60e AND ZS=ZS4 AND session_bucket=off_hours`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=off_hours  •  AVOID when HTF20 strongly against

### W21.  `T1=T1c AND ZS=ZS4 AND session_bucket=off_hours`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=off_hours  •  AVOID when HTF20 strongly against

### W22.  `T4=T4c AND ZS=ZS4 AND session_bucket=off_hours`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=off_hours  •  AVOID when HTF20 strongly against

### W23.  `ZS=ZS4 AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  zscore +1 to +2 overbought; session=off_hours  •  AVOID when HTF20 strongly against

### W24.  `H60=H60e AND T1=T1c AND ZS=ZS4 AND session_bucket=off_hours`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought; session=off_hours  •  AVOID when HTF20 strongly against

### W25.  `H60=H60e AND T4=T4c AND ZS=ZS4 AND session_bucket=off_hours`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought; session=off_hours  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=164  W=60/L=104  WR=36.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=164  W=60/L=104  WR=36.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 60-70 strong

### L02.  `H20=H20a AND BBP=BBP5 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=164  W=60/L=104  WR=36.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=164  W=60/L=104  WR=36.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought

### L03.  `H20=H20a AND T4=T4a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=145  W=54/L=91  WR=37.2%
- Sharpen: sharpest is T1=T1c (22/91 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched upper band; RSI 60-70 strong  •  ONLY when 1h trend AGAINST trade

### L04.  `H20=H20a AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=144  W=55/L=89  WR=38.2%
- Sharpen: sharpest is BBP=BBP4 (44/89 of losers there)
- **Sharp: n=48  W=4/L=44  WR=8.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when upper third

### L05.  `H20=H20a AND H60=H60a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=140  W=54/L=86  WR=38.6%
- Sharpen: sharpest is T4=T4c (13/86 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched upper band; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L06.  `H20=H20a AND BBP=BBP5 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=140  W=54/L=86  WR=38.6%
- Sharpen: sharpest is T4=T4c (13/86 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; just touched upper band; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L07.  `H20=H20a AND T1=T1a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=136  W=54/L=82  WR=39.7%
- Sharpen: sharpest is T4=T4c (13/82 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; just touched upper band; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L08.  `H20=H20a AND H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (37/78 of losers there)
- **Sharp: n=40  W=3/L=37  WR=7.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when upper third

### L09.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (37/78 of losers there)
- **Sharp: n=40  W=3/L=37  WR=7.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when upper third

### L10.  `H20=H20e AND H60=H60a AND T4=T4a`
- Raw: n=119  W=28/L=91  WR=23.5%
- Sharpen: sharpest is session_bucket=ny_close (38/91 of losers there)
- **Sharp: n=38  W=0/L=38  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when session=ny_close

### L11.  `H20=H20e AND T1=T1a AND T4=T4a`
- Raw: n=119  W=28/L=91  WR=23.5%
- Sharpen: sharpest is session_bucket=ny_close (38/91 of losers there)
- **Sharp: n=38  W=0/L=38  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when session=ny_close

### L12.  `H20=H20e AND T4=T4a AND direction_exec=long`
- Raw: n=119  W=28/L=91  WR=23.5%
- Sharpen: sharpest is session_bucket=ny_close (38/91 of losers there)
- **Sharp: n=38  W=0/L=38  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade  •  ONLY when session=ny_close

### L13.  `H20=H20e AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=119  W=28/L=91  WR=23.5%
- Sharpen: sharpest is session_bucket=ny_close (38/91 of losers there)
- **Sharp: n=38  W=0/L=38  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when session=ny_close

### L14.  `H20=H20e AND H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=119  W=28/L=91  WR=23.5%
- Sharpen: sharpest is session_bucket=ny_close (38/91 of losers there)
- **Sharp: n=38  W=0/L=38  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when session=ny_close

### L15.  `H20=H20e AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=119  W=28/L=91  WR=23.5%
- Sharpen: sharpest is session_bucket=ny_close (38/91 of losers there)
- **Sharp: n=38  W=0/L=38  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when session=ny_close

### L16.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=112  W=41/L=71  WR=36.6%
- Sharpen: sharpest is H60=H60a (57/71 of losers there)
- **Sharp: n=78  W=21/L=57  WR=26.9%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L17.  `H20=H20a AND T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=97  W=32/L=65  WR=33.0%
- Sharpen: sharpest is BBP=BBP5 (13/65 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when just touched upper band

### L18.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=97  W=32/L=65  WR=33.0%
- Sharpen: sharpest is BBP=BBP5 (13/65 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when just touched upper band

### L19.  `T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is H60=H60a (42/56 of losers there)
- **Sharp: n=61  W=19/L=42  WR=31.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 aligned WITH trade

### L20.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is H60=H60a (42/56 of losers there)
- **Sharp: n=61  W=19/L=42  WR=31.1%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 aligned WITH trade

### L21.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=92  W=30/L=62  WR=32.6%
- Sharpen: sharpest is BBP=BBP5 (13/62 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when just touched upper band

### L22.  `T1=T1c AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=92  W=36/L=56  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=92  W=36/L=56  WR=39.1%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=ny_open

### L23.  `H20=H20a AND T1=T1c AND T4=T4a AND BBP=BBP4`
- Raw: n=88  W=24/L=64  WR=27.3%
- Sharpen: sharpest is RSI=RSI5 (44/64 of losers there)
- **Sharp: n=48  W=4/L=44  WR=8.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; upper third  •  ONLY when RSI 60-70 strong

### L24.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=86  W=31/L=55  WR=36.0%
- Sharpen: sharpest is BBP=BBP4 (35/55 of losers there)
- **Sharp: n=36  W=1/L=35  WR=2.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong; session=asia  •  ONLY when upper third

### L25.  `H60=H60a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=85  W=30/L=55  WR=35.3%
- Sharpen: sharpest is session_bucket=asia (43/55 of losers there)
- **Sharp: n=57  W=14/L=43  WR=24.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
