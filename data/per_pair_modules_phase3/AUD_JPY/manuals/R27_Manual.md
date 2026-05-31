# AUD_JPY — R27 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,151**  (W=2,628 / L=1,523)  -  WR: **63.3%**

## Session distribution

- asia: n=1412  W=883/L=529  WR=62.5%
- ny_close: n=749  W=459/L=290  WR=61.3%
- london_open: n=602  W=400/L=202  WR=66.4%
- london: n=393  W=256/L=137  WR=65.1%
- ny_open: n=374  W=227/L=147  WR=60.7%
- ny_mid: n=278  W=178/L=100  WR=64.0%
- off_hours: n=183  W=113/L=70  WR=61.7%
- asia_late: n=160  W=112/L=48  WR=70.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=119  W=103/L=16  WR=86.6%
- Refine: exclude BBP=BBP6 drops 9/16 losers (56%)
- **Final: n=108  W=101/L=7  WR=93.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when deep above upper band

### W02.  `T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=119  W=103/L=16  WR=86.6%
- Refine: exclude BBP=BBP6 drops 9/16 losers (56%)
- **Final: n=108  W=101/L=7  WR=93.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=asia  •  AVOID when deep above upper band

### W03.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=119  W=103/L=16  WR=86.6%
- Refine: exclude BBP=BBP6 drops 9/16 losers (56%)
- **Final: n=108  W=101/L=7  WR=93.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when deep above upper band

### W04.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=119  W=103/L=16  WR=86.6%
- Refine: exclude BBP=BBP6 drops 9/16 losers (56%)
- **Final: n=108  W=101/L=7  WR=93.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when deep above upper band

### W05.  `T1=T1c AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=119  W=103/L=16  WR=86.6%
- Refine: exclude BBP=BBP6 drops 9/16 losers (56%)
- **Final: n=108  W=101/L=7  WR=93.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when deep above upper band

### W06.  `H60=H60a AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=109  W=97/L=12  WR=89.0%
- Refine: exclude BBP=BBP6 drops 9/12 losers (75%)
- **Final: n=98  W=95/L=3  WR=96.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when deep above upper band

### W07.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=109  W=97/L=12  WR=89.0%
- Refine: exclude BBP=BBP6 drops 9/12 losers (75%)
- **Final: n=98  W=95/L=3  WR=96.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when deep above upper band

### W08.  `H60=H60a AND T1=T1a AND session_bucket=asia_late`
- Raw: n=101  W=91/L=10  WR=90.1%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia_late  •  AVOID when RSI 50-60 upper neutral

### W09.  `H60=H60a AND T4=T4a AND session_bucket=asia_late`
- Raw: n=101  W=91/L=10  WR=90.1%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia_late  •  AVOID when RSI 50-60 upper neutral

### W10.  `H60=H60a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=101  W=91/L=10  WR=90.1%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=asia_late  •  AVOID when RSI 50-60 upper neutral

### W11.  `T1=T1a AND T4=T4a AND session_bucket=asia_late`
- Raw: n=101  W=91/L=10  WR=90.1%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=asia_late  •  AVOID when RSI 50-60 upper neutral

### W12.  `T1=T1a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=101  W=91/L=10  WR=90.1%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=asia_late  •  AVOID when RSI 50-60 upper neutral

### W13.  `T4=T4a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=101  W=91/L=10  WR=90.1%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=asia_late  •  AVOID when RSI 50-60 upper neutral

### W14.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=asia_late`
- Raw: n=101  W=91/L=10  WR=90.1%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia_late  •  AVOID when RSI 50-60 upper neutral

### W15.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=101  W=91/L=10  WR=90.1%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia_late  •  AVOID when RSI 50-60 upper neutral

### W16.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=101  W=91/L=10  WR=90.1%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia_late  •  AVOID when RSI 50-60 upper neutral

### W17.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=101  W=91/L=10  WR=90.1%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=asia_late  •  AVOID when RSI 50-60 upper neutral

### W18.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=london`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude T1=T1c drops 9/13 losers (69%)
- **Final: n=76  W=72/L=4  WR=94.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=london  •  AVOID when 1h trend AGAINST trade

### W19.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude T1=T1c drops 9/13 losers (69%)
- **Final: n=76  W=72/L=4  WR=94.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london  •  AVOID when 1h trend AGAINST trade

### W20.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=94  W=85/L=9  WR=90.4%
- Refine: exclude session_bucket=asia_late drops 4/9 losers (44%)
- **Final: n=86  W=81/L=5  WR=94.2%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=asia_late

