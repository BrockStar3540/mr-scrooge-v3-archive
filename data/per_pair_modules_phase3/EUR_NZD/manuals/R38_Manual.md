# EUR_NZD — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **5,089**  (W=3,105 / L=1,984)  -  WR: **61.0%**

## Session distribution

- asia: n=1523  W=921/L=602  WR=60.5%
- ny_mid: n=1303  W=797/L=506  WR=61.2%
- london_open: n=664  W=416/L=248  WR=62.7%
- ny_open: n=603  W=372/L=231  WR=61.7%
- london: n=472  W=293/L=179  WR=62.1%
- ny_close: n=318  W=187/L=131  WR=58.8%
- off_hours: n=120  W=69/L=51  WR=57.5%
- asia_late: n=86  W=50/L=36  WR=58.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=123  W=107/L=16  WR=87.0%
- Refine: exclude ZS=ZS3 drops 8/16 losers (50%)
- **Final: n=97  W=89/L=8  WR=91.8%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W02.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=115  W=99/L=16  WR=86.1%
- Refine: exclude ZS=ZS3 drops 8/16 losers (50%)
- **Final: n=97  W=89/L=8  WR=91.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W03.  `T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=112  W=102/L=10  WR=91.1%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 30-40 weak

### W04.  `T1=T1c AND T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=112  W=102/L=10  WR=91.1%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 30-40 weak

### W05.  `T4=T4c AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude H20=H20e drops 15/16 losers (94%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W06.  `T4=T4c AND BBP=BBP3 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude H20=H20e drops 14/15 losers (93%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; middle of band; RSI 40-50 lower neutral  •  AVOID when HTF20 strongly against

### W07.  `T1=T1c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=104  W=92/L=12  WR=88.5%
- Refine: exclude BBP=BBP3 drops 5/12 losers (42%)
- **Final: n=86  W=79/L=7  WR=91.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when middle of band

### W08.  `RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=104  W=92/L=12  WR=88.5%
- Refine: exclude BBP=BBP3 drops 5/12 losers (42%)
- **Final: n=86  W=79/L=7  WR=91.9%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=asia  •  AVOID when middle of band

### W09.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=104  W=92/L=12  WR=88.5%
- Refine: exclude BBP=BBP3 drops 5/12 losers (42%)
- **Final: n=86  W=79/L=7  WR=91.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when middle of band

### W10.  `T4=T4a AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude T1=T1a drops 12/12 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=london_open  •  AVOID when 1h trend WITH trade

