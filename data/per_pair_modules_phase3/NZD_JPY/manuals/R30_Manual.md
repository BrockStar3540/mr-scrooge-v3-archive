# NZD_JPY — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **4,391**  (W=2,676 / L=1,715)  -  WR: **60.9%**

## Session distribution

- asia: n=1529  W=942/L=587  WR=61.6%
- ny_mid: n=793  W=466/L=327  WR=58.8%
- ny_close: n=549  W=340/L=209  WR=61.9%
- london_open: n=517  W=324/L=193  WR=62.7%
- london: n=469  W=265/L=204  WR=56.5%
- ny_open: n=217  W=136/L=81  WR=62.7%
- asia_late: n=195  W=122/L=73  WR=62.6%
- off_hours: n=122  W=81/L=41  WR=66.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=183  W=162/L=21  WR=88.5%
- Refine: exclude ZS=ZS2 drops 5/21 losers (24%)
- **Final: n=169  W=153/L=16  WR=90.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W02.  `T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=148  W=132/L=16  WR=89.2%
- Refine: exclude ZS=ZS2 drops 5/16 losers (31%)
- **Final: n=140  W=129/L=11  WR=92.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W03.  `T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=148  W=132/L=16  WR=89.2%
- Refine: exclude ZS=ZS2 drops 5/16 losers (31%)
- **Final: n=140  W=129/L=11  WR=92.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W04.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=148  W=132/L=16  WR=89.2%
- Refine: exclude ZS=ZS2 drops 5/16 losers (31%)
- **Final: n=140  W=129/L=11  WR=92.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W05.  `H20=H20a AND T4=T4c AND RSI=RSI3`
- Raw: n=134  W=120/L=14  WR=89.6%
- Refine: exclude ZS=ZS2 drops 5/14 losers (36%)
- **Final: n=120  W=111/L=9  WR=92.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W06.  `H20=H20a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=134  W=120/L=14  WR=89.6%
- Refine: exclude ZS=ZS2 drops 5/14 losers (36%)
- **Final: n=120  W=111/L=9  WR=92.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W07.  `H20=H20a AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=134  W=120/L=14  WR=89.6%
- Refine: exclude ZS=ZS2 drops 5/14 losers (36%)
- **Final: n=120  W=111/L=9  WR=92.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W08.  `H60=H60a AND T4=T4c AND RSI=RSI3`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude ZS=ZS2 drops 5/15 losers (33%)
- **Final: n=100  W=90/L=10  WR=90.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W09.  `H60=H60a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude ZS=ZS2 drops 5/15 losers (33%)
- **Final: n=100  W=90/L=10  WR=90.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W10.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude ZS=ZS2 drops 5/15 losers (33%)
- **Final: n=100  W=90/L=10  WR=90.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W11.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude ZS=ZS2 drops 5/15 losers (33%)
- **Final: n=100  W=90/L=10  WR=90.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W12.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude ZS=ZS2 drops 5/15 losers (33%)
- **Final: n=100  W=90/L=10  WR=90.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W13.  `H60=H60e AND T4=T4c AND ZS=ZS3`
- Raw: n=105  W=91/L=14  WR=86.7%
- Refine: exclude session_bucket=asia drops 8/14 losers (57%)
- **Final: n=82  W=76/L=6  WR=92.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when session=asia

### W14.  `H20=H20a AND T1=T1c AND RSI=RSI3`
- Raw: n=99  W=90/L=9  WR=90.9%
- Refine: exclude ZS=ZS2 drops 5/9 losers (56%)
- **Final: n=91  W=87/L=4  WR=95.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W15.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=99  W=90/L=9  WR=90.9%
- Refine: exclude ZS=ZS2 drops 5/9 losers (56%)
- **Final: n=91  W=87/L=4  WR=95.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W16.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=99  W=90/L=9  WR=90.9%
- Refine: exclude ZS=ZS2 drops 5/9 losers (56%)
- **Final: n=91  W=87/L=4  WR=95.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W17.  `H20=H20a AND H60=H60e AND session_bucket=london_open`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/11 losers (18%)
- **Final: n=85  W=76/L=9  WR=89.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=london_open  •  AVOID when strategy=delta_tag_and_go_v2

### W18.  `H20=H20a AND H60=H60e AND T1=T1a AND session_bucket=london_open`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/11 losers (18%)
- **Final: n=85  W=76/L=9  WR=89.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when strategy=delta_tag_and_go_v2

### W19.  `H20=H20a AND BBP=BBP0 AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=88  W=78/L=10  WR=88.6%
- Refine: exclude session_bucket=london drops 5/10 losers (50%)
- **Final: n=83  W=78/L=5  WR=94.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep below lower band; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W20.  `H20=H20a AND T1=T1a AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude session_bucket=london drops 9/12 losers (75%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W21.  `H20=H20a AND T4=T4a AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude session_bucket=london drops 9/12 losers (75%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W22.  `H20=H20a AND RSI=RSI1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude session_bucket=london drops 9/12 losers (75%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W23.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude T1=T1a drops 4/11 losers (36%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W24.  `BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude strategy_id=alpha_pullback_v2 drops 3/9 losers (33%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: LONG**  •  upper third; RSI 40-50 lower neutral  •  AVOID when strategy=alpha_pullback_v2

### W25.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude strategy_id=alpha_pullback_v2 drops 3/9 losers (33%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  AVOID when strategy=alpha_pullback_v2

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND RSI=RSI0`
- Raw: n=143  W=56/L=87  WR=39.2%
- Sharpen: sharpest is H20=H20a (49/87 of losers there)
- **Sharp: n=61  W=12/L=49  WR=19.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when HTF20 aligned WITH trade

### L02.  `T1=T1c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=143  W=56/L=87  WR=39.2%
- Sharpen: sharpest is H20=H20a (49/87 of losers there)
- **Sharp: n=61  W=12/L=49  WR=19.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when HTF20 aligned WITH trade

### L03.  `T4=T4c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=143  W=56/L=87  WR=39.2%
- Sharpen: sharpest is H20=H20a (49/87 of losers there)
- **Sharp: n=61  W=12/L=49  WR=19.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when HTF20 aligned WITH trade

### L04.  `T1=T1c AND T4=T4c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=143  W=56/L=87  WR=39.2%
- Sharpen: sharpest is H20=H20a (49/87 of losers there)
- **Sharp: n=61  W=12/L=49  WR=19.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when HTF20 aligned WITH trade

### L05.  `T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=133  W=26/L=107  WR=19.5%
- Sharpen: sharpest is session_bucket=asia (36/107 of losers there)
- **Sharp: n=38  W=2/L=36  WR=5.3%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L06.  `H20=H20a AND H60=H60e AND T4=T4a AND RSI=RSI2`
- Raw: n=130  W=49/L=81  WR=37.7%
- Sharpen: sharpest is BBP=BBP2 (29/81 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when lower third

### L07.  `H20=H20a AND H60=H60e AND RSI=RSI2 AND direction_exec=short`
- Raw: n=130  W=49/L=81  WR=37.7%
- Sharpen: sharpest is BBP=BBP2 (29/81 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 30-40 weak  •  ONLY when lower third

### L08.  `T4=T4c AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=126  W=47/L=79  WR=37.3%
- Sharpen: sharpest is BBP=BBP0 (47/79 of losers there)
- **Sharp: n=53  W=6/L=47  WR=11.3%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_mid  •  ONLY when deep below lower band

### L09.  `H60=H60a AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=121  W=44/L=77  WR=36.4%
- Sharpen: sharpest is BBP=BBP0 (47/77 of losers there)
- **Sharp: n=53  W=6/L=47  WR=11.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=ny_mid  •  ONLY when deep below lower band

### L10.  `T1=T1c AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=121  W=44/L=77  WR=36.4%
- Sharpen: sharpest is BBP=BBP0 (47/77 of losers there)
- **Sharp: n=53  W=6/L=47  WR=11.3%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_mid  •  ONLY when deep below lower band

### L11.  `ZS=ZS1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=121  W=44/L=77  WR=36.4%
- Sharpen: sharpest is BBP=BBP0 (47/77 of losers there)
- **Sharp: n=53  W=6/L=47  WR=11.3%**
- **Dir: LONG**  •  zscore -3 to -2 deep oversold; session=ny_mid  •  ONLY when deep below lower band

### L12.  `H60=H60a AND T1=T1c AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=121  W=44/L=77  WR=36.4%
- Sharpen: sharpest is BBP=BBP0 (47/77 of losers there)
- **Sharp: n=53  W=6/L=47  WR=11.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_mid  •  ONLY when deep below lower band

### L13.  `H60=H60a AND ZS=ZS1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=121  W=44/L=77  WR=36.4%
- Sharpen: sharpest is BBP=BBP0 (47/77 of losers there)
- **Sharp: n=53  W=6/L=47  WR=11.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=ny_mid  •  ONLY when deep below lower band

### L14.  `T1=T1c AND ZS=ZS1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=121  W=44/L=77  WR=36.4%
- Sharpen: sharpest is BBP=BBP0 (47/77 of losers there)
- **Sharp: n=53  W=6/L=47  WR=11.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_mid  •  ONLY when deep below lower band

### L15.  `T4=T4a AND BBP=BBP3 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=111  W=42/L=69  WR=37.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=111  W=42/L=69  WR=37.8%**
- **Dir: SHORT**  •  4h trend WITH trade; middle of band; RSI 30-40 weak

### L16.  `T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=110  W=21/L=89  WR=19.1%
- Sharpen: sharpest is session_bucket=asia (36/89 of losers there)
- **Sharp: n=38  W=2/L=36  WR=5.3%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L17.  `H60=H60a AND T4=T4c AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=110  W=40/L=70  WR=36.4%
- Sharpen: sharpest is BBP=BBP0 (42/70 of losers there)
- **Sharp: n=48  W=6/L=42  WR=12.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_mid  •  ONLY when deep below lower band

### L18.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=110  W=40/L=70  WR=36.4%
- Sharpen: sharpest is BBP=BBP0 (42/70 of losers there)
- **Sharp: n=48  W=6/L=42  WR=12.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_mid  •  ONLY when deep below lower band

### L19.  `T4=T4c AND ZS=ZS1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=110  W=40/L=70  WR=36.4%
- Sharpen: sharpest is BBP=BBP0 (42/70 of losers there)
- **Sharp: n=48  W=6/L=42  WR=12.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_mid  •  ONLY when deep below lower band

### L20.  `H60=H60a AND T4=T4a AND BBP=BBP2`
- Raw: n=110  W=44/L=66  WR=40.0%
- Sharpen: sharpest is T1=T1c (38/66 of losers there)
- **Sharp: n=56  W=18/L=38  WR=32.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third  •  ONLY when 1h trend AGAINST trade

### L21.  `T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=108  W=21/L=87  WR=19.4%
- Sharpen: sharpest is session_bucket=asia (36/87 of losers there)
- **Sharp: n=38  W=2/L=36  WR=5.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L22.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=108  W=21/L=87  WR=19.4%
- Sharpen: sharpest is session_bucket=asia (36/87 of losers there)
- **Sharp: n=38  W=2/L=36  WR=5.3%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L23.  `H20=H20a AND H60=H60e AND session_bucket=london`
- Raw: n=108  W=40/L=68  WR=37.0%
- Sharpen: sharpest is T1=T1c (49/68 of losers there)
- **Sharp: n=61  W=12/L=49  WR=19.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=london  •  ONLY when 1h trend AGAINST trade

### L24.  `T1=T1a AND T4=T4a AND BBP=BBP3 AND RSI=RSI2`
- Raw: n=108  W=42/L=66  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=108  W=42/L=66  WR=38.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; middle of band; RSI 30-40 weak

### L25.  `H60=H60e AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=106  W=36/L=70  WR=34.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=106  W=36/L=70  WR=34.0%**
- **Dir: ?**  •  HTF60 strongly against; just touched lower band; RSI 30-40 weak

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
