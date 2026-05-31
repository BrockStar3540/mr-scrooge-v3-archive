# EUR_JPY — R38 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR1**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,598**  (W=1,625 / L=973)  -  WR: **62.5%**

## Session distribution

- asia: n=710  W=445/L=265  WR=62.7%
- london_open: n=692  W=427/L=265  WR=61.7%
- asia_late: n=295  W=187/L=108  WR=63.4%
- london: n=293  W=192/L=101  WR=65.5%
- ny_mid: n=244  W=156/L=88  WR=63.9%
- ny_open: n=140  W=87/L=53  WR=62.1%
- ny_close: n=130  W=76/L=54  WR=58.5%
- off_hours: n=94  W=55/L=39  WR=58.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60e AND RSI=RSI3`
- Raw: n=130  W=111/L=19  WR=85.4%
- Refine: exclude session_bucket=ny_mid drops 8/19 losers (42%)
- **Final: n=121  W=110/L=11  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W02.  `H20=H20a AND H60=H60e AND RSI=RSI3 AND direction_exec=short`
- Raw: n=130  W=111/L=19  WR=85.4%
- Refine: exclude session_bucket=ny_mid drops 8/19 losers (42%)
- **Final: n=121  W=110/L=11  WR=90.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W03.  `H20=H20a AND BBP=BBP2 AND session_bucket=london_open`
- Raw: n=109  W=93/L=16  WR=85.3%
- Refine: exclude strategy_id=bravo_failed_momentum drops 4/16 losers (25%)
- **Final: n=100  W=88/L=12  WR=88.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; session=london_open  •  AVOID when strategy=bravo_failed_momentum

### W04.  `H20=H20a AND T4=T4c AND session_bucket=asia_late`
- Raw: n=106  W=98/L=8  WR=92.5%
- Refine: exclude RSI=RSI4 drops 8/8 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia_late  •  AVOID when RSI 50-60 upper neutral

### W05.  `H20=H20a AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude H60=H60d drops 3/14 losers (21%)
- **Final: n=96  W=85/L=11  WR=88.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -2 to -1 oversold; session=london_open  •  AVOID when HTF60 mildly against

### W06.  `H20=H20a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude H60=H60d drops 3/14 losers (21%)
- **Final: n=96  W=85/L=11  WR=88.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; zscore -2 to -1 oversold; session=london_open  •  AVOID when HTF60 mildly against

### W07.  `H20=H20e AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H60=H60e drops 13/14 losers (93%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF60 strongly against

### W08.  `H20=H20a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude ZS=ZS1 drops 9/9 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep below lower band  •  AVOID when zscore -3 to -2 deep oversold

### W09.  `H20=H20e AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=83  W=72/L=11  WR=86.7%
- Refine: exclude RSI=RSI5 drops 10/11 losers (91%)
- **Final: n=69  W=68/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF20 strongly against; session=ny_mid  •  AVOID when RSI 60-70 strong

### W10.  `H20=H20a AND H60=H60a AND BBP=BBP0`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude ZS=ZS1 drops 9/9 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band  •  AVOID when zscore -3 to -2 deep oversold

### W11.  `H20=H20a AND H60=H60a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude ZS=ZS1 drops 9/9 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band  •  AVOID when zscore -3 to -2 deep oversold

### W12.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude H60=H60d drops 5/11 losers (45%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when HTF60 mildly against

