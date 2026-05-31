# EUR_AUD — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,193**  (W=2,610 / L=1,583)  -  WR: **62.2%**

## Session distribution

- asia: n=967  W=575/L=392  WR=59.5%
- ny_mid: n=915  W=590/L=325  WR=64.5%
- london_open: n=847  W=532/L=315  WR=62.8%
- ny_open: n=644  W=406/L=238  WR=63.0%
- ny_close: n=324  W=208/L=116  WR=64.2%
- london: n=306  W=184/L=122  WR=60.1%
- asia_late: n=169  W=108/L=61  WR=63.9%
- off_hours: n=21  W=7/L=14  WR=33.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=188  W=163/L=25  WR=86.7%
- Refine: exclude ZS=ZS1 drops 17/25 losers (68%)
- **Final: n=135  W=127/L=8  WR=94.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when zscore -3 to -2 deep oversold

### W02.  `H20=H20a AND T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=188  W=163/L=25  WR=86.7%
- Refine: exclude ZS=ZS1 drops 17/25 losers (68%)
- **Final: n=135  W=127/L=8  WR=94.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when zscore -3 to -2 deep oversold

### W03.  `BBP=BBP2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=171  W=148/L=23  WR=86.5%
- Refine: exclude RSI=RSI4 drops 10/23 losers (43%)
- **Final: n=161  W=148/L=13  WR=91.9%**
- **Dir: SHORT**  •  lower third; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W04.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=171  W=146/L=25  WR=85.4%
- Refine: exclude ZS=ZS1 drops 17/25 losers (68%)
- **Final: n=119  W=111/L=8  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when zscore -3 to -2 deep oversold

### W05.  `H20=H20a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=165  W=141/L=24  WR=85.5%
- Refine: exclude T1=T1c drops 21/24 losers (88%)
- **Final: n=103  W=100/L=3  WR=97.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W06.  `H60=H60a AND T4=T4a AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=162  W=138/L=24  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 14/24 losers (58%)
- **Final: n=109  W=99/L=10  WR=90.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; just touched lower band; RSI 30-40 weak  •  AVOID when session=ny_mid

### W07.  `ZS=ZS2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=159  W=140/L=19  WR=88.1%
- Refine: exclude T1=T1c drops 11/19 losers (58%)
- **Final: n=112  W=104/L=8  WR=92.9%**
- **Dir: SHORT**  •  zscore -2 to -1 oversold; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W08.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=159  W=140/L=19  WR=88.1%
- Refine: exclude T1=T1c drops 11/19 losers (58%)
- **Final: n=112  W=104/L=8  WR=92.9%**
- **Dir: SHORT**  •  lower third; zscore -2 to -1 oversold; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W09.  `H20=H20a AND BBP=BBP2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=154  W=136/L=18  WR=88.3%
- Refine: exclude T1=T1c drops 15/18 losers (83%)
- **Final: n=103  W=100/L=3  WR=97.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; lower third; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W10.  `H20=H20a AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=153  W=133/L=20  WR=86.9%
- Refine: exclude T1=T1c drops 17/20 losers (85%)
- **Final: n=95  W=92/L=3  WR=96.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -2 to -1 oversold; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W11.  `H20=H20a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=153  W=133/L=20  WR=86.9%
- Refine: exclude T1=T1c drops 17/20 losers (85%)
- **Final: n=95  W=92/L=3  WR=96.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; zscore -2 to -1 oversold; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W12.  `H60=H60a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=146  W=128/L=18  WR=87.7%
- Refine: exclude RSI=RSI4 drops 10/18 losers (56%)
- **Final: n=136  W=128/L=8  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W13.  `H60=H60a AND BBP=BBP2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=146  W=128/L=18  WR=87.7%
- Refine: exclude RSI=RSI4 drops 10/18 losers (56%)
- **Final: n=136  W=128/L=8  WR=94.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; lower third; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W14.  `H20=H20a AND ZS=ZS2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=142  W=128/L=14  WR=90.1%
- Refine: exclude T1=T1c drops 11/14 losers (79%)
- **Final: n=95  W=92/L=3  WR=96.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore -2 to -1 oversold; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W15.  `H20=H20a AND H60=H60a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=140  W=122/L=18  WR=87.1%
- Refine: exclude RSI=RSI4 drops 10/18 losers (56%)
- **Final: n=130  W=122/L=8  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W16.  `H60=H60a AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=134  W=120/L=14  WR=89.6%
- Refine: exclude T1=T1c drops 11/14 losers (79%)
- **Final: n=87  W=84/L=3  WR=96.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W17.  `H60=H60a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=134  W=120/L=14  WR=89.6%
- Refine: exclude T1=T1c drops 11/14 losers (79%)
- **Final: n=87  W=84/L=3  WR=96.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; zscore -2 to -1 oversold; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W18.  `H60=H60a AND ZS=ZS2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=134  W=120/L=14  WR=89.6%
- Refine: exclude T1=T1c drops 11/14 losers (79%)
- **Final: n=87  W=84/L=3  WR=96.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W19.  `H20=H20a AND H60=H60a AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=128  W=114/L=14  WR=89.1%
- Refine: exclude T1=T1c drops 11/14 losers (79%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W20.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude BBP=BBP1 drops 9/9 losers (100%)
- **Final: n=90  W=90/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when just touched lower band

### W21.  `T1=T1a AND BBP=BBP2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=120  W=112/L=8  WR=93.3%
- Refine: exclude H60=H60b drops 5/8 losers (62%)
- **Final: n=109  W=106/L=3  WR=97.2%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; session=ny_open  •  AVOID when HTF60 slightly aligned

