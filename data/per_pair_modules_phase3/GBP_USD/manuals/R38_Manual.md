# GBP_USD — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,722**  (W=1,696 / L=1,026)  -  WR: **62.3%**

## Session distribution

- asia: n=1194  W=769/L=425  WR=64.4%
- ny_close: n=457  W=269/L=188  WR=58.9%
- london_open: n=275  W=186/L=89  WR=67.6%
- ny_mid: n=232  W=139/L=93  WR=59.9%
- ny_open: n=174  W=103/L=71  WR=59.2%
- london: n=169  W=111/L=58  WR=65.7%
- off_hours: n=115  W=59/L=56  WR=51.3%
- asia_late: n=106  W=60/L=46  WR=56.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=302  W=258/L=44  WR=85.4%
- Refine: exclude H20=H20b drops 14/44 losers (32%)
- **Final: n=250  W=220/L=30  WR=88.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when HTF20 slightly aligned

### W02.  `T4=T4c AND ZS=ZS3 AND direction_exec=long`
- Raw: n=289  W=248/L=41  WR=85.8%
- Refine: exclude session_bucket=ny_close drops 14/41 losers (34%)
- **Final: n=258  W=231/L=27  WR=89.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W03.  `T4=T4c AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=285  W=244/L=41  WR=85.6%
- Refine: exclude session_bucket=ny_close drops 14/41 losers (34%)
- **Final: n=254  W=227/L=27  WR=89.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W04.  `T1=T1a AND T4=T4c AND ZS=ZS3 AND direction_exec=long`
- Raw: n=254  W=218/L=36  WR=85.8%
- Refine: exclude BBP=BBP3 drops 26/36 losers (72%)
- **Final: n=142  W=132/L=10  WR=93.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when middle of band

### W05.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=240  W=205/L=35  WR=85.4%
- Refine: exclude ZS=ZS4 drops 31/35 losers (89%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when zscore +1 to +2 overbought

### W06.  `H20=H20a AND H60=H60a AND BBP=BBP4`
- Raw: n=221  W=192/L=29  WR=86.9%
- Refine: no further refinement
- **Final: n=221  W=192/L=29  WR=86.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third

### W07.  `H60=H60a AND T1=T1a AND T4=T4c AND BBP=BBP4`
- Raw: n=215  W=186/L=29  WR=86.5%
- Refine: exclude ZS=ZS4 drops 28/29 losers (97%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when zscore +1 to +2 overbought

### W08.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=206  W=182/L=24  WR=88.3%
- Refine: exclude session_bucket=london drops 9/24 losers (38%)
- **Final: n=163  W=148/L=15  WR=90.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=london

### W09.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=190  W=165/L=25  WR=86.8%
- Refine: exclude session_bucket=london drops 8/25 losers (32%)
- **Final: n=166  W=149/L=17  WR=89.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third  •  AVOID when session=london

### W10.  `H60=H60a AND T4=T4c AND ZS=ZS3`
- Raw: n=187  W=165/L=22  WR=88.2%
- Refine: exclude BBP=BBP3 drops 16/22 losers (73%)
- **Final: n=107  W=101/L=6  WR=94.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when middle of band

### W11.  `H60=H60a AND T4=T4c AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=186  W=165/L=21  WR=88.7%
- Refine: exclude BBP=BBP3 drops 15/21 losers (71%)
- **Final: n=107  W=101/L=6  WR=94.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when middle of band

### W12.  `H20=H20a AND H60=H60a AND ZS=ZS4`
- Raw: n=185  W=159/L=26  WR=85.9%
- Refine: no further refinement
- **Final: n=185  W=159/L=26  WR=85.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought

### W13.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=185  W=159/L=26  WR=85.9%
- Refine: no further refinement
- **Final: n=185  W=159/L=26  WR=85.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought

### W14.  `H20=H20a AND H60=H60a AND T4=T4c AND BBP=BBP4`
- Raw: n=183  W=160/L=23  WR=87.4%
- Refine: exclude ZS=ZS4 drops 23/23 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when zscore +1 to +2 overbought

### W15.  `H60=H60a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=180  W=155/L=25  WR=86.1%
- Refine: exclude T4=T4a drops 8/25 losers (32%)
- **Final: n=167  W=150/L=17  WR=89.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore -1 to +1 neutral  •  AVOID when 4h trend WITH trade

### W16.  `H60=H60a AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=177  W=153/L=24  WR=86.4%
- Refine: exclude T4=T4a drops 7/24 losers (29%)
- **Final: n=167  W=150/L=17  WR=89.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when 4h trend WITH trade

