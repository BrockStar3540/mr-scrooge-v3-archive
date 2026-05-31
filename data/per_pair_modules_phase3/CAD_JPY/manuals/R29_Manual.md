# CAD_JPY — R29 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,480**  (W=2,186 / L=1,294)  -  WR: **62.8%**

## Session distribution

- asia: n=1237  W=770/L=467  WR=62.2%
- ny_close: n=687  W=429/L=258  WR=62.4%
- london_open: n=439  W=286/L=153  WR=65.1%
- ny_open: n=315  W=192/L=123  WR=61.0%
- london: n=242  W=159/L=83  WR=65.7%
- ny_mid: n=208  W=139/L=69  WR=66.8%
- asia_late: n=182  W=109/L=73  WR=59.9%
- off_hours: n=170  W=102/L=68  WR=60.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60a AND T4=T4a`
- Raw: n=206  W=179/L=27  WR=86.9%
- Refine: exclude session_bucket=london_open drops 7/27 losers (26%)
- **Final: n=199  W=179/L=20  WR=89.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=london_open

### W02.  `H20=H20e AND H60=H60a AND direction_exec=long`
- Raw: n=206  W=179/L=27  WR=86.9%
- Refine: exclude session_bucket=london_open drops 7/27 losers (26%)
- **Final: n=199  W=179/L=20  WR=89.9%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade  •  AVOID when session=london_open

### W03.  `H20=H20e AND T4=T4a AND direction_exec=long`
- Raw: n=206  W=179/L=27  WR=86.9%
- Refine: exclude session_bucket=london_open drops 7/27 losers (26%)
- **Final: n=199  W=179/L=20  WR=89.9%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade  •  AVOID when session=london_open

### W04.  `H20=H20e AND H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=206  W=179/L=27  WR=86.9%
- Refine: exclude session_bucket=london_open drops 7/27 losers (26%)
- **Final: n=199  W=179/L=20  WR=89.9%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=london_open

### W05.  `H20=H20e AND H60=H60a AND T1=T1a`
- Raw: n=203  W=176/L=27  WR=86.7%
- Refine: exclude session_bucket=london_open drops 7/27 losers (26%)
- **Final: n=196  W=176/L=20  WR=89.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=london_open

### W06.  `H20=H20e AND T1=T1a AND T4=T4a`
- Raw: n=203  W=176/L=27  WR=86.7%
- Refine: exclude session_bucket=london_open drops 7/27 losers (26%)
- **Final: n=196  W=176/L=20  WR=89.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=london_open

### W07.  `H20=H20e AND T1=T1a AND direction_exec=long`
- Raw: n=203  W=176/L=27  WR=86.7%
- Refine: exclude session_bucket=london_open drops 7/27 losers (26%)
- **Final: n=196  W=176/L=20  WR=89.8%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade  •  AVOID when session=london_open

### W08.  `H20=H20e AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=203  W=176/L=27  WR=86.7%
- Refine: exclude session_bucket=london_open drops 7/27 losers (26%)
- **Final: n=196  W=176/L=20  WR=89.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=london_open

### W09.  `H20=H20e AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=203  W=176/L=27  WR=86.7%
- Refine: exclude session_bucket=london_open drops 7/27 losers (26%)
- **Final: n=196  W=176/L=20  WR=89.8%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=london_open

### W10.  `H20=H20e AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=203  W=176/L=27  WR=86.7%
- Refine: exclude session_bucket=london_open drops 7/27 losers (26%)
- **Final: n=196  W=176/L=20  WR=89.8%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=london_open

### W11.  `H20=H20e AND T4=T4a AND RSI=RSI4`
- Raw: n=164  W=149/L=15  WR=90.9%
- Refine: exclude BBP=BBP4 drops 10/15 losers (67%)
- **Final: n=91  W=86/L=5  WR=94.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when upper third