### W22.  `T1=T1a AND ZS=ZS2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=112  W=104/L=8  WR=92.9%
- Refine: exclude H60=H60b drops 5/8 losers (62%)
- **Final: n=101  W=98/L=3  WR=97.0%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=ny_open  •  AVOID when HTF60 slightly aligned

### W23.  `T4=T4a AND BBP=BBP2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=104  W=94/L=10  WR=90.4%
- Refine: exclude H60=H60b drops 5/10 losers (50%)
- **Final: n=93  W=88/L=5  WR=94.6%**
- **Dir: SHORT**  •  4h trend WITH trade; lower third; session=ny_open  •  AVOID when HTF60 slightly aligned

### W24.  `H20=H20a AND T1=T1a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=103  W=100/L=3  WR=97.1%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W25.  `T4=T4a AND ZS=ZS2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=102  W=92/L=10  WR=90.2%
- Refine: exclude H60=H60b drops 5/10 losers (50%)
- **Final: n=91  W=86/L=5  WR=94.5%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -2 to -1 oversold; session=ny_open  •  AVOID when HTF60 slightly aligned

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=149  W=58/L=91  WR=38.9%
- Sharpen: sharpest is RSI=RSI2 (40/91 of losers there)
- **Sharp: n=47  W=7/L=40  WR=14.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L02.  `H20=H20e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=142  W=48/L=94  WR=33.8%
- Sharpen: sharpest is BBP=BBP2 (52/94 of losers there)
- **Sharp: n=60  W=8/L=52  WR=13.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when lower third

### L03.  `H20=H20e AND T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=142  W=48/L=94  WR=33.8%
- Sharpen: sharpest is BBP=BBP2 (52/94 of losers there)
- **Sharp: n=60  W=8/L=52  WR=13.3%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when lower third

### L04.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=129  W=46/L=83  WR=35.7%
- Sharpen: sharpest is BBP=BBP2 (44/83 of losers there)
- **Sharp: n=52  W=8/L=44  WR=15.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when lower third

