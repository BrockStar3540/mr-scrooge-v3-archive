# GBP_USD — R32 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **4,535**  (W=2,744 / L=1,791)  -  WR: **60.5%**

## Session distribution

- ny_mid: n=1323  W=786/L=537  WR=59.4%
- london_open: n=1071  W=657/L=414  WR=61.3%
- ny_open: n=799  W=473/L=326  WR=59.2%
- ny_close: n=471  W=302/L=169  WR=64.1%
- asia: n=420  W=249/L=171  WR=59.3%
- london: n=322  W=189/L=133  WR=58.7%
- asia_late: n=114  W=76/L=38  WR=66.7%
- off_hours: n=15  W=12/L=3  WR=80.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T1=T1a AND session_bucket=ny_open`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude BBP=BBP2 drops 10/15 losers (67%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when lower third

### W02.  `H20=H20e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude BBP=BBP2 drops 10/15 losers (67%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_open  •  AVOID when lower third

### W03.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=ny_open`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude BBP=BBP2 drops 10/15 losers (67%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when lower third

### W04.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude BBP=BBP2 drops 10/15 losers (67%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  AVOID when lower third

### W05.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude BBP=BBP2 drops 10/15 losers (67%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when lower third

### W06.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude BBP=BBP2 drops 10/15 losers (67%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when lower third

### W07.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude BBP=BBP2 drops 10/15 losers (67%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when lower third

### W08.  `T1=T1a AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=102  W=93/L=9  WR=91.2%
- Refine: exclude BBP=BBP1 drops 9/9 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=london_open  •  AVOID when just touched lower band

### W09.  `T4=T4a AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=102  W=93/L=9  WR=91.2%
- Refine: exclude BBP=BBP1 drops 9/9 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=london_open  •  AVOID when just touched lower band

### W10.  `ZS=ZS1 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=102  W=93/L=9  WR=91.2%
- Refine: exclude BBP=BBP1 drops 9/9 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: SHORT**  •  zscore -3 to -2 deep oversold; session=london_open  •  AVOID when just touched lower band

### W11.  `T1=T1a AND T4=T4a AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=102  W=93/L=9  WR=91.2%
- Refine: exclude BBP=BBP1 drops 9/9 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=london_open  •  AVOID when just touched lower band

### W12.  `T1=T1a AND ZS=ZS1 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=102  W=93/L=9  WR=91.2%
- Refine: exclude BBP=BBP1 drops 9/9 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=london_open  •  AVOID when just touched lower band

### W13.  `T4=T4a AND ZS=ZS1 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=102  W=93/L=9  WR=91.2%
- Refine: exclude BBP=BBP1 drops 9/9 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=london_open  •  AVOID when just touched lower band

### W14.  `T1=T1a AND BBP=BBP0 AND RSI=RSI1`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=80  W=74/L=6  WR=92.5%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W15.  `T4=T4a AND BBP=BBP0 AND RSI=RSI1`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=80  W=74/L=6  WR=92.5%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W16.  `BBP=BBP0 AND RSI=RSI1 AND direction_exec=short`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=80  W=74/L=6  WR=92.5%**
- **Dir: SHORT**  •  deep below lower band; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W17.  `T1=T1a AND T4=T4a AND BBP=BBP0 AND RSI=RSI1`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=80  W=74/L=6  WR=92.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W18.  `T1=T1a AND BBP=BBP0 AND RSI=RSI1 AND direction_exec=short`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=80  W=74/L=6  WR=92.5%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W19.  `T4=T4a AND BBP=BBP0 AND RSI=RSI1 AND direction_exec=short`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude session_bucket=ny_mid drops 7/13 losers (54%)
- **Final: n=80  W=74/L=6  WR=92.5%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W20.  `T1=T1a AND BBP=BBP0 AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 7/12 losers (58%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W21.  `T4=T4a AND BBP=BBP0 AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 7/12 losers (58%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W22.  `BBP=BBP0 AND RSI=RSI1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 7/12 losers (58%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: SHORT**  •  deep below lower band; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W23.  `H20=H20e AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: no further refinement
- **Final: n=77  W=68/L=9  WR=88.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 30-40 weak; session=ny_open

### W24.  `H20=H20e AND T4=T4a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude T1=T1a drops 10/10 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; lower third; session=ny_open  •  AVOID when 1h trend WITH trade

### W25.  `H20=H20e AND BBP=BBP1 AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude H60=H60a drops 6/10 losers (60%)
- **Final: n=43  W=39/L=4  WR=90.7%**
- **Dir: ?**  •  HTF20 strongly against; just touched lower band; RSI 30-40 weak; session=ny_open  •  AVOID when HTF60 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI1`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: sharpest is ZS=ZS1 (29/90 of losers there)
- **Sharp: n=37  W=8/L=29  WR=21.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L02.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI1`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: sharpest is ZS=ZS1 (29/90 of losers there)
- **Sharp: n=37  W=8/L=29  WR=21.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L03.  `H20=H20a AND H60=H60a AND RSI=RSI1 AND direction_exec=long`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: sharpest is ZS=ZS1 (29/90 of losers there)
- **Sharp: n=37  W=8/L=29  WR=21.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L04.  `H20=H20a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=121  W=41/L=80  WR=33.9%
- Sharpen: sharpest is RSI=RSI2 (51/80 of losers there)
- **Sharp: n=62  W=11/L=51  WR=17.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L05.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=121  W=41/L=80  WR=33.9%
- Sharpen: sharpest is RSI=RSI2 (51/80 of losers there)
- **Sharp: n=62  W=11/L=51  WR=17.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L06.  `H20=H20a AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=118  W=45/L=73  WR=38.1%
- Sharpen: sharpest is session_bucket=ny_open (27/73 of losers there)
- **Sharp: n=31  W=4/L=27  WR=12.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L07.  `H20=H20a AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=118  W=45/L=73  WR=38.1%
- Sharpen: sharpest is session_bucket=ny_open (27/73 of losers there)
- **Sharp: n=31  W=4/L=27  WR=12.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L08.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=116  W=38/L=78  WR=32.8%
- Sharpen: sharpest is T4=T4c (51/78 of losers there)
- **Sharp: n=62  W=11/L=51  WR=17.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L09.  `H20=H20a AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=113  W=40/L=73  WR=35.4%
- Sharpen: sharpest is T4=T4c (49/73 of losers there)
- **Sharp: n=67  W=18/L=49  WR=26.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -2 to -1 oversold; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L10.  `H20=H20a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=113  W=40/L=73  WR=35.4%
- Sharpen: sharpest is T4=T4c (49/73 of losers there)
- **Sharp: n=67  W=18/L=49  WR=26.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; zscore -2 to -1 oversold; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L11.  `H20=H20e AND T4=T4c AND BBP=BBP0`
- Raw: n=104  W=35/L=69  WR=33.7%
- Sharpen: sharpest is H60=H60a (26/69 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; deep below lower band  •  ONLY when HTF60 aligned WITH trade

### L12.  `H60=H60d AND T1=T1c AND BBP=BBP2`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is RSI=RSI0 (14/62 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; lower third  •  ONLY when RSI<20 extreme oversold

### L13.  `H60=H60d AND T4=T4c AND BBP=BBP2`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is RSI=RSI0 (14/62 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; lower third  •  ONLY when RSI<20 extreme oversold

### L14.  `H60=H60d AND BBP=BBP2 AND direction_exec=long`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is RSI=RSI0 (14/62 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: LONG**  •  HTF60 mildly against; lower third  •  ONLY when RSI<20 extreme oversold

### L15.  `H60=H60d AND T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is RSI=RSI0 (14/62 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when RSI<20 extreme oversold

### L16.  `H60=H60d AND T1=T1c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is RSI=RSI0 (14/62 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade; lower third  •  ONLY when RSI<20 extreme oversold

### L17.  `H60=H60d AND T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is RSI=RSI0 (14/62 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: LONG**  •  HTF60 mildly against; 4h trend AGAINST trade; lower third  •  ONLY when RSI<20 extreme oversold

### L18.  `H20=H20e AND T1=T1c AND BBP=BBP0`
- Raw: n=100  W=35/L=65  WR=35.0%
- Sharpen: sharpest is session_bucket=ny_open (30/65 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; deep below lower band  •  ONLY when session=ny_open

### L19.  `H20=H20e AND BBP=BBP0 AND direction_exec=long`
- Raw: n=100  W=35/L=65  WR=35.0%
- Sharpen: sharpest is session_bucket=ny_open (30/65 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; deep below lower band  •  ONLY when session=ny_open

### L20.  `H20=H20e AND T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=100  W=35/L=65  WR=35.0%
- Sharpen: sharpest is session_bucket=ny_open (30/65 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; deep below lower band  •  ONLY when session=ny_open

### L21.  `T1=T1c AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=97  W=26/L=71  WR=26.8%
- Sharpen: sharpest is H60=H60b (13/71 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london_open  •  ONLY when HTF60 slightly aligned

### L22.  `T4=T4c AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=97  W=26/L=71  WR=26.8%
- Sharpen: sharpest is H60=H60b (13/71 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london_open  •  ONLY when HTF60 slightly aligned

### L23.  `ZS=ZS1 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=97  W=26/L=71  WR=26.8%
- Sharpen: sharpest is H60=H60b (13/71 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  zscore -3 to -2 deep oversold; session=london_open  •  ONLY when HTF60 slightly aligned

### L24.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=97  W=26/L=71  WR=26.8%
- Sharpen: sharpest is H60=H60b (13/71 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london_open  •  ONLY when HTF60 slightly aligned

### L25.  `T1=T1c AND ZS=ZS1 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=97  W=26/L=71  WR=26.8%
- Sharpen: sharpest is H60=H60b (13/71 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london_open  •  ONLY when HTF60 slightly aligned

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(55/44) | T1c(45/56) |
| T4 | T4a(54/44) | T4c(46/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(55/44) | long(45/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
