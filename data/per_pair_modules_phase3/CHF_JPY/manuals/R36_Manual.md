# CHF_JPY — R36 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,510**  (W=2,060 / L=1,450)  -  WR: **58.7%**

## Session distribution

- london_open: n=1052  W=621/L=431  WR=59.0%
- ny_mid: n=1006  W=609/L=397  WR=60.5%
- asia: n=972  W=563/L=409  WR=57.9%
- ny_open: n=278  W=155/L=123  WR=55.8%
- off_hours: n=85  W=44/L=41  WR=51.8%
- london: n=79  W=42/L=37  WR=53.2%
- asia_late: n=35  W=24/L=11  WR=68.6%
- ny_close: n=3  W=2/L=1  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=143  W=122/L=21  WR=85.3%
- Refine: exclude H20=H20e drops 18/21 losers (86%)
- **Final: n=96  W=93/L=3  WR=96.9%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when HTF20 strongly against

### W02.  `H20=H20a AND T1=T1a AND BBP=BBP2`
- Raw: n=137  W=123/L=14  WR=89.8%
- Refine: exclude session_bucket=asia drops 8/14 losers (57%)
- **Final: n=94  W=88/L=6  WR=93.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when session=asia

### W03.  `H20=H20a AND H60=H60a AND T1=T1a AND BBP=BBP2`
- Raw: n=137  W=123/L=14  WR=89.8%
- Refine: exclude session_bucket=asia drops 8/14 losers (57%)
- **Final: n=94  W=88/L=6  WR=93.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when session=asia

### W04.  `H20=H20a AND T1=T1a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=137  W=123/L=14  WR=89.8%
- Refine: exclude session_bucket=asia drops 8/14 losers (57%)
- **Final: n=94  W=88/L=6  WR=93.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when session=asia

### W05.  `T4=T4c AND BBP=BBP5 AND session_bucket=london_open`
- Raw: n=126  W=108/L=18  WR=85.7%
- Refine: exclude H20=H20e drops 18/18 losers (100%)
- **Final: n=91  W=91/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; session=london_open  •  AVOID when HTF20 strongly against

### W06.  `T4=T4c AND BBP=BBP5 AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=126  W=108/L=18  WR=85.7%
- Refine: exclude H20=H20e drops 18/18 losers (100%)
- **Final: n=91  W=91/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when HTF20 strongly against

