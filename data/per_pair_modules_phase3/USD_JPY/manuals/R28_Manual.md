# USD_JPY — R28 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **5,322**  (W=3,374 / L=1,948)  -  WR: **63.4%**

## Session distribution

- asia: n=1850  W=1168/L=682  WR=63.1%
- ny_close: n=978  W=630/L=348  WR=64.4%
- london_open: n=670  W=438/L=232  WR=65.4%
- london: n=596  W=383/L=213  WR=64.3%
- ny_open: n=443  W=265/L=178  WR=59.8%
- asia_late: n=297  W=187/L=110  WR=63.0%
- ny_mid: n=286  W=178/L=108  WR=62.2%
- off_hours: n=202  W=125/L=77  WR=61.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=335  W=291/L=44  WR=86.9%
- Refine: exclude session_bucket=ny_open drops 17/44 losers (39%)
- **Final: n=304  W=277/L=27  WR=91.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=ny_open

### W02.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=190  W=162/L=28  WR=85.3%
- Refine: exclude H20=H20c drops 16/28 losers (57%)
- **Final: n=132  W=120/L=12  WR=90.9%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 neutral

### W03.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=177  W=152/L=25  WR=85.9%
- Refine: exclude BBP=BBP4 drops 18/25 losers (72%)
- **Final: n=82  W=75/L=7  WR=91.5%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when upper third

### W04.  `H20=H20a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=171  W=147/L=24  WR=86.0%
- Refine: exclude BBP=BBP4 drops 15/24 losers (62%)
- **Final: n=111  W=102/L=9  WR=91.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when upper third

### W05.  `H20=H20a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=169  W=145/L=24  WR=85.8%
- Refine: exclude BBP=BBP4 drops 15/24 losers (62%)
- **Final: n=109  W=100/L=9  WR=91.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when upper third

