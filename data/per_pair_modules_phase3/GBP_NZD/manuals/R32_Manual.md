# GBP_NZD — R32 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **5,486**  (W=3,134 / L=2,352)  -  WR: **57.1%**

## Session distribution

- asia: n=1793  W=1027/L=766  WR=57.3%
- ny_mid: n=946  W=529/L=417  WR=55.9%
- ny_close: n=752  W=434/L=318  WR=57.7%
- london_open: n=751  W=426/L=325  WR=56.7%
- ny_open: n=549  W=305/L=244  WR=55.6%
- london: n=402  W=247/L=155  WR=61.4%
- off_hours: n=181  W=96/L=85  WR=53.0%
- asia_late: n=112  W=70/L=42  WR=62.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=191  W=164/L=27  WR=85.9%
- Refine: exclude ZS=ZS3 drops 16/27 losers (59%)
- **Final: n=156  W=145/L=11  WR=92.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W02.  `BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=183  W=172/L=11  WR=94.0%
- Refine: exclude H60=H60b drops 4/11 losers (36%)
- **Final: n=177  W=170/L=7  WR=96.0%**
- **Dir: LONG**  •  lower third; RSI 50-60 upper neutral  •  AVOID when HTF60 slightly aligned

### W03.  `H60=H60e AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=182  W=155/L=27  WR=85.2%
- Refine: exclude ZS=ZS3 drops 16/27 losers (59%)
- **Final: n=155  W=144/L=11  WR=92.9%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W04.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=181  W=155/L=26  WR=85.6%
- Refine: exclude ZS=ZS3 drops 15/26 losers (58%)
- **Final: n=155  W=144/L=11  WR=92.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W05.  `RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=160  W=149/L=11  WR=93.1%
- Refine: exclude H60=H60b drops 4/11 losers (36%)
- **Final: n=154  W=147/L=7  WR=95.5%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when HTF60 slightly aligned

### W06.  `BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=160  W=149/L=11  WR=93.1%
- Refine: exclude H60=H60b drops 4/11 losers (36%)
- **Final: n=154  W=147/L=7  WR=95.5%**
- **Dir: LONG**  •  lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when HTF60 slightly aligned

### W07.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=149  W=133/L=16  WR=89.3%
- Refine: exclude H20=H20e drops 14/16 losers (88%)
- **Final: n=85  W=83/L=2  WR=97.6%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_close  •  AVOID when HTF20 strongly against

### W08.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=149  W=128/L=21  WR=85.9%
- Refine: exclude H20=H20d drops 19/21 losers (90%)
- **Final: n=116  W=114/L=2  WR=98.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 mildly against

### W09.  `T4=T4c AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=147  W=125/L=22  WR=85.0%
- Refine: exclude direction_exec=short drops 15/22 losers (68%)
- **Final: n=128  W=121/L=7  WR=94.5%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when short

### W10.  `T4=T4c AND BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=147  W=125/L=22  WR=85.0%
- Refine: exclude direction_exec=short drops 15/22 losers (68%)
- **Final: n=128  W=121/L=7  WR=94.5%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when short

### W11.  `H60=H60e AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=146  W=131/L=15  WR=89.7%
- Refine: exclude H20=H20e drops 15/15 losers (100%)
- **Final: n=81  W=81/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_close  •  AVOID when HTF20 strongly against

### W12.  `T1=T1c AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=145  W=131/L=14  WR=90.3%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=81  W=81/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when HTF20 strongly against

### W13.  `H60=H60e AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=140  W=125/L=15  WR=89.3%
- Refine: exclude direction_exec=short drops 8/15 losers (53%)
- **Final: n=132  W=125/L=7  WR=94.7%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 50-60 upper neutral  •  AVOID when short

### W14.  `T4=T4c AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=139  W=132/L=7  WR=95.0%
- Refine: exclude H60=H60b drops 4/7 losers (57%)
- **Final: n=133  W=130/L=3  WR=97.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; RSI 50-60 upper neutral  •  AVOID when HTF60 slightly aligned

### W15.  `H60=H60e AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=132  W=125/L=7  WR=94.7%
- Refine: exclude H20=H20d drops 4/7 losers (57%)
- **Final: n=125  W=122/L=3  WR=97.6%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; RSI 50-60 upper neutral  •  AVOID when HTF20 mildly against

