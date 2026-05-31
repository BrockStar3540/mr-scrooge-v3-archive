# AUD_NZD — R26 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,465**  (W=1,549 / L=916)  -  WR: **62.8%**

## Session distribution

- asia: n=958  W=605/L=353  WR=63.2%
- ny_mid: n=397  W=239/L=158  WR=60.2%
- ny_open: n=333  W=217/L=116  WR=65.2%
- london_open: n=279  W=168/L=111  WR=60.2%
- ny_close: n=194  W=123/L=71  WR=63.4%
- london: n=125  W=77/L=48  WR=61.6%
- off_hours: n=107  W=71/L=36  WR=66.4%
- asia_late: n=72  W=49/L=23  WR=68.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=123  W=105/L=18  WR=85.4%
- Refine: exclude H60=H60e drops 8/18 losers (44%)
- **Final: n=98  W=88/L=10  WR=89.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF60 strongly against

### W02.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=113  W=103/L=10  WR=91.2%
- Refine: exclude RSI=RSI5 drops 7/10 losers (70%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 60-70 strong

### W03.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=113  W=103/L=10  WR=91.2%
- Refine: exclude RSI=RSI5 drops 7/10 losers (70%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 60-70 strong

### W04.  `H20=H20d AND T1=T1a AND RSI=RSI4`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude BBP=BBP5 drops 8/15 losers (53%)
- **Final: n=88  W=81/L=7  WR=92.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when just touched upper band

### W05.  `H20=H20d AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=96  W=85/L=11  WR=88.5%
- Refine: exclude T1=T1c drops 8/11 losers (73%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  HTF20 mildly against; upper third; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W06.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude T1=T1c drops 11/12 losers (92%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend AGAINST trade

### W07.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude T1=T1c drops 11/12 losers (92%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend AGAINST trade

### W08.  `H60=H60a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=93  W=85/L=8  WR=91.4%
- Refine: exclude H20=H20a drops 7/8 losers (88%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF20 aligned WITH trade

### W09.  `T1=T1a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=93  W=85/L=8  WR=91.4%
- Refine: exclude H20=H20a drops 7/8 losers (88%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF20 aligned WITH trade

### W10.  `RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=93  W=85/L=8  WR=91.4%
- Refine: exclude H20=H20a drops 7/8 losers (88%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: LONG**  •  RSI 60-70 strong; session=asia  •  AVOID when HTF20 aligned WITH trade

### W11.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=93  W=85/L=8  WR=91.4%
- Refine: exclude H20=H20a drops 7/8 losers (88%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF20 aligned WITH trade

### W12.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=93  W=85/L=8  WR=91.4%
- Refine: exclude H20=H20a drops 7/8 losers (88%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF20 aligned WITH trade

### W13.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=93  W=85/L=8  WR=91.4%
- Refine: exclude H20=H20a drops 7/8 losers (88%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF20 aligned WITH trade

### W14.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude T4=T4c drops 7/13 losers (54%)
- **Final: n=55  W=49/L=6  WR=89.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; session=asia  •  AVOID when 4h trend AGAINST trade

### W15.  `H20=H20a AND T1=T1a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: no further refinement
- **Final: n=88  W=75/L=13  WR=85.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought; session=asia

### W16.  `H60=H60a AND T1=T1a AND T4=T4a AND ZS=ZS4`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude RSI=RSI5 drops 10/12 losers (83%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 60-70 strong

### W17.  `T1=T1a AND T4=T4a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude RSI=RSI5 drops 10/12 losers (83%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 60-70 strong

### W18.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude T1=T1a drops 8/8 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend WITH trade

### W19.  `H20=H20a AND H60=H60a AND RSI=RSI5`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude session_bucket=asia drops 7/10 losers (70%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=asia

### W20.  `H20=H20a AND T1=T1a AND RSI=RSI5`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude session_bucket=asia drops 7/10 losers (70%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=asia

### W21.  `H20=H20a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude session_bucket=asia drops 7/10 losers (70%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=asia

### W22.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude session_bucket=asia drops 7/10 losers (70%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=asia

### W23.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude session_bucket=asia drops 7/10 losers (70%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=asia

### W24.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude session_bucket=asia drops 7/10 losers (70%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=asia

### W25.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=76  W=70/L=6  WR=92.1%
- Refine: exclude BBP=BBP5 drops 4/6 losers (67%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when just touched upper band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=144  W=56/L=88  WR=38.9%
- Sharpen: sharpest is ZS=ZS4 (31/88 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when zscore +1 to +2 overbought

### L02.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=144  W=56/L=88  WR=38.9%
- Sharpen: sharpest is ZS=ZS4 (31/88 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when zscore +1 to +2 overbought

### L03.  `H20=H20e AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=102  W=39/L=63  WR=38.2%
- Sharpen: sharpest is T4=T4c (38/63 of losers there)
- **Sharp: n=44  W=6/L=38  WR=13.6%**
- **Dir: ?**  •  HTF20 strongly against; upper third; session=asia  •  ONLY when 4h trend AGAINST trade

### L04.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is T4=T4c (34/59 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; session=asia  •  ONLY when 4h trend AGAINST trade

### L05.  `H20=H20e AND BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is T4=T4c (34/59 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; session=asia  •  ONLY when 4h trend AGAINST trade

### L06.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=95  W=32/L=63  WR=33.7%
- Sharpen: sharpest is BBP=BBP4 (26/63 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when upper third

### L07.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=89  W=33/L=56  WR=37.1%
- Sharpen: sharpest is RSI=RSI5 (32/56 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; session=asia  •  ONLY when RSI 60-70 strong

### L08.  `T1=T1c AND BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=89  W=33/L=56  WR=37.1%
- Sharpen: sharpest is RSI=RSI5 (32/56 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; session=asia  •  ONLY when RSI 60-70 strong

### L09.  `H60=H60e AND T1=T1c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=85  W=31/L=54  WR=36.5%
- Sharpen: sharpest is RSI=RSI5 (32/54 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 60-70 strong

### L10.  `T1=T1c AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=85  W=31/L=54  WR=36.5%
- Sharpen: sharpest is RSI=RSI5 (32/54 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 60-70 strong

### L11.  `H20=H20e AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=84  W=26/L=58  WR=31.0%
- Sharpen: sharpest is T4=T4c (35/58 of losers there)
- **Sharp: n=38  W=3/L=35  WR=7.9%**
- **Dir: ?**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=asia  •  ONLY when 4h trend AGAINST trade

### L12.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=84  W=26/L=58  WR=31.0%
- Sharpen: sharpest is T4=T4c (35/58 of losers there)
- **Sharp: n=38  W=3/L=35  WR=7.9%**
- **Dir: ?**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when 4h trend AGAINST trade

### L13.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=84  W=28/L=56  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (24/56 of losers there)
- **Sharp: n=31  W=7/L=24  WR=22.6%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L14.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (37/48 of losers there)
- **Sharp: n=52  W=15/L=37  WR=28.8%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=asia

### L15.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (37/48 of losers there)
- **Sharp: n=52  W=15/L=37  WR=28.8%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=asia

### L16.  `H20=H20e AND H60=H60e AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=79  W=25/L=54  WR=31.6%
- Sharpen: sharpest is T4=T4c (31/54 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +1 to +2 overbought; session=asia  •  ONLY when 4h trend AGAINST trade

### L17.  `H20=H20e AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=79  W=25/L=54  WR=31.6%
- Sharpen: sharpest is T4=T4c (31/54 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=asia  •  ONLY when 4h trend AGAINST trade

### L18.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is session_bucket=asia (36/47 of losers there)
- **Sharp: n=50  W=14/L=36  WR=28.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=asia

### L19.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is session_bucket=asia (36/47 of losers there)
- **Sharp: n=50  W=14/L=36  WR=28.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=asia

### L20.  `H20=H20b AND T1=T1c AND RSI=RSI4`
- Raw: n=73  W=29/L=44  WR=39.7%
- Sharpen: sharpest is T4=T4a (27/44 of losers there)
- **Sharp: n=40  W=13/L=27  WR=32.5%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L21.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=72  W=15/L=57  WR=20.8%
- Sharpen: sharpest is BBP=BBP4 (25/57 of losers there)
- **Sharp: n=26  W=1/L=25  WR=3.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when upper third

### L22.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=72  W=15/L=57  WR=20.8%
- Sharpen: sharpest is BBP=BBP4 (25/57 of losers there)
- **Sharp: n=26  W=1/L=25  WR=3.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when upper third

### L23.  `H20=H20e AND H60=H60e AND RSI=RSI5`
- Raw: n=71  W=18/L=53  WR=25.4%
- Sharpen: sharpest is BBP=BBP6 (20/53 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when deep above upper band

### L24.  `H20=H20e AND T1=T1c AND RSI=RSI5`
- Raw: n=71  W=18/L=53  WR=25.4%
- Sharpen: sharpest is BBP=BBP6 (20/53 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when deep above upper band

### L25.  `H20=H20e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=71  W=18/L=53  WR=25.4%
- Sharpen: sharpest is BBP=BBP6 (20/53 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong  •  ONLY when deep above upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(33/26) | H20e(27/37) |
| H60 | — | — |
| T1 | T1a(54/45) | T1c(45/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
