# EUR_CAD — R24 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,336**  (W=2,118 / L=1,218)  -  WR: **63.5%**

## Session distribution

- london_open: n=1133  W=721/L=412  WR=63.6%
- ny_open: n=655  W=389/L=266  WR=59.4%
- ny_mid: n=612  W=394/L=218  WR=64.4%
- london: n=461  W=299/L=162  WR=64.9%
- asia: n=177  W=115/L=62  WR=65.0%
- asia_late: n=177  W=115/L=62  WR=65.0%
- ny_close: n=100  W=71/L=29  WR=71.0%
- off_hours: n=21  W=14/L=7  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=219  W=193/L=26  WR=88.1%
- Refine: exclude H60=H60c drops 13/26 losers (50%)
- **Final: n=182  W=169/L=13  WR=92.9%**
- **Dir: SHORT**  •  deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF60 neutral

### W02.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=213  W=187/L=26  WR=87.8%
- Refine: exclude H60=H60c drops 13/26 losers (50%)
- **Final: n=176  W=163/L=13  WR=92.6%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF60 neutral

### W03.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=213  W=187/L=26  WR=87.8%
- Refine: exclude H60=H60c drops 13/26 losers (50%)
- **Final: n=176  W=163/L=13  WR=92.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF60 neutral

### W04.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=182  W=161/L=21  WR=88.5%
- Refine: exclude session_bucket=ny_open drops 10/21 losers (48%)
- **Final: n=160  W=149/L=11  WR=93.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W05.  `T1=T1c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=180  W=155/L=25  WR=86.1%
- Refine: exclude BBP=BBP5 drops 21/25 losers (84%)
- **Final: n=110  W=106/L=4  WR=96.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W06.  `T1=T1c AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=180  W=155/L=25  WR=86.1%
- Refine: exclude BBP=BBP5 drops 21/25 losers (84%)
- **Final: n=110  W=106/L=4  WR=96.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W07.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=176  W=155/L=21  WR=88.1%
- Refine: exclude session_bucket=ny_open drops 10/21 losers (48%)
- **Final: n=154  W=143/L=11  WR=92.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W08.  `H60=H60a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=169  W=149/L=20  WR=88.2%
- Refine: exclude BBP=BBP5 drops 15/20 losers (75%)
- **Final: n=98  W=93/L=5  WR=94.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W09.  `H60=H60a AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=169  W=149/L=20  WR=88.2%
- Refine: exclude BBP=BBP5 drops 15/20 losers (75%)
- **Final: n=98  W=93/L=5  WR=94.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W10.  `H60=H60a AND T4=T4c AND ZS=ZS5`
- Raw: n=161  W=141/L=20  WR=87.6%
- Refine: exclude BBP=BBP5 drops 15/20 losers (75%)
- **Final: n=92  W=87/L=5  WR=94.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W11.  `H60=H60a AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=161  W=141/L=20  WR=87.6%
- Refine: exclude BBP=BBP5 drops 15/20 losers (75%)
- **Final: n=92  W=87/L=5  WR=94.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W12.  `H60=H60a AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=161  W=141/L=20  WR=87.6%
- Refine: exclude BBP=BBP5 drops 15/20 losers (75%)
- **Final: n=92  W=87/L=5  WR=94.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W13.  `T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=139  W=130/L=9  WR=93.5%
- Refine: exclude RSI=RSI5 drops 9/9 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when RSI 60-70 strong

### W14.  `T1=T1c AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=130  W=113/L=17  WR=86.9%
- Refine: exclude ZS=ZS6 drops 13/17 losers (76%)
- **Final: n=110  W=106/L=4  WR=96.4%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  AVOID when zscore >+3 extreme

### W15.  `T1=T1c AND BBP=BBP6 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=130  W=113/L=17  WR=86.9%
- Refine: exclude ZS=ZS6 drops 13/17 losers (76%)
- **Final: n=110  W=106/L=4  WR=96.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  AVOID when zscore >+3 extreme

### W16.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=124  W=107/L=17  WR=86.3%
- Refine: exclude ZS=ZS6 drops 13/17 losers (76%)
- **Final: n=104  W=100/L=4  WR=96.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  AVOID when zscore >+3 extreme

### W17.  `H60=H60c AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude H20=H20d drops 15/17 losers (88%)
- **Final: n=75  W=73/L=2  WR=97.3%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 mildly against

### W18.  `BBP=BBP6 AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=115  W=106/L=9  WR=92.2%
- Refine: exclude H60=H60c drops 5/9 losers (56%)
- **Final: n=110  W=106/L=4  WR=96.4%**
- **Dir: SHORT**  •  deep above upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF60 neutral

### W19.  `H60=H60a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude BBP=BBP5 drops 8/12 losers (67%)
- **Final: n=84  W=80/L=4  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W20.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude BBP=BBP5 drops 8/12 losers (67%)
- **Final: n=84  W=80/L=4  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W21.  `H60=H60a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude BBP=BBP5 drops 8/12 losers (67%)
- **Final: n=84  W=80/L=4  WR=95.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W22.  `T1=T1c AND BBP=BBP6 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=110  W=106/L=4  WR=96.4%
- Refine: exclude H20=H20c drops 4/4 losers (100%)
- **Final: n=102  W=102/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF20 neutral

### W23.  `T4=T4c AND BBP=BBP6 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=109  W=100/L=9  WR=91.7%
- Refine: exclude H60=H60c drops 5/9 losers (56%)
- **Final: n=104  W=100/L=4  WR=96.2%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF60 neutral

