# CAD_JPY — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,897**  (W=1,859 / L=1,038)  -  WR: **64.2%**

## Session distribution

- asia: n=779  W=492/L=287  WR=63.2%
- ny_close: n=624  W=404/L=220  WR=64.7%
- ny_open: n=470  W=304/L=166  WR=64.7%
- london_open: n=417  W=276/L=141  WR=66.2%
- ny_mid: n=320  W=198/L=122  WR=61.9%
- london: n=128  W=82/L=46  WR=64.1%
- off_hours: n=114  W=75/L=39  WR=65.8%
- asia_late: n=45  W=28/L=17  WR=62.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=259  W=222/L=37  WR=85.7%
- Refine: exclude BBP=BBP5 drops 18/37 losers (49%)
- **Final: n=206  W=187/L=19  WR=90.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_open  •  AVOID when just touched upper band

### W02.  `H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=228  W=200/L=28  WR=87.7%
- Refine: exclude RSI=RSI6 drops 16/28 losers (57%)
- **Final: n=154  W=142/L=12  WR=92.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 70-80 overbought

### W03.  `T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=228  W=200/L=28  WR=87.7%
- Refine: exclude RSI=RSI6 drops 16/28 losers (57%)
- **Final: n=154  W=142/L=12  WR=92.2%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_open  •  AVOID when RSI 70-80 overbought

### W04.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=228  W=200/L=28  WR=87.7%
- Refine: exclude RSI=RSI6 drops 16/28 losers (57%)
- **Final: n=154  W=142/L=12  WR=92.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 70-80 overbought

### W05.  `H20=H20a AND H60=H60a AND session_bucket=ny_open`
- Raw: n=224  W=194/L=30  WR=86.6%
- Refine: exclude RSI=RSI6 drops 16/30 losers (53%)
- **Final: n=150  W=136/L=14  WR=90.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  AVOID when RSI 70-80 overbought

### W06.  `H20=H20a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=224  W=194/L=30  WR=86.6%
- Refine: exclude RSI=RSI6 drops 16/30 losers (53%)
- **Final: n=150  W=136/L=14  WR=90.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_open  •  AVOID when RSI 70-80 overbought

### W07.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=224  W=194/L=30  WR=86.6%
- Refine: exclude RSI=RSI6 drops 16/30 losers (53%)
- **Final: n=150  W=136/L=14  WR=90.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  AVOID when RSI 70-80 overbought

### W08.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=196  W=168/L=28  WR=85.7%
- Refine: exclude RSI=RSI6 drops 16/28 losers (57%)
- **Final: n=122  W=110/L=12  WR=90.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 70-80 overbought

### W09.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=196  W=168/L=28  WR=85.7%
- Refine: exclude RSI=RSI6 drops 16/28 losers (57%)
- **Final: n=122  W=110/L=12  WR=90.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 70-80 overbought

### W10.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=196  W=168/L=28  WR=85.7%
- Refine: exclude RSI=RSI6 drops 16/28 losers (57%)
- **Final: n=122  W=110/L=12  WR=90.2%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 70-80 overbought

### W11.  `H20=H20a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=193  W=172/L=21  WR=89.1%
- Refine: exclude RSI=RSI6 drops 16/21 losers (76%)
- **Final: n=119  W=114/L=5  WR=95.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 70-80 overbought

### W12.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=193  W=172/L=21  WR=89.1%
- Refine: exclude RSI=RSI6 drops 16/21 losers (76%)
- **Final: n=119  W=114/L=5  WR=95.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 70-80 overbought

### W13.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=193  W=172/L=21  WR=89.1%
- Refine: exclude RSI=RSI6 drops 16/21 losers (76%)
- **Final: n=119  W=114/L=5  WR=95.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 70-80 overbought

### W14.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=161  W=140/L=21  WR=87.0%
- Refine: exclude RSI=RSI6 drops 16/21 losers (76%)
- **Final: n=87  W=82/L=5  WR=94.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 70-80 overbought

