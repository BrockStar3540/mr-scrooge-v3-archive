# CHF_JPY — R24 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,745**  (W=2,882 / L=1,863)  -  WR: **60.7%**

## Session distribution

- asia: n=1263  W=790/L=473  WR=62.5%
- london_open: n=1075  W=650/L=425  WR=60.5%
- ny_mid: n=862  W=514/L=348  WR=59.6%
- london: n=514  W=312/L=202  WR=60.7%
- ny_open: n=512  W=298/L=214  WR=58.2%
- ny_close: n=273  W=173/L=100  WR=63.4%
- off_hours: n=156  W=86/L=70  WR=55.1%
- asia_late: n=90  W=59/L=31  WR=65.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=198  W=174/L=24  WR=87.9%
- Refine: exclude H60=H60e drops 24/24 losers (100%)
- **Final: n=90  W=90/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when HTF60 strongly against

### W02.  `H20=H20a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=188  W=161/L=27  WR=85.6%
- Refine: exclude H60=H60a drops 27/27 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF60 aligned WITH trade

### W03.  `T4=T4a AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=178  W=155/L=23  WR=87.1%
- Refine: exclude BBP=BBP5 drops 23/23 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when just touched upper band

### W04.  `H20=H20e AND T4=T4a AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=165  W=150/L=15  WR=90.9%
- Refine: exclude H60=H60e drops 15/15 losers (100%)
- **Final: n=90  W=90/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when HTF60 strongly against

### W05.  `H20=H20e AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=165  W=150/L=15  WR=90.9%
- Refine: exclude H60=H60e drops 15/15 losers (100%)
- **Final: n=90  W=90/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when HTF60 strongly against

### W06.  `H20=H20e AND T1=T1a AND RSI=RSI5`
- Raw: n=162  W=149/L=13  WR=92.0%
- Refine: exclude H60=H60c drops 7/13 losers (54%)
- **Final: n=155  W=149/L=6  WR=96.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 neutral

### W07.  `H20=H20e AND RSI=RSI5 AND direction_exec=long`
- Raw: n=162  W=149/L=13  WR=92.0%
- Refine: exclude H60=H60c drops 7/13 losers (54%)
- **Final: n=155  W=149/L=6  WR=96.1%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 60-70 strong  •  AVOID when HTF60 neutral

### W08.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=162  W=149/L=13  WR=92.0%
- Refine: exclude H60=H60c drops 7/13 losers (54%)
- **Final: n=155  W=149/L=6  WR=96.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 neutral

### W09.  `H20=H20e AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=162  W=149/L=13  WR=92.0%
- Refine: exclude H60=H60c drops 7/13 losers (54%)
- **Final: n=155  W=149/L=6  WR=96.1%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 neutral

### W10.  `H20=H20e AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=162  W=149/L=13  WR=92.0%
- Refine: exclude H60=H60c drops 7/13 losers (54%)
- **Final: n=155  W=149/L=6  WR=96.1%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 neutral

