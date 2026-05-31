# EUR_USD — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,355**  (W=1,463 / L=892)  -  WR: **62.1%**

## Session distribution

- ny_mid: n=669  W=418/L=251  WR=62.5%
- london_open: n=543  W=341/L=202  WR=62.8%
- ny_open: n=423  W=252/L=171  WR=59.6%
- london: n=251  W=159/L=92  WR=63.3%
- asia: n=244  W=157/L=87  WR=64.3%
- ny_close: n=144  W=82/L=62  WR=56.9%
- asia_late: n=81  W=54/L=27  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=214  W=186/L=28  WR=86.9%
- Refine: exclude H20=H20e drops 13/28 losers (46%)
- **Final: n=152  W=137/L=15  WR=90.1%**
- **Dir: LONG**  •  1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when HTF20 strongly against

### W02.  `H60=H60a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=193  W=175/L=18  WR=90.7%
- Refine: exclude ZS=ZS4 drops 13/18 losers (72%)
- **Final: n=105  W=100/L=5  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W03.  `H60=H60a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=190  W=165/L=25  WR=86.8%
- Refine: exclude RSI=RSI6 drops 14/25 losers (56%)
- **Final: n=154  W=143/L=11  WR=92.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_mid  •  AVOID when RSI 70-80 overbought

### W04.  `H60=H60a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=187  W=162/L=25  WR=86.6%
- Refine: exclude RSI=RSI6 drops 14/25 losers (56%)
- **Final: n=151  W=140/L=11  WR=92.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when RSI 70-80 overbought

### W05.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=184  W=159/L=25  WR=86.4%
- Refine: exclude RSI=RSI6 drops 14/25 losers (56%)
- **Final: n=148  W=137/L=11  WR=92.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when RSI 70-80 overbought

### W06.  `H60=H60a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=171  W=146/L=25  WR=85.4%
- Refine: exclude RSI=RSI6 drops 14/25 losers (56%)
- **Final: n=135  W=124/L=11  WR=91.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when RSI 70-80 overbought

### W07.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=171  W=146/L=25  WR=85.4%
- Refine: exclude RSI=RSI6 drops 14/25 losers (56%)
- **Final: n=135  W=124/L=11  WR=91.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when RSI 70-80 overbought

### W08.  `T4=T4a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=169  W=150/L=19  WR=88.8%
- Refine: exclude H20=H20e drops 8/19 losers (42%)
- **Final: n=136  W=125/L=11  WR=91.9%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when HTF20 strongly against

### W09.  `T1=T1a AND T4=T4a AND ZS=ZS3`
- Raw: n=165  W=146/L=19  WR=88.5%
- Refine: exclude H20=H20e drops 8/19 losers (42%)
- **Final: n=132  W=121/L=11  WR=91.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when HTF20 strongly against

### W10.  `T1=T1a AND T4=T4a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=165  W=146/L=19  WR=88.5%
- Refine: exclude H20=H20e drops 8/19 losers (42%)
- **Final: n=132  W=121/L=11  WR=91.7%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when HTF20 strongly against

### W11.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=154  W=143/L=11  WR=92.9%
- Refine: exclude ZS=ZS4 drops 11/11 losers (100%)
- **Final: n=85  W=85/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W12.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=151  W=140/L=11  WR=92.7%
- Refine: exclude ZS=ZS4 drops 11/11 losers (100%)
- **Final: n=79  W=79/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W13.  `RSI=RSI5 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=138  W=120/L=18  WR=87.0%
- Refine: exclude H20=H20e drops 9/18 losers (50%)
- **Final: n=96  W=87/L=9  WR=90.6%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when HTF20 strongly against

### W14.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=138  W=118/L=20  WR=85.5%
- Refine: exclude H20=H20a drops 20/20 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W15.  `T1=T1a AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=136  W=118/L=18  WR=86.8%
- Refine: exclude H20=H20e drops 9/18 losers (50%)
- **Final: n=94  W=85/L=9  WR=90.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when HTF20 strongly against

