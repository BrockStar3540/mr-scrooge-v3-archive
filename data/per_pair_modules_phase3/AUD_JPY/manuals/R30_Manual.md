# AUD_JPY — R30 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,981**  (W=1,892 / L=1,089)  -  WR: **63.5%**

## Session distribution

- asia: n=1244  W=791/L=453  WR=63.6%
- ny_close: n=496  W=303/L=193  WR=61.1%
- ny_open: n=355  W=222/L=133  WR=62.5%
- london_open: n=329  W=210/L=119  WR=63.8%
- london: n=208  W=138/L=70  WR=66.3%
- asia_late: n=150  W=97/L=53  WR=64.7%
- off_hours: n=110  W=72/L=38  WR=65.5%
- ny_mid: n=89  W=59/L=30  WR=66.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=214  W=183/L=31  WR=85.5%
- Refine: exclude ZS=ZS3 drops 15/31 losers (48%)
- **Final: n=173  W=157/L=16  WR=90.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore -1 to +1 neutral

### W02.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=214  W=183/L=31  WR=85.5%
- Refine: exclude ZS=ZS3 drops 15/31 losers (48%)
- **Final: n=173  W=157/L=16  WR=90.8%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore -1 to +1 neutral

### W03.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=208  W=179/L=29  WR=86.1%
- Refine: exclude ZS=ZS3 drops 14/29 losers (48%)
- **Final: n=168  W=153/L=15  WR=91.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore -1 to +1 neutral

### W04.  `H20=H20a AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=179  W=156/L=23  WR=87.2%
- Refine: exclude ZS=ZS3 drops 12/23 losers (52%)
- **Final: n=144  W=133/L=11  WR=92.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore -1 to +1 neutral

### W05.  `H20=H20a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=172  W=152/L=20  WR=88.4%
- Refine: exclude RSI=RSI4 drops 12/20 losers (60%)
- **Final: n=135  W=127/L=8  WR=94.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W06.  `H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=172  W=152/L=20  WR=88.4%
- Refine: exclude RSI=RSI4 drops 12/20 losers (60%)
- **Final: n=135  W=127/L=8  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W07.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=172  W=152/L=20  WR=88.4%
- Refine: exclude RSI=RSI4 drops 12/20 losers (60%)
- **Final: n=135  W=127/L=8  WR=94.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W08.  `T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=172  W=152/L=20  WR=88.4%
- Refine: exclude RSI=RSI4 drops 12/20 losers (60%)
- **Final: n=135  W=127/L=8  WR=94.1%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W09.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=172  W=152/L=20  WR=88.4%
- Refine: exclude RSI=RSI4 drops 12/20 losers (60%)
- **Final: n=135  W=127/L=8  WR=94.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W10.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=172  W=152/L=20  WR=88.4%
- Refine: exclude RSI=RSI4 drops 12/20 losers (60%)
- **Final: n=135  W=127/L=8  WR=94.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W11.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=172  W=152/L=20  WR=88.4%
- Refine: exclude RSI=RSI4 drops 12/20 losers (60%)
- **Final: n=135  W=127/L=8  WR=94.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W12.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=172  W=152/L=20  WR=88.4%
- Refine: exclude RSI=RSI4 drops 12/20 losers (60%)
- **Final: n=135  W=127/L=8  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W13.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=172  W=152/L=20  WR=88.4%
- Refine: exclude RSI=RSI4 drops 12/20 losers (60%)
- **Final: n=135  W=127/L=8  WR=94.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W14.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=172  W=152/L=20  WR=88.4%
- Refine: exclude RSI=RSI4 drops 12/20 losers (60%)
- **Final: n=135  W=127/L=8  WR=94.1%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W15.  `H20=H20a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=125  W=117/L=8  WR=93.6%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when upper third

### W16.  `H60=H60a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=125  W=117/L=8  WR=93.6%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when upper third

### W17.  `T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=125  W=117/L=8  WR=93.6%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when upper third

### W18.  `T4=T4a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=125  W=117/L=8  WR=93.6%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when upper third

### W19.  `RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=125  W=117/L=8  WR=93.6%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 60-70 strong; session=ny_open  •  AVOID when upper third

### W20.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=125  W=117/L=8  WR=93.6%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when upper third

### W21.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=125  W=117/L=8  WR=93.6%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when upper third

### W22.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=125  W=117/L=8  WR=93.6%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when upper third

### W23.  `H20=H20a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=125  W=117/L=8  WR=93.6%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when upper third

### W24.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=125  W=117/L=8  WR=93.6%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when upper third

### W25.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=125  W=117/L=8  WR=93.6%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when upper third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=228  W=88/L=140  WR=38.6%
- Sharpen: sharpest is H20=H20e (114/140 of losers there)
- **Sharp: n=172  W=58/L=114  WR=33.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 strongly against

