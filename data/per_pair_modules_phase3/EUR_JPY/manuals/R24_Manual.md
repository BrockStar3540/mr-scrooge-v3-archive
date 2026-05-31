# EUR_JPY — R24 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,314**  (W=2,035 / L=1,279)  -  WR: **61.4%**

## Session distribution

- asia: n=913  W=547/L=366  WR=59.9%
- london_open: n=752  W=479/L=273  WR=63.7%
- ny_open: n=611  W=372/L=239  WR=60.9%
- ny_mid: n=487  W=295/L=192  WR=60.6%
- ny_close: n=236  W=144/L=92  WR=61.0%
- london: n=165  W=100/L=65  WR=60.6%
- asia_late: n=114  W=73/L=41  WR=64.0%
- off_hours: n=36  W=25/L=11  WR=69.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude H20=H20a drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 aligned WITH trade

### W02.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude H20=H20a drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 aligned WITH trade

### W03.  `H20=H20e AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude ZS=ZS3 drops 11/13 losers (85%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W04.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 6/13 losers (46%)
- **Final: n=66  W=59/L=7  WR=89.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W05.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude ZS=ZS4 drops 11/12 losers (92%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W06.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude ZS=ZS4 drops 11/12 losers (92%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W07.  `H20=H20b AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=82  W=76/L=6  WR=92.7%
- Refine: exclude session_bucket=london drops 4/6 losers (67%)
- **Final: n=78  W=76/L=2  WR=97.4%**
- **Dir: ?**  •  HTF20 slightly aligned; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W08.  `T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude H20=H20d drops 5/11 losers (45%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when HTF20 mildly against

### W09.  `T1=T1c AND BBP=BBP6 AND ZS=ZS6`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude H20=H20c drops 11/11 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; zscore >+3 extreme  •  AVOID when HTF20 neutral

### W10.  `T1=T1c AND ZS=ZS6 AND direction_exec=short`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude H20=H20c drops 11/11 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore >+3 extreme  •  AVOID when HTF20 neutral

### W11.  `T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude H20=H20d drops 5/11 losers (45%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: LONG**  •  4h trend WITH trade; lower third  •  AVOID when HTF20 mildly against

### W12.  `BBP=BBP6 AND ZS=ZS6 AND direction_exec=short`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude H20=H20c drops 11/11 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep above upper band; zscore >+3 extreme  •  AVOID when HTF20 neutral

### W13.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude H20=H20d drops 5/11 losers (45%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when HTF20 mildly against

### W14.  `T1=T1c AND BBP=BBP6 AND ZS=ZS6 AND direction_exec=short`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude H20=H20c drops 11/11 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; zscore >+3 extreme  •  AVOID when HTF20 neutral

### W15.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude ZS=ZS3 drops 9/11 losers (82%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W16.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=london_open`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude ZS=ZS4 drops 8/8 losers (100%)
- **Final: n=43  W=43/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W17.  `H60=H60a AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude H20=H20a drops 11/11 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 aligned WITH trade

### W18.  `T1=T1a AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude H20=H20a drops 11/11 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 aligned WITH trade

### W19.  `RSI=RSI5 AND ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude H20=H20a drops 11/11 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 aligned WITH trade

### W20.  `H60=H60a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude H20=H20a drops 10/10 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 aligned WITH trade

### W21.  `T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude H20=H20d drops 5/9 losers (56%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when HTF20 mildly against

### W22.  `T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude H20=H20d drops 5/9 losers (56%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when HTF20 mildly against

### W23.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude H20=H20d drops 5/9 losers (56%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when HTF20 mildly against

### W24.  `T1=T1a AND T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude H20=H20d drops 5/9 losers (56%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when HTF20 mildly against

### W25.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude H20=H20d drops 5/9 losers (56%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when HTF20 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=195  W=76/L=119  WR=39.0%
- Sharpen: sharpest is BBP=BBP6 (56/119 of losers there)
- **Sharp: n=70  W=14/L=56  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L02.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=195  W=76/L=119  WR=39.0%
- Sharpen: sharpest is BBP=BBP6 (56/119 of losers there)
- **Sharp: n=70  W=14/L=56  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L03.  `H60=H60e AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=195  W=76/L=119  WR=39.0%
- Sharpen: sharpest is BBP=BBP6 (56/119 of losers there)
- **Sharp: n=70  W=14/L=56  WR=20.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L04.  `T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=150  W=60/L=90  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (30/90 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L05.  `H20=H20b AND BBP=BBP4 AND direction_exec=short`
- Raw: n=125  W=42/L=83  WR=33.6%
- Sharpen: sharpest is RSI=RSI5 (30/83 of losers there)
- **Sharp: n=35  W=5/L=30  WR=14.3%**
- **Dir: SHORT**  •  HTF20 slightly aligned; upper third  •  ONLY when RSI 60-70 strong

### L06.  `H20=H20b AND H60=H60e AND BBP=BBP4`
- Raw: n=121  W=42/L=79  WR=34.7%
- Sharpen: sharpest is T1=T1a (20/79 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; upper third  •  ONLY when 1h trend WITH trade

### L07.  `T4=T4a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=116  W=41/L=75  WR=35.3%
- Sharpen: sharpest is ZS=ZS5 (53/75 of losers there)
- **Sharp: n=67  W=14/L=53  WR=20.9%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L08.  `T4=T4a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=115  W=44/L=71  WR=38.3%
- Sharpen: sharpest is H20=H20d (26/71 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF20 mildly against

### L09.  `H20=H20b AND T1=T1c AND BBP=BBP4`
- Raw: n=114  W=42/L=72  WR=36.8%
- Sharpen: sharpest is RSI=RSI5 (30/72 of losers there)
- **Sharp: n=35  W=5/L=30  WR=14.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; upper third  •  ONLY when RSI 60-70 strong

### L10.  `H20=H20b AND T1=T1c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=114  W=42/L=72  WR=36.8%
- Sharpen: sharpest is RSI=RSI5 (30/72 of losers there)
- **Sharp: n=35  W=5/L=30  WR=14.3%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend AGAINST trade; upper third  •  ONLY when RSI 60-70 strong

### L11.  `H20=H20b AND H60=H60e AND BBP=BBP4 AND direction_exec=short`
- Raw: n=112  W=42/L=70  WR=37.5%
- Sharpen: sharpest is T1=T1a (11/70 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 strongly against; upper third  •  ONLY when 1h trend WITH trade

### L12.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=108  W=41/L=67  WR=38.0%
- Sharpen: sharpest is RSI=RSI5 (53/67 of losers there)
- **Sharp: n=67  W=14/L=53  WR=20.9%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L13.  `T1=T1c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=107  W=39/L=68  WR=36.4%
- Sharpen: sharpest is H20=H20e (40/68 of losers there)
- **Sharp: n=45  W=5/L=40  WR=11.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; lower third  •  ONLY when HTF20 strongly against

### L14.  `H20=H20b AND ZS=ZS4 AND direction_exec=short`
- Raw: n=104  W=37/L=67  WR=35.6%
- Sharpen: sharpest is RSI=RSI5 (27/67 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: SHORT**  •  HTF20 slightly aligned; zscore +1 to +2 overbought  •  ONLY when RSI 60-70 strong

### L15.  `H20=H20b AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=104  W=37/L=67  WR=35.6%
- Sharpen: sharpest is RSI=RSI5 (27/67 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: SHORT**  •  HTF20 slightly aligned; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 60-70 strong

### L16.  `T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is H20=H20d (17/64 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_close  •  ONLY when HTF20 mildly against

### L17.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is ZS=ZS4 (54/61 of losers there)
- **Sharp: n=82  W=28/L=54  WR=34.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L18.  `H20=H20a AND BBP=BBP4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is ZS=ZS4 (54/61 of losers there)
- **Sharp: n=82  W=28/L=54  WR=34.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L19.  `H60=H60e AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: sharpest is RSI=RSI5 (56/61 of losers there)
- **Sharp: n=70  W=14/L=56  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L20.  `H60=H60d AND T4=T4c AND ZS=ZS4`
- Raw: n=99  W=37/L=62  WR=37.4%
- Sharpen: sharpest is session_bucket=asia (14/62 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=asia

### L21.  `H60=H60d AND T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=99  W=37/L=62  WR=37.4%
- Sharpen: sharpest is session_bucket=asia (14/62 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=asia

### L22.  `H60=H60d AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=99  W=37/L=62  WR=37.4%
- Sharpen: sharpest is session_bucket=asia (14/62 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when session=asia

### L23.  `H60=H60d AND T4=T4c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=99  W=37/L=62  WR=37.4%
- Sharpen: sharpest is session_bucket=asia (14/62 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=asia

### L24.  `H20=H20b AND H60=H60e AND ZS=ZS4`
- Raw: n=98  W=37/L=61  WR=37.8%
- Sharpen: sharpest is T1=T1a (16/61 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L25.  `H20=H20b AND H60=H60e AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=98  W=37/L=61  WR=37.8%
- Sharpen: sharpest is T1=T1a (16/61 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(41/33) | H60e(33/43) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(52/46) | short(48/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
