# NZD_JPY — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,889**  (W=1,878 / L=1,011)  -  WR: **65.0%**

## Session distribution

- asia: n=1183  W=757/L=426  WR=64.0%
- london_open: n=400  W=270/L=130  WR=67.5%
- ny_open: n=359  W=242/L=117  WR=67.4%
- ny_close: n=308  W=197/L=111  WR=64.0%
- ny_mid: n=276  W=175/L=101  WR=63.4%
- london: n=172  W=112/L=60  WR=65.1%
- asia_late: n=136  W=89/L=47  WR=65.4%
- off_hours: n=55  W=36/L=19  WR=65.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=260  W=226/L=34  WR=86.9%
- Refine: exclude T4=T4c drops 25/34 losers (74%)
- **Final: n=137  W=128/L=9  WR=93.4%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band  •  AVOID when 4h trend AGAINST trade

### W02.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=259  W=222/L=37  WR=85.7%
- Refine: exclude T4=T4c drops 29/37 losers (78%)
- **Final: n=155  W=147/L=8  WR=94.8%**
- **Dir: SHORT**  •  deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W03.  `T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=248  W=214/L=34  WR=86.3%
- Refine: exclude RSI=RSI3 drops 30/34 losers (88%)
- **Final: n=112  W=108/L=4  WR=96.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W04.  `T1=T1a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=217  W=188/L=29  WR=86.6%
- Refine: exclude T4=T4c drops 25/29 losers (86%)
- **Final: n=112  W=108/L=4  WR=96.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W05.  `RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=217  W=188/L=29  WR=86.6%
- Refine: exclude T4=T4c drops 25/29 losers (86%)
- **Final: n=112  W=108/L=4  WR=96.4%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W06.  `T1=T1a AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=217  W=188/L=29  WR=86.6%
- Refine: exclude T4=T4c drops 25/29 losers (86%)
- **Final: n=112  W=108/L=4  WR=96.4%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W07.  `H60=H60e AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=200  W=170/L=30  WR=85.0%
- Refine: exclude T4=T4c drops 25/30 losers (83%)
- **Final: n=100  W=95/L=5  WR=95.0%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W08.  `T1=T1a AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=198  W=178/L=20  WR=89.9%
- Refine: exclude BBP=BBP1 drops 20/20 losers (100%)
- **Final: n=116  W=116/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W09.  `T1=T1a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=192  W=175/L=17  WR=91.1%
- Refine: exclude T4=T4c drops 17/17 losers (100%)
- **Final: n=116  W=116/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W10.  `H60=H60e AND T1=T1a AND BBP=BBP0`
- Raw: n=183  W=156/L=27  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 12/27 losers (44%)
- **Final: n=156  W=141/L=15  WR=90.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; deep below lower band  •  AVOID when session=ny_mid

### W11.  `H60=H60e AND T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=183  W=156/L=27  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 12/27 losers (44%)
- **Final: n=156  W=141/L=15  WR=90.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; deep below lower band  •  AVOID when session=ny_mid

### W12.  `RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=178  W=157/L=21  WR=88.2%
- Refine: exclude H20=H20d drops 6/21 losers (29%)
- **Final: n=167  W=152/L=15  WR=91.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF20 mildly against

### W13.  `T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=176  W=159/L=17  WR=90.3%
- Refine: exclude ZS=ZS0 drops 9/17 losers (53%)
- **Final: n=155  W=147/L=8  WR=94.8%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band  •  AVOID when zscore <-3 extreme

### W14.  `T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=173  W=150/L=23  WR=86.7%
- Refine: exclude BBP=BBP2 drops 15/23 losers (65%)
- **Final: n=119  W=111/L=8  WR=93.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when lower third

### W15.  `T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=173  W=150/L=23  WR=86.7%
- Refine: exclude BBP=BBP2 drops 15/23 losers (65%)
- **Final: n=119  W=111/L=8  WR=93.3%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak  •  AVOID when lower third

