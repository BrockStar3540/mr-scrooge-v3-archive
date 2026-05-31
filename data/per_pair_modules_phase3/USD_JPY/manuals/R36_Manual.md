# USD_JPY — R36 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,686**  (W=1,584 / L=1,102)  -  WR: **59.0%**

## Session distribution

- ny_mid: n=895  W=550/L=345  WR=61.5%
- london_open: n=686  W=396/L=290  WR=57.7%
- asia: n=634  W=360/L=274  WR=56.8%
- ny_close: n=201  W=121/L=80  WR=60.2%
- asia_late: n=132  W=71/L=61  WR=53.8%
- ny_open: n=131  W=82/L=49  WR=62.6%
- london: n=5  W=3/L=2  WR=60.0%
- off_hours: n=2  W=1/L=1  WR=50.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T4=T4c AND BBP=BBP6`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 13/15 losers (87%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band  •  AVOID when session=ny_mid

### W02.  `H60=H60e AND T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 13/15 losers (87%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band  •  AVOID when session=ny_mid

### W03.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude ZS=ZS3 drops 11/15 losers (73%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W04.  `H60=H60a AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=102  W=92/L=10  WR=90.2%
- Refine: exclude ZS=ZS3 drops 9/10 losers (90%)
- **Final: n=81  W=80/L=1  WR=98.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W05.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude H20=H20a drops 9/15 losers (60%)
- **Final: n=54  W=48/L=6  WR=88.9%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W06.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude H20=H20a drops 9/15 losers (60%)
- **Final: n=54  W=48/L=6  WR=88.9%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W07.  `T1=T1a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude H20=H20b drops 2/12 losers (17%)
- **Final: n=91  W=81/L=10  WR=89.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W08.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude H20=H20b drops 2/12 losers (17%)
- **Final: n=91  W=81/L=10  WR=89.0%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W09.  `H20=H20a AND H60=H60d AND session_bucket=london_open`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude T1=T1c drops 9/11 losers (82%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; session=london_open  •  AVOID when 1h trend AGAINST trade

### W10.  `H60=H60d AND T4=T4a AND session_bucket=london_open`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude T1=T1c drops 9/11 losers (82%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend WITH trade; session=london_open  •  AVOID when 1h trend AGAINST trade

### W11.  `H20=H20a AND H60=H60d AND T4=T4a AND session_bucket=london_open`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude T1=T1c drops 9/11 losers (82%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend WITH trade; session=london_open  •  AVOID when 1h trend AGAINST trade

### W12.  `BBP=BBP5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude H20=H20e drops 8/9 losers (89%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: LONG**  •  just touched upper band; session=ny_mid  •  AVOID when HTF20 strongly against

### W13.  `BBP=BBP5 AND ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude H20=H20e drops 8/9 losers (89%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: LONG**  •  just touched upper band; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 strongly against

### W14.  `H60=H60a AND ZS=ZS4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude RSI=RSI4 drops 6/7 losers (86%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W15.  `T1=T1a AND BBP=BBP5 AND session_bucket=ny_mid`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude H20=H20e drops 8/11 losers (73%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; session=ny_mid  •  AVOID when HTF20 strongly against

### W16.  `T1=T1a AND BBP=BBP5 AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude H20=H20e drops 8/11 losers (73%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 strongly against

### W17.  `H20=H20a AND T1=T1a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude T4=T4a drops 11/11 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; just touched upper band; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W18.  `H20=H20a AND BBP=BBP5 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude T4=T4a drops 11/11 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; just touched upper band; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W19.  `H60=H60a AND T1=T1a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude T4=T4a drops 11/11 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; just touched upper band; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W20.  `H60=H60a AND BBP=BBP5 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude T4=T4a drops 11/11 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; just touched upper band; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W21.  `H20=H20a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=74  W=70/L=4  WR=94.6%
- Refine: exclude BBP=BBP5 drops 3/4 losers (75%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when just touched upper band

### W22.  `T1=T1a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=74  W=70/L=4  WR=94.6%
- Refine: exclude BBP=BBP5 drops 3/4 losers (75%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when just touched upper band

### W23.  `T4=T4a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=74  W=70/L=4  WR=94.6%
- Refine: exclude BBP=BBP5 drops 3/4 losers (75%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when just touched upper band

### W24.  `RSI=RSI6 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=74  W=70/L=4  WR=94.6%
- Refine: exclude BBP=BBP5 drops 3/4 losers (75%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: LONG**  •  RSI 70-80 overbought; session=london_open  •  AVOID when just touched upper band

### W25.  `H20=H20a AND T1=T1a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=74  W=70/L=4  WR=94.6%
- Refine: exclude BBP=BBP5 drops 3/4 losers (75%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when just touched upper band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T4=T4c AND session_bucket=london_open`
- Raw: n=282  W=111/L=171  WR=39.4%
- Sharpen: sharpest is RSI=RSI6 (57/171 of losers there)
- **Sharp: n=62  W=5/L=57  WR=8.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 70-80 overbought

### L02.  `H20=H20e AND T1=T1c AND session_bucket=london_open`
- Raw: n=195  W=65/L=130  WR=33.3%
- Sharpen: sharpest is RSI=RSI6 (57/130 of losers there)
- **Sharp: n=62  W=5/L=57  WR=8.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 70-80 overbought

### L03.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=195  W=65/L=130  WR=33.3%
- Sharpen: sharpest is RSI=RSI6 (57/130 of losers there)
- **Sharp: n=62  W=5/L=57  WR=8.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 70-80 overbought

### L04.  `RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=183  W=63/L=120  WR=34.4%
- Sharpen: sharpest is BBP=BBP6 (29/120 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: LONG**  •  RSI 60-70 strong; session=london_open  •  ONLY when deep above upper band

### L05.  `H20=H20e AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=173  W=64/L=109  WR=37.0%
- Sharpen: sharpest is T1=T1c (82/109 of losers there)
- **Sharp: n=107  W=25/L=82  WR=23.4%**
- **Dir: ?**  •  HTF20 strongly against; upper third; session=london_open  •  ONLY when 1h trend AGAINST trade

### L06.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=173  W=64/L=109  WR=37.0%
- Sharpen: sharpest is T1=T1c (82/109 of losers there)
- **Sharp: n=107  W=25/L=82  WR=23.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; session=london_open  •  ONLY when 1h trend AGAINST trade

### L07.  `H20=H20e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=165  W=55/L=110  WR=33.3%
- Sharpen: sharpest is RSI=RSI6 (57/110 of losers there)
- **Sharp: n=62  W=5/L=57  WR=8.1%**
- **Dir: SHORT**  •  HTF20 strongly against; session=london_open  •  ONLY when RSI 70-80 overbought

### L08.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=165  W=55/L=110  WR=33.3%
- Sharpen: sharpest is RSI=RSI6 (57/110 of losers there)
- **Sharp: n=62  W=5/L=57  WR=8.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 70-80 overbought

### L09.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=165  W=55/L=110  WR=33.3%
- Sharpen: sharpest is RSI=RSI6 (57/110 of losers there)
- **Sharp: n=62  W=5/L=57  WR=8.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 70-80 overbought

### L10.  `T1=T1c AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=157  W=59/L=98  WR=37.6%
- Sharpen: sharpest is H20=H20e (81/98 of losers there)
- **Sharp: n=100  W=19/L=81  WR=19.0%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=london_open  •  ONLY when HTF20 strongly against

### L11.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=157  W=59/L=98  WR=37.6%
- Sharpen: sharpest is H20=H20e (81/98 of losers there)
- **Sharp: n=100  W=19/L=81  WR=19.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=london_open  •  ONLY when HTF20 strongly against

### L12.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=153  W=53/L=100  WR=34.6%
- Sharpen: sharpest is BBP=BBP6 (29/100 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=london_open  •  ONLY when deep above upper band

### L13.  `H20=H20e AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=146  W=51/L=95  WR=34.9%
- Sharpen: sharpest is T1=T1c (81/95 of losers there)
- **Sharp: n=100  W=19/L=81  WR=19.0%**
- **Dir: ?**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=london_open  •  ONLY when 1h trend AGAINST trade

### L14.  `H20=H20e AND T4=T4c AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=146  W=51/L=95  WR=34.9%
- Sharpen: sharpest is T1=T1c (81/95 of losers there)
- **Sharp: n=100  W=19/L=81  WR=19.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought; session=london_open  •  ONLY when 1h trend AGAINST trade

### L15.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=146  W=51/L=95  WR=34.9%
- Sharpen: sharpest is T1=T1c (81/95 of losers there)
- **Sharp: n=100  W=19/L=81  WR=19.0%**
- **Dir: ?**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought; session=london_open  •  ONLY when 1h trend AGAINST trade

### L16.  `H60=H60e AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=133  W=44/L=89  WR=33.1%
- Sharpen: sharpest is T1=T1c (71/89 of losers there)
- **Sharp: n=92  W=21/L=71  WR=22.8%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=london_open  •  ONLY when 1h trend AGAINST trade

### L17.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=133  W=44/L=89  WR=33.1%
- Sharpen: sharpest is T1=T1c (71/89 of losers there)
- **Sharp: n=92  W=21/L=71  WR=22.8%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=london_open  •  ONLY when 1h trend AGAINST trade

### L18.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=132  W=47/L=85  WR=35.6%
- Sharpen: sharpest is H20=H20e (82/85 of losers there)
- **Sharp: n=107  W=25/L=82  WR=23.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; session=london_open  •  ONLY when HTF20 strongly against

### L19.  `H60=H60a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is ZS=ZS6 (34/80 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L20.  `BBP=BBP6 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=127  W=47/L=80  WR=37.0%
- Sharpen: sharpest is session_bucket=london_open (29/80 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: LONG**  •  deep above upper band; RSI 60-70 strong  •  ONLY when session=london_open

### L21.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is T1=T1c (67/76 of losers there)
- **Sharp: n=92  W=25/L=67  WR=27.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; session=london_open  •  ONLY when 1h trend AGAINST trade

### L22.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is T1=T1c (67/76 of losers there)
- **Sharp: n=92  W=25/L=67  WR=27.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; session=london_open  •  ONLY when 1h trend AGAINST trade

### L23.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=120  W=47/L=73  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=120  W=47/L=73  WR=39.2%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong; session=london_open

### L24.  `T1=T1c AND T4=T4c AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=119  W=37/L=82  WR=31.1%
- Sharpen: sharpest is H20=H20e (81/82 of losers there)
- **Sharp: n=100  W=19/L=81  WR=19.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought; session=london_open  •  ONLY when HTF20 strongly against

### L25.  `T1=T1a AND BBP=BBP6 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=118  W=47/L=71  WR=39.8%
- Sharpen: sharpest is session_bucket=london_open (29/71 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band; RSI 60-70 strong  •  ONLY when session=london_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(47/38) | H20e(38/47) |
| H60 | H60a(49/41) | H60e(40/47) |
| T1 | T1a(53/46) | T1c(47/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