### W11.  `T1=T1a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=157  W=134/L=23  WR=85.4%
- Refine: exclude H20=H20e drops 8/23 losers (35%)
- **Final: n=142  W=127/L=15  WR=89.4%**
- **Dir: LONG**  •  1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W12.  `T1=T1a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=157  W=134/L=23  WR=85.4%
- Refine: exclude H20=H20e drops 8/23 losers (35%)
- **Final: n=142  W=127/L=15  WR=89.4%**
- **Dir: LONG**  •  1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W13.  `H20=H20e AND H60=H60a AND RSI=RSI5`
- Raw: n=152  W=146/L=6  WR=96.1%
- Refine: exclude session_bucket=ny_mid drops 5/6 losers (83%)
- **Final: n=111  W=110/L=1  WR=99.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W14.  `H20=H20e AND H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=152  W=146/L=6  WR=96.1%
- Refine: exclude session_bucket=ny_mid drops 5/6 losers (83%)
- **Final: n=111  W=110/L=1  WR=99.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W15.  `H20=H20e AND H60=H60a AND T4=T4a AND RSI=RSI5`
- Raw: n=152  W=146/L=6  WR=96.1%
- Refine: exclude session_bucket=ny_mid drops 5/6 losers (83%)
- **Final: n=111  W=110/L=1  WR=99.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W16.  `H20=H20e AND H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=152  W=146/L=6  WR=96.1%
- Refine: exclude session_bucket=ny_mid drops 5/6 losers (83%)
- **Final: n=111  W=110/L=1  WR=99.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W17.  `H20=H20e AND T1=T1a AND session_bucket=london_open`
- Raw: n=149  W=127/L=22  WR=85.2%
- Refine: exclude H60=H60c drops 15/22 losers (68%)
- **Final: n=134  W=127/L=7  WR=94.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when HTF60 neutral

### W18.  `H60=H60a AND RSI=RSI5 AND session_bucket=london`
- Raw: n=145  W=132/L=13  WR=91.0%
- Refine: exclude BBP=BBP5 drops 8/13 losers (62%)
- **Final: n=120  W=115/L=5  WR=95.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london  •  AVOID when just touched upper band

### W19.  `T1=T1a AND RSI=RSI5 AND session_bucket=london`
- Raw: n=145  W=132/L=13  WR=91.0%
- Refine: exclude BBP=BBP5 drops 8/13 losers (62%)
- **Final: n=120  W=115/L=5  WR=95.8%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=london  •  AVOID when just touched upper band

### W20.  `RSI=RSI5 AND direction_exec=long AND session_bucket=london`
- Raw: n=145  W=132/L=13  WR=91.0%
- Refine: exclude BBP=BBP5 drops 8/13 losers (62%)
- **Final: n=120  W=115/L=5  WR=95.8%**
- **Dir: LONG**  •  RSI 60-70 strong; session=london  •  AVOID when just touched upper band

### W21.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=london`
- Raw: n=145  W=132/L=13  WR=91.0%
- Refine: exclude BBP=BBP5 drops 8/13 losers (62%)
- **Final: n=120  W=115/L=5  WR=95.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=london  •  AVOID when just touched upper band

### W22.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london`
- Raw: n=145  W=132/L=13  WR=91.0%
- Refine: exclude BBP=BBP5 drops 8/13 losers (62%)
- **Final: n=120  W=115/L=5  WR=95.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london  •  AVOID when just touched upper band

### W23.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london`
- Raw: n=145  W=132/L=13  WR=91.0%
- Refine: exclude BBP=BBP5 drops 8/13 losers (62%)
- **Final: n=120  W=115/L=5  WR=95.8%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=london  •  AVOID when just touched upper band

### W24.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=130  W=124/L=6  WR=95.4%
- Refine: exclude H20=H20c drops 5/6 losers (83%)
- **Final: n=114  W=113/L=1  WR=99.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when HTF20 neutral

