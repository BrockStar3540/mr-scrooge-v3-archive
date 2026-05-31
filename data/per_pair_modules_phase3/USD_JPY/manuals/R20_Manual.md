# USD_JPY — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,988**  (W=2,457 / L=1,531)  -  WR: **61.6%**

## Session distribution

- asia: n=1356  W=843/L=513  WR=62.2%
- ny_mid: n=872  W=534/L=338  WR=61.2%
- london_open: n=585  W=373/L=212  WR=63.8%
- ny_open: n=441  W=264/L=177  WR=59.9%
- ny_close: n=420  W=252/L=168  WR=60.0%
- asia_late: n=201  W=123/L=78  WR=61.2%
- london: n=74  W=45/L=29  WR=60.8%
- off_hours: n=39  W=23/L=16  WR=59.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=249  W=212/L=37  WR=85.1%
- Refine: exclude T4=T4c drops 25/37 losers (68%)
- **Final: n=140  W=128/L=12  WR=91.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when 4h trend AGAINST trade

### W02.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=212  W=189/L=23  WR=89.2%
- Refine: exclude session_bucket=ny_mid drops 12/23 losers (52%)
- **Final: n=173  W=162/L=11  WR=93.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W03.  `H60=H60a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=212  W=189/L=23  WR=89.2%
- Refine: exclude session_bucket=ny_mid drops 12/23 losers (52%)
- **Final: n=173  W=162/L=11  WR=93.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W04.  `H60=H60a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=174  W=151/L=23  WR=86.8%
- Refine: exclude H20=H20a drops 23/23 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched upper band; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W05.  `H60=H60a AND BBP=BBP5 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=174  W=151/L=23  WR=86.8%
- Refine: exclude H20=H20a drops 23/23 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W06.  `H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=160  W=136/L=24  WR=85.0%
- Refine: exclude T4=T4a drops 10/24 losers (42%)
- **Final: n=139  W=125/L=14  WR=89.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when 4h trend WITH trade

### W07.  `H60=H60a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=160  W=136/L=24  WR=85.0%
- Refine: exclude T4=T4a drops 10/24 losers (42%)
- **Final: n=139  W=125/L=14  WR=89.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_open  •  AVOID when 4h trend WITH trade

### W08.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=160  W=136/L=24  WR=85.0%
- Refine: exclude T4=T4a drops 10/24 losers (42%)
- **Final: n=139  W=125/L=14  WR=89.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when 4h trend WITH trade

### W09.  `H20=H20a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=153  W=136/L=17  WR=88.9%
- Refine: exclude T4=T4a drops 10/17 losers (59%)
- **Final: n=132  W=125/L=7  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when 4h trend WITH trade

### W10.  `H20=H20a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=153  W=136/L=17  WR=88.9%
- Refine: exclude T4=T4a drops 10/17 losers (59%)
- **Final: n=132  W=125/L=7  WR=94.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_open  •  AVOID when 4h trend WITH trade

### W11.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=153  W=136/L=17  WR=88.9%
- Refine: exclude T4=T4a drops 10/17 losers (59%)
- **Final: n=132  W=125/L=7  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when 4h trend WITH trade

### W12.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=153  W=136/L=17  WR=88.9%
- Refine: exclude T4=T4a drops 10/17 losers (59%)
- **Final: n=132  W=125/L=7  WR=94.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  AVOID when 4h trend WITH trade

### W13.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=153  W=136/L=17  WR=88.9%
- Refine: exclude T4=T4a drops 10/17 losers (59%)
- **Final: n=132  W=125/L=7  WR=94.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when 4h trend WITH trade

### W14.  `H60=H60a AND T1=T1a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=144  W=128/L=16  WR=88.9%
- Refine: exclude H20=H20a drops 16/16 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; just touched upper band; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W15.  `H60=H60a AND BBP=BBP5 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=144  W=128/L=16  WR=88.9%
- Refine: exclude H20=H20a drops 16/16 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; just touched upper band; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W16.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=140  W=128/L=12  WR=91.4%
- Refine: exclude session_bucket=ny_open drops 6/12 losers (50%)
- **Final: n=134  W=128/L=6  WR=95.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W17.  `T1=T1a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=139  W=125/L=14  WR=89.9%
- Refine: exclude ZS=ZS3 drops 9/14 losers (64%)
- **Final: n=126  W=121/L=5  WR=96.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W18.  `T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=139  W=125/L=14  WR=89.9%
- Refine: exclude ZS=ZS3 drops 9/14 losers (64%)
- **Final: n=126  W=121/L=5  WR=96.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W19.  `H60=H60a AND T1=T1a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=139  W=125/L=14  WR=89.9%
- Refine: exclude ZS=ZS3 drops 9/14 losers (64%)
- **Final: n=126  W=121/L=5  WR=96.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W20.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=139  W=125/L=14  WR=89.9%
- Refine: exclude ZS=ZS3 drops 9/14 losers (64%)
- **Final: n=126  W=121/L=5  WR=96.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W21.  `T1=T1a AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=139  W=125/L=14  WR=89.9%
- Refine: exclude ZS=ZS3 drops 9/14 losers (64%)
- **Final: n=126  W=121/L=5  WR=96.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W22.  `H20=H20a AND T1=T1a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=132  W=125/L=7  WR=94.7%
- Refine: exclude BBP=BBP3 drops 3/7 losers (43%)
- **Final: n=127  W=123/L=4  WR=96.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when middle of band

