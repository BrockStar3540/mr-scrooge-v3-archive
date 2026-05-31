# AUD_USD — R24 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,377**  (W=1,444 / L=933)  -  WR: **60.7%**

## Session distribution

- asia: n=622  W=393/L=229  WR=63.2%
- ny_mid: n=531  W=293/L=238  WR=55.2%
- ny_close: n=386  W=236/L=150  WR=61.1%
- ny_open: n=282  W=169/L=113  WR=59.9%
- london: n=226  W=146/L=80  WR=64.6%
- london_open: n=209  W=126/L=83  WR=60.3%
- asia_late: n=82  W=57/L=25  WR=69.5%
- off_hours: n=39  W=24/L=15  WR=61.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=104  W=94/L=10  WR=90.4%
- Refine: exclude ZS=ZS0 drops 6/10 losers (60%)
- **Final: n=88  W=84/L=4  WR=95.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=asia  •  AVOID when zscore <-3 extreme

### W02.  `RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=104  W=94/L=10  WR=90.4%
- Refine: exclude ZS=ZS0 drops 6/10 losers (60%)
- **Final: n=88  W=84/L=4  WR=95.5%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=asia  •  AVOID when zscore <-3 extreme

### W03.  `H60=H60e AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=104  W=94/L=10  WR=90.4%
- Refine: exclude ZS=ZS0 drops 6/10 losers (60%)
- **Final: n=88  W=84/L=4  WR=95.5%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=asia  •  AVOID when zscore <-3 extreme

### W04.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude T4=T4c drops 14/15 losers (93%)
- **Final: n=34  W=33/L=1  WR=97.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W05.  `H20=H20e AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude T4=T4c drops 14/15 losers (93%)
- **Final: n=34  W=33/L=1  WR=97.1%**
- **Dir: SHORT**  •  HTF20 strongly against; lower third; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W06.  `H60=H60e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 strongly against

### W07.  `T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_open  •  AVOID when HTF20 strongly against

### W08.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 strongly against

### W09.  `T1=T1c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude T4=T4c drops 4/12 losers (33%)
- **Final: n=75  W=67/L=8  WR=89.3%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  AVOID when 4h trend AGAINST trade

### W10.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude T4=T4c drops 4/12 losers (33%)
- **Final: n=75  W=67/L=8  WR=89.3%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when 4h trend AGAINST trade

### W11.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude T4=T4c drops 4/12 losers (33%)
- **Final: n=75  W=67/L=8  WR=89.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when 4h trend AGAINST trade

