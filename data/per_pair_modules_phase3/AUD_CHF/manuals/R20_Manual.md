# AUD_CHF — R20 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,327**  (W=863 / L=464)  -  WR: **65.0%**

## Session distribution

- asia: n=507  W=323/L=184  WR=63.7%
- london_open: n=253  W=174/L=79  WR=68.8%
- ny_mid: n=229  W=150/L=79  WR=65.5%
- ny_open: n=110  W=74/L=36  WR=67.3%
- ny_close: n=92  W=55/L=37  WR=59.8%
- london: n=61  W=37/L=24  WR=60.7%
- asia_late: n=38  W=29/L=9  WR=76.3%
- off_hours: n=37  W=21/L=16  WR=56.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND RSI=RSI4`
- Raw: n=130  W=111/L=19  WR=85.4%
- Refine: exclude H60=H60b drops 6/19 losers (32%)
- **Final: n=124  W=111/L=13  WR=89.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF60 slightly aligned

### W02.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=114  W=101/L=13  WR=88.6%
- Refine: exclude session_bucket=asia drops 9/13 losers (69%)
- **Final: n=67  W=63/L=4  WR=94.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W03.  `H20=H20a AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=109  W=93/L=16  WR=85.3%
- Refine: exclude H60=H60b drops 6/16 losers (38%)
- **Final: n=103  W=93/L=10  WR=90.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF60 slightly aligned

### W04.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI4`
- Raw: n=103  W=93/L=10  WR=90.3%
- Refine: exclude ZS=ZS2 drops 3/10 losers (30%)
- **Final: n=100  W=93/L=7  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore -2 to -1 oversold

### W05.  `H20=H20a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude ZS=ZS4 drops 9/11 losers (82%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore +1 to +2 overbought

### W06.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude ZS=ZS4 drops 6/8 losers (75%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore +1 to +2 overbought

### W07.  `H20=H20a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude ZS=ZS4 drops 6/8 losers (75%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore +1 to +2 overbought

### W08.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude ZS=ZS4 drops 9/11 losers (82%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore +1 to +2 overbought

### W09.  `H20=H20c AND T1=T1c AND T4=T4a`
- Raw: n=68  W=61/L=7  WR=89.7%
- Refine: exclude ZS=ZS5 drops 3/7 losers (43%)
- **Final: n=62  W=58/L=4  WR=93.5%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when zscore +2 to +3 deep overbought

### W10.  `H60=H60a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude BBP=BBP5 drops 5/10 losers (50%)
- **Final: n=48  W=43/L=5  WR=89.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when just touched upper band

### W11.  `H60=H60a AND RSI=RSI4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude BBP=BBP5 drops 5/10 losers (50%)
- **Final: n=48  W=43/L=5  WR=89.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when just touched upper band

