# GBP_JPY — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,048**  (W=2,400 / L=1,648)  -  WR: **59.3%**

## Session distribution

- asia: n=2002  W=1185/L=817  WR=59.2%
- ny_close: n=1164  W=700/L=464  WR=60.1%
- ny_open: n=295  W=181/L=114  WR=61.4%
- off_hours: n=218  W=129/L=89  WR=59.2%
- london: n=199  W=112/L=87  WR=56.3%
- asia_late: n=108  W=55/L=53  WR=50.9%
- ny_mid: n=52  W=33/L=19  WR=63.5%
- london_open: n=10  W=5/L=5  WR=50.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `RSI=RSI4 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=139  W=129/L=10  WR=92.8%
- Refine: exclude strategy_id=charlie_compression_breakout drops 4/10 losers (40%)
- **Final: n=121  W=115/L=6  WR=95.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when strategy=charlie_compression_breakout

### W02.  `H60=H60a AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=134  W=124/L=10  WR=92.5%
- Refine: exclude strategy_id=charlie_compression_breakout drops 4/10 losers (40%)
- **Final: n=117  W=111/L=6  WR=94.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when strategy=charlie_compression_breakout

### W03.  `H60=H60a AND RSI=RSI4 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=134  W=124/L=10  WR=92.5%
- Refine: exclude strategy_id=charlie_compression_breakout drops 4/10 losers (40%)
- **Final: n=117  W=111/L=6  WR=94.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when strategy=charlie_compression_breakout

### W04.  `BBP=BBP1 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude strategy_id=charlie_compression_breakout drops 4/9 losers (44%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: LONG**  •  just touched lower band; RSI 50-60 upper neutral  •  AVOID when strategy=charlie_compression_breakout

### W05.  `BBP=BBP1 AND RSI=RSI4 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude strategy_id=charlie_compression_breakout drops 4/9 losers (44%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: LONG**  •  just touched lower band; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when strategy=charlie_compression_breakout

### W06.  `H60=H60a AND BBP=BBP1 AND RSI=RSI4`
- Raw: n=103  W=94/L=9  WR=91.3%
- Refine: exclude strategy_id=charlie_compression_breakout drops 4/9 losers (44%)
- **Final: n=91  W=86/L=5  WR=94.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched lower band; RSI 50-60 upper neutral  •  AVOID when strategy=charlie_compression_breakout

### W07.  `H60=H60a AND BBP=BBP1 AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=103  W=94/L=9  WR=91.3%
- Refine: exclude strategy_id=charlie_compression_breakout drops 4/9 losers (44%)
- **Final: n=91  W=86/L=5  WR=94.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched lower band; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when strategy=charlie_compression_breakout

### W08.  `H60=H60a AND BBP=BBP1 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=103  W=94/L=9  WR=91.3%
- Refine: exclude strategy_id=charlie_compression_breakout drops 4/9 losers (44%)
- **Final: n=91  W=86/L=5  WR=94.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; just touched lower band; RSI 50-60 upper neutral  •  AVOID when strategy=charlie_compression_breakout

### W09.  `H20=H20a AND H60=H60a AND T4=T4a AND BBP=BBP2`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude RSI=RSI3 drops 4/15 losers (27%)
- **Final: n=93  W=82/L=11  WR=88.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; lower third  •  AVOID when RSI 40-50 lower neutral

### W10.  `H20=H20a AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude RSI=RSI3 drops 4/15 losers (27%)
- **Final: n=93  W=82/L=11  WR=88.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third  •  AVOID when RSI 40-50 lower neutral