### W07.  `H20=H20a AND H60=H60a AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=110  W=97/L=13  WR=88.2%
- Refine: exclude ZS=ZS2 drops 11/13 losers (85%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when zscore -2 to -1 oversold

### W08.  `H20=H20a AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=110  W=97/L=13  WR=88.2%
- Refine: exclude ZS=ZS2 drops 11/13 losers (85%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when zscore -2 to -1 oversold

### W09.  `H20=H20a AND T1=T1a AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=103  W=91/L=12  WR=88.3%
- Refine: exclude ZS=ZS2 drops 11/12 losers (92%)
- **Final: n=37  W=36/L=1  WR=97.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when zscore -2 to -1 oversold

### W10.  `H20=H20a AND T1=T1a AND ZS=ZS2`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude session_bucket=asia drops 8/13 losers (62%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=asia

### W11.  `H20=H20a AND H60=H60a AND T1=T1a AND ZS=ZS2`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude session_bucket=asia drops 8/13 losers (62%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=asia

### W12.  `H20=H20a AND T1=T1a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude session_bucket=asia drops 8/13 losers (62%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when session=asia

### W13.  `H20=H20a AND T1=T1a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude session_bucket=asia drops 8/13 losers (62%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=asia

### W14.  `T1=T1c AND T4=T4c AND BBP=BBP5`
- Raw: n=88  W=79/L=9  WR=89.8%
- Refine: exclude H20=H20d drops 5/9 losers (56%)
- **Final: n=75  W=71/L=4  WR=94.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band  •  AVOID when HTF20 mildly against

### W15.  `T1=T1c AND T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=88  W=79/L=9  WR=89.8%
- Refine: exclude H20=H20d drops 5/9 losers (56%)
- **Final: n=75  W=71/L=4  WR=94.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 mildly against

### W16.  `T1=T1c AND T4=T4c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=88  W=79/L=9  WR=89.8%
- Refine: exclude H20=H20d drops 5/9 losers (56%)
- **Final: n=75  W=71/L=4  WR=94.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band  •  AVOID when HTF20 mildly against

### W17.  `H60=H60a AND T1=T1a AND RSI=RSI6`
- Raw: n=84  W=75/L=9  WR=89.3%
- Refine: exclude BBP=BBP4 drops 6/9 losers (67%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when upper third

### W18.  `H60=H60a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=84  W=75/L=9  WR=89.3%
- Refine: exclude BBP=BBP4 drops 6/9 losers (67%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 70-80 overbought  •  AVOID when upper third

### W19.  `T1=T1a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=84  W=75/L=9  WR=89.3%
- Refine: exclude BBP=BBP4 drops 6/9 losers (67%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought  •  AVOID when upper third

### W20.  `H60=H60a AND T1=T1a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=84  W=75/L=9  WR=89.3%
- Refine: exclude BBP=BBP4 drops 6/9 losers (67%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when upper third

### W21.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude BBP=BBP3 drops 12/12 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when middle of band

### W22.  `T4=T4a AND RSI=RSI5 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude BBP=BBP3 drops 12/12 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when middle of band

### W23.  `H20=H20a AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude ZS=ZS2 drops 9/9 losers (100%)
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when zscore -2 to -1 oversold

### W24.  `H20=H20a AND T4=T4c AND BBP=BBP2`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude ZS=ZS3 drops 5/9 losers (56%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when zscore -1 to +1 neutral

### W25.  `H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude BBP=BBP2 drops 9/11 losers (82%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when lower third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4a AND session_bucket=london_open`
- Raw: n=281  W=108/L=173  WR=38.4%
- Sharpen: sharpest is H20=H20c (39/173 of losers there)
- **Sharp: n=45  W=6/L=39  WR=13.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when HTF20 neutral

### L02.  `T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=235  W=92/L=143  WR=39.1%
- Sharpen: sharpest is BBP=BBP5 (35/143 of losers there)
- **Sharp: n=35  W=0/L=35  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london_open  •  ONLY when just touched upper band

### L03.  `T1=T1c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=234  W=92/L=142  WR=39.3%
- Sharpen: sharpest is H20=H20c (45/142 of losers there)
- **Sharp: n=49  W=4/L=45  WR=8.2%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=london_open  •  ONLY when HTF20 neutral

### L04.  `T1=T1c AND BBP=BBP4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=200  W=79/L=121  WR=39.5%
- Sharpen: sharpest is H20=H20c (28/121 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; session=london_open  •  ONLY when HTF20 neutral

### L05.  `T1=T1c AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=194  W=64/L=130  WR=33.0%
- Sharpen: sharpest is BBP=BBP5 (35/130 of losers there)
- **Sharp: n=35  W=0/L=35  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when just touched upper band

### L06.  `H20=H20e AND T1=T1c AND session_bucket=london_open`
- Raw: n=186  W=73/L=113  WR=39.2%
- Sharpen: sharpest is RSI=RSI6 (29/113 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 70-80 overbought

### L07.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=186  W=73/L=113  WR=39.2%
- Sharpen: sharpest is RSI=RSI6 (29/113 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 70-80 overbought

### L08.  `H20=H20e AND T4=T4a AND session_bucket=london_open`
- Raw: n=185  W=72/L=113  WR=38.9%
- Sharpen: sharpest is BBP=BBP5 (34/113 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=london_open  •  ONLY when just touched upper band

### L09.  `H60=H60a AND T4=T4a AND RSI=RSI3`
- Raw: n=165  W=59/L=106  WR=35.8%
- Sharpen: sharpest is ZS=ZS1 (48/106 of losers there)
- **Sharp: n=50  W=2/L=48  WR=4.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L10.  `T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=161  W=59/L=102  WR=36.6%
- Sharpen: sharpest is ZS=ZS1 (48/102 of losers there)
- **Sharp: n=50  W=2/L=48  WR=4.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L11.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=161  W=59/L=102  WR=36.6%
- Sharpen: sharpest is ZS=ZS1 (48/102 of losers there)
- **Sharp: n=50  W=2/L=48  WR=4.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L12.  `H60=H60e AND T1=T1c AND T4=T4a AND session_bucket=london_open`
- Raw: n=155  W=55/L=100  WR=35.5%
- Sharpen: sharpest is H20=H20c (39/100 of losers there)
- **Sharp: n=45  W=6/L=39  WR=13.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when HTF20 neutral

### L13.  `T1=T1c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=151  W=60/L=91  WR=39.7%
- Sharpen: sharpest is H20=H20e (71/91 of losers there)
- **Sharp: n=102  W=31/L=71  WR=30.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; lower third  •  ONLY when HTF20 strongly against

### L14.  `H60=H60e AND T1=T1c AND BBP=BBP2`
- Raw: n=150  W=60/L=90  WR=40.0%
- Sharpen: sharpest is H20=H20e (71/90 of losers there)
- **Sharp: n=102  W=31/L=71  WR=30.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when HTF20 strongly against

### L15.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=150  W=60/L=90  WR=40.0%
- Sharpen: sharpest is H20=H20e (71/90 of losers there)
- **Sharp: n=102  W=31/L=71  WR=30.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when HTF20 strongly against

### L16.  `H20=H20a AND H60=H60a AND RSI=RSI3`
- Raw: n=139  W=51/L=88  WR=36.7%
- Sharpen: sharpest is ZS=ZS1 (42/88 of losers there)
- **Sharp: n=44  W=2/L=42  WR=4.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L17.  `H20=H20a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=139  W=51/L=88  WR=36.7%
- Sharpen: sharpest is ZS=ZS1 (42/88 of losers there)
- **Sharp: n=44  W=2/L=42  WR=4.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L18.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=139  W=51/L=88  WR=36.7%
- Sharpen: sharpest is ZS=ZS1 (42/88 of losers there)
- **Sharp: n=44  W=2/L=42  WR=4.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=133  W=44/L=89  WR=33.1%
- Sharpen: sharpest is direction_exec=short (43/89 of losers there)
- **Sharp: n=49  W=6/L=43  WR=12.2%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when short

### L20.  `H20=H20a AND T4=T4a AND RSI=RSI3`
- Raw: n=129  W=40/L=89  WR=31.0%
- Sharpen: sharpest is ZS=ZS1 (42/89 of losers there)
- **Sharp: n=44  W=2/L=42  WR=4.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L21.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=127  W=43/L=84  WR=33.9%
- Sharpen: sharpest is BBP=BBP5 (24/84 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=london_open  •  ONLY when just touched upper band

### L22.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=127  W=45/L=82  WR=35.4%
- Sharpen: sharpest is H20=H20c (26/82 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; session=london_open  •  ONLY when HTF20 neutral

### L23.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI3`
- Raw: n=123  W=40/L=83  WR=32.5%
- Sharpen: sharpest is ZS=ZS1 (42/83 of losers there)
- **Sharp: n=44  W=2/L=42  WR=4.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L24.  `H20=H20a AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=123  W=40/L=83  WR=32.5%
- Sharpen: sharpest is ZS=ZS1 (42/83 of losers there)
- **Sharp: n=44  W=2/L=42  WR=4.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L25.  `H20=H20e AND T1=T1c AND T4=T4a AND session_bucket=london_open`
- Raw: n=123  W=43/L=80  WR=35.0%
- Sharpen: sharpest is BBP=BBP5 (24/80 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when just touched upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(53/46) | T1c(47/54) |
| T4 | T4c(54/45) | T4a(46/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