### W06.  `T1=T1a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=164  W=140/L=24  WR=85.4%
- Refine: exclude T4=T4a drops 20/24 losers (83%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when 4h trend WITH trade

### W07.  `BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=161  W=137/L=24  WR=85.1%
- Refine: exclude H20=H20d drops 15/24 losers (62%)
- **Final: n=128  W=119/L=9  WR=93.0%**
- **Dir: LONG**  •  deep above upper band; RSI 50-60 upper neutral  •  AVOID when HTF20 mildly against

### W08.  `T1=T1a AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=149  W=128/L=21  WR=85.9%
- Refine: exclude H20=H20e drops 15/21 losers (71%)
- **Final: n=83  W=77/L=6  WR=92.8%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 strongly against

### W09.  `H20=H20a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=145  W=124/L=21  WR=85.5%
- Refine: exclude H60=H60e drops 6/21 losers (29%)
- **Final: n=132  W=117/L=15  WR=88.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 strongly against

### W10.  `T1=T1a AND T4=T4a AND session_bucket=london`
- Raw: n=137  W=120/L=17  WR=87.6%
- Refine: exclude H60=H60a drops 11/17 losers (65%)
- **Final: n=111  W=105/L=6  WR=94.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london  •  AVOID when HTF60 aligned WITH trade

### W11.  `H60=H60b AND T1=T1a AND RSI=RSI4`
- Raw: n=135  W=116/L=19  WR=85.9%
- Refine: exclude H20=H20e drops 14/19 losers (74%)
- **Final: n=109  W=104/L=5  WR=95.4%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W12.  `H60=H60b AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=135  W=116/L=19  WR=85.9%
- Refine: exclude H20=H20e drops 14/19 losers (74%)
- **Final: n=109  W=104/L=5  WR=95.4%**
- **Dir: LONG**  •  HTF60 slightly aligned; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W13.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=132  W=117/L=15  WR=88.6%
- Refine: exclude H60=H60a drops 15/15 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W14.  `H20=H20e AND T4=T4a AND session_bucket=london_open`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude T1=T1c drops 14/19 losers (74%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=london_open  •  AVOID when 1h trend AGAINST trade

### W15.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude T1=T1c drops 14/19 losers (74%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=london_open  •  AVOID when 1h trend AGAINST trade

### W16.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=london_open`
- Raw: n=126  W=108/L=18  WR=85.7%
- Refine: exclude T1=T1c drops 14/18 losers (78%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=london_open  •  AVOID when 1h trend AGAINST trade

### W17.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=london`
- Raw: n=125  W=109/L=16  WR=87.2%
- Refine: exclude T4=T4c drops 14/16 losers (88%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when 4h trend AGAINST trade

### W18.  `H20=H20e AND T4=T4a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=125  W=107/L=18  WR=85.6%
- Refine: exclude T1=T1c drops 15/18 losers (83%)
- **Final: n=55  W=52/L=3  WR=94.5%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W19.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=123  W=117/L=6  WR=95.1%
- Refine: exclude H60=H60e drops 3/6 losers (50%)
- **Final: n=92  W=89/L=3  WR=96.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when HTF60 strongly against

### W20.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=122  W=106/L=16  WR=86.9%
- Refine: exclude BBP=BBP1 drops 8/16 losers (50%)
- **Final: n=100  W=92/L=8  WR=92.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W21.  `T4=T4a AND BBP=BBP2 AND session_bucket=ny_close`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude H20=H20c drops 7/18 losers (39%)
- **Final: n=109  W=98/L=11  WR=89.9%**
- **Dir: ?**  •  4h trend WITH trade; lower third; session=ny_close  •  AVOID when HTF20 neutral

### W22.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=london_open`
- Raw: n=121  W=106/L=15  WR=87.6%
- Refine: exclude BBP=BBP1 drops 8/15 losers (53%)
- **Final: n=99  W=92/L=7  WR=92.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W23.  `H20=H20a AND T1=T1a AND T4=T4a AND ZS=ZS4`
- Raw: n=121  W=105/L=16  WR=86.8%
- Refine: exclude H60=H60a drops 11/16 losers (69%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when HTF60 aligned WITH trade

### W24.  `H20=H20a AND H60=H60a AND session_bucket=ny_open`
- Raw: n=116  W=100/L=16  WR=86.2%
- Refine: exclude T4=T4c drops 12/16 losers (75%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W25.  `H20=H20a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=114  W=101/L=13  WR=88.6%
- Refine: exclude session_bucket=ny_close drops 8/13 losers (62%)
- **Final: n=98  W=93/L=5  WR=94.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=390  W=146/L=244  WR=37.4%
- Sharpen: sharpest is T1=T1c (147/244 of losers there)
- **Sharp: n=212  W=65/L=147  WR=30.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L02.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=370  W=147/L=223  WR=39.7%
- Sharpen: sharpest is H20=H20a (147/223 of losers there)
- **Sharp: n=212  W=65/L=147  WR=30.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L03.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=283  W=103/L=180  WR=36.4%
- Sharpen: sharpest is H60=H60d (37/180 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF60 mildly against

### L04.  `T4=T4c AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=255  W=92/L=163  WR=36.1%
- Sharpen: sharpest is H20=H20c (27/163 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF20 neutral

### L05.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=249  W=85/L=164  WR=34.1%
- Sharpen: sharpest is session_bucket=london (31/164 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london

### L06.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=240  W=94/L=146  WR=39.2%
- Sharpen: sharpest is H60=H60d (40/146 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF60 mildly against

### L07.  `RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=237  W=90/L=147  WR=38.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=237  W=90/L=147  WR=38.0%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=asia

### L08.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=230  W=91/L=139  WR=39.6%
- Sharpen: sharpest is BBP=BBP6 (52/139 of losers there)
- **Sharp: n=69  W=17/L=52  WR=24.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when deep above upper band

### L09.  `H20=H20a AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=218  W=84/L=134  WR=38.5%
- Sharpen: sharpest is T1=T1c (57/134 of losers there)
- **Sharp: n=71  W=14/L=57  WR=19.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when 1h trend AGAINST trade

### L10.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=210  W=81/L=129  WR=38.6%
- Sharpen: sharpest is H20=H20a (57/129 of losers there)
- **Sharp: n=71  W=14/L=57  WR=19.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF20 aligned WITH trade

### L11.  `H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=210  W=82/L=128  WR=39.0%
- Sharpen: sharpest is BBP=BBP6 (31/128 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when deep above upper band

### L12.  `H60=H60e AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=210  W=82/L=128  WR=39.0%
- Sharpen: sharpest is BBP=BBP6 (31/128 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when deep above upper band

### L13.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=192  W=73/L=119  WR=38.0%
- Sharpen: sharpest is H60=H60d (37/119 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF60 mildly against

### L14.  `H20=H20c AND T1=T1c AND T4=T4c`
- Raw: n=161  W=63/L=98  WR=39.1%
- Sharpen: sharpest is RSI=RSI3 (57/98 of losers there)
- **Sharp: n=70  W=13/L=57  WR=18.6%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L15.  `H20=H20c AND T1=T1c AND RSI=RSI3`
- Raw: n=160  W=59/L=101  WR=36.9%
- Sharpen: sharpest is T4=T4c (57/101 of losers there)
- **Sharp: n=70  W=13/L=57  WR=18.6%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L16.  `H20=H20a AND T4=T4c AND BBP=BBP2`
- Raw: n=159  W=60/L=99  WR=37.7%
- Sharpen: sharpest is session_bucket=asia (50/99 of losers there)
- **Sharp: n=68  W=18/L=50  WR=26.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when session=asia

### L17.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=151  W=56/L=95  WR=37.1%
- Sharpen: sharpest is BBP=BBP2 (19/95 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when lower third

### L18.  `H20=H20a AND T4=T4c AND ZS=ZS2`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is session_bucket=asia (49/93 of losers there)
- **Sharp: n=65  W=16/L=49  WR=24.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=asia

### L19.  `H20=H20a AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is session_bucket=asia (49/93 of losers there)
- **Sharp: n=65  W=16/L=49  WR=24.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when session=asia

### L20.  `T4=T4c AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=145  W=56/L=89  WR=38.6%
- Sharpen: sharpest is T1=T1c (56/89 of losers there)
- **Sharp: n=79  W=23/L=56  WR=29.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend AGAINST trade

### L21.  `H60=H60a AND BBP=BBP0 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=145  W=57/L=88  WR=39.3%
- Sharpen: sharpest is T1=T1c (50/88 of losers there)
- **Sharp: n=73  W=23/L=50  WR=31.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral; session=asia  •  ONLY when 1h trend AGAINST trade

### L22.  `H20=H20a AND T1=T1c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=144  W=57/L=87  WR=39.6%
- Sharpen: sharpest is T4=T4c (43/87 of losers there)
- **Sharp: n=56  W=13/L=43  WR=23.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L23.  `H20=H20a AND T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=143  W=49/L=94  WR=34.3%
- Sharpen: sharpest is session_bucket=asia (50/94 of losers there)
- **Sharp: n=61  W=11/L=50  WR=18.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when session=asia

### L24.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=141  W=54/L=87  WR=38.3%
- Sharpen: sharpest is H60=H60d (22/87 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 mildly against

### L25.  `H20=H20a AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=137  W=50/L=87  WR=36.5%
- Sharpen: sharpest is T1=T1c (48/87 of losers there)
- **Sharp: n=66  W=18/L=48  WR=27.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(55/44) | T1c(45/56) |
| T4 | T4a(57/43) | T4c(43/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
