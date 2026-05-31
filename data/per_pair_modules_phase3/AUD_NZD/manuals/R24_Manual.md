# AUD_NZD — R24 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,833**  (W=1,800 / L=1,033)  -  WR: **63.5%**

## Session distribution

- asia: n=1296  W=814/L=482  WR=62.8%
- london_open: n=590  W=375/L=215  WR=63.6%
- ny_mid: n=422  W=280/L=142  WR=66.4%
- ny_open: n=204  W=134/L=70  WR=65.7%
- london: n=141  W=85/L=56  WR=60.3%
- ny_close: n=103  W=65/L=38  WR=63.1%
- asia_late: n=39  W=25/L=14  WR=64.1%
- off_hours: n=38  W=22/L=16  WR=57.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T4=T4a AND BBP=BBP6`
- Raw: n=147  W=128/L=19  WR=87.1%
- Refine: exclude RSI=RSI7 drops 6/19 losers (32%)
- **Final: n=141  W=128/L=13  WR=90.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when RSI>80 extreme overbought

### W02.  `H20=H20a AND H60=H60a AND T4=T4a AND BBP=BBP6`
- Raw: n=147  W=128/L=19  WR=87.1%
- Refine: exclude RSI=RSI7 drops 6/19 losers (32%)
- **Final: n=141  W=128/L=13  WR=90.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when RSI>80 extreme overbought

### W03.  `H20=H20a AND T1=T1a AND T4=T4a AND BBP=BBP6`
- Raw: n=147  W=128/L=19  WR=87.1%
- Refine: exclude RSI=RSI7 drops 6/19 losers (32%)
- **Final: n=141  W=128/L=13  WR=90.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when RSI>80 extreme overbought

### W04.  `H20=H20a AND T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=147  W=128/L=19  WR=87.1%
- Refine: exclude RSI=RSI7 drops 6/19 losers (32%)
- **Final: n=141  W=128/L=13  WR=90.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when RSI>80 extreme overbought

### W05.  `H20=H20a AND T4=T4a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=147  W=126/L=21  WR=85.7%
- Refine: no further refinement
- **Final: n=147  W=126/L=21  WR=85.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought

### W06.  `T4=T4a AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=141  W=123/L=18  WR=87.2%
- Refine: exclude ZS=ZS5 drops 18/18 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; session=asia  •  AVOID when zscore +2 to +3 deep overbought

### W07.  `H20=H20a AND T4=T4a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=139  W=119/L=20  WR=85.6%
- Refine: exclude RSI=RSI7 drops 4/20 losers (20%)
- **Final: n=131  W=115/L=16  WR=87.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when RSI>80 extreme overbought

### W08.  `H20=H20a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=135  W=117/L=18  WR=86.7%
- Refine: exclude session_bucket=london_open drops 6/18 losers (33%)
- **Final: n=113  W=101/L=12  WR=89.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W09.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=129  W=111/L=18  WR=86.0%
- Refine: exclude session_bucket=london_open drops 6/18 losers (33%)
- **Final: n=107  W=95/L=12  WR=88.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W10.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=129  W=111/L=18  WR=86.0%
- Refine: exclude session_bucket=london_open drops 6/18 losers (33%)
- **Final: n=107  W=95/L=12  WR=88.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W11.  `H20=H20a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=129  W=111/L=18  WR=86.0%
- Refine: exclude session_bucket=london_open drops 6/18 losers (33%)
- **Final: n=107  W=95/L=12  WR=88.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W12.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=127  W=111/L=16  WR=87.4%
- Refine: exclude session_bucket=london drops 3/16 losers (19%)
- **Final: n=123  W=110/L=13  WR=89.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W13.  `T4=T4a AND BBP=BBP6 AND RSI=RSI6`
- Raw: n=125  W=108/L=17  WR=86.4%
- Refine: exclude H20=H20d drops 6/17 losers (35%)
- **Final: n=119  W=108/L=11  WR=90.8%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 70-80 overbought  •  AVOID when HTF20 mildly against

### W14.  `H60=H60a AND T4=T4a AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=123  W=105/L=18  WR=85.4%
- Refine: exclude ZS=ZS5 drops 18/18 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band; session=asia  •  AVOID when zscore +2 to +3 deep overbought

