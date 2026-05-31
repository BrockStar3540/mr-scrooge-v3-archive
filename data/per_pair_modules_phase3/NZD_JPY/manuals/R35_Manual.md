# NZD_JPY — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,144**  (W=1,996 / L=1,148)  -  WR: **63.5%**

## Session distribution

- asia: n=961  W=629/L=332  WR=65.5%
- ny_mid: n=465  W=290/L=175  WR=62.4%
- ny_open: n=436  W=273/L=163  WR=62.6%
- london_open: n=409  W=249/L=160  WR=60.9%
- ny_close: n=356  W=231/L=125  WR=64.9%
- london: n=256  W=164/L=92  WR=64.1%
- off_hours: n=142  W=84/L=58  WR=59.2%
- asia_late: n=119  W=76/L=43  WR=63.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=288  W=246/L=42  WR=85.4%
- Refine: exclude session_bucket=london_open drops 15/42 losers (36%)
- **Final: n=259  W=232/L=27  WR=89.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W02.  `T4=T4a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=205  W=189/L=16  WR=92.2%
- Refine: exclude BBP=BBP4 drops 15/16 losers (94%)
- **Final: n=120  W=119/L=1  WR=99.2%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W03.  `H60=H60a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=201  W=181/L=20  WR=90.0%
- Refine: exclude ZS=ZS4 drops 16/20 losers (80%)
- **Final: n=104  W=100/L=4  WR=96.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore +1 to +2 overbought

### W04.  `T1=T1a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=201  W=181/L=20  WR=90.0%
- Refine: exclude ZS=ZS4 drops 16/20 losers (80%)
- **Final: n=104  W=100/L=4  WR=96.2%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore +1 to +2 overbought

### W05.  `RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=201  W=181/L=20  WR=90.0%
- Refine: exclude ZS=ZS4 drops 16/20 losers (80%)
- **Final: n=104  W=100/L=4  WR=96.2%**
- **Dir: LONG**  •  RSI 60-70 strong; session=asia  •  AVOID when zscore +1 to +2 overbought

### W06.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=201  W=181/L=20  WR=90.0%
- Refine: exclude ZS=ZS4 drops 16/20 losers (80%)
- **Final: n=104  W=100/L=4  WR=96.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore +1 to +2 overbought

### W07.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=201  W=181/L=20  WR=90.0%
- Refine: exclude ZS=ZS4 drops 16/20 losers (80%)
- **Final: n=104  W=100/L=4  WR=96.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore +1 to +2 overbought

### W08.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=201  W=181/L=20  WR=90.0%
- Refine: exclude ZS=ZS4 drops 16/20 losers (80%)
- **Final: n=104  W=100/L=4  WR=96.2%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore +1 to +2 overbought

### W09.  `T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=199  W=173/L=26  WR=86.9%
- Refine: exclude ZS=ZS4 drops 19/26 losers (73%)
- **Final: n=105  W=98/L=7  WR=93.3%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore +1 to +2 overbought