### W12.  `H20=H20b AND T4=T4a AND RSI=RSI4`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude session_bucket=ny_mid drops 7/12 losers (58%)
- **Final: n=80  W=75/L=5  WR=93.8%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W13.  `T1=T1a AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude session_bucket=ny_mid drops 3/12 losers (25%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W14.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude H20=H20d drops 6/12 losers (50%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when HTF20 mildly against

### W15.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude H20=H20d drops 6/12 losers (50%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: SHORT**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when HTF20 mildly against

### W16.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude session_bucket=ny_mid drops 3/11 losers (27%)
- **Final: n=77  W=69/L=8  WR=89.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W17.  `T1=T1a AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude session_bucket=ny_mid drops 3/11 losers (27%)
- **Final: n=77  W=69/L=8  WR=89.6%**
- **Dir: LONG**  •  1h trend WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W18.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude H20=H20d drops 5/10 losers (50%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third; session=asia  •  AVOID when HTF20 mildly against

### W19.  `H20=H20e AND H60=H60e AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=ny_open drops 4/10 losers (40%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W20.  `H20=H20e AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=ny_open drops 4/10 losers (40%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W21.  `T1=T1c AND T4=T4a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude H20=H20a drops 4/8 losers (50%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 aligned WITH trade

### W22.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude session_bucket=ny_open drops 4/11 losers (36%)
- **Final: n=68  W=61/L=7  WR=89.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W23.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude session_bucket=ny_open drops 4/11 losers (36%)
- **Final: n=68  W=61/L=7  WR=89.7%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W24.  `T1=T1a AND T4=T4c AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude session_bucket=asia drops 7/9 losers (78%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third; RSI 50-60 upper neutral  •  AVOID when session=asia

### W25.  `H60=H60a AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude session_bucket=asia drops 6/8 losers (75%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=249  W=97/L=152  WR=39.0%
- Sharpen: sharpest is T4=T4a (120/152 of losers there)
- **Sharp: n=173  W=53/L=120  WR=30.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_mid  •  ONLY when 4h trend WITH trade

### L02.  `H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=193  W=70/L=123  WR=36.3%
- Sharpen: sharpest is ZS=ZS0 (19/123 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore <-3 extreme

### L03.  `T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=193  W=70/L=123  WR=36.3%
- Sharpen: sharpest is ZS=ZS0 (19/123 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore <-3 extreme

### L04.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=193  W=70/L=123  WR=36.3%
- Sharpen: sharpest is ZS=ZS0 (19/123 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore <-3 extreme

### L05.  `T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=189  W=62/L=127  WR=32.8%
- Sharpen: sharpest is ZS=ZS5 (28/127 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `H60=H60a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=173  W=53/L=120  WR=30.6%
- Sharpen: sharpest is BBP=BBP0 (41/120 of losers there)
- **Sharp: n=50  W=9/L=41  WR=18.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when deep below lower band

### L07.  `T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=173  W=53/L=120  WR=30.6%
- Sharpen: sharpest is BBP=BBP0 (41/120 of losers there)
- **Sharp: n=50  W=9/L=41  WR=18.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_mid  •  ONLY when deep below lower band

### L08.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=173  W=53/L=120  WR=30.6%
- Sharpen: sharpest is BBP=BBP0 (41/120 of losers there)
- **Sharp: n=50  W=9/L=41  WR=18.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when deep below lower band

### L09.  `H20=H20a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=171  W=56/L=115  WR=32.7%
- Sharpen: sharpest is BBP=BBP4 (29/115 of losers there)
- **Sharp: n=30  W=1/L=29  WR=3.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when upper third

### L10.  `H20=H20a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=162  W=53/L=109  WR=32.7%
- Sharpen: sharpest is BBP=BBP4 (19/109 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when upper third

### L11.  `H20=H20a AND H60=H60a AND session_bucket=ny_mid`
- Raw: n=161  W=54/L=107  WR=33.5%
- Sharpen: sharpest is BBP=BBP4 (27/107 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_mid  •  ONLY when upper third

### L12.  `H20=H20a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=161  W=54/L=107  WR=33.5%
- Sharpen: sharpest is BBP=BBP4 (27/107 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_mid  •  ONLY when upper third

### L13.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=161  W=54/L=107  WR=33.5%
- Sharpen: sharpest is BBP=BBP4 (27/107 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_mid  •  ONLY when upper third

### L14.  `H60=H60a AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=151  W=49/L=102  WR=32.5%
- Sharpen: sharpest is BBP=BBP0 (40/102 of losers there)
- **Sharp: n=49  W=9/L=40  WR=18.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when deep below lower band

### L15.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=151  W=49/L=102  WR=32.5%
- Sharpen: sharpest is BBP=BBP0 (40/102 of losers there)
- **Sharp: n=49  W=9/L=40  WR=18.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when deep below lower band

### L16.  `H60=H60a AND T4=T4a AND RSI=RSI3`
- Raw: n=145  W=53/L=92  WR=36.6%
- Sharpen: sharpest is session_bucket=asia (19/92 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L17.  `T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=145  W=53/L=92  WR=36.6%
- Sharpen: sharpest is session_bucket=asia (19/92 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L18.  `H60=H60a AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=145  W=53/L=92  WR=36.6%
- Sharpen: sharpest is session_bucket=asia (19/92 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L19.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=145  W=53/L=92  WR=36.6%
- Sharpen: sharpest is session_bucket=asia (19/92 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L20.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=145  W=53/L=92  WR=36.6%
- Sharpen: sharpest is session_bucket=asia (19/92 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L21.  `H20=H20a AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=142  W=44/L=98  WR=31.0%
- Sharpen: sharpest is BBP=BBP0 (40/98 of losers there)
- **Sharp: n=49  W=9/L=40  WR=18.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when deep below lower band

### L22.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=138  W=45/L=93  WR=32.6%
- Sharpen: sharpest is BBP=BBP4 (15/93 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when upper third

### L23.  `H20=H20a AND T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=138  W=45/L=93  WR=32.6%
- Sharpen: sharpest is BBP=BBP4 (15/93 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when upper third

### L24.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI3`
- Raw: n=133  W=49/L=84  WR=36.8%
- Sharpen: sharpest is session_bucket=asia (19/84 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L25.  `H20=H20a AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=133  W=49/L=84  WR=36.8%
- Sharpen: sharpest is session_bucket=asia (19/84 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(18/12) | — |
| H60 | H60e(54/44) | H60a(46/56) |
| T1 | T1a(54/48) | T1c(46/52) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/44) | long(46/56) |
| session_bucket | — | ny_mid(20/26) |

*Read: `bucket(winner%/loser%)`.*