### W16.  `T4=T4c AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=128  W=121/L=7  WR=94.5%
- Refine: exclude H60=H60b drops 4/7 losers (57%)
- **Final: n=122  W=119/L=3  WR=97.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when HTF60 slightly aligned

### W17.  `H20=H20e AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=120  W=113/L=7  WR=94.2%
- Refine: exclude H60=H60b drops 4/7 losers (57%)
- **Final: n=114  W=111/L=3  WR=97.4%**
- **Dir: LONG**  •  HTF20 strongly against; lower third; RSI 50-60 upper neutral  •  AVOID when HTF60 slightly aligned

### W18.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=120  W=109/L=11  WR=90.8%
- Refine: exclude ZS=ZS3 drops 10/11 losers (91%)
- **Final: n=98  W=97/L=1  WR=99.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W19.  `H60=H60e AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=119  W=107/L=12  WR=89.9%
- Refine: exclude T4=T4a drops 9/12 losers (75%)
- **Final: n=88  W=85/L=3  WR=96.6%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W20.  `H60=H60e AND BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=119  W=107/L=12  WR=89.9%
- Refine: exclude T4=T4a drops 9/12 losers (75%)
- **Final: n=88  W=85/L=3  WR=96.6%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W21.  `H60=H60e AND T1=T1c AND T4=T4a AND session_bucket=ny_close`
- Raw: n=115  W=103/L=12  WR=89.6%
- Refine: exclude ZS=ZS3 drops 11/12 losers (92%)
- **Final: n=98  W=97/L=1  WR=99.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W22.  `T1=T1a AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=114  W=109/L=5  WR=95.6%
- Refine: exclude H60=H60b drops 4/5 losers (80%)
- **Final: n=108  W=107/L=1  WR=99.1%**
- **Dir: LONG**  •  1h trend WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when HTF60 slightly aligned

### W23.  `H60=H60e AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=114  W=107/L=7  WR=93.9%
- Refine: exclude H20=H20d drops 4/7 losers (57%)
- **Final: n=107  W=104/L=3  WR=97.2%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 mildly against

### W24.  `H20=H20e AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=112  W=105/L=7  WR=93.8%
- Refine: exclude H60=H60b drops 4/7 losers (57%)
- **Final: n=106  W=103/L=3  WR=97.2%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when HTF60 slightly aligned

### W25.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=111  W=101/L=10  WR=91.0%
- Refine: exclude ZS=ZS3 drops 9/10 losers (90%)
- **Final: n=98  W=97/L=1  WR=99.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=878  W=350/L=528  WR=39.9%
- Sharpen: sharpest is T4=T4c (228/528 of losers there)
- **Sharp: n=316  W=88/L=228  WR=27.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L02.  `T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=472  W=160/L=312  WR=33.9%
- Sharpen: sharpest is H60=H60a (228/312 of losers there)
- **Sharp: n=316  W=88/L=228  WR=27.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L03.  `H60=H60a AND T1=T1a AND RSI=RSI4`
- Raw: n=471  W=179/L=292  WR=38.0%
- Sharpen: sharpest is session_bucket=ny_close (115/292 of losers there)
- **Sharp: n=148  W=33/L=115  WR=22.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L04.  `T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=464  W=161/L=303  WR=34.7%
- Sharpen: sharpest is session_bucket=ny_close (102/303 of losers there)
- **Sharp: n=121  W=19/L=102  WR=15.7%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L05.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=379  W=132/L=247  WR=34.8%
- Sharpen: sharpest is session_bucket=ny_close (102/247 of losers there)
- **Sharp: n=121  W=19/L=102  WR=15.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L06.  `H20=H20e AND H60=H60a AND RSI=RSI4`
- Raw: n=379  W=147/L=232  WR=38.8%
- Sharpen: sharpest is direction_exec=short (199/232 of losers there)
- **Sharp: n=303  W=104/L=199  WR=34.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  ONLY when short

### L07.  `H60=H60a AND T4=T4c AND RSI=RSI4`
- Raw: n=376  W=125/L=251  WR=33.2%
- Sharpen: sharpest is direction_exec=short (228/251 of losers there)
- **Sharp: n=316  W=88/L=228  WR=27.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when short

