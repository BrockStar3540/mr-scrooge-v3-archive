# EUR_CAD — R36 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,146**  (W=1,983 / L=1,163)  -  WR: **63.0%**

## Session distribution

- ny_close: n=1527  W=958/L=569  WR=62.7%
- asia: n=935  W=600/L=335  WR=64.2%
- off_hours: n=233  W=145/L=88  WR=62.2%
- london_open: n=204  W=128/L=76  WR=62.7%
- london: n=102  W=62/L=40  WR=60.8%
- ny_mid: n=67  W=44/L=23  WR=65.7%
- ny_open: n=59  W=34/L=25  WR=57.6%
- asia_late: n=19  W=12/L=7  WR=63.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60d AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=232  W=200/L=32  WR=86.2%
- Refine: exclude H20=H20c drops 10/32 losers (31%)
- **Final: n=218  W=196/L=22  WR=89.9%**
- **Dir: LONG**  •  HTF60 mildly against; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 neutral

### W02.  `H60=H60d AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=216  W=184/L=32  WR=85.2%
- Refine: exclude H20=H20c drops 10/32 losers (31%)
- **Final: n=202  W=180/L=22  WR=89.1%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 neutral

### W03.  `H20=H20b AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=166  W=144/L=22  WR=86.7%
- Refine: exclude T4=T4c drops 15/22 losers (68%)
- **Final: n=93  W=86/L=7  WR=92.5%**
- **Dir: ?**  •  HTF20 slightly aligned; RSI 60-70 strong; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W04.  `H20=H20a AND T4=T4c AND session_bucket=asia`
- Raw: n=155  W=132/L=23  WR=85.2%
- Refine: exclude BBP=BBP2 drops 7/23 losers (30%)
- **Final: n=133  W=117/L=16  WR=88.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when lower third

### W05.  `H20=H20a AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=155  W=132/L=23  WR=85.2%
- Refine: exclude BBP=BBP2 drops 7/23 losers (30%)
- **Final: n=133  W=117/L=16  WR=88.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when lower third

### W06.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=153  W=132/L=21  WR=86.3%
- Refine: exclude BBP=BBP2 drops 6/21 losers (29%)
- **Final: n=132  W=117/L=15  WR=88.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when lower third

### W07.  `H20=H20a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=134  W=114/L=20  WR=85.1%
- Refine: exclude BBP=BBP2 drops 6/20 losers (30%)
- **Final: n=116  W=102/L=14  WR=87.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when lower third

### W08.  `H20=H20b AND H60=H60d AND session_bucket=ny_close`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude T4=T4c drops 11/15 losers (73%)
- **Final: n=82  W=78/L=4  WR=95.1%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 mildly against; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W09.  `H20=H20b AND H60=H60d AND T1=T1a AND session_bucket=ny_close`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude T4=T4c drops 11/15 losers (73%)
- **Final: n=82  W=78/L=4  WR=95.1%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 mildly against; 1h trend WITH trade; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W10.  `H20=H20b AND H60=H60d AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude T4=T4c drops 11/15 losers (73%)
- **Final: n=82  W=78/L=4  WR=95.1%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 mildly against; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W11.  `H20=H20b AND T4=T4a AND session_bucket=ny_close`
- Raw: n=104  W=94/L=10  WR=90.4%
- Refine: exclude H60=H60b drops 6/10 losers (60%)
- **Final: n=82  W=78/L=4  WR=95.1%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; session=ny_close  •  AVOID when HTF60 slightly aligned

### W12.  `H20=H20b AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=104  W=94/L=10  WR=90.4%
- Refine: exclude H60=H60b drops 6/10 losers (60%)
- **Final: n=82  W=78/L=4  WR=95.1%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when HTF60 slightly aligned

### W13.  `H20=H20b AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=104  W=94/L=10  WR=90.4%
- Refine: exclude H60=H60b drops 6/10 losers (60%)
- **Final: n=82  W=78/L=4  WR=95.1%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade; session=ny_close  •  AVOID when HTF60 slightly aligned

### W14.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=99  W=86/L=13  WR=86.9%
- Refine: exclude ZS=ZS2 drops 5/13 losers (38%)
- **Final: n=80  W=72/L=8  WR=90.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore -2 to -1 oversold