### W25.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=130  W=124/L=6  WR=95.4%
- Refine: exclude H20=H20c drops 5/6 losers (83%)
- **Final: n=114  W=113/L=1  WR=99.1%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when HTF20 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=376  W=144/L=232  WR=38.3%
- Sharpen: sharpest is H20=H20a (94/232 of losers there)
- **Sharp: n=106  W=12/L=94  WR=11.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L02.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=376  W=144/L=232  WR=38.3%
- Sharpen: sharpest is H20=H20a (94/232 of losers there)
- **Sharp: n=106  W=12/L=94  WR=11.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L03.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=376  W=144/L=232  WR=38.3%
- Sharpen: sharpest is H20=H20a (94/232 of losers there)
- **Sharp: n=106  W=12/L=94  WR=11.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L04.  `H20=H20a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=266  W=98/L=168  WR=36.8%
- Sharpen: sharpest is session_bucket=london_open (96/168 of losers there)
- **Sharp: n=104  W=8/L=96  WR=7.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L05.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=232  W=71/L=161  WR=30.6%
- Sharpen: sharpest is session_bucket=london_open (96/161 of losers there)
- **Sharp: n=104  W=8/L=96  WR=7.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L06.  `H60=H60e AND T4=T4c AND session_bucket=london_open`
- Raw: n=228  W=91/L=137  WR=39.9%
- Sharpen: sharpest is RSI=RSI5 (76/137 of losers there)
- **Sharp: n=82  W=6/L=76  WR=7.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 60-70 strong

### L07.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=228  W=91/L=137  WR=39.9%
- Sharpen: sharpest is RSI=RSI5 (76/137 of losers there)
- **Sharp: n=82  W=6/L=76  WR=7.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 60-70 strong

### L08.  `H20=H20a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=220  W=78/L=142  WR=35.5%
- Sharpen: sharpest is ZS=ZS5 (96/142 of losers there)
- **Sharp: n=104  W=8/L=96  WR=7.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H60=H60e AND BBP=BBP2 AND direction_exec=short`
- Raw: n=219  W=80/L=139  WR=36.5%
- Sharpen: sharpest is T4=T4a (58/139 of losers there)
- **Sharp: n=75  W=17/L=58  WR=22.7%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third  •  ONLY when 4h trend WITH trade

### L10.  `H60=H60e AND direction_exec=short AND session_bucket=london`
- Raw: n=217  W=84/L=133  WR=38.7%
- Sharpen: sharpest is RSI=RSI5 (92/133 of losers there)
- **Sharp: n=111  W=19/L=92  WR=17.1%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london  •  ONLY when RSI 60-70 strong

### L11.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=216  W=74/L=142  WR=34.3%
- Sharpen: sharpest is ZS=ZS5 (96/142 of losers there)
- **Sharp: n=104  W=8/L=96  WR=7.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L12.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=198  W=73/L=125  WR=36.9%
- Sharpen: sharpest is RSI=RSI5 (76/125 of losers there)
- **Sharp: n=82  W=6/L=76  WR=7.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 60-70 strong

### L13.  `H60=H60e AND T1=T1c AND session_bucket=london`
- Raw: n=182  W=69/L=113  WR=37.9%
- Sharpen: sharpest is RSI=RSI5 (92/113 of losers there)
- **Sharp: n=111  W=19/L=92  WR=17.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london  •  ONLY when RSI 60-70 strong

### L14.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=182  W=69/L=113  WR=37.9%
- Sharpen: sharpest is RSI=RSI5 (92/113 of losers there)
- **Sharp: n=111  W=19/L=92  WR=17.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london  •  ONLY when RSI 60-70 strong

### L15.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=180  W=61/L=119  WR=33.9%
- Sharpen: sharpest is session_bucket=ny_close (19/119 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  lower third; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L16.  `H20=H20e AND T4=T4c AND RSI=RSI5`
- Raw: n=172  W=68/L=104  WR=39.5%
- Sharpen: sharpest is session_bucket=london (32/104 of losers there)
- **Sharp: n=37  W=5/L=32  WR=13.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london

### L17.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=172  W=68/L=104  WR=39.5%
- Sharpen: sharpest is session_bucket=london (32/104 of losers there)
- **Sharp: n=37  W=5/L=32  WR=13.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london

### L18.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=172  W=68/L=104  WR=39.5%
- Sharpen: sharpest is session_bucket=london (32/104 of losers there)
- **Sharp: n=37  W=5/L=32  WR=13.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london

### L19.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=172  W=68/L=104  WR=39.5%
- Sharpen: sharpest is session_bucket=london (32/104 of losers there)
- **Sharp: n=37  W=5/L=32  WR=13.5%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london

### L20.  `T4=T4c AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=171  W=66/L=105  WR=38.6%
- Sharpen: sharpest is H20=H20a (96/105 of losers there)
- **Sharp: n=104  W=8/L=96  WR=7.7%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L21.  `H20=H20e AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=168  W=54/L=114  WR=32.1%
- Sharpen: sharpest is BBP=BBP6 (53/114 of losers there)
- **Sharp: n=70  W=17/L=53  WR=24.3%**
- **Dir: ?**  •  HTF20 strongly against; zscore +2 to +3 deep overbought; session=asia  •  ONLY when deep above upper band

### L22.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=164  W=61/L=103  WR=37.2%
- Sharpen: sharpest is H20=H20a (69/103 of losers there)
- **Sharp: n=81  W=12/L=69  WR=14.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L23.  `H20=H20a AND H60=H60e AND T4=T4c`
- Raw: n=160  W=58/L=102  WR=36.2%
- Sharpen: sharpest is RSI=RSI5 (94/102 of losers there)
- **Sharp: n=106  W=12/L=94  WR=11.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L24.  `H20=H20a AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=160  W=58/L=102  WR=36.2%
- Sharpen: sharpest is RSI=RSI5 (94/102 of losers there)
- **Sharp: n=106  W=12/L=94  WR=11.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L25.  `H60=H60e AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=158  W=53/L=105  WR=33.5%
- Sharpen: sharpest is session_bucket=ny_close (16/105 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; lower third; zscore -2 to -1 oversold  •  ONLY when session=ny_close

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20e(38/43) |
| H60 | H60a(51/40) | H60e(40/51) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/46) | short(46/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
