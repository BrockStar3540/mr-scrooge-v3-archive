# NZD_CHF — R27 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **724**  (W=491 / L=233)  -  WR: **67.8%**

## Session distribution

- asia: n=362  W=250/L=112  WR=69.1%
- ny_mid: n=150  W=102/L=48  WR=68.0%
- london_open: n=99  W=63/L=36  WR=63.6%
- ny_close: n=47  W=33/L=14  WR=70.2%
- london: n=22  W=16/L=6  WR=72.7%
- asia_late: n=18  W=13/L=5  WR=72.2%
- off_hours: n=14  W=8/L=6  WR=57.1%
- ny_open: n=12  W=6/L=6  WR=50.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=162  W=139/L=23  WR=85.8%
- Refine: exclude session_bucket=ny_mid drops 19/23 losers (83%)
- **Final: n=86  W=82/L=4  WR=95.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when session=ny_mid

### W02.  `H20=H20e AND H60=H60e AND T1=T1c`
- Raw: n=154  W=131/L=23  WR=85.1%
- Refine: exclude session_bucket=ny_mid drops 19/23 losers (83%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when session=ny_mid

### W03.  `H20=H20e AND H60=H60e AND direction_exec=short`
- Raw: n=154  W=131/L=23  WR=85.1%
- Refine: exclude session_bucket=ny_mid drops 19/23 losers (83%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against  •  AVOID when session=ny_mid

### W04.  `H20=H20e AND H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=154  W=131/L=23  WR=85.1%
- Refine: exclude session_bucket=ny_mid drops 19/23 losers (83%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when session=ny_mid

### W05.  `H20=H20e AND H60=H60e AND T4=T4a`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude ZS=ZS4 drops 11/15 losers (73%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  AVOID when zscore +1 to +2 overbought

### W06.  `H20=H20e AND H60=H60e AND RSI=RSI6`
- Raw: n=102  W=92/L=10  WR=90.2%
- Refine: exclude session_bucket=ny_mid drops 6/10 losers (60%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W07.  `H20=H20e AND H60=H60e AND session_bucket=asia`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude T1=T1a drops 11/12 losers (92%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  AVOID when 1h trend WITH trade

### W08.  `H60=H60e AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude session_bucket=london_open drops 7/10 losers (70%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 70-80 overbought  •  AVOID when session=london_open

### W09.  `H60=H60e AND T1=T1c AND RSI=RSI6`
- Raw: n=86  W=80/L=6  WR=93.0%
- Refine: exclude session_bucket=ny_mid drops 6/6 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W10.  `H60=H60e AND RSI=RSI6 AND direction_exec=short`
- Raw: n=86  W=80/L=6  WR=93.0%
- Refine: exclude session_bucket=ny_mid drops 6/6 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W11.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI6`
- Raw: n=86  W=80/L=6  WR=93.0%
- Refine: exclude session_bucket=ny_mid drops 6/6 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W12.  `H20=H20e AND H60=H60e AND RSI=RSI6 AND direction_exec=short`
- Raw: n=86  W=80/L=6  WR=93.0%
- Refine: exclude session_bucket=ny_mid drops 6/6 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W13.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=86  W=80/L=6  WR=93.0%
- Refine: exclude session_bucket=ny_mid drops 6/6 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W14.  `H60=H60e AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude session_bucket=london_open drops 7/10 losers (70%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W15.  `H60=H60e AND BBP=BBP4 AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude session_bucket=london_open drops 7/10 losers (70%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 70-80 overbought; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W16.  `H20=H20e AND H60=H60e AND ZS=ZS5`
- Raw: n=83  W=78/L=5  WR=94.0%
- Refine: exclude session_bucket=ny_mid drops 5/5 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W17.  `H20=H20e AND T1=T1c AND ZS=ZS5`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude H60=H60a drops 6/11 losers (55%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W18.  `H20=H20e AND ZS=ZS5 AND direction_exec=short`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude H60=H60a drops 6/11 losers (55%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W19.  `H20=H20e AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude H60=H60a drops 6/11 losers (55%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W20.  `H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude H20=H20e drops 11/11 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=asia  •  AVOID when HTF20 strongly against

### W21.  `H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude H20=H20e drops 11/11 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when HTF20 strongly against

### W22.  `H60=H60e AND direction_exec=long AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude H20=H20e drops 11/11 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; session=asia  •  AVOID when HTF20 strongly against

### W23.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude H20=H20e drops 11/11 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF20 strongly against

### W24.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude H20=H20e drops 11/11 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=asia  •  AVOID when HTF20 strongly against

### W25.  `H60=H60e AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude H20=H20e drops 11/11 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T4=T4c AND RSI=RSI6`
- Raw: n=69  W=26/L=43  WR=37.7%
- Sharpen: sharpest is session_bucket=asia (19/43 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L02.  `H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is H20=H20e (17/41 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  ONLY when HTF20 strongly against

### L03.  `H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is H20=H20e (17/41 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF20 strongly against

### L04.  `H60=H60a AND direction_exec=short AND session_bucket=asia`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is H20=H20e (17/41 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=asia  •  ONLY when HTF20 strongly against

### L05.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is H20=H20e (17/41 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF20 strongly against

### L06.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is H20=H20e (17/41 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  ONLY when HTF20 strongly against

### L07.  `H60=H60a AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is H20=H20e (17/41 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF20 strongly against

### L08.  `T1=T1c AND T4=T4c AND BBP=BBP6`
- Raw: n=42  W=16/L=26  WR=38.1%
- Sharpen: sharpest is session_bucket=asia (26/26 of losers there)
- **Sharp: n=34  W=8/L=26  WR=23.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when session=asia

### L09.  `T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=42  W=16/L=26  WR=38.1%
- Sharpen: sharpest is session_bucket=asia (26/26 of losers there)
- **Sharp: n=34  W=8/L=26  WR=23.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band  •  ONLY when session=asia

### L10.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=42  W=16/L=26  WR=38.1%
- Sharpen: sharpest is session_bucket=asia (26/26 of losers there)
- **Sharp: n=34  W=8/L=26  WR=23.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when session=asia

### L11.  `H20=H20a AND H60=H60a AND ZS=ZS5`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is BBP=BBP6 (16/25 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L12.  `H20=H20b AND H60=H60d AND ZS=ZS5`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is RSI=RSI7 (11/22 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 mildly against; zscore +2 to +3 deep overbought  •  ONLY when RSI>80 extreme overbought

### L13.  `H20=H20b AND T1=T1c AND ZS=ZS5`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is RSI=RSI7 (11/22 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI>80 extreme overbought

### L14.  `H20=H20b AND T4=T4c AND ZS=ZS5`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is RSI=RSI7 (11/22 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI>80 extreme overbought

### L15.  `H20=H20b AND ZS=ZS5 AND direction_exec=short`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is RSI=RSI7 (11/22 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: SHORT**  •  HTF20 slightly aligned; zscore +2 to +3 deep overbought  •  ONLY when RSI>80 extreme overbought

### L16.  `H20=H20b AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is RSI=RSI7 (11/22 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: ?**  •  HTF20 slightly aligned; zscore +2 to +3 deep overbought; session=asia  •  ONLY when RSI>80 extreme overbought

### L17.  `H60=H60d AND T1=T1c AND ZS=ZS5`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is RSI=RSI7 (11/22 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI>80 extreme overbought

### L18.  `H60=H60d AND T4=T4c AND ZS=ZS5`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is RSI=RSI7 (11/22 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI>80 extreme overbought

### L19.  `H60=H60d AND ZS=ZS5 AND direction_exec=short`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is RSI=RSI7 (11/22 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: SHORT**  •  HTF60 mildly against; zscore +2 to +3 deep overbought  •  ONLY when RSI>80 extreme overbought

### L20.  `H60=H60d AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is RSI=RSI7 (11/22 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: ?**  •  HTF60 mildly against; zscore +2 to +3 deep overbought; session=asia  •  ONLY when RSI>80 extreme overbought

### L21.  `H20=H20b AND H60=H60d AND T1=T1c AND ZS=ZS5`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is RSI=RSI7 (11/22 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 mildly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI>80 extreme overbought

### L22.  `H20=H20b AND H60=H60d AND T4=T4c AND ZS=ZS5`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is RSI=RSI7 (11/22 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 mildly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI>80 extreme overbought

### L23.  `H20=H20b AND H60=H60d AND ZS=ZS5 AND direction_exec=short`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is RSI=RSI7 (11/22 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 mildly against; zscore +2 to +3 deep overbought  •  ONLY when RSI>80 extreme overbought

### L24.  `H20=H20b AND H60=H60d AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is RSI=RSI7 (11/22 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 mildly against; zscore +2 to +3 deep overbought; session=asia  •  ONLY when RSI>80 extreme overbought

### L25.  `H20=H20b AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is RSI=RSI7 (11/22 of losers there)
- **Sharp: n=15  W=4/L=11  WR=26.7%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI>80 extreme overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(46/27) | H20a(28/47) |
| H60 | H60e(49/20) | H60a(25/50) |
| T1 | — | — |
| T4 | T4a(48/42) | T4c(52/58) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
