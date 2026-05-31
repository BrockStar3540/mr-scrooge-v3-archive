# AUD_JPY — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **5,876**  (W=3,675 / L=2,201)  -  WR: **62.5%**

## Session distribution

- asia: n=1685  W=1067/L=618  WR=63.3%
- ny_close: n=1297  W=802/L=495  WR=61.8%
- ny_open: n=885  W=555/L=330  WR=62.7%
- ny_mid: n=744  W=467/L=277  WR=62.8%
- london_open: n=405  W=258/L=147  WR=63.7%
- london: n=403  W=244/L=159  WR=60.5%
- off_hours: n=249  W=150/L=99  WR=60.2%
- asia_late: n=208  W=132/L=76  WR=63.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=157  W=135/L=22  WR=86.0%
- Refine: no further refinement
- **Final: n=157  W=135/L=22  WR=86.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong; session=ny_open

### W02.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=157  W=135/L=22  WR=86.0%
- Refine: no further refinement
- **Final: n=157  W=135/L=22  WR=86.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 60-70 strong; session=ny_open

### W03.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=157  W=135/L=22  WR=86.0%
- Refine: no further refinement
- **Final: n=157  W=135/L=22  WR=86.0%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 60-70 strong; session=ny_open

### W04.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=157  W=135/L=22  WR=86.0%
- Refine: no further refinement
- **Final: n=157  W=135/L=22  WR=86.0%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong; session=ny_open

### W05.  `H60=H60a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=149  W=127/L=22  WR=85.2%
- Refine: no further refinement
- **Final: n=149  W=127/L=22  WR=85.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_open

### W06.  `T1=T1a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=149  W=127/L=22  WR=85.2%
- Refine: no further refinement
- **Final: n=149  W=127/L=22  WR=85.2%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_open

### W07.  `T4=T4a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=149  W=127/L=22  WR=85.2%
- Refine: no further refinement
- **Final: n=149  W=127/L=22  WR=85.2%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_open

### W08.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=149  W=127/L=22  WR=85.2%
- Refine: no further refinement
- **Final: n=149  W=127/L=22  WR=85.2%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_open

### W09.  `H20=H20a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=147  W=125/L=22  WR=85.0%
- Refine: no further refinement
- **Final: n=147  W=125/L=22  WR=85.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 60-70 strong; session=ny_open

### W10.  `H20=H20a AND H60=H60a AND session_bucket=asia_late`
- Raw: n=115  W=107/L=8  WR=93.0%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia_late  •  AVOID when upper third

### W11.  `H20=H20a AND T1=T1a AND session_bucket=asia_late`
- Raw: n=115  W=107/L=8  WR=93.0%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia_late  •  AVOID when upper third

### W12.  `H20=H20a AND T4=T4a AND session_bucket=asia_late`
- Raw: n=115  W=107/L=8  WR=93.0%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia_late  •  AVOID when upper third

### W13.  `H20=H20a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=115  W=107/L=8  WR=93.0%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=asia_late  •  AVOID when upper third

### W14.  `H60=H60a AND T1=T1a AND session_bucket=asia_late`
- Raw: n=115  W=107/L=8  WR=93.0%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia_late  •  AVOID when upper third

### W15.  `H60=H60a AND T4=T4a AND session_bucket=asia_late`
- Raw: n=115  W=107/L=8  WR=93.0%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia_late  •  AVOID when upper third

### W16.  `H60=H60a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=115  W=107/L=8  WR=93.0%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=asia_late  •  AVOID when upper third

### W17.  `T1=T1a AND T4=T4a AND session_bucket=asia_late`
- Raw: n=115  W=107/L=8  WR=93.0%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=asia_late  •  AVOID when upper third

### W18.  `T1=T1a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=115  W=107/L=8  WR=93.0%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=asia_late  •  AVOID when upper third

### W19.  `T4=T4a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=115  W=107/L=8  WR=93.0%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=asia_late  •  AVOID when upper third

### W20.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=asia_late`
- Raw: n=115  W=107/L=8  WR=93.0%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=asia_late  •  AVOID when upper third

### W21.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=asia_late`
- Raw: n=115  W=107/L=8  WR=93.0%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=asia_late  •  AVOID when upper third

### W22.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=115  W=107/L=8  WR=93.0%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia_late  •  AVOID when upper third

### W23.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=asia_late`
- Raw: n=115  W=107/L=8  WR=93.0%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia_late  •  AVOID when upper third

### W24.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=115  W=107/L=8  WR=93.0%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia_late  •  AVOID when upper third

