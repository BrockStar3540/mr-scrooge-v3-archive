# AUD_CHF — R28 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,184**  (W=780 / L=404)  -  WR: **65.9%**

## Session distribution

- asia: n=388  W=268/L=120  WR=69.1%
- ny_close: n=262  W=175/L=87  WR=66.8%
- ny_mid: n=144  W=85/L=59  WR=59.0%
- london: n=125  W=81/L=44  WR=64.8%
- london_open: n=120  W=75/L=45  WR=62.5%
- ny_open: n=97  W=63/L=34  WR=64.9%
- asia_late: n=24  W=16/L=8  WR=66.7%
- off_hours: n=24  W=17/L=7  WR=70.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=258  W=223/L=35  WR=86.4%
- Refine: exclude RSI=RSI6 drops 24/35 losers (69%)
- **Final: n=126  W=115/L=11  WR=91.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third  •  AVOID when RSI 70-80 overbought

### W02.  `H20=H20a AND T1=T1a AND BBP=BBP4`
- Raw: n=250  W=215/L=35  WR=86.0%
- Refine: exclude session_bucket=asia_late drops 7/35 losers (20%)
- **Final: n=243  W=215/L=28  WR=88.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when session=asia_late

### W03.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=250  W=215/L=35  WR=86.0%
- Refine: exclude session_bucket=asia_late drops 7/35 losers (20%)
- **Final: n=243  W=215/L=28  WR=88.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when session=asia_late

### W04.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=243  W=213/L=30  WR=87.7%
- Refine: exclude session_bucket=asia_late drops 7/30 losers (23%)
- **Final: n=236  W=213/L=23  WR=90.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=asia_late

### W05.  `H20=H20a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=243  W=213/L=30  WR=87.7%
- Refine: exclude session_bucket=asia_late drops 7/30 losers (23%)
- **Final: n=236  W=213/L=23  WR=90.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when session=asia_late

### W06.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=243  W=213/L=30  WR=87.7%
- Refine: exclude session_bucket=asia_late drops 7/30 losers (23%)
- **Final: n=236  W=213/L=23  WR=90.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=asia_late

### W07.  `H20=H20a AND T1=T1a AND ZS=ZS4`
- Raw: n=235  W=205/L=30  WR=87.2%
- Refine: exclude session_bucket=asia_late drops 7/30 losers (23%)
- **Final: n=228  W=205/L=23  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=asia_late

### W08.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=235  W=205/L=30  WR=87.2%
- Refine: exclude session_bucket=asia_late drops 7/30 losers (23%)
- **Final: n=228  W=205/L=23  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=asia_late

### W09.  `H20=H20a AND T1=T1a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=235  W=205/L=30  WR=87.2%
- Refine: exclude session_bucket=asia_late drops 7/30 losers (23%)
- **Final: n=228  W=205/L=23  WR=89.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=asia_late

### W10.  `T4=T4a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=235  W=204/L=31  WR=86.8%
- Refine: exclude RSI=RSI5 drops 16/31 losers (52%)
- **Final: n=161  W=146/L=15  WR=90.7%**
- **Dir: LONG**  •  4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 60-70 strong

### W11.  `T4=T4a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=235  W=204/L=31  WR=86.8%
- Refine: exclude RSI=RSI5 drops 16/31 losers (52%)
- **Final: n=161  W=146/L=15  WR=90.7%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 60-70 strong

### W12.  `H20=H20a AND H60=H60a AND BBP=BBP4`
- Raw: n=233  W=201/L=32  WR=86.3%
- Refine: exclude RSI=RSI6 drops 24/32 losers (75%)
- **Final: n=111  W=103/L=8  WR=92.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third  •  AVOID when RSI 70-80 overbought

### W13.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=233  W=201/L=32  WR=86.3%
- Refine: exclude RSI=RSI6 drops 24/32 losers (75%)
- **Final: n=111  W=103/L=8  WR=92.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third  •  AVOID when RSI 70-80 overbought

### W14.  `T1=T1a AND T4=T4a AND ZS=ZS4`
- Raw: n=227  W=196/L=31  WR=86.3%
- Refine: exclude session_bucket=asia drops 17/31 losers (55%)
- **Final: n=153  W=139/L=14  WR=90.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=asia

### W15.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=227  W=196/L=31  WR=86.3%
- Refine: exclude session_bucket=asia drops 17/31 losers (55%)
- **Final: n=153  W=139/L=14  WR=90.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=asia

### W16.  `T1=T1a AND T4=T4a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=227  W=196/L=31  WR=86.3%
- Refine: exclude session_bucket=asia drops 17/31 losers (55%)
- **Final: n=153  W=139/L=14  WR=90.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=asia

### W17.  `H20=H20a AND H60=H60a AND T1=T1a AND BBP=BBP4`
- Raw: n=225  W=193/L=32  WR=85.8%
- Refine: exclude RSI=RSI6 drops 24/32 losers (75%)
- **Final: n=103  W=95/L=8  WR=92.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when RSI 70-80 overbought

### W18.  `H20=H20a AND H60=H60a AND ZS=ZS4`
- Raw: n=222  W=194/L=28  WR=87.4%
- Refine: exclude RSI=RSI6 drops 21/28 losers (75%)
- **Final: n=106  W=99/L=7  WR=93.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 70-80 overbought

### W19.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=222  W=194/L=28  WR=87.4%
- Refine: exclude RSI=RSI6 drops 21/28 losers (75%)
- **Final: n=106  W=99/L=7  WR=93.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 70-80 overbought

