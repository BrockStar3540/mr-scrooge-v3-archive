# GBP_USD — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,061**  (W=1,907 / L=1,154)  -  WR: **62.3%**

## Session distribution

- ny_mid: n=1138  W=706/L=432  WR=62.0%
- london_open: n=588  W=366/L=222  WR=62.2%
- ny_close: n=354  W=231/L=123  WR=65.3%
- london: n=340  W=211/L=129  WR=62.1%
- ny_open: n=322  W=190/L=132  WR=59.0%
- asia: n=207  W=133/L=74  WR=64.3%
- asia_late: n=59  W=38/L=21  WR=64.4%
- off_hours: n=53  W=32/L=21  WR=60.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=166  W=146/L=20  WR=88.0%
- Refine: no further refinement
- **Final: n=166  W=146/L=20  WR=88.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_mid

### W02.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=166  W=146/L=20  WR=88.0%
- Refine: no further refinement
- **Final: n=166  W=146/L=20  WR=88.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_mid

### W03.  `H20=H20a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=126  W=110/L=16  WR=87.3%
- Refine: exclude H60=H60e drops 11/16 losers (69%)
- **Final: n=88  W=83/L=5  WR=94.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF60 strongly against

### W04.  `T4=T4a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=124  W=113/L=11  WR=91.1%
- Refine: exclude ZS=ZS5 drops 11/11 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 60-70 strong  •  AVOID when zscore +2 to +3 deep overbought

### W05.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=114  W=98/L=16  WR=86.0%
- Refine: exclude session_bucket=off_hours drops 10/16 losers (62%)
- **Final: n=100  W=94/L=6  WR=94.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=off_hours