### W16.  `T1=T1a AND RSI=RSI5 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=136  W=118/L=18  WR=86.8%
- Refine: exclude H20=H20e drops 9/18 losers (50%)
- **Final: n=94  W=85/L=9  WR=90.4%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when HTF20 strongly against

### W17.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=135  W=124/L=11  WR=91.9%
- Refine: exclude ZS=ZS4 drops 11/11 losers (100%)
- **Final: n=66  W=66/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W18.  `T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=130  W=116/L=14  WR=89.2%
- Refine: exclude RSI=RSI4 drops 13/14 losers (93%)
- **Final: n=113  W=112/L=1  WR=99.1%**
- **Dir: LONG**  •  1h trend WITH trade; session=london  •  AVOID when RSI 50-60 upper neutral

### W19.  `H20=H20a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=124  W=111/L=13  WR=89.5%
- Refine: exclude session_bucket=london drops 4/13 losers (31%)
- **Final: n=113  W=104/L=9  WR=92.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore -1 to +1 neutral  •  AVOID when session=london

### W20.  `BBP=BBP3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=124  W=110/L=14  WR=88.7%
- Refine: exclude H20=H20e drops 9/14 losers (64%)
- **Final: n=79  W=74/L=5  WR=93.7%**
- **Dir: LONG**  •  middle of band; zscore -1 to +1 neutral  •  AVOID when HTF20 strongly against

### W21.  `H20=H20a AND direction_exec=long AND session_bucket=london`
- Raw: n=122  W=108/L=14  WR=88.5%
- Refine: exclude RSI=RSI4 drops 13/14 losers (93%)
- **Final: n=105  W=104/L=1  WR=99.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london  •  AVOID when RSI 50-60 upper neutral

### W22.  `T1=T1a AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=122  W=106/L=16  WR=86.9%
- Refine: exclude RSI=RSI4 drops 7/16 losers (44%)
- **Final: n=107  W=98/L=9  WR=91.6%**
- **Dir: ?**  •  1h trend WITH trade; middle of band; zscore -1 to +1 neutral  •  AVOID when RSI 50-60 upper neutral

### W23.  `H20=H20a AND T1=T1a AND ZS=ZS3`
- Raw: n=120  W=107/L=13  WR=89.2%
- Refine: exclude session_bucket=london drops 4/13 losers (31%)
- **Final: n=109  W=100/L=9  WR=91.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=london

### W24.  `H20=H20a AND T1=T1a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=120  W=107/L=13  WR=89.2%
- Refine: exclude session_bucket=london drops 4/13 losers (31%)
- **Final: n=109  W=100/L=9  WR=91.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=london