### W12.  `T1=T1c AND T4=T4a AND BBP=BBP6`
- Raw: n=64  W=55/L=9  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 5/9 losers (56%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; deep above upper band  •  AVOID when session=ny_mid

### W13.  `T1=T1c AND T4=T4a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=63  W=55/L=8  WR=87.3%
- Refine: exclude session_bucket=ny_mid drops 5/8 losers (62%)
- **Final: n=57  W=54/L=3  WR=94.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W14.  `H20=H20a AND H60=H60a AND BBP=BBP6`
- Raw: n=57  W=50/L=7  WR=87.7%
- Refine: exclude session_bucket=ny_mid drops 4/7 losers (57%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep above upper band  •  AVOID when session=ny_mid

### W15.  `H20=H20a AND H60=H60a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=57  W=50/L=7  WR=87.7%
- Refine: exclude session_bucket=ny_mid drops 4/7 losers (57%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep above upper band  •  AVOID when session=ny_mid

### W16.  `H20=H20a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude direction_exec=long drops 8/8 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when long

### W17.  `T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude H60=H60a drops 7/8 losers (88%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W18.  `T4=T4a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude RSI=RSI3 drops 8/8 losers (100%)
- **Final: n=12  W=12/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when RSI 40-50 lower neutral

### W19.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude RSI=RSI3 drops 8/8 losers (100%)
- **Final: n=12  W=12/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold; session=asia  •  AVOID when RSI 40-50 lower neutral

### W20.  `H20=H20c AND H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=55  W=49/L=6  WR=89.1%
- Refine: exclude ZS=ZS5 drops 3/6 losers (50%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when zscore +2 to +3 deep overbought

### W21.  `H20=H20c AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=55  W=49/L=6  WR=89.1%
- Refine: exclude ZS=ZS5 drops 3/6 losers (50%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when zscore +2 to +3 deep overbought

### W22.  `H20=H20a AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude session_bucket=asia drops 7/7 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; upper third  •  AVOID when session=asia

### W23.  `H20=H20a AND T4=T4a AND ZS=ZS5`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude T1=T1c drops 8/8 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when 1h trend AGAINST trade

### W24.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP1`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude session_bucket=asia drops 4/8 losers (50%)
- **Final: n=43  W=39/L=4  WR=90.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; just touched lower band  •  AVOID when session=asia

### W25.  `H20=H20e AND H60=H60e AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude session_bucket=asia drops 5/8 losers (62%)
- **Final: n=42  W=39/L=3  WR=92.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=88  W=32/L=56  WR=36.4%
- Sharpen: sharpest is H20=H20e (44/56 of losers there)
- **Sharp: n=63  W=19/L=44  WR=30.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L02.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=88  W=32/L=56  WR=36.4%
- Sharpen: sharpest is H20=H20e (44/56 of losers there)
- **Sharp: n=63  W=19/L=44  WR=30.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L03.  `H60=H60e AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is ZS=ZS6 (9/55 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore >+3 extreme

### L04.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is ZS=ZS6 (9/55 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore >+3 extreme

### L05.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=85  W=31/L=54  WR=36.5%
- Sharpen: sharpest is H60=H60e (44/54 of losers there)
- **Sharp: n=63  W=19/L=44  WR=30.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L06.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI4`
- Raw: n=73  W=22/L=51  WR=30.1%
- Sharpen: sharpest is session_bucket=asia (20/51 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L07.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is ZS=ZS1 (10/41 of losers there)
- **Sharp: n=11  W=1/L=10  WR=9.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L08.  `H20=H20c AND T1=T1a AND session_bucket=asia`
- Raw: n=57  W=19/L=38  WR=33.3%
- Sharpen: sharpest is BBP=BBP1 (7/38 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; session=asia  •  ONLY when just touched lower band

### L09.  `H20=H20e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=53  W=19/L=34  WR=35.8%
- Sharpen: sharpest is H60=H60e (34/34 of losers there)
- **Sharp: n=45  W=11/L=34  WR=24.4%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF60 strongly against

### L10.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is BBP=BBP6 (14/30 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when deep above upper band

### L11.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=45  W=11/L=34  WR=24.4%
- Sharpen: sharpest is BBP=BBP6 (14/34 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when deep above upper band

### L12.  `H20=H20e AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=45  W=11/L=34  WR=24.4%
- Sharpen: sharpest is BBP=BBP6 (14/34 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when deep above upper band

### L13.  `T4=T4c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=44  W=16/L=28  WR=36.4%
- Sharpen: sharpest is T1=T1a (22/28 of losers there)
- **Sharp: n=30  W=8/L=22  WR=26.7%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  ONLY when 1h trend WITH trade

### L14.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=44  W=16/L=28  WR=36.4%
- Sharpen: sharpest is T1=T1a (22/28 of losers there)
- **Sharp: n=30  W=8/L=22  WR=26.7%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=asia  •  ONLY when 1h trend WITH trade

### L15.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=44  W=17/L=27  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_close (9/27 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L16.  `H20=H20a AND T4=T4a AND BBP=BBP1`
- Raw: n=43  W=17/L=26  WR=39.5%
- Sharpen: sharpest is H60=H60a (26/26 of losers there)
- **Sharp: n=38  W=12/L=26  WR=31.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched lower band  •  ONLY when HTF60 aligned WITH trade

### L17.  `H20=H20a AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=43  W=17/L=26  WR=39.5%
- Sharpen: sharpest is H60=H60a (26/26 of losers there)
- **Sharp: n=38  W=12/L=26  WR=31.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched lower band; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L18.  `H20=H20a AND T4=T4a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=43  W=17/L=26  WR=39.5%
- Sharpen: sharpest is H60=H60a (26/26 of losers there)
- **Sharp: n=38  W=12/L=26  WR=31.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L19.  `H20=H20a AND BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=43  W=17/L=26  WR=39.5%
- Sharpen: sharpest is H60=H60a (26/26 of losers there)
- **Sharp: n=38  W=12/L=26  WR=31.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L20.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=43  W=17/L=26  WR=39.5%
- Sharpen: sharpest is session_bucket=ny_close (8/26 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=ny_close

### L21.  `H20=H20c AND T1=T1a AND T4=T4c`
- Raw: n=42  W=12/L=30  WR=28.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=42  W=12/L=30  WR=28.6%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend AGAINST trade

### L22.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP4`
- Raw: n=41  W=13/L=28  WR=31.7%
- Sharpen: sharpest is session_bucket=ny_close (9/28 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when session=ny_close

### L23.  `H20=H20a AND T4=T4a AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=41  W=15/L=26  WR=36.6%
- Sharpen: sharpest is H60=H60a (26/26 of losers there)
- **Sharp: n=36  W=10/L=26  WR=27.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched lower band; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L24.  `H20=H20e AND H60=H60e AND T1=T1c AND ZS=ZS4`
- Raw: n=40  W=13/L=27  WR=32.5%
- Sharpen: sharpest is session_bucket=ny_close (8/27 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=ny_close

### L25.  `H20=H20a AND H60=H60a AND BBP=BBP1`
- Raw: n=40  W=14/L=26  WR=35.0%
- Sharpen: sharpest is T1=T1a (5/26 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched lower band  •  ONLY when 1h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(52/47) | H60e(45/51) |
| T1 | — | — |
| T4 | T4a(55/47) | T4c(45/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
