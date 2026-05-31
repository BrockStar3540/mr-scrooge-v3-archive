# GBP_CHF — R29 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,389**  (W=1,579 / L=810)  -  WR: **66.1%**

## Session distribution

- london_open: n=654  W=432/L=222  WR=66.1%
- asia: n=379  W=238/L=141  WR=62.8%
- london: n=324  W=216/L=108  WR=66.7%
- ny_close: n=317  W=216/L=101  WR=68.1%
- ny_open: n=293  W=198/L=95  WR=67.6%
- ny_mid: n=258  W=175/L=83  WR=67.8%
- asia_late: n=103  W=67/L=36  WR=65.0%
- off_hours: n=61  W=37/L=24  WR=60.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=248  W=212/L=36  WR=85.5%
- Refine: exclude H60=H60c drops 13/36 losers (36%)
- **Final: n=209  W=186/L=23  WR=89.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF60 neutral

### W02.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=199  W=171/L=28  WR=85.9%
- Refine: exclude H60=H60c drops 13/28 losers (46%)
- **Final: n=160  W=145/L=15  WR=90.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF60 neutral

### W03.  `H20=H20a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=158  W=138/L=20  WR=87.3%
- Refine: exclude T4=T4a drops 19/20 losers (95%)
- **Final: n=103  W=102/L=1  WR=99.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london_open  •  AVOID when 4h trend WITH trade

### W04.  `H20=H20a AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=154  W=132/L=22  WR=85.7%
- Refine: exclude BBP=BBP0 drops 11/22 losers (50%)
- **Final: n=136  W=125/L=11  WR=91.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when deep below lower band

### W05.  `T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=136  W=118/L=18  WR=86.8%
- Refine: exclude H60=H60a drops 12/18 losers (67%)
- **Final: n=84  W=78/L=6  WR=92.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W06.  `H60=H60e AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=133  W=115/L=18  WR=86.5%
- Refine: exclude H20=H20a drops 14/18 losers (78%)
- **Final: n=91  W=87/L=4  WR=95.6%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when HTF20 aligned WITH trade

### W07.  `T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=127  W=113/L=14  WR=89.0%
- Refine: exclude T4=T4a drops 12/14 losers (86%)
- **Final: n=71  W=69/L=2  WR=97.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_close  •  AVOID when 4h trend WITH trade

### W08.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=125  W=109/L=16  WR=87.2%
- Refine: exclude session_bucket=london_open drops 13/16 losers (81%)
- **Final: n=96  W=93/L=3  WR=96.9%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W09.  `H20=H20e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude H60=H60a drops 9/18 losers (50%)
- **Final: n=102  W=93/L=9  WR=91.2%**
- **Dir: LONG**  •  HTF20 strongly against; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W10.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=121  W=105/L=16  WR=86.8%
- Refine: exclude H20=H20b drops 7/16 losers (44%)
- **Final: n=102  W=93/L=9  WR=91.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF20 slightly aligned

### W11.  `T1=T1a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=120  W=110/L=10  WR=91.7%
- Refine: exclude H20=H20d drops 4/10 losers (40%)
- **Final: n=108  W=102/L=6  WR=94.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when HTF20 mildly against

### W12.  `RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=120  W=110/L=10  WR=91.7%
- Refine: exclude H20=H20d drops 4/10 losers (40%)
- **Final: n=108  W=102/L=6  WR=94.4%**
- **Dir: LONG**  •  RSI 60-70 strong; session=london_open  •  AVOID when HTF20 mildly against

### W13.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=120  W=110/L=10  WR=91.7%
- Refine: exclude H20=H20d drops 4/10 losers (40%)
- **Final: n=108  W=102/L=6  WR=94.4%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when HTF20 mildly against

### W14.  `T1=T1c AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=115  W=102/L=13  WR=88.7%
- Refine: exclude H20=H20b drops 4/13 losers (31%)
- **Final: n=107  W=98/L=9  WR=91.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF20 slightly aligned

### W15.  `H20=H20a AND T1=T1a AND RSI=RSI5`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude session_bucket=london drops 9/13 losers (69%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london

### W16.  `H20=H20a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude session_bucket=london drops 9/13 losers (69%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=london

### W17.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude session_bucket=london drops 9/13 losers (69%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london

### W18.  `H20=H20a AND T1=T1a AND T4=T4c AND session_bucket=london_open`
- Raw: n=110  W=99/L=11  WR=90.0%
- Refine: exclude RSI=RSI2 drops 10/11 losers (91%)
- **Final: n=91  W=90/L=1  WR=98.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when RSI 30-40 weak

### W19.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude session_bucket=asia_late drops 7/15 losers (47%)
- **Final: n=99  W=91/L=8  WR=91.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia_late

### W20.  `H20=H20a AND H60=H60e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude T4=T4a drops 14/15 losers (93%)
- **Final: n=69  W=68/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=london_open  •  AVOID when 4h trend WITH trade

### W21.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=103  W=102/L=1  WR=99.0%
- Refine: no further refinement
- **Final: n=103  W=102/L=1  WR=99.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=london_open

