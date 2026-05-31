# GBP_CHF — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,205**  (W=748 / L=457)  -  WR: **62.1%**

## Session distribution

- ny_mid: n=692  W=430/L=262  WR=62.1%
- london: n=151  W=90/L=61  WR=59.6%
- ny_open: n=118  W=69/L=49  WR=58.5%
- ny_close: n=113  W=72/L=41  WR=63.7%
- asia: n=74  W=47/L=27  WR=63.5%
- london_open: n=57  W=40/L=17  WR=70.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude session_bucket=ny_close drops 7/14 losers (50%)
- **Final: n=82  W=75/L=7  WR=91.5%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 60-70 strong  •  AVOID when session=ny_close

### W02.  `H20=H20e AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude session_bucket=ny_close drops 7/14 losers (50%)
- **Final: n=82  W=75/L=7  WR=91.5%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W03.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude session_bucket=ny_close drops 7/14 losers (50%)
- **Final: n=82  W=75/L=7  WR=91.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; RSI 60-70 strong  •  AVOID when session=ny_close

### W04.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude session_bucket=ny_close drops 7/14 losers (50%)
- **Final: n=82  W=75/L=7  WR=91.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W05.  `H20=H20e AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude session_bucket=ny_close drops 7/14 losers (50%)
- **Final: n=82  W=75/L=7  WR=91.5%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W06.  `H60=H60e AND T1=T1a AND session_bucket=london`
- Raw: n=89  W=82/L=7  WR=92.1%
- Refine: exclude H20=H20a drops 7/7 losers (100%)
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when HTF20 aligned WITH trade

### W07.  `H60=H60e AND direction_exec=long AND session_bucket=london`
- Raw: n=89  W=82/L=7  WR=92.1%
- Refine: exclude H20=H20a drops 7/7 losers (100%)
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; session=london  •  AVOID when HTF20 aligned WITH trade

### W08.  `T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=89  W=82/L=7  WR=92.1%
- Refine: exclude H20=H20a drops 7/7 losers (100%)
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=london  •  AVOID when HTF20 aligned WITH trade

### W09.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=89  W=82/L=7  WR=92.1%
- Refine: exclude H20=H20a drops 7/7 losers (100%)
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when HTF20 aligned WITH trade

### W10.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude RSI=RSI5 drops 7/10 losers (70%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; session=ny_mid  •  AVOID when RSI 60-70 strong

### W11.  `H60=H60a AND T1=T1a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude RSI=RSI5 drops 7/10 losers (70%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when RSI 60-70 strong

### W12.  `H60=H60a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude RSI=RSI5 drops 7/10 losers (70%)
- **Final: n=52  W=49/L=3  WR=94.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; session=ny_mid  •  AVOID when RSI 60-70 strong

### W13.  `H20=H20e AND H60=H60e AND session_bucket=london`
- Raw: n=69  W=69/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=london

### W14.  `H20=H20e AND T1=T1a AND session_bucket=london`
- Raw: n=69  W=69/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=london

### W15.  `H20=H20e AND direction_exec=long AND session_bucket=london`
- Raw: n=69  W=69/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; session=london

### W16.  `H60=H60e AND T4=T4c AND session_bucket=london`
- Raw: n=69  W=69/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london

### W17.  `T1=T1a AND T4=T4c AND session_bucket=london`
- Raw: n=69  W=69/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london

### W18.  `T4=T4c AND direction_exec=long AND session_bucket=london`
- Raw: n=69  W=69/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=london

### W19.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=london`
- Raw: n=69  W=69/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=london

### W20.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=london`
- Raw: n=69  W=69/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=london

### W21.  `H20=H20e AND H60=H60e AND direction_exec=long AND session_bucket=london`
- Raw: n=69  W=69/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; session=london

### W22.  `H20=H20e AND T1=T1a AND T4=T4c AND session_bucket=london`
- Raw: n=69  W=69/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=london

