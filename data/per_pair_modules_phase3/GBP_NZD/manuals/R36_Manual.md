# GBP_NZD — R36 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR1**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,446**  (W=2,684 / L=1,762)  -  WR: **60.4%**

## Session distribution

- asia: n=1497  W=897/L=600  WR=59.9%
- london_open: n=922  W=571/L=351  WR=61.9%
- london: n=479  W=292/L=187  WR=61.0%
- ny_open: n=387  W=239/L=148  WR=61.8%
- ny_close: n=371  W=237/L=134  WR=63.9%
- asia_late: n=345  W=201/L=144  WR=58.3%
- ny_mid: n=233  W=132/L=101  WR=56.7%
- off_hours: n=212  W=115/L=97  WR=54.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=181  W=156/L=25  WR=86.2%
- Refine: exclude H60=H60a drops 19/25 losers (76%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; upper third  •  AVOID when HTF60 aligned WITH trade

### W02.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=174  W=151/L=23  WR=86.8%
- Refine: exclude H60=H60a drops 19/23 losers (83%)
- **Final: n=99  W=95/L=4  WR=96.0%**
- **Dir: LONG**  •  deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF60 aligned WITH trade

### W03.  `H20=H20e AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=170  W=148/L=22  WR=87.1%
- Refine: exclude session_bucket=asia drops 12/22 losers (55%)
- **Final: n=119  W=109/L=10  WR=91.6%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W04.  `T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=155  W=132/L=23  WR=85.2%
- Refine: exclude H60=H60a drops 19/23 losers (83%)
- **Final: n=87  W=83/L=4  WR=95.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band  •  AVOID when HTF60 aligned WITH trade

### W05.  `BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=149  W=135/L=14  WR=90.6%
- Refine: exclude H60=H60a drops 12/14 losers (86%)
- **Final: n=85  W=83/L=2  WR=97.6%**
- **Dir: LONG**  •  deep below lower band; RSI 40-50 lower neutral  •  AVOID when HTF60 aligned WITH trade

### W06.  `T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=146  W=125/L=21  WR=85.6%
- Refine: exclude H60=H60a drops 17/21 losers (81%)
- **Final: n=86  W=82/L=4  WR=95.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band  •  AVOID when HTF60 aligned WITH trade

### W07.  `T1=T1a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=139  W=129/L=10  WR=92.8%
- Refine: exclude H60=H60a drops 9/10 losers (90%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: LONG**  •  1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 aligned WITH trade

### W08.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=135  W=125/L=10  WR=92.6%
- Refine: exclude H60=H60a drops 9/10 losers (90%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 aligned WITH trade

### W09.  `BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=135  W=121/L=14  WR=89.6%
- Refine: exclude H60=H60a drops 12/14 losers (86%)
- **Final: n=71  W=69/L=2  WR=97.2%**
- **Dir: LONG**  •  deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 aligned WITH trade

### W10.  `T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=113  W=99/L=14  WR=87.6%
- Refine: exclude BBP=BBP1 drops 14/14 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W11.  `H20=H20e AND BBP=BBP0 AND direction_exec=long`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude H60=H60a drops 12/16 losers (75%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: LONG**  •  HTF20 strongly against; deep below lower band  •  AVOID when HTF60 aligned WITH trade

### W12.  `T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=111  W=103/L=8  WR=92.8%
- Refine: exclude H20=H20e drops 6/8 losers (75%)
- **Final: n=99  W=97/L=2  WR=98.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W13.  `T4=T4a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude H60=H60a drops 9/9 losers (100%)
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 aligned WITH trade

### W14.  `T4=T4a AND BBP=BBP4 AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=107  W=95/L=12  WR=88.8%
- Refine: exclude H60=H60a drops 8/12 losers (67%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W15.  `T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude RSI=RSI3 drops 15/15 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=london  •  AVOID when RSI 40-50 lower neutral

### W16.  `H20=H20a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude T4=T4c drops 10/15 losers (67%)
- **Final: n=88  W=83/L=5  WR=94.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=london_open  •  AVOID when 4h trend AGAINST trade

### W17.  `H20=H20a AND H60=H60d AND T4=T4a AND direction_exec=short`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude BBP=BBP2 drops 6/14 losers (43%)
- **Final: n=75  W=67/L=8  WR=89.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend WITH trade  •  AVOID when lower third

### W18.  `H60=H60e AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=99  W=87/L=12  WR=87.9%
- Refine: exclude session_bucket=asia drops 7/12 losers (58%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W19.  `H20=H20a AND BBP=BBP4 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude T1=T1c drops 6/13 losers (46%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 40-50 lower neutral; session=asia  •  AVOID when 1h trend AGAINST trade

### W20.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude H20=H20d drops 7/14 losers (50%)
- **Final: n=83  W=76/L=7  WR=91.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when HTF20 mildly against

### W21.  `H20=H20d AND H60=H60c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude session_bucket=asia drops 12/14 losers (86%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 neutral; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=asia

### W22.  `H20=H20a AND H60=H60d AND T1=T1a AND T4=T4a`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude BBP=BBP2 drops 6/13 losers (46%)
- **Final: n=66  W=59/L=7  WR=89.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when lower third

### W23.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=91  W=86/L=5  WR=94.5%
- Refine: exclude H20=H20e drops 5/5 losers (100%)
- **Final: n=80  W=80/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W24.  `H20=H20e AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude H60=H60a drops 11/13 losers (85%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: ?**  •  HTF20 strongly against; deep below lower band; RSI 40-50 lower neutral  •  AVOID when HTF60 aligned WITH trade

### W25.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude H60=H60a drops 3/11 losers (27%)
- **Final: n=81  W=73/L=8  WR=90.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF60 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND BBP=BBP4 AND direction_exec=long`
- Raw: n=271  W=100/L=171  WR=36.9%
- Sharpen: sharpest is RSI=RSI3 (118/171 of losers there)
- **Sharp: n=167  W=49/L=118  WR=29.3%**
- **Dir: LONG**  •  HTF20 strongly against; upper third  •  ONLY when RSI 40-50 lower neutral

### L02.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=254  W=90/L=164  WR=35.4%
- Sharpen: sharpest is RSI=RSI3 (114/164 of losers there)
- **Sharp: n=153  W=39/L=114  WR=25.5%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third  •  ONLY when RSI 40-50 lower neutral

### L03.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=238  W=92/L=146  WR=38.7%
- Sharpen: sharpest is H20=H20e (89/146 of losers there)
- **Sharp: n=123  W=34/L=89  WR=27.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L04.  `T4=T4c AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=229  W=90/L=139  WR=39.3%
- Sharpen: sharpest is H20=H20e (87/139 of losers there)
- **Sharp: n=121  W=34/L=87  WR=28.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L05.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=226  W=76/L=150  WR=33.6%
- Sharpen: sharpest is session_bucket=asia (55/150 of losers there)
- **Sharp: n=69  W=14/L=55  WR=20.3%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L06.  `H20=H20e AND ZS=ZS4 AND direction_exec=long`
- Raw: n=223  W=85/L=138  WR=38.1%
- Sharpen: sharpest is session_bucket=asia (57/138 of losers there)
- **Sharp: n=78  W=21/L=57  WR=26.9%**
- **Dir: LONG**  •  HTF20 strongly against; zscore +1 to +2 overbought  •  ONLY when session=asia

### L07.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=223  W=85/L=138  WR=38.1%
- Sharpen: sharpest is session_bucket=asia (57/138 of losers there)
- **Sharp: n=78  W=21/L=57  WR=26.9%**
- **Dir: LONG**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when session=asia

### L08.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=211  W=82/L=129  WR=38.9%
- Sharpen: sharpest is direction_exec=long (114/129 of losers there)
- **Sharp: n=153  W=39/L=114  WR=25.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  ONLY when long

### L09.  `H20=H20e AND T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=206  W=75/L=131  WR=36.4%
- Sharpen: sharpest is session_bucket=london_open (37/131 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=london_open

### L10.  `H20=H20e AND H60=H60a AND BBP=BBP4`
- Raw: n=201  W=80/L=121  WR=39.8%
- Sharpen: sharpest is T1=T1c (28/121 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; upper third  •  ONLY when 1h trend AGAINST trade

### L11.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=188  W=73/L=115  WR=38.8%
- Sharpen: sharpest is H20=H20e (69/115 of losers there)
- **Sharp: n=101  W=32/L=69  WR=31.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L12.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=182  W=68/L=114  WR=37.4%
- Sharpen: sharpest is BBP=BBP1 (40/114 of losers there)
- **Sharp: n=42  W=2/L=40  WR=4.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when just touched lower band

### L13.  `H20=H20e AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=167  W=49/L=118  WR=29.3%
- Sharpen: sharpest is H60=H60a (44/118 of losers there)
- **Sharp: n=52  W=8/L=44  WR=15.4%**
- **Dir: LONG**  •  HTF20 strongly against; upper third; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L14.  `T4=T4c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=167  W=66/L=101  WR=39.5%
- Sharpen: sharpest is H20=H20e (73/101 of losers there)
- **Sharp: n=107  W=34/L=73  WR=31.8%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; session=asia  •  ONLY when HTF20 strongly against

### L15.  `BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=165  W=63/L=102  WR=38.2%
- Sharpen: sharpest is H20=H20e (71/102 of losers there)
- **Sharp: n=100  W=29/L=71  WR=29.0%**
- **Dir: LONG**  •  upper third; session=asia  •  ONLY when HTF20 strongly against

### L16.  `T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=164  W=62/L=102  WR=37.8%
- Sharpen: sharpest is BBP=BBP1 (35/102 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when just touched lower band

### L17.  `T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=164  W=62/L=102  WR=37.8%
- Sharpen: sharpest is BBP=BBP1 (35/102 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when just touched lower band

### L18.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=164  W=62/L=102  WR=37.8%
- Sharpen: sharpest is BBP=BBP1 (35/102 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when just touched lower band

### L19.  `T4=T4a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=162  W=54/L=108  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (41/108 of losers there)
- **Sharp: n=51  W=10/L=41  WR=19.6%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L20.  `H20=H20e AND H60=H60a AND ZS=ZS4`
- Raw: n=160  W=64/L=96  WR=40.0%
- Sharpen: sharpest is T1=T1c (24/96 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L21.  `H20=H20e AND H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=160  W=64/L=96  WR=40.0%
- Sharpen: sharpest is T1=T1c (24/96 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L22.  `T4=T4c AND BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=149  W=53/L=96  WR=35.6%
- Sharpen: sharpest is H20=H20e (68/96 of losers there)
- **Sharp: n=97  W=29/L=68  WR=29.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; session=asia  •  ONLY when HTF20 strongly against

### L23.  `T1=T1a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: sharpest is RSI=RSI4 (35/90 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: SHORT**  •  1h trend WITH trade; session=asia_late  •  ONLY when RSI 50-60 upper neutral

### L24.  `H20=H20e AND H60=H60a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=146  W=55/L=91  WR=37.7%
- Sharpen: sharpest is RSI=RSI3 (44/91 of losers there)
- **Sharp: n=52  W=8/L=44  WR=15.4%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; upper third  •  ONLY when RSI 40-50 lower neutral

### L25.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=145  W=58/L=87  WR=40.0%
- Sharpen: sharpest is H60=H60a (45/87 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF60 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(34/29) | H20e(29/35) |
| H60 | — | — |
| T1 | T1a(53/48) | T1c(47/52) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
