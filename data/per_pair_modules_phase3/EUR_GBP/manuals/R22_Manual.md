# EUR_GBP — R22 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,110**  (W=735 / L=375)  -  WR: **66.2%**

## Session distribution

- london_open: n=223  W=146/L=77  WR=65.5%
- ny_mid: n=223  W=154/L=69  WR=69.1%
- asia: n=184  W=122/L=62  WR=66.3%
- london: n=147  W=100/L=47  WR=68.0%
- ny_close: n=132  W=81/L=51  WR=61.4%
- asia_late: n=98  W=65/L=33  WR=66.3%
- ny_open: n=63  W=42/L=21  WR=66.7%
- off_hours: n=40  W=25/L=15  WR=62.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=258  W=225/L=33  WR=87.2%
- Refine: exclude BBP=BBP4 drops 26/33 losers (79%)
- **Final: n=130  W=123/L=7  WR=94.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when upper third

### W02.  `H20=H20a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=149  W=134/L=15  WR=89.9%
- Refine: exclude BBP=BBP4 drops 12/15 losers (80%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  AVOID when upper third

### W03.  `H20=H20a AND T1=T1c AND RSI=RSI5`
- Raw: n=146  W=132/L=14  WR=90.4%
- Refine: exclude session_bucket=ny_mid drops 6/14 losers (43%)
- **Final: n=119  W=111/L=8  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W04.  `H20=H20a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=146  W=132/L=14  WR=90.4%
- Refine: exclude session_bucket=ny_mid drops 6/14 losers (43%)
- **Final: n=119  W=111/L=8  WR=93.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W05.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=137  W=121/L=16  WR=88.3%
- Refine: exclude BBP=BBP1 drops 10/16 losers (62%)
- **Final: n=99  W=93/L=6  WR=93.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak  •  AVOID when just touched lower band

### W06.  `T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=136  W=125/L=11  WR=91.9%
- Refine: exclude session_bucket=london_open drops 9/11 losers (82%)
- **Final: n=97  W=95/L=2  WR=97.9%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W07.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=136  W=123/L=13  WR=90.4%
- Refine: exclude T4=T4c drops 11/13 losers (85%)
- **Final: n=81  W=79/L=2  WR=97.5%**
- **Dir: SHORT**  •  upper third; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W08.  `T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=133  W=123/L=10  WR=92.5%
- Refine: exclude H20=H20e drops 8/10 losers (80%)
- **Final: n=100  W=98/L=2  WR=98.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 strongly against

### W09.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=133  W=123/L=10  WR=92.5%
- Refine: exclude H20=H20e drops 8/10 losers (80%)
- **Final: n=100  W=98/L=2  WR=98.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 strongly against

### W10.  `T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude ZS=ZS4 drops 8/19 losers (42%)
- **Final: n=112  W=101/L=11  WR=90.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when zscore +1 to +2 overbought

### W11.  `H20=H20a AND H60=H60a AND T1=T1c`
- Raw: n=125  W=113/L=12  WR=90.4%
- Refine: exclude session_bucket=ny_mid drops 6/12 losers (50%)
- **Final: n=102  W=96/L=6  WR=94.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=ny_mid

### W12.  `H20=H20a AND H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=125  W=113/L=12  WR=90.4%
- Refine: exclude session_bucket=ny_mid drops 6/12 losers (50%)
- **Final: n=102  W=96/L=6  WR=94.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=ny_mid

### W13.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=121  W=103/L=18  WR=85.1%
- Refine: exclude direction_exec=long drops 16/18 losers (89%)
- **Final: n=81  W=79/L=2  WR=97.5%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when long

### W14.  `H20=H20b AND T1=T1c AND direction_exec=short`
- Raw: n=120  W=106/L=14  WR=88.3%
- Refine: exclude T4=T4c drops 10/14 losers (71%)
- **Final: n=99  W=95/L=4  WR=96.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend AGAINST trade  •  AVOID when 4h trend AGAINST trade

### W15.  `T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=119  W=108/L=11  WR=90.8%
- Refine: exclude H60=H60b drops 3/11 losers (27%)
- **Final: n=116  W=108/L=8  WR=93.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 slightly aligned

### W16.  `RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=116  W=104/L=12  WR=89.7%
- Refine: exclude T4=T4c drops 11/12 losers (92%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 4h trend AGAINST trade

### W17.  `BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=116  W=104/L=12  WR=89.7%
- Refine: exclude T4=T4c drops 11/12 losers (92%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: SHORT**  •  upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 4h trend AGAINST trade

### W18.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=116  W=101/L=15  WR=87.1%
- Refine: exclude T4=T4c drops 10/15 losers (67%)
- **Final: n=80  W=75/L=5  WR=93.8%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W19.  `H20=H20b AND T1=T1c AND T4=T4a`
- Raw: n=115  W=111/L=4  WR=96.5%
- Refine: exclude RSI=RSI2 drops 3/4 losers (75%)
- **Final: n=106  W=105/L=1  WR=99.1%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when RSI 30-40 weak

### W20.  `T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=112  W=101/L=11  WR=90.2%
- Refine: exclude H20=H20b drops 6/11 losers (55%)
- **Final: n=106  W=101/L=5  WR=95.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W21.  `H20=H20a AND H60=H60a AND RSI=RSI5`
- Raw: n=112  W=100/L=12  WR=89.3%
- Refine: exclude session_bucket=ny_mid drops 6/12 losers (50%)
- **Final: n=97  W=91/L=6  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W22.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=112  W=100/L=12  WR=89.3%
- Refine: exclude session_bucket=ny_mid drops 6/12 losers (50%)
- **Final: n=97  W=91/L=6  WR=93.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W23.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI5`
- Raw: n=109  W=98/L=11  WR=89.9%
- Refine: exclude session_bucket=ny_mid drops 6/11 losers (55%)
- **Final: n=94  W=89/L=5  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W24.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=105  W=92/L=13  WR=87.6%
- Refine: exclude T4=T4c drops 10/13 losers (77%)
- **Final: n=72  W=69/L=3  WR=95.8%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 4h trend AGAINST trade

### W25.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=105  W=92/L=13  WR=87.6%
- Refine: exclude T4=T4c drops 10/13 losers (77%)
- **Final: n=72  W=69/L=3  WR=95.8%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 4h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=164  W=56/L=108  WR=34.1%
- Sharpen: sharpest is H20=H20e (63/108 of losers there)
- **Sharp: n=85  W=22/L=63  WR=25.9%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L02.  `H20=H20e AND RSI=RSI5 AND direction_exec=long`
- Raw: n=95  W=27/L=68  WR=28.4%
- Sharpen: sharpest is session_bucket=london (16/68 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 60-70 strong  •  ONLY when session=london

### L03.  `H20=H20e AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=94  W=36/L=58  WR=38.3%
- Sharpen: sharpest is RSI=RSI5 (50/58 of losers there)
- **Sharp: n=68  W=18/L=50  WR=26.5%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L04.  `T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=91  W=26/L=65  WR=28.6%
- Sharpen: sharpest is RSI=RSI2 (54/65 of losers there)
- **Sharp: n=65  W=11/L=54  WR=16.9%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 30-40 weak

### L05.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is H20=H20e (38/54 of losers there)
- **Sharp: n=54  W=16/L=38  WR=29.6%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L06.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is H20=H20e (38/53 of losers there)
- **Sharp: n=54  W=16/L=38  WR=29.6%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L07.  `T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=85  W=19/L=66  WR=22.4%
- Sharpen: sharpest is H20=H20a (31/66 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 aligned WITH trade

### L08.  `H20=H20e AND T1=T1a AND RSI=RSI5`
- Raw: n=85  W=22/L=63  WR=25.9%
- Sharpen: sharpest is session_bucket=london (16/63 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L09.  `H20=H20e AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=85  W=22/L=63  WR=25.9%
- Sharpen: sharpest is session_bucket=london (16/63 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L10.  `T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=85  W=32/L=53  WR=37.6%
- Sharpen: sharpest is T4=T4c (31/53 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L11.  `H20=H20d AND T1=T1a AND T4=T4c`
- Raw: n=82  W=25/L=57  WR=30.5%
- Sharpen: sharpest is H60=H60e (9/57 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF60 strongly against

### L12.  `T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=75  W=21/L=54  WR=28.0%
- Sharpen: sharpest is BBP=BBP5 (18/54 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when just touched upper band

### L13.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is T4=T4c (29/45 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: LONG**  •  upper third; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L14.  `H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=71  W=17/L=54  WR=23.9%
- Sharpen: sharpest is direction_exec=short (38/54 of losers there)
- **Sharp: n=45  W=7/L=38  WR=15.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when short

### L15.  `H20=H20e AND H60=H60e AND T1=T1a`
- Raw: n=70  W=21/L=49  WR=30.0%
- Sharpen: sharpest is ZS=ZS5 (13/49 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `H20=H20e AND H60=H60e AND T1=T1a AND direction_exec=long`
- Raw: n=70  W=21/L=49  WR=30.0%
- Sharpen: sharpest is ZS=ZS5 (13/49 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L17.  `H20=H20e AND H60=H60e AND RSI=RSI5`
- Raw: n=70  W=22/L=48  WR=31.4%
- Sharpen: sharpest is ZS=ZS5 (13/48 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L18.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND direction_exec=long`
- Raw: n=70  W=22/L=48  WR=31.4%
- Sharpen: sharpest is ZS=ZS5 (13/48 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L19.  `H20=H20d AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=69  W=21/L=48  WR=30.4%
- Sharpen: sharpest is RSI=RSI4 (20/48 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L20.  `H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=69  W=23/L=46  WR=33.3%
- Sharpen: sharpest is T4=T4a (38/46 of losers there)
- **Sharp: n=45  W=7/L=38  WR=15.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when 4h trend WITH trade

### L21.  `T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=68  W=11/L=57  WR=16.2%
- Sharpen: sharpest is H20=H20a (27/57 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 aligned WITH trade

### L22.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=68  W=18/L=50  WR=26.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=68  W=18/L=50  WR=26.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong

### L23.  `H20=H20e AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=68  W=18/L=50  WR=26.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=68  W=18/L=50  WR=26.5%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; RSI 60-70 strong

### L24.  `T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=65  W=11/L=54  WR=16.9%
- Sharpen: sharpest is H20=H20a (27/54 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 aligned WITH trade

### L25.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=65  W=11/L=54  WR=16.9%
- Sharpen: sharpest is H20=H20a (27/54 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(23/14) | H20d(16/22) |
| H60 | — | — |
| T1 | T1c(69/29) | T1a(30/70) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(56/45) | long(44/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
