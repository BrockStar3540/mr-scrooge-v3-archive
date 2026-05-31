# GBP_NZD — R22 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,147**  (W=1,856 / L=1,291)  -  WR: **59.0%**

## Session distribution

- london_open: n=1146  W=674/L=472  WR=58.8%
- asia: n=533  W=313/L=220  WR=58.7%
- ny_open: n=475  W=277/L=198  WR=58.3%
- ny_mid: n=436  W=259/L=177  WR=59.4%
- london: n=210  W=122/L=88  WR=58.1%
- ny_close: n=160  W=97/L=63  WR=60.6%
- off_hours: n=132  W=79/L=53  WR=59.8%
- asia_late: n=55  W=35/L=20  WR=63.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T1=T1a AND session_bucket=london_open`
- Raw: n=110  W=98/L=12  WR=89.1%
- Refine: exclude BBP=BBP5 drops 7/12 losers (58%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when just touched upper band

### W02.  `H20=H20e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=110  W=98/L=12  WR=89.1%
- Refine: exclude BBP=BBP5 drops 7/12 losers (58%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: LONG**  •  HTF20 strongly against; session=london_open  •  AVOID when just touched upper band

### W03.  `H20=H20e AND H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=110  W=98/L=12  WR=89.1%
- Refine: exclude BBP=BBP5 drops 7/12 losers (58%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when just touched upper band

### W04.  `H20=H20e AND H60=H60a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=110  W=98/L=12  WR=89.1%
- Refine: exclude BBP=BBP5 drops 7/12 losers (58%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=london_open  •  AVOID when just touched upper band

### W05.  `H20=H20e AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=110  W=98/L=12  WR=89.1%
- Refine: exclude BBP=BBP5 drops 7/12 losers (58%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when just touched upper band

### W06.  `T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=100  W=86/L=14  WR=86.0%
- Refine: exclude session_bucket=ny_open drops 10/14 losers (71%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W07.  `T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=100  W=86/L=14  WR=86.0%
- Refine: exclude session_bucket=ny_open drops 10/14 losers (71%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W08.  `T1=T1a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=100  W=86/L=14  WR=86.0%
- Refine: exclude session_bucket=ny_open drops 10/14 losers (71%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W09.  `H20=H20a AND T1=T1c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude session_bucket=london_open drops 11/12 losers (92%)
- **Final: n=82  W=81/L=1  WR=98.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W10.  `H20=H20a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude session_bucket=london_open drops 11/12 losers (92%)
- **Final: n=82  W=81/L=1  WR=98.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W11.  `H60=H60a AND T4=T4c AND BBP=BBP5`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude session_bucket=asia drops 5/13 losers (38%)
- **Final: n=90  W=82/L=8  WR=91.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; just touched upper band  •  AVOID when session=asia

### W12.  `H60=H60a AND T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude session_bucket=asia drops 5/13 losers (38%)
- **Final: n=90  W=82/L=8  WR=91.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W13.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=88  W=84/L=4  WR=95.5%
- Refine: exclude session_bucket=london_open drops 3/4 losers (75%)
- **Final: n=82  W=81/L=1  WR=98.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W14.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=87  W=82/L=5  WR=94.3%
- Refine: exclude RSI=RSI6 drops 5/5 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third; session=london_open  •  AVOID when RSI 70-80 overbought

### W15.  `H20=H20e AND T1=T1a AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=87  W=82/L=5  WR=94.3%
- Refine: exclude RSI=RSI6 drops 5/5 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought; session=london_open  •  AVOID when RSI 70-80 overbought

### W16.  `H20=H20e AND BBP=BBP4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=87  W=82/L=5  WR=94.3%
- Refine: exclude RSI=RSI6 drops 5/5 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; upper third; session=london_open  •  AVOID when RSI 70-80 overbought

### W17.  `H20=H20e AND ZS=ZS4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=87  W=82/L=5  WR=94.3%
- Refine: exclude RSI=RSI6 drops 5/5 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=london_open  •  AVOID when RSI 70-80 overbought

### W18.  `H60=H60a AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude T4=T4a drops 10/11 losers (91%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when 4h trend WITH trade

### W19.  `H60=H60a AND T1=T1c AND BBP=BBP5`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude session_bucket=asia drops 5/12 losers (42%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched upper band  •  AVOID when session=asia

### W20.  `H60=H60a AND BBP=BBP5 AND direction_exec=short`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude session_bucket=asia drops 5/12 losers (42%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; just touched upper band  •  AVOID when session=asia

### W21.  `H60=H60a AND T1=T1c AND T4=T4c AND BBP=BBP5`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude session_bucket=asia drops 5/12 losers (42%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band  •  AVOID when session=asia

### W22.  `H60=H60a AND T1=T1c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude session_bucket=asia drops 5/12 losers (42%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W23.  `H60=H60a AND T1=T1c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude session_bucket=asia drops 5/12 losers (42%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched upper band  •  AVOID when session=asia

### W24.  `H60=H60a AND T4=T4c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude session_bucket=asia drops 5/12 losers (42%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; just touched upper band  •  AVOID when session=asia

### W25.  `H60=H60a AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude session_bucket=asia drops 5/12 losers (42%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=240  W=91/L=149  WR=37.9%
- Sharpen: sharpest is H20=H20a (41/149 of losers there)
- **Sharp: n=50  W=9/L=41  WR=18.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L02.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=240  W=91/L=149  WR=37.9%
- Sharpen: sharpest is H20=H20a (41/149 of losers there)
- **Sharp: n=50  W=9/L=41  WR=18.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L03.  `T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=231  W=92/L=139  WR=39.8%
- Sharpen: sharpest is H60=H60e (82/139 of losers there)
- **Sharp: n=110  W=28/L=82  WR=25.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L04.  `H20=H20a AND T4=T4a AND ZS=ZS5`
- Raw: n=135  W=54/L=81  WR=40.0%
- Sharpen: sharpest is H60=H60e (64/81 of losers there)
- **Sharp: n=98  W=34/L=64  WR=34.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L05.  `H60=H60e AND T4=T4a AND ZS=ZS5`
- Raw: n=126  W=36/L=90  WR=28.6%
- Sharpen: sharpest is session_bucket=ny_open (21/90 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L06.  `T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=126  W=48/L=78  WR=38.1%
- Sharpen: sharpest is session_bucket=asia (28/78 of losers there)
- **Sharp: n=35  W=7/L=28  WR=20.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L07.  `T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=126  W=48/L=78  WR=38.1%
- Sharpen: sharpest is session_bucket=asia (28/78 of losers there)
- **Sharp: n=35  W=7/L=28  WR=20.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L08.  `T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=126  W=48/L=78  WR=38.1%
- Sharpen: sharpest is session_bucket=asia (28/78 of losers there)
- **Sharp: n=35  W=7/L=28  WR=20.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L09.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=126  W=48/L=78  WR=38.1%
- Sharpen: sharpest is session_bucket=asia (28/78 of losers there)
- **Sharp: n=35  W=7/L=28  WR=20.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L10.  `H60=H60e AND T1=T1a AND ZS=ZS5`
- Raw: n=120  W=36/L=84  WR=30.0%
- Sharpen: sharpest is session_bucket=ny_open (21/84 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L11.  `H60=H60e AND ZS=ZS5 AND direction_exec=long`
- Raw: n=120  W=36/L=84  WR=30.0%
- Sharpen: sharpest is session_bucket=ny_open (21/84 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L12.  `H60=H60e AND T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=120  W=36/L=84  WR=30.0%
- Sharpen: sharpest is session_bucket=ny_open (21/84 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L13.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: sharpest is H60=H60e (56/73 of losers there)
- **Sharp: n=82  W=26/L=56  WR=31.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L14.  `H60=H60e AND T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=118  W=36/L=82  WR=30.5%
- Sharpen: sharpest is session_bucket=ny_open (21/82 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L15.  `H60=H60e AND T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=118  W=36/L=82  WR=30.5%
- Sharpen: sharpest is session_bucket=ny_open (21/82 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L16.  `H20=H20a AND H60=H60e AND RSI=RSI6`
- Raw: n=115  W=46/L=69  WR=40.0%
- Sharpen: sharpest is session_bucket=london (28/69 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 70-80 overbought  •  ONLY when session=london

### L17.  `T1=T1c AND BBP=BBP2 AND RSI=RSI5`
- Raw: n=114  W=45/L=69  WR=39.5%
- Sharpen: sharpest is H60=H60e (34/69 of losers there)
- **Sharp: n=43  W=9/L=34  WR=20.9%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L18.  `BBP=BBP2 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=114  W=45/L=69  WR=39.5%
- Sharpen: sharpest is H60=H60e (34/69 of losers there)
- **Sharp: n=43  W=9/L=34  WR=20.9%**
- **Dir: SHORT**  •  lower third; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L19.  `T1=T1c AND BBP=BBP2 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=114  W=45/L=69  WR=39.5%
- Sharpen: sharpest is H60=H60e (34/69 of losers there)
- **Sharp: n=43  W=9/L=34  WR=20.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; lower third; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L20.  `H60=H60e AND T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=110  W=28/L=82  WR=25.5%
- Sharpen: sharpest is session_bucket=london_open (26/82 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L21.  `T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=107  W=37/L=70  WR=34.6%
- Sharpen: sharpest is session_bucket=london_open (21/70 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band  •  ONLY when session=london_open

### L22.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND RSI=RSI5`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is H60=H60e (30/64 of losers there)
- **Sharp: n=38  W=8/L=30  WR=21.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L23.  `T4=T4c AND BBP=BBP2 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is H60=H60e (30/64 of losers there)
- **Sharp: n=38  W=8/L=30  WR=21.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; lower third; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L24.  `T1=T1a AND T4=T4a AND BBP=BBP6`
- Raw: n=105  W=37/L=68  WR=35.2%
- Sharpen: sharpest is session_bucket=london_open (21/68 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when session=london_open

### L25.  `T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=105  W=37/L=68  WR=35.2%
- Sharpen: sharpest is session_bucket=london_open (21/68 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band  •  ONLY when session=london_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(49/43) | H60e(42/48) |
| T1 | T1a(52/45) | T1c(48/55) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(52/45) | short(48/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
