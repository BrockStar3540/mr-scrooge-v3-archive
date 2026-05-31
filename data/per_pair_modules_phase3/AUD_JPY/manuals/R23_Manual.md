# AUD_JPY — R23 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR1**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,563**  (W=1,612 / L=951)  -  WR: **62.9%**

## Session distribution

- asia: n=878  W=548/L=330  WR=62.4%
- ny_close: n=400  W=256/L=144  WR=64.0%
- london_open: n=331  W=201/L=130  WR=60.7%
- ny_open: n=278  W=180/L=98  WR=64.7%
- ny_mid: n=229  W=139/L=90  WR=60.7%
- asia_late: n=212  W=138/L=74  WR=65.1%
- london: n=189  W=120/L=69  WR=63.5%
- off_hours: n=46  W=30/L=16  WR=65.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=151  W=131/L=20  WR=86.8%
- Refine: exclude ZS=ZS3 drops 6/20 losers (30%)
- **Final: n=129  W=115/L=14  WR=89.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W02.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=110  W=96/L=14  WR=87.3%
- Refine: exclude T1=T1c drops 5/14 losers (36%)
- **Final: n=88  W=79/L=9  WR=89.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend AGAINST trade

### W03.  `H60=H60a AND T1=T1a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude RSI=RSI4 drops 11/12 losers (92%)
- **Final: n=25  W=24/L=1  WR=96.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when RSI 50-60 upper neutral

### W04.  `T1=T1a AND ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude RSI=RSI4 drops 11/12 losers (92%)
- **Final: n=25  W=24/L=1  WR=96.0%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when RSI 50-60 upper neutral

### W05.  `H20=H20a AND T1=T1a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=95  W=84/L=11  WR=88.4%
- Refine: exclude RSI=RSI4 drops 10/11 losers (91%)
- **Final: n=25  W=24/L=1  WR=96.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when RSI 50-60 upper neutral

### W06.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude BBP=BBP5 drops 8/12 losers (67%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W07.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=83  W=73/L=10  WR=88.0%
- Refine: exclude BBP=BBP5 drops 5/10 losers (50%)
- **Final: n=60  W=55/L=5  WR=91.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=asia  •  AVOID when just touched upper band

### W08.  `T1=T1a AND T4=T4c AND BBP=BBP6`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude H60=H60a drops 10/11 losers (91%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; deep above upper band  •  AVOID when HTF60 aligned WITH trade

### W09.  `H20=H20a AND T1=T1a AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude RSI=RSI4 drops 10/11 losers (91%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep above upper band; session=asia  •  AVOID when RSI 50-60 upper neutral

### W10.  `H60=H60a AND T1=T1a AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude RSI=RSI4 drops 10/11 losers (91%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band; session=asia  •  AVOID when RSI 50-60 upper neutral

### W11.  `T1=T1a AND BBP=BBP6 AND direction_exec=long AND session_bucket=asia`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude RSI=RSI4 drops 10/11 losers (91%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band; session=asia  •  AVOID when RSI 50-60 upper neutral

### W12.  `H20=H20a AND T1=T1a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude RSI=RSI4 drops 9/10 losers (90%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI 50-60 upper neutral

### W13.  `T4=T4c AND BBP=BBP6 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude ZS=ZS6 drops 3/8 losers (38%)
- **Final: n=60  W=55/L=5  WR=91.7%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore >+3 extreme

### W14.  `H60=H60e AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude RSI=RSI3 drops 5/8 losers (62%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W15.  `ZS=ZS4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude RSI=RSI3 drops 5/8 losers (62%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: SHORT**  •  zscore +1 to +2 overbought; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W16.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude RSI=RSI3 drops 5/8 losers (62%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W17.  `H60=H60e AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude RSI=RSI3 drops 5/8 losers (62%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W18.  `T1=T1a AND T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude H60=H60a drops 7/8 losers (88%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W19.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude RSI=RSI3 drops 5/8 losers (62%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: SHORT**  •  upper third; zscore +1 to +2 overbought; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W20.  `H20=H20a AND T4=T4c AND ZS=ZS5`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude strategy_id=alpha_breakout_retest_v2 drops 2/7 losers (29%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when strategy=alpha_breakout_retest_v2

