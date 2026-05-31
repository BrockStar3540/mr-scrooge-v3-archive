# GBP_USD — R25 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,847**  (W=2,421 / L=1,426)  -  WR: **62.9%**

## Session distribution

- asia: n=1219  W=762/L=457  WR=62.5%
- london_open: n=797  W=518/L=279  WR=65.0%
- ny_close: n=421  W=265/L=156  WR=62.9%
- ny_mid: n=413  W=265/L=148  WR=64.2%
- london: n=394  W=257/L=137  WR=65.2%
- ny_open: n=283  W=169/L=114  WR=59.7%
- asia_late: n=234  W=137/L=97  WR=58.5%
- off_hours: n=86  W=48/L=38  WR=55.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=163  W=144/L=19  WR=88.3%
- Refine: exclude ZS=ZS2 drops 9/19 losers (47%)
- **Final: n=139  W=129/L=10  WR=92.8%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W02.  `H20=H20e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=157  W=144/L=13  WR=91.7%
- Refine: exclude BBP=BBP3 drops 6/13 losers (46%)
- **Final: n=127  W=120/L=7  WR=94.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_mid  •  AVOID when middle of band

### W03.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=157  W=144/L=13  WR=91.7%
- Refine: exclude BBP=BBP3 drops 6/13 losers (46%)
- **Final: n=127  W=120/L=7  WR=94.5%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_mid  •  AVOID when middle of band

### W04.  `H20=H20a AND H60=H60b AND T4=T4c`
- Raw: n=153  W=141/L=12  WR=92.2%
- Refine: exclude direction_exec=short drops 11/12 losers (92%)
- **Final: n=90  W=89/L=1  WR=98.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 4h trend AGAINST trade  •  AVOID when short

### W05.  `T1=T1c AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=146  W=125/L=21  WR=85.6%
- Refine: exclude session_bucket=ny_close drops 6/21 losers (29%)
- **Final: n=140  W=125/L=15  WR=89.3%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched upper band; RSI 60-70 strong  •  AVOID when session=ny_close

### W06.  `T1=T1c AND BBP=BBP5 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=146  W=125/L=21  WR=85.6%
- Refine: exclude session_bucket=ny_close drops 6/21 losers (29%)
- **Final: n=140  W=125/L=15  WR=89.3%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W07.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude session_bucket=asia drops 12/21 losers (57%)
- **Final: n=90  W=81/L=9  WR=90.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=asia

### W08.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude session_bucket=asia drops 12/21 losers (57%)
- **Final: n=90  W=81/L=9  WR=90.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=asia