### W23.  `H20=H20e AND T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=69  W=69/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; session=london

### W24.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=london`
- Raw: n=69  W=69/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london

### W25.  `H60=H60e AND T1=T1a AND T4=T4c AND session_bucket=london`
- Raw: n=69  W=69/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=116  W=45/L=71  WR=38.8%
- Sharpen: sharpest is session_bucket=london (39/71 of losers there)
- **Sharp: n=39  W=0/L=39  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=london

### L02.  `H20=H20a AND H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=116  W=45/L=71  WR=38.8%
- Sharpen: sharpest is session_bucket=london (39/71 of losers there)
- **Sharp: n=39  W=0/L=39  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=london

### L03.  `H20=H20a AND H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=112  W=41/L=71  WR=36.6%
- Sharpen: sharpest is session_bucket=london (39/71 of losers there)
- **Sharp: n=39  W=0/L=39  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when session=london

### L04.  `H60=H60a AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=112  W=41/L=71  WR=36.6%
- Sharpen: sharpest is session_bucket=london (39/71 of losers there)
- **Sharp: n=39  W=0/L=39  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=london

### L05.  `H20=H20a AND T1=T1c AND BBP=BBP4`
- Raw: n=95  W=33/L=62  WR=34.7%
- Sharpen: sharpest is session_bucket=london (28/62 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third  •  ONLY when session=london

### L06.  `H20=H20a AND T1=T1c AND ZS=ZS4`
- Raw: n=94  W=33/L=61  WR=35.1%
- Sharpen: sharpest is session_bucket=london (28/61 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=london

### L07.  `H20=H20a AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=94  W=33/L=61  WR=35.1%
- Sharpen: sharpest is session_bucket=london (28/61 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when session=london

### L08.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is H20=H20a (52/56 of losers there)
- **Sharp: n=68  W=16/L=52  WR=23.5%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L09.  `H20=H20a AND H60=H60a AND RSI=RSI5`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is session_bucket=london (24/56 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L10.  `H20=H20a AND T1=T1c AND RSI=RSI5`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is session_bucket=london (24/56 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london

### L11.  `H20=H20a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is session_bucket=london (24/56 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L12.  `H60=H60a AND T4=T4a AND RSI=RSI5`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is session_bucket=london (24/56 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L13.  `T4=T4a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is H20=H20a (52/56 of losers there)
- **Sharp: n=68  W=16/L=52  WR=23.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when HTF20 aligned WITH trade

### L14.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI5`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is session_bucket=london (24/56 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london

### L15.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI5`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is session_bucket=london (24/56 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L16.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is session_bucket=london (24/56 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L17.  `H20=H20a AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is session_bucket=london (24/56 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L18.  `H20=H20a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is session_bucket=london (24/56 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london

### L19.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is session_bucket=london (24/56 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L20.  `H60=H60a AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is session_bucket=london (24/56 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L21.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is session_bucket=london (24/56 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L22.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is H20=H20a (52/56 of losers there)
- **Sharp: n=68  W=16/L=52  WR=23.5%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when HTF20 aligned WITH trade

### L23.  `H60=H60e AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=91  W=36/L=55  WR=39.6%
- Sharpen: sharpest is RSI=RSI4 (29/55 of losers there)
- **Sharp: n=36  W=7/L=29  WR=19.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 50-60 upper neutral

### L24.  `H20=H20a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=89  W=34/L=55  WR=38.2%
- Sharpen: sharpest is session_bucket=london (28/55 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; upper third  •  ONLY when session=london

### L25.  `H20=H20a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=89  W=34/L=55  WR=38.2%
- Sharpen: sharpest is session_bucket=london (28/55 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought  •  ONLY when session=london

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(42/35) | H20a(34/44) |
| H60 | — | — |
| T1 | T1a(58/42) | T1c(42/58) |
| T4 | T4c(56/43) | T4a(44/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(56/43) | short(44/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