### W24.  `H20=H20d AND T1=T1c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=108  W=94/L=14  WR=87.0%
- Refine: exclude session_bucket=asia drops 7/14 losers (50%)
- **Final: n=81  W=74/L=7  WR=91.4%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; upper third; RSI 60-70 strong  •  AVOID when session=asia

### W25.  `H20=H20d AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=108  W=94/L=14  WR=87.0%
- Refine: exclude session_bucket=asia drops 7/14 losers (50%)
- **Final: n=81  W=74/L=7  WR=91.4%**
- **Dir: SHORT**  •  HTF20 mildly against; upper third; RSI 60-70 strong  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=165  W=66/L=99  WR=40.0%
- Sharpen: sharpest is H60=H60c (39/99 of losers there)
- **Sharp: n=43  W=4/L=39  WR=9.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF60 neutral

### L02.  `T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=164  W=62/L=102  WR=37.8%
- Sharpen: sharpest is H20=H20a (36/102 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band  •  ONLY when HTF20 aligned WITH trade

### L03.  `T1=T1a AND T4=T4a AND BBP=BBP6`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: sharpest is H20=H20a (20/82 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when HTF20 aligned WITH trade

### L04.  `T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: sharpest is H20=H20a (20/82 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band  •  ONLY when HTF20 aligned WITH trade

### L05.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: sharpest is H20=H20a (20/82 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when HTF20 aligned WITH trade

### L06.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=133  W=51/L=82  WR=38.3%
- Sharpen: sharpest is RSI=RSI4 (42/82 of losers there)
- **Sharp: n=48  W=6/L=42  WR=12.5%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L07.  `BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=127  W=45/L=82  WR=35.4%
- Sharpen: sharpest is RSI=RSI4 (42/82 of losers there)
- **Sharp: n=48  W=6/L=42  WR=12.5%**
- **Dir: LONG**  •  deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L08.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=127  W=45/L=82  WR=35.4%
- Sharpen: sharpest is RSI=RSI4 (42/82 of losers there)
- **Sharp: n=48  W=6/L=42  WR=12.5%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L09.  `H60=H60c AND T4=T4c AND RSI=RSI5`
- Raw: n=107  W=40/L=67  WR=37.4%
- Sharpen: sharpest is session_bucket=ny_mid (39/67 of losers there)
- **Sharp: n=43  W=4/L=39  WR=9.3%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L10.  `H20=H20a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=98  W=36/L=62  WR=36.7%
- Sharpen: sharpest is BBP=BBP6 (24/62 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london_open  •  ONLY when deep above upper band

### L11.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=98  W=36/L=62  WR=36.7%
- Sharpen: sharpest is BBP=BBP6 (24/62 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when deep above upper band

### L12.  `T4=T4c AND ZS=ZS1 AND direction_exec=short`
- Raw: n=98  W=39/L=59  WR=39.8%
- Sharpen: sharpest is H20=H20a (24/59 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when HTF20 aligned WITH trade

### L13.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=97  W=35/L=62  WR=36.1%
- Sharpen: sharpest is H20=H20a (14/62 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L14.  `T1=T1a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=97  W=35/L=62  WR=36.1%
- Sharpen: sharpest is H20=H20a (14/62 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L15.  `T4=T4c AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=94  W=29/L=65  WR=30.9%
- Sharpen: sharpest is H20=H20a (31/65 of losers there)
- **Sharp: n=32  W=1/L=31  WR=3.1%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L16.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=94  W=29/L=65  WR=30.9%
- Sharpen: sharpest is H20=H20a (31/65 of losers there)
- **Sharp: n=32  W=1/L=31  WR=3.1%**
- **Dir: SHORT**  •  upper third; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L17.  `T4=T4c AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=89  W=29/L=60  WR=32.6%
- Sharpen: sharpest is H60=H60c (27/60 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF60 neutral

### L18.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=89  W=29/L=60  WR=32.6%
- Sharpen: sharpest is H60=H60c (27/60 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: SHORT**  •  RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF60 neutral

### L19.  `H60=H60c AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=89  W=33/L=56  WR=37.1%
- Sharpen: sharpest is session_bucket=ny_mid (39/56 of losers there)
- **Sharp: n=43  W=4/L=39  WR=9.3%**
- **Dir: SHORT**  •  HTF60 neutral; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L20.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=86  W=22/L=64  WR=25.6%
- Sharpen: sharpest is session_bucket=ny_mid (31/64 of losers there)
- **Sharp: n=32  W=1/L=31  WR=3.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third; RSI 60-70 strong  •  ONLY when session=ny_mid

### L21.  `H20=H20b AND T1=T1a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=86  W=32/L=54  WR=37.2%
- Sharpen: sharpest is session_bucket=ny_open (24/54 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; upper third; RSI 60-70 strong  •  ONLY when session=ny_open

### L22.  `H20=H20b AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=86  W=32/L=54  WR=37.2%
- Sharpen: sharpest is session_bucket=ny_open (24/54 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; upper third; RSI 60-70 strong  •  ONLY when session=ny_open

### L23.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=85  W=23/L=62  WR=27.1%
- Sharpen: sharpest is H20=H20a (32/62 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L24.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=85  W=23/L=62  WR=27.1%
- Sharpen: sharpest is H20=H20a (32/62 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L25.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=85  W=23/L=62  WR=27.1%
- Sharpen: sharpest is H20=H20a (32/62 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20d(24/17), H20e(27/20) | H20a(21/29) |
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