### W20.  `H20=H20a AND H60=H60a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=222  W=194/L=28  WR=87.4%
- Refine: exclude RSI=RSI6 drops 21/28 losers (75%)
- **Final: n=106  W=99/L=7  WR=93.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 70-80 overbought

### W21.  `H20=H20a AND T4=T4a AND BBP=BBP4`
- Raw: n=220  W=192/L=28  WR=87.3%
- Refine: exclude session_bucket=asia_late drops 7/28 losers (25%)
- **Final: n=213  W=192/L=21  WR=90.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; upper third  •  AVOID when session=asia_late

### W22.  `H20=H20a AND T4=T4a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=220  W=192/L=28  WR=87.3%
- Refine: exclude session_bucket=asia_late drops 7/28 losers (25%)
- **Final: n=213  W=192/L=21  WR=90.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; upper third  •  AVOID when session=asia_late

### W23.  `H20=H20a AND H60=H60a AND T1=T1a AND ZS=ZS4`
- Raw: n=214  W=186/L=28  WR=86.9%
- Refine: exclude session_bucket=asia_late drops 7/28 losers (25%)
- **Final: n=207  W=186/L=21  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=asia_late

### W24.  `H60=H60a AND T4=T4a AND ZS=ZS4`
- Raw: n=214  W=185/L=29  WR=86.4%
- Refine: exclude session_bucket=asia_late drops 7/29 losers (24%)
- **Final: n=207  W=185/L=22  WR=89.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=asia_late

### W25.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=214  W=185/L=29  WR=86.4%
- Refine: exclude session_bucket=asia_late drops 7/29 losers (24%)
- **Final: n=207  W=185/L=22  WR=89.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=asia_late

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND ZS=ZS4`
- Raw: n=184  W=73/L=111  WR=39.7%
- Sharpen: sharpest is session_bucket=ny_mid (29/111 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L02.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=184  W=73/L=111  WR=39.7%
- Sharpen: sharpest is session_bucket=ny_mid (29/111 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L03.  `H20=H20e AND H60=H60e AND ZS=ZS4 AND direction_exec=short`
- Raw: n=184  W=73/L=111  WR=39.7%
- Sharpen: sharpest is session_bucket=ny_mid (29/111 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L04.  `T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=65  W=22/L=43  WR=33.8%
- Sharpen: sharpest is H20=H20e (43/43 of losers there)
- **Sharp: n=47  W=4/L=43  WR=8.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 strongly against

### L05.  `H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is H20=H20e (42/42 of losers there)
- **Sharp: n=46  W=4/L=42  WR=8.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 strongly against

### L06.  `H60=H60e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is H20=H20e (42/42 of losers there)
- **Sharp: n=46  W=4/L=42  WR=8.7%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_mid  •  ONLY when HTF20 strongly against

### L07.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is H20=H20e (42/42 of losers there)
- **Sharp: n=46  W=4/L=42  WR=8.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 strongly against

### L08.  `H20=H20b AND T4=T4a AND RSI=RSI5`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_mid (7/36 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L09.  `H20=H20b AND RSI=RSI5 AND direction_exec=long`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_mid (7/36 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 60-70 strong  •  ONLY when session=ny_mid

### L10.  `H20=H20b AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_mid (7/36 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L11.  `H20=H20b AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_mid (7/36 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L12.  `H20=H20b AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_mid (7/36 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L13.  `T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=55  W=20/L=35  WR=36.4%
- Sharpen: sharpest is H20=H20e (35/35 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 strongly against

### L14.  `T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=55  W=20/L=35  WR=36.4%
- Sharpen: sharpest is H20=H20e (35/35 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 strongly against

### L15.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=55  W=20/L=35  WR=36.4%
- Sharpen: sharpest is H20=H20e (35/35 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 strongly against

### L16.  `H60=H60e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=54  W=20/L=34  WR=37.0%
- Sharpen: sharpest is H20=H20e (34/34 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 strongly against

### L17.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=54  W=20/L=34  WR=37.0%
- Sharpen: sharpest is H20=H20e (34/34 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 strongly against

### L18.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=54  W=20/L=34  WR=37.0%
- Sharpen: sharpest is H20=H20e (34/34 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 strongly against

### L19.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=50  W=20/L=30  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (21/30 of losers there)
- **Sharp: n=31  W=10/L=21  WR=32.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; RSI 60-70 strong  •  ONLY when session=asia

### L20.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is T1=T1a (5/30 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L21.  `H20=H20e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=47  W=4/L=43  WR=8.5%
- Sharpen: sharpest is T4=T4c (35/43 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L22.  `H20=H20e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=47  W=4/L=43  WR=8.5%
- Sharpen: sharpest is T4=T4c (35/43 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L23.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=47  W=4/L=43  WR=8.5%
- Sharpen: sharpest is T4=T4c (35/43 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L24.  `H20=H20e AND H60=H60e AND T4=T4a`
- Raw: n=47  W=10/L=37  WR=21.3%
- Sharpen: sharpest is ZS=ZS5 (11/37 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `H20=H20e AND T4=T4a AND direction_exec=short`
- Raw: n=47  W=10/L=37  WR=21.3%
- Sharpen: sharpest is ZS=ZS5 (11/37 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(51/24), H20d(13/7) | H20e(28/55) |
| H60 | H60a(52/33) | H60e(37/54) |
| T1 | T1a(56/41) | T1c(44/59) |
| T4 | T4a(55/42) | T4c(45/58) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(58/39) | short(42/61) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
