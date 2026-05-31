# EUR_CHF — R24 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,135**  (W=707 / L=428)  -  WR: **62.3%**

## Session distribution

- ny_mid: n=420  W=256/L=164  WR=61.0%
- ny_open: n=192  W=121/L=71  WR=63.0%
- ny_close: n=182  W=117/L=65  WR=64.3%
- asia: n=105  W=69/L=36  WR=65.7%
- london: n=95  W=62/L=33  WR=65.3%
- london_open: n=73  W=46/L=27  WR=63.0%
- off_hours: n=68  W=36/L=32  WR=52.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=151  W=130/L=21  WR=86.1%
- Refine: exclude session_bucket=ny_mid drops 17/21 losers (81%)
- **Final: n=108  W=104/L=4  WR=96.3%**
- **Dir: ?**  •  1h trend WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W02.  `RSI=RSI1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=151  W=130/L=21  WR=86.1%
- Refine: exclude session_bucket=ny_mid drops 17/21 losers (81%)
- **Final: n=108  W=104/L=4  WR=96.3%**
- **Dir: SHORT**  •  RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W03.  `T1=T1a AND RSI=RSI1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=151  W=130/L=21  WR=86.1%
- Refine: exclude session_bucket=ny_mid drops 17/21 losers (81%)
- **Final: n=108  W=104/L=4  WR=96.3%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W04.  `T1=T1a AND T4=T4a AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=143  W=122/L=21  WR=85.3%
- Refine: exclude session_bucket=ny_mid drops 17/21 losers (81%)
- **Final: n=100  W=96/L=4  WR=96.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W05.  `T4=T4a AND RSI=RSI1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=143  W=122/L=21  WR=85.3%
- Refine: exclude session_bucket=ny_mid drops 17/21 losers (81%)
- **Final: n=100  W=96/L=4  WR=96.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W06.  `H20=H20a AND T1=T1a AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=133  W=116/L=17  WR=87.2%
- Refine: exclude session_bucket=ny_mid drops 13/17 losers (76%)
- **Final: n=106  W=102/L=4  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W07.  `H20=H20a AND RSI=RSI1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=133  W=116/L=17  WR=87.2%
- Refine: exclude session_bucket=ny_mid drops 13/17 losers (76%)
- **Final: n=106  W=102/L=4  WR=96.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W08.  `H20=H20a AND T4=T4a AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=125  W=108/L=17  WR=86.4%
- Refine: exclude session_bucket=ny_mid drops 13/17 losers (76%)
- **Final: n=98  W=94/L=4  WR=95.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W09.  `H20=H20a AND H60=H60a AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=123  W=106/L=17  WR=86.2%
- Refine: exclude session_bucket=ny_mid drops 13/17 losers (76%)
- **Final: n=96  W=92/L=4  WR=95.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W10.  `T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=104  W=97/L=7  WR=93.3%
- Refine: exclude RSI=RSI2 drops 6/7 losers (86%)
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_open  •  AVOID when RSI 30-40 weak

### W11.  `H20=H20a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=103  W=93/L=10  WR=90.3%
- Refine: exclude H60=H60b drops 9/10 losers (90%)
- **Final: n=89  W=88/L=1  WR=98.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when HTF60 slightly aligned

### W12.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=101  W=97/L=4  WR=96.0%
- Refine: exclude H60=H60c drops 3/4 losers (75%)
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF60 neutral

### W13.  `T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=101  W=97/L=4  WR=96.0%
- Refine: exclude H60=H60c drops 3/4 losers (75%)
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_open  •  AVOID when HTF60 neutral

### W14.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=101  W=97/L=4  WR=96.0%
- Refine: exclude H60=H60c drops 3/4 losers (75%)
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF60 neutral

### W15.  `T1=T1a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=95  W=94/L=1  WR=98.9%
- Refine: no further refinement
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: ?**  •  1h trend WITH trade; RSI 20-30 oversold; session=ny_open

### W16.  `T4=T4a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=95  W=94/L=1  WR=98.9%
- Refine: no further refinement
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: ?**  •  4h trend WITH trade; RSI 20-30 oversold; session=ny_open

### W17.  `RSI=RSI1 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=95  W=94/L=1  WR=98.9%
- Refine: no further refinement
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: SHORT**  •  RSI 20-30 oversold; session=ny_open

### W18.  `T1=T1a AND T4=T4a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=95  W=94/L=1  WR=98.9%
- Refine: no further refinement
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold; session=ny_open

### W19.  `T1=T1a AND RSI=RSI1 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=95  W=94/L=1  WR=98.9%
- Refine: no further refinement
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 20-30 oversold; session=ny_open

### W20.  `T4=T4a AND RSI=RSI1 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=95  W=94/L=1  WR=98.9%
- Refine: no further refinement
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 20-30 oversold; session=ny_open

### W21.  `H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=92  W=88/L=4  WR=95.7%
- Refine: exclude H20=H20b drops 3/4 losers (75%)
- **Final: n=89  W=88/L=1  WR=98.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when HTF20 slightly aligned

### W22.  `H60=H60a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=92  W=88/L=4  WR=95.7%
- Refine: exclude H20=H20b drops 3/4 losers (75%)
- **Final: n=89  W=88/L=1  WR=98.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_open  •  AVOID when HTF20 slightly aligned

### W23.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=92  W=88/L=4  WR=95.7%
- Refine: exclude H20=H20b drops 3/4 losers (75%)
- **Final: n=89  W=88/L=1  WR=98.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when HTF20 slightly aligned

