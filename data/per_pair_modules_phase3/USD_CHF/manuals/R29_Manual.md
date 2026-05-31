# USD_CHF — R29 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,088**  (W=703 / L=385)  -  WR: **64.6%**

## Session distribution

- ny_open: n=213  W=138/L=75  WR=64.8%
- ny_mid: n=200  W=120/L=80  WR=60.0%
- london_open: n=195  W=131/L=64  WR=67.2%
- london: n=169  W=111/L=58  WR=65.7%
- ny_close: n=163  W=107/L=56  WR=65.6%
- asia: n=120  W=78/L=42  WR=65.0%
- off_hours: n=18  W=10/L=8  WR=55.6%
- asia_late: n=10  W=8/L=2  WR=80.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=223  W=199/L=24  WR=89.2%
- Refine: exclude H20=H20d drops 14/24 losers (58%)
- **Final: n=178  W=168/L=10  WR=94.4%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak  •  AVOID when HTF20 mildly against

### W02.  `T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=171  W=150/L=21  WR=87.7%
- Refine: exclude H60=H60e drops 11/21 losers (52%)
- **Final: n=147  W=137/L=10  WR=93.2%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak  •  AVOID when HTF60 strongly against

### W03.  `H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=157  W=149/L=8  WR=94.9%
- Refine: exclude RSI=RSI3 drops 8/8 losers (100%)
- **Final: n=89  W=89/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when RSI 40-50 lower neutral

### W04.  `T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=152  W=138/L=14  WR=90.8%
- Refine: exclude H20=H20d drops 8/14 losers (57%)
- **Final: n=144  W=138/L=6  WR=95.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when HTF20 mildly against

### W05.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=152  W=138/L=14  WR=90.8%
- Refine: exclude H20=H20d drops 8/14 losers (57%)
- **Final: n=144  W=138/L=6  WR=95.8%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when HTF20 mildly against

### W06.  `H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=134  W=131/L=3  WR=97.8%
- Refine: exclude RSI=RSI3 drops 3/3 losers (100%)
- **Final: n=89  W=89/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when RSI 40-50 lower neutral

### W07.  `H60=H60a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=134  W=131/L=3  WR=97.8%
- Refine: exclude RSI=RSI3 drops 3/3 losers (100%)
- **Final: n=89  W=89/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when RSI 40-50 lower neutral

### W08.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=127  W=109/L=18  WR=85.8%
- Refine: exclude session_bucket=ny_close drops 9/18 losers (50%)
- **Final: n=116  W=107/L=9  WR=92.2%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when session=ny_close

### W09.  `H60=H60a AND T1=T1a AND RSI=RSI2`
- Raw: n=121  W=117/L=4  WR=96.7%
- Refine: exclude T4=T4c drops 4/4 losers (100%)
- **Final: n=79  W=79/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when 4h trend AGAINST trade

### W10.  `T1=T1a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=114  W=100/L=14  WR=87.7%
- Refine: exclude H20=H20d drops 7/14 losers (50%)
- **Final: n=98  W=91/L=7  WR=92.9%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 30-40 weak  •  AVOID when HTF20 mildly against

### W11.  `T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude session_bucket=ny_close drops 9/17 losers (53%)
- **Final: n=101  W=93/L=8  WR=92.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W12.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude session_bucket=ny_close drops 9/17 losers (53%)
- **Final: n=101  W=93/L=8  WR=92.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W13.  `H60=H60a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=111  W=107/L=4  WR=96.4%
- Refine: exclude T4=T4c drops 4/4 losers (100%)
- **Final: n=79  W=79/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 30-40 weak  •  AVOID when 4h trend AGAINST trade

### W14.  `H60=H60a AND T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=111  W=107/L=4  WR=96.4%
- Refine: exclude T4=T4c drops 4/4 losers (100%)
- **Final: n=79  W=79/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when 4h trend AGAINST trade

### W15.  `T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=111  W=99/L=12  WR=89.2%
- Refine: exclude H20=H20e drops 7/12 losers (58%)
- **Final: n=81  W=76/L=5  WR=93.8%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_open  •  AVOID when HTF20 strongly against

