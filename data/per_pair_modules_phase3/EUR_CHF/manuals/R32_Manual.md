# EUR_CHF — R32 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **790**  (W=509 / L=281)  -  WR: **64.4%**

## Session distribution

- ny_mid: n=216  W=140/L=76  WR=64.8%
- london_open: n=189  W=127/L=62  WR=67.2%
- ny_open: n=161  W=99/L=62  WR=61.5%
- off_hours: n=85  W=53/L=32  WR=62.4%
- asia: n=81  W=53/L=28  WR=65.4%
- london: n=39  W=23/L=16  WR=59.0%
- ny_close: n=11  W=8/L=3  WR=72.7%
- asia_late: n=8  W=6/L=2  WR=75.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND direction_exec=short`
- Raw: n=164  W=144/L=20  WR=87.8%
- Refine: exclude H60=H60a drops 20/20 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  AVOID when HTF60 aligned WITH trade

### W02.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=143  W=124/L=19  WR=86.7%
- Refine: exclude H60=H60a drops 19/19 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF60 aligned WITH trade

### W03.  `H20=H20a AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=110  W=96/L=14  WR=87.3%
- Refine: exclude BBP=BBP2 drops 9/14 losers (64%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when lower third

### W04.  `T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=81  W=72/L=9  WR=88.9%
- Refine: exclude H20=H20e drops 4/9 losers (44%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third  •  AVOID when HTF20 strongly against

### W05.  `T1=T1a AND T4=T4a AND ZS=ZS4`
- Raw: n=76  W=68/L=8  WR=89.5%
- Refine: exclude H20=H20e drops 4/8 losers (50%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W06.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=76  W=68/L=8  WR=89.5%
- Refine: exclude H20=H20e drops 4/8 losers (50%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W07.  `H20=H20a AND T1=T1c AND RSI=RSI3`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude session_bucket=ny_mid drops 7/11 losers (64%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W08.  `T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude ZS=ZS5 drops 5/8 losers (62%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when zscore +2 to +3 deep overbought

### W09.  `H20=H20a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude BBP=BBP2 drops 4/7 losers (57%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=ny_mid  •  AVOID when lower third

### W10.  `T1=T1a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude H20=H20e drops 8/10 losers (80%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when HTF20 strongly against

### W11.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude H20=H20e drops 8/10 losers (80%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W12.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude H60=H60d drops 4/9 losers (44%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 mildly against

### W13.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude H20=H20e drops 7/9 losers (78%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when HTF20 strongly against

### W14.  `T1=T1a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude H20=H20e drops 7/7 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W15.  `H20=H20a AND T1=T1a AND BBP=BBP4`
- Raw: n=60  W=54/L=6  WR=90.0%
- Refine: exclude H60=H60e drops 3/6 losers (50%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when HTF60 strongly against

### W16.  `H20=H20a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=58  W=53/L=5  WR=91.4%
- Refine: exclude BBP=BBP5 drops 3/5 losers (60%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W17.  `H20=H20a AND T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=58  W=53/L=5  WR=91.4%
- Refine: exclude BBP=BBP5 drops 3/5 losers (60%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W18.  `T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=56  W=51/L=5  WR=91.1%
- Refine: exclude BBP=BBP5 drops 3/5 losers (60%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W19.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=56  W=51/L=5  WR=91.1%
- Refine: exclude BBP=BBP5 drops 3/5 losers (60%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W20.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=56  W=51/L=5  WR=91.1%
- Refine: exclude BBP=BBP5 drops 3/5 losers (60%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W21.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=56  W=51/L=5  WR=91.1%
- Refine: exclude BBP=BBP5 drops 3/5 losers (60%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W22.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=56  W=51/L=5  WR=91.1%
- Refine: exclude H20=H20e drops 5/5 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W23.  `H20=H20a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=54  W=50/L=4  WR=92.6%
- Refine: exclude H60=H60e drops 4/4 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W24.  `T4=T4a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude direction_exec=short drops 8/8 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=london_open  •  AVOID when short

### W25.  `H20=H20a AND T1=T1a AND ZS=ZS4`
- Raw: n=53  W=48/L=5  WR=90.6%
- Refine: exclude H60=H60e drops 3/5 losers (60%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when HTF60 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND direction_exec=long`
- Raw: n=97  W=31/L=66  WR=32.0%
- Sharpen: sharpest is H60=H60c (16/66 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade  •  ONLY when HTF60 neutral

### L02.  `T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=91  W=32/L=59  WR=35.2%
- Sharpen: sharpest is ZS=ZS3 (13/59 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L03.  `H20=H20e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=90  W=29/L=61  WR=32.2%
- Sharpen: sharpest is H60=H60c (16/61 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when HTF60 neutral

### L04.  `T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is BBP=BBP6 (8/53 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when deep above upper band

### L05.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=85  W=32/L=53  WR=37.6%
- Sharpen: sharpest is H20=H20c (20/53 of losers there)
- **Sharp: n=25  W=5/L=20  WR=20.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF20 neutral

### L06.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is ZS=ZS1 (18/48 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L07.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=78  W=27/L=51  WR=34.6%
- Sharpen: sharpest is H20=H20c (12/51 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 neutral

### L08.  `H20=H20e AND H60=H60e AND T1=T1c`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is ZS=ZS1 (16/47 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L09.  `H20=H20e AND H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is ZS=ZS1 (16/47 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L10.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=74  W=27/L=47  WR=36.5%
- Sharpen: sharpest is H20=H20c (11/47 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 neutral

### L11.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=74  W=27/L=47  WR=36.5%
- Sharpen: sharpest is H20=H20c (11/47 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 neutral

### L12.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is ZS=ZS1 (16/45 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L13.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=68  W=24/L=44  WR=35.3%
- Sharpen: sharpest is ZS=ZS1 (18/44 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L14.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=64  W=23/L=41  WR=35.9%
- Sharpen: sharpest is T1=T1c (21/41 of losers there)
- **Sharp: n=27  W=6/L=21  WR=22.2%**
- **Dir: ?**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L15.  `H20=H20e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: sharpest is BBP=BBP0 (13/37 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when deep below lower band

### L16.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: sharpest is ZS=ZS1 (15/37 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L17.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=55  W=19/L=36  WR=34.5%
- Sharpen: sharpest is ZS=ZS3 (9/36 of losers there)
- **Sharp: n=10  W=1/L=9  WR=10.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L18.  `H20=H20e AND T4=T4c AND ZS=ZS4`
- Raw: n=55  W=21/L=34  WR=38.2%
- Sharpen: sharpest is T1=T1c (18/34 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L19.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=55  W=21/L=34  WR=38.2%
- Sharpen: sharpest is T1=T1c (18/34 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L20.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=54  W=20/L=34  WR=37.0%
- Sharpen: sharpest is H20=H20c (12/34 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 neutral

### L21.  `H60=H60a AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=52  W=19/L=33  WR=36.5%
- Sharpen: sharpest is ZS=ZS3 (9/33 of losers there)
- **Sharp: n=10  W=1/L=9  WR=10.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L22.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is H20=H20c (11/32 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 neutral

### L23.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=49  W=18/L=31  WR=36.7%
- Sharpen: sharpest is H20=H20e (21/31 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L24.  `H60=H60a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=49  W=19/L=30  WR=38.8%
- Sharpen: sharpest is direction_exec=short (30/30 of losers there)
- **Sharp: n=41  W=11/L=30  WR=26.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when short

### L25.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=48  W=17/L=31  WR=35.4%
- Sharpen: sharpest is session_bucket=ny_open (12/31 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(56/30) | H20e(26/52) |
| H60 | H60e(45/37), H60b(6/0) | H60a(39/50), H60d(0/6) |
| T1 | T1a(61/38) | T1c(39/62) |
| T4 | T4a(56/47) | T4c(44/53) |
| BBP | — | — |
| RSI | RSI3(52/47) | RSI4(36/44) |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