### W15.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=123  W=105/L=18  WR=85.4%
- Refine: exclude ZS=ZS5 drops 18/18 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band; session=asia  •  AVOID when zscore +2 to +3 deep overbought

### W16.  `T4=T4a AND BBP=BBP6 AND direction_exec=long AND session_bucket=asia`
- Raw: n=123  W=105/L=18  WR=85.4%
- Refine: exclude ZS=ZS5 drops 18/18 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band; session=asia  •  AVOID when zscore +2 to +3 deep overbought

### W17.  `T4=T4a AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=112  W=101/L=11  WR=90.2%
- Refine: exclude H20=H20a drops 7/11 losers (64%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W18.  `H20=H20c AND H60=H60a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude ZS=ZS2 drops 5/12 losers (42%)
- **Final: n=92  W=85/L=7  WR=92.4%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -2 to -1 oversold

### W19.  `H20=H20c AND T1=T1a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude ZS=ZS2 drops 5/12 losers (42%)
- **Final: n=92  W=85/L=7  WR=92.4%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -2 to -1 oversold

### W20.  `H20=H20c AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude ZS=ZS2 drops 5/12 losers (42%)
- **Final: n=92  W=85/L=7  WR=92.4%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -2 to -1 oversold

### W21.  `H20=H20c AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude ZS=ZS2 drops 5/12 losers (42%)
- **Final: n=92  W=85/L=7  WR=92.4%**
- **Dir: LONG**  •  HTF20 neutral; RSI 60-70 strong; session=asia  •  AVOID when zscore -2 to -1 oversold

### W22.  `H60=H60a AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude H20=H20a drops 10/14 losers (71%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W23.  `T1=T1a AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude H20=H20a drops 10/14 losers (71%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: ?**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W24.  `ZS=ZS5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude H20=H20a drops 10/14 losers (71%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: LONG**  •  zscore +2 to +3 deep overbought; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W25.  `H20=H20a AND T4=T4a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude session_bucket=london drops 3/14 losers (21%)
- **Final: n=93  W=82/L=11  WR=88.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched upper band; RSI 60-70 strong  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=340  W=135/L=205  WR=39.7%
- Sharpen: sharpest is H20=H20e (157/205 of losers there)
- **Sharp: n=240  W=83/L=157  WR=34.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L02.  `T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=340  W=135/L=205  WR=39.7%
- Sharpen: sharpest is H20=H20e (157/205 of losers there)
- **Sharp: n=240  W=83/L=157  WR=34.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L03.  `T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=340  W=135/L=205  WR=39.7%
- Sharpen: sharpest is H20=H20e (157/205 of losers there)
- **Sharp: n=240  W=83/L=157  WR=34.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L04.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=340  W=135/L=205  WR=39.7%
- Sharpen: sharpest is H20=H20e (157/205 of losers there)
- **Sharp: n=240  W=83/L=157  WR=34.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L05.  `H60=H60e AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=340  W=135/L=205  WR=39.7%
- Sharpen: sharpest is H20=H20e (157/205 of losers there)
- **Sharp: n=240  W=83/L=157  WR=34.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L06.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=340  W=135/L=205  WR=39.7%
- Sharpen: sharpest is H20=H20e (157/205 of losers there)
- **Sharp: n=240  W=83/L=157  WR=34.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L07.  `H20=H20e AND T4=T4c AND ZS=ZS5`
- Raw: n=240  W=83/L=157  WR=34.6%
- Sharpen: sharpest is RSI=RSI6 (76/157 of losers there)
- **Sharp: n=103  W=27/L=76  WR=26.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L08.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=240  W=83/L=157  WR=34.6%
- Sharpen: sharpest is RSI=RSI6 (76/157 of losers there)
- **Sharp: n=103  W=27/L=76  WR=26.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L09.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=240  W=83/L=157  WR=34.6%
- Sharpen: sharpest is RSI=RSI6 (76/157 of losers there)
- **Sharp: n=103  W=27/L=76  WR=26.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L10.  `H20=H20e AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=240  W=83/L=157  WR=34.6%
- Sharpen: sharpest is RSI=RSI6 (76/157 of losers there)
- **Sharp: n=103  W=27/L=76  WR=26.2%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L11.  `H20=H20e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=224  W=80/L=144  WR=35.7%
- Sharpen: sharpest is ZS=ZS5 (41/144 of losers there)
- **Sharp: n=48  W=7/L=41  WR=14.6%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L12.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=212  W=80/L=132  WR=37.7%
- Sharpen: sharpest is ZS=ZS5 (34/132 of losers there)
- **Sharp: n=41  W=7/L=34  WR=17.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L13.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=212  W=80/L=132  WR=37.7%
- Sharpen: sharpest is ZS=ZS5 (34/132 of losers there)
- **Sharp: n=41  W=7/L=34  WR=17.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L14.  `H20=H20e AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=212  W=80/L=132  WR=37.7%
- Sharpen: sharpest is ZS=ZS5 (34/132 of losers there)
- **Sharp: n=41  W=7/L=34  WR=17.1%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L15.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=204  W=80/L=124  WR=39.2%
- Sharpen: sharpest is ZS=ZS5 (34/124 of losers there)
- **Sharp: n=41  W=7/L=34  WR=17.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `H20=H20e AND T4=T4c AND BBP=BBP5`
- Raw: n=171  W=66/L=105  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_mid (34/105 of losers there)
- **Sharp: n=45  W=11/L=34  WR=24.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched upper band  •  ONLY when session=ny_mid

### L17.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP5`
- Raw: n=171  W=66/L=105  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_mid (34/105 of losers there)
- **Sharp: n=45  W=11/L=34  WR=24.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; just touched upper band  •  ONLY when session=ny_mid

### L18.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP5`
- Raw: n=171  W=66/L=105  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_mid (34/105 of losers there)
- **Sharp: n=45  W=11/L=34  WR=24.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band  •  ONLY when session=ny_mid

### L19.  `H20=H20e AND T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=171  W=66/L=105  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_mid (34/105 of losers there)
- **Sharp: n=45  W=11/L=34  WR=24.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L20.  `H20=H20e AND T4=T4c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=171  W=66/L=105  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_mid (34/105 of losers there)
- **Sharp: n=45  W=11/L=34  WR=24.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched upper band  •  ONLY when session=ny_mid

### L21.  `T4=T4c AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=160  W=51/L=109  WR=31.9%
- Sharpen: sharpest is session_bucket=london_open (36/109 of losers there)
- **Sharp: n=38  W=2/L=36  WR=5.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L22.  `H60=H60e AND T4=T4c AND BBP=BBP6`
- Raw: n=160  W=54/L=106  WR=33.8%
- Sharpen: sharpest is ZS=ZS5 (73/106 of losers there)
- **Sharp: n=102  W=29/L=73  WR=28.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `T1=T1c AND T4=T4c AND BBP=BBP6`
- Raw: n=160  W=54/L=106  WR=33.8%
- Sharpen: sharpest is ZS=ZS5 (73/106 of losers there)
- **Sharp: n=102  W=29/L=73  WR=28.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=160  W=54/L=106  WR=33.8%
- Sharpen: sharpest is ZS=ZS5 (73/106 of losers there)
- **Sharp: n=102  W=29/L=73  WR=28.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP6`
- Raw: n=160  W=54/L=106  WR=33.8%
- Sharpen: sharpest is ZS=ZS5 (73/106 of losers there)
- **Sharp: n=102  W=29/L=73  WR=28.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when zscore +2 to +3 deep overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(45/27) | H20e(29/48) |
| H60 | H60a(57/40) | H60e(43/60) |
| T1 | T1a(57/40) | T1c(43/60) |
| T4 | T4a(59/38) | T4c(41/62) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(57/40) | short(43/60) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
