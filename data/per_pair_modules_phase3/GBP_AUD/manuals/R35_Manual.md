# GBP_AUD — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **4,368**  (W=2,575 / L=1,793)  -  WR: **59.0%**

## Session distribution

- asia: n=1604  W=928/L=676  WR=57.9%
- london_open: n=841  W=493/L=348  WR=58.6%
- ny_mid: n=684  W=408/L=276  WR=59.6%
- london: n=404  W=250/L=154  WR=61.9%
- ny_open: n=288  W=175/L=113  WR=60.8%
- ny_close: n=264  W=154/L=110  WR=58.3%
- asia_late: n=231  W=136/L=95  WR=58.9%
- off_hours: n=52  W=31/L=21  WR=59.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=199  W=172/L=27  WR=86.4%
- Refine: exclude BBP=BBP5 drops 12/27 losers (44%)
- **Final: n=173  W=158/L=15  WR=91.3%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_mid  •  AVOID when just touched upper band

### W02.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=199  W=172/L=27  WR=86.4%
- Refine: exclude BBP=BBP5 drops 12/27 losers (44%)
- **Final: n=173  W=158/L=15  WR=91.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; session=ny_mid  •  AVOID when just touched upper band

### W03.  `H20=H20e AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=199  W=172/L=27  WR=86.4%
- Refine: exclude BBP=BBP5 drops 12/27 losers (44%)
- **Final: n=173  W=158/L=15  WR=91.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when just touched upper band

### W04.  `H20=H20e AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=199  W=172/L=27  WR=86.4%
- Refine: exclude BBP=BBP5 drops 12/27 losers (44%)
- **Final: n=173  W=158/L=15  WR=91.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when just touched upper band

### W05.  `H20=H20e AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=199  W=172/L=27  WR=86.4%
- Refine: exclude BBP=BBP5 drops 12/27 losers (44%)
- **Final: n=173  W=158/L=15  WR=91.3%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_mid  •  AVOID when just touched upper band

### W06.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=138  W=119/L=19  WR=86.2%
- Refine: exclude RSI=RSI6 drops 4/19 losers (21%)
- **Final: n=130  W=115/L=15  WR=88.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third; session=ny_mid  •  AVOID when RSI 70-80 overbought

### W07.  `H20=H20e AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=130  W=115/L=15  WR=88.5%
- Refine: no further refinement
- **Final: n=130  W=115/L=15  WR=88.5%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 60-70 strong; session=ny_mid

### W08.  `H20=H20e AND T1=T1a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=129  W=111/L=18  WR=86.0%
- Refine: exclude RSI=RSI6 drops 4/18 losers (22%)
- **Final: n=123  W=109/L=14  WR=88.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when RSI 70-80 overbought

### W09.  `H20=H20e AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=123  W=109/L=14  WR=88.6%
- Refine: no further refinement
- **Final: n=123  W=109/L=14  WR=88.6%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_mid

### W10.  `H60=H60e AND T1=T1c AND ZS=ZS5`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude session_bucket=asia drops 15/15 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W11.  `T1=T1c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude session_bucket=asia drops 15/15 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W12.  `H20=H20e AND H60=H60e AND T1=T1c AND ZS=ZS5`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude session_bucket=asia drops 15/15 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W13.  `H20=H20e AND T1=T1c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude session_bucket=asia drops 15/15 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W14.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude session_bucket=asia drops 15/15 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W15.  `H60=H60e AND T1=T1c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude session_bucket=asia drops 15/15 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W16.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude session_bucket=asia drops 15/15 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W17.  `H20=H20a AND T4=T4c AND ZS=ZS2`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude RSI=RSI5 drops 8/14 losers (57%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when RSI 60-70 strong

### W18.  `H20=H20a AND H60=H60a AND T4=T4c AND ZS=ZS2`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude RSI=RSI5 drops 8/14 losers (57%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when RSI 60-70 strong

### W19.  `H20=H20a AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude RSI=RSI5 drops 8/14 losers (57%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 60-70 strong

### W20.  `H20=H20a AND T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude RSI=RSI5 drops 8/14 losers (57%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when RSI 60-70 strong

### W21.  `H20=H20e AND T1=T1c AND BBP=BBP6`
- Raw: n=92  W=84/L=8  WR=91.3%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; deep above upper band  •  AVOID when session=asia

### W22.  `T4=T4c AND RSI=RSI5 AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude BBP=BBP2 drops 3/11 losers (27%)
- **Final: n=80  W=72/L=8  WR=90.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore -1 to +1 neutral; session=asia  •  AVOID when lower third

### W23.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude BBP=BBP4 drops 6/13 losers (46%)
- **Final: n=58  W=51/L=7  WR=87.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when upper third

### W24.  `T1=T1c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude BBP=BBP4 drops 6/13 losers (46%)
- **Final: n=58  W=51/L=7  WR=87.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when upper third

