# EUR_GBP — R37 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **533**  (W=361 / L=172)  -  WR: **67.7%**

## Session distribution

- london_open: n=167  W=108/L=59  WR=64.7%
- london: n=101  W=66/L=35  WR=65.3%
- ny_open: n=80  W=54/L=26  WR=67.5%
- asia: n=52  W=36/L=16  WR=69.2%
- ny_mid: n=52  W=39/L=13  WR=75.0%
- ny_close: n=48  W=32/L=16  WR=66.7%
- asia_late: n=20  W=14/L=6  WR=70.0%
- off_hours: n=13  W=12/L=1  WR=92.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60d AND T1=T1c AND direction_exec=short`
- Raw: n=100  W=88/L=12  WR=88.0%
- Refine: exclude session_bucket=london_open drops 8/12 losers (67%)
- **Final: n=84  W=80/L=4  WR=95.2%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend AGAINST trade  •  AVOID when session=london_open

### W02.  `H60=H60d AND T1=T1c AND RSI=RSI5`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude session_bucket=london_open drops 8/10 losers (80%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=london_open

### W03.  `H60=H60d AND RSI=RSI5 AND direction_exec=short`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude session_bucket=london_open drops 8/10 losers (80%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: SHORT**  •  HTF60 mildly against; RSI 60-70 strong  •  AVOID when session=london_open

### W04.  `H60=H60d AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude session_bucket=london_open drops 8/10 losers (80%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=london_open

### W05.  `H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude H20=H20a drops 9/10 losers (90%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W06.  `H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude H20=H20a drops 9/10 losers (90%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W07.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude H20=H20a drops 9/10 losers (90%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W08.  `H60=H60d AND T4=T4a AND RSI=RSI5`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude session_bucket=london_open drops 7/9 losers (78%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W09.  `H20=H20e AND T1=T1c AND direction_exec=short`
- Raw: n=58  W=52/L=6  WR=89.7%
- Refine: exclude session_bucket=ny_open drops 5/6 losers (83%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade  •  AVOID when session=ny_open

### W10.  `H60=H60d AND T4=T4a AND direction_exec=short`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude T1=T1a drops 4/6 losers (67%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend WITH trade  •  AVOID when 1h trend WITH trade

### W11.  `H20=H20e AND T1=T1c AND RSI=RSI5`
- Raw: n=51  W=46/L=5  WR=90.2%
- Refine: exclude session_bucket=ny_open drops 5/5 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W12.  `H20=H20e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=51  W=46/L=5  WR=90.2%
- Refine: exclude session_bucket=ny_open drops 5/5 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong  •  AVOID when session=ny_open

### W13.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=51  W=46/L=5  WR=90.2%
- Refine: exclude session_bucket=ny_open drops 5/5 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W14.  `H20=H20e AND H60=H60d AND RSI=RSI5`
- Raw: n=51  W=44/L=7  WR=86.3%
- Refine: exclude session_bucket=london_open drops 7/7 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; RSI 60-70 strong  •  AVOID when session=london_open

### W15.  `H20=H20e AND H60=H60d AND T4=T4a AND RSI=RSI5`
- Raw: n=51  W=44/L=7  WR=86.3%
- Refine: exclude session_bucket=london_open drops 7/7 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W16.  `H60=H60d AND T1=T1c AND T4=T4a`
- Raw: n=50  W=48/L=2  WR=96.0%
- Refine: exclude session_bucket=london drops 2/2 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=london

### W17.  `H60=H60d AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=50  W=48/L=2  WR=96.0%
- Refine: exclude session_bucket=london drops 2/2 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=london

### W18.  `H60=H60d AND RSI=RSI5 AND session_bucket=london`
- Raw: n=48  W=46/L=2  WR=95.8%
- Refine: exclude T4=T4a drops 2/2 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 mildly against; RSI 60-70 strong; session=london  •  AVOID when 4h trend WITH trade

### W19.  `T1=T1a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=48  W=46/L=2  WR=95.8%
- Refine: exclude T4=T4a drops 2/2 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when 4h trend WITH trade

### W20.  `H20=H20e AND T1=T1a AND BBP=BBP6`
- Raw: n=48  W=43/L=5  WR=89.6%
- Refine: exclude H60=H60b drops 4/5 losers (80%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; deep above upper band  •  AVOID when HTF60 slightly aligned

### W21.  `H20=H20e AND H60=H60a AND T1=T1a`
- Raw: n=47  W=46/L=1  WR=97.9%
- Refine: no further refinement
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade

### W22.  `H20=H20a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=47  W=42/L=5  WR=89.4%
- Refine: exclude T1=T1a drops 4/5 losers (80%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when 1h trend WITH trade

### W23.  `H20=H20a AND H60=H60d AND session_bucket=london`
- Raw: n=46  W=42/L=4  WR=91.3%
- Refine: exclude BBP=BBP2 drops 2/4 losers (50%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; session=london  •  AVOID when lower third

### W24.  `H60=H60a AND T1=T1a AND BBP=BBP4`
- Raw: n=46  W=42/L=4  WR=91.3%
- Refine: exclude H20=H20a drops 4/4 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when HTF20 aligned WITH trade

### W25.  `H60=H60d AND T1=T1c AND session_bucket=london`
- Raw: n=46  W=42/L=4  WR=91.3%
- Refine: exclude BBP=BBP2 drops 2/4 losers (50%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; session=london  •  AVOID when lower third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is H20=H20d (13/32 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L02.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is H20=H20d (13/32 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L03.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is H20=H20d (13/32 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L04.  `T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=33  W=12/L=21  WR=36.4%
- Sharpen: sharpest is H60=H60e (13/21 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band  •  ONLY when HTF60 strongly against

### L05.  `H60=H60b AND RSI=RSI5 AND session_bucket=london`
- Raw: n=32  W=8/L=24  WR=25.0%
- Sharpen: sharpest is ZS=ZS5 (14/24 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 slightly aligned; RSI 60-70 strong; session=london  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `H20=H20e AND H60=H60b AND session_bucket=london`
- Raw: n=31  W=10/L=21  WR=32.3%
- Sharpen: sharpest is ZS=ZS5 (10/21 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; session=london  •  ONLY when zscore +2 to +3 deep overbought

### L07.  `H60=H60b AND T1=T1a AND session_bucket=london`
- Raw: n=31  W=10/L=21  WR=32.3%
- Sharpen: sharpest is ZS=ZS5 (10/21 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; session=london  •  ONLY when zscore +2 to +3 deep overbought

### L08.  `H60=H60b AND direction_exec=long AND session_bucket=london`
- Raw: n=31  W=10/L=21  WR=32.3%
- Sharpen: sharpest is ZS=ZS5 (10/21 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF60 slightly aligned; session=london  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H20=H20e AND H60=H60b AND T1=T1a AND session_bucket=london`
- Raw: n=31  W=10/L=21  WR=32.3%
- Sharpen: sharpest is ZS=ZS5 (10/21 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 1h trend WITH trade; session=london  •  ONLY when zscore +2 to +3 deep overbought

### L10.  `H20=H20e AND H60=H60b AND direction_exec=long AND session_bucket=london`
- Raw: n=31  W=10/L=21  WR=32.3%
- Sharpen: sharpest is ZS=ZS5 (10/21 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 slightly aligned; session=london  •  ONLY when zscore +2 to +3 deep overbought

### L11.  `H60=H60b AND T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=31  W=10/L=21  WR=32.3%
- Sharpen: sharpest is ZS=ZS5 (10/21 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF60 slightly aligned; 1h trend WITH trade; session=london  •  ONLY when zscore +2 to +3 deep overbought

### L12.  `H20=H20a AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=30  W=8/L=22  WR=26.7%
- Sharpen: sharpest is RSI=RSI5 (22/22 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when RSI 60-70 strong

### L13.  `ZS=ZS5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=30  W=8/L=22  WR=26.7%
- Sharpen: sharpest is RSI=RSI5 (22/22 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: SHORT**  •  zscore +2 to +3 deep overbought; session=london_open  •  ONLY when RSI 60-70 strong

### L14.  `H20=H20a AND ZS=ZS5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=30  W=8/L=22  WR=26.7%
- Sharpen: sharpest is RSI=RSI5 (22/22 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when RSI 60-70 strong

### L15.  `H20=H20a AND T4=T4a AND session_bucket=london_open`
- Raw: n=30  W=10/L=20  WR=33.3%
- Sharpen: sharpest is RSI=RSI5 (16/20 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when RSI 60-70 strong

### L16.  `T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=30  W=10/L=20  WR=33.3%
- Sharpen: sharpest is RSI=RSI5 (16/20 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london_open  •  ONLY when RSI 60-70 strong

### L17.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=30  W=10/L=20  WR=33.3%
- Sharpen: sharpest is RSI=RSI5 (16/20 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when RSI 60-70 strong

### L18.  `H20=H20e AND T4=T4a AND session_bucket=london`
- Raw: n=30  W=12/L=18  WR=40.0%
- Sharpen: sharpest is H60=H60b (18/18 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=london  •  ONLY when HTF60 slightly aligned

### L19.  `T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=30  W=12/L=18  WR=40.0%
- Sharpen: sharpest is H20=H20e (14/18 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_open  •  ONLY when HTF20 strongly against

### L20.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=london`
- Raw: n=30  W=12/L=18  WR=40.0%
- Sharpen: sharpest is H60=H60b (18/18 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=london  •  ONLY when HTF60 slightly aligned

### L21.  `H20=H20e AND T4=T4a AND direction_exec=long AND session_bucket=london`
- Raw: n=30  W=12/L=18  WR=40.0%
- Sharpen: sharpest is H60=H60b (18/18 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; session=london  •  ONLY when HTF60 slightly aligned

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(49/37) | H20a(39/48) |
| H60 | H60d(29/14), H60a(26/17) | H60b(12/26), H60e(16/27) |
| T1 | — | — |
| T4 | T4c(52/44) | T4a(48/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