### W10.  `H20=H20a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=197  W=171/L=26  WR=86.8%
- Refine: exclude BBP=BBP4 drops 23/26 losers (88%)
- **Final: n=116  W=113/L=3  WR=97.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W11.  `T1=T1a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=197  W=171/L=26  WR=86.8%
- Refine: exclude BBP=BBP4 drops 23/26 losers (88%)
- **Final: n=116  W=113/L=3  WR=97.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W12.  `RSI=RSI6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=197  W=171/L=26  WR=86.8%
- Refine: exclude BBP=BBP4 drops 23/26 losers (88%)
- **Final: n=116  W=113/L=3  WR=97.4%**
- **Dir: LONG**  •  RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W13.  `H20=H20a AND T1=T1a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=197  W=171/L=26  WR=86.8%
- Refine: exclude BBP=BBP4 drops 23/26 losers (88%)
- **Final: n=116  W=113/L=3  WR=97.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W14.  `H20=H20a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=197  W=171/L=26  WR=86.8%
- Refine: exclude BBP=BBP4 drops 23/26 losers (88%)
- **Final: n=116  W=113/L=3  WR=97.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W15.  `T1=T1a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=197  W=171/L=26  WR=86.8%
- Refine: exclude BBP=BBP4 drops 23/26 losers (88%)
- **Final: n=116  W=113/L=3  WR=97.4%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W16.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=193  W=173/L=20  WR=89.6%
- Refine: exclude ZS=ZS4 drops 16/20 losers (80%)
- **Final: n=102  W=98/L=4  WR=96.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore +1 to +2 overbought

### W17.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=193  W=173/L=20  WR=89.6%
- Refine: exclude ZS=ZS4 drops 16/20 losers (80%)
- **Final: n=102  W=98/L=4  WR=96.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore +1 to +2 overbought

### W18.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=193  W=173/L=20  WR=89.6%
- Refine: exclude ZS=ZS4 drops 16/20 losers (80%)
- **Final: n=102  W=98/L=4  WR=96.1%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore +1 to +2 overbought

### W19.  `H20=H20a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=190  W=162/L=28  WR=85.3%
- Refine: exclude H60=H60a drops 26/28 losers (93%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=asia  •  AVOID when HTF60 aligned WITH trade

### W20.  `H60=H60a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=178  W=163/L=15  WR=91.6%
- Refine: exclude BBP=BBP4 drops 14/15 losers (93%)
- **Final: n=112  W=111/L=1  WR=99.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W21.  `H20=H20a AND H60=H60a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=178  W=163/L=15  WR=91.6%
- Refine: exclude BBP=BBP4 drops 14/15 losers (93%)
- **Final: n=112  W=111/L=1  WR=99.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W22.  `H20=H20a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=178  W=163/L=15  WR=91.6%
- Refine: exclude BBP=BBP4 drops 14/15 losers (93%)
- **Final: n=112  W=111/L=1  WR=99.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W23.  `H60=H60a AND T1=T1a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=178  W=163/L=15  WR=91.6%
- Refine: exclude BBP=BBP4 drops 14/15 losers (93%)
- **Final: n=112  W=111/L=1  WR=99.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W24.  `H60=H60a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=178  W=163/L=15  WR=91.6%
- Refine: exclude BBP=BBP4 drops 14/15 losers (93%)
- **Final: n=112  W=111/L=1  WR=99.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W25.  `H60=H60a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=178  W=163/L=15  WR=91.6%
- Refine: exclude BBP=BBP4 drops 14/15 losers (93%)
- **Final: n=112  W=111/L=1  WR=99.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T4=T4c AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=180  W=68/L=112  WR=37.8%
- Sharpen: sharpest is session_bucket=ny_mid (52/112 of losers there)
- **Sharp: n=59  W=7/L=52  WR=11.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L02.  `T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=179  W=68/L=111  WR=38.0%
- Sharpen: sharpest is ZS=ZS5 (37/111 of losers there)
- **Sharp: n=42  W=5/L=37  WR=11.9%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L03.  `H60=H60e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=177  W=60/L=117  WR=33.9%
- Sharpen: sharpest is ZS=ZS5 (40/117 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L04.  `T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=177  W=60/L=117  WR=33.9%
- Sharpen: sharpest is ZS=ZS5 (40/117 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L05.  `RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=177  W=60/L=117  WR=33.9%
- Sharpen: sharpest is ZS=ZS5 (40/117 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=177  W=60/L=117  WR=33.9%
- Sharpen: sharpest is ZS=ZS5 (40/117 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L07.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=177  W=60/L=117  WR=33.9%
- Sharpen: sharpest is ZS=ZS5 (40/117 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L08.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=177  W=60/L=117  WR=33.9%
- Sharpen: sharpest is ZS=ZS5 (40/117 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=171  W=60/L=111  WR=35.1%
- Sharpen: sharpest is ZS=ZS5 (37/111 of losers there)
- **Sharp: n=40  W=3/L=37  WR=7.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L10.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=171  W=60/L=111  WR=35.1%
- Sharpen: sharpest is ZS=ZS5 (37/111 of losers there)
- **Sharp: n=40  W=3/L=37  WR=7.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L11.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=171  W=60/L=111  WR=35.1%
- Sharpen: sharpest is ZS=ZS5 (37/111 of losers there)
- **Sharp: n=40  W=3/L=37  WR=7.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L12.  `H20=H20e AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is H60=H60e (92/93 of losers there)
- **Sharp: n=121  W=29/L=92  WR=24.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 strongly against

### L13.  `T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is H60=H60e (92/93 of losers there)
- **Sharp: n=121  W=29/L=92  WR=24.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 strongly against

### L14.  `RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is H60=H60e (92/93 of losers there)
- **Sharp: n=121  W=29/L=92  WR=24.0%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 strongly against

### L15.  `H20=H20e AND T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is H60=H60e (92/93 of losers there)
- **Sharp: n=121  W=29/L=92  WR=24.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 strongly against

### L16.  `H20=H20e AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is H60=H60e (92/93 of losers there)
- **Sharp: n=121  W=29/L=92  WR=24.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 strongly against

### L17.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is H60=H60e (92/93 of losers there)
- **Sharp: n=121  W=29/L=92  WR=24.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF60 strongly against

### L18.  `T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=140  W=37/L=103  WR=26.4%
- Sharpen: sharpest is ZS=ZS5 (54/103 of losers there)
- **Sharp: n=63  W=9/L=54  WR=14.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L19.  `H20=H20e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=139  W=45/L=94  WR=32.4%
- Sharpen: sharpest is ZS=ZS5 (31/94 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L20.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=139  W=45/L=94  WR=32.4%
- Sharpen: sharpest is ZS=ZS5 (31/94 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L21.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=139  W=45/L=94  WR=32.4%
- Sharpen: sharpest is ZS=ZS5 (31/94 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L22.  `H20=H20e AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=139  W=45/L=94  WR=32.4%
- Sharpen: sharpest is ZS=ZS5 (31/94 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `H20=H20e AND H60=H60e AND BBP=BBP6`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=134  W=52/L=82  WR=38.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep above upper band

### L24.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP6`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=134  W=52/L=82  WR=38.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; deep above upper band

### L25.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP6`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=134  W=52/L=82  WR=38.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; deep above upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(57/40) | H20e(40/58) |
| H60 | H60a(56/38) | H60e(38/56) |
| T1 | T1a(59/41) | T1c(41/59) |
| T4 | T4a(59/41) | T4c(41/59) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(59/41) | short(41/59) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