### W11.  `T1=T1a AND RSI=RSI4 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=93  W=87/L=6  WR=93.5%
- Refine: exclude H20=H20e drops 4/6 losers (67%)
- **Final: n=70  W=68/L=2  WR=97.1%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W12.  `RSI=RSI4 AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=91  W=86/L=5  WR=94.5%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/5 losers (60%)
- **Final: n=77  W=75/L=2  WR=97.4%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -3 to -2 deep oversold; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W13.  `T4=T4c AND RSI=RSI4 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=91  W=84/L=7  WR=92.3%
- Refine: exclude H20=H20a drops 6/7 losers (86%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 aligned WITH trade

### W14.  `H20=H20a AND T1=T1a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude RSI=RSI3 drops 10/12 losers (83%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W15.  `H60=H60a AND RSI=RSI4 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=88  W=83/L=5  WR=94.3%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/5 losers (60%)
- **Final: n=74  W=72/L=2  WR=97.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W16.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=88  W=82/L=6  WR=93.2%
- Refine: exclude H20=H20e drops 4/6 losers (67%)
- **Final: n=65  W=63/L=2  WR=96.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W17.  `H60=H60a AND T4=T4c AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=86  W=79/L=7  WR=91.9%
- Refine: exclude H20=H20a drops 6/7 losers (86%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 aligned WITH trade

### W18.  `BBP=BBP2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=83  W=72/L=11  WR=86.7%
- Refine: exclude T1=T1a drops 11/11 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: LONG**  •  lower third; session=ny_close  •  AVOID when 1h trend WITH trade

### W19.  `H20=H20a AND H60=H60a AND T1=T1a AND ZS=ZS1`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude RSI=RSI3 drops 10/12 losers (83%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W20.  `T1=T1a AND BBP=BBP1 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=79  W=74/L=5  WR=93.7%
- Refine: exclude H20=H20e drops 3/5 losers (60%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: LONG**  •  1h trend WITH trade; just touched lower band; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W21.  `H20=H20a AND H60=H60e AND RSI=RSI3`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude T1=T1a drops 8/9 losers (89%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W22.  `H20=H20a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude T1=T1a drops 8/9 losers (89%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W23.  `H20=H20a AND H60=H60e AND RSI=RSI3 AND direction_exec=short`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude T1=T1a drops 8/9 losers (89%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W24.  `H20=H20a AND H60=H60a AND T4=T4a AND ZS=ZS2`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude RSI=RSI3 drops 4/11 losers (36%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W25.  `H20=H20a AND T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude RSI=RSI3 drops 4/11 losers (36%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=458  W=182/L=276  WR=39.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=458  W=182/L=276  WR=39.7%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral

### L02.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=415  W=160/L=255  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=415  W=160/L=255  WR=38.6%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought

### L03.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=415  W=160/L=255  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=415  W=160/L=255  WR=38.6%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought

### L04.  `H60=H60a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=375  W=143/L=232  WR=38.1%
- Sharpen: sharpest is H20=H20e (54/232 of losers there)
- **Sharp: n=63  W=9/L=54  WR=14.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L05.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=335  W=134/L=201  WR=40.0%
- Sharpen: sharpest is T4=T4a (95/201 of losers there)
- **Sharp: n=134  W=39/L=95  WR=29.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L06.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=313  W=124/L=189  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=313  W=124/L=189  WR=39.6%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought

### L07.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=310  W=124/L=186  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=310  W=124/L=186  WR=40.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought

### L08.  `H20=H20e AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=279  W=110/L=169  WR=39.4%
- Sharpen: sharpest is ZS=ZS4 (95/169 of losers there)
- **Sharp: n=134  W=39/L=95  WR=29.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +1 to +2 overbought

### L09.  `T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=270  W=104/L=166  WR=38.5%
- Sharpen: sharpest is H20=H20e (49/166 of losers there)
- **Sharp: n=57  W=8/L=49  WR=14.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L10.  `H60=H60a AND T4=T4c AND RSI=RSI3`
- Raw: n=263  W=98/L=165  WR=37.3%
- Sharpen: sharpest is H20=H20e (49/165 of losers there)
- **Sharp: n=57  W=8/L=49  WR=14.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L11.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=263  W=98/L=165  WR=37.3%
- Sharpen: sharpest is H20=H20e (49/165 of losers there)
- **Sharp: n=57  W=8/L=49  WR=14.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L12.  `H20=H20e AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=254  W=93/L=161  WR=36.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=254  W=93/L=161  WR=36.6%**
- **Dir: ?**  •  HTF20 strongly against; upper third; session=asia

### L13.  `H20=H20e AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=234  W=87/L=147  WR=37.2%
- Sharpen: sharpest is T4=T4a (82/147 of losers there)
- **Sharp: n=115  W=33/L=82  WR=28.7%**
- **Dir: ?**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=asia  •  ONLY when 4h trend WITH trade

### L14.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=234  W=87/L=147  WR=37.2%
- Sharpen: sharpest is T4=T4a (82/147 of losers there)
- **Sharp: n=115  W=33/L=82  WR=28.7%**
- **Dir: ?**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when 4h trend WITH trade

### L15.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=225  W=78/L=147  WR=34.7%
- Sharpen: sharpest is H60=H60a (55/147 of losers there)
- **Sharp: n=70  W=15/L=55  WR=21.4%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF60 aligned WITH trade

### L16.  `H60=H60a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=224  W=82/L=142  WR=36.6%
- Sharpen: sharpest is H20=H20e (41/142 of losers there)
- **Sharp: n=45  W=4/L=41  WR=8.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF20 strongly against

### L17.  `RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=224  W=82/L=142  WR=36.6%
- Sharpen: sharpest is H20=H20e (41/142 of losers there)
- **Sharp: n=45  W=4/L=41  WR=8.9%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=asia  •  ONLY when HTF20 strongly against

### L18.  `H60=H60a AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=224  W=82/L=142  WR=36.6%
- Sharpen: sharpest is H20=H20e (41/142 of losers there)
- **Sharp: n=45  W=4/L=41  WR=8.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF20 strongly against

### L19.  `H20=H20e AND H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=212  W=77/L=135  WR=36.3%
- Sharpen: sharpest is RSI=RSI3 (45/135 of losers there)
- **Sharp: n=45  W=0/L=45  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L20.  `H20=H20e AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=212  W=77/L=135  WR=36.3%
- Sharpen: sharpest is RSI=RSI3 (45/135 of losers there)
- **Sharp: n=45  W=0/L=45  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L21.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=205  W=72/L=133  WR=35.1%
- Sharpen: sharpest is H60=H60a (45/133 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  ONLY when HTF60 aligned WITH trade

### L22.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=202  W=75/L=127  WR=37.1%
- Sharpen: sharpest is T4=T4a (82/127 of losers there)
- **Sharp: n=118  W=36/L=82  WR=30.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third; session=asia  •  ONLY when 4h trend WITH trade

### L23.  `H20=H20e AND T1=T1c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=194  W=72/L=122  WR=37.1%
- Sharpen: sharpest is T4=T4a (80/122 of losers there)
- **Sharp: n=113  W=33/L=80  WR=29.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  ONLY when 4h trend WITH trade

### L24.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=182  W=69/L=113  WR=37.9%
- Sharpen: sharpest is ZS=ZS4 (82/113 of losers there)
- **Sharp: n=115  W=33/L=82  WR=28.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +1 to +2 overbought

### L25.  `T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=173  W=60/L=113  WR=34.7%
- Sharpen: sharpest is H20=H20e (46/113 of losers there)
- **Sharp: n=47  W=1/L=46  WR=2.1%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(45/35) | H20e(35/45) |
| H60 | H60a(53/44) | H60e(42/50) |
| T1 | T1a(54/46) | T1c(46/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/46) | short(45/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
