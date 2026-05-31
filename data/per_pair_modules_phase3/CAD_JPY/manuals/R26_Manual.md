# CAD_JPY — R26 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,076**  (W=1,295 / L=781)  -  WR: **62.4%**

## Session distribution

- ny_mid: n=675  W=434/L=241  WR=64.3%
- asia: n=586  W=373/L=213  WR=63.7%
- london_open: n=417  W=256/L=161  WR=61.4%
- ny_open: n=203  W=110/L=93  WR=54.2%
- ny_close: n=128  W=84/L=44  WR=65.6%
- london: n=48  W=27/L=21  WR=56.2%
- off_hours: n=12  W=5/L=7  WR=41.7%
- asia_late: n=7  W=6/L=1  WR=85.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=132  W=113/L=19  WR=85.6%
- Refine: exclude H60=H60e drops 11/19 losers (58%)
- **Final: n=96  W=88/L=8  WR=91.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF60 strongly against

### W02.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=112  W=99/L=13  WR=88.4%
- Refine: exclude ZS=ZS3 drops 9/13 losers (69%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when zscore -1 to +1 neutral

### W03.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=109  W=101/L=8  WR=92.7%
- Refine: exclude ZS=ZS3 drops 5/8 losers (62%)
- **Final: n=90  W=87/L=3  WR=96.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when zscore -1 to +1 neutral

### W04.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=103  W=91/L=12  WR=88.3%
- Refine: exclude ZS=ZS3 drops 9/12 losers (75%)
- **Final: n=78  W=75/L=3  WR=96.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when zscore -1 to +1 neutral

### W05.  `T1=T1a AND T4=T4a AND ZS=ZS3`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude session_bucket=asia drops 11/13 losers (85%)
- **Final: n=67  W=65/L=2  WR=97.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia

### W06.  `H20=H20a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude H60=H60a drops 8/8 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

### W07.  `T1=T1a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude H20=H20e drops 7/11 losers (64%)
- **Final: n=57  W=53/L=4  WR=93.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when HTF20 strongly against

### W08.  `H60=H60e AND RSI=RSI3 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude H20=H20e drops 10/10 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 strongly against

### W09.  `T4=T4c AND RSI=RSI3 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude H20=H20e drops 10/10 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 strongly against

### W10.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude H20=H20e drops 10/10 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 strongly against

### W11.  `H60=H60a AND T1=T1a AND BBP=BBP2`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=asia drops 8/10 losers (80%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when session=asia

### W12.  `T1=T1a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=asia drops 8/10 losers (80%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: LONG**  •  1h trend WITH trade; lower third  •  AVOID when session=asia

### W13.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=asia drops 8/10 losers (80%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when session=asia

### W14.  `T1=T1a AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=70  W=66/L=4  WR=94.3%
- Refine: exclude H20=H20e drops 3/4 losers (75%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; session=asia  •  AVOID when HTF20 strongly against

### W15.  `H20=H20e AND T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude session_bucket=asia drops 8/9 losers (89%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=asia

### W16.  `H20=H20a AND H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude BBP=BBP3 drops 7/10 losers (70%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; session=asia  •  AVOID when middle of band

### W17.  `H60=H60e AND T1=T1a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude H20=H20e drops 5/5 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 strongly against

### W18.  `T1=T1a AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude H20=H20e drops 5/5 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 strongly against

### W19.  `H60=H60a AND T1=T1c AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude H20=H20a drops 9/9 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W20.  `T1=T1c AND ZS=ZS1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude H20=H20a drops 9/9 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W21.  `H60=H60e AND ZS=ZS5 AND direction_exec=short`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude H20=H20e drops 10/10 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W22.  `BBP=BBP0 AND direction_exec=short AND session_bucket=asia`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude H20=H20c drops 8/9 losers (89%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: SHORT**  •  deep below lower band; session=asia  •  AVOID when HTF20 neutral

### W23.  `H60=H60e AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude H20=H20c drops 8/8 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; session=asia  •  AVOID when HTF20 neutral

### W24.  `H60=H60e AND BBP=BBP0 AND direction_exec=short AND session_bucket=asia`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude H20=H20c drops 8/8 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; deep below lower band; session=asia  •  AVOID when HTF20 neutral

### W25.  `H20=H20a AND T4=T4c AND session_bucket=asia`
- Raw: n=64  W=55/L=9  WR=85.9%
- Refine: exclude ZS=ZS2 drops 5/9 losers (56%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -2 to -1 oversold

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=165  W=66/L=99  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (38/99 of losers there)
- **Sharp: n=41  W=3/L=38  WR=7.3%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=ny_open

### L02.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=134  W=53/L=81  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_open (25/81 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=ny_open

### L03.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=132  W=51/L=81  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_open (25/81 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=ny_open

### L04.  `T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=124  W=48/L=76  WR=38.7%
- Sharpen: sharpest is RSI=RSI3 (68/76 of losers there)
- **Sharp: n=86  W=18/L=68  WR=20.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L05.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=103  W=40/L=63  WR=38.8%
- Sharpen: sharpest is RSI=RSI3 (62/63 of losers there)
- **Sharp: n=80  W=18/L=62  WR=22.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L06.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_open (17/59 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=ny_open

### L07.  `T1=T1a AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_open (25/59 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=ny_open

### L08.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=92  W=26/L=66  WR=28.3%
- Sharpen: sharpest is ZS=ZS1 (38/66 of losers there)
- **Sharp: n=38  W=0/L=38  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L09.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=86  W=18/L=68  WR=20.9%
- Sharpen: sharpest is ZS=ZS1 (38/68 of losers there)
- **Sharp: n=38  W=0/L=38  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L10.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=81  W=25/L=56  WR=30.9%
- Sharpen: sharpest is ZS=ZS1 (32/56 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L11.  `ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=81  W=30/L=51  WR=37.0%
- Sharpen: sharpest is H20=H20e (25/51 of losers there)
- **Sharp: n=26  W=1/L=25  WR=3.8%**
- **Dir: LONG**  •  zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF20 strongly against

### L12.  `T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=81  W=32/L=49  WR=39.5%
- Sharpen: sharpest is H60=H60a (28/49 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=london_open  •  ONLY when HTF60 aligned WITH trade

### L13.  `T4=T4a AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is BBP=BBP0 (25/50 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when deep below lower band

### L14.  `T1=T1c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=75  W=24/L=51  WR=32.0%
- Sharpen: sharpest is H20=H20e (31/51 of losers there)
- **Sharp: n=35  W=4/L=31  WR=11.4%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF20 strongly against

### L15.  `H60=H60a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is RSI=RSI3 (44/45 of losers there)
- **Sharp: n=60  W=16/L=44  WR=26.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when RSI 40-50 lower neutral

### L16.  `H60=H60a AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is RSI=RSI3 (44/45 of losers there)
- **Sharp: n=60  W=16/L=44  WR=26.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when RSI 40-50 lower neutral

### L17.  `H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=72  W=16/L=56  WR=22.2%
- Sharpen: sharpest is H20=H20a (26/56 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L18.  `T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=72  W=16/L=56  WR=22.2%
- Sharpen: sharpest is H20=H20a (26/56 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L19.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=72  W=16/L=56  WR=22.2%
- Sharpen: sharpest is H20=H20a (26/56 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L20.  `H60=H60a AND T4=T4a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=70  W=26/L=44  WR=37.1%
- Sharpen: sharpest is BBP=BBP0 (25/44 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when deep below lower band

### L21.  `T4=T4a AND RSI=RSI3 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=66  W=16/L=50  WR=24.2%
- Sharpen: sharpest is T1=T1c (38/50 of losers there)
- **Sharp: n=38  W=0/L=38  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold; session=asia  •  ONLY when 1h trend AGAINST trade

### L22.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=66  W=16/L=50  WR=24.2%
- Sharpen: sharpest is T1=T1c (38/50 of losers there)
- **Sharp: n=38  W=0/L=38  WR=0.0%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold; session=asia  •  ONLY when 1h trend AGAINST trade

### L23.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is ZS=ZS3 (11/40 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L24.  `H20=H20e AND T1=T1c AND ZS=ZS1`
- Raw: n=65  W=26/L=39  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (31/39 of losers there)
- **Sharp: n=35  W=4/L=31  WR=11.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L25.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is ZS=ZS3 (11/40 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(44/37) | H20e(37/43) |
| H60 | — | — |
| T1 | T1a(53/47) | T1c(46/51) |
| T4 | T4a(54/47) | T4c(46/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