### W24.  `H20=H20a AND H60=H60a AND session_bucket=ny_open`
- Raw: n=89  W=88/L=1  WR=98.9%
- Refine: no further refinement
- **Final: n=89  W=88/L=1  WR=98.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open

### W25.  `H20=H20a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=89  W=88/L=1  WR=98.9%
- Refine: no further refinement
- **Final: n=89  W=88/L=1  WR=98.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND RSI=RSI1`
- Raw: n=228  W=86/L=142  WR=37.7%
- Sharpen: sharpest is session_bucket=ny_open (54/142 of losers there)
- **Sharp: n=57  W=3/L=54  WR=5.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L02.  `H20=H20e AND RSI=RSI1 AND direction_exec=long`
- Raw: n=228  W=86/L=142  WR=37.7%
- Sharpen: sharpest is session_bucket=ny_open (54/142 of losers there)
- **Sharp: n=57  W=3/L=54  WR=5.3%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 20-30 oversold  •  ONLY when session=ny_open

### L03.  `H20=H20e AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=228  W=86/L=142  WR=37.7%
- Sharpen: sharpest is session_bucket=ny_open (54/142 of losers there)
- **Sharp: n=57  W=3/L=54  WR=5.3%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L04.  `H20=H20e AND T4=T4c AND RSI=RSI1`
- Raw: n=219  W=86/L=133  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_open (54/133 of losers there)
- **Sharp: n=57  W=3/L=54  WR=5.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L05.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=219  W=86/L=133  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_open (54/133 of losers there)
- **Sharp: n=57  W=3/L=54  WR=5.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L06.  `H20=H20e AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=219  W=86/L=133  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_open (54/133 of losers there)
- **Sharp: n=57  W=3/L=54  WR=5.3%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_open

### L07.  `T1=T1c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=162  W=63/L=99  WR=38.9%
- Sharpen: sharpest is H20=H20e (91/99 of losers there)
- **Sharp: n=124  W=33/L=91  WR=26.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L08.  `T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=135  W=41/L=94  WR=30.4%
- Sharpen: sharpest is session_bucket=ny_open (37/94 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L09.  `T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=135  W=41/L=94  WR=30.4%
- Sharpen: sharpest is session_bucket=ny_open (37/94 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L10.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=135  W=41/L=94  WR=30.4%
- Sharpen: sharpest is session_bucket=ny_open (37/94 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L11.  `T4=T4c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=132  W=46/L=86  WR=34.8%
- Sharpen: sharpest is session_bucket=ny_open (27/86 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L12.  `H20=H20e AND T4=T4c AND ZS=ZS1`
- Raw: n=128  W=33/L=95  WR=25.8%
- Sharpen: sharpest is session_bucket=ny_open (36/95 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L13.  `H60=H60e AND T4=T4c AND ZS=ZS1`
- Raw: n=125  W=41/L=84  WR=32.8%
- Sharpen: sharpest is session_bucket=ny_open (36/84 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L14.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=125  W=41/L=84  WR=32.8%
- Sharpen: sharpest is session_bucket=ny_open (36/84 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L15.  `H60=H60e AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=125  W=41/L=84  WR=32.8%
- Sharpen: sharpest is session_bucket=ny_open (36/84 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L16.  `H20=H20e AND T1=T1c AND ZS=ZS1`
- Raw: n=124  W=33/L=91  WR=26.6%
- Sharpen: sharpest is session_bucket=ny_open (36/91 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L17.  `H20=H20e AND ZS=ZS1 AND direction_exec=long`
- Raw: n=124  W=33/L=91  WR=26.6%
- Sharpen: sharpest is session_bucket=ny_open (36/91 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L18.  `H20=H20e AND T1=T1c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=124  W=33/L=91  WR=26.6%
- Sharpen: sharpest is session_bucket=ny_open (36/91 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L19.  `H20=H20e AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=121  W=40/L=81  WR=33.1%
- Sharpen: sharpest is session_bucket=ny_open (23/81 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: ?**  •  HTF20 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L20.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=119  W=33/L=86  WR=27.7%
- Sharpen: sharpest is session_bucket=ny_open (36/86 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L21.  `H20=H20e AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=119  W=33/L=86  WR=27.7%
- Sharpen: sharpest is session_bucket=ny_open (36/86 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L22.  `H20=H20e AND H60=H60e AND ZS=ZS1`
- Raw: n=117  W=33/L=84  WR=28.2%
- Sharpen: sharpest is session_bucket=ny_open (36/84 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L23.  `H20=H20e AND H60=H60e AND T1=T1c AND ZS=ZS1`
- Raw: n=117  W=33/L=84  WR=28.2%
- Sharpen: sharpest is session_bucket=ny_open (36/84 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L24.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS1`
- Raw: n=117  W=33/L=84  WR=28.2%
- Sharpen: sharpest is session_bucket=ny_open (36/84 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L25.  `H20=H20e AND H60=H60e AND ZS=ZS1 AND direction_exec=long`
- Raw: n=117  W=33/L=84  WR=28.2%
- Sharpen: sharpest is session_bucket=ny_open (36/84 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(58/29) | H20e(30/60) |
| H60 | H60a(49/31) | H60e(32/50) |
| T1 | T1a(60/38) | T1c(40/62) |
| T4 | T4a(61/37) | T4c(39/63) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(60/38) | long(40/62) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