### W15.  `H20=H20b AND H60=H60d AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude T4=T4c drops 11/12 losers (92%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 mildly against; RSI 60-70 strong; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W16.  `H20=H20b AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=93  W=86/L=7  WR=92.5%
- Refine: exclude H60=H60b drops 6/7 losers (86%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 60-70 strong; session=ny_close  •  AVOID when HTF60 slightly aligned

### W17.  `H20=H20b AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude T4=T4c drops 6/12 losers (50%)
- **Final: n=61  W=55/L=6  WR=90.2%**
- **Dir: ?**  •  HTF20 slightly aligned; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when 4h trend AGAINST trade

### W18.  `H20=H20b AND H60=H60d AND T4=T4a AND session_bucket=ny_close`
- Raw: n=82  W=78/L=4  WR=95.1%
- Refine: exclude RSI=RSI4 drops 3/4 losers (75%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 mildly against; 4h trend WITH trade; session=ny_close  •  AVOID when RSI 50-60 upper neutral

### W19.  `T4=T4c AND RSI=RSI4 AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=81  W=71/L=10  WR=87.7%
- Refine: exclude strategy_id=charlie_compression_breakout drops 5/10 losers (50%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral; session=asia  •  AVOID when strategy=charlie_compression_breakout

### W20.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude ZS=ZS5 drops 6/11 losers (55%)
- **Final: n=72  W=67/L=5  WR=93.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when zscore +2 to +3 deep overbought

### W21.  `H20=H20a AND T4=T4a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=76  W=71/L=5  WR=93.4%
- Refine: exclude session_bucket=asia drops 5/5 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band; RSI 60-70 strong  •  AVOID when session=asia

### W22.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude ZS=ZS2 drops 5/11 losers (45%)
- **Final: n=57  W=51/L=6  WR=89.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore -2 to -1 oversold

### W23.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude RSI=RSI5 drops 11/11 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when RSI 60-70 strong

### W24.  `H20=H20a AND H60=H60d AND T1=T1a`
- Raw: n=74  W=71/L=3  WR=95.9%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade  •  AVOID when lower third

### W25.  `H20=H20a AND H60=H60d AND T4=T4a`
- Raw: n=74  W=71/L=3  WR=95.9%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend WITH trade  •  AVOID when lower third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60b AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=191  W=75/L=116  WR=39.3%
- Sharpen: sharpest is H20=H20d (45/116 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 4h trend AGAINST trade; session=ny_close  •  ONLY when HTF20 mildly against

### L02.  `H20=H20e AND T1=T1c AND RSI=RSI5`
- Raw: n=180  W=67/L=113  WR=37.2%
- Sharpen: sharpest is H60=H60e (33/113 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L03.  `H20=H20e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=177  W=67/L=110  WR=37.9%
- Sharpen: sharpest is H60=H60e (30/110 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L04.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=177  W=67/L=110  WR=37.9%
- Sharpen: sharpest is H60=H60e (30/110 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L05.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=175  W=67/L=108  WR=38.3%
- Sharpen: sharpest is H60=H60e (30/108 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L06.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=175  W=67/L=108  WR=38.3%
- Sharpen: sharpest is H60=H60e (30/108 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L07.  `T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=57/L=90  WR=38.8%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=asia

### L08.  `H20=H20a AND T4=T4a AND session_bucket=asia`
- Raw: n=140  W=51/L=89  WR=36.4%
- Sharpen: sharpest is BBP=BBP4 (31/89 of losers there)
- **Sharp: n=39  W=8/L=31  WR=20.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  ONLY when upper third

### L09.  `T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=139  W=54/L=85  WR=38.8%
- Sharpen: sharpest is T1=T1a (53/85 of losers there)
- **Sharp: n=59  W=6/L=53  WR=10.2%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L10.  `H20=H20d AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=131  W=50/L=81  WR=38.2%
- Sharpen: sharpest is H60=H60e (30/81 of losers there)
- **Sharp: n=35  W=5/L=30  WR=14.3%**
- **Dir: ?**  •  HTF20 mildly against; RSI 60-70 strong; session=ny_close  •  ONLY when HTF60 strongly against

### L11.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=123  W=49/L=74  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=123  W=49/L=74  WR=39.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia

### L12.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=123  W=49/L=74  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=123  W=49/L=74  WR=39.8%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=asia

### L13.  `H60=H60e AND T4=T4a AND RSI=RSI3`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is T1=T1a (38/60 of losers there)
- **Sharp: n=42  W=4/L=38  WR=9.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L14.  `H60=H60e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is T1=T1a (38/60 of losers there)
- **Sharp: n=42  W=4/L=38  WR=9.5%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L15.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is T1=T1a (38/60 of losers there)
- **Sharp: n=42  W=4/L=38  WR=9.5%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L16.  `T1=T1a AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=95  W=35/L=60  WR=36.8%
- Sharpen: sharpest is ZS=ZS4 (28/60 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: LONG**  •  1h trend WITH trade; session=off_hours  •  ONLY when zscore +1 to +2 overbought

### L17.  `T4=T4a AND ZS=ZS2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is RSI=RSI3 (35/58 of losers there)
- **Sharp: n=39  W=4/L=35  WR=10.3%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -2 to -1 oversold; session=ny_close  •  ONLY when RSI 40-50 lower neutral

### L18.  `H20=H20d AND T4=T4c AND session_bucket=ny_close`
- Raw: n=82  W=30/L=52  WR=36.6%
- Sharpen: sharpest is H60=H60b (45/52 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; session=ny_close  •  ONLY when HTF60 slightly aligned

### L19.  `H20=H20d AND T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=82  W=30/L=52  WR=36.6%
- Sharpen: sharpest is H60=H60b (45/52 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when HTF60 slightly aligned

### L20.  `H20=H20d AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=82  W=30/L=52  WR=36.6%
- Sharpen: sharpest is H60=H60b (45/52 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend AGAINST trade; session=ny_close  •  ONLY when HTF60 slightly aligned

### L21.  `H20=H20d AND H60=H60b AND session_bucket=ny_close`
- Raw: n=80  W=30/L=50  WR=37.5%
- Sharpen: sharpest is T4=T4c (45/50 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 slightly aligned; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L22.  `H20=H20d AND H60=H60b AND T1=T1c AND session_bucket=ny_close`
- Raw: n=80  W=30/L=50  WR=37.5%
- Sharpen: sharpest is T4=T4c (45/50 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 slightly aligned; 1h trend AGAINST trade; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L23.  `H20=H20d AND H60=H60b AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=80  W=30/L=50  WR=37.5%
- Sharpen: sharpest is T4=T4c (45/50 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 slightly aligned; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L24.  `H20=H20a AND T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=78  W=30/L=48  WR=38.5%
- Sharpen: sharpest is session_bucket=ny_close (32/48 of losers there)
- **Sharp: n=37  W=5/L=32  WR=13.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L25.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5 AND session_bucket=ny_close`
- Raw: n=77  W=30/L=47  WR=39.0%
- Sharpen: sharpest is H20=H20e (18/47 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought; session=ny_close  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(13/7) | H20e(32/38) |
| H60 | H60d(18/10) | H60b(12/18) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
