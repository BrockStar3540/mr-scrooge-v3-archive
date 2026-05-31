# AUD_NZD — R29 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,588**  (W=1,042 / L=546)  -  WR: **65.6%**

## Session distribution

- asia: n=585  W=376/L=209  WR=64.3%
- london_open: n=350  W=236/L=114  WR=67.4%
- ny_mid: n=255  W=164/L=91  WR=64.3%
- london: n=163  W=116/L=47  WR=71.2%
- ny_open: n=104  W=64/L=40  WR=61.5%
- asia_late: n=65  W=42/L=23  WR=64.6%
- ny_close: n=59  W=40/L=19  WR=67.8%
- off_hours: n=7  W=4/L=3  WR=57.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=159  W=140/L=19  WR=88.1%
- Refine: exclude T4=T4a drops 11/19 losers (58%)
- **Final: n=114  W=106/L=8  WR=93.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third  •  AVOID when 4h trend WITH trade

### W02.  `H60=H60a AND T1=T1c AND BBP=BBP4`
- Raw: n=138  W=120/L=18  WR=87.0%
- Refine: exclude T4=T4a drops 10/18 losers (56%)
- **Final: n=102  W=94/L=8  WR=92.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third  •  AVOID when 4h trend WITH trade

### W03.  `T1=T1c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=138  W=120/L=18  WR=87.0%
- Refine: exclude T4=T4a drops 10/18 losers (56%)
- **Final: n=102  W=94/L=8  WR=92.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third  •  AVOID when 4h trend WITH trade

### W04.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=138  W=120/L=18  WR=87.0%
- Refine: exclude T4=T4a drops 10/18 losers (56%)
- **Final: n=102  W=94/L=8  WR=92.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third  •  AVOID when 4h trend WITH trade

### W05.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=127  W=112/L=15  WR=88.2%
- Refine: exclude T4=T4a drops 7/15 losers (47%)
- **Final: n=90  W=82/L=8  WR=91.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when 4h trend WITH trade

### W06.  `H60=H60a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=127  W=112/L=15  WR=88.2%
- Refine: exclude T4=T4a drops 7/15 losers (47%)
- **Final: n=90  W=82/L=8  WR=91.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when 4h trend WITH trade

### W07.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=127  W=112/L=15  WR=88.2%
- Refine: exclude T4=T4a drops 7/15 losers (47%)
- **Final: n=90  W=82/L=8  WR=91.1%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought  •  AVOID when 4h trend WITH trade

### W08.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=127  W=112/L=15  WR=88.2%
- Refine: exclude T4=T4a drops 7/15 losers (47%)
- **Final: n=90  W=82/L=8  WR=91.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when 4h trend WITH trade

### W09.  `H60=H60a AND T4=T4c AND BBP=BBP4`
- Raw: n=114  W=106/L=8  WR=93.0%
- Refine: exclude H20=H20b drops 5/8 losers (62%)
- **Final: n=82  W=79/L=3  WR=96.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when HTF20 slightly aligned

### W10.  `T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=114  W=106/L=8  WR=93.0%
- Refine: exclude H20=H20b drops 5/8 losers (62%)
- **Final: n=82  W=79/L=3  WR=96.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third  •  AVOID when HTF20 slightly aligned

### W11.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=114  W=106/L=8  WR=93.0%
- Refine: exclude H20=H20b drops 5/8 losers (62%)
- **Final: n=82  W=79/L=3  WR=96.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when HTF20 slightly aligned

### W12.  `T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=108  W=96/L=12  WR=88.9%
- Refine: exclude H20=H20e drops 4/12 losers (33%)
- **Final: n=102  W=94/L=8  WR=92.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  AVOID when HTF20 strongly against

