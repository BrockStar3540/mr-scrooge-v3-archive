# CAD_JPY — R36 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,845**  (W=1,163 / L=682)  -  WR: **63.0%**

## Session distribution

- asia: n=764  W=481/L=283  WR=63.0%
- london_open: n=340  W=223/L=117  WR=65.6%
- asia_late: n=198  W=129/L=69  WR=65.2%
- london: n=193  W=121/L=72  WR=62.7%
- ny_open: n=187  W=111/L=76  WR=59.4%
- off_hours: n=79  W=48/L=31  WR=60.8%
- ny_mid: n=49  W=27/L=22  WR=55.1%
- ny_close: n=35  W=23/L=12  WR=65.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T4=T4a AND RSI=RSI2`
- Raw: n=120  W=105/L=15  WR=87.5%
- Refine: exclude session_bucket=ny_open drops 5/15 losers (33%)
- **Final: n=107  W=97/L=10  WR=90.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=ny_open

### W02.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI2`
- Raw: n=118  W=105/L=13  WR=89.0%
- Refine: exclude BBP=BBP2 drops 5/13 losers (38%)
- **Final: n=97  W=89/L=8  WR=91.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when lower third

### W03.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=118  W=105/L=13  WR=89.0%
- Refine: exclude BBP=BBP2 drops 5/13 losers (38%)
- **Final: n=97  W=89/L=8  WR=91.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when lower third

### W04.  `H20=H20e AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=118  W=105/L=13  WR=89.0%
- Refine: exclude BBP=BBP2 drops 5/13 losers (38%)
- **Final: n=97  W=89/L=8  WR=91.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when lower third

### W05.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude T1=T1a drops 9/13 losers (69%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend WITH trade

### W06.  `T4=T4c AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude T1=T1a drops 9/13 losers (69%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend WITH trade

### W07.  `H60=H60a AND direction_exec=long AND session_bucket=london`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude ZS=ZS4 drops 8/13 losers (62%)
- **Final: n=51  W=46/L=5  WR=90.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=london  •  AVOID when zscore +1 to +2 overbought

### W08.  `H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude session_bucket=asia drops 12/12 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when session=asia

### W09.  `H60=H60a AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude session_bucket=asia drops 12/12 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when session=asia

### W10.  `T4=T4a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude session_bucket=asia drops 8/9 losers (89%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W11.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=82  W=75/L=7  WR=91.5%
- Refine: exclude BBP=BBP1 drops 4/7 losers (57%)
- **Final: n=74  W=71/L=3  WR=95.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when just touched lower band

### W12.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=82  W=75/L=7  WR=91.5%
- Refine: exclude BBP=BBP1 drops 4/7 losers (57%)
- **Final: n=74  W=71/L=3  WR=95.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when just touched lower band

### W13.  `H60=H60a AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude session_bucket=asia drops 10/10 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W14.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude session_bucket=asia drops 8/9 losers (89%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W15.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude session_bucket=asia drops 8/9 losers (89%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W16.  `T4=T4a AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude session_bucket=asia drops 8/9 losers (89%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W17.  `H20=H20a AND T4=T4c AND session_bucket=asia_late`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude BBP=BBP2 drops 7/10 losers (70%)
- **Final: n=34  W=31/L=3  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia_late  •  AVOID when lower third

### W18.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude BBP=BBP2 drops 7/10 losers (70%)
- **Final: n=34  W=31/L=3  WR=91.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia_late  •  AVOID when lower third

### W19.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=asia_late`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude BBP=BBP2 drops 7/9 losers (78%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia_late  •  AVOID when lower third

