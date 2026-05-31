# USD_CAD — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,244**  (W=1,441 / L=803)  -  WR: **64.2%**

## Session distribution

- ny_close: n=587  W=382/L=205  WR=65.1%
- ny_mid: n=562  W=364/L=198  WR=64.8%
- asia: n=407  W=263/L=144  WR=64.6%
- london_open: n=231  W=141/L=90  WR=61.0%
- london: n=177  W=113/L=64  WR=63.8%
- off_hours: n=140  W=91/L=49  WR=65.0%
- ny_open: n=124  W=75/L=49  WR=60.5%
- asia_late: n=16  W=12/L=4  WR=75.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T4=T4a AND RSI=RSI6`
- Raw: n=160  W=139/L=21  WR=86.9%
- Refine: exclude session_bucket=ny_mid drops 6/21 losers (29%)
- **Final: n=144  W=129/L=15  WR=89.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W02.  `H20=H20e AND T1=T1a AND RSI=RSI6`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 6/21 losers (29%)
- **Final: n=126  W=111/L=15  WR=88.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W03.  `H20=H20e AND RSI=RSI6 AND direction_exec=long`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 6/21 losers (29%)
- **Final: n=126  W=111/L=15  WR=88.1%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W04.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI6`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 6/21 losers (29%)
- **Final: n=126  W=111/L=15  WR=88.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W05.  `H20=H20e AND T1=T1a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 6/21 losers (29%)
- **Final: n=126  W=111/L=15  WR=88.1%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W06.  `H20=H20e AND T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 6/21 losers (29%)
- **Final: n=126  W=111/L=15  WR=88.1%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W07.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude BBP=BBP4 drops 10/16 losers (62%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_close  •  AVOID when upper third

### W08.  `H60=H60d AND T4=T4c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude session_bucket=asia drops 6/15 losers (40%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when session=asia

### W09.  `H20=H20e AND H60=H60e AND T1=T1a AND RSI=RSI6`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude BBP=BBP4 drops 11/13 losers (85%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when upper third

### W10.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI6`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude BBP=BBP4 drops 11/13 losers (85%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when upper third

### W11.  `H20=H20e AND H60=H60e AND RSI=RSI6 AND direction_exec=long`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude BBP=BBP4 drops 11/13 losers (85%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought  •  AVOID when upper third

### W12.  `H20=H20d AND T1=T1c AND ZS=ZS5`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=london_open drops 9/13 losers (69%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W13.  `H20=H20d AND T4=T4c AND ZS=ZS5`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=london_open drops 9/13 losers (69%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W14.  `H20=H20d AND ZS=ZS5 AND direction_exec=short`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=london_open drops 9/13 losers (69%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: SHORT**  •  HTF20 mildly against; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W15.  `H20=H20d AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=london_open drops 9/13 losers (69%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W16.  `H20=H20d AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=london_open drops 9/13 losers (69%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W17.  `H20=H20d AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=london_open drops 9/13 losers (69%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W18.  `H20=H20d AND T1=T1c AND session_bucket=ny_close`
- Raw: n=87  W=79/L=8  WR=90.8%
- Refine: exclude H60=H60c drops 8/8 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; session=ny_close  •  AVOID when HTF60 neutral

### W19.  `H20=H20d AND T4=T4c AND session_bucket=ny_close`
- Raw: n=87  W=79/L=8  WR=90.8%
- Refine: exclude H60=H60c drops 8/8 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; session=ny_close  •  AVOID when HTF60 neutral

### W20.  `H20=H20d AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=87  W=79/L=8  WR=90.8%
- Refine: exclude H60=H60c drops 8/8 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 mildly against; session=ny_close  •  AVOID when HTF60 neutral

### W21.  `H20=H20d AND T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=87  W=79/L=8  WR=90.8%
- Refine: exclude H60=H60c drops 8/8 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when HTF60 neutral

### W22.  `H20=H20d AND T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=87  W=79/L=8  WR=90.8%
- Refine: exclude H60=H60c drops 8/8 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; session=ny_close  •  AVOID when HTF60 neutral

### W23.  `H20=H20d AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=87  W=79/L=8  WR=90.8%
- Refine: exclude H60=H60c drops 8/8 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend AGAINST trade; session=ny_close  •  AVOID when HTF60 neutral

### W24.  `H20=H20e AND T4=T4a AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude session_bucket=ny_open drops 8/13 losers (62%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=ny_open

### W25.  `T4=T4c AND RSI=RSI5 AND session_bucket=london`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude H60=H60a drops 12/12 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=london  •  AVOID when HTF60 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=99  W=35/L=64  WR=35.4%
- Sharpen: sharpest is ZS=ZS5 (21/64 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_close  •  ONLY when zscore +2 to +3 deep overbought

### L02.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI6`
- Raw: n=78  W=28/L=50  WR=35.9%
- Sharpen: sharpest is BBP=BBP6 (21/50 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when deep above upper band

### L03.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI6`
- Raw: n=78  W=28/L=50  WR=35.9%
- Sharpen: sharpest is BBP=BBP6 (21/50 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when deep above upper band

### L04.  `H20=H20a AND H60=H60a AND RSI=RSI6 AND direction_exec=short`
- Raw: n=78  W=28/L=50  WR=35.9%
- Sharpen: sharpest is BBP=BBP6 (21/50 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 70-80 overbought  •  ONLY when deep above upper band

### L05.  `H20=H20a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is H60=H60a (33/45 of losers there)
- **Sharp: n=42  W=9/L=33  WR=21.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L06.  `T4=T4a AND RSI=RSI5 AND session_bucket=london`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is H20=H20a (24/45 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=london  •  ONLY when HTF20 aligned WITH trade

### L07.  `H60=H60a AND T1=T1a AND session_bucket=ny_close`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is H20=H20b (24/44 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_close  •  ONLY when HTF20 slightly aligned

### L08.  `H60=H60a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is H20=H20b (24/44 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_close  •  ONLY when HTF20 slightly aligned

### L09.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is H20=H20b (24/44 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when HTF20 slightly aligned

### L10.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is H20=H20b (24/44 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_close  •  ONLY when HTF20 slightly aligned

### L11.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is H20=H20b (24/44 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when HTF20 slightly aligned

### L12.  `H20=H20b AND T1=T1a AND session_bucket=ny_close`
- Raw: n=67  W=22/L=45  WR=32.8%
- Sharpen: sharpest is H60=H60a (24/45 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L13.  `H20=H20b AND T4=T4a AND session_bucket=ny_close`
- Raw: n=67  W=22/L=45  WR=32.8%
- Sharpen: sharpest is H60=H60a (24/45 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L14.  `H20=H20b AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=67  W=22/L=45  WR=32.8%
- Sharpen: sharpest is H60=H60a (24/45 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L15.  `H20=H20b AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=67  W=22/L=45  WR=32.8%
- Sharpen: sharpest is H60=H60a (24/45 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L16.  `H20=H20b AND T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=67  W=22/L=45  WR=32.8%
- Sharpen: sharpest is H60=H60a (24/45 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L17.  `H20=H20b AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=67  W=22/L=45  WR=32.8%
- Sharpen: sharpest is H60=H60a (24/45 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L18.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=61  W=18/L=43  WR=29.5%
- Sharpen: sharpest is H20=H20b (24/43 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_close  •  ONLY when HTF20 slightly aligned

### L19.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=61  W=18/L=43  WR=29.5%
- Sharpen: sharpest is H20=H20b (24/43 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_close  •  ONLY when HTF20 slightly aligned

### L20.  `H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=59  W=19/L=40  WR=32.2%
- Sharpen: sharpest is BBP=BBP5 (7/40 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when just touched upper band

### L21.  `T1=T1c AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=58  W=22/L=36  WR=37.9%
- Sharpen: sharpest is H60=H60a (35/36 of losers there)
- **Sharp: n=35  W=0/L=35  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=off_hours  •  ONLY when HTF60 aligned WITH trade

### L22.  `H20=H20a AND T1=T1c AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=57  W=22/L=35  WR=38.6%
- Sharpen: sharpest is H60=H60a (33/35 of losers there)
- **Sharp: n=42  W=9/L=33  WR=21.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L23.  `H20=H20a AND T4=T4c AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=57  W=22/L=35  WR=38.6%
- Sharpen: sharpest is H60=H60a (33/35 of losers there)
- **Sharp: n=42  W=9/L=33  WR=21.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L24.  `H20=H20a AND RSI=RSI6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=57  W=22/L=35  WR=38.6%
- Sharpen: sharpest is H60=H60a (33/35 of losers there)
- **Sharp: n=42  W=9/L=33  WR=21.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L25.  `H60=H60a AND ZS=ZS5 AND session_bucket=ny_close`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is RSI=RSI5 (33/33 of losers there)
- **Sharp: n=39  W=6/L=33  WR=15.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_close  •  ONLY when RSI 60-70 strong

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20d(17/8), H20e(37/32) | H20b(9/16), H20a(32/39) |
| H60 | — | H60a(32/39) |
| T1 | — | — |
| T4 | T4c(54/48) | T4a(46/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