### W22.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=101  W=94/L=7  WR=93.1%
- Refine: exclude T4=T4a drops 6/7 losers (86%)
- **Final: n=89  W=88/L=1  WR=98.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when 4h trend WITH trade

### W23.  `H20=H20a AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude session_bucket=london_open drops 7/12 losers (58%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W24.  `RSI=RSI4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude T4=T4a drops 12/14 losers (86%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=ny_close  •  AVOID when 4h trend WITH trade

### W25.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude T4=T4a drops 12/14 losers (86%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=203  W=81/L=122  WR=39.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=203  W=81/L=122  WR=39.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral

### L02.  `H20=H20e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=135  W=51/L=84  WR=37.8%
- Sharpen: sharpest is T4=T4a (52/84 of losers there)
- **Sharp: n=63  W=11/L=52  WR=17.5%**
- **Dir: SHORT**  •  HTF20 strongly against; session=london_open  •  ONLY when 4h trend WITH trade

### L03.  `H60=H60a AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=104  W=41/L=63  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_open (13/63 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=ny_open

### L04.  `H20=H20e AND T1=T1c AND T4=T4a AND session_bucket=london_open`
- Raw: n=90  W=33/L=57  WR=36.7%
- Sharpen: sharpest is RSI=RSI5 (32/57 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when RSI 60-70 strong

### L05.  `T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is T4=T4a (37/54 of losers there)
- **Sharp: n=42  W=5/L=37  WR=11.9%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_close  •  ONLY when 4h trend WITH trade

### L06.  `H20=H20e AND T1=T1c AND RSI=RSI5`
- Raw: n=87  W=30/L=57  WR=34.5%
- Sharpen: sharpest is session_bucket=london_open (32/57 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london_open

### L07.  `H20=H20e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=87  W=30/L=57  WR=34.5%
- Sharpen: sharpest is session_bucket=london_open (32/57 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong  •  ONLY when session=london_open

### L08.  `T1=T1c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=87  W=30/L=57  WR=34.5%
- Sharpen: sharpest is H20=H20e (32/57 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when HTF20 strongly against

### L09.  `RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=87  W=30/L=57  WR=34.5%
- Sharpen: sharpest is H20=H20e (32/57 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=london_open  •  ONLY when HTF20 strongly against

### L10.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=87  W=30/L=57  WR=34.5%
- Sharpen: sharpest is session_bucket=london_open (32/57 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london_open

### L11.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=87  W=30/L=57  WR=34.5%
- Sharpen: sharpest is H20=H20e (32/57 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when HTF20 strongly against

### L12.  `H20=H20e AND H60=H60a AND direction_exec=long`
- Raw: n=85  W=32/L=53  WR=37.6%
- Sharpen: sharpest is T1=T1a (35/53 of losers there)
- **Sharp: n=47  W=12/L=35  WR=25.5%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade  •  ONLY when 1h trend WITH trade

### L13.  `T1=T1a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=83  W=23/L=60  WR=27.7%
- Sharpen: sharpest is H60=H60a (25/60 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L14.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is T4=T4a (49/52 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when 4h trend WITH trade

### L15.  `T1=T1a AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=73  W=29/L=44  WR=39.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=73  W=29/L=44  WR=39.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral

### L16.  `T1=T1a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=68  W=21/L=47  WR=30.9%
- Sharpen: sharpest is H60=H60a (20/47 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L17.  `H20=H20e AND H60=H60a AND T1=T1c AND session_bucket=london_open`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is RSI=RSI5 (20/41 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 60-70 strong

### L18.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=67  W=21/L=46  WR=31.3%
- Sharpen: sharpest is T4=T4c (24/46 of losers there)
- **Sharp: n=29  W=5/L=24  WR=17.2%**
- **Dir: SHORT**  •  deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L19.  `H20=H20c AND T1=T1a AND direction_exec=short`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is BBP=BBP0 (10/41 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade  •  ONLY when deep below lower band

### L20.  `H20=H20e AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=66  W=18/L=48  WR=27.3%
- Sharpen: sharpest is session_bucket=london_open (32/48 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london_open

### L21.  `H20=H20e AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=66  W=18/L=48  WR=27.3%
- Sharpen: sharpest is session_bucket=london_open (32/48 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london_open

### L22.  `H20=H20e AND T1=T1a AND ZS=ZS5`
- Raw: n=64  W=21/L=43  WR=32.8%
- Sharpen: sharpest is session_bucket=asia (14/43 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L23.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is H20=H20e (32/40 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong; session=london_open  •  ONLY when HTF20 strongly against

### L24.  `T4=T4a AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is H20=H20e (32/40 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong; session=london_open  •  ONLY when HTF20 strongly against

### L25.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=63  W=11/L=52  WR=17.5%
- Sharpen: sharpest is RSI=RSI5 (32/52 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=london_open  •  ONLY when RSI 60-70 strong

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(38/29) | H20e(32/40) |
| H60 | — | — |
| T1 | T1c(56/44) | T1a(43/55) |
| T4 | T4a(51/46) | T4c(49/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
