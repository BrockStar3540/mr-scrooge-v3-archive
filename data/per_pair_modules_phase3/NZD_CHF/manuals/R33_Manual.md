# NZD_CHF — R33 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **634**  (W=422 / L=212)  -  WR: **66.6%**

## Session distribution

- asia: n=257  W=169/L=88  WR=65.8%
- london_open: n=144  W=91/L=53  WR=63.2%
- london: n=58  W=42/L=16  WR=72.4%
- ny_open: n=52  W=37/L=15  WR=71.2%
- ny_close: n=48  W=34/L=14  WR=70.8%
- ny_mid: n=40  W=26/L=14  WR=65.0%
- off_hours: n=32  W=21/L=11  WR=65.6%
- asia_late: n=3  W=2/L=1  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T4=T4c AND RSI=RSI4`
- Raw: n=125  W=107/L=18  WR=85.6%
- Refine: exclude session_bucket=london drops 9/18 losers (50%)
- **Final: n=110  W=101/L=9  WR=91.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=london

### W02.  `H20=H20e AND T1=T1c AND T4=T4c`
- Raw: n=111  W=100/L=11  WR=90.1%
- Refine: exclude H60=H60a drops 3/11 losers (27%)
- **Final: n=108  W=100/L=8  WR=92.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when HTF60 aligned WITH trade

### W03.  `H20=H20e AND H60=H60e AND RSI=RSI4`
- Raw: n=110  W=95/L=15  WR=86.4%
- Refine: exclude session_bucket=london drops 9/15 losers (60%)
- **Final: n=95  W=89/L=6  WR=93.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral  •  AVOID when session=london

### W04.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI4`
- Raw: n=110  W=95/L=15  WR=86.4%
- Refine: exclude session_bucket=london drops 9/15 losers (60%)
- **Final: n=95  W=89/L=6  WR=93.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=london

### W05.  `H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=107  W=95/L=12  WR=88.8%
- Refine: exclude session_bucket=ny_mid drops 6/12 losers (50%)
- **Final: n=99  W=93/L=6  WR=93.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_mid

### W06.  `H20=H20e AND T4=T4c AND session_bucket=asia`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude T1=T1a drops 11/15 losers (73%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when 1h trend WITH trade

### W07.  `H20=H20e AND H60=H60e AND T1=T1c`
- Raw: n=99  W=94/L=5  WR=94.9%
- Refine: exclude session_bucket=ny_mid drops 2/5 losers (40%)
- **Final: n=95  W=92/L=3  WR=96.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when session=ny_mid

### W08.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=99  W=94/L=5  WR=94.9%
- Refine: exclude session_bucket=ny_mid drops 2/5 losers (40%)
- **Final: n=95  W=92/L=3  WR=96.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_mid

### W09.  `T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude session_bucket=london drops 9/13 losers (69%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=london

### W10.  `H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude T1=T1a drops 13/13 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when 1h trend WITH trade

### W11.  `H20=H20e AND H60=H60e AND session_bucket=asia`
- Raw: n=91  W=80/L=11  WR=87.9%
- Refine: exclude T1=T1a drops 11/11 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  AVOID when 1h trend WITH trade

### W12.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=91  W=80/L=11  WR=87.9%
- Refine: exclude T1=T1a drops 11/11 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when 1h trend WITH trade

### W13.  `H20=H20e AND T4=T4c AND BBP=BBP4`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude session_bucket=london drops 6/12 losers (50%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third  •  AVOID when session=london

### W14.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude session_bucket=london drops 6/12 losers (50%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought  •  AVOID when session=london

### W15.  `T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude H60=H60d drops 5/10 losers (50%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=asia  •  AVOID when HTF60 mildly against

### W16.  `H20=H20e AND H60=H60e AND direction_exec=short`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude BBP=BBP0 drops 6/11 losers (55%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against  •  AVOID when deep below lower band

### W17.  `H20=H20e AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude BBP=BBP0 drops 6/11 losers (55%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when deep below lower band