### W15.  `H60=H60a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=154  W=142/L=12  WR=92.2%
- Refine: exclude BBP=BBP5 drops 7/12 losers (58%)
- **Final: n=134  W=129/L=5  WR=96.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W16.  `T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=154  W=142/L=12  WR=92.2%
- Refine: exclude BBP=BBP5 drops 7/12 losers (58%)
- **Final: n=134  W=129/L=5  WR=96.3%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W17.  `RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=154  W=142/L=12  WR=92.2%
- Refine: exclude BBP=BBP5 drops 7/12 losers (58%)
- **Final: n=134  W=129/L=5  WR=96.3%**
- **Dir: LONG**  •  RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W18.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=154  W=142/L=12  WR=92.2%
- Refine: exclude BBP=BBP5 drops 7/12 losers (58%)
- **Final: n=134  W=129/L=5  WR=96.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W19.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=154  W=142/L=12  WR=92.2%
- Refine: exclude BBP=BBP5 drops 7/12 losers (58%)
- **Final: n=134  W=129/L=5  WR=96.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W20.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=154  W=142/L=12  WR=92.2%
- Refine: exclude BBP=BBP5 drops 7/12 losers (58%)
- **Final: n=134  W=129/L=5  WR=96.3%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W21.  `T1=T1a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=126  W=114/L=12  WR=90.5%
- Refine: exclude RSI=RSI6 drops 6/12 losers (50%)
- **Final: n=96  W=90/L=6  WR=93.8%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=ny_open  •  AVOID when RSI 70-80 overbought

### W22.  `T1=T1a AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=122  W=110/L=12  WR=90.2%
- Refine: exclude RSI=RSI6 drops 6/12 losers (50%)
- **Final: n=92  W=86/L=6  WR=93.5%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when RSI 70-80 overbought

### W23.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=122  W=110/L=12  WR=90.2%
- Refine: exclude BBP=BBP5 drops 7/12 losers (58%)
- **Final: n=104  W=99/L=5  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W24.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=122  W=110/L=12  WR=90.2%
- Refine: exclude BBP=BBP5 drops 7/12 losers (58%)
- **Final: n=104  W=99/L=5  WR=95.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W25.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=122  W=110/L=12  WR=90.2%
- Refine: exclude RSI=RSI6 drops 6/12 losers (50%)
- **Final: n=92  W=86/L=6  WR=93.5%**
- **Dir: ?**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought; session=ny_open  •  AVOID when RSI 70-80 overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=211  W=82/L=129  WR=38.9%
- Sharpen: sharpest is RSI=RSI5 (85/129 of losers there)
- **Sharp: n=105  W=20/L=85  WR=19.0%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_open  •  ONLY when RSI 60-70 strong

### L02.  `H20=H20e AND H60=H60e AND session_bucket=ny_open`
- Raw: n=183  W=73/L=110  WR=39.9%
- Sharpen: sharpest is RSI=RSI5 (66/110 of losers there)
- **Sharp: n=77  W=11/L=66  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when RSI 60-70 strong

### L03.  `H20=H20e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=183  W=73/L=110  WR=39.9%
- Sharpen: sharpest is RSI=RSI5 (66/110 of losers there)
- **Sharp: n=77  W=11/L=66  WR=14.3%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_open  •  ONLY when RSI 60-70 strong

### L04.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=183  W=73/L=110  WR=39.9%
- Sharpen: sharpest is RSI=RSI5 (66/110 of losers there)
- **Sharp: n=77  W=11/L=66  WR=14.3%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when RSI 60-70 strong

