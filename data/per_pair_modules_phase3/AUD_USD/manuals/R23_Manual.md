# AUD_USD — R23 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,180**  (W=1,348 / L=832)  -  WR: **61.8%**

## Session distribution

- ny_mid: n=919  W=565/L=354  WR=61.5%
- ny_close: n=590  W=375/L=215  WR=63.6%
- london_open: n=233  W=144/L=89  WR=61.8%
- asia: n=179  W=107/L=72  WR=59.8%
- ny_open: n=158  W=94/L=64  WR=59.5%
- london: n=71  W=40/L=31  WR=56.3%
- asia_late: n=19  W=16/L=3  WR=84.2%
- off_hours: n=11  W=7/L=4  WR=63.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND BBP=BBP6`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep above upper band  •  AVOID when session=london_open

### W02.  `H20=H20a AND T1=T1a AND BBP=BBP6`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when session=london_open

### W03.  `H20=H20a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep above upper band  •  AVOID when session=london_open

### W04.  `H20=H20a AND H60=H60a AND T1=T1a AND BBP=BBP6`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when session=london_open

### W05.  `H20=H20a AND H60=H60a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep above upper band  •  AVOID when session=london_open

### W06.  `H20=H20a AND T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when session=london_open

### W07.  `T1=T1a AND ZS=ZS3 AND session_bucket=ny_close`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude RSI=RSI5 drops 8/10 losers (80%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: ?**  •  1h trend WITH trade; zscore -1 to +1 neutral; session=ny_close  •  AVOID when RSI 60-70 strong

### W08.  `H60=H60a AND T1=T1a AND T4=T4c AND ZS=ZS3`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude BBP=BBP4 drops 4/10 losers (40%)
- **Final: n=58  W=52/L=6  WR=89.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when upper third

### W09.  `H60=H60e AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude RSI=RSI6 drops 3/9 losers (33%)
- **Final: n=61  W=55/L=6  WR=90.2%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=london_open  •  AVOID when RSI 70-80 overbought

### W10.  `T1=T1c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude RSI=RSI6 drops 3/9 losers (33%)
- **Final: n=61  W=55/L=6  WR=90.2%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=london_open  •  AVOID when RSI 70-80 overbought

### W11.  `BBP=BBP4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude RSI=RSI6 drops 3/9 losers (33%)
- **Final: n=61  W=55/L=6  WR=90.2%**
- **Dir: SHORT**  •  upper third; session=london_open  •  AVOID when RSI 70-80 overbought

### W12.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude RSI=RSI6 drops 3/9 losers (33%)
- **Final: n=61  W=55/L=6  WR=90.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; session=london_open  •  AVOID when RSI 70-80 overbought

### W13.  `H60=H60e AND BBP=BBP4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude RSI=RSI6 drops 3/9 losers (33%)
- **Final: n=61  W=55/L=6  WR=90.2%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; session=london_open  •  AVOID when RSI 70-80 overbought

### W14.  `T1=T1c AND BBP=BBP4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude RSI=RSI6 drops 3/9 losers (33%)
- **Final: n=61  W=55/L=6  WR=90.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; session=london_open  •  AVOID when RSI 70-80 overbought

### W15.  `H20=H20d AND T1=T1a AND RSI=RSI4`
- Raw: n=62  W=58/L=4  WR=93.5%
- Refine: exclude ZS=ZS4 drops 4/4 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore +1 to +2 overbought

### W16.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=61  W=55/L=6  WR=90.2%
- Refine: exclude T4=T4a drops 2/6 losers (33%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong; session=london_open  •  AVOID when 4h trend WITH trade

### W17.  `T1=T1c AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=61  W=55/L=6  WR=90.2%
- Refine: exclude T4=T4a drops 2/6 losers (33%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 60-70 strong; session=london_open  •  AVOID when 4h trend WITH trade

### W18.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=61  W=55/L=6  WR=90.2%
- Refine: exclude T4=T4a drops 2/6 losers (33%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: SHORT**  •  upper third; RSI 60-70 strong; session=london_open  •  AVOID when 4h trend WITH trade

### W19.  `T1=T1a AND T4=T4c AND BBP=BBP3 AND direction_exec=long`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude session_bucket=london drops 4/9 losers (44%)
- **Final: n=50  W=45/L=5  WR=90.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; middle of band  •  AVOID when session=london

### W20.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude H20=H20e drops 4/7 losers (57%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; session=london_open  •  AVOID when HTF20 strongly against

### W21.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude H20=H20e drops 4/7 losers (57%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; session=london_open  •  AVOID when HTF20 strongly against

### W22.  `T4=T4c AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude H60=H60a drops 3/7 losers (43%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 60-70 strong; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W23.  `T4=T4c AND BBP=BBP4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude H20=H20e drops 4/7 losers (57%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; session=london_open  •  AVOID when HTF20 strongly against

### W24.  `H20=H20d AND H60=H60a AND RSI=RSI4`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude BBP=BBP4 drops 4/4 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when upper third

### W25.  `H20=H20d AND RSI=RSI4 AND direction_exec=long`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude BBP=BBP4 drops 4/4 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 mildly against; RSI 50-60 upper neutral  •  AVOID when upper third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=253  W=99/L=154  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=253  W=99/L=154  WR=39.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_mid

### L02.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=159  W=61/L=98  WR=38.4%
- Sharpen: sharpest is H60=H60a (18/98 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L03.  `H60=H60e AND T4=T4c AND BBP=BBP6`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is ZS=ZS5 (40/61 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band  •  ONLY when zscore +2 to +3 deep overbought

### L04.  `T1=T1c AND T4=T4c AND BBP=BBP6`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is ZS=ZS5 (40/61 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when zscore +2 to +3 deep overbought

### L05.  `T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is ZS=ZS5 (40/61 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP6`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is ZS=ZS5 (40/61 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when zscore +2 to +3 deep overbought

### L07.  `H60=H60e AND T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is ZS=ZS5 (40/61 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band  •  ONLY when zscore +2 to +3 deep overbought

### L08.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is ZS=ZS5 (40/61 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=98  W=39/L=59  WR=39.8%
- Sharpen: sharpest is ZS=ZS5 (12/59 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_close  •  ONLY when zscore +2 to +3 deep overbought

### L10.  `H20=H20e AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is ZS=ZS5 (28/52 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: ?**  •  HTF20 strongly against; RSI 70-80 overbought; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L11.  `H60=H60e AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is ZS=ZS5 (28/52 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L12.  `T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is ZS=ZS5 (28/52 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L13.  `T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is ZS=ZS5 (28/52 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L14.  `RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is ZS=ZS5 (28/52 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L15.  `H20=H20e AND H60=H60e AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is ZS=ZS5 (28/52 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `H20=H20e AND T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is ZS=ZS5 (28/52 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L17.  `H20=H20e AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is ZS=ZS5 (28/52 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L18.  `H20=H20e AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is ZS=ZS5 (28/52 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 70-80 overbought; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L19.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is ZS=ZS5 (28/52 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L20.  `H60=H60e AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is ZS=ZS5 (28/52 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L21.  `H60=H60e AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is ZS=ZS5 (28/52 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L22.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is ZS=ZS5 (28/52 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is ZS=ZS5 (28/52 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `T4=T4c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is ZS=ZS5 (28/52 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `H20=H20e AND H60=H60e AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=68  W=23/L=45  WR=33.8%
- Sharpen: sharpest is RSI=RSI6 (28/45 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when RSI 70-80 overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(44/35) | H20e(34/44) |
| H60 | H60a(51/46) | H60e(46/52) |
| T1 | T1a(53/46) | T1c(47/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
