# NZD_USD — R29 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,437**  (W=1,565 / L=872)  -  WR: **64.2%**

## Session distribution

- asia: n=518  W=341/L=177  WR=65.8%
- ny_mid: n=508  W=328/L=180  WR=64.6%
- london_open: n=422  W=274/L=148  WR=64.9%
- ny_close: n=390  W=247/L=143  WR=63.3%
- ny_open: n=362  W=232/L=130  WR=64.1%
- london: n=144  W=90/L=54  WR=62.5%
- asia_late: n=77  W=45/L=32  WR=58.4%
- off_hours: n=16  W=8/L=8  WR=50.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T1=T1a AND RSI=RSI5`
- Raw: n=163  W=151/L=12  WR=92.6%
- Refine: exclude T4=T4c drops 12/12 losers (100%)
- **Final: n=82  W=82/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when 4h trend AGAINST trade

### W02.  `H20=H20e AND T1=T1a AND ZS=ZS5`
- Raw: n=153  W=134/L=19  WR=87.6%
- Refine: exclude H60=H60e drops 12/19 losers (63%)
- **Final: n=110  W=103/L=7  WR=93.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 strongly against

### W03.  `T1=T1a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=151  W=129/L=22  WR=85.4%
- Refine: exclude H20=H20a drops 15/22 losers (68%)
- **Final: n=94  W=87/L=7  WR=92.6%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W04.  `H20=H20e AND RSI=RSI5 AND direction_exec=long`
- Raw: n=150  W=141/L=9  WR=94.0%
- Refine: exclude H60=H60e drops 9/9 losers (100%)
- **Final: n=96  W=96/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W05.  `H20=H20e AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=150  W=141/L=9  WR=94.0%
- Refine: exclude H60=H60e drops 9/9 losers (100%)
- **Final: n=96  W=96/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W06.  `H20=H20e AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=150  W=129/L=21  WR=86.0%
- Refine: exclude session_bucket=asia drops 18/21 losers (86%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=asia

### W07.  `H60=H60a AND T1=T1a AND ZS=ZS5`
- Raw: n=140  W=125/L=15  WR=89.3%
- Refine: exclude RSI=RSI4 drops 11/15 losers (73%)
- **Final: n=85  W=81/L=4  WR=95.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 50-60 upper neutral

### W08.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=137  W=117/L=20  WR=85.4%
- Refine: exclude H20=H20e drops 17/20 losers (85%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF20 strongly against

### W09.  `H60=H60a AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=131  W=115/L=16  WR=87.8%
- Refine: exclude RSI=RSI4 drops 13/16 losers (81%)
- **Final: n=103  W=100/L=3  WR=97.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W10.  `H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=129  W=111/L=18  WR=86.0%
- Refine: exclude H20=H20a drops 11/18 losers (61%)
- **Final: n=87  W=80/L=7  WR=92.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W11.  `H20=H20e AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=124  W=111/L=13  WR=89.5%
- Refine: exclude RSI=RSI4 drops 9/13 losers (69%)
- **Final: n=110  W=106/L=4  WR=96.4%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W12.  `H20=H20a AND H60=H60a AND T1=T1c AND direction_exec=long`
- Raw: n=122  W=106/L=16  WR=86.9%
- Refine: exclude session_bucket=ny_mid drops 9/16 losers (56%)
- **Final: n=107  W=100/L=7  WR=93.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=ny_mid

### W13.  `H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=115  W=110/L=5  WR=95.7%
- Refine: exclude T4=T4c drops 5/5 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when 4h trend AGAINST trade

### W14.  `H20=H20e AND ZS=ZS5 AND direction_exec=long`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude T4=T4c drops 11/12 losers (92%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: LONG**  •  HTF20 strongly against; zscore +2 to +3 deep overbought  •  AVOID when 4h trend AGAINST trade

### W15.  `H60=H60a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=111  W=100/L=11  WR=90.1%
- Refine: exclude H20=H20a drops 11/11 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W16.  `H20=H20a AND H60=H60a AND RSI=RSI3`
- Raw: n=109  W=93/L=16  WR=85.3%
- Refine: exclude T1=T1a drops 9/16 losers (56%)
- **Final: n=81  W=74/L=7  WR=91.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W17.  `T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=105  W=94/L=11  WR=89.5%
- Refine: exclude RSI=RSI3 drops 6/11 losers (55%)
- **Final: n=88  W=83/L=5  WR=94.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W18.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude session_bucket=london_open drops 6/14 losers (43%)
- **Final: n=94  W=86/L=8  WR=91.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W19.  `H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=102  W=100/L=2  WR=98.0%
- Refine: exclude session_bucket=london drops 2/2 losers (100%)
- **Final: n=98  W=98/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=london

### W20.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=102  W=100/L=2  WR=98.0%
- Refine: exclude session_bucket=london drops 2/2 losers (100%)
- **Final: n=98  W=98/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london

### W21.  `H20=H20e AND T1=T1a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=101  W=95/L=6  WR=94.1%
- Refine: exclude T4=T4c drops 6/6 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when 4h trend AGAINST trade

### W22.  `H20=H20e AND H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=99  W=96/L=3  WR=97.0%
- Refine: exclude direction_exec=short drops 3/3 losers (100%)
- **Final: n=86  W=86/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when short

### W23.  `H20=H20e AND H60=H60a AND T1=T1a AND ZS=ZS5`
- Raw: n=99  W=93/L=6  WR=93.9%
- Refine: exclude direction_exec=short drops 6/6 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when short

### W24.  `H20=H20e AND T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=99  W=93/L=6  WR=93.9%
- Refine: exclude T4=T4c drops 5/6 losers (83%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when 4h trend AGAINST trade

### W25.  `H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=99  W=88/L=11  WR=88.9%
- Refine: exclude BBP=BBP6 drops 9/11 losers (82%)
- **Final: n=66  W=64/L=2  WR=97.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when deep above upper band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=146  W=55/L=91  WR=37.7%
- Sharpen: sharpest is ZS=ZS1 (29/91 of losers there)
- **Sharp: n=36  W=7/L=29  WR=19.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L02.  `H20=H20a AND T1=T1c AND RSI=RSI5`
- Raw: n=123  W=35/L=88  WR=28.5%
- Sharpen: sharpest is session_bucket=ny_close (26/88 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_close

### L03.  `H20=H20a AND T1=T1c AND ZS=ZS5`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is BBP=BBP5 (40/73 of losers there)
- **Sharp: n=52  W=12/L=40  WR=23.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when just touched upper band

### L04.  `H20=H20a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=111  W=29/L=82  WR=26.1%
- Sharpen: sharpest is session_bucket=ny_close (26/82 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=ny_close

### L05.  `H20=H20a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=111  W=29/L=82  WR=26.1%
- Sharpen: sharpest is session_bucket=ny_close (26/82 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_close

### L06.  `H60=H60e AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=95  W=31/L=64  WR=32.6%
- Sharpen: sharpest is session_bucket=ny_mid (13/64 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L07.  `H20=H20a AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=95  W=32/L=63  WR=33.7%
- Sharpen: sharpest is RSI=RSI5 (43/63 of losers there)
- **Sharp: n=53  W=10/L=43  WR=18.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L08.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=91  W=29/L=62  WR=31.9%
- Sharpen: sharpest is session_bucket=ny_mid (13/62 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L09.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=91  W=34/L=57  WR=37.4%
- Sharpen: sharpest is direction_exec=short (28/57 of losers there)
- **Sharp: n=35  W=7/L=28  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong  •  ONLY when short

### L10.  `H60=H60e AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=89  W=34/L=55  WR=38.2%
- Sharpen: sharpest is direction_exec=short (28/55 of losers there)
- **Sharp: n=35  W=7/L=28  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when short

### L11.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=89  W=34/L=55  WR=38.2%
- Sharpen: sharpest is direction_exec=short (28/55 of losers there)
- **Sharp: n=35  W=7/L=28  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when short

### L12.  `H60=H60e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=88  W=28/L=60  WR=31.8%
- Sharpen: sharpest is H20=H20a (26/60 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L13.  `T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=88  W=33/L=55  WR=37.5%
- Sharpen: sharpest is session_bucket=ny_open (11/55 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=ny_open

### L14.  `H20=H20a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is RSI=RSI5 (47/53 of losers there)
- **Sharp: n=63  W=16/L=47  WR=25.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L15.  `H20=H20a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=84  W=32/L=52  WR=38.1%
- Sharpen: sharpest is direction_exec=short (27/52 of losers there)
- **Sharp: n=38  W=11/L=27  WR=28.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 60-70 strong  •  ONLY when short

### L16.  `H20=H20a AND T4=T4c AND RSI=RSI5`
- Raw: n=80  W=28/L=52  WR=35.0%
- Sharpen: sharpest is T1=T1c (43/52 of losers there)
- **Sharp: n=53  W=10/L=43  WR=18.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when 1h trend AGAINST trade

### L17.  `H20=H20a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=80  W=28/L=52  WR=35.0%
- Sharpen: sharpest is direction_exec=short (27/52 of losers there)
- **Sharp: n=34  W=7/L=27  WR=20.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when short

### L18.  `H20=H20a AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=80  W=28/L=52  WR=35.0%
- Sharpen: sharpest is direction_exec=short (27/52 of losers there)
- **Sharp: n=34  W=7/L=27  WR=20.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when short

### L19.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=79  W=23/L=56  WR=29.1%
- Sharpen: sharpest is session_bucket=ny_mid (13/56 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong  •  ONLY when session=ny_mid

### L20.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=79  W=23/L=56  WR=29.1%
- Sharpen: sharpest is session_bucket=ny_mid (13/56 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L21.  `H20=H20a AND H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=78  W=25/L=53  WR=32.1%
- Sharpen: sharpest is session_bucket=ny_mid (13/53 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L22.  `T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=76  W=27/L=49  WR=35.5%
- Sharpen: sharpest is session_bucket=ny_open (11/49 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=ny_open

### L23.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=76  W=27/L=49  WR=35.5%
- Sharpen: sharpest is session_bucket=ny_open (11/49 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=ny_open

### L24.  `H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=73  W=29/L=44  WR=39.7%
- Sharpen: sharpest is BBP=BBP1 (10/44 of losers there)
- **Sharp: n=11  W=1/L=10  WR=9.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when just touched lower band

### L25.  `H60=H60e AND ZS=ZS1 AND direction_exec=short`
- Raw: n=73  W=29/L=44  WR=39.7%
- Sharpen: sharpest is T4=T4c (29/44 of losers there)
- **Sharp: n=36  W=7/L=29  WR=19.4%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(46/38) | H20a(39/49) |
| H60 | H60a(51/37) | H60e(36/51) |
| T1 | T1a(52/44) | T1c(47/56) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