### L05.  `H60=H60e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=182  W=66/L=116  WR=36.3%
- Sharpen: sharpest is RSI=RSI5 (85/116 of losers there)
- **Sharp: n=105  W=20/L=85  WR=19.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L06.  `T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=182  W=66/L=116  WR=36.3%
- Sharpen: sharpest is RSI=RSI5 (85/116 of losers there)
- **Sharp: n=105  W=20/L=85  WR=19.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L07.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=182  W=66/L=116  WR=36.3%
- Sharpen: sharpest is RSI=RSI5 (85/116 of losers there)
- **Sharp: n=105  W=20/L=85  WR=19.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L08.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=167  W=66/L=101  WR=39.5%
- Sharpen: sharpest is RSI=RSI5 (70/101 of losers there)
- **Sharp: n=90  W=20/L=70  WR=22.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L09.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=167  W=66/L=101  WR=39.5%
- Sharpen: sharpest is RSI=RSI5 (70/101 of losers there)
- **Sharp: n=90  W=20/L=70  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L10.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=167  W=66/L=101  WR=39.5%
- Sharpen: sharpest is RSI=RSI5 (70/101 of losers there)
- **Sharp: n=90  W=20/L=70  WR=22.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L11.  `H20=H20e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=154  W=57/L=97  WR=37.0%
- Sharpen: sharpest is RSI=RSI5 (66/97 of losers there)
- **Sharp: n=77  W=11/L=66  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L12.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=154  W=57/L=97  WR=37.0%
- Sharpen: sharpest is RSI=RSI5 (66/97 of losers there)
- **Sharp: n=77  W=11/L=66  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L13.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=154  W=57/L=97  WR=37.0%
- Sharpen: sharpest is RSI=RSI5 (66/97 of losers there)
- **Sharp: n=77  W=11/L=66  WR=14.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L14.  `H60=H60e AND BBP=BBP6 AND direction_exec=short`
- Raw: n=114  W=40/L=74  WR=35.1%
- Sharpen: sharpest is session_bucket=ny_open (39/74 of losers there)
- **Sharp: n=43  W=4/L=39  WR=9.3%**
- **Dir: SHORT**  •  HTF60 strongly against; deep above upper band  •  ONLY when session=ny_open

### L15.  `H20=H20e AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=112  W=39/L=73  WR=34.8%
- Sharpen: sharpest is H60=H60e (66/73 of losers there)
- **Sharp: n=77  W=11/L=66  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_open  •  ONLY when HTF60 strongly against

### L16.  `H60=H60e AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=105  W=20/L=85  WR=19.0%
- Sharpen: sharpest is BBP=BBP6 (24/85 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_open  •  ONLY when deep above upper band

### L17.  `T1=T1c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=105  W=20/L=85  WR=19.0%
- Sharpen: sharpest is BBP=BBP6 (24/85 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when deep above upper band

### L18.  `RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=105  W=20/L=85  WR=19.0%
- Sharpen: sharpest is BBP=BBP6 (24/85 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=ny_open  •  ONLY when deep above upper band

### L19.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=105  W=20/L=85  WR=19.0%
- Sharpen: sharpest is BBP=BBP6 (24/85 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when deep above upper band

### L20.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=105  W=20/L=85  WR=19.0%
- Sharpen: sharpest is BBP=BBP6 (24/85 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_open  •  ONLY when deep above upper band

### L21.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=105  W=20/L=85  WR=19.0%
- Sharpen: sharpest is BBP=BBP6 (24/85 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when deep above upper band

### L22.  `H60=H60e AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=105  W=36/L=69  WR=34.3%
- Sharpen: sharpest is session_bucket=ny_open (34/69 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L23.  `BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=105  W=36/L=69  WR=34.3%
- Sharpen: sharpest is session_bucket=ny_open (34/69 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: SHORT**  •  deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L24.  `H60=H60e AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=105  W=36/L=69  WR=34.3%
- Sharpen: sharpest is session_bucket=ny_open (34/69 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: SHORT**  •  HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L25.  `H60=H60e AND T1=T1c AND BBP=BBP6`
- Raw: n=104  W=40/L=64  WR=38.5%
- Sharpen: sharpest is session_bucket=ny_open (29/64 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band  •  ONLY when session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(51/44) | H20e(43/50) |
| H60 | H60a(53/45) | H60e(47/55) |
| T1 | T1a(53/46) | T1c(47/54) |
| T4 | T4a(54/48) | T4c(46/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/45) | short(47/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
