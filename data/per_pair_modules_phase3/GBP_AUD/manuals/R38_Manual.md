# GBP_AUD — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,918**  (W=2,338 / L=1,580)  -  WR: **59.7%**

## Session distribution

- london_open: n=1057  W=645/L=412  WR=61.0%
- asia: n=970  W=591/L=379  WR=60.9%
- ny_open: n=579  W=344/L=235  WR=59.4%
- ny_mid: n=438  W=258/L=180  WR=58.9%
- london: n=325  W=188/L=137  WR=57.8%
- ny_close: n=306  W=176/L=130  WR=57.5%
- asia_late: n=191  W=114/L=77  WR=59.7%
- off_hours: n=52  W=22/L=30  WR=42.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=143  W=135/L=8  WR=94.4%
- Refine: exclude H20=H20e drops 7/8 losers (88%)
- **Final: n=118  W=117/L=1  WR=99.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_open  •  AVOID when HTF20 strongly against

### W02.  `T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=143  W=135/L=8  WR=94.4%
- Refine: exclude H20=H20e drops 7/8 losers (88%)
- **Final: n=118  W=117/L=1  WR=99.2%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when HTF20 strongly against

### W03.  `RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=143  W=135/L=8  WR=94.4%
- Refine: exclude H20=H20e drops 7/8 losers (88%)
- **Final: n=118  W=117/L=1  WR=99.2%**
- **Dir: LONG**  •  RSI 60-70 strong; session=ny_open  •  AVOID when HTF20 strongly against

### W04.  `H60=H60e AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=143  W=135/L=8  WR=94.4%
- Refine: exclude H20=H20e drops 7/8 losers (88%)
- **Final: n=118  W=117/L=1  WR=99.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when HTF20 strongly against

### W05.  `H60=H60e AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=143  W=135/L=8  WR=94.4%
- Refine: exclude H20=H20e drops 7/8 losers (88%)
- **Final: n=118  W=117/L=1  WR=99.2%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_open  •  AVOID when HTF20 strongly against

### W06.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=143  W=135/L=8  WR=94.4%
- Refine: exclude H20=H20e drops 7/8 losers (88%)
- **Final: n=118  W=117/L=1  WR=99.2%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when HTF20 strongly against

### W07.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=139  W=121/L=18  WR=87.1%
- Refine: exclude H20=H20a drops 18/18 losers (100%)
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W08.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=139  W=121/L=18  WR=87.1%
- Refine: exclude H20=H20a drops 18/18 losers (100%)
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W09.  `H20=H20a AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=122  W=116/L=6  WR=95.1%
- Refine: exclude H60=H60e drops 5/6 losers (83%)
- **Final: n=79  W=78/L=1  WR=98.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when HTF60 strongly against

### W10.  `H60=H60a AND T4=T4c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=119  W=107/L=12  WR=89.9%
- Refine: exclude H20=H20e drops 7/12 losers (58%)
- **Final: n=104  W=99/L=5  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W11.  `T4=T4c AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=119  W=107/L=12  WR=89.9%
- Refine: exclude H20=H20e drops 7/12 losers (58%)
- **Final: n=104  W=99/L=5  WR=95.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W12.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=119  W=103/L=16  WR=86.6%
- Refine: exclude H20=H20a drops 16/16 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W13.  `T4=T4a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=119  W=103/L=16  WR=86.6%
- Refine: exclude H20=H20a drops 16/16 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W14.  `H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude H20=H20e drops 17/17 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF20 strongly against

### W15.  `T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude H20=H20e drops 17/17 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF20 strongly against

### W16.  `T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude H20=H20e drops 17/17 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF20 strongly against

### W17.  `H60=H60e AND T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude H20=H20e drops 17/17 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF20 strongly against

### W18.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude H20=H20e drops 17/17 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF20 strongly against

### W19.  `T1=T1a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude H20=H20e drops 17/17 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF20 strongly against

### W20.  `T1=T1a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=109  W=95/L=14  WR=87.2%
- Refine: exclude RSI=RSI4 drops 14/14 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W21.  `H60=H60a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=108  W=103/L=5  WR=95.4%
- Refine: exclude H20=H20a drops 4/5 losers (80%)
- **Final: n=78  W=77/L=1  WR=98.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W22.  `BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=108  W=103/L=5  WR=95.4%
- Refine: exclude H20=H20a drops 4/5 losers (80%)
- **Final: n=78  W=77/L=1  WR=98.7%**
- **Dir: SHORT**  •  upper third; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W23.  `H60=H60a AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=108  W=103/L=5  WR=95.4%
- Refine: exclude H20=H20a drops 4/5 losers (80%)
- **Final: n=78  W=77/L=1  WR=98.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W24.  `H20=H20c AND T1=T1a AND ZS=ZS5`
- Raw: n=101  W=91/L=10  WR=90.1%
- Refine: exclude BBP=BBP5 drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W25.  `H20=H20a AND RSI=RSI4 AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=100  W=94/L=6  WR=94.0%
- Refine: exclude BBP=BBP5 drops 6/6 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when just touched upper band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1c AND RSI=RSI5`
- Raw: n=297  W=98/L=199  WR=33.0%
- Sharpen: sharpest is session_bucket=ny_open (87/199 of losers there)
- **Sharp: n=101  W=14/L=87  WR=13.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_open

### L02.  `H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=297  W=98/L=199  WR=33.0%
- Sharpen: sharpest is session_bucket=ny_open (87/199 of losers there)
- **Sharp: n=101  W=14/L=87  WR=13.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=ny_open