### W21.  `H60=H60e AND T1=T1a AND session_bucket=london`
- Raw: n=76  W=72/L=4  WR=94.7%
- Refine: exclude BBP=BBP2 drops 3/4 losers (75%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when lower third

### W22.  `T1=T1a AND direction_exec=short AND session_bucket=london`
- Raw: n=76  W=72/L=4  WR=94.7%
- Refine: exclude BBP=BBP2 drops 3/4 losers (75%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london  •  AVOID when lower third

### W23.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=london`
- Raw: n=76  W=72/L=4  WR=94.7%
- Refine: exclude BBP=BBP2 drops 3/4 losers (75%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when lower third

### W24.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=london`
- Raw: n=76  W=72/L=4  WR=94.7%
- Refine: exclude BBP=BBP2 drops 3/4 losers (75%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=london  •  AVOID when lower third

### W25.  `H60=H60e AND T1=T1a AND T4=T4c AND session_bucket=london`
- Raw: n=76  W=72/L=4  WR=94.7%
- Refine: exclude BBP=BBP2 drops 3/4 losers (75%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when lower third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=154  W=59/L=95  WR=38.3%
- Sharpen: sharpest is T4=T4a (20/95 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L02.  `BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=154  W=59/L=95  WR=38.3%
- Sharpen: sharpest is T4=T4a (20/95 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L03.  `H60=H60e AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=154  W=59/L=95  WR=38.3%
- Sharpen: sharpest is T4=T4a (20/95 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L04.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=145  W=52/L=93  WR=35.9%
- Sharpen: sharpest is session_bucket=asia (38/93 of losers there)
- **Sharp: n=46  W=8/L=38  WR=17.4%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L05.  `H60=H60e AND T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=134  W=50/L=84  WR=37.3%
- Sharpen: sharpest is session_bucket=asia (29/84 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L06.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=134  W=50/L=84  WR=37.3%
- Sharpen: sharpest is session_bucket=asia (29/84 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L07.  `H20=H20e AND T1=T1c AND BBP=BBP6`
- Raw: n=129  W=51/L=78  WR=39.5%
- Sharpen: sharpest is RSI=RSI5 (28/78 of losers there)
- **Sharp: n=35  W=7/L=28  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L08.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP6`
- Raw: n=129  W=51/L=78  WR=39.5%
- Sharpen: sharpest is RSI=RSI5 (28/78 of losers there)
- **Sharp: n=35  W=7/L=28  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L09.  `H20=H20e AND T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=129  W=51/L=78  WR=39.5%
- Sharpen: sharpest is RSI=RSI5 (28/78 of losers there)
- **Sharp: n=35  W=7/L=28  WR=20.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L10.  `H20=H20e AND H60=H60e AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=118  W=42/L=76  WR=35.6%
- Sharpen: sharpest is T4=T4a (20/76 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L11.  `H20=H20e AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=118  W=42/L=76  WR=35.6%
- Sharpen: sharpest is T4=T4a (20/76 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  HTF20 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L12.  `H20=H20e AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=114  W=45/L=69  WR=39.5%
- Sharpen: sharpest is T4=T4a (30/69 of losers there)
- **Sharp: n=36  W=6/L=30  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; zscore +2 to +3 deep overbought; session=asia  •  ONLY when 4h trend WITH trade

### L13.  `H60=H60e AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=109  W=42/L=67  WR=38.5%
- Sharpen: sharpest is ZS=ZS5 (39/67 of losers there)
- **Sharp: n=49  W=10/L=39  WR=20.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L14.  `T1=T1c AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=109  W=42/L=67  WR=38.5%
- Sharpen: sharpest is ZS=ZS5 (39/67 of losers there)
- **Sharp: n=49  W=10/L=39  WR=20.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L15.  `T1=T1a AND BBP=BBP4 AND ZS=ZS3`
- Raw: n=106  W=41/L=65  WR=38.7%
- Sharpen: sharpest is RSI=RSI4 (52/65 of losers there)
- **Sharp: n=75  W=23/L=52  WR=30.7%**
- **Dir: ?**  •  1h trend WITH trade; upper third; zscore -1 to +1 neutral  •  ONLY when RSI 50-60 upper neutral

### L16.  `H20=H20e AND H60=H60e AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=103  W=40/L=63  WR=38.8%
- Sharpen: sharpest is T4=T4a (30/63 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +2 to +3 deep overbought; session=asia  •  ONLY when 4h trend WITH trade

### L17.  `H20=H20e AND ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=103  W=40/L=63  WR=38.8%
- Sharpen: sharpest is T4=T4a (30/63 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore +2 to +3 deep overbought; session=asia  •  ONLY when 4h trend WITH trade

### L18.  `H20=H20e AND T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=98  W=33/L=65  WR=33.7%
- Sharpen: sharpest is session_bucket=asia (29/65 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L19.  `H60=H60a AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is BBP=BBP4 (27/53 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=off_hours  •  ONLY when upper third

### L20.  `H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=83  W=28/L=55  WR=33.7%
- Sharpen: sharpest is T4=T4c (52/55 of losers there)
- **Sharp: n=66  W=14/L=52  WR=21.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=asia  •  ONLY when 4h trend AGAINST trade

### L21.  `T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=83  W=28/L=55  WR=33.7%
- Sharpen: sharpest is T4=T4c (52/55 of losers there)
- **Sharp: n=66  W=14/L=52  WR=21.2%**
- **Dir: SHORT**  •  1h trend WITH trade; session=asia  •  ONLY when 4h trend AGAINST trade

### L22.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=83  W=28/L=55  WR=33.7%
- Sharpen: sharpest is T4=T4c (52/55 of losers there)
- **Sharp: n=66  W=14/L=52  WR=21.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend AGAINST trade

### L23.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=83  W=28/L=55  WR=33.7%
- Sharpen: sharpest is T4=T4c (52/55 of losers there)
- **Sharp: n=66  W=14/L=52  WR=21.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=asia  •  ONLY when 4h trend AGAINST trade

### L24.  `T1=T1a AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=83  W=28/L=55  WR=33.7%
- Sharpen: sharpest is T4=T4c (52/55 of losers there)
- **Sharp: n=66  W=14/L=52  WR=21.2%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend AGAINST trade

### L25.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND ZS=ZS3`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is RSI=RSI4 (39/50 of losers there)
- **Sharp: n=59  W=20/L=39  WR=33.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; zscore -1 to +1 neutral  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(52/47) | H60e(48/53) |
| T1 | T1a(52/47) | T1c(48/53) |
| T4 | T4a(54/47) | T4c(46/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(52/47) | short(48/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
