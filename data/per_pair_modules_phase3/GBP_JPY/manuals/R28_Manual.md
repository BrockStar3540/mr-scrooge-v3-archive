# GBP_JPY — R28 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,207**  (W=2,433 / L=1,774)  -  WR: **57.8%**

## Session distribution

- asia: n=1217  W=705/L=512  WR=57.9%
- ny_mid: n=1022  W=606/L=416  WR=59.3%
- london_open: n=959  W=536/L=423  WR=55.9%
- london: n=350  W=197/L=153  WR=56.3%
- ny_close: n=303  W=177/L=126  WR=58.4%
- ny_open: n=243  W=147/L=96  WR=60.5%
- asia_late: n=62  W=36/L=26  WR=58.1%
- off_hours: n=51  W=29/L=22  WR=56.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20d AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=134  W=116/L=18  WR=86.6%
- Refine: exclude session_bucket=ny_mid drops 8/18 losers (44%)
- **Final: n=118  W=108/L=10  WR=91.5%**
- **Dir: ?**  •  HTF20 mildly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W02.  `H20=H20d AND H60=H60e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=134  W=116/L=18  WR=86.6%
- Refine: exclude session_bucket=ny_mid drops 8/18 losers (44%)
- **Final: n=118  W=108/L=10  WR=91.5%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W03.  `H20=H20d AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=134  W=116/L=18  WR=86.6%
- Refine: exclude session_bucket=ny_mid drops 8/18 losers (44%)
- **Final: n=118  W=108/L=10  WR=91.5%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W04.  `H20=H20d AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=134  W=116/L=18  WR=86.6%
- Refine: exclude session_bucket=ny_mid drops 8/18 losers (44%)
- **Final: n=118  W=108/L=10  WR=91.5%**
- **Dir: ?**  •  HTF20 mildly against; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W05.  `H20=H20d AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=134  W=116/L=18  WR=86.6%
- Refine: exclude session_bucket=ny_mid drops 8/18 losers (44%)
- **Final: n=118  W=108/L=10  WR=91.5%**
- **Dir: SHORT**  •  HTF20 mildly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W06.  `H60=H60e AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=112  W=103/L=9  WR=92.0%
- Refine: exclude T1=T1a drops 9/9 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend WITH trade

### W07.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=112  W=103/L=9  WR=92.0%
- Refine: exclude T1=T1a drops 9/9 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: SHORT**  •  upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend WITH trade

### W08.  `H60=H60e AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=104  W=96/L=8  WR=92.3%
- Refine: exclude T1=T1a drops 8/8 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when 1h trend WITH trade

### W09.  `RSI=RSI4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=104  W=96/L=8  WR=92.3%
- Refine: exclude T1=T1a drops 8/8 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when 1h trend WITH trade

### W10.  `H60=H60a AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude H20=H20b drops 7/11 losers (64%)
- **Final: n=54  W=50/L=4  WR=92.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 slightly aligned

### W11.  `T1=T1a AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude H20=H20b drops 7/11 losers (64%)
- **Final: n=54  W=50/L=4  WR=92.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 slightly aligned

### W12.  `T4=T4a AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude H20=H20b drops 7/11 losers (64%)
- **Final: n=54  W=50/L=4  WR=92.6%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 slightly aligned

### W13.  `RSI=RSI5 AND ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude H20=H20b drops 7/11 losers (64%)
- **Final: n=54  W=50/L=4  WR=92.6%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 slightly aligned