### W17.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=170  W=149/L=21  WR=87.6%
- Refine: exclude session_bucket=ny_mid drops 7/21 losers (33%)
- **Final: n=138  W=124/L=14  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W18.  `H60=H60a AND T4=T4c AND ZS=ZS3 AND direction_exec=long`
- Raw: n=167  W=150/L=17  WR=89.8%
- Refine: exclude BBP=BBP3 drops 13/17 losers (76%)
- **Final: n=96  W=92/L=4  WR=95.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when middle of band

### W19.  `H60=H60a AND T1=T1a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=162  W=141/L=21  WR=87.0%
- Refine: exclude BBP=BBP3 drops 15/21 losers (71%)
- **Final: n=95  W=89/L=6  WR=93.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when middle of band

### W20.  `H60=H60a AND T1=T1a AND T4=T4c AND ZS=ZS3`
- Raw: n=156  W=141/L=15  WR=90.4%
- Refine: exclude BBP=BBP3 drops 14/15 losers (93%)
- **Final: n=92  W=91/L=1  WR=98.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when middle of band

### W21.  `H20=H20a AND H60=H60a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=156  W=134/L=22  WR=85.9%
- Refine: no further refinement
- **Final: n=156  W=134/L=22  WR=85.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought

### W22.  `H20=H20a AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=153  W=131/L=22  WR=85.6%
- Refine: exclude H60=H60d drops 8/22 losers (36%)
- **Final: n=125  W=111/L=14  WR=88.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF60 mildly against

### W23.  `H20=H20a AND H60=H60a AND T1=T1a AND BBP=BBP4`
- Raw: n=141  W=123/L=18  WR=87.2%
- Refine: exclude session_bucket=london drops 4/18 losers (22%)
- **Final: n=137  W=123/L=14  WR=89.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when session=london

### W24.  `BBP=BBP4 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=127  W=113/L=14  WR=89.0%
- Refine: exclude H60=H60e drops 6/14 losers (43%)
- **Final: n=108  W=100/L=8  WR=92.6%**
- **Dir: LONG**  •  upper third; zscore -1 to +1 neutral  •  AVOID when HTF60 strongly against

### W25.  `T4=T4c AND BBP=BBP4 AND ZS=ZS3`
- Raw: n=124  W=110/L=14  WR=88.7%
- Refine: exclude T1=T1c drops 7/14 losers (50%)
- **Final: n=99  W=92/L=7  WR=92.9%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; zscore -1 to +1 neutral  •  AVOID when 1h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=261  W=102/L=159  WR=39.1%
- Sharpen: sharpest is T4=T4a (144/159 of losers there)
- **Sharp: n=201  W=57/L=144  WR=28.4%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend WITH trade

### L02.  `T4=T4a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=253  W=82/L=171  WR=32.4%
- Sharpen: sharpest is H60=H60e (103/171 of losers there)
- **Sharp: n=139  W=36/L=103  WR=25.9%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF60 strongly against

### L03.  `H60=H60e AND BBP=BBP4 AND direction_exec=short`
- Raw: n=242  W=96/L=146  WR=39.7%
- Sharpen: sharpest is ZS=ZS3 (39/146 of losers there)
- **Sharp: n=48  W=9/L=39  WR=18.8%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third  •  ONLY when zscore -1 to +1 neutral

### L04.  `H60=H60e AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=236  W=93/L=143  WR=39.4%
- Sharpen: sharpest is ZS=ZS3 (39/143 of losers there)
- **Sharp: n=48  W=9/L=39  WR=18.8%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L05.  `H60=H60e AND T4=T4a AND BBP=BBP4`
- Raw: n=235  W=94/L=141  WR=40.0%
- Sharpen: sharpest is ZS=ZS3 (41/141 of losers there)
- **Sharp: n=52  W=11/L=41  WR=21.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third  •  ONLY when zscore -1 to +1 neutral

### L06.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=229  W=88/L=141  WR=38.4%
- Sharpen: sharpest is ZS=ZS3 (41/141 of losers there)
- **Sharp: n=52  W=11/L=41  WR=21.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L07.  `T1=T1c AND ZS=ZS3 AND direction_exec=short`
- Raw: n=222  W=87/L=135  WR=39.2%
- Sharpen: sharpest is H60=H60e (89/135 of losers there)
- **Sharp: n=118  W=29/L=89  WR=24.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when HTF60 strongly against