### W23.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=132  W=125/L=7  WR=94.7%
- Refine: exclude BBP=BBP3 drops 3/7 losers (43%)
- **Final: n=127  W=123/L=4  WR=96.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when middle of band

### W24.  `H60=H60a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=129  W=110/L=19  WR=85.3%
- Refine: exclude ZS=ZS3 drops 9/19 losers (47%)
- **Final: n=108  W=98/L=10  WR=90.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore -1 to +1 neutral

### W25.  `H60=H60a AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=126  W=109/L=17  WR=86.5%
- Refine: exclude RSI=RSI4 drops 12/17 losers (71%)
- **Final: n=86  W=81/L=5  WR=94.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -1 to +1 neutral; session=asia  •  AVOID when RSI 50-60 upper neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND session_bucket=asia`
- Raw: n=508  W=203/L=305  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=508  W=203/L=305  WR=40.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=asia

### L02.  `H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=500  W=193/L=307  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=500  W=193/L=307  WR=38.6%**
- **Dir: SHORT**  •  HTF60 strongly against; session=asia

### L03.  `H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=478  W=189/L=289  WR=39.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=478  W=189/L=289  WR=39.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=asia

### L04.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=478  W=189/L=289  WR=39.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=478  W=189/L=289  WR=39.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=asia

### L05.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=466  W=183/L=283  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=466  W=183/L=283  WR=39.3%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=asia

### L06.  `H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=438  W=171/L=267  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=438  W=171/L=267  WR=39.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia

### L07.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=438  W=171/L=267  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=438  W=171/L=267  WR=39.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=asia

### L08.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=438  W=171/L=267  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=438  W=171/L=267  WR=39.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia

### L09.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=432  W=171/L=261  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=432  W=171/L=261  WR=39.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia

### L10.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=332  W=130/L=202  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=332  W=130/L=202  WR=39.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=asia

### L11.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=332  W=130/L=202  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=332  W=130/L=202  WR=39.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=asia

### L12.  `H60=H60e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=309  W=120/L=189  WR=38.8%
- Sharpen: sharpest is ZS=ZS5 (57/189 of losers there)
- **Sharp: n=71  W=14/L=57  WR=19.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L13.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=309  W=120/L=189  WR=38.8%
- Sharpen: sharpest is ZS=ZS5 (57/189 of losers there)
- **Sharp: n=71  W=14/L=57  WR=19.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L14.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=309  W=120/L=189  WR=38.8%
- Sharpen: sharpest is ZS=ZS5 (57/189 of losers there)
- **Sharp: n=71  W=14/L=57  WR=19.7%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L15.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=303  W=114/L=189  WR=37.6%
- Sharpen: sharpest is ZS=ZS5 (57/189 of losers there)
- **Sharp: n=71  W=14/L=57  WR=19.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `H60=H60e AND T1=T1c AND ZS=ZS5`
- Raw: n=302  W=112/L=190  WR=37.1%
- Sharpen: sharpest is RSI=RSI5 (142/190 of losers there)
- **Sharp: n=192  W=50/L=142  WR=26.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L17.  `H60=H60e AND ZS=ZS5 AND direction_exec=short`
- Raw: n=302  W=112/L=190  WR=37.1%
- Sharpen: sharpest is RSI=RSI5 (142/190 of losers there)
- **Sharp: n=192  W=50/L=142  WR=26.0%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L18.  `H60=H60e AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=302  W=112/L=190  WR=37.1%
- Sharpen: sharpest is RSI=RSI5 (142/190 of losers there)
- **Sharp: n=192  W=50/L=142  WR=26.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L19.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=291  W=106/L=185  WR=36.4%
- Sharpen: sharpest is ZS=ZS5 (57/185 of losers there)
- **Sharp: n=71  W=14/L=57  WR=19.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L20.  `H60=H60e AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=248  W=94/L=154  WR=37.9%
- Sharpen: sharpest is RSI=RSI5 (105/154 of losers there)
- **Sharp: n=137  W=32/L=105  WR=23.4%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L21.  `H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=230  W=85/L=145  WR=37.0%
- Sharpen: sharpest is RSI=RSI5 (105/145 of losers there)
- **Sharp: n=137  W=32/L=105  WR=23.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L22.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=230  W=85/L=145  WR=37.0%
- Sharpen: sharpest is RSI=RSI5 (105/145 of losers there)
- **Sharp: n=137  W=32/L=105  WR=23.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L23.  `H60=H60e AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=230  W=85/L=145  WR=37.0%
- Sharpen: sharpest is RSI=RSI5 (105/145 of losers there)
- **Sharp: n=137  W=32/L=105  WR=23.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L24.  `H60=H60e AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=213  W=59/L=154  WR=27.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=213  W=59/L=154  WR=27.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; zscore +2 to +3 deep overbought

### L25.  `H60=H60e AND T1=T1c AND BBP=BBP5`
- Raw: n=209  W=74/L=135  WR=35.4%
- Sharpen: sharpest is RSI=RSI5 (93/135 of losers there)
- **Sharp: n=123  W=30/L=93  WR=24.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched upper band  •  ONLY when RSI 60-70 strong

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(51/38) | H20e(37/51) |
| H60 | H60a(53/34) | H60e(36/53) |
| T1 | T1a(60/38) | T1c(40/62) |
| T4 | T4a(56/43) | T4c(44/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(61/37) | short(39/63) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
