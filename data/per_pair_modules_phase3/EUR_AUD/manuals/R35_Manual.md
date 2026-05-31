# EUR_AUD — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,394**  (W=2,596 / L=1,798)  -  WR: **59.1%**

## Session distribution

- asia: n=1114  W=642/L=472  WR=57.6%
- ny_close: n=999  W=600/L=399  WR=60.1%
- ny_mid: n=993  W=584/L=409  WR=58.8%
- ny_open: n=519  W=296/L=223  WR=57.0%
- london_open: n=366  W=218/L=148  WR=59.6%
- off_hours: n=184  W=116/L=68  WR=63.0%
- london: n=165  W=107/L=58  WR=64.8%
- asia_late: n=54  W=33/L=21  WR=61.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60e AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=117  W=101/L=16  WR=86.3%
- Refine: exclude session_bucket=ny_close drops 10/16 losers (62%)
- **Final: n=107  W=101/L=6  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W02.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=117  W=101/L=16  WR=86.3%
- Refine: exclude session_bucket=ny_close drops 10/16 losers (62%)
- **Final: n=107  W=101/L=6  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W03.  `H20=H20e AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=117  W=101/L=16  WR=86.3%
- Refine: exclude session_bucket=ny_close drops 10/16 losers (62%)
- **Final: n=107  W=101/L=6  WR=94.4%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W04.  `H20=H20a AND T4=T4a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: no further refinement
- **Final: n=94  W=81/L=13  WR=86.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third; session=ny_open

### W05.  `H20=H20a AND T4=T4a AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude RSI=RSI2 drops 12/12 losers (100%)
- **Final: n=12  W=12/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold; session=ny_open  •  AVOID when RSI 30-40 weak

