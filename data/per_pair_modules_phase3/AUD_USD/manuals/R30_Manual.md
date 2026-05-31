# AUD_USD — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,169**  (W=2,009 / L=1,160)  -  WR: **63.4%**

## Session distribution

- asia: n=1205  W=747/L=458  WR=62.0%
- ny_mid: n=491  W=317/L=174  WR=64.6%
- london_open: n=404  W=274/L=130  WR=67.8%
- ny_close: n=294  W=189/L=105  WR=64.3%
- london: n=276  W=185/L=91  WR=67.0%
- ny_open: n=269  W=152/L=117  WR=56.5%
- asia_late: n=158  W=103/L=55  WR=65.2%
- off_hours: n=72  W=42/L=30  WR=58.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND session_bucket=ny_mid`
- Raw: n=183  W=158/L=25  WR=86.3%
- Refine: exclude BBP=BBP5 drops 11/25 losers (44%)
- **Final: n=139  W=125/L=14  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W02.  `H20=H20a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=183  W=158/L=25  WR=86.3%
- Refine: exclude BBP=BBP5 drops 11/25 losers (44%)
- **Final: n=139  W=125/L=14  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W03.  `H20=H20a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=183  W=158/L=25  WR=86.3%
- Refine: exclude BBP=BBP5 drops 11/25 losers (44%)
- **Final: n=139  W=125/L=14  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W04.  `H20=H20a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=183  W=158/L=25  WR=86.3%
- Refine: exclude BBP=BBP5 drops 11/25 losers (44%)
- **Final: n=139  W=125/L=14  WR=89.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W05.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=183  W=158/L=25  WR=86.3%
- Refine: exclude BBP=BBP5 drops 11/25 losers (44%)
- **Final: n=139  W=125/L=14  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W06.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=183  W=158/L=25  WR=86.3%
- Refine: exclude BBP=BBP5 drops 11/25 losers (44%)
- **Final: n=139  W=125/L=14  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W07.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=183  W=158/L=25  WR=86.3%
- Refine: exclude BBP=BBP5 drops 11/25 losers (44%)
- **Final: n=139  W=125/L=14  WR=89.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W08.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=183  W=158/L=25  WR=86.3%
- Refine: exclude BBP=BBP5 drops 11/25 losers (44%)
- **Final: n=139  W=125/L=14  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W09.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=183  W=158/L=25  WR=86.3%
- Refine: exclude BBP=BBP5 drops 11/25 losers (44%)
- **Final: n=139  W=125/L=14  WR=89.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W10.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=183  W=158/L=25  WR=86.3%
- Refine: exclude BBP=BBP5 drops 11/25 losers (44%)
- **Final: n=139  W=125/L=14  WR=89.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W11.  `T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=153  W=142/L=11  WR=92.8%
- Refine: exclude BBP=BBP2 drops 6/11 losers (55%)
- **Final: n=115  W=110/L=5  WR=95.7%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when lower third

### W12.  `H60=H60a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=151  W=137/L=14  WR=90.7%
- Refine: exclude BBP=BBP2 drops 8/14 losers (57%)
- **Final: n=114  W=108/L=6  WR=94.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when lower third

### W13.  `T1=T1a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=151  W=137/L=14  WR=90.7%
- Refine: exclude BBP=BBP2 drops 8/14 losers (57%)
- **Final: n=114  W=108/L=6  WR=94.7%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when lower third

### W14.  `RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=151  W=137/L=14  WR=90.7%
- Refine: exclude BBP=BBP2 drops 8/14 losers (57%)
- **Final: n=114  W=108/L=6  WR=94.7%**
- **Dir: LONG**  •  RSI 60-70 strong; session=asia  •  AVOID when lower third

### W15.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=151  W=137/L=14  WR=90.7%
- Refine: exclude BBP=BBP2 drops 8/14 losers (57%)
- **Final: n=114  W=108/L=6  WR=94.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when lower third

### W16.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=151  W=137/L=14  WR=90.7%
- Refine: exclude BBP=BBP2 drops 8/14 losers (57%)
- **Final: n=114  W=108/L=6  WR=94.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when lower third

### W17.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=151  W=137/L=14  WR=90.7%
- Refine: exclude BBP=BBP2 drops 8/14 losers (57%)
- **Final: n=114  W=108/L=6  WR=94.7%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when lower third