### W12.  `H20=H20e AND H60=H60a AND RSI=RSI4`
- Raw: n=147  W=133/L=14  WR=90.5%
- Refine: exclude BBP=BBP4 drops 10/14 losers (71%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when upper third

### W13.  `H20=H20e AND RSI=RSI4 AND direction_exec=long`
- Raw: n=147  W=133/L=14  WR=90.5%
- Refine: exclude BBP=BBP4 drops 10/14 losers (71%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral  •  AVOID when upper third

### W14.  `H20=H20e AND H60=H60a AND T1=T1a AND RSI=RSI4`
- Raw: n=147  W=133/L=14  WR=90.5%
- Refine: exclude BBP=BBP4 drops 10/14 losers (71%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when upper third

### W15.  `H20=H20e AND H60=H60a AND T4=T4a AND RSI=RSI4`
- Raw: n=147  W=133/L=14  WR=90.5%
- Refine: exclude BBP=BBP4 drops 10/14 losers (71%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when upper third

### W16.  `H20=H20e AND H60=H60a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=147  W=133/L=14  WR=90.5%
- Refine: exclude BBP=BBP4 drops 10/14 losers (71%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when upper third

### W17.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=147  W=133/L=14  WR=90.5%
- Refine: exclude BBP=BBP4 drops 10/14 losers (71%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when upper third

### W18.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=147  W=133/L=14  WR=90.5%
- Refine: exclude BBP=BBP4 drops 10/14 losers (71%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when upper third

### W19.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=147  W=133/L=14  WR=90.5%
- Refine: exclude BBP=BBP4 drops 10/14 losers (71%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when upper third

### W20.  `H60=H60a AND T4=T4a AND session_bucket=london`
- Raw: n=140  W=120/L=20  WR=85.7%
- Refine: exclude BBP=BBP2 drops 11/20 losers (55%)
- **Final: n=103  W=94/L=9  WR=91.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london  •  AVOID when lower third

### W21.  `H60=H60a AND direction_exec=long AND session_bucket=london`
- Raw: n=140  W=120/L=20  WR=85.7%
- Refine: exclude BBP=BBP2 drops 11/20 losers (55%)
- **Final: n=103  W=94/L=9  WR=91.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=london  •  AVOID when lower third

### W22.  `T4=T4a AND direction_exec=long AND session_bucket=london`
- Raw: n=140  W=120/L=20  WR=85.7%
- Refine: exclude BBP=BBP2 drops 11/20 losers (55%)
- **Final: n=103  W=94/L=9  WR=91.3%**
- **Dir: LONG**  •  4h trend WITH trade; session=london  •  AVOID when lower third

### W23.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=london`
- Raw: n=140  W=120/L=20  WR=85.7%
- Refine: exclude BBP=BBP2 drops 11/20 losers (55%)
- **Final: n=103  W=94/L=9  WR=91.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london  •  AVOID when lower third

### W24.  `H60=H60a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=125  W=114/L=11  WR=91.2%
- Refine: exclude BBP=BBP5 drops 5/11 losers (45%)
- **Final: n=99  W=93/L=6  WR=93.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_close  •  AVOID when just touched upper band

### W25.  `T1=T1a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=125  W=114/L=11  WR=91.2%
- Refine: exclude BBP=BBP5 drops 5/11 losers (45%)
- **Final: n=99  W=93/L=6  WR=93.9%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_close  •  AVOID when just touched upper band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND RSI=RSI5`
- Raw: n=291  W=116/L=175  WR=39.9%
- Sharpen: sharpest is session_bucket=ny_close (69/175 of losers there)
- **Sharp: n=77  W=8/L=69  WR=10.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when session=ny_close

### L02.  `H20=H20e AND T4=T4c AND RSI=RSI5`
- Raw: n=291  W=116/L=175  WR=39.9%
- Sharpen: sharpest is session_bucket=ny_close (69/175 of losers there)
- **Sharp: n=77  W=8/L=69  WR=10.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_close

### L03.  `H20=H20e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=291  W=116/L=175  WR=39.9%
- Sharpen: sharpest is session_bucket=ny_close (69/175 of losers there)
- **Sharp: n=77  W=8/L=69  WR=10.4%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong  •  ONLY when session=ny_close

### L04.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=291  W=116/L=175  WR=39.9%
- Sharpen: sharpest is session_bucket=ny_close (69/175 of losers there)
- **Sharp: n=77  W=8/L=69  WR=10.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_close

### L05.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=291  W=116/L=175  WR=39.9%
- Sharpen: sharpest is session_bucket=ny_close (69/175 of losers there)
- **Sharp: n=77  W=8/L=69  WR=10.4%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when session=ny_close

### L06.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=291  W=116/L=175  WR=39.9%
- Sharpen: sharpest is session_bucket=ny_close (69/175 of losers there)
- **Sharp: n=77  W=8/L=69  WR=10.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_close

### L07.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=196  W=75/L=121  WR=38.3%
- Sharpen: sharpest is RSI=RSI5 (26/121 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 60-70 strong

### L08.  `H60=H60e AND T4=T4c AND ZS=ZS2`
- Raw: n=187  W=74/L=113  WR=39.6%
- Sharpen: sharpest is RSI=RSI5 (26/113 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 60-70 strong

### L09.  `T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=187  W=74/L=113  WR=39.6%
- Sharpen: sharpest is RSI=RSI5 (26/113 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 60-70 strong

### L10.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=187  W=74/L=113  WR=39.6%
- Sharpen: sharpest is RSI=RSI5 (26/113 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 60-70 strong

### L11.  `H60=H60e AND T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=187  W=74/L=113  WR=39.6%
- Sharpen: sharpest is RSI=RSI5 (26/113 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 60-70 strong

### L12.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=187  W=74/L=113  WR=39.6%
- Sharpen: sharpest is RSI=RSI5 (26/113 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 60-70 strong

### L13.  `H20=H20a AND H60=H60e AND T4=T4c`
- Raw: n=168  W=60/L=108  WR=35.7%
- Sharpen: sharpest is session_bucket=ny_open (25/108 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L14.  `H20=H20a AND H60=H60e AND direction_exec=short`
- Raw: n=168  W=60/L=108  WR=35.7%
- Sharpen: sharpest is session_bucket=ny_open (25/108 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  ONLY when session=ny_open

### L15.  `H20=H20a AND T4=T4c AND direction_exec=short`
- Raw: n=168  W=60/L=108  WR=35.7%
- Sharpen: sharpest is session_bucket=ny_open (25/108 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L16.  `H20=H20a AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=168  W=60/L=108  WR=35.7%
- Sharpen: sharpest is session_bucket=ny_open (25/108 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L17.  `H20=H20a AND H60=H60e AND T1=T1c`
- Raw: n=165  W=60/L=105  WR=36.4%
- Sharpen: sharpest is session_bucket=ny_open (25/105 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when session=ny_open

### L18.  `H20=H20a AND T1=T1c AND T4=T4c`
- Raw: n=165  W=60/L=105  WR=36.4%
- Sharpen: sharpest is session_bucket=ny_open (25/105 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L19.  `H20=H20a AND T1=T1c AND direction_exec=short`
- Raw: n=165  W=60/L=105  WR=36.4%
- Sharpen: sharpest is session_bucket=ny_open (25/105 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when session=ny_open

### L20.  `H20=H20a AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=165  W=60/L=105  WR=36.4%
- Sharpen: sharpest is session_bucket=ny_open (25/105 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L21.  `H20=H20a AND H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=165  W=60/L=105  WR=36.4%
- Sharpen: sharpest is session_bucket=ny_open (25/105 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when session=ny_open

### L22.  `H20=H20a AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=165  W=60/L=105  WR=36.4%
- Sharpen: sharpest is session_bucket=ny_open (25/105 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L23.  `H20=H20e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=148  W=53/L=95  WR=35.8%
- Sharpen: sharpest is RSI=RSI5 (69/95 of losers there)
- **Sharp: n=77  W=8/L=69  WR=10.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when RSI 60-70 strong

### L24.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=148  W=53/L=95  WR=35.8%
- Sharpen: sharpest is RSI=RSI5 (69/95 of losers there)
- **Sharp: n=77  W=8/L=69  WR=10.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when RSI 60-70 strong

### L25.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=148  W=53/L=95  WR=35.8%
- Sharpen: sharpest is RSI=RSI5 (69/95 of losers there)
- **Sharp: n=77  W=8/L=69  WR=10.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when RSI 60-70 strong

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(43/36) | H20e(34/40) |
| H60 | H60a(60/42) | H60e(40/58) |
| T1 | T1a(58/43) | T1c(42/56) |
| T4 | T4a(60/41) | T4c(40/59) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(60/42) | short(40/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
