# NZD_CHF — R22 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,861**  (W=1,262 / L=599)  -  WR: **67.8%**

## Session distribution

- asia: n=428  W=287/L=141  WR=67.1%
- london_open: n=391  W=264/L=127  WR=67.5%
- ny_close: n=269  W=188/L=81  WR=69.9%
- london: n=259  W=164/L=95  WR=63.3%
- ny_open: n=203  W=142/L=61  WR=70.0%
- ny_mid: n=171  W=121/L=50  WR=70.8%
- asia_late: n=108  W=73/L=35  WR=67.6%
- off_hours: n=32  W=23/L=9  WR=71.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND direction_exec=long`
- Raw: n=312  W=273/L=39  WR=87.5%
- Refine: exclude session_bucket=ny_mid drops 11/39 losers (28%)
- **Final: n=281  W=253/L=28  WR=90.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=ny_mid

### W02.  `H20=H20a AND T1=T1a AND T4=T4a`
- Raw: n=271  W=250/L=21  WR=92.3%
- Refine: exclude ZS=ZS4 drops 13/21 losers (62%)
- **Final: n=190  W=182/L=8  WR=95.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when zscore +1 to +2 overbought

### W03.  `H20=H20a AND T1=T1a AND RSI=RSI5`
- Raw: n=234  W=205/L=29  WR=87.6%
- Refine: exclude T4=T4c drops 17/29 losers (59%)
- **Final: n=166  W=154/L=12  WR=92.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when 4h trend AGAINST trade

### W04.  `H20=H20a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=234  W=205/L=29  WR=87.6%
- Refine: exclude T4=T4c drops 17/29 losers (59%)
- **Final: n=166  W=154/L=12  WR=92.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  AVOID when 4h trend AGAINST trade

### W05.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=234  W=205/L=29  WR=87.6%
- Refine: exclude T4=T4c drops 17/29 losers (59%)
- **Final: n=166  W=154/L=12  WR=92.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when 4h trend AGAINST trade

### W06.  `H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=221  W=188/L=33  WR=85.1%
- Refine: exclude session_bucket=ny_close drops 15/33 losers (45%)
- **Final: n=189  W=171/L=18  WR=90.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_close

### W07.  `H20=H20a AND H60=H60a AND T1=T1a`
- Raw: n=214  W=197/L=17  WR=92.1%
- Refine: exclude RSI=RSI5 drops 16/17 losers (94%)
- **Final: n=103  W=102/L=1  WR=99.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when RSI 60-70 strong

### W08.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=197  W=176/L=21  WR=89.3%
- Refine: exclude session_bucket=ny_mid drops 6/21 losers (29%)
- **Final: n=189  W=174/L=15  WR=92.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W09.  `T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=185  W=164/L=21  WR=88.6%
- Refine: exclude H20=H20d drops 15/21 losers (71%)
- **Final: n=156  W=150/L=6  WR=96.2%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak  •  AVOID when HTF20 mildly against

### W10.  `T1=T1a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=182  W=156/L=26  WR=85.7%
- Refine: exclude H60=H60b drops 5/26 losers (19%)
- **Final: n=177  W=156/L=21  WR=88.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF60 slightly aligned

### W11.  `RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=182  W=156/L=26  WR=85.7%
- Refine: exclude H60=H60b drops 5/26 losers (19%)
- **Final: n=177  W=156/L=21  WR=88.1%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF60 slightly aligned

### W12.  `T1=T1a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=182  W=156/L=26  WR=85.7%
- Refine: exclude H60=H60b drops 5/26 losers (19%)
- **Final: n=177  W=156/L=21  WR=88.1%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF60 slightly aligned

### W13.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=166  W=154/L=12  WR=92.8%
- Refine: exclude session_bucket=ny_mid drops 4/12 losers (33%)
- **Final: n=162  W=154/L=8  WR=95.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W14.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=166  W=154/L=12  WR=92.8%
- Refine: exclude session_bucket=ny_mid drops 4/12 losers (33%)
- **Final: n=162  W=154/L=8  WR=95.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W15.  `T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=164  W=146/L=18  WR=89.0%
- Refine: exclude RSI=RSI4 drops 13/18 losers (72%)
- **Final: n=118  W=113/L=5  WR=95.8%**
- **Dir: LONG**  •  1h trend WITH trade; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W16.  `H20=H20a AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=162  W=145/L=17  WR=89.5%
- Refine: exclude session_bucket=london drops 10/17 losers (59%)
- **Final: n=125  W=118/L=7  WR=94.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=london

### W17.  `H60=H60a AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=160  W=136/L=24  WR=85.0%
- Refine: exclude H20=H20c drops 5/24 losers (21%)
- **Final: n=154  W=135/L=19  WR=87.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when HTF20 neutral

### W18.  `H20=H20a AND T1=T1a AND BBP=BBP4`
- Raw: n=152  W=130/L=22  WR=85.5%
- Refine: exclude H60=H60d drops 6/22 losers (27%)
- **Final: n=140  W=124/L=16  WR=88.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when HTF60 mildly against

### W19.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude H20=H20e drops 12/21 losers (57%)
- **Final: n=94  W=85/L=9  WR=90.4%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W20.  `H20=H20a AND T4=T4a AND session_bucket=asia`
- Raw: n=134  W=121/L=13  WR=90.3%
- Refine: exclude RSI=RSI2 drops 5/13 losers (38%)
- **Final: n=127  W=119/L=8  WR=93.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 30-40 weak