### W13.  `H20=H20a AND T1=T1a AND session_bucket=asia_late`
- Raw: n=75  W=69/L=6  WR=92.0%
- Refine: exclude RSI=RSI4 drops 5/6 losers (83%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia_late  •  AVOID when RSI 50-60 upper neutral

### W14.  `H20=H20a AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=74  W=67/L=7  WR=90.5%
- Refine: exclude ZS=ZS1 drops 7/7 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when zscore -3 to -2 deep oversold

### W15.  `H20=H20a AND BBP=BBP2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude H60=H60d drops 3/9 losers (33%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; lower third; session=london_open  •  AVOID when HTF60 mildly against

### W16.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude H60=H60a drops 6/8 losers (75%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W17.  `T4=T4c AND RSI=RSI3 AND session_bucket=asia_late`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude BBP=BBP2 drops 9/10 losers (90%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia_late  •  AVOID when lower third

### W18.  `T4=T4c AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude H20=H20e drops 4/8 losers (50%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=asia_late  •  AVOID when HTF20 strongly against

### W19.  `H20=H20a AND T1=T1a AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude T4=T4c drops 8/9 losers (89%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold; session=london_open  •  AVOID when 4h trend AGAINST trade

### W20.  `H20=H20a AND H60=H60e AND T1=T1c`
- Raw: n=67  W=61/L=6  WR=91.0%
- Refine: exclude RSI=RSI4 drops 6/6 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W21.  `H20=H20a AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=67  W=61/L=6  WR=91.0%
- Refine: exclude RSI=RSI4 drops 6/6 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W22.  `H20=H20a AND H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=67  W=61/L=6  WR=91.0%
- Refine: exclude RSI=RSI4 drops 6/6 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W23.  `H20=H20a AND H60=H60e AND BBP=BBP2 AND session_bucket=london_open`
- Raw: n=67  W=61/L=6  WR=91.0%
- Refine: exclude RSI=RSI2 drops 6/6 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; lower third; session=london_open  •  AVOID when RSI 30-40 weak

### W24.  `H60=H60e AND T1=T1a AND T4=T4c AND session_bucket=asia_late`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude BBP=BBP4 drops 7/9 losers (78%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=asia_late  •  AVOID when upper third

### W25.  `H20=H20a AND T4=T4c AND BBP=BBP2 AND session_bucket=london_open`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude T1=T1a drops 8/9 losers (89%)
- **Final: n=31  W=30/L=1  WR=96.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third; session=london_open  •  AVOID when 1h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60a AND RSI=RSI3`
- Raw: n=112  W=39/L=73  WR=34.8%
- Sharpen: sharpest is T1=T1a (24/73 of losers there)
- **Sharp: n=27  W=3/L=24  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L02.  `H20=H20e AND H60=H60a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=112  W=39/L=73  WR=34.8%
- Sharpen: sharpest is T1=T1a (24/73 of losers there)
- **Sharp: n=27  W=3/L=24  WR=11.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L03.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=104  W=40/L=64  WR=38.5%
- Sharpen: sharpest is session_bucket=london (23/64 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london

### L04.  `H20=H20e AND H60=H60a AND T4=T4a AND RSI=RSI3`
- Raw: n=90  W=32/L=58  WR=35.6%
- Sharpen: sharpest is T1=T1a (24/58 of losers there)
- **Sharp: n=27  W=3/L=24  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L05.  `H60=H60e AND BBP=BBP0 AND direction_exec=short`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is ZS=ZS0 (20/53 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; deep below lower band  •  ONLY when zscore <-3 extreme

### L06.  `T1=T1c AND T4=T4a AND session_bucket=asia_late`
- Raw: n=80  W=27/L=53  WR=33.8%
- Sharpen: sharpest is H20=H20e (37/53 of losers there)
- **Sharp: n=40  W=3/L=37  WR=7.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia_late  •  ONLY when HTF20 strongly against

### L07.  `T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=76  W=27/L=49  WR=35.5%
- Sharpen: sharpest is ZS=ZS0 (26/49 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L08.  `H20=H20e AND T4=T4a AND session_bucket=asia_late`
- Raw: n=71  W=12/L=59  WR=16.9%
- Sharpen: sharpest is RSI=RSI3 (28/59 of losers there)
- **Sharp: n=29  W=1/L=28  WR=3.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=asia_late  •  ONLY when RSI 40-50 lower neutral

### L09.  `H20=H20a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=70  W=23/L=47  WR=32.9%
- Sharpen: sharpest is T1=T1c (24/47 of losers there)
- **Sharp: n=27  W=3/L=24  WR=11.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L10.  `H20=H20e AND BBP=BBP0 AND direction_exec=short`
- Raw: n=69  W=23/L=46  WR=33.3%
- Sharpen: sharpest is ZS=ZS0 (26/46 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; deep below lower band  •  ONLY when zscore <-3 extreme

### L11.  `H20=H20a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=68  W=24/L=44  WR=35.3%
- Sharpen: sharpest is direction_exec=short (21/44 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when short

### L12.  `T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=65  W=23/L=42  WR=35.4%
- Sharpen: sharpest is ZS=ZS0 (18/42 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L13.  `H20=H20a AND T4=T4c AND BBP=BBP6`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is session_bucket=ny_mid (14/40 of losers there)
- **Sharp: n=18  W=4/L=14  WR=22.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when session=ny_mid

### L14.  `T4=T4c AND BBP=BBP6 AND direction_exec=long`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is H20=H20e (7/40 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep above upper band  •  ONLY when HTF20 strongly against

### L15.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=63  W=25/L=38  WR=39.7%
- Sharpen: sharpest is T4=T4c (12/38 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when 4h trend AGAINST trade

### L16.  `H20=H20e AND H60=H60e AND BBP=BBP0`
- Raw: n=62  W=23/L=39  WR=37.1%
- Sharpen: sharpest is ZS=ZS0 (20/39 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep below lower band  •  ONLY when zscore <-3 extreme

### L17.  `H20=H20e AND H60=H60e AND BBP=BBP0 AND direction_exec=short`
- Raw: n=62  W=23/L=39  WR=37.1%
- Sharpen: sharpest is ZS=ZS0 (20/39 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; deep below lower band  •  ONLY when zscore <-3 extreme

### L18.  `T1=T1c AND ZS=ZS3 AND session_bucket=london_open`
- Raw: n=61  W=23/L=38  WR=37.7%
- Sharpen: sharpest is RSI=RSI4 (27/38 of losers there)
- **Sharp: n=33  W=6/L=27  WR=18.2%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -1 to +1 neutral; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L19.  `H20=H20a AND T4=T4c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=59  W=21/L=38  WR=35.6%
- Sharpen: sharpest is session_bucket=ny_mid (14/38 of losers there)
- **Sharp: n=18  W=4/L=14  WR=22.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L20.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=59  W=23/L=36  WR=39.0%
- Sharpen: sharpest is H60=H60c (13/36 of losers there)
- **Sharp: n=16  W=3/L=13  WR=18.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF60 neutral

### L21.  `T4=T4a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=59  W=23/L=36  WR=39.0%
- Sharpen: sharpest is session_bucket=asia_late (14/36 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=asia_late

### L22.  `H20=H20e AND T1=T1c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=57  W=22/L=35  WR=38.6%
- Sharpen: sharpest is RSI=RSI4 (23/35 of losers there)
- **Sharp: n=30  W=7/L=23  WR=23.3%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L23.  `H20=H20e AND T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=56  W=19/L=37  WR=33.9%
- Sharpen: sharpest is ZS=ZS0 (25/37 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L24.  `T4=T4a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=55  W=15/L=40  WR=27.3%
- Sharpen: sharpest is H20=H20e (38/40 of losers there)
- **Sharp: n=44  W=6/L=38  WR=13.6%**
- **Dir: SHORT**  •  4h trend WITH trade; session=asia_late  •  ONLY when HTF20 strongly against

### L25.  `T4=T4c AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=55  W=21/L=34  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=55  W=21/L=34  WR=38.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(51/44) | H20e(43/49) |
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