### W09.  `T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=133  W=116/L=17  WR=87.2%
- Refine: exclude RSI=RSI5 drops 13/17 losers (76%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when RSI 60-70 strong

### W10.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=133  W=116/L=17  WR=87.2%
- Refine: exclude RSI=RSI5 drops 13/17 losers (76%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when RSI 60-70 strong

### W11.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI5`
- Raw: n=129  W=110/L=19  WR=85.3%
- Refine: exclude session_bucket=asia drops 10/19 losers (53%)
- **Final: n=78  W=69/L=9  WR=88.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=asia

### W12.  `T1=T1c AND BBP=BBP5 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=128  W=113/L=15  WR=88.3%
- Refine: exclude session_bucket=ny_close drops 6/15 losers (40%)
- **Final: n=122  W=113/L=9  WR=92.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band; RSI 60-70 strong  •  AVOID when session=ny_close

### W13.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=125  W=108/L=17  WR=86.4%
- Refine: exclude T1=T1a drops 6/17 losers (35%)
- **Final: n=119  W=108/L=11  WR=90.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_mid  •  AVOID when 1h trend WITH trade

### W14.  `H60=H60b AND T1=T1a AND T4=T4c`
- Raw: n=124  W=118/L=6  WR=95.2%
- Refine: exclude session_bucket=ny_open drops 5/6 losers (83%)
- **Final: n=94  W=93/L=1  WR=98.9%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W15.  `H60=H60b AND T4=T4c AND BBP=BBP4`
- Raw: n=120  W=113/L=7  WR=94.2%
- Refine: exclude session_bucket=ny_mid drops 5/7 losers (71%)
- **Final: n=111  W=109/L=2  WR=98.2%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend AGAINST trade; upper third  •  AVOID when session=ny_mid

### W16.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=119  W=108/L=11  WR=90.8%
- Refine: exclude BBP=BBP3 drops 5/11 losers (45%)
- **Final: n=92  W=86/L=6  WR=93.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when middle of band

### W17.  `H20=H20a AND H60=H60b AND T1=T1a AND T4=T4c`
- Raw: n=117  W=113/L=4  WR=96.6%
- Refine: exclude BBP=BBP5 drops 3/4 losers (75%)
- **Final: n=101  W=100/L=1  WR=99.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when just touched upper band

### W18.  `ZS=ZS5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=111  W=99/L=12  WR=89.2%
- Refine: exclude T4=T4a drops 7/12 losers (58%)
- **Final: n=104  W=99/L=5  WR=95.2%**
- **Dir: SHORT**  •  zscore +2 to +3 deep overbought; session=london_open  •  AVOID when 4h trend WITH trade

### W19.  `H20=H20e AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=111  W=97/L=14  WR=87.4%
- Refine: exclude ZS=ZS6 drops 9/14 losers (64%)
- **Final: n=79  W=74/L=5  WR=93.7%**
- **Dir: SHORT**  •  HTF20 strongly against; deep above upper band; RSI 50-60 upper neutral  •  AVOID when zscore >+3 extreme

### W20.  `H60=H60b AND T4=T4c AND RSI=RSI5`
- Raw: n=109  W=100/L=9  WR=91.7%
- Refine: exclude session_bucket=ny_mid drops 6/9 losers (67%)
- **Final: n=95  W=92/L=3  WR=96.8%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W21.  `T1=T1c AND T4=T4c AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=108  W=96/L=12  WR=88.9%
- Refine: exclude session_bucket=ny_close drops 6/12 losers (50%)
- **Final: n=102  W=96/L=6  WR=94.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band; RSI 60-70 strong  •  AVOID when session=ny_close

### W22.  `T1=T1c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude H60=H60e drops 13/16 losers (81%)
- **Final: n=70  W=67/L=3  WR=95.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF60 strongly against

### W23.  `T4=T4c AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=106  W=101/L=5  WR=95.3%
- Refine: exclude H60=H60e drops 2/5 losers (40%)
- **Final: n=88  W=85/L=3  WR=96.6%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when HTF60 strongly against

### W24.  `T4=T4c AND ZS=ZS5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=104  W=99/L=5  WR=95.2%
- Refine: exclude H60=H60e drops 2/5 losers (40%)
- **Final: n=86  W=83/L=3  WR=96.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when HTF60 strongly against

### W25.  `T1=T1a AND T4=T4c AND session_bucket=london_open`
- Raw: n=104  W=93/L=11  WR=89.4%
- Refine: exclude RSI=RSI4 drops 10/11 losers (91%)
- **Final: n=88  W=87/L=1  WR=98.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when RSI 50-60 upper neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=198  W=79/L=119  WR=39.9%
- Sharpen: sharpest is T4=T4a (92/119 of losers there)
- **Sharp: n=132  W=40/L=92  WR=30.3%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L02.  `T4=T4a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=170  W=66/L=104  WR=38.8%
- Sharpen: sharpest is T1=T1a (92/104 of losers there)
- **Sharp: n=132  W=40/L=92  WR=30.3%**
- **Dir: LONG**  •  4h trend WITH trade; just touched upper band  •  ONLY when 1h trend WITH trade

### L03.  `T4=T4a AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=170  W=66/L=104  WR=38.8%
- Sharpen: sharpest is T1=T1a (92/104 of losers there)
- **Sharp: n=132  W=40/L=92  WR=30.3%**
- **Dir: LONG**  •  4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 1h trend WITH trade

### L04.  `H60=H60e AND T1=T1c AND BBP=BBP4`
- Raw: n=168  W=67/L=101  WR=39.9%
- Sharpen: sharpest is H20=H20e (63/101 of losers there)
- **Sharp: n=91  W=28/L=63  WR=30.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when HTF20 strongly against

### L05.  `T1=T1a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=164  W=57/L=107  WR=34.8%
- Sharpen: sharpest is H20=H20e (42/107 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: LONG**  •  1h trend WITH trade; just touched upper band  •  ONLY when HTF20 strongly against

### L06.  `T1=T1a AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=164  W=57/L=107  WR=34.8%
- Sharpen: sharpest is H20=H20e (42/107 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: LONG**  •  1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L07.  `H20=H20e AND H60=H60e AND BBP=BBP4`
- Raw: n=163  W=65/L=98  WR=39.9%
- Sharpen: sharpest is T1=T1c (63/98 of losers there)
- **Sharp: n=91  W=28/L=63  WR=30.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third  •  ONLY when 1h trend AGAINST trade

### L08.  `H60=H60e AND T1=T1c AND ZS=ZS4`
- Raw: n=162  W=63/L=99  WR=38.9%
- Sharpen: sharpest is H20=H20e (62/99 of losers there)
- **Sharp: n=90  W=28/L=62  WR=31.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L09.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=162  W=63/L=99  WR=38.9%
- Sharpen: sharpest is H20=H20e (62/99 of losers there)
- **Sharp: n=90  W=28/L=62  WR=31.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L10.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=145  W=52/L=93  WR=35.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=145  W=52/L=93  WR=35.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third

### L11.  `H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=142  W=53/L=89  WR=37.3%
- Sharpen: sharpest is T1=T1c (76/89 of losers there)
- **Sharp: n=104  W=28/L=76  WR=26.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when 1h trend AGAINST trade

### L12.  `H60=H60e AND T1=T1c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=139  W=48/L=91  WR=34.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=139  W=48/L=91  WR=34.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought

### L13.  `T1=T1a AND T4=T4a AND BBP=BBP5`
- Raw: n=132  W=40/L=92  WR=30.3%
- Sharpen: sharpest is session_bucket=asia (28/92 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched upper band  •  ONLY when session=asia

### L14.  `T1=T1a AND T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=132  W=40/L=92  WR=30.3%
- Sharpen: sharpest is session_bucket=asia (28/92 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L15.  `T1=T1a AND T4=T4a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=132  W=40/L=92  WR=30.3%
- Sharpen: sharpest is session_bucket=asia (28/92 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; just touched upper band  •  ONLY when session=asia

### L16.  `H20=H20e AND H60=H60d AND T4=T4a`
- Raw: n=120  W=24/L=96  WR=20.0%
- Sharpen: sharpest is direction_exec=short (60/96 of losers there)
- **Sharp: n=68  W=8/L=60  WR=11.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 4h trend WITH trade  •  ONLY when short

### L17.  `H20=H20a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=120  W=44/L=76  WR=36.7%
- Sharpen: sharpest is ZS=ZS5 (21/76 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L18.  `H20=H20e AND H60=H60a AND T1=T1a AND RSI=RSI4`
- Raw: n=112  W=44/L=68  WR=39.3%
- Sharpen: sharpest is T4=T4a (30/68 of losers there)
- **Sharp: n=42  W=12/L=30  WR=28.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L19.  `H20=H20a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=111  W=35/L=76  WR=31.5%
- Sharpen: sharpest is ZS=ZS5 (21/76 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L20.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=111  W=35/L=76  WR=31.5%
- Sharpen: sharpest is ZS=ZS5 (21/76 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L21.  `T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=109  W=41/L=68  WR=37.6%
- Sharpen: sharpest is T1=T1a (68/68 of losers there)
- **Sharp: n=100  W=32/L=68  WR=32.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_mid  •  ONLY when 1h trend WITH trade

### L22.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=105  W=39/L=66  WR=37.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia

### L23.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=104  W=28/L=76  WR=26.9%
- Sharpen: sharpest is BBP=BBP6 (14/76 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when deep above upper band

### L24.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=104  W=28/L=76  WR=26.9%
- Sharpen: sharpest is BBP=BBP6 (14/76 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when deep above upper band

### L25.  `H20=H20a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=101  W=30/L=71  WR=29.7%
- Sharpen: sharpest is BBP=BBP5 (18/71 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when just touched upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(37/31), H60b(15/10) | H60e(31/38) |
| T1 | — | — |
| T4 | T4c(54/45) | T4a(46/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/47) | long(46/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
