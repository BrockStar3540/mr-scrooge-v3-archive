# AUD_NZD — R34 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,342**  (W=886 / L=456)  -  WR: **66.0%**

## Session distribution

- asia: n=361  W=240/L=121  WR=66.5%
- london_open: n=215  W=144/L=71  WR=67.0%
- ny_close: n=204  W=138/L=66  WR=67.6%
- ny_mid: n=180  W=118/L=62  WR=65.6%
- london: n=139  W=100/L=39  WR=71.9%
- ny_open: n=120  W=70/L=50  WR=58.3%
- off_hours: n=82  W=50/L=32  WR=61.0%
- asia_late: n=41  W=26/L=15  WR=63.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=81  W=71/L=10  WR=87.7%
- Refine: exclude RSI=RSI6 drops 9/10 losers (90%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when RSI 70-80 overbought

### W02.  `H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=81  W=71/L=10  WR=87.7%
- Refine: exclude RSI=RSI6 drops 9/10 losers (90%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade  •  AVOID when RSI 70-80 overbought

### W03.  `T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=81  W=71/L=10  WR=87.7%
- Refine: exclude RSI=RSI6 drops 9/10 losers (90%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when RSI 70-80 overbought

### W04.  `H60=H60e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=81  W=71/L=10  WR=87.7%
- Refine: exclude RSI=RSI6 drops 9/10 losers (90%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when RSI 70-80 overbought

### W05.  `H20=H20c AND H60=H60a AND T1=T1a`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude session_bucket=ny_open drops 8/9 losers (89%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=ny_open

### W06.  `H20=H20c AND H60=H60a AND direction_exec=long`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude session_bucket=ny_open drops 8/9 losers (89%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade  •  AVOID when session=ny_open

### W07.  `H20=H20c AND T1=T1a AND direction_exec=long`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude session_bucket=ny_open drops 8/9 losers (89%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade  •  AVOID when session=ny_open

### W08.  `H20=H20c AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude session_bucket=ny_open drops 8/9 losers (89%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=ny_open

### W09.  `H20=H20c AND H60=H60a AND RSI=RSI6`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude session_bucket=ny_open drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_open

### W10.  `H20=H20c AND T1=T1a AND RSI=RSI6`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude session_bucket=ny_open drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_open

### W11.  `H20=H20c AND RSI=RSI6 AND direction_exec=long`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude session_bucket=ny_open drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; RSI 70-80 overbought  •  AVOID when session=ny_open

### W12.  `H20=H20c AND H60=H60a AND T1=T1a AND RSI=RSI6`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude session_bucket=ny_open drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_open

### W13.  `H20=H20c AND H60=H60a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude session_bucket=ny_open drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_open

### W14.  `H20=H20c AND T1=T1a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude session_bucket=ny_open drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_open

### W15.  `H20=H20c AND H60=H60a AND T4=T4a`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude session_bucket=ny_open drops 8/9 losers (89%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W16.  `H20=H20c AND T1=T1a AND T4=T4a`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude session_bucket=ny_open drops 8/9 losers (89%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W17.  `H20=H20c AND T4=T4a AND direction_exec=long`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude session_bucket=ny_open drops 8/9 losers (89%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend WITH trade  •  AVOID when session=ny_open

### W18.  `H20=H20c AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude session_bucket=ny_open drops 8/9 losers (89%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W19.  `H20=H20c AND H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude session_bucket=ny_open drops 8/9 losers (89%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W20.  `H20=H20c AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude session_bucket=ny_open drops 8/9 losers (89%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W21.  `T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude H20=H20b drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=asia  •  AVOID when HTF20 slightly aligned

### W22.  `T4=T4a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude H20=H20b drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 slightly aligned

### W23.  `T4=T4a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude H20=H20b drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  4h trend WITH trade; upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 slightly aligned

### W24.  `H20=H20c AND H60=H60a AND T4=T4a AND RSI=RSI6`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude session_bucket=ny_open drops 8/8 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_open

### W25.  `H20=H20c AND T1=T1a AND T4=T4a AND RSI=RSI6`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude session_bucket=ny_open drops 8/8 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is RSI=RSI6 (26/32 of losers there)
- **Sharp: n=32  W=6/L=26  WR=18.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 70-80 overbought

### L02.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is RSI=RSI6 (26/32 of losers there)
- **Sharp: n=32  W=6/L=26  WR=18.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 70-80 overbought

### L03.  `T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is RSI=RSI6 (26/32 of losers there)
- **Sharp: n=32  W=6/L=26  WR=18.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 70-80 overbought

### L04.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is RSI=RSI6 (26/32 of losers there)
- **Sharp: n=32  W=6/L=26  WR=18.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 70-80 overbought

### L05.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is RSI=RSI6 (26/32 of losers there)
- **Sharp: n=32  W=6/L=26  WR=18.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 70-80 overbought

### L06.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is RSI=RSI6 (26/32 of losers there)
- **Sharp: n=32  W=6/L=26  WR=18.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 70-80 overbought

### L07.  `H20=H20e AND T4=T4c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=42  W=16/L=26  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=42  W=16/L=26  WR=38.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia

### L08.  `H20=H20c AND H60=H60e AND T1=T1c`
- Raw: n=40  W=2/L=38  WR=5.0%
- Sharpen: sharpest is BBP=BBP4 (18/38 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when upper third

### L09.  `H20=H20c AND H60=H60e AND direction_exec=short`
- Raw: n=40  W=2/L=38  WR=5.0%
- Sharpen: sharpest is BBP=BBP4 (18/38 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against  •  ONLY when upper third

### L10.  `H20=H20c AND T1=T1c AND direction_exec=short`
- Raw: n=40  W=2/L=38  WR=5.0%
- Sharpen: sharpest is BBP=BBP4 (18/38 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade  •  ONLY when upper third

### L11.  `H20=H20c AND H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=40  W=2/L=38  WR=5.0%
- Sharpen: sharpest is BBP=BBP4 (18/38 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when upper third

### L12.  `H20=H20a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (10/24 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=london_open  •  ONLY when zscore >+3 extreme

### L13.  `H20=H20a AND H60=H60a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (10/24 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 70-80 overbought; session=london_open  •  ONLY when zscore >+3 extreme

### L14.  `H20=H20a AND T1=T1a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (10/24 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=london_open  •  ONLY when zscore >+3 extreme

### L15.  `H20=H20a AND RSI=RSI6 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (10/24 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=london_open  •  ONLY when zscore >+3 extreme

### L16.  `H20=H20c AND T4=T4c AND RSI=RSI6`
- Raw: n=39  W=6/L=33  WR=15.4%
- Sharpen: sharpest is H60=H60e (33/33 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 strongly against

### L17.  `H20=H20c AND H60=H60e AND RSI=RSI6`
- Raw: n=38  W=2/L=36  WR=5.3%
- Sharpen: sharpest is BBP=BBP4 (17/36 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; RSI 70-80 overbought  •  ONLY when upper third

### L18.  `H20=H20c AND T1=T1c AND RSI=RSI6`
- Raw: n=38  W=2/L=36  WR=5.3%
- Sharpen: sharpest is BBP=BBP4 (17/36 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when upper third

### L19.  `H20=H20c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=38  W=2/L=36  WR=5.3%
- Sharpen: sharpest is BBP=BBP4 (17/36 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; RSI 70-80 overbought  •  ONLY when upper third

### L20.  `H20=H20c AND H60=H60e AND T1=T1c AND RSI=RSI6`
- Raw: n=38  W=2/L=36  WR=5.3%
- Sharpen: sharpest is BBP=BBP4 (17/36 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when upper third

### L21.  `H20=H20c AND H60=H60e AND RSI=RSI6 AND direction_exec=short`
- Raw: n=38  W=2/L=36  WR=5.3%
- Sharpen: sharpest is BBP=BBP4 (17/36 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; RSI 70-80 overbought  •  ONLY when upper third

### L22.  `H20=H20c AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=38  W=2/L=36  WR=5.3%
- Sharpen: sharpest is BBP=BBP4 (17/36 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when upper third

### L23.  `H20=H20c AND H60=H60e AND T4=T4c`
- Raw: n=37  W=2/L=35  WR=5.4%
- Sharpen: sharpest is BBP=BBP4 (16/35 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when upper third

### L24.  `H20=H20c AND T1=T1c AND T4=T4c`
- Raw: n=37  W=2/L=35  WR=5.4%
- Sharpen: sharpest is BBP=BBP4 (16/35 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when upper third

### L25.  `H20=H20c AND T4=T4c AND direction_exec=short`
- Raw: n=37  W=2/L=35  WR=5.4%
- Sharpen: sharpest is BBP=BBP4 (16/35 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend AGAINST trade  •  ONLY when upper third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(44/34) | H20e(40/48) |
| H60 | H60a(51/43) | H60e(49/57) |
| T1 | T1a(51/43) | T1c(49/57) |
| T4 | T4a(56/36) | T4c(44/64) |
| BBP | — | — |
| RSI | — | — |
| ZS | ZS4(46/41) | — |
| strategy_id | — | — |
| direction_exec | long(51/43) | short(49/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