### L02.  `RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=228  W=88/L=140  WR=38.6%
- Sharpen: sharpest is H20=H20e (114/140 of losers there)
- **Sharp: n=172  W=58/L=114  WR=33.7%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 strongly against

### L03.  `H60=H60e AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=228  W=88/L=140  WR=38.6%
- Sharpen: sharpest is H20=H20e (114/140 of losers there)
- **Sharp: n=172  W=58/L=114  WR=33.7%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 strongly against

### L04.  `T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=227  W=88/L=139  WR=38.8%
- Sharpen: sharpest is H20=H20e (114/139 of losers there)
- **Sharp: n=172  W=58/L=114  WR=33.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 strongly against

### L05.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=221  W=84/L=137  WR=38.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=221  W=84/L=137  WR=38.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia

### L06.  `T4=T4c AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=221  W=84/L=137  WR=38.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=221  W=84/L=137  WR=38.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia

### L07.  `H20=H20e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=179  W=62/L=117  WR=34.6%
- Sharpen: sharpest is ZS=ZS5 (35/117 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L08.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=172  W=58/L=114  WR=33.7%
- Sharpen: sharpest is ZS=ZS5 (35/114 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=172  W=58/L=114  WR=33.7%
- Sharpen: sharpest is ZS=ZS5 (35/114 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L10.  `H20=H20e AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=172  W=58/L=114  WR=33.7%
- Sharpen: sharpest is ZS=ZS5 (35/114 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L11.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=166  W=60/L=106  WR=36.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=166  W=60/L=106  WR=36.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia

### L12.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=166  W=60/L=106  WR=36.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=166  W=60/L=106  WR=36.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia

### L13.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=159  W=56/L=103  WR=35.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=159  W=56/L=103  WR=35.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia

### L14.  `H20=H20e AND H60=H60e AND session_bucket=ny_open`
- Raw: n=146  W=53/L=93  WR=36.3%
- Sharpen: sharpest is RSI=RSI5 (74/93 of losers there)
- **Sharp: n=85  W=11/L=74  WR=12.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when RSI 60-70 strong

### L15.  `H20=H20e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=146  W=53/L=93  WR=36.3%
- Sharpen: sharpest is RSI=RSI5 (74/93 of losers there)
- **Sharp: n=85  W=11/L=74  WR=12.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L16.  `H20=H20e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=146  W=53/L=93  WR=36.3%
- Sharpen: sharpest is RSI=RSI5 (74/93 of losers there)
- **Sharp: n=85  W=11/L=74  WR=12.9%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_open  •  ONLY when RSI 60-70 strong

### L17.  `H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=146  W=53/L=93  WR=36.3%
- Sharpen: sharpest is RSI=RSI5 (74/93 of losers there)
- **Sharp: n=85  W=11/L=74  WR=12.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L18.  `H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=146  W=53/L=93  WR=36.3%
- Sharpen: sharpest is RSI=RSI5 (74/93 of losers there)
- **Sharp: n=85  W=11/L=74  WR=12.9%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_open  •  ONLY when RSI 60-70 strong

### L19.  `T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=146  W=53/L=93  WR=36.3%
- Sharpen: sharpest is RSI=RSI5 (74/93 of losers there)
- **Sharp: n=85  W=11/L=74  WR=12.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L20.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=146  W=53/L=93  WR=36.3%
- Sharpen: sharpest is RSI=RSI5 (74/93 of losers there)
- **Sharp: n=85  W=11/L=74  WR=12.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L21.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=146  W=53/L=93  WR=36.3%
- Sharpen: sharpest is RSI=RSI5 (74/93 of losers there)
- **Sharp: n=85  W=11/L=74  WR=12.9%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when RSI 60-70 strong

### L22.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=146  W=53/L=93  WR=36.3%
- Sharpen: sharpest is RSI=RSI5 (74/93 of losers there)
- **Sharp: n=85  W=11/L=74  WR=12.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L23.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=146  W=53/L=93  WR=36.3%
- Sharpen: sharpest is RSI=RSI5 (74/93 of losers there)
- **Sharp: n=85  W=11/L=74  WR=12.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L24.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=134  W=43/L=91  WR=32.1%
- Sharpen: sharpest is ZS=ZS4 (33/91 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +1 to +2 overbought

### L25.  `H20=H20e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=117  W=25/L=92  WR=21.4%
- Sharpen: sharpest is RSI=RSI5 (74/92 of losers there)
- **Sharp: n=85  W=11/L=74  WR=12.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(50/42) | H20e(40/47) |
| H60 | H60a(54/48) | H60e(46/52) |
| T1 | T1a(55/46) | T1c(45/54) |
| T4 | T4a(55/46) | T4c(45/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/48) | short(46/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