### W25.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude BBP=BBP4 drops 6/13 losers (46%)
- **Final: n=58  W=51/L=7  WR=87.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when upper third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=263  W=91/L=172  WR=34.6%
- Sharpen: sharpest is BBP=BBP6 (39/172 of losers there)
- **Sharp: n=39  W=0/L=39  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when deep above upper band

### L02.  `H60=H60a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=259  W=99/L=160  WR=38.2%
- Sharpen: sharpest is RSI=RSI5 (146/160 of losers there)
- **Sharp: n=215  W=69/L=146  WR=32.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L03.  `T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=259  W=99/L=160  WR=38.2%
- Sharpen: sharpest is RSI=RSI5 (146/160 of losers there)
- **Sharp: n=215  W=69/L=146  WR=32.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L04.  `H60=H60a AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=259  W=99/L=160  WR=38.2%
- Sharpen: sharpest is RSI=RSI5 (146/160 of losers there)
- **Sharp: n=215  W=69/L=146  WR=32.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L05.  `T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=251  W=91/L=160  WR=36.3%
- Sharpen: sharpest is RSI=RSI5 (146/160 of losers there)
- **Sharp: n=215  W=69/L=146  WR=32.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L06.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=251  W=91/L=160  WR=36.3%
- Sharpen: sharpest is RSI=RSI5 (146/160 of losers there)
- **Sharp: n=215  W=69/L=146  WR=32.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L07.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=251  W=91/L=160  WR=36.3%
- Sharpen: sharpest is RSI=RSI5 (146/160 of losers there)
- **Sharp: n=215  W=69/L=146  WR=32.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L08.  `H20=H20a AND H60=H60a AND T1=T1a`
- Raw: n=243  W=97/L=146  WR=39.9%
- Sharpen: sharpest is ZS=ZS5 (67/146 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H20=H20a AND T1=T1a AND direction_exec=short`
- Raw: n=243  W=97/L=146  WR=39.9%
- Sharpen: sharpest is ZS=ZS5 (67/146 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L10.  `H20=H20a AND H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=243  W=97/L=146  WR=39.9%
- Sharpen: sharpest is ZS=ZS5 (67/146 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L11.  `H20=H20e AND T1=T1a AND RSI=RSI4`
- Raw: n=230  W=91/L=139  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=230  W=91/L=139  WR=39.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral

### L12.  `H20=H20e AND H60=H60e AND T1=T1a AND RSI=RSI4`
- Raw: n=230  W=91/L=139  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=230  W=91/L=139  WR=39.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral

### L13.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=230  W=91/L=139  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=230  W=91/L=139  WR=39.6%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral

### L14.  `H20=H20a AND H60=H60a AND session_bucket=ny_mid`
- Raw: n=228  W=86/L=142  WR=37.7%
- Sharpen: sharpest is RSI=RSI5 (117/142 of losers there)
- **Sharp: n=162  W=45/L=117  WR=27.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L15.  `H20=H20a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=228  W=86/L=142  WR=37.7%
- Sharpen: sharpest is RSI=RSI5 (117/142 of losers there)
- **Sharp: n=162  W=45/L=117  WR=27.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L16.  `H20=H20a AND H60=H60a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=228  W=86/L=142  WR=37.7%
- Sharpen: sharpest is RSI=RSI5 (117/142 of losers there)
- **Sharp: n=162  W=45/L=117  WR=27.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L17.  `H20=H20a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=220  W=78/L=142  WR=35.5%
- Sharpen: sharpest is RSI=RSI5 (117/142 of losers there)
- **Sharp: n=162  W=45/L=117  WR=27.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L18.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=220  W=78/L=142  WR=35.5%
- Sharpen: sharpest is RSI=RSI5 (117/142 of losers there)
- **Sharp: n=162  W=45/L=117  WR=27.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L19.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=220  W=78/L=142  WR=35.5%
- Sharpen: sharpest is RSI=RSI5 (117/142 of losers there)
- **Sharp: n=162  W=45/L=117  WR=27.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L20.  `H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=217  W=71/L=146  WR=32.7%
- Sharpen: sharpest is ZS=ZS5 (67/146 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L21.  `T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=217  W=71/L=146  WR=32.7%
- Sharpen: sharpest is ZS=ZS5 (67/146 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L22.  `H20=H20a AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=217  W=71/L=146  WR=32.7%
- Sharpen: sharpest is ZS=ZS5 (67/146 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=217  W=71/L=146  WR=32.7%
- Sharpen: sharpest is ZS=ZS5 (67/146 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `H60=H60a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=217  W=71/L=146  WR=32.7%
- Sharpen: sharpest is ZS=ZS5 (67/146 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=215  W=69/L=146  WR=32.1%
- Sharpen: sharpest is BBP=BBP6 (39/146 of losers there)
- **Sharp: n=39  W=0/L=39  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when deep above upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1c(55/48) | T1a(45/52) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