### W20.  `H20=H20e AND T4=T4a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=62  W=56/L=6  WR=90.3%
- Refine: exclude session_bucket=asia drops 5/6 losers (83%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W21.  `T1=T1c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude BBP=BBP0 drops 8/9 losers (89%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W22.  `H20=H20a AND H60=H60a AND session_bucket=london`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude T4=T4c drops 6/7 losers (86%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london  •  AVOID when 4h trend AGAINST trade

### W23.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=london`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude T4=T4c drops 6/7 losers (86%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london  •  AVOID when 4h trend AGAINST trade

### W24.  `T4=T4a AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=60  W=52/L=8  WR=86.7%
- Refine: exclude session_bucket=asia drops 7/8 losers (88%)
- **Final: n=32  W=31/L=1  WR=96.9%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; RSI 30-40 weak  •  AVOID when session=asia

### W25.  `T4=T4a AND BBP=BBP1 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=60  W=52/L=8  WR=86.7%
- Refine: exclude session_bucket=asia drops 7/8 losers (88%)
- **Final: n=32  W=31/L=1  WR=96.9%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T4=T4c AND RSI=RSI2`
- Raw: n=87  W=23/L=64  WR=26.4%
- Sharpen: sharpest is session_bucket=london_open (24/64 of losers there)
- **Sharp: n=25  W=1/L=24  WR=4.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L02.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI2`
- Raw: n=82  W=20/L=62  WR=24.4%
- Sharpen: sharpest is session_bucket=london_open (24/62 of losers there)
- **Sharp: n=25  W=1/L=24  WR=4.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L03.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=82  W=20/L=62  WR=24.4%
- Sharpen: sharpest is session_bucket=london_open (24/62 of losers there)
- **Sharp: n=25  W=1/L=24  WR=4.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L04.  `H20=H20a AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=82  W=20/L=62  WR=24.4%
- Sharpen: sharpest is session_bucket=london_open (24/62 of losers there)
- **Sharp: n=25  W=1/L=24  WR=4.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L05.  `H60=H60e AND direction_exec=short AND session_bucket=london`
- Raw: n=74  W=27/L=47  WR=36.5%
- Sharpen: sharpest is T4=T4c (31/47 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london  •  ONLY when 4h trend AGAINST trade

### L06.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=71  W=24/L=47  WR=33.8%
- Sharpen: sharpest is H20=H20a (29/47 of losers there)
- **Sharp: n=39  W=10/L=29  WR=25.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 aligned WITH trade

### L07.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=71  W=24/L=47  WR=33.8%
- Sharpen: sharpest is H20=H20a (29/47 of losers there)
- **Sharp: n=39  W=10/L=29  WR=25.6%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 aligned WITH trade

### L08.  `T1=T1a AND direction_exec=short AND session_bucket=london`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is T4=T4c (31/43 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london  •  ONLY when 4h trend AGAINST trade

### L09.  `H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=69  W=16/L=53  WR=23.2%
- Sharpen: sharpest is RSI=RSI4 (28/53 of losers there)
- **Sharp: n=31  W=3/L=28  WR=9.7%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_open  •  ONLY when RSI 50-60 upper neutral

### L10.  `H60=H60e AND T1=T1a AND session_bucket=london`
- Raw: n=63  W=23/L=40  WR=36.5%
- Sharpen: sharpest is T4=T4c (31/40 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=london  •  ONLY when 4h trend AGAINST trade

### L11.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=london`
- Raw: n=63  W=23/L=40  WR=36.5%
- Sharpen: sharpest is T4=T4c (31/40 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=london  •  ONLY when 4h trend AGAINST trade

### L12.  `H60=H60e AND T4=T4a AND session_bucket=asia_late`
- Raw: n=63  W=24/L=39  WR=38.1%
- Sharpen: sharpest is H20=H20e (31/39 of losers there)
- **Sharp: n=41  W=10/L=31  WR=24.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=asia_late  •  ONLY when HTF20 strongly against

### L13.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=63  W=24/L=39  WR=38.1%
- Sharpen: sharpest is H20=H20e (31/39 of losers there)
- **Sharp: n=41  W=10/L=31  WR=24.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=asia_late  •  ONLY when HTF20 strongly against

### L14.  `H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=55  W=16/L=39  WR=29.1%
- Sharpen: sharpest is RSI=RSI4 (31/39 of losers there)
- **Sharp: n=40  W=9/L=31  WR=22.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L15.  `H60=H60e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=55  W=16/L=39  WR=29.1%
- Sharpen: sharpest is RSI=RSI4 (31/39 of losers there)
- **Sharp: n=40  W=9/L=31  WR=22.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L16.  `T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=55  W=19/L=36  WR=34.5%
- Sharpen: sharpest is H20=H20a (25/36 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when HTF20 aligned WITH trade

### L17.  `H60=H60a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is T4=T4c (18/33 of losers there)
- **Sharp: n=26  W=8/L=18  WR=30.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=asia  •  ONLY when 4h trend AGAINST trade

### L18.  `ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is T4=T4c (18/33 of losers there)
- **Sharp: n=26  W=8/L=18  WR=30.8%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=asia  •  ONLY when 4h trend AGAINST trade

### L19.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI4`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (29/33 of losers there)
- **Sharp: n=39  W=10/L=29  WR=25.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L20.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (29/33 of losers there)
- **Sharp: n=39  W=10/L=29  WR=25.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L21.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is T4=T4c (18/33 of losers there)
- **Sharp: n=26  W=8/L=18  WR=30.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when 4h trend AGAINST trade

### L22.  `H60=H60a AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is T4=T4c (18/33 of losers there)
- **Sharp: n=26  W=8/L=18  WR=30.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=asia  •  ONLY when 4h trend AGAINST trade

### L23.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is T4=T4c (18/33 of losers there)
- **Sharp: n=26  W=8/L=18  WR=30.8%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when 4h trend AGAINST trade

### L24.  `H60=H60a AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=51  W=20/L=31  WR=39.2%
- Sharpen: sharpest is T4=T4a (17/31 of losers there)
- **Sharp: n=24  W=7/L=17  WR=29.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; session=asia  •  ONLY when 4h trend WITH trade

### L25.  `BBP=BBP0 AND direction_exec=long AND session_bucket=asia`
- Raw: n=51  W=20/L=31  WR=39.2%
- Sharpen: sharpest is T4=T4a (17/31 of losers there)
- **Sharp: n=24  W=7/L=17  WR=29.2%**
- **Dir: LONG**  •  deep below lower band; session=asia  •  ONLY when 4h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(45/38) | H20a(37/46) |
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