### W11.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude session_bucket=ny_mid drops 10/13 losers (77%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W12.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude session_bucket=ny_mid drops 10/13 losers (77%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W13.  `H20=H20e AND H60=H60e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude session_bucket=ny_mid drops 10/13 losers (77%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W14.  `H60=H60a AND T4=T4c AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude H20=H20b drops 14/14 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W15.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=93  W=82/L=11  WR=88.2%
- Refine: exclude session_bucket=ny_mid drops 10/11 losers (91%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W16.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude H20=H20a drops 9/12 losers (75%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; RSI 30-40 weak  •  AVOID when HTF20 aligned WITH trade

### W17.  `T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude H20=H20d drops 5/10 losers (50%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=asia  •  AVOID when HTF20 mildly against

### W18.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=88  W=79/L=9  WR=89.8%
- Refine: exclude BBP=BBP0 drops 9/9 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W19.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude H20=H20a drops 9/11 losers (82%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; RSI 30-40 weak  •  AVOID when HTF20 aligned WITH trade

### W20.  `H60=H60a AND BBP=BBP4 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude H20=H20a drops 9/11 losers (82%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third; RSI 30-40 weak  •  AVOID when HTF20 aligned WITH trade

### W21.  `H20=H20d AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude BBP=BBP2 drops 9/12 losers (75%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: ?**  •  HTF20 mildly against; RSI 30-40 weak; session=london_open  •  AVOID when lower third

### W22.  `H20=H20d AND T4=T4a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude BBP=BBP2 drops 9/12 losers (75%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when lower third

### W23.  `H60=H60a AND T1=T1c AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=84  W=77/L=7  WR=91.7%
- Refine: exclude H20=H20b drops 7/7 losers (100%)
- **Final: n=57  W=57/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W24.  `H60=H60a AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=84  W=77/L=7  WR=91.7%
- Refine: exclude H20=H20b drops 7/7 losers (100%)
- **Final: n=57  W=57/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W25.  `T1=T1c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=84  W=75/L=9  WR=89.3%
- Refine: exclude BBP=BBP0 drops 9/9 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=164  W=64/L=100  WR=39.0%
- Sharpen: sharpest is ZS=ZS1 (22/100 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L02.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=157  W=61/L=96  WR=38.9%
- Sharpen: sharpest is ZS=ZS1 (22/96 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L03.  `T4=T4c AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=153  W=60/L=93  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (34/93 of losers there)
- **Sharp: n=42  W=8/L=34  WR=19.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 30-40 weak  •  ONLY when session=asia

### L04.  `RSI=RSI3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=146  W=56/L=90  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=146  W=56/L=90  WR=38.4%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -1 to +1 neutral

### L05.  `BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=122  W=41/L=81  WR=33.6%
- Sharpen: sharpest is H20=H20b (24/81 of losers there)
- **Sharp: n=25  W=1/L=24  WR=4.0%**
- **Dir: SHORT**  •  lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 slightly aligned

### L06.  `H20=H20e AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=121  W=43/L=78  WR=35.5%
- Sharpen: sharpest is session_bucket=asia (25/78 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: ?**  •  HTF20 strongly against; just touched lower band; RSI 30-40 weak  •  ONLY when session=asia

### L07.  `H20=H20e AND BBP=BBP1 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=121  W=43/L=78  WR=35.5%
- Sharpen: sharpest is session_bucket=asia (25/78 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: ?**  •  HTF20 strongly against; just touched lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L08.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=119  W=47/L=72  WR=39.5%
- Sharpen: sharpest is H20=H20b (24/72 of losers there)
- **Sharp: n=25  W=1/L=24  WR=4.0%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 slightly aligned

### L09.  `T4=T4a AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=116  W=42/L=74  WR=36.2%
- Sharpen: sharpest is BBP=BBP3 (51/74 of losers there)
- **Sharp: n=72  W=21/L=51  WR=29.2%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when middle of band

### L10.  `T1=T1a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=116  W=44/L=72  WR=37.9%
- Sharpen: sharpest is direction_exec=short (67/72 of losers there)
- **Sharp: n=99  W=32/L=67  WR=32.3%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when short

### L11.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=113  W=41/L=72  WR=36.3%
- Sharpen: sharpest is H20=H20b (24/72 of losers there)
- **Sharp: n=25  W=1/L=24  WR=4.0%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 slightly aligned

### L12.  `RSI=RSI3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=111  W=39/L=72  WR=35.1%
- Sharpen: sharpest is H60=H60e (18/72 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=ny_mid  •  ONLY when HTF60 strongly against

### L13.  `T4=T4a AND BBP=BBP2 AND session_bucket=london`
- Raw: n=102  W=35/L=67  WR=34.3%
- Sharpen: sharpest is H60=H60e (15/67 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; lower third; session=london  •  ONLY when HTF60 strongly against

### L14.  `BBP=BBP2 AND direction_exec=short AND session_bucket=london`
- Raw: n=102  W=35/L=67  WR=34.3%
- Sharpen: sharpest is H60=H60e (15/67 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  lower third; session=london  •  ONLY when HTF60 strongly against

### L15.  `T4=T4a AND BBP=BBP2 AND direction_exec=short AND session_bucket=london`
- Raw: n=102  W=35/L=67  WR=34.3%
- Sharpen: sharpest is H60=H60e (15/67 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; lower third; session=london  •  ONLY when HTF60 strongly against

### L16.  `H20=H20e AND T1=T1c AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (19/61 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; just touched lower band; RSI 30-40 weak  •  ONLY when session=asia

### L17.  `H20=H20e AND BBP=BBP1 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (19/61 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: LONG**  •  HTF20 strongly against; just touched lower band; RSI 30-40 weak  •  ONLY when session=asia

### L18.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: sharpest is H20=H20b (24/61 of losers there)
- **Sharp: n=25  W=1/L=24  WR=4.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 slightly aligned

### L19.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: sharpest is H20=H20b (24/61 of losers there)
- **Sharp: n=25  W=1/L=24  WR=4.0%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 slightly aligned

### L20.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=99  W=32/L=67  WR=32.3%
- Sharpen: sharpest is H60=H60e (18/67 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when HTF60 strongly against

### L21.  `BBP=BBP3 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=99  W=34/L=65  WR=34.3%
- Sharpen: sharpest is T4=T4a (51/65 of losers there)
- **Sharp: n=72  W=21/L=51  WR=29.2%**
- **Dir: SHORT**  •  middle of band; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L22.  `BBP=BBP3 AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=99  W=34/L=65  WR=34.3%
- Sharpen: sharpest is T4=T4a (51/65 of losers there)
- **Sharp: n=72  W=21/L=51  WR=29.2%**
- **Dir: SHORT**  •  middle of band; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend WITH trade

### L23.  `H20=H20a AND T1=T1c AND ZS=ZS3`
- Raw: n=99  W=37/L=62  WR=37.4%
- Sharpen: sharpest is session_bucket=asia (21/62 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when session=asia

### L24.  `RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=99  W=37/L=62  WR=37.4%
- Sharpen: sharpest is H20=H20b (24/62 of losers there)
- **Sharp: n=25  W=1/L=24  WR=4.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 slightly aligned

### L25.  `BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=99  W=37/L=62  WR=37.4%
- Sharpen: sharpest is H20=H20b (24/62 of losers there)
- **Sharp: n=25  W=1/L=24  WR=4.0%**
- **Dir: SHORT**  •  lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 slightly aligned

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