### L08.  `H20=H20e AND T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=330  W=131/L=199  WR=39.7%
- Sharpen: sharpest is ZS=ZS1 (65/199 of losers there)
- **Sharp: n=83  W=18/L=65  WR=21.7%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L09.  `H20=H20e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=324  W=120/L=204  WR=37.0%
- Sharpen: sharpest is session_bucket=ny_close (38/204 of losers there)
- **Sharp: n=38  W=0/L=38  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L10.  `H60=H60a AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=316  W=88/L=228  WR=27.8%
- Sharpen: sharpest is session_bucket=ny_close (62/228 of losers there)
- **Sharp: n=62  W=0/L=62  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L11.  `H20=H20e AND H60=H60a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=303  W=104/L=199  WR=34.3%
- Sharpen: sharpest is T4=T4c (126/199 of losers there)
- **Sharp: n=166  W=40/L=126  WR=24.1%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L12.  `H60=H60a AND T1=T1a AND BBP=BBP4`
- Raw: n=270  W=102/L=168  WR=37.8%
- Sharpen: sharpest is session_bucket=ny_close (57/168 of losers there)
- **Sharp: n=69  W=12/L=57  WR=17.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  ONLY when session=ny_close

### L13.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=266  W=82/L=184  WR=30.8%
- Sharpen: sharpest is session_bucket=ny_close (62/184 of losers there)
- **Sharp: n=62  W=0/L=62  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L14.  `H60=H60a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=264  W=101/L=163  WR=38.3%
- Sharpen: sharpest is T4=T4c (91/163 of losers there)
- **Sharp: n=114  W=23/L=91  WR=20.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L15.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=252  W=91/L=161  WR=36.1%
- Sharpen: sharpest is ZS=ZS1 (62/161 of losers there)
- **Sharp: n=75  W=13/L=62  WR=17.3%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L16.  `H60=H60a AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=241  W=90/L=151  WR=37.3%
- Sharpen: sharpest is session_bucket=ny_close (73/151 of losers there)
- **Sharp: n=87  W=14/L=73  WR=16.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L17.  `H60=H60a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=236  W=93/L=143  WR=39.4%
- Sharpen: sharpest is T4=T4c (85/143 of losers there)
- **Sharp: n=106  W=21/L=85  WR=19.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L18.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=230  W=89/L=141  WR=38.7%
- Sharpen: sharpest is BBP=BBP2 (24/141 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when lower third

### L19.  `H20=H20e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=228  W=75/L=153  WR=32.9%
- Sharpen: sharpest is H60=H60d (31/153 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF60 mildly against

### L20.  `H20=H20e AND H60=H60a AND T4=T4c AND RSI=RSI4`
- Raw: n=226  W=77/L=149  WR=34.1%
- Sharpen: sharpest is direction_exec=short (126/149 of losers there)
- **Sharp: n=166  W=40/L=126  WR=24.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when short

### L21.  `H20=H20e AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=226  W=90/L=136  WR=39.8%
- Sharpen: sharpest is T1=T1a (94/136 of losers there)
- **Sharp: n=130  W=36/L=94  WR=27.7%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L22.  `H60=H60a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=225  W=78/L=147  WR=34.7%
- Sharpen: sharpest is T1=T1a (104/147 of losers there)
- **Sharp: n=125  W=21/L=104  WR=16.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_close  •  ONLY when 1h trend WITH trade

### L23.  `T1=T1a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=214  W=85/L=129  WR=39.7%
- Sharpen: sharpest is H60=H60c (39/129 of losers there)
- **Sharp: n=50  W=11/L=39  WR=22.0%**
- **Dir: ?**  •  1h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 neutral

### L24.  `H60=H60a AND T1=T1a AND ZS=ZS4`
- Raw: n=208  W=75/L=133  WR=36.1%
- Sharpen: sharpest is session_bucket=ny_close (52/133 of losers there)
- **Sharp: n=55  W=3/L=52  WR=5.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when session=ny_close

### L25.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=208  W=75/L=133  WR=36.1%
- Sharpen: sharpest is session_bucket=ny_close (52/133 of losers there)
- **Sharp: n=55  W=3/L=52  WR=5.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when session=ny_close

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(47/38) | H60a(37/46) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