### W16.  `T1=T1a AND T4=T4a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=110  W=95/L=15  WR=86.4%
- Refine: exclude session_bucket=ny_close drops 7/15 losers (47%)
- **Final: n=101  W=93/L=8  WR=92.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W17.  `T1=T1a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=104  W=92/L=12  WR=88.5%
- Refine: exclude H20=H20d drops 6/12 losers (50%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when HTF20 mildly against

### W18.  `T1=T1a AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=104  W=92/L=12  WR=88.5%
- Refine: exclude H20=H20d drops 6/12 losers (50%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when HTF20 mildly against

### W19.  `T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=101  W=95/L=6  WR=94.1%
- Refine: exclude H60=H60c drops 5/6 losers (83%)
- **Final: n=87  W=86/L=1  WR=98.9%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_open  •  AVOID when HTF60 neutral

### W20.  `T1=T1a AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=101  W=90/L=11  WR=89.1%
- Refine: exclude H20=H20d drops 7/11 losers (64%)
- **Final: n=85  W=81/L=4  WR=95.3%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; RSI 30-40 weak  •  AVOID when HTF20 mildly against

### W21.  `RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude H60=H60e drops 10/15 losers (67%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when HTF60 strongly against

### W22.  `BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude H60=H60e drops 10/15 losers (67%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: SHORT**  •  lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when HTF60 strongly against

### W23.  `H60=H60a AND T4=T4a AND RSI=RSI3`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude H20=H20b drops 4/12 losers (33%)
- **Final: n=87  W=79/L=8  WR=90.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF20 slightly aligned

### W24.  `H60=H60a AND T4=T4a AND RSI=RSI2`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude T1=T1c drops 14/14 losers (100%)
- **Final: n=79  W=79/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when 1h trend AGAINST trade

### W25.  `T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude BBP=BBP1 drops 8/14 losers (57%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london_open  •  AVOID when just touched lower band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=150  W=46/L=104  WR=30.7%
- Sharpen: sharpest is H20=H20e (44/104 of losers there)
- **Sharp: n=46  W=2/L=44  WR=4.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L02.  `H20=H20e AND T4=T4c AND direction_exec=long`
- Raw: n=132  W=50/L=82  WR=37.9%
- Sharpen: sharpest is H60=H60e (46/82 of losers there)
- **Sharp: n=58  W=12/L=46  WR=20.7%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade  •  ONLY when HTF60 strongly against

### L03.  `T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=123  W=40/L=83  WR=32.5%
- Sharpen: sharpest is H60=H60e (53/83 of losers there)
- **Sharp: n=54  W=1/L=53  WR=1.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L04.  `H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=120  W=23/L=97  WR=19.2%
- Sharpen: sharpest is RSI=RSI2 (53/97 of losers there)
- **Sharp: n=54  W=1/L=53  WR=1.9%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L05.  `H20=H20e AND T1=T1c AND T4=T4c`
- Raw: n=112  W=41/L=71  WR=36.6%
- Sharpen: sharpest is RSI=RSI2 (43/71 of losers there)
- **Sharp: n=45  W=2/L=43  WR=4.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L06.  `T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=110  W=30/L=80  WR=27.3%
- Sharpen: sharpest is H60=H60e (53/80 of losers there)
- **Sharp: n=54  W=1/L=53  WR=1.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L07.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=110  W=30/L=80  WR=27.3%
- Sharpen: sharpest is H60=H60e (53/80 of losers there)
- **Sharp: n=54  W=1/L=53  WR=1.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L08.  `H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=100  W=12/L=88  WR=12.0%
- Sharpen: sharpest is RSI=RSI2 (53/88 of losers there)
- **Sharp: n=54  W=1/L=53  WR=1.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L09.  `H60=H60e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=98  W=11/L=87  WR=11.2%
- Sharpen: sharpest is RSI=RSI2 (53/87 of losers there)
- **Sharp: n=54  W=1/L=53  WR=1.9%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L10.  `H20=H20e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=96  W=29/L=67  WR=30.2%
- Sharpen: sharpest is RSI=RSI2 (43/67 of losers there)
- **Sharp: n=45  W=2/L=43  WR=4.4%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L11.  `T4=T4c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=93  W=36/L=57  WR=38.7%
- Sharpen: sharpest is H60=H60e (37/57 of losers there)
- **Sharp: n=42  W=5/L=37  WR=11.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L12.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=93  W=36/L=57  WR=38.7%
- Sharpen: sharpest is H60=H60e (37/57 of losers there)
- **Sharp: n=42  W=5/L=37  WR=11.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L13.  `H60=H60e AND T4=T4c AND RSI=RSI2`
- Raw: n=91  W=32/L=59  WR=35.2%
- Sharpen: sharpest is T1=T1c (53/59 of losers there)
- **Sharp: n=54  W=1/L=53  WR=1.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 1h trend AGAINST trade

### L14.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=87  W=31/L=56  WR=35.6%
- Sharpen: sharpest is H60=H60e (39/56 of losers there)
- **Sharp: n=45  W=6/L=39  WR=13.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when HTF60 strongly against

### L15.  `T1=T1c AND T4=T4c AND ZS=ZS2`
- Raw: n=86  W=32/L=54  WR=37.2%
- Sharpen: sharpest is H60=H60e (37/54 of losers there)
- **Sharp: n=42  W=5/L=37  WR=11.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L16.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=86  W=32/L=54  WR=37.2%
- Sharpen: sharpest is H60=H60e (37/54 of losers there)
- **Sharp: n=42  W=5/L=37  WR=11.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L17.  `H60=H60e AND T1=T1c AND RSI=RSI2`
- Raw: n=81  W=12/L=69  WR=14.8%
- Sharpen: sharpest is T4=T4c (53/69 of losers there)
- **Sharp: n=54  W=1/L=53  WR=1.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L18.  `H60=H60e AND T1=T1c AND BBP=BBP2`
- Raw: n=81  W=28/L=53  WR=34.6%
- Sharpen: sharpest is RSI=RSI2 (38/53 of losers there)
- **Sharp: n=38  W=0/L=38  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when RSI 30-40 weak

### L19.  `T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=80  W=30/L=50  WR=37.5%
- Sharpen: sharpest is H60=H60e (44/50 of losers there)
- **Sharp: n=52  W=8/L=44  WR=15.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L20.  `H60=H60e AND BBP=BBP2 AND direction_exec=long`
- Raw: n=77  W=29/L=48  WR=37.7%
- Sharpen: sharpest is RSI=RSI2 (32/48 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; lower third  •  ONLY when RSI 30-40 weak

### L21.  `T1=T1c AND T4=T4c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=76  W=25/L=51  WR=32.9%
- Sharpen: sharpest is H60=H60e (36/51 of losers there)
- **Sharp: n=40  W=4/L=36  WR=10.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L22.  `T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=75  W=21/L=54  WR=28.0%
- Sharpen: sharpest is T4=T4c (48/54 of losers there)
- **Sharp: n=54  W=6/L=48  WR=11.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L23.  `H20=H20e AND H60=H60e AND direction_exec=long`
- Raw: n=75  W=25/L=50  WR=33.3%
- Sharpen: sharpest is RSI=RSI2 (28/50 of losers there)
- **Sharp: n=29  W=1/L=28  WR=3.4%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against  •  ONLY when RSI 30-40 weak

### L24.  `H60=H60e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=74  W=12/L=62  WR=16.2%
- Sharpen: sharpest is T4=T4c (53/62 of losers there)
- **Sharp: n=54  W=1/L=53  WR=1.9%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L25.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=74  W=12/L=62  WR=16.2%
- Sharpen: sharpest is T4=T4c (53/62 of losers there)
- **Sharp: n=54  W=1/L=53  WR=1.9%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(35/29) | H20e(28/35) |
| H60 | H60a(41/22) | H60e(28/47) |
| T1 | T1a(58/43) | T1c(42/57) |
| T4 | T4a(61/36) | T4c(39/64) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(61/40) | long(39/60) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