### L08.  `T4=T4a AND ZS=ZS3 AND direction_exec=short`
- Raw: n=203  W=57/L=146  WR=28.1%
- Sharpen: sharpest is BBP=BBP4 (50/146 of losers there)
- **Sharp: n=57  W=7/L=50  WR=12.3%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when upper third

### L09.  `T4=T4a AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=201  W=57/L=144  WR=28.4%
- Sharpen: sharpest is BBP=BBP4 (48/144 of losers there)
- **Sharp: n=55  W=7/L=48  WR=12.7%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when upper third

### L10.  `H20=H20e AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=201  W=80/L=121  WR=39.8%
- Sharpen: sharpest is H60=H60e (87/121 of losers there)
- **Sharp: n=128  W=41/L=87  WR=32.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L11.  `T1=T1c AND T4=T4a AND ZS=ZS3`
- Raw: n=196  W=62/L=134  WR=31.6%
- Sharpen: sharpest is H60=H60e (88/134 of losers there)
- **Sharp: n=114  W=26/L=88  WR=22.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when HTF60 strongly against

### L12.  `H20=H20e AND T4=T4a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=196  W=77/L=119  WR=39.3%
- Sharpen: sharpest is H60=H60e (83/119 of losers there)
- **Sharp: n=123  W=40/L=83  WR=32.5%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; upper third  •  ONLY when HTF60 strongly against

### L13.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=191  W=61/L=130  WR=31.9%
- Sharpen: sharpest is H60=H60e (88/130 of losers there)
- **Sharp: n=114  W=26/L=88  WR=22.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF60 strongly against

### L14.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=190  W=68/L=122  WR=35.8%
- Sharpen: sharpest is ZS=ZS3 (38/122 of losers there)
- **Sharp: n=41  W=3/L=38  WR=7.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; upper third  •  ONLY when zscore -1 to +1 neutral

### L15.  `H60=H60e AND T1=T1c AND T4=T4a AND BBP=BBP4`
- Raw: n=177  W=69/L=108  WR=39.0%
- Sharpen: sharpest is ZS=ZS3 (36/108 of losers there)
- **Sharp: n=41  W=5/L=36  WR=12.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; upper third  •  ONLY when zscore -1 to +1 neutral

### L16.  `T1=T1c AND T4=T4a AND ZS=ZS3 AND direction_exec=short`
- Raw: n=176  W=52/L=124  WR=29.5%
- Sharpen: sharpest is H60=H60e (84/124 of losers there)
- **Sharp: n=107  W=23/L=84  WR=21.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when HTF60 strongly against

### L17.  `H20=H20e AND H60=H60e AND BBP=BBP4`
- Raw: n=173  W=64/L=109  WR=37.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=173  W=64/L=109  WR=37.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third

### L18.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=161  W=55/L=106  WR=34.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=161  W=55/L=106  WR=34.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; RSI 50-60 upper neutral

### L19.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND direction_exec=short`
- Raw: n=159  W=57/L=102  WR=35.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=159  W=57/L=102  WR=35.8%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; upper third

### L20.  `H20=H20e AND H60=H60e AND ZS=ZS4`
- Raw: n=148  W=57/L=91  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=148  W=57/L=91  WR=38.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +1 to +2 overbought

### L21.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=148  W=57/L=91  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=148  W=57/L=91  WR=38.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; zscore +1 to +2 overbought

### L22.  `H60=H60e AND T1=T1c AND ZS=ZS3`
- Raw: n=142  W=49/L=93  WR=34.5%
- Sharpen: sharpest is T4=T4a (88/93 of losers there)
- **Sharp: n=114  W=26/L=88  WR=22.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when 4h trend WITH trade

### L23.  `T4=T4a AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=142  W=53/L=89  WR=37.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=142  W=53/L=89  WR=37.3%**
- **Dir: ?**  •  4h trend WITH trade; middle of band; zscore -1 to +1 neutral

### L24.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=142  W=55/L=87  WR=38.7%
- Sharpen: sharpest is H20=H20b (38/87 of losers there)
- **Sharp: n=46  W=8/L=38  WR=17.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF20 slightly aligned

### L25.  `H60=H60e AND T4=T4a AND ZS=ZS3`
- Raw: n=141  W=38/L=103  WR=27.0%
- Sharpen: sharpest is direction_exec=short (93/103 of losers there)
- **Sharp: n=118  W=25/L=93  WR=21.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when short

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(38/27), H60b(18/13) | H60e(28/41) |
| T1 | T1a(54/45) | T1c(46/55) |
| T4 | T4c(61/41) | T4a(39/59) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(58/39) | short(42/61) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