### W21.  `T1=T1a AND T4=T4c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude H20=H20a drops 7/7 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W22.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=67  W=60/L=7  WR=89.6%
- Refine: exclude BBP=BBP5 drops 5/7 losers (71%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when just touched upper band

### W23.  `T1=T1a AND T4=T4c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude strategy_id=alpha_breakout_retest_v2 drops 2/7 losers (29%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when strategy=alpha_breakout_retest_v2

### W24.  `H20=H20a AND T1=T1a AND T4=T4c AND BBP=BBP4`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude session_bucket=ny_open drops 4/7 losers (57%)
- **Final: n=54  W=51/L=3  WR=94.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when session=ny_open

### W25.  `H20=H20a AND H60=H60a AND T4=T4c AND ZS=ZS5`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude strategy_id=alpha_breakout_retest_v2 drops 2/7 losers (29%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when strategy=alpha_breakout_retest_v2

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=123  W=47/L=76  WR=38.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral

### L02.  `H20=H20e AND T1=T1c AND ZS=ZS5`
- Raw: n=95  W=35/L=60  WR=36.8%
- Sharpen: sharpest is session_bucket=london_open (19/60 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L03.  `H60=H60e AND T1=T1c AND ZS=ZS5`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is session_bucket=london_open (19/58 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L04.  `T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is session_bucket=london_open (19/58 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L05.  `H60=H60e AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is session_bucket=london_open (19/58 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L06.  `H20=H20e AND H60=H60e AND T1=T1c AND ZS=ZS5`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is session_bucket=london_open (19/57 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L07.  `H20=H20e AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is session_bucket=london_open (19/57 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L08.  `T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=87  W=29/L=58  WR=33.3%
- Sharpen: sharpest is ZS=ZS5 (19/58 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (45/51 of losers there)
- **Sharp: n=69  W=24/L=45  WR=34.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; session=asia  •  ONLY when RSI 50-60 upper neutral

### L10.  `T1=T1c AND BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (45/51 of losers there)
- **Sharp: n=69  W=24/L=45  WR=34.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; session=asia  •  ONLY when RSI 50-60 upper neutral

### L11.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=79  W=31/L=48  WR=39.2%
- Sharpen: sharpest is session_bucket=london_open (19/48 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L12.  `T1=T1c AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=79  W=31/L=48  WR=39.2%
- Sharpen: sharpest is session_bucket=london_open (19/48 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L13.  `H60=H60e AND T1=T1c AND BBP=BBP0`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is RSI=RSI4 (23/47 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep below lower band  •  ONLY when RSI 50-60 upper neutral

### L14.  `T1=T1c AND BBP=BBP0 AND direction_exec=short`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is RSI=RSI4 (23/47 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep below lower band  •  ONLY when RSI 50-60 upper neutral

### L15.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is session_bucket=london_open (19/47 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L16.  `H60=H60e AND T1=T1c AND BBP=BBP0 AND direction_exec=short`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is RSI=RSI4 (23/47 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; deep below lower band  •  ONLY when RSI 50-60 upper neutral

### L17.  `H60=H60e AND T1=T1c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=75  W=30/L=45  WR=40.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought; session=asia

### L18.  `T1=T1c AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=75  W=30/L=45  WR=40.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=asia

### L19.  `T1=T1c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is H60=H60e (29/42 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF60 strongly against

### L20.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is ZS=ZS5 (19/40 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L21.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is session_bucket=london_open (19/40 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L22.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is ZS=ZS5 (19/40 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is session_bucket=london_open (19/40 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L24.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is ZS=ZS5 (19/40 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=65  W=26/L=39  WR=40.0%
- Sharpen: sharpest is session_bucket=london_open (19/39 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(49/39) | H20e(40/48) |
| H60 | H60a(53/47) | H60e(47/53) |
| T1 | T1a(58/42) | T1c(42/58) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/47) | short(47/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