### W16.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=173  W=150/L=23  WR=86.7%
- Refine: exclude BBP=BBP2 drops 15/23 losers (65%)
- **Final: n=119  W=111/L=8  WR=93.3%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when lower third

### W17.  `H60=H60e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=171  W=149/L=22  WR=87.1%
- Refine: exclude T4=T4c drops 22/22 losers (100%)
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W18.  `H60=H60e AND T1=T1a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=171  W=149/L=22  WR=87.1%
- Refine: exclude T4=T4c drops 22/22 losers (100%)
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W19.  `H60=H60e AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=171  W=149/L=22  WR=87.1%
- Refine: exclude T4=T4c drops 22/22 losers (100%)
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W20.  `T4=T4a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=155  W=147/L=8  WR=94.8%
- Refine: exclude T1=T1c drops 8/8 losers (100%)
- **Final: n=116  W=116/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when 1h trend AGAINST trade

### W21.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=155  W=137/L=18  WR=88.4%
- Refine: exclude H20=H20d drops 6/18 losers (33%)
- **Final: n=144  W=132/L=12  WR=91.7%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF20 mildly against

### W22.  `T1=T1a AND T4=T4a AND BBP=BBP0`
- Raw: n=150  W=132/L=18  WR=88.0%
- Refine: exclude H20=H20c drops 9/18 losers (50%)
- **Final: n=141  W=132/L=9  WR=93.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band  •  AVOID when HTF20 neutral

### W23.  `H20=H20e AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=147  W=125/L=22  WR=85.0%
- Refine: exclude direction_exec=long drops 16/22 losers (73%)
- **Final: n=114  W=108/L=6  WR=94.7%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; session=london_open  •  AVOID when long

### W24.  `H60=H60e AND T1=T1a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=142  W=129/L=13  WR=90.8%
- Refine: exclude T4=T4c drops 13/13 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W25.  `T1=T1a AND T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=137  W=128/L=9  WR=93.4%
- Refine: exclude ZS=ZS0 drops 9/9 losers (100%)
- **Final: n=116  W=116/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band  •  AVOID when zscore <-3 extreme

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=219  W=79/L=140  WR=36.1%
- Sharpen: sharpest is RSI=RSI2 (62/140 of losers there)
- **Sharp: n=68  W=6/L=62  WR=8.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L02.  `T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=189  W=64/L=125  WR=33.9%
- Sharpen: sharpest is RSI=RSI2 (62/125 of losers there)
- **Sharp: n=68  W=6/L=62  WR=8.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L03.  `T1=T1c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=177  W=57/L=120  WR=32.2%
- Sharpen: sharpest is T4=T4c (62/120 of losers there)
- **Sharp: n=68  W=6/L=62  WR=8.8%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L04.  `RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=177  W=57/L=120  WR=32.2%
- Sharpen: sharpest is T4=T4c (62/120 of losers there)
- **Sharp: n=68  W=6/L=62  WR=8.8%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L05.  `T1=T1c AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=177  W=57/L=120  WR=32.2%
- Sharpen: sharpest is T4=T4c (62/120 of losers there)
- **Sharp: n=68  W=6/L=62  WR=8.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L06.  `H60=H60a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=156  W=52/L=104  WR=33.3%
- Sharpen: sharpest is T4=T4c (60/104 of losers there)
- **Sharp: n=70  W=10/L=60  WR=14.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L07.  `T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=154  W=55/L=99  WR=35.7%
- Sharpen: sharpest is T4=T4c (63/99 of losers there)
- **Sharp: n=83  W=20/L=63  WR=24.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when 4h trend AGAINST trade

### L08.  `RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=154  W=55/L=99  WR=35.7%
- Sharpen: sharpest is T4=T4c (63/99 of losers there)
- **Sharp: n=83  W=20/L=63  WR=24.1%**
- **Dir: LONG**  •  RSI 30-40 weak; session=asia  •  ONLY when 4h trend AGAINST trade

