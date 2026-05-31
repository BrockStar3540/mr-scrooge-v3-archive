# USD_JPY — R22 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,765**  (W=2,261 / L=1,504)  -  WR: **60.1%**

## Session distribution

- asia: n=1329  W=809/L=520  WR=60.9%
- london_open: n=709  W=424/L=285  WR=59.8%
- ny_mid: n=602  W=366/L=236  WR=60.8%
- ny_open: n=534  W=288/L=246  WR=53.9%
- ny_close: n=217  W=136/L=81  WR=62.7%
- london: n=200  W=128/L=72  WR=64.0%
- asia_late: n=141  W=88/L=53  WR=62.4%
- off_hours: n=33  W=22/L=11  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=240  W=206/L=34  WR=85.8%
- Refine: exclude ZS=ZS1 drops 9/34 losers (26%)
- **Final: n=227  W=202/L=25  WR=89.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -3 to -2 deep oversold

### W02.  `H60=H60a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=201  W=173/L=28  WR=86.1%
- Refine: exclude ZS=ZS1 drops 9/28 losers (32%)
- **Final: n=188  W=169/L=19  WR=89.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -3 to -2 deep oversold

### W03.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=201  W=173/L=28  WR=86.1%
- Refine: exclude ZS=ZS1 drops 9/28 losers (32%)
- **Final: n=188  W=169/L=19  WR=89.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -3 to -2 deep oversold

### W04.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H60=H60e drops 13/14 losers (93%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF60 strongly against