### W25.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=115  W=107/L=8  WR=93.0%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia_late  •  AVOID when upper third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=127  W=46/L=81  WR=36.2%
- Sharpen: sharpest is H20=H20c (17/81 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_open  •  ONLY when HTF20 neutral

### L02.  `T1=T1c AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=127  W=46/L=81  WR=36.2%
- Sharpen: sharpest is H20=H20c (17/81 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_open  •  ONLY when HTF20 neutral

### L03.  `T4=T4c AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=127  W=46/L=81  WR=36.2%
- Sharpen: sharpest is H20=H20c (17/81 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_open  •  ONLY when HTF20 neutral

### L04.  `RSI=RSI6 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=127  W=46/L=81  WR=36.2%
- Sharpen: sharpest is H20=H20c (17/81 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=ny_open  •  ONLY when HTF20 neutral

### L05.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=127  W=46/L=81  WR=36.2%
- Sharpen: sharpest is H20=H20c (17/81 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=ny_open  •  ONLY when HTF20 neutral

### L06.  `H60=H60e AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=127  W=46/L=81  WR=36.2%
- Sharpen: sharpest is H20=H20c (17/81 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_open  •  ONLY when HTF20 neutral

### L07.  `H60=H60e AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=127  W=46/L=81  WR=36.2%
- Sharpen: sharpest is H20=H20c (17/81 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_open  •  ONLY when HTF20 neutral

### L08.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=127  W=46/L=81  WR=36.2%
- Sharpen: sharpest is H20=H20c (17/81 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_open  •  ONLY when HTF20 neutral

### L09.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=127  W=46/L=81  WR=36.2%
- Sharpen: sharpest is H20=H20c (17/81 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_open  •  ONLY when HTF20 neutral

### L10.  `T4=T4c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=127  W=46/L=81  WR=36.2%
- Sharpen: sharpest is H20=H20c (17/81 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_open  •  ONLY when HTF20 neutral

### L11.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=109  W=35/L=74  WR=32.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=109  W=35/L=74  WR=32.1%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong; session=ny_open

### L12.  `T1=T1c AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=109  W=35/L=74  WR=32.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=109  W=35/L=74  WR=32.1%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 60-70 strong; session=ny_open

### L13.  `T4=T4c AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=109  W=35/L=74  WR=32.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=109  W=35/L=74  WR=32.1%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 60-70 strong; session=ny_open

### L14.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=109  W=35/L=74  WR=32.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=109  W=35/L=74  WR=32.1%**
- **Dir: SHORT**  •  upper third; RSI 60-70 strong; session=ny_open

### L15.  `H60=H60e AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=103  W=31/L=72  WR=30.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=103  W=31/L=72  WR=30.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_open

### L16.  `T1=T1c AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=103  W=31/L=72  WR=30.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=103  W=31/L=72  WR=30.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_open

### L17.  `T4=T4c AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=103  W=31/L=72  WR=30.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=103  W=31/L=72  WR=30.1%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_open

### L18.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=103  W=31/L=72  WR=30.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=103  W=31/L=72  WR=30.1%**
- **Dir: SHORT**  •  RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_open

### L19.  `H20=H20e AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=98  W=35/L=63  WR=35.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=98  W=35/L=63  WR=35.7%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 60-70 strong; session=ny_open

### L20.  `H20=H20e AND H60=H60e AND session_bucket=asia_late`
- Raw: n=93  W=25/L=68  WR=26.9%
- Sharpen: sharpest is RSI=RSI7 (18/68 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=asia_late  •  ONLY when RSI>80 extreme overbought

### L21.  `H20=H20e AND T1=T1c AND session_bucket=asia_late`
- Raw: n=93  W=25/L=68  WR=26.9%
- Sharpen: sharpest is RSI=RSI7 (18/68 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia_late  •  ONLY when RSI>80 extreme overbought

### L22.  `H20=H20e AND T4=T4c AND session_bucket=asia_late`
- Raw: n=93  W=25/L=68  WR=26.9%
- Sharpen: sharpest is RSI=RSI7 (18/68 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia_late  •  ONLY when RSI>80 extreme overbought

### L23.  `H20=H20e AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=93  W=25/L=68  WR=26.9%
- Sharpen: sharpest is RSI=RSI7 (18/68 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=asia_late  •  ONLY when RSI>80 extreme overbought

### L24.  `H60=H60e AND T1=T1c AND session_bucket=asia_late`
- Raw: n=93  W=25/L=68  WR=26.9%
- Sharpen: sharpest is RSI=RSI7 (18/68 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=asia_late  •  ONLY when RSI>80 extreme overbought

### L25.  `H60=H60e AND T4=T4c AND session_bucket=asia_late`
- Raw: n=93  W=25/L=68  WR=26.9%
- Sharpen: sharpest is RSI=RSI7 (18/68 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia_late  •  ONLY when RSI>80 extreme overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(51/42) | H20e(44/53) |
| H60 | H60a(53/45) | H60e(47/55) |
| T1 | T1a(53/45) | T1c(47/55) |
| T4 | T4a(54/45) | T4c(46/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/45) | short(47/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
