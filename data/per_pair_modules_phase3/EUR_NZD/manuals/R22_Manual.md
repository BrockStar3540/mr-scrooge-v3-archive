# EUR_NZD — R22 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,773**  (W=1,698 / L=1,075)  -  WR: **61.2%**

## Session distribution

- asia: n=1018  W=616/L=402  WR=60.5%
- ny_close: n=902  W=559/L=343  WR=62.0%
- london: n=227  W=135/L=92  WR=59.5%
- ny_open: n=181  W=116/L=65  WR=64.1%
- london_open: n=123  W=78/L=45  WR=63.4%
- off_hours: n=118  W=57/L=61  WR=48.3%
- asia_late: n=112  W=76/L=36  WR=67.9%
- ny_mid: n=92  W=61/L=31  WR=66.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude T1=T1c drops 8/14 losers (57%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when 1h trend AGAINST trade

### W02.  `H60=H60a AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude ZS=ZS3 drops 6/13 losers (46%)
- **Final: n=86  W=79/L=7  WR=91.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 70-80 overbought  •  AVOID when zscore -1 to +1 neutral

### W03.  `H60=H60a AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=86  W=79/L=7  WR=91.9%
- Refine: exclude H20=H20e drops 6/7 losers (86%)
- **Final: n=65  W=64/L=1  WR=98.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W04.  `H60=H60a AND BBP=BBP4 AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=86  W=79/L=7  WR=91.9%
- Refine: exclude H20=H20e drops 6/7 losers (86%)
- **Final: n=65  W=64/L=1  WR=98.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 70-80 overbought; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W05.  `H20=H20e AND H60=H60a AND RSI=RSI4`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=london drops 9/10 losers (90%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when session=london

### W06.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude RSI=RSI5 drops 11/11 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 60-70 strong

### W07.  `T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude RSI=RSI5 drops 11/11 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_open  •  AVOID when RSI 60-70 strong

### W08.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude RSI=RSI5 drops 11/11 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 60-70 strong

### W09.  `H20=H20a AND H60=H60e AND T1=T1a AND ZS=ZS5`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude BBP=BBP6 drops 6/11 losers (55%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W10.  `H20=H20a AND H60=H60e AND ZS=ZS5 AND direction_exec=long`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude BBP=BBP6 drops 6/11 losers (55%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W11.  `H20=H20d AND T4=T4a AND RSI=RSI6`
- Raw: n=72  W=69/L=3  WR=95.8%
- Refine: exclude session_bucket=ny_mid drops 3/3 losers (100%)
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W12.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=71  W=65/L=6  WR=91.5%
- Refine: exclude H20=H20a drops 6/6 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W13.  `T4=T4a AND RSI=RSI6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=71  W=65/L=6  WR=91.5%
- Refine: exclude H20=H20a drops 6/6 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W14.  `H60=H60a AND T4=T4a AND RSI=RSI6`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when zscore -1 to +1 neutral

### W15.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI6`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when zscore -1 to +1 neutral

### W16.  `H60=H60a AND T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when zscore -1 to +1 neutral

### W17.  `H20=H20a AND H60=H60e AND ZS=ZS5 AND session_bucket=ny_close`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude BBP=BBP5 drops 7/7 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; zscore +2 to +3 deep overbought; session=ny_close  •  AVOID when just touched upper band

### W18.  `H20=H20e AND H60=H60a AND session_bucket=london`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude RSI=RSI4 drops 9/9 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=london  •  AVOID when RSI 50-60 upper neutral

### W19.  `T1=T1c AND T4=T4c AND BBP=BBP3 AND session_bucket=asia`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude strategy_id=bravo_failed_momentum drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; middle of band; session=asia  •  AVOID when strategy=bravo_failed_momentum

### W20.  `T4=T4c AND BBP=BBP3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude strategy_id=bravo_failed_momentum drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; middle of band; session=asia  •  AVOID when strategy=bravo_failed_momentum

### W21.  `H20=H20e AND RSI=RSI5 AND session_bucket=london`
- Raw: n=64  W=64/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; session=london

### W22.  `T1=T1a AND BBP=BBP5 AND session_bucket=asia`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude H20=H20e drops 8/8 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; session=asia  •  AVOID when HTF20 strongly against

### W23.  `BBP=BBP5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude H20=H20e drops 8/8 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: LONG**  •  just touched upper band; session=asia  •  AVOID when HTF20 strongly against

### W24.  `T1=T1a AND BBP=BBP5 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude H20=H20e drops 8/8 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 strongly against

### W25.  `T1=T1a AND BBP=BBP5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude H20=H20e drops 8/8 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; just touched upper band; session=asia  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=111  W=39/L=72  WR=35.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=111  W=39/L=72  WR=35.1%**
- **Dir: ?**  •  1h trend WITH trade; zscore -1 to +1 neutral; session=asia

### L02.  `ZS=ZS3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=111  W=39/L=72  WR=35.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=111  W=39/L=72  WR=35.1%**
- **Dir: LONG**  •  zscore -1 to +1 neutral; session=asia

### L03.  `T1=T1a AND ZS=ZS3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=111  W=39/L=72  WR=35.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=111  W=39/L=72  WR=35.1%**
- **Dir: LONG**  •  1h trend WITH trade; zscore -1 to +1 neutral; session=asia

### L04.  `T4=T4c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=105  W=37/L=68  WR=35.2%
- Sharpen: sharpest is T1=T1c (58/68 of losers there)
- **Sharp: n=76  W=18/L=58  WR=23.7%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when 1h trend AGAINST trade

### L05.  `T1=T1c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=98  W=28/L=70  WR=28.6%
- Sharpen: sharpest is H60=H60a (34/70 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF60 aligned WITH trade

### L06.  `ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=98  W=28/L=70  WR=28.6%
- Sharpen: sharpest is H60=H60a (34/70 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: SHORT**  •  zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF60 aligned WITH trade

### L07.  `T1=T1c AND ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=98  W=28/L=70  WR=28.6%
- Sharpen: sharpest is H60=H60a (34/70 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF60 aligned WITH trade

### L08.  `H20=H20b AND T1=T1c AND T4=T4c`
- Raw: n=95  W=34/L=61  WR=35.8%
- Sharpen: sharpest is session_bucket=asia (23/61 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L09.  `H20=H20b AND H60=H60e AND T4=T4c`
- Raw: n=91  W=33/L=58  WR=36.3%
- Sharpen: sharpest is session_bucket=asia (23/58 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=asia

### L10.  `H20=H20b AND T4=T4c AND direction_exec=short`
- Raw: n=91  W=33/L=58  WR=36.3%
- Sharpen: sharpest is session_bucket=asia (23/58 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend AGAINST trade  •  ONLY when session=asia

### L11.  `H20=H20b AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=91  W=33/L=58  WR=36.3%
- Sharpen: sharpest is session_bucket=asia (23/58 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L12.  `H20=H20b AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=91  W=33/L=58  WR=36.3%
- Sharpen: sharpest is session_bucket=asia (23/58 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=asia

### L13.  `H20=H20b AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=91  W=33/L=58  WR=36.3%
- Sharpen: sharpest is session_bucket=asia (23/58 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L14.  `H20=H20e AND T1=T1c AND BBP=BBP5`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is H60=H60a (34/54 of losers there)
- **Sharp: n=46  W=12/L=34  WR=26.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; just touched upper band  •  ONLY when HTF60 aligned WITH trade

### L15.  `H20=H20e AND BBP=BBP5 AND direction_exec=short`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is H60=H60a (34/54 of losers there)
- **Sharp: n=46  W=12/L=34  WR=26.1%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched upper band  •  ONLY when HTF60 aligned WITH trade

### L16.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP5`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is H60=H60a (34/54 of losers there)
- **Sharp: n=46  W=12/L=34  WR=26.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band  •  ONLY when HTF60 aligned WITH trade

### L17.  `H20=H20e AND T1=T1c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is H60=H60a (34/54 of losers there)
- **Sharp: n=46  W=12/L=34  WR=26.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L18.  `H20=H20e AND T1=T1c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is H60=H60a (34/54 of losers there)
- **Sharp: n=46  W=12/L=34  WR=26.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; just touched upper band  •  ONLY when HTF60 aligned WITH trade

### L19.  `H20=H20e AND T4=T4c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is H60=H60a (34/54 of losers there)
- **Sharp: n=46  W=12/L=34  WR=26.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched upper band  •  ONLY when HTF60 aligned WITH trade

### L20.  `H20=H20e AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is H60=H60a (34/54 of losers there)
- **Sharp: n=46  W=12/L=34  WR=26.1%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L21.  `H60=H60e AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=85  W=28/L=57  WR=32.9%
- Sharpen: sharpest is session_bucket=asia (35/57 of losers there)
- **Sharp: n=42  W=7/L=35  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 70-80 overbought  •  ONLY when session=asia

### L22.  `T1=T1a AND RSI=RSI5 AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=85  W=29/L=56  WR=34.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=85  W=29/L=56  WR=34.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral; session=asia

### L23.  `RSI=RSI5 AND ZS=ZS3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=85  W=29/L=56  WR=34.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=85  W=29/L=56  WR=34.1%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore -1 to +1 neutral; session=asia

### L24.  `T1=T1c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is H20=H20b (23/50 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when HTF20 slightly aligned

### L25.  `RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is H20=H20b (23/50 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=asia  •  ONLY when HTF20 slightly aligned

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(39/33), H60b(17/12) | H60e(31/39) |
| T1 | T1a(54/45) | T1c(46/55) |
| T4 | T4a(55/45) | T4c(45/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/46) | short(46/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