### W14.  `H20=H20d AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude ZS=ZS3 drops 5/13 losers (38%)
- **Final: n=80  W=72/L=8  WR=90.0%**
- **Dir: ?**  •  HTF20 mildly against; upper third; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W15.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude BBP=BBP3 drops 8/13 losers (62%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when middle of band

### W16.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude BBP=BBP3 drops 8/13 losers (62%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when middle of band

### W17.  `H20=H20d AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=80  W=72/L=8  WR=90.0%
- Refine: exclude H60=H60d drops 5/8 losers (62%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  HTF20 mildly against; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF60 mildly against

### W18.  `H20=H20d AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=80  W=72/L=8  WR=90.0%
- Refine: exclude H60=H60d drops 5/8 losers (62%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  HTF20 mildly against; upper third; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF60 mildly against

### W19.  `H60=H60e AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude ZS=ZS3 drops 5/11 losers (45%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W20.  `T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude ZS=ZS3 drops 5/11 losers (45%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W21.  `RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude ZS=ZS3 drops 5/11 losers (45%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W22.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude ZS=ZS3 drops 5/11 losers (45%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W23.  `H60=H60e AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude ZS=ZS3 drops 5/11 losers (45%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W24.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude ZS=ZS3 drops 5/11 losers (45%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W25.  `H60=H60e AND T1=T1a AND BBP=BBP5`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude H20=H20c drops 11/11 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; just touched upper band  •  AVOID when HTF20 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=413  W=165/L=248  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (117/248 of losers there)
- **Sharp: n=143  W=26/L=117  WR=18.2%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L02.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=243  W=87/L=156  WR=35.8%
- Sharpen: sharpest is direction_exec=long (117/156 of losers there)
- **Sharp: n=143  W=26/L=117  WR=18.2%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when long

### L03.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=237  W=82/L=155  WR=34.6%
- Sharpen: sharpest is T4=T4a (115/155 of losers there)
- **Sharp: n=141  W=26/L=115  WR=18.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L04.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=235  W=78/L=157  WR=33.2%
- Sharpen: sharpest is T4=T4a (117/157 of losers there)
- **Sharp: n=143  W=26/L=117  WR=18.2%**
- **Dir: LONG**  •  upper third; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L05.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=233  W=78/L=155  WR=33.5%
- Sharpen: sharpest is T4=T4a (115/155 of losers there)
- **Sharp: n=141  W=26/L=115  WR=18.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L06.  `H20=H20b AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=227  W=78/L=149  WR=34.4%
- Sharpen: sharpest is RSI=RSI4 (75/149 of losers there)
- **Sharp: n=89  W=14/L=75  WR=15.7%**
- **Dir: ?**  •  HTF20 slightly aligned; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L07.  `H20=H20b AND H60=H60a AND BBP=BBP4`
- Raw: n=214  W=82/L=132  WR=38.3%
- Sharpen: sharpest is RSI=RSI4 (81/132 of losers there)
- **Sharp: n=101  W=20/L=81  WR=19.8%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; upper third  •  ONLY when RSI 50-60 upper neutral

### L08.  `H20=H20b AND T4=T4a AND BBP=BBP4`
- Raw: n=214  W=82/L=132  WR=38.3%
- Sharpen: sharpest is RSI=RSI4 (81/132 of losers there)
- **Sharp: n=101  W=20/L=81  WR=19.8%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; upper third  •  ONLY when RSI 50-60 upper neutral

### L09.  `H20=H20b AND BBP=BBP4 AND direction_exec=long`
- Raw: n=214  W=82/L=132  WR=38.3%
- Sharpen: sharpest is RSI=RSI4 (81/132 of losers there)
- **Sharp: n=101  W=20/L=81  WR=19.8%**
- **Dir: LONG**  •  HTF20 slightly aligned; upper third  •  ONLY when RSI 50-60 upper neutral

### L10.  `H20=H20b AND H60=H60a AND T4=T4a AND BBP=BBP4`
- Raw: n=214  W=82/L=132  WR=38.3%
- Sharpen: sharpest is RSI=RSI4 (81/132 of losers there)
- **Sharp: n=101  W=20/L=81  WR=19.8%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade; upper third  •  ONLY when RSI 50-60 upper neutral

### L11.  `H20=H20b AND H60=H60a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=214  W=82/L=132  WR=38.3%
- Sharpen: sharpest is RSI=RSI4 (81/132 of losers there)
- **Sharp: n=101  W=20/L=81  WR=19.8%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; upper third  •  ONLY when RSI 50-60 upper neutral

### L12.  `H20=H20b AND T4=T4a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=214  W=82/L=132  WR=38.3%
- Sharpen: sharpest is RSI=RSI4 (81/132 of losers there)
- **Sharp: n=101  W=20/L=81  WR=19.8%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade; upper third  •  ONLY when RSI 50-60 upper neutral

### L13.  `T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=209  W=75/L=134  WR=35.9%
- Sharpen: sharpest is H60=H60a (96/134 of losers there)
- **Sharp: n=116  W=20/L=96  WR=17.2%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 aligned WITH trade

### L14.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=209  W=75/L=134  WR=35.9%
- Sharpen: sharpest is H60=H60a (96/134 of losers there)
- **Sharp: n=116  W=20/L=96  WR=17.2%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 aligned WITH trade

### L15.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=202  W=72/L=130  WR=35.6%
- Sharpen: sharpest is T4=T4a (96/130 of losers there)
- **Sharp: n=116  W=20/L=96  WR=17.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L16.  `RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=202  W=72/L=130  WR=35.6%
- Sharpen: sharpest is T4=T4a (96/130 of losers there)
- **Sharp: n=116  W=20/L=96  WR=17.2%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L17.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=202  W=72/L=130  WR=35.6%
- Sharpen: sharpest is T4=T4a (96/130 of losers there)
- **Sharp: n=116  W=20/L=96  WR=17.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L18.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=202  W=72/L=130  WR=35.6%
- Sharpen: sharpest is T4=T4a (96/130 of losers there)
- **Sharp: n=116  W=20/L=96  WR=17.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L19.  `BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=202  W=72/L=130  WR=35.6%
- Sharpen: sharpest is T4=T4a (96/130 of losers there)
- **Sharp: n=116  W=20/L=96  WR=17.2%**
- **Dir: LONG**  •  upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L20.  `ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=193  W=74/L=119  WR=38.3%
- Sharpen: sharpest is RSI=RSI4 (62/119 of losers there)
- **Sharp: n=72  W=10/L=62  WR=13.9%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 50-60 upper neutral

### L21.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=193  W=74/L=119  WR=38.3%
- Sharpen: sharpest is RSI=RSI4 (62/119 of losers there)
- **Sharp: n=72  W=10/L=62  WR=13.9%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 50-60 upper neutral

### L22.  `H60=H60a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=177  W=63/L=114  WR=35.6%
- Sharpen: sharpest is BBP=BBP4 (69/114 of losers there)
- **Sharp: n=81  W=12/L=69  WR=14.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L23.  `RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=177  W=63/L=114  WR=35.6%
- Sharpen: sharpest is BBP=BBP4 (69/114 of losers there)
- **Sharp: n=81  W=12/L=69  WR=14.8%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L24.  `H60=H60a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=177  W=63/L=114  WR=35.6%
- Sharpen: sharpest is BBP=BBP4 (69/114 of losers there)
- **Sharp: n=81  W=12/L=69  WR=14.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L25.  `H20=H20b AND H60=H60a AND ZS=ZS4`
- Raw: n=174  W=58/L=116  WR=33.3%
- Sharpen: sharpest is RSI=RSI4 (75/116 of losers there)
- **Sharp: n=89  W=14/L=75  WR=15.7%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(49/43) | H60a(41/47) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(55/47) | long(45/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
