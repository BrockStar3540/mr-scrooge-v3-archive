# AUD_NZD — R37 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,652**  (W=1,049 / L=603)  -  WR: **63.5%**

## Session distribution

- asia: n=569  W=377/L=192  WR=66.3%
- ny_mid: n=222  W=137/L=85  WR=61.7%
- london_open: n=210  W=130/L=80  WR=61.9%
- london: n=202  W=124/L=78  WR=61.4%
- ny_close: n=155  W=93/L=62  WR=60.0%
- ny_open: n=118  W=82/L=36  WR=69.5%
- off_hours: n=115  W=66/L=49  WR=57.4%
- asia_late: n=61  W=40/L=21  WR=65.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=266  W=229/L=37  WR=86.1%
- Refine: exclude session_bucket=london drops 12/37 losers (32%)
- **Final: n=232  W=207/L=25  WR=89.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong  •  AVOID when session=london

### W02.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=266  W=229/L=37  WR=86.1%
- Refine: exclude session_bucket=london drops 12/37 losers (32%)
- **Final: n=232  W=207/L=25  WR=89.2%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong  •  AVOID when session=london

### W03.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=266  W=229/L=37  WR=86.1%
- Refine: exclude session_bucket=london drops 12/37 losers (32%)
- **Final: n=232  W=207/L=25  WR=89.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong  •  AVOID when session=london

### W04.  `H60=H60a AND T1=T1a AND session_bucket=asia`
- Raw: n=263  W=229/L=34  WR=87.1%
- Refine: exclude ZS=ZS3 drops 15/34 losers (44%)
- **Final: n=199  W=180/L=19  WR=90.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W05.  `T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=263  W=229/L=34  WR=87.1%
- Refine: exclude ZS=ZS3 drops 15/34 losers (44%)
- **Final: n=199  W=180/L=19  WR=90.5%**
- **Dir: LONG**  •  1h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W06.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=263  W=229/L=34  WR=87.1%
- Refine: exclude ZS=ZS3 drops 15/34 losers (44%)
- **Final: n=199  W=180/L=19  WR=90.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W07.  `T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=251  W=219/L=32  WR=87.3%
- Refine: exclude ZS=ZS3 drops 13/32 losers (41%)
- **Final: n=199  W=180/L=19  WR=90.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W08.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=251  W=219/L=32  WR=87.3%
- Refine: exclude ZS=ZS3 drops 13/32 losers (41%)
- **Final: n=199  W=180/L=19  WR=90.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W09.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=251  W=219/L=32  WR=87.3%
- Refine: exclude ZS=ZS3 drops 13/32 losers (41%)
- **Final: n=199  W=180/L=19  WR=90.5%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W10.  `H20=H20a AND T1=T1a AND session_bucket=asia`
- Raw: n=245  W=213/L=32  WR=86.9%
- Refine: exclude ZS=ZS3 drops 13/32 losers (41%)
- **Final: n=193  W=174/L=19  WR=90.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W11.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=asia`
- Raw: n=245  W=213/L=32  WR=86.9%
- Refine: exclude ZS=ZS3 drops 13/32 losers (41%)
- **Final: n=193  W=174/L=19  WR=90.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W12.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=245  W=213/L=32  WR=86.9%
- Refine: exclude ZS=ZS3 drops 13/32 losers (41%)
- **Final: n=193  W=174/L=19  WR=90.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W13.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=245  W=213/L=32  WR=86.9%
- Refine: exclude ZS=ZS3 drops 13/32 losers (41%)
- **Final: n=193  W=174/L=19  WR=90.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W14.  `H60=H60a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=239  W=206/L=33  WR=86.2%
- Refine: exclude session_bucket=london drops 10/33 losers (30%)
- **Final: n=211  W=188/L=23  WR=89.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when session=london

### W15.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=239  W=206/L=33  WR=86.2%
- Refine: exclude session_bucket=london drops 10/33 losers (30%)
- **Final: n=211  W=188/L=23  WR=89.1%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when session=london

### W16.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=239  W=206/L=33  WR=86.2%
- Refine: exclude session_bucket=london drops 10/33 losers (30%)
- **Final: n=211  W=188/L=23  WR=89.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when session=london

### W17.  `H60=H60a AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=239  W=206/L=33  WR=86.2%
- Refine: exclude session_bucket=london drops 10/33 losers (30%)
- **Final: n=211  W=188/L=23  WR=89.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when session=london

### W18.  `BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=239  W=206/L=33  WR=86.2%
- Refine: exclude session_bucket=london drops 10/33 losers (30%)
- **Final: n=211  W=188/L=23  WR=89.1%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when session=london

### W19.  `H60=H60a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=234  W=203/L=31  WR=86.8%
- Refine: exclude H20=H20a drops 31/31 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF20 aligned WITH trade

### W20.  `T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=234  W=203/L=31  WR=86.8%
- Refine: exclude H20=H20a drops 31/31 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF20 aligned WITH trade

### W21.  `RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=234  W=203/L=31  WR=86.8%
- Refine: exclude H20=H20a drops 31/31 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 60-70 strong; session=asia  •  AVOID when HTF20 aligned WITH trade

### W22.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=234  W=203/L=31  WR=86.8%
- Refine: exclude H20=H20a drops 31/31 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF20 aligned WITH trade

### W23.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=234  W=203/L=31  WR=86.8%
- Refine: exclude H20=H20a drops 31/31 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF20 aligned WITH trade

### W24.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=234  W=203/L=31  WR=86.8%
- Refine: exclude H20=H20a drops 31/31 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF20 aligned WITH trade