### W25.  `T1=T1a AND BBP=BBP3 AND direction_exec=long`
- Raw: n=120  W=106/L=14  WR=88.3%
- Refine: exclude H20=H20e drops 9/14 losers (64%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: LONG**  •  1h trend WITH trade; middle of band  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=308  W=120/L=188  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_mid (107/188 of losers there)
- **Sharp: n=156  W=49/L=107  WR=31.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L02.  `H20=H20e AND H60=H60e AND T4=T4c`
- Raw: n=224  W=88/L=136  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=224  W=88/L=136  WR=39.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade

### L03.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=211  W=84/L=127  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_mid (94/127 of losers there)
- **Sharp: n=120  W=26/L=94  WR=21.7%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong  •  ONLY when session=ny_mid

### L04.  `H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=204  W=71/L=133  WR=34.8%
- Sharpen: sharpest is session_bucket=ny_mid (93/133 of losers there)
- **Sharp: n=120  W=27/L=93  WR=22.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L05.  `H20=H20e AND H60=H60e AND RSI=RSI5`
- Raw: n=198  W=78/L=120  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_mid (67/120 of losers there)
- **Sharp: n=93  W=26/L=67  WR=28.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when session=ny_mid

### L06.  `H60=H60e AND BBP=BBP4 AND direction_exec=short`
- Raw: n=192  W=70/L=122  WR=36.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=192  W=70/L=122  WR=36.5%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third

### L07.  `H60=H60e AND T4=T4c AND BBP=BBP4`
- Raw: n=190  W=63/L=127  WR=33.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=190  W=63/L=127  WR=33.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third

### L08.  `H20=H20e AND H60=H60e AND direction_exec=short`
- Raw: n=189  W=68/L=121  WR=36.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=189  W=68/L=121  WR=36.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against

### L09.  `H60=H60e AND T1=T1c AND BBP=BBP4`
- Raw: n=186  W=68/L=118  WR=36.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=186  W=68/L=118  WR=36.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third

### L10.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=185  W=68/L=117  WR=36.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=185  W=68/L=117  WR=36.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third

### L11.  `H20=H20e AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=181  W=66/L=115  WR=36.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=181  W=66/L=115  WR=36.5%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade

### L12.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=177  W=58/L=119  WR=32.8%
- Sharpen: sharpest is session_bucket=ny_mid (91/119 of losers there)
- **Sharp: n=117  W=26/L=91  WR=22.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L13.  `H60=H60e AND ZS=ZS4 AND direction_exec=short`
- Raw: n=175  W=66/L=109  WR=37.7%
- Sharpen: sharpest is session_bucket=ny_mid (57/109 of losers there)
- **Sharp: n=80  W=23/L=57  WR=28.7%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L14.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=175  W=66/L=109  WR=37.7%
- Sharpen: sharpest is session_bucket=ny_mid (57/109 of losers there)
- **Sharp: n=80  W=23/L=57  WR=28.7%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L15.  `H60=H60e AND T4=T4c AND ZS=ZS4`
- Raw: n=172  W=59/L=113  WR=34.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=172  W=59/L=113  WR=34.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought

### L16.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=172  W=59/L=113  WR=34.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=172  W=59/L=113  WR=34.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought

### L17.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=170  W=56/L=114  WR=32.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=170  W=56/L=114  WR=32.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third

### L18.  `T1=T1c AND ZS=ZS3 AND direction_exec=short`
- Raw: n=169  W=51/L=118  WR=30.2%
- Sharpen: sharpest is RSI=RSI6 (24/118 of losers there)
- **Sharp: n=25  W=1/L=24  WR=4.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when RSI 70-80 overbought

### L19.  `H60=H60e AND T1=T1c AND ZS=ZS4`
- Raw: n=169  W=64/L=105  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_mid (57/105 of losers there)
- **Sharp: n=80  W=23/L=57  WR=28.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L20.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=169  W=64/L=105  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_mid (57/105 of losers there)
- **Sharp: n=80  W=23/L=57  WR=28.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L21.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=168  W=56/L=112  WR=33.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=168  W=56/L=112  WR=33.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third

### L22.  `H60=H60e AND T1=T1c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=168  W=64/L=104  WR=38.1%
- Sharpen: sharpest is session_bucket=ny_mid (57/104 of losers there)
- **Sharp: n=80  W=23/L=57  WR=28.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L23.  `H20=H20e AND H60=H60e AND T1=T1c`
- Raw: n=167  W=66/L=101  WR=39.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=167  W=66/L=101  WR=39.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade

### L24.  `H20=H20e AND H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=167  W=66/L=101  WR=39.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=167  W=66/L=101  WR=39.5%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade

### L25.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=164  W=58/L=106  WR=35.4%
- Sharpen: sharpest is session_bucket=ny_mid (78/106 of losers there)
- **Sharp: n=104  W=26/L=78  WR=25.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(51/31) | H20e(32/53) |
| H60 | — | H60e(34/39) |
| T1 | T1a(59/36) | T1c(40/63) |
| T4 | T4a(58/37) | T4c(41/62) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(60/35) | short(40/65) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