### W21.  `H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=134  W=118/L=16  WR=88.1%
- Refine: exclude ZS=ZS4 drops 13/16 losers (81%)
- **Final: n=98  W=95/L=3  WR=96.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when zscore +1 to +2 overbought

### W22.  `T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=132  W=113/L=19  WR=85.6%
- Refine: exclude H20=H20e drops 11/19 losers (58%)
- **Final: n=85  W=77/L=8  WR=90.6%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W23.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=132  W=113/L=19  WR=85.6%
- Refine: exclude H20=H20e drops 11/19 losers (58%)
- **Final: n=85  W=77/L=8  WR=90.6%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W24.  `H20=H20a AND T4=T4a AND ZS=ZS5`
- Raw: n=129  W=110/L=19  WR=85.3%
- Refine: exclude T1=T1c drops 14/19 losers (74%)
- **Final: n=85  W=80/L=5  WR=94.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when 1h trend AGAINST trade

### W25.  `H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude H20=H20b drops 9/9 losers (100%)
- **Final: n=100  W=100/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when HTF20 slightly aligned

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND T1=T1c`
- Raw: n=175  W=68/L=107  WR=38.9%
- Sharpen: sharpest is session_bucket=london_open (35/107 of losers there)
- **Sharp: n=38  W=3/L=35  WR=7.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when session=london_open

### L02.  `T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=126  W=48/L=78  WR=38.1%
- Sharpen: sharpest is H20=H20e (32/78 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london_open  •  ONLY when HTF20 strongly against

### L03.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=121  W=38/L=83  WR=31.4%
- Sharpen: sharpest is H20=H20e (39/83 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L04.  `H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=109  W=38/L=71  WR=34.9%
- Sharpen: sharpest is H20=H20e (35/71 of losers there)
- **Sharp: n=38  W=3/L=35  WR=7.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when HTF20 strongly against

### L05.  `T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=96  W=37/L=59  WR=38.5%
- Sharpen: sharpest is T1=T1a (23/59 of losers there)
- **Sharp: n=30  W=7/L=23  WR=23.3%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L06.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=96  W=37/L=59  WR=38.5%
- Sharpen: sharpest is T1=T1a (23/59 of losers there)
- **Sharp: n=30  W=7/L=23  WR=23.3%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L07.  `T1=T1c AND T4=T4a AND session_bucket=london_open`
- Raw: n=90  W=24/L=66  WR=26.7%
- Sharpen: sharpest is H20=H20e (18/66 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when HTF20 strongly against

### L08.  `H20=H20e AND T4=T4c AND session_bucket=asia`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is RSI=RSI3 (8/53 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L09.  `H20=H20e AND H60=H60e AND RSI=RSI4`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is T1=T1c (33/51 of losers there)
- **Sharp: n=44  W=11/L=33  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L10.  `H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is H20=H20e (23/51 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london_open  •  ONLY when HTF20 strongly against

### L11.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is H20=H20e (23/51 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when HTF20 strongly against

### L12.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=76  W=19/L=57  WR=25.0%
- Sharpen: sharpest is BBP=BBP5 (12/57 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when just touched upper band

### L13.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=73  W=25/L=48  WR=34.2%
- Sharpen: sharpest is H60=H60a (18/48 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L14.  `T4=T4c AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=73  W=25/L=48  WR=34.2%
- Sharpen: sharpest is H60=H60a (18/48 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L15.  `H60=H60e AND T1=T1c AND T4=T4a AND BBP=BBP4`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is session_bucket=london_open (16/44 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; upper third  •  ONLY when session=london_open

### L16.  `T1=T1c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=71  W=15/L=56  WR=21.1%
- Sharpen: sharpest is T4=T4c (26/56 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when 4h trend AGAINST trade

### L17.  `RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=71  W=15/L=56  WR=21.1%
- Sharpen: sharpest is T4=T4c (26/56 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=london_open  •  ONLY when 4h trend AGAINST trade

### L18.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=71  W=15/L=56  WR=21.1%
- Sharpen: sharpest is T4=T4c (26/56 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when 4h trend AGAINST trade

### L19.  `H20=H20a AND H60=H60e AND T1=T1c`
- Raw: n=69  W=23/L=46  WR=33.3%
- Sharpen: sharpest is BBP=BBP4 (16/46 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when upper third

### L20.  `H60=H60e AND T1=T1c AND session_bucket=london`
- Raw: n=68  W=24/L=44  WR=35.3%
- Sharpen: sharpest is H20=H20a (13/44 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london  •  ONLY when HTF20 aligned WITH trade

### L21.  `T1=T1c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is H20=H20e (16/41 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third  •  ONLY when HTF20 strongly against

### L22.  `H20=H20e AND T1=T1c AND session_bucket=asia`
- Raw: n=67  W=24/L=43  WR=35.8%
- Sharpen: sharpest is H60=H60a (30/43 of losers there)
- **Sharp: n=35  W=5/L=30  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L23.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=67  W=24/L=43  WR=35.8%
- Sharpen: sharpest is H60=H60a (30/43 of losers there)
- **Sharp: n=35  W=5/L=30  WR=14.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L24.  `T1=T1c AND T4=T4a AND RSI=RSI2`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is session_bucket=london_open (13/41 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when session=london_open

### L25.  `T4=T4a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is session_bucket=london_open (13/41 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 30-40 weak  •  ONLY when session=london_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(39/23) | H20e(27/40), H20d(13/19) |
| H60 | H60a(41/25) | H60e(27/40), H60b(8/14) |
| T1 | T1a(59/35) | T1c(41/65) |
| T4 | T4c(52/47) | T4a(48/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