### W25.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=234  W=199/L=35  WR=85.0%
- Refine: exclude session_bucket=london drops 10/35 losers (29%)
- **Final: n=216  W=191/L=25  WR=88.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=102  W=39/L=63  WR=38.2%
- Sharpen: sharpest is RSI=RSI5 (53/63 of losers there)
- **Sharp: n=77  W=24/L=53  WR=31.2%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=asia  •  ONLY when RSI 60-70 strong

### L02.  `BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=102  W=39/L=63  WR=38.2%
- Sharpen: sharpest is RSI=RSI5 (53/63 of losers there)
- **Sharp: n=77  W=24/L=53  WR=31.2%**
- **Dir: SHORT**  •  upper third; session=asia  •  ONLY when RSI 60-70 strong

### L03.  `H60=H60e AND BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=102  W=39/L=63  WR=38.2%
- Sharpen: sharpest is RSI=RSI5 (53/63 of losers there)
- **Sharp: n=77  W=24/L=53  WR=31.2%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; session=asia  •  ONLY when RSI 60-70 strong

### L04.  `T4=T4c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=98  W=33/L=65  WR=33.7%
- Sharpen: sharpest is RSI=RSI6 (10/65 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; session=asia  •  ONLY when RSI 70-80 overbought

### L05.  `T1=T1c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=98  W=39/L=59  WR=39.8%
- Sharpen: sharpest is RSI=RSI6 (12/59 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L06.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=96  W=33/L=63  WR=34.4%
- Sharpen: sharpest is RSI=RSI6 (10/63 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; session=asia  •  ONLY when RSI 70-80 overbought

### L07.  `T4=T4c AND BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=96  W=33/L=63  WR=34.4%
- Sharpen: sharpest is RSI=RSI6 (10/63 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; session=asia  •  ONLY when RSI 70-80 overbought

### L08.  `H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is H20=H20e (45/58 of losers there)
- **Sharp: n=63  W=18/L=45  WR=28.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 strongly against

### L09.  `H60=H60e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is H20=H20e (45/58 of losers there)
- **Sharp: n=63  W=18/L=45  WR=28.6%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_mid  •  ONLY when HTF20 strongly against

### L10.  `T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is H20=H20e (45/58 of losers there)
- **Sharp: n=63  W=18/L=45  WR=28.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 strongly against

### L11.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is H20=H20e (45/58 of losers there)
- **Sharp: n=63  W=18/L=45  WR=28.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 strongly against

### L12.  `H60=H60e AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=89  W=32/L=57  WR=36.0%
- Sharpen: sharpest is RSI=RSI6 (10/57 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 70-80 overbought

### L13.  `T4=T4c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=89  W=32/L=57  WR=36.0%
- Sharpen: sharpest is RSI=RSI6 (10/57 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 70-80 overbought

### L14.  `ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=89  W=32/L=57  WR=36.0%
- Sharpen: sharpest is RSI=RSI6 (10/57 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 70-80 overbought

### L15.  `H60=H60e AND T4=T4c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=89  W=32/L=57  WR=36.0%
- Sharpen: sharpest is RSI=RSI6 (10/57 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 70-80 overbought

### L16.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=89  W=32/L=57  WR=36.0%
- Sharpen: sharpest is RSI=RSI6 (10/57 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 70-80 overbought

### L17.  `H60=H60e AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=89  W=32/L=57  WR=36.0%
- Sharpen: sharpest is RSI=RSI6 (10/57 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 70-80 overbought

### L18.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=89  W=32/L=57  WR=36.0%
- Sharpen: sharpest is RSI=RSI6 (10/57 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 70-80 overbought

### L19.  `T4=T4c AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=89  W=32/L=57  WR=36.0%
- Sharpen: sharpest is RSI=RSI6 (10/57 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 70-80 overbought

### L20.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=89  W=32/L=57  WR=36.0%
- Sharpen: sharpest is RSI=RSI6 (10/57 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 70-80 overbought

### L21.  `H20=H20e AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=84  W=31/L=53  WR=36.9%
- Sharpen: sharpest is T1=T1c (48/53 of losers there)
- **Sharp: n=70  W=22/L=48  WR=31.4%**
- **Dir: ?**  •  HTF20 strongly against; upper third; session=asia  •  ONLY when 1h trend AGAINST trade

### L22.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=84  W=31/L=53  WR=36.9%
- Sharpen: sharpest is T1=T1c (48/53 of losers there)
- **Sharp: n=70  W=22/L=48  WR=31.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; session=asia  •  ONLY when 1h trend AGAINST trade

### L23.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=84  W=31/L=53  WR=36.9%
- Sharpen: sharpest is T1=T1c (48/53 of losers there)
- **Sharp: n=70  W=22/L=48  WR=31.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; session=asia  •  ONLY when 1h trend AGAINST trade

### L24.  `H20=H20e AND BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=84  W=31/L=53  WR=36.9%
- Sharpen: sharpest is T1=T1c (48/53 of losers there)
- **Sharp: n=70  W=22/L=48  WR=31.4%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; session=asia  •  ONLY when 1h trend AGAINST trade

### L25.  `H20=H20e AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=79  W=30/L=49  WR=38.0%
- Sharpen: sharpest is RSI=RSI6 (10/49 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 70-80 overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(53/27) | H20e(27/53) |
| H60 | H60a(64/36) | H60e(36/64) |
| T1 | T1a(62/38) | T1c(38/62) |
| T4 | T4a(60/40) | T4c(40/60) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(64/36) | short(36/64) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