### W06.  `T1=T1c AND ZS=ZS3 AND session_bucket=london_open`
- Raw: n=68  W=62/L=6  WR=91.2%
- Refine: exclude RSI=RSI1 drops 2/6 losers (33%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -1 to +1 neutral; session=london_open  •  AVOID when RSI 20-30 oversold

### W07.  `H20=H20e AND BBP=BBP2 AND session_bucket=off_hours`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  HTF20 strongly against; lower third; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W08.  `H60=H60e AND BBP=BBP2 AND session_bucket=off_hours`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  HTF60 strongly against; lower third; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W09.  `T1=T1c AND BBP=BBP2 AND session_bucket=off_hours`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W10.  `T4=T4c AND BBP=BBP2 AND session_bucket=off_hours`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W11.  `BBP=BBP2 AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: LONG**  •  lower third; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W12.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND session_bucket=off_hours`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W13.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND session_bucket=off_hours`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W14.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND session_bucket=off_hours`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W15.  `H20=H20e AND BBP=BBP2 AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: LONG**  •  HTF20 strongly against; lower third; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W16.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND session_bucket=off_hours`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W17.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND session_bucket=off_hours`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W18.  `H60=H60e AND BBP=BBP2 AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W19.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND session_bucket=off_hours`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W20.  `T1=T1c AND BBP=BBP2 AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W21.  `T4=T4c AND BBP=BBP2 AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W22.  `H60=H60e AND ZS=ZS3 AND session_bucket=london_open`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude BBP=BBP2 drops 3/7 losers (43%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: ?**  •  HTF60 strongly against; zscore -1 to +1 neutral; session=london_open  •  AVOID when lower third

### W23.  `T4=T4c AND ZS=ZS3 AND session_bucket=london_open`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude BBP=BBP2 drops 3/7 losers (43%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -1 to +1 neutral; session=london_open  •  AVOID when lower third

### W24.  `ZS=ZS3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude BBP=BBP2 drops 3/7 losers (43%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: LONG**  •  zscore -1 to +1 neutral; session=london_open  •  AVOID when lower third

### W25.  `H60=H60e AND T4=T4c AND ZS=ZS3 AND session_bucket=london_open`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude BBP=BBP2 drops 3/7 losers (43%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -1 to +1 neutral; session=london_open  •  AVOID when lower third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=221  W=84/L=137  WR=38.0%
- Sharpen: sharpest is session_bucket=asia (65/137 of losers there)
- **Sharp: n=84  W=19/L=65  WR=22.6%**
- **Dir: ?**  •  HTF60 strongly against; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L02.  `T1=T1c AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=221  W=84/L=137  WR=38.0%
- Sharpen: sharpest is session_bucket=asia (65/137 of losers there)
- **Sharp: n=84  W=19/L=65  WR=22.6%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L03.  `T4=T4c AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=221  W=84/L=137  WR=38.0%
- Sharpen: sharpest is session_bucket=asia (65/137 of losers there)
- **Sharp: n=84  W=19/L=65  WR=22.6%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L04.  `RSI=RSI1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=221  W=84/L=137  WR=38.0%
- Sharpen: sharpest is session_bucket=asia (65/137 of losers there)
- **Sharp: n=84  W=19/L=65  WR=22.6%**
- **Dir: LONG**  •  RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L05.  `H60=H60e AND T1=T1c AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=221  W=84/L=137  WR=38.0%
- Sharpen: sharpest is session_bucket=asia (65/137 of losers there)
- **Sharp: n=84  W=19/L=65  WR=22.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L06.  `H60=H60e AND T4=T4c AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=221  W=84/L=137  WR=38.0%
- Sharpen: sharpest is session_bucket=asia (65/137 of losers there)
- **Sharp: n=84  W=19/L=65  WR=22.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L07.  `H60=H60e AND RSI=RSI1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=221  W=84/L=137  WR=38.0%
- Sharpen: sharpest is session_bucket=asia (65/137 of losers there)
- **Sharp: n=84  W=19/L=65  WR=22.6%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L08.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=221  W=84/L=137  WR=38.0%
- Sharpen: sharpest is session_bucket=asia (65/137 of losers there)
- **Sharp: n=84  W=19/L=65  WR=22.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L09.  `T1=T1c AND RSI=RSI1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=221  W=84/L=137  WR=38.0%
- Sharpen: sharpest is session_bucket=asia (65/137 of losers there)
- **Sharp: n=84  W=19/L=65  WR=22.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L10.  `T4=T4c AND RSI=RSI1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=221  W=84/L=137  WR=38.0%
- Sharpen: sharpest is session_bucket=asia (65/137 of losers there)
- **Sharp: n=84  W=19/L=65  WR=22.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L11.  `H20=H20e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=175  W=63/L=112  WR=36.0%
- Sharpen: sharpest is RSI=RSI1 (45/112 of losers there)
- **Sharp: n=52  W=7/L=45  WR=13.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 20-30 oversold

### L12.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=175  W=63/L=112  WR=36.0%
- Sharpen: sharpest is RSI=RSI1 (45/112 of losers there)
- **Sharp: n=52  W=7/L=45  WR=13.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 20-30 oversold

### L13.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=175  W=63/L=112  WR=36.0%
- Sharpen: sharpest is RSI=RSI1 (45/112 of losers there)
- **Sharp: n=52  W=7/L=45  WR=13.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 20-30 oversold

### L14.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=175  W=63/L=112  WR=36.0%
- Sharpen: sharpest is RSI=RSI1 (45/112 of losers there)
- **Sharp: n=52  W=7/L=45  WR=13.5%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 20-30 oversold

### L15.  `H60=H60e AND BBP=BBP0 AND RSI=RSI1`
- Raw: n=141  W=51/L=90  WR=36.2%
- Sharpen: sharpest is session_bucket=ny_open (29/90 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; RSI 20-30 oversold  •  ONLY when session=ny_open

### L16.  `T1=T1c AND BBP=BBP0 AND RSI=RSI1`
- Raw: n=141  W=51/L=90  WR=36.2%
- Sharpen: sharpest is session_bucket=ny_open (29/90 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; RSI 20-30 oversold  •  ONLY when session=ny_open

### L17.  `T4=T4c AND BBP=BBP0 AND RSI=RSI1`
- Raw: n=141  W=51/L=90  WR=36.2%
- Sharpen: sharpest is session_bucket=ny_open (29/90 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 20-30 oversold  •  ONLY when session=ny_open

### L18.  `BBP=BBP0 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=141  W=51/L=90  WR=36.2%
- Sharpen: sharpest is session_bucket=ny_open (29/90 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: LONG**  •  deep below lower band; RSI 20-30 oversold  •  ONLY when session=ny_open

### L19.  `H60=H60e AND T1=T1c AND BBP=BBP0 AND RSI=RSI1`
- Raw: n=141  W=51/L=90  WR=36.2%
- Sharpen: sharpest is session_bucket=ny_open (29/90 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep below lower band; RSI 20-30 oversold  •  ONLY when session=ny_open

### L20.  `H60=H60e AND T4=T4c AND BBP=BBP0 AND RSI=RSI1`
- Raw: n=141  W=51/L=90  WR=36.2%
- Sharpen: sharpest is session_bucket=ny_open (29/90 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band; RSI 20-30 oversold  •  ONLY when session=ny_open

### L21.  `H60=H60e AND BBP=BBP0 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=141  W=51/L=90  WR=36.2%
- Sharpen: sharpest is session_bucket=ny_open (29/90 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: LONG**  •  HTF60 strongly against; deep below lower band; RSI 20-30 oversold  •  ONLY when session=ny_open

### L22.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND RSI=RSI1`
- Raw: n=141  W=51/L=90  WR=36.2%
- Sharpen: sharpest is session_bucket=ny_open (29/90 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band; RSI 20-30 oversold  •  ONLY when session=ny_open

### L23.  `T1=T1c AND BBP=BBP0 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=141  W=51/L=90  WR=36.2%
- Sharpen: sharpest is session_bucket=ny_open (29/90 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; RSI 20-30 oversold  •  ONLY when session=ny_open

### L24.  `T4=T4c AND BBP=BBP0 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=141  W=51/L=90  WR=36.2%
- Sharpen: sharpest is session_bucket=ny_open (29/90 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band; RSI 20-30 oversold  •  ONLY when session=ny_open

### L25.  `H60=H60e AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=127  W=49/L=78  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=127  W=49/L=78  WR=38.6%**
- **Dir: ?**  •  HTF60 strongly against; lower third; session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(54/45) | H20e(46/55) |
| H60 | H60a(54/43) | H60e(46/57) |
| T1 | T1a(54/43) | T1c(46/57) |
| T4 | T4a(54/44) | T4c(46/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/43) | long(46/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