### L09.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=154  W=55/L=99  WR=35.7%
- Sharpen: sharpest is T4=T4c (63/99 of losers there)
- **Sharp: n=83  W=20/L=63  WR=24.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when 4h trend AGAINST trade

### L10.  `H60=H60a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=153  W=52/L=101  WR=34.0%
- Sharpen: sharpest is T4=T4c (57/101 of losers there)
- **Sharp: n=67  W=10/L=57  WR=14.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L11.  `H60=H60a AND T4=T4c AND ZS=ZS1`
- Raw: n=148  W=47/L=101  WR=31.8%
- Sharpen: sharpest is RSI=RSI2 (41/101 of losers there)
- **Sharp: n=41  W=0/L=41  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L12.  `H60=H60a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=146  W=47/L=99  WR=32.2%
- Sharpen: sharpest is T4=T4c (41/99 of losers there)
- **Sharp: n=41  W=0/L=41  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L13.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=146  W=47/L=99  WR=32.2%
- Sharpen: sharpest is T4=T4c (41/99 of losers there)
- **Sharp: n=41  W=0/L=41  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L14.  `H60=H60a AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=146  W=47/L=99  WR=32.2%
- Sharpen: sharpest is T4=T4c (41/99 of losers there)
- **Sharp: n=41  W=0/L=41  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L15.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=145  W=39/L=106  WR=26.9%
- Sharpen: sharpest is RSI=RSI2 (62/106 of losers there)
- **Sharp: n=68  W=6/L=62  WR=8.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L16.  `H60=H60a AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=145  W=47/L=98  WR=32.4%
- Sharpen: sharpest is RSI=RSI2 (41/98 of losers there)
- **Sharp: n=41  W=0/L=41  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L17.  `H20=H20a AND H60=H60a AND T1=T1c AND ZS=ZS1`
- Raw: n=139  W=54/L=85  WR=38.8%
- Sharpen: sharpest is T4=T4c (36/85 of losers there)
- **Sharp: n=38  W=2/L=36  WR=5.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L18.  `H20=H20a AND T1=T1c AND T4=T4c`
- Raw: n=135  W=51/L=84  WR=37.8%
- Sharpen: sharpest is ZS=ZS1 (47/84 of losers there)
- **Sharp: n=49  W=2/L=47  WR=4.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=133  W=40/L=93  WR=30.1%
- Sharpen: sharpest is RSI=RSI2 (39/93 of losers there)
- **Sharp: n=43  W=4/L=39  WR=9.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L20.  `T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=133  W=44/L=89  WR=33.1%
- Sharpen: sharpest is ZS=ZS1 (62/89 of losers there)
- **Sharp: n=68  W=6/L=62  WR=8.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L21.  `T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=133  W=44/L=89  WR=33.1%
- Sharpen: sharpest is ZS=ZS1 (62/89 of losers there)
- **Sharp: n=68  W=6/L=62  WR=8.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L22.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=133  W=44/L=89  WR=33.1%
- Sharpen: sharpest is ZS=ZS1 (62/89 of losers there)
- **Sharp: n=68  W=6/L=62  WR=8.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L23.  `T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=129  W=42/L=87  WR=32.6%
- Sharpen: sharpest is RSI=RSI2 (39/87 of losers there)
- **Sharp: n=43  W=4/L=39  WR=9.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L24.  `H20=H20a AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=128  W=44/L=84  WR=34.4%
- Sharpen: sharpest is ZS=ZS1 (47/84 of losers there)
- **Sharp: n=49  W=2/L=47  WR=4.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L25.  `H60=H60a AND T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=121  W=44/L=77  WR=36.4%
- Sharpen: sharpest is T4=T4c (42/77 of losers there)
- **Sharp: n=48  W=6/L=42  WR=12.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(54/44) | T1c(46/56) |
| T4 | T4a(55/45) | T4c(45/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/43) | long(47/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
