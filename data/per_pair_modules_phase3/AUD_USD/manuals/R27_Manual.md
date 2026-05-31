# AUD_USD — R27 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,196**  (W=1,387 / L=809)  -  WR: **63.2%**

## Session distribution

- ny_mid: n=692  W=438/L=254  WR=63.3%
- asia: n=495  W=310/L=185  WR=62.6%
- london_open: n=320  W=207/L=113  WR=64.7%
- ny_close: n=239  W=130/L=109  WR=54.4%
- ny_open: n=225  W=150/L=75  WR=66.7%
- london: n=138  W=84/L=54  WR=60.9%
- asia_late: n=87  W=68/L=19  WR=78.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=324  W=281/L=43  WR=86.7%
- Refine: exclude session_bucket=asia drops 14/43 losers (33%)
- **Final: n=278  W=249/L=29  WR=89.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=asia

### W02.  `H60=H60d AND T1=T1a AND T4=T4a`
- Raw: n=205  W=175/L=30  WR=85.4%
- Refine: exclude session_bucket=london_open drops 12/30 losers (40%)
- **Final: n=191  W=173/L=18  WR=90.6%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=london_open

### W03.  `H60=H60d AND T1=T1a AND direction_exec=long`
- Raw: n=205  W=175/L=30  WR=85.4%
- Refine: exclude session_bucket=london_open drops 12/30 losers (40%)
- **Final: n=191  W=173/L=18  WR=90.6%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend WITH trade  •  AVOID when session=london_open

### W04.  `H60=H60d AND T4=T4a AND direction_exec=long`
- Raw: n=205  W=175/L=30  WR=85.4%
- Refine: exclude session_bucket=london_open drops 12/30 losers (40%)
- **Final: n=191  W=173/L=18  WR=90.6%**
- **Dir: LONG**  •  HTF60 mildly against; 4h trend WITH trade  •  AVOID when session=london_open

### W05.  `H60=H60d AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=205  W=175/L=30  WR=85.4%
- Refine: exclude session_bucket=london_open drops 12/30 losers (40%)
- **Final: n=191  W=173/L=18  WR=90.6%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=london_open

### W06.  `H60=H60a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=179  W=160/L=19  WR=89.4%
- Refine: exclude H20=H20a drops 19/19 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W07.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=162  W=140/L=22  WR=86.4%
- Refine: exclude T1=T1c drops 7/22 losers (32%)
- **Final: n=155  W=140/L=15  WR=90.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; RSI 60-70 strong  •  AVOID when 1h trend AGAINST trade