### L03.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=297  W=98/L=199  WR=33.0%
- Sharpen: sharpest is session_bucket=ny_open (87/199 of losers there)
- **Sharp: n=101  W=14/L=87  WR=13.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_open

### L04.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=297  W=98/L=199  WR=33.0%
- Sharpen: sharpest is session_bucket=ny_open (87/199 of losers there)
- **Sharp: n=101  W=14/L=87  WR=13.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_open

### L05.  `H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=220  W=79/L=141  WR=35.9%
- Sharpen: sharpest is H20=H20b (44/141 of losers there)
- **Sharp: n=44  W=0/L=44  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 slightly aligned

### L06.  `T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=220  W=79/L=141  WR=35.9%
- Sharpen: sharpest is H20=H20b (44/141 of losers there)
- **Sharp: n=44  W=0/L=44  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 slightly aligned

### L07.  `T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=220  W=79/L=141  WR=35.9%
- Sharpen: sharpest is H20=H20b (44/141 of losers there)
- **Sharp: n=44  W=0/L=44  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 slightly aligned

### L08.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=220  W=79/L=141  WR=35.9%
- Sharpen: sharpest is H20=H20b (44/141 of losers there)
- **Sharp: n=44  W=0/L=44  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 slightly aligned

### L09.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=220  W=79/L=141  WR=35.9%
- Sharpen: sharpest is H20=H20b (44/141 of losers there)
- **Sharp: n=44  W=0/L=44  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 slightly aligned

### L10.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=220  W=79/L=141  WR=35.9%
- Sharpen: sharpest is H20=H20b (44/141 of losers there)
- **Sharp: n=44  W=0/L=44  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 slightly aligned

### L11.  `H20=H20e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=217  W=80/L=137  WR=36.9%
- Sharpen: sharpest is session_bucket=london_open (46/137 of losers there)
- **Sharp: n=49  W=3/L=46  WR=6.1%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L12.  `H20=H20e AND H60=H60e AND ZS=ZS5`
- Raw: n=209  W=83/L=126  WR=39.7%
- Sharpen: sharpest is session_bucket=london_open (37/126 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L13.  `H20=H20e AND ZS=ZS5 AND direction_exec=long`
- Raw: n=209  W=83/L=126  WR=39.7%
- Sharpen: sharpest is session_bucket=london_open (37/126 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L14.  `H20=H20e AND H60=H60e AND T1=T1a AND ZS=ZS5`
- Raw: n=209  W=83/L=126  WR=39.7%
- Sharpen: sharpest is session_bucket=london_open (37/126 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L15.  `H20=H20e AND H60=H60e AND ZS=ZS5 AND direction_exec=long`
- Raw: n=209  W=83/L=126  WR=39.7%
- Sharpen: sharpest is session_bucket=london_open (37/126 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L16.  `H20=H20e AND T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=209  W=83/L=126  WR=39.7%
- Sharpen: sharpest is session_bucket=london_open (37/126 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L17.  `T1=T1c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=198  W=70/L=128  WR=35.4%
- Sharpen: sharpest is T4=T4a (49/128 of losers there)
- **Sharp: n=49  W=0/L=49  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=london_open  •  ONLY when 4h trend WITH trade

### L18.  `T1=T1c AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=175  W=54/L=121  WR=30.9%
- Sharpen: sharpest is T4=T4a (48/121 of losers there)
- **Sharp: n=48  W=0/L=48  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=london_open  •  ONLY when 4h trend WITH trade

### L19.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=175  W=54/L=121  WR=30.9%
- Sharpen: sharpest is T4=T4a (48/121 of losers there)
- **Sharp: n=48  W=0/L=48  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=london_open  •  ONLY when 4h trend WITH trade

### L20.  `H20=H20e AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=167  W=63/L=104  WR=37.7%
- Sharpen: sharpest is session_bucket=london_open (28/104 of losers there)
- **Sharp: n=31  W=3/L=28  WR=9.7%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L21.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=164  W=62/L=102  WR=37.8%
- Sharpen: sharpest is T4=T4a (75/102 of losers there)
- **Sharp: n=101  W=26/L=75  WR=25.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L22.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=162  W=60/L=102  WR=37.0%
- Sharpen: sharpest is T4=T4a (75/102 of losers there)
- **Sharp: n=101  W=26/L=75  WR=25.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L23.  `H20=H20e AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=162  W=60/L=102  WR=37.0%
- Sharpen: sharpest is T4=T4a (75/102 of losers there)
- **Sharp: n=101  W=26/L=75  WR=25.7%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L24.  `H60=H60a AND T1=T1c AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=147  W=54/L=93  WR=36.7%
- Sharpen: sharpest is H20=H20a (68/93 of losers there)
- **Sharp: n=86  W=18/L=68  WR=20.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L25.  `T1=T1c AND ZS=ZS4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=147  W=54/L=93  WR=36.7%
- Sharpen: sharpest is H20=H20a (68/93 of losers there)
- **Sharp: n=86  W=18/L=68  WR=20.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=london_open  •  ONLY when HTF20 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(43/30) | H20e(29/41) |
| H60 | H60a(53/47) | H60e(47/53) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/47) | long(47/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