### L05.  `BBP=BBP2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is T1=T1c (58/77 of losers there)
- **Sharp: n=71  W=13/L=58  WR=18.3%**
- **Dir: LONG**  •  lower third; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L06.  `H20=H20e AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=115  W=44/L=71  WR=38.3%
- Sharpen: sharpest is T1=T1c (52/71 of losers there)
- **Sharp: n=60  W=8/L=52  WR=13.3%**
- **Dir: LONG**  •  HTF20 strongly against; lower third; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L07.  `ZS=ZS2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=110  W=41/L=69  WR=37.3%
- Sharpen: sharpest is T1=T1c (51/69 of losers there)
- **Sharp: n=64  W=13/L=51  WR=20.3%**
- **Dir: LONG**  •  zscore -2 to -1 oversold; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L08.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=110  W=41/L=69  WR=37.3%
- Sharpen: sharpest is T1=T1c (51/69 of losers there)
- **Sharp: n=64  W=13/L=51  WR=20.3%**
- **Dir: LONG**  •  lower third; zscore -2 to -1 oversold; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L09.  `H60=H60e AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=110  W=44/L=66  WR=40.0%
- Sharpen: sharpest is T1=T1c (47/66 of losers there)
- **Sharp: n=55  W=8/L=47  WR=14.5%**
- **Dir: ?**  •  HTF60 strongly against; lower third; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L10.  `H60=H60e AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=110  W=44/L=66  WR=40.0%
- Sharpen: sharpest is T1=T1c (47/66 of losers there)
- **Sharp: n=55  W=8/L=47  WR=14.5%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L11.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=103  W=41/L=62  WR=39.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; session=ny_mid

### L12.  `H20=H20e AND ZS=ZS2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=99  W=36/L=63  WR=36.4%
- Sharpen: sharpest is T1=T1c (45/63 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: LONG**  •  HTF20 strongly against; zscore -2 to -1 oversold; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L13.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=98  W=27/L=71  WR=27.6%
- Sharpen: sharpest is RSI=RSI2 (21/71 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L14.  `H60=H60e AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=94  W=36/L=58  WR=38.3%
- Sharpen: sharpest is T1=T1c (40/58 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; zscore -2 to -1 oversold; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L15.  `H60=H60e AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=94  W=36/L=58  WR=38.3%
- Sharpen: sharpest is T1=T1c (40/58 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; lower third; zscore -2 to -1 oversold; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L16.  `H60=H60e AND ZS=ZS2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=94  W=36/L=58  WR=38.3%
- Sharpen: sharpest is T1=T1c (40/58 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: LONG**  •  HTF60 strongly against; zscore -2 to -1 oversold; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L17.  `T4=T4a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=93  W=29/L=64  WR=31.2%
- Sharpen: sharpest is session_bucket=london_open (17/64 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; RSI 50-60 upper neutral  •  ONLY when session=london_open

### L18.  `BBP=BBP5 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=93  W=29/L=64  WR=31.2%
- Sharpen: sharpest is session_bucket=london_open (17/64 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: SHORT**  •  just touched upper band; RSI 50-60 upper neutral  •  ONLY when session=london_open

### L19.  `T4=T4a AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=93  W=29/L=64  WR=31.2%
- Sharpen: sharpest is session_bucket=london_open (17/64 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L20.  `T4=T4a AND BBP=BBP5 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=93  W=29/L=64  WR=31.2%
- Sharpen: sharpest is session_bucket=london_open (17/64 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: SHORT**  •  4h trend WITH trade; just touched upper band; RSI 50-60 upper neutral  •  ONLY when session=london_open

### L21.  `BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=93  W=29/L=64  WR=31.2%
- Sharpen: sharpest is session_bucket=london_open (17/64 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: SHORT**  •  just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L22.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is H20=H20a (47/56 of losers there)
- **Sharp: n=65  W=18/L=47  WR=27.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 aligned WITH trade

### L23.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is H20=H20a (47/56 of losers there)
- **Sharp: n=65  W=18/L=47  WR=27.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 aligned WITH trade

### L24.  `T1=T1a AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is H20=H20a (47/56 of losers there)
- **Sharp: n=65  W=18/L=47  WR=27.7%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 aligned WITH trade

### L25.  `H20=H20e AND H60=H60e AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=91  W=36/L=55  WR=39.6%
- Sharpen: sharpest is T1=T1c (37/55 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore -2 to -1 oversold; session=ny_open  •  ONLY when 1h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(53/46) | H20e(45/52) |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(53/47) | T4c(47/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