### W13.  `H60=H60a AND T1=T1c AND ZS=ZS4`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude H20=H20b drops 5/14 losers (36%)
- **Final: n=90  W=81/L=9  WR=90.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W14.  `T1=T1c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude H20=H20b drops 5/14 losers (36%)
- **Final: n=90  W=81/L=9  WR=90.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W15.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude H20=H20b drops 5/14 losers (36%)
- **Final: n=90  W=81/L=9  WR=90.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W16.  `H60=H60a AND T1=T1c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude H20=H20b drops 5/14 losers (36%)
- **Final: n=90  W=81/L=9  WR=90.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W17.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude H20=H20b drops 5/14 losers (36%)
- **Final: n=90  W=81/L=9  WR=90.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W18.  `H60=H60a AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=102  W=94/L=8  WR=92.2%
- Refine: exclude H20=H20b drops 5/8 losers (62%)
- **Final: n=82  W=79/L=3  WR=96.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  AVOID when HTF20 slightly aligned

### W19.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=102  W=94/L=8  WR=92.2%
- Refine: exclude H20=H20b drops 5/8 losers (62%)
- **Final: n=82  W=79/L=3  WR=96.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  AVOID when HTF20 slightly aligned

### W20.  `H60=H60a AND T4=T4c AND ZS=ZS4`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude RSI=RSI2 drops 6/8 losers (75%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when RSI 30-40 weak

### W21.  `T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude RSI=RSI2 drops 6/8 losers (75%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when RSI 30-40 weak

### W22.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude RSI=RSI2 drops 6/8 losers (75%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 30-40 weak

### W23.  `H60=H60a AND T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude RSI=RSI2 drops 6/8 losers (75%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when RSI 30-40 weak

### W24.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude RSI=RSI2 drops 6/8 losers (75%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 30-40 weak

### W25.  `T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude H20=H20e drops 4/12 losers (33%)
- **Final: n=78  W=70/L=8  WR=89.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND BBP=BBP4 AND direction_exec=short`
- Raw: n=107  W=37/L=70  WR=34.6%
- Sharpen: sharpest is T4=T4a (51/70 of losers there)
- **Sharp: n=69  W=18/L=51  WR=26.1%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third  •  ONLY when 4h trend WITH trade

### L02.  `H60=H60e AND T1=T1a AND BBP=BBP4`
- Raw: n=94  W=35/L=59  WR=37.2%
- Sharpen: sharpest is T4=T4a (44/59 of losers there)
- **Sharp: n=62  W=18/L=44  WR=29.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third  •  ONLY when 4h trend WITH trade

### L03.  `T1=T1a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=94  W=35/L=59  WR=37.2%
- Sharpen: sharpest is T4=T4a (44/59 of losers there)
- **Sharp: n=62  W=18/L=44  WR=29.0%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third  •  ONLY when 4h trend WITH trade

### L04.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=94  W=35/L=59  WR=37.2%
- Sharpen: sharpest is T4=T4a (44/59 of losers there)
- **Sharp: n=62  W=18/L=44  WR=29.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; upper third  •  ONLY when 4h trend WITH trade

### L05.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=86  W=30/L=56  WR=34.9%
- Sharpen: sharpest is RSI=RSI3 (28/56 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 40-50 lower neutral

### L06.  `H60=H60e AND ZS=ZS4 AND direction_exec=short`
- Raw: n=86  W=30/L=56  WR=34.9%
- Sharpen: sharpest is RSI=RSI3 (28/56 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +1 to +2 overbought  •  ONLY when RSI 40-50 lower neutral

### L07.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=86  W=30/L=56  WR=34.9%
- Sharpen: sharpest is RSI=RSI3 (28/56 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: SHORT**  •  upper third; zscore +1 to +2 overbought  •  ONLY when RSI 40-50 lower neutral

### L08.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=86  W=30/L=56  WR=34.9%
- Sharpen: sharpest is RSI=RSI3 (28/56 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 40-50 lower neutral

### L09.  `H20=H20c AND H60=H60e AND T4=T4a`
- Raw: n=85  W=30/L=55  WR=35.3%
- Sharpen: sharpest is BBP=BBP4 (18/55 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend WITH trade  •  ONLY when upper third

### L10.  `H20=H20c AND T1=T1a AND T4=T4a`
- Raw: n=85  W=30/L=55  WR=35.3%
- Sharpen: sharpest is BBP=BBP4 (18/55 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when upper third

### L11.  `H20=H20c AND T4=T4a AND direction_exec=short`
- Raw: n=85  W=30/L=55  WR=35.3%
- Sharpen: sharpest is BBP=BBP4 (18/55 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend WITH trade  •  ONLY when upper third

### L12.  `H20=H20c AND H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=85  W=30/L=55  WR=35.3%
- Sharpen: sharpest is BBP=BBP4 (18/55 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when upper third

### L13.  `H20=H20c AND H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=85  W=30/L=55  WR=35.3%
- Sharpen: sharpest is BBP=BBP4 (18/55 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; 4h trend WITH trade  •  ONLY when upper third

### L14.  `H20=H20c AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=85  W=30/L=55  WR=35.3%
- Sharpen: sharpest is BBP=BBP4 (18/55 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when upper third

### L15.  `H60=H60e AND T1=T1a AND ZS=ZS4`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is RSI=RSI3 (28/45 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when RSI 40-50 lower neutral

### L16.  `H60=H60a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is T4=T4c (33/45 of losers there)
- **Sharp: n=49  W=16/L=33  WR=32.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when 4h trend AGAINST trade

### L17.  `T1=T1a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is RSI=RSI3 (28/45 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when RSI 40-50 lower neutral

### L18.  `T1=T1c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is T4=T4c (33/45 of losers there)
- **Sharp: n=49  W=16/L=33  WR=32.7%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when 4h trend AGAINST trade

### L19.  `ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is T4=T4c (33/45 of losers there)
- **Sharp: n=49  W=16/L=33  WR=32.7%**
- **Dir: LONG**  •  zscore -3 to -2 deep oversold; session=asia  •  ONLY when 4h trend AGAINST trade

### L20.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is RSI=RSI3 (28/45 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 40-50 lower neutral

### L21.  `H60=H60e AND T1=T1a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is RSI=RSI3 (28/45 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when RSI 40-50 lower neutral

### L22.  `H60=H60a AND T1=T1c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is T4=T4c (33/45 of losers there)
- **Sharp: n=49  W=16/L=33  WR=32.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when 4h trend AGAINST trade

### L23.  `H60=H60a AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is T4=T4c (33/45 of losers there)
- **Sharp: n=49  W=16/L=33  WR=32.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when 4h trend AGAINST trade

### L24.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is RSI=RSI3 (28/45 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 40-50 lower neutral

### L25.  `T1=T1c AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is T4=T4c (33/45 of losers there)
- **Sharp: n=49  W=16/L=33  WR=32.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4c(56/43) | T4a(42/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