### W18.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=144  W=134/L=10  WR=93.1%
- Refine: exclude strategy_id=alpha_extended_fade_v2 drops 4/10 losers (40%)
- **Final: n=128  W=122/L=6  WR=95.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when strategy=alpha_extended_fade_v2

### W19.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=144  W=134/L=10  WR=93.1%
- Refine: exclude strategy_id=alpha_extended_fade_v2 drops 4/10 losers (40%)
- **Final: n=128  W=122/L=6  WR=95.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when strategy=alpha_extended_fade_v2

### W20.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=144  W=134/L=10  WR=93.1%
- Refine: exclude strategy_id=alpha_extended_fade_v2 drops 4/10 losers (40%)
- **Final: n=128  W=122/L=6  WR=95.3%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when strategy=alpha_extended_fade_v2

### W21.  `H20=H20a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=128  W=115/L=13  WR=89.8%
- Refine: exclude RSI=RSI6 drops 13/13 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=ny_mid  •  AVOID when RSI 70-80 overbought

### W22.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=122  W=109/L=13  WR=89.3%
- Refine: exclude RSI=RSI6 drops 13/13 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; session=ny_mid  •  AVOID when RSI 70-80 overbought

### W23.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=122  W=109/L=13  WR=89.3%
- Refine: exclude RSI=RSI6 drops 13/13 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; session=ny_mid  •  AVOID when RSI 70-80 overbought

### W24.  `H20=H20a AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=122  W=109/L=13  WR=89.3%
- Refine: exclude RSI=RSI6 drops 13/13 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; upper third; session=ny_mid  •  AVOID when RSI 70-80 overbought

### W25.  `H20=H20a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=122  W=109/L=13  WR=89.3%
- Refine: exclude RSI=RSI6 drops 13/13 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; session=ny_mid  •  AVOID when RSI 70-80 overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND session_bucket=ny_mid`
- Raw: n=153  W=59/L=94  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=153  W=59/L=94  WR=38.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_mid

### L02.  `H20=H20e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=153  W=59/L=94  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=153  W=59/L=94  WR=38.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_mid

### L03.  `H20=H20e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=153  W=59/L=94  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=153  W=59/L=94  WR=38.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_mid

### L04.  `H20=H20e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=153  W=59/L=94  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=153  W=59/L=94  WR=38.6%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_mid

### L05.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=153  W=59/L=94  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=153  W=59/L=94  WR=38.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid

### L06.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=153  W=59/L=94  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=153  W=59/L=94  WR=38.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=ny_mid

### L07.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=153  W=59/L=94  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=153  W=59/L=94  WR=38.6%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_mid

### L08.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=153  W=59/L=94  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=153  W=59/L=94  WR=38.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid

### L09.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=153  W=59/L=94  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=153  W=59/L=94  WR=38.6%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_mid

### L10.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=153  W=59/L=94  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=153  W=59/L=94  WR=38.6%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_mid

### L11.  `H20=H20e AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=52/L=78  WR=40.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 70-80 overbought; session=ny_mid

### L12.  `H60=H60e AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=52/L=78  WR=40.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_mid

### L13.  `T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=52/L=78  WR=40.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid

### L14.  `T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=52/L=78  WR=40.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid

### L15.  `RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=52/L=78  WR=40.0%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=ny_mid

### L16.  `H20=H20e AND H60=H60e AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=52/L=78  WR=40.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought; session=ny_mid

### L17.  `H20=H20e AND T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=52/L=78  WR=40.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid

### L18.  `H20=H20e AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=52/L=78  WR=40.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid

### L19.  `H20=H20e AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=52/L=78  WR=40.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 70-80 overbought; session=ny_mid

### L20.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=52/L=78  WR=40.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid

### L21.  `H60=H60e AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=52/L=78  WR=40.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid

### L22.  `H60=H60e AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=52/L=78  WR=40.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_mid

### L23.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=52/L=78  WR=40.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid

### L24.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=52/L=78  WR=40.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid

### L25.  `T4=T4c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=52/L=78  WR=40.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(46/40) | H20e(42/48) |
| H60 | H60a(53/46) | H60e(47/54) |
| T1 | T1a(54/45) | T1c(46/55) |
| T4 | T4a(53/45) | T4c(47/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/46) | short(47/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