### W05.  `RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=83  W=73/L=10  WR=88.0%
- Refine: exclude H20=H20a drops 5/10 losers (50%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W06.  `H20=H20a AND T1=T1a AND RSI=RSI0`
- Raw: n=76  W=68/L=8  WR=89.5%
- Refine: exclude strategy_id=BR3_inside_bar_short drops 2/8 losers (25%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI<20 extreme oversold  •  AVOID when strategy=BR3_inside_bar_short

### W07.  `H20=H20a AND T4=T4a AND RSI=RSI0`
- Raw: n=76  W=68/L=8  WR=89.5%
- Refine: exclude strategy_id=BR3_inside_bar_short drops 2/8 losers (25%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI<20 extreme oversold  •  AVOID when strategy=BR3_inside_bar_short

### W08.  `H20=H20a AND RSI=RSI0 AND direction_exec=short`
- Raw: n=76  W=68/L=8  WR=89.5%
- Refine: exclude strategy_id=BR3_inside_bar_short drops 2/8 losers (25%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI<20 extreme oversold  •  AVOID when strategy=BR3_inside_bar_short

### W09.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI0`
- Raw: n=76  W=68/L=8  WR=89.5%
- Refine: exclude strategy_id=BR3_inside_bar_short drops 2/8 losers (25%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI<20 extreme oversold  •  AVOID when strategy=BR3_inside_bar_short

### W10.  `H20=H20a AND T1=T1a AND RSI=RSI0 AND direction_exec=short`
- Raw: n=76  W=68/L=8  WR=89.5%
- Refine: exclude strategy_id=BR3_inside_bar_short drops 2/8 losers (25%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI<20 extreme oversold  •  AVOID when strategy=BR3_inside_bar_short

### W11.  `H20=H20a AND T4=T4a AND RSI=RSI0 AND direction_exec=short`
- Raw: n=76  W=68/L=8  WR=89.5%
- Refine: exclude strategy_id=BR3_inside_bar_short drops 2/8 losers (25%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI<20 extreme oversold  •  AVOID when strategy=BR3_inside_bar_short

### W12.  `H20=H20a AND T4=T4c AND RSI=RSI3`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W13.  `H20=H20a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W14.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI3`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W15.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W16.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W17.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W18.  `H20=H20a AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W19.  `H60=H60a AND T1=T1a AND session_bucket=asia`
- Raw: n=75  W=68/L=7  WR=90.7%
- Refine: exclude RSI=RSI0 drops 7/7 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when RSI<20 extreme oversold

### W20.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=asia`
- Raw: n=75  W=68/L=7  WR=90.7%
- Refine: exclude RSI=RSI0 drops 7/7 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when RSI<20 extreme oversold

### W21.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=75  W=68/L=7  WR=90.7%
- Refine: exclude RSI=RSI0 drops 7/7 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI<20 extreme oversold

### W22.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=75  W=68/L=7  WR=90.7%
- Refine: exclude RSI=RSI0 drops 7/7 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when RSI<20 extreme oversold

### W23.  `T4=T4c AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude H20=H20a drops 5/11 losers (45%)
- **Final: n=55  W=49/L=6  WR=89.1%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W24.  `T4=T4c AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude H20=H20a drops 5/10 losers (50%)
- **Final: n=54  W=49/L=5  WR=90.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W25.  `T1=T1c AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude H20=H20a drops 5/9 losers (56%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=200  W=69/L=131  WR=34.5%
- Sharpen: sharpest is session_bucket=ny_mid (38/131 of losers there)
- **Sharp: n=46  W=8/L=38  WR=17.4%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L02.  `T1=T1c AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=169  W=60/L=109  WR=35.5%
- Sharpen: sharpest is T4=T4c (53/109 of losers there)
- **Sharp: n=67  W=14/L=53  WR=20.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  ONLY when 4h trend AGAINST trade

### L03.  `RSI=RSI2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=167  W=53/L=114  WR=31.7%
- Sharpen: sharpest is H20=H20e (59/114 of losers there)
- **Sharp: n=71  W=12/L=59  WR=16.9%**
- **Dir: LONG**  •  RSI 30-40 weak; session=london_open  •  ONLY when HTF20 strongly against

### L04.  `T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=166  W=51/L=115  WR=30.7%
- Sharpen: sharpest is session_bucket=ny_mid (38/115 of losers there)
- **Sharp: n=46  W=8/L=38  WR=17.4%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L05.  `T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=160  W=51/L=109  WR=31.9%
- Sharpen: sharpest is session_bucket=ny_mid (38/109 of losers there)
- **Sharp: n=46  W=8/L=38  WR=17.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L06.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=160  W=51/L=109  WR=31.9%
- Sharpen: sharpest is session_bucket=ny_mid (38/109 of losers there)
- **Sharp: n=46  W=8/L=38  WR=17.4%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L07.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=160  W=51/L=109  WR=31.9%
- Sharpen: sharpest is H20=H20e (59/109 of losers there)
- **Sharp: n=71  W=12/L=59  WR=16.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  ONLY when HTF20 strongly against

### L08.  `T1=T1c AND T4=T4c AND RSI=RSI0`
- Raw: n=148  W=51/L=97  WR=34.5%
- Sharpen: sharpest is ZS=ZS2 (61/97 of losers there)
- **Sharp: n=78  W=17/L=61  WR=21.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when zscore -2 to -1 oversold

### L09.  `T1=T1c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=148  W=51/L=97  WR=34.5%
- Sharpen: sharpest is ZS=ZS2 (61/97 of losers there)
- **Sharp: n=78  W=17/L=61  WR=21.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when zscore -2 to -1 oversold

### L10.  `T4=T4c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=148  W=51/L=97  WR=34.5%
- Sharpen: sharpest is ZS=ZS2 (61/97 of losers there)
- **Sharp: n=78  W=17/L=61  WR=21.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when zscore -2 to -1 oversold

### L11.  `T1=T1c AND T4=T4c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=148  W=51/L=97  WR=34.5%
- Sharpen: sharpest is ZS=ZS2 (61/97 of losers there)
- **Sharp: n=78  W=17/L=61  WR=21.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when zscore -2 to -1 oversold

### L12.  `H60=H60e AND RSI=RSI3 AND direction_exec=short`
- Raw: n=140  W=39/L=101  WR=27.9%
- Sharpen: sharpest is session_bucket=ny_mid (37/101 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L13.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=140  W=39/L=101  WR=27.9%
- Sharpen: sharpest is session_bucket=ny_mid (37/101 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L14.  `H60=H60e AND T4=T4a AND RSI=RSI3`
- Raw: n=134  W=39/L=95  WR=29.1%
- Sharpen: sharpest is session_bucket=ny_mid (37/95 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L15.  `H60=H60e AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=134  W=39/L=95  WR=29.1%
- Sharpen: sharpest is session_bucket=ny_mid (37/95 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L16.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=134  W=39/L=95  WR=29.1%
- Sharpen: sharpest is session_bucket=ny_mid (37/95 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L17.  `T1=T1c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=128  W=45/L=83  WR=35.2%
- Sharpen: sharpest is BBP=BBP0 (42/83 of losers there)
- **Sharp: n=45  W=3/L=42  WR=6.7%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when deep below lower band

### L18.  `H20=H20a AND T4=T4a AND RSI=RSI3`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: sharpest is H60=H60e (38/73 of losers there)
- **Sharp: n=54  W=16/L=38  WR=29.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L19.  `H20=H20a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: sharpest is H60=H60e (38/73 of losers there)
- **Sharp: n=54  W=16/L=38  WR=29.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L20.  `H20=H20a AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: sharpest is H60=H60e (38/73 of losers there)
- **Sharp: n=54  W=16/L=38  WR=29.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L21.  `T1=T1c AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=118  W=44/L=74  WR=37.3%
- Sharpen: sharpest is BBP=BBP0 (33/74 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when deep below lower band

### L22.  `H20=H20e AND T1=T1c AND session_bucket=london_open`
- Raw: n=107  W=41/L=66  WR=38.3%
- Sharpen: sharpest is RSI=RSI2 (59/66 of losers there)
- **Sharp: n=80  W=21/L=59  WR=26.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 30-40 weak

### L23.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=104  W=40/L=64  WR=38.5%
- Sharpen: sharpest is direction_exec=long (28/64 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third; session=asia  •  ONLY when long

### L24.  `RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=100  W=37/L=63  WR=37.0%
- Sharpen: sharpest is BBP=BBP4 (24/63 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=asia  •  ONLY when upper third

### L25.  `H60=H60e AND T4=T4a AND BBP=BBP0`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=100  W=39/L=61  WR=39.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; deep below lower band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4c(53/47) | T4a(47/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