### W18.  `H20=H20e AND H60=H60e AND BBP=BBP4`
- Raw: n=73  W=64/L=9  WR=87.7%
- Refine: exclude session_bucket=london drops 6/9 losers (67%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third  •  AVOID when session=london

### W19.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP4`
- Raw: n=73  W=64/L=9  WR=87.7%
- Refine: exclude session_bucket=london drops 6/9 losers (67%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; upper third  •  AVOID when session=london

### W20.  `H20=H20e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude H60=H60d drops 3/6 losers (50%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when HTF60 mildly against

### W21.  `H20=H20e AND T1=T1c AND session_bucket=asia`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude H60=H60c drops 5/9 losers (56%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when HTF60 neutral

### W22.  `H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude H20=H20a drops 6/9 losers (67%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when HTF20 aligned WITH trade

### W23.  `H60=H60e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=67  W=59/L=8  WR=88.1%
- Refine: exclude session_bucket=ny_mid drops 6/8 losers (75%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_mid

### W24.  `H20=H20e AND H60=H60e AND ZS=ZS4`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude session_bucket=london drops 6/9 losers (67%)
- **Final: n=55  W=52/L=3  WR=94.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +1 to +2 overbought  •  AVOID when session=london

### W25.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS4`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude session_bucket=london drops 6/9 losers (67%)
- **Final: n=55  W=52/L=3  WR=94.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T1=T1a AND T4=T4a`
- Raw: n=94  W=34/L=60  WR=36.2%
- Sharpen: sharpest is H60=H60a (49/60 of losers there)
- **Sharp: n=66  W=17/L=49  WR=25.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF60 aligned WITH trade

### L02.  `H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is session_bucket=asia (27/50 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when session=asia

### L03.  `H20=H20a AND H60=H60a AND T1=T1a`
- Raw: n=66  W=17/L=49  WR=25.8%
- Sharpen: sharpest is session_bucket=asia (27/49 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when session=asia

### L04.  `H20=H20a AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=66  W=17/L=49  WR=25.8%
- Sharpen: sharpest is session_bucket=asia (27/49 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when session=asia

### L05.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=60  W=19/L=41  WR=31.7%
- Sharpen: sharpest is H60=H60a (30/41 of losers there)
- **Sharp: n=36  W=6/L=30  WR=16.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF60 aligned WITH trade

### L06.  `H20=H20a AND T4=T4a AND session_bucket=london_open`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is ZS=ZS1 (13/36 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L07.  `H20=H20a AND T1=T1a AND RSI=RSI3`
- Raw: n=53  W=18/L=35  WR=34.0%
- Sharpen: sharpest is H60=H60a (28/35 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L08.  `T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=51  W=17/L=34  WR=33.3%
- Sharpen: sharpest is H60=H60a (27/34 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L09.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=49  W=14/L=35  WR=28.6%
- Sharpen: sharpest is session_bucket=asia (26/35 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L10.  `H20=H20a AND T1=T1a AND session_bucket=asia`
- Raw: n=49  W=15/L=34  WR=30.6%
- Sharpen: sharpest is H60=H60a (27/34 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L11.  `H20=H20a AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=46  W=16/L=30  WR=34.8%
- Sharpen: sharpest is H60=H60a (23/30 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L12.  `H20=H20a AND H60=H60a AND direction_exec=short AND session_bucket=asia`
- Raw: n=46  W=18/L=28  WR=39.1%
- Sharpen: sharpest is T1=T1a (18/28 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia  •  ONLY when 1h trend WITH trade

### L13.  `H60=H60a AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=46  W=18/L=28  WR=39.1%
- Sharpen: sharpest is T1=T1a (18/28 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  ONLY when 1h trend WITH trade

### L14.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=45  W=11/L=34  WR=24.4%
- Sharpen: sharpest is H60=H60a (27/34 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L15.  `H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is H20=H20a (30/31 of losers there)
- **Sharp: n=36  W=6/L=30  WR=16.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when HTF20 aligned WITH trade

### L16.  `H60=H60a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=43  W=12/L=31  WR=27.9%
- Sharpen: sharpest is H20=H20a (30/31 of losers there)
- **Sharp: n=36  W=6/L=30  WR=16.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF20 aligned WITH trade

### L17.  `H20=H20a AND H60=H60a AND session_bucket=london_open`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is ZS=ZS1 (12/28 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L18.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=london_open`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is ZS=ZS1 (12/28 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=40  W=15/L=25  WR=37.5%
- Sharpen: sharpest is H60=H60a (18/25 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L20.  `H60=H60a AND T1=T1a AND RSI=RSI3`
- Raw: n=38  W=9/L=29  WR=23.7%
- Sharpen: sharpest is H20=H20a (28/29 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L21.  `H20=H20a AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=38  W=13/L=25  WR=34.2%
- Sharpen: sharpest is H60=H60a (18/25 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L22.  `H20=H20a AND H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=36  W=6/L=30  WR=16.7%
- Sharpen: sharpest is session_bucket=asia (18/30 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when session=asia

### L23.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=36  W=7/L=29  WR=19.4%
- Sharpen: sharpest is session_bucket=asia (23/29 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L24.  `H20=H20a AND T4=T4a AND ZS=ZS1`
- Raw: n=35  W=3/L=32  WR=8.6%
- Sharpen: sharpest is direction_exec=short (20/32 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when short

### L25.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=35  W=9/L=26  WR=25.7%
- Sharpen: sharpest is H20=H20a (26/26 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF20 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(49/27) | H20a(34/57) |
| H60 | H60e(45/23) | H60a(27/49) |
| T1 | — | — |
| T4 | T4c(62/30) | T4a(38/70) |
| BBP | — | BBP0(9/14) |
| RSI | RSI4(49/42) | RSI3(49/56) |
| ZS | — | ZS1(12/20) |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