### W08.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=155  W=134/L=21  WR=86.5%
- Refine: exclude T1=T1c drops 6/21 losers (29%)
- **Final: n=149  W=134/L=15  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W09.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=147  W=128/L=19  WR=87.1%
- Refine: exclude T1=T1c drops 9/19 losers (47%)
- **Final: n=132  W=122/L=10  WR=92.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W10.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=147  W=128/L=19  WR=87.1%
- Refine: exclude T1=T1c drops 9/19 losers (47%)
- **Final: n=132  W=122/L=10  WR=92.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W11.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=132  W=122/L=10  WR=92.4%
- Refine: exclude ZS=ZS2 drops 4/10 losers (40%)
- **Final: n=116  W=110/L=6  WR=94.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W12.  `H20=H20e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=110  W=95/L=15  WR=86.4%
- Refine: exclude RSI=RSI4 drops 12/15 losers (80%)
- **Final: n=85  W=82/L=3  WR=96.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when RSI 50-60 upper neutral

### W13.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=108  W=100/L=8  WR=92.6%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W14.  `H20=H20a AND H60=H60d AND T1=T1a`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude ZS=ZS5 drops 5/15 losers (33%)
- **Final: n=101  W=91/L=10  WR=90.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade  •  AVOID when zscore +2 to +3 deep overbought

### W15.  `H20=H20a AND H60=H60d AND T4=T4a`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude ZS=ZS5 drops 5/15 losers (33%)
- **Final: n=101  W=91/L=10  WR=90.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend WITH trade  •  AVOID when zscore +2 to +3 deep overbought

### W16.  `H20=H20a AND H60=H60d AND direction_exec=long`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude ZS=ZS5 drops 5/15 losers (33%)
- **Final: n=101  W=91/L=10  WR=90.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 mildly against  •  AVOID when zscore +2 to +3 deep overbought

### W17.  `H20=H20a AND H60=H60d AND T1=T1a AND T4=T4a`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude ZS=ZS5 drops 5/15 losers (33%)
- **Final: n=101  W=91/L=10  WR=90.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when zscore +2 to +3 deep overbought

### W18.  `H20=H20a AND H60=H60d AND T1=T1a AND direction_exec=long`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude ZS=ZS5 drops 5/15 losers (33%)
- **Final: n=101  W=91/L=10  WR=90.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade  •  AVOID when zscore +2 to +3 deep overbought

### W19.  `H20=H20a AND H60=H60d AND T4=T4a AND direction_exec=long`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude ZS=ZS5 drops 5/15 losers (33%)
- **Final: n=101  W=91/L=10  WR=90.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend WITH trade  •  AVOID when zscore +2 to +3 deep overbought

### W20.  `H60=H60a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=99  W=92/L=7  WR=92.9%
- Refine: exclude H20=H20a drops 7/7 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W21.  `H20=H20e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude RSI=RSI4 drops 12/12 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when RSI 50-60 upper neutral

### W22.  `H20=H20e AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=87  W=79/L=8  WR=90.8%
- Refine: exclude ZS=ZS3 drops 7/8 losers (88%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W23.  `H20=H20e AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=85  W=82/L=3  WR=96.5%
- Refine: exclude BBP=BBP2 drops 2/3 losers (67%)
- **Final: n=83  W=82/L=1  WR=98.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when lower third

### W24.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude ZS=ZS3 drops 7/8 losers (88%)
- **Final: n=69  W=68/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W25.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude BBP=BBP6 drops 5/12 losers (42%)
- **Final: n=66  W=59/L=7  WR=89.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60b AND T1=T1c AND T4=T4c`
- Raw: n=160  W=58/L=102  WR=36.2%
- Sharpen: sharpest is session_bucket=asia (37/102 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L02.  `H60=H60b AND T1=T1c AND direction_exec=short`
- Raw: n=160  W=58/L=102  WR=36.2%
- Sharpen: sharpest is session_bucket=asia (37/102 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 1h trend AGAINST trade  •  ONLY when session=asia

### L03.  `H60=H60b AND T4=T4c AND direction_exec=short`
- Raw: n=160  W=58/L=102  WR=36.2%
- Sharpen: sharpest is session_bucket=asia (37/102 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 4h trend AGAINST trade  •  ONLY when session=asia

### L04.  `H60=H60b AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=160  W=58/L=102  WR=36.2%
- Sharpen: sharpest is session_bucket=asia (37/102 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L05.  `H60=H60e AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=152  W=60/L=92  WR=39.5%
- Sharpen: sharpest is H20=H20a (30/92 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L06.  `T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=111  W=40/L=71  WR=36.0%
- Sharpen: sharpest is BBP=BBP6 (16/71 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_close  •  ONLY when deep above upper band

### L07.  `H20=H20e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=109  W=39/L=70  WR=35.8%
- Sharpen: sharpest is BBP=BBP6 (16/70 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when deep above upper band

### L08.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=109  W=39/L=70  WR=35.8%
- Sharpen: sharpest is BBP=BBP6 (16/70 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when deep above upper band

### L09.  `H20=H20a AND T4=T4c AND RSI=RSI5`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is session_bucket=ny_mid (28/66 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L10.  `H20=H20a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is session_bucket=ny_mid (28/66 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L11.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is session_bucket=ny_mid (28/66 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L12.  `H20=H20a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is session_bucket=ny_mid (28/66 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L13.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is session_bucket=ny_mid (28/66 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L14.  `H60=H60b AND T1=T1c AND RSI=RSI5`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: sharpest is session_bucket=asia (30/66 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=asia

### L15.  `H60=H60b AND T4=T4c AND RSI=RSI5`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: sharpest is session_bucket=asia (30/66 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=asia

### L16.  `H60=H60b AND RSI=RSI5 AND direction_exec=short`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: sharpest is session_bucket=asia (30/66 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  HTF60 slightly aligned; RSI 60-70 strong  •  ONLY when session=asia

### L17.  `H60=H60b AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: sharpest is session_bucket=asia (30/66 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=asia

### L18.  `H60=H60b AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: sharpest is session_bucket=asia (30/66 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=asia

### L19.  `H60=H60b AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: sharpest is session_bucket=asia (30/66 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=asia

### L20.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=101  W=30/L=71  WR=29.7%
- Sharpen: sharpest is BBP=BBP4 (42/71 of losers there)
- **Sharp: n=52  W=10/L=42  WR=19.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when upper third

### L21.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is ZS=ZS5 (16/60 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L22.  `H20=H20a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=93  W=33/L=60  WR=35.5%
- Sharpen: sharpest is BBP=BBP6 (15/60 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when deep above upper band

### L23.  `H20=H20a AND H60=H60e AND T1=T1c`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is session_bucket=ny_mid (25/55 of losers there)
- **Sharp: n=32  W=7/L=25  WR=21.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when session=ny_mid

### L24.  `H20=H20a AND H60=H60e AND T4=T4c`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is session_bucket=ny_mid (25/55 of losers there)
- **Sharp: n=32  W=7/L=25  WR=21.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L25.  `H20=H20a AND H60=H60e AND direction_exec=short`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is session_bucket=ny_mid (25/55 of losers there)
- **Sharp: n=32  W=7/L=25  WR=21.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  ONLY when session=ny_mid

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(48/42) | H20e(43/49) |
| H60 | H60a(46/33), H60d(13/7) | H60e(34/46), H60b(6/14) |
| T1 | T1a(58/42) | T1c(42/58) |
| T4 | T4a(58/41) | T4c(42/59) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(58/42) | short(42/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