### W06.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=111  W=99/L=12  WR=89.2%
- Refine: exclude session_bucket=ny_open drops 5/12 losers (42%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W07.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=110  W=94/L=16  WR=85.5%
- Refine: exclude H20=H20a drops 16/16 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W08.  `H20=H20e AND T4=T4a AND direction_exec=long`
- Raw: n=109  W=100/L=9  WR=91.7%
- Refine: exclude ZS=ZS5 drops 7/9 losers (78%)
- **Final: n=94  W=92/L=2  WR=97.9%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade  •  AVOID when zscore +2 to +3 deep overbought

### W09.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=106  W=93/L=13  WR=87.7%
- Refine: exclude H60=H60e drops 8/13 losers (62%)
- **Final: n=88  W=83/L=5  WR=94.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF60 strongly against

### W10.  `H20=H20e AND BBP=BBP2 AND direction_exec=long`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude session_bucket=asia drops 9/15 losers (60%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: LONG**  •  HTF20 strongly against; lower third  •  AVOID when session=asia

### W11.  `T1=T1c AND BBP=BBP2 AND session_bucket=london_open`
- Raw: n=105  W=92/L=13  WR=87.6%
- Refine: exclude RSI=RSI4 drops 11/13 losers (85%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W12.  `H20=H20e AND T1=T1a AND T4=T4a`
- Raw: n=104  W=96/L=8  WR=92.3%
- Refine: exclude ZS=ZS5 drops 7/8 losers (88%)
- **Final: n=89  W=88/L=1  WR=98.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when zscore +2 to +3 deep overbought

### W13.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude session_bucket=off_hours drops 10/14 losers (71%)
- **Final: n=90  W=86/L=4  WR=95.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=off_hours

### W14.  `H60=H60e AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=102  W=90/L=12  WR=88.2%
- Refine: exclude session_bucket=off_hours drops 10/12 losers (83%)
- **Final: n=88  W=86/L=2  WR=97.7%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=off_hours

### W15.  `H20=H20e AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=98  W=90/L=8  WR=91.8%
- Refine: exclude ZS=ZS5 drops 7/8 losers (88%)
- **Final: n=83  W=82/L=1  WR=98.8%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when zscore +2 to +3 deep overbought

### W16.  `H20=H20e AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude RSI=RSI2 drops 3/14 losers (21%)
- **Final: n=90  W=79/L=11  WR=87.8%**
- **Dir: ?**  •  HTF20 strongly against; lower third; session=ny_mid  •  AVOID when RSI 30-40 weak

### W17.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude RSI=RSI2 drops 3/14 losers (21%)
- **Final: n=90  W=79/L=11  WR=87.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; session=ny_mid  •  AVOID when RSI 30-40 weak

### W18.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude T4=T4c drops 12/12 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when 4h trend AGAINST trade

### W19.  `T4=T4a AND BBP=BBP6 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=91  W=80/L=11  WR=87.9%
- Refine: exclude H20=H20e drops 7/11 losers (64%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W20.  `H20=H20e AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude H60=H60d drops 8/8 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; upper third; RSI 60-70 strong  •  AVOID when HTF60 mildly against

### W21.  `T1=T1c AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude RSI=RSI4 drops 9/10 losers (90%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W22.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude RSI=RSI4 drops 9/10 losers (90%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W23.  `H20=H20a AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude T1=T1c drops 11/11 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when 1h trend AGAINST trade

### W24.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude H20=H20a drops 13/13 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W25.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=87  W=79/L=8  WR=90.8%
- Refine: exclude ZS=ZS5 drops 7/8 losers (88%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore +2 to +3 deep overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=232  W=92/L=140  WR=39.7%
- Sharpen: sharpest is T4=T4c (95/140 of losers there)
- **Sharp: n=134  W=39/L=95  WR=29.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L02.  `RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=232  W=92/L=140  WR=39.7%
- Sharpen: sharpest is T4=T4c (95/140 of losers there)
- **Sharp: n=134  W=39/L=95  WR=29.1%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L03.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=232  W=92/L=140  WR=39.7%
- Sharpen: sharpest is T4=T4c (95/140 of losers there)
- **Sharp: n=134  W=39/L=95  WR=29.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L04.  `T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=220  W=88/L=132  WR=40.0%
- Sharpen: sharpest is H20=H20a (52/132 of losers there)
- **Sharp: n=56  W=4/L=52  WR=7.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L05.  `T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=201  W=78/L=123  WR=38.8%
- Sharpen: sharpest is H20=H20a (52/123 of losers there)
- **Sharp: n=56  W=4/L=52  WR=7.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L06.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=201  W=78/L=123  WR=38.8%
- Sharpen: sharpest is H20=H20a (52/123 of losers there)
- **Sharp: n=56  W=4/L=52  WR=7.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L07.  `H20=H20a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=135  W=54/L=81  WR=40.0%
- Sharpen: sharpest is T4=T4c (52/81 of losers there)
- **Sharp: n=56  W=4/L=52  WR=7.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L08.  `H20=H20a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=135  W=54/L=81  WR=40.0%
- Sharpen: sharpest is T4=T4c (52/81 of losers there)
- **Sharp: n=56  W=4/L=52  WR=7.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L09.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=134  W=39/L=95  WR=29.1%
- Sharpen: sharpest is H20=H20a (36/95 of losers there)
- **Sharp: n=40  W=4/L=36  WR=10.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L10.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=134  W=39/L=95  WR=29.1%
- Sharpen: sharpest is H20=H20a (36/95 of losers there)
- **Sharp: n=40  W=4/L=36  WR=10.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L11.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=128  W=50/L=78  WR=39.1%
- Sharpen: sharpest is session_bucket=london (17/78 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=london

### L12.  `T1=T1a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is direction_exec=long (76/77 of losers there)
- **Sharp: n=111  W=35/L=76  WR=31.5%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when long

### L13.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is direction_exec=long (76/77 of losers there)
- **Sharp: n=111  W=35/L=76  WR=31.5%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when long

### L14.  `RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=125  W=42/L=83  WR=33.6%
- Sharpen: sharpest is session_bucket=ny_mid (28/83 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L15.  `BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=125  W=42/L=83  WR=33.6%
- Sharpen: sharpest is session_bucket=ny_mid (28/83 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: LONG**  •  upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L16.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=121  W=45/L=76  WR=37.2%
- Sharpen: sharpest is ZS=ZS5 (33/76 of losers there)
- **Sharp: n=38  W=5/L=33  WR=13.2%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L17.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=121  W=45/L=76  WR=37.2%
- Sharpen: sharpest is ZS=ZS5 (33/76 of losers there)
- **Sharp: n=38  W=5/L=33  WR=13.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L18.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=112  W=43/L=69  WR=38.4%
- Sharpen: sharpest is T4=T4c (27/69 of losers there)
- **Sharp: n=31  W=4/L=27  WR=12.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L19.  `T1=T1a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=111  W=35/L=76  WR=31.5%
- Sharpen: sharpest is session_bucket=ny_mid (25/76 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L20.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=111  W=44/L=67  WR=39.6%
- Sharpen: sharpest is ZS=ZS4 (18/67 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L21.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is H60=H60a (22/62 of losers there)
- **Sharp: n=28  W=6/L=22  WR=21.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L22.  `H20=H20a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=95  W=32/L=63  WR=33.7%
- Sharpen: sharpest is session_bucket=ny_open (13/63 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=ny_open

### L23.  `T4=T4c AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=93  W=24/L=69  WR=25.8%
- Sharpen: sharpest is ZS=ZS6 (20/69 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  ONLY when zscore >+3 extreme

### L24.  `T4=T4c AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is H20=H20a (16/57 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L25.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is T1=T1c (27/56 of losers there)
- **Sharp: n=35  W=8/L=27  WR=22.9%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(54/44) | H20a(45/55) |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
