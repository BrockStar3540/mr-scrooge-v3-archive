# AUD_USD — R22 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,948**  (W=1,905 / L=1,043)  -  WR: **64.6%**

## Session distribution

- asia: n=809  W=528/L=281  WR=65.3%
- ny_close: n=718  W=465/L=253  WR=64.8%
- ny_mid: n=470  W=305/L=165  WR=64.9%
- ny_open: n=302  W=181/L=121  WR=59.9%
- london_open: n=247  W=164/L=83  WR=66.4%
- asia_late: n=209  W=133/L=76  WR=63.6%
- london: n=142  W=98/L=44  WR=69.0%
- off_hours: n=51  W=31/L=20  WR=60.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=140  W=121/L=19  WR=86.4%
- Refine: exclude T4=T4a drops 17/19 losers (89%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when 4h trend WITH trade

### W02.  `H60=H60a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=140  W=121/L=19  WR=86.4%
- Refine: exclude T4=T4a drops 17/19 losers (89%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_open  •  AVOID when 4h trend WITH trade

### W03.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=140  W=121/L=19  WR=86.4%
- Refine: exclude T4=T4a drops 17/19 losers (89%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when 4h trend WITH trade

### W04.  `H20=H20e AND T1=T1a AND RSI=RSI5`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude session_bucket=ny_mid drops 7/17 losers (41%)
- **Final: n=111  W=101/L=10  WR=91.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W05.  `H20=H20e AND RSI=RSI5 AND direction_exec=long`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude session_bucket=ny_mid drops 7/17 losers (41%)
- **Final: n=111  W=101/L=10  WR=91.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 60-70 strong  •  AVOID when session=ny_mid

### W06.  `H20=H20e AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude session_bucket=ny_mid drops 7/17 losers (41%)
- **Final: n=111  W=101/L=10  WR=91.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W07.  `H60=H60a AND T4=T4a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=118  W=102/L=16  WR=86.4%
- Refine: exclude H20=H20a drops 13/16 losers (81%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W08.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=118  W=102/L=16  WR=86.4%
- Refine: exclude H20=H20a drops 13/16 losers (81%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W09.  `T4=T4a AND BBP=BBP6 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=118  W=102/L=16  WR=86.4%
- Refine: exclude H20=H20a drops 13/16 losers (81%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W10.  `T1=T1c AND T4=T4c AND session_bucket=asia_late`
- Raw: n=107  W=96/L=11  WR=89.7%
- Refine: exclude RSI=RSI5 drops 10/11 losers (91%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia_late  •  AVOID when RSI 60-70 strong

### W11.  `T4=T4c AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=107  W=96/L=11  WR=89.7%
- Refine: exclude RSI=RSI5 drops 10/11 losers (91%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=asia_late  •  AVOID when RSI 60-70 strong

### W12.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=107  W=96/L=11  WR=89.7%
- Refine: exclude RSI=RSI5 drops 10/11 losers (91%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia_late  •  AVOID when RSI 60-70 strong

### W13.  `H20=H20e AND T4=T4c AND session_bucket=asia_late`
- Raw: n=105  W=94/L=11  WR=89.5%
- Refine: exclude RSI=RSI5 drops 10/11 losers (91%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia_late  •  AVOID when RSI 60-70 strong

### W14.  `H60=H60e AND T4=T4c AND session_bucket=asia_late`
- Raw: n=105  W=94/L=11  WR=89.5%
- Refine: exclude RSI=RSI5 drops 10/11 losers (91%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia_late  •  AVOID when RSI 60-70 strong

### W15.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=asia_late`
- Raw: n=105  W=94/L=11  WR=89.5%
- Refine: exclude RSI=RSI5 drops 10/11 losers (91%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=asia_late  •  AVOID when RSI 60-70 strong

### W16.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=asia_late`
- Raw: n=105  W=94/L=11  WR=89.5%
- Refine: exclude RSI=RSI5 drops 10/11 losers (91%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia_late  •  AVOID when RSI 60-70 strong

### W17.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=105  W=94/L=11  WR=89.5%
- Refine: exclude RSI=RSI5 drops 10/11 losers (91%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia_late  •  AVOID when RSI 60-70 strong

### W18.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=asia_late`
- Raw: n=105  W=94/L=11  WR=89.5%
- Refine: exclude RSI=RSI5 drops 10/11 losers (91%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia_late  •  AVOID when RSI 60-70 strong

### W19.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=105  W=94/L=11  WR=89.5%
- Refine: exclude RSI=RSI5 drops 10/11 losers (91%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia_late  •  AVOID when RSI 60-70 strong

### W20.  `H20=H20e AND T1=T1a AND ZS=ZS5`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude H60=H60d drops 11/11 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 mildly against

### W21.  `H20=H20e AND ZS=ZS5 AND direction_exec=long`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude H60=H60d drops 11/11 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; zscore +2 to +3 deep overbought  •  AVOID when HTF60 mildly against

### W22.  `H20=H20e AND T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude H60=H60d drops 11/11 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 mildly against

### W23.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=91  W=81/L=10  WR=89.0%
- Refine: exclude H20=H20a drops 10/10 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 60-70 strong; session=asia  •  AVOID when HTF20 aligned WITH trade

### W24.  `T1=T1a AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude H20=H20a drops 12/12 losers (100%)
- **Final: n=13  W=13/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 70-80 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W25.  `T1=T1a AND RSI=RSI6 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude H20=H20a drops 12/12 losers (100%)
- **Final: n=13  W=13/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=150  W=55/L=95  WR=36.7%
- Sharpen: sharpest is ZS=ZS5 (54/95 of losers there)
- **Sharp: n=68  W=14/L=54  WR=20.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when zscore +2 to +3 deep overbought

### L02.  `H60=H60e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=139  W=45/L=94  WR=32.4%
- Sharpen: sharpest is T4=T4a (27/94 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when 4h trend WITH trade

### L03.  `H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=139  W=45/L=94  WR=32.4%
- Sharpen: sharpest is T4=T4a (27/94 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_open  •  ONLY when 4h trend WITH trade

### L04.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=139  W=45/L=94  WR=32.4%
- Sharpen: sharpest is T4=T4a (27/94 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when 4h trend WITH trade

### L05.  `H20=H20e AND H60=H60e AND session_bucket=ny_close`
- Raw: n=118  W=37/L=81  WR=31.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=118  W=37/L=81  WR=31.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_close

### L06.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=118  W=37/L=81  WR=31.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=118  W=37/L=81  WR=31.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=ny_close

### L07.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=118  W=37/L=81  WR=31.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=118  W=37/L=81  WR=31.4%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_close

### L08.  `H20=H20e AND H60=H60e AND session_bucket=ny_open`
- Raw: n=113  W=45/L=68  WR=39.8%
- Sharpen: sharpest is RSI=RSI6 (41/68 of losers there)
- **Sharp: n=56  W=15/L=41  WR=26.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when RSI 70-80 overbought

### L09.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=113  W=45/L=68  WR=39.8%
- Sharpen: sharpest is RSI=RSI6 (41/68 of losers there)
- **Sharp: n=56  W=15/L=41  WR=26.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 70-80 overbought

### L10.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=113  W=45/L=68  WR=39.8%
- Sharpen: sharpest is RSI=RSI6 (41/68 of losers there)
- **Sharp: n=56  W=15/L=41  WR=26.8%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when RSI 70-80 overbought

### L11.  `H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=111  W=32/L=79  WR=28.8%
- Sharpen: sharpest is session_bucket=ny_open (27/79 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=ny_open

### L12.  `H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=111  W=32/L=79  WR=28.8%
- Sharpen: sharpest is session_bucket=ny_open (27/79 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade  •  ONLY when session=ny_open

### L13.  `H60=H60e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=111  W=32/L=79  WR=28.8%
- Sharpen: sharpest is session_bucket=ny_open (27/79 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=ny_open

### L14.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=ny_close`
- Raw: n=107  W=37/L=70  WR=34.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=107  W=37/L=70  WR=34.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=ny_close

### L15.  `H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=98  W=29/L=69  WR=29.6%
- Sharpen: sharpest is session_bucket=ny_open (27/69 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=ny_open

### L16.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=98  W=29/L=69  WR=29.6%
- Sharpen: sharpest is session_bucket=ny_open (27/69 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=ny_open

### L17.  `H60=H60e AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=98  W=29/L=69  WR=29.6%
- Sharpen: sharpest is session_bucket=ny_open (27/69 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=ny_open

### L18.  `T1=T1c AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=95  W=36/L=59  WR=37.9%
- Sharpen: sharpest is H20=H20c (10/59 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 neutral

### L19.  `BBP=BBP4 AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=95  W=36/L=59  WR=37.9%
- Sharpen: sharpest is H20=H20c (10/59 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  upper third; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 neutral

### L20.  `T1=T1a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is RSI=RSI6 (33/58 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: LONG**  •  1h trend WITH trade; session=asia_late  •  ONLY when RSI 70-80 overbought

### L21.  `T1=T1c AND RSI=RSI6 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=93  W=34/L=59  WR=36.6%
- Sharpen: sharpest is H20=H20c (10/59 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 neutral

### L22.  `RSI=RSI6 AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=93  W=34/L=59  WR=36.6%
- Sharpen: sharpest is H20=H20c (10/59 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  RSI 70-80 overbought; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 neutral

### L23.  `T4=T4c AND RSI=RSI6 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is H20=H20c (10/54 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 neutral

### L24.  `T1=T1a AND T4=T4a AND session_bucket=asia_late`
- Raw: n=81  W=23/L=58  WR=28.4%
- Sharpen: sharpest is RSI=RSI6 (33/58 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=asia_late  •  ONLY when RSI 70-80 overbought

### L25.  `T4=T4a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=81  W=23/L=58  WR=28.4%
- Sharpen: sharpest is RSI=RSI6 (33/58 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: LONG**  •  4h trend WITH trade; session=asia_late  •  ONLY when RSI 70-80 overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(49/35), H60d(8/2) | H60e(39/54) |
| T1 | T1a(55/40) | T1c(45/60) |
| T4 | T4a(51/44) | T4c(49/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/40) | short(45/60) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
