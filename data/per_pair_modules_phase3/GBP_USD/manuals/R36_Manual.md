# GBP_USD — R36 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,450**  (W=2,190 / L=1,260)  -  WR: **63.5%**

## Session distribution

- london_open: n=1234  W=779/L=455  WR=63.1%
- ny_open: n=652  W=408/L=244  WR=62.6%
- london: n=584  W=380/L=204  WR=65.1%
- ny_mid: n=359  W=224/L=135  WR=62.4%
- asia: n=355  W=229/L=126  WR=64.5%
- asia_late: n=215  W=135/L=80  WR=62.8%
- ny_close: n=51  W=35/L=16  WR=68.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=223  W=190/L=33  WR=85.2%
- Refine: exclude T4=T4a drops 21/33 losers (64%)
- **Final: n=141  W=129/L=12  WR=91.5%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=london_open  •  AVOID when 4h trend WITH trade

### W02.  `H20=H20e AND T4=T4a AND RSI=RSI3`
- Raw: n=205  W=183/L=22  WR=89.3%
- Refine: exclude ZS=ZS2 drops 16/22 losers (73%)
- **Final: n=108  W=102/L=6  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W03.  `T1=T1c AND T4=T4a AND session_bucket=ny_open`
- Raw: n=203  W=183/L=20  WR=90.1%
- Refine: exclude BBP=BBP2 drops 9/20 losers (45%)
- **Final: n=151  W=140/L=11  WR=92.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_open  •  AVOID when lower third

### W04.  `H20=H20a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=200  W=173/L=27  WR=86.5%
- Refine: exclude H60=H60e drops 27/27 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W05.  `H20=H20a AND T1=T1a AND RSI=RSI5`
- Raw: n=185  W=161/L=24  WR=87.0%
- Refine: exclude H60=H60e drops 24/24 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W06.  `T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=185  W=161/L=24  WR=87.0%
- Refine: exclude H60=H60e drops 24/24 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W07.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=185  W=161/L=24  WR=87.0%
- Refine: exclude H60=H60e drops 24/24 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W08.  `H20=H20e AND H60=H60e AND session_bucket=london_open`
- Raw: n=180  W=159/L=21  WR=88.3%
- Refine: exclude RSI=RSI3 drops 15/21 losers (71%)
- **Final: n=123  W=117/L=6  WR=95.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W09.  `H20=H20e AND T4=T4a AND direction_exec=long`
- Raw: n=169  W=146/L=23  WR=86.4%
- Refine: exclude session_bucket=london_open drops 13/23 losers (57%)
- **Final: n=126  W=116/L=10  WR=92.1%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade  •  AVOID when session=london_open

### W10.  `H20=H20a AND T4=T4a AND RSI=RSI5`
- Raw: n=167  W=148/L=19  WR=88.6%
- Refine: exclude H60=H60e drops 19/19 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W11.  `T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=167  W=148/L=19  WR=88.6%
- Refine: exclude H60=H60e drops 19/19 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W12.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=167  W=148/L=19  WR=88.6%
- Refine: exclude H60=H60e drops 19/19 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W13.  `H20=H20e AND RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=157  W=142/L=15  WR=90.4%
- Refine: exclude ZS=ZS2 drops 11/15 losers (73%)
- **Final: n=106  W=102/L=4  WR=96.2%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=london_open  •  AVOID when zscore -2 to -1 oversold

### W14.  `T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=152  W=136/L=16  WR=89.5%
- Refine: exclude H60=H60e drops 16/16 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W15.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=152  W=136/L=16  WR=89.5%
- Refine: exclude H60=H60e drops 16/16 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W16.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=152  W=136/L=16  WR=89.5%
- Refine: exclude H60=H60e drops 16/16 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W17.  `H20=H20e AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=152  W=133/L=19  WR=87.5%
- Refine: exclude ZS=ZS2 drops 16/19 losers (84%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W18.  `H20=H20e AND RSI=RSI3 AND session_bucket=london`
- Raw: n=146  W=125/L=21  WR=85.6%
- Refine: exclude BBP=BBP2 drops 14/21 losers (67%)
- **Final: n=86  W=79/L=7  WR=91.9%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; session=london  •  AVOID when lower third

### W19.  `H20=H20a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=145  W=128/L=17  WR=88.3%
- Refine: exclude ZS=ZS5 drops 9/17 losers (53%)
- **Final: n=118  W=110/L=8  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W20.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=145  W=128/L=17  WR=88.3%
- Refine: exclude ZS=ZS5 drops 9/17 losers (53%)
- **Final: n=118  W=110/L=8  WR=93.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W21.  `H20=H20e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=145  W=124/L=21  WR=85.5%
- Refine: exclude RSI=RSI4 drops 14/21 losers (67%)
- **Final: n=83  W=76/L=7  WR=91.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W22.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=141  W=129/L=12  WR=91.5%
- Refine: exclude H60=H60b drops 4/12 losers (33%)
- **Final: n=137  W=129/L=8  WR=94.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when HTF60 slightly aligned

### W23.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=133  W=119/L=14  WR=89.5%
- Refine: exclude RSI=RSI3 drops 14/14 losers (100%)
- **Final: n=83  W=83/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W24.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=125  W=112/L=13  WR=89.6%
- Refine: exclude BBP=BBP5 drops 5/13 losers (38%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_open  •  AVOID when just touched upper band

### W25.  `H60=H60d AND T4=T4c AND RSI=RSI4`
- Raw: n=124  W=108/L=16  WR=87.1%
- Refine: exclude BBP=BBP4 drops 11/16 losers (69%)
- **Final: n=84  W=79/L=5  WR=94.0%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when upper third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T1=T1c AND T4=T4c`
- Raw: n=183  W=62/L=121  WR=33.9%
- Sharpen: sharpest is H60=H60a (55/121 of losers there)
- **Sharp: n=65  W=10/L=55  WR=15.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when HTF60 aligned WITH trade

### L02.  `T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=183  W=70/L=113  WR=38.3%
- Sharpen: sharpest is ZS=ZS4 (44/113 of losers there)
- **Sharp: n=44  W=0/L=44  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when zscore +1 to +2 overbought

### L03.  `H20=H20a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=180  W=66/L=114  WR=36.7%
- Sharpen: sharpest is H60=H60a (61/114 of losers there)
- **Sharp: n=71  W=10/L=61  WR=14.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when HTF60 aligned WITH trade

### L04.  `H20=H20e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=151  W=41/L=110  WR=27.2%
- Sharpen: sharpest is BBP=BBP4 (58/110 of losers there)
- **Sharp: n=66  W=8/L=58  WR=12.1%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong  •  ONLY when upper third

### L05.  `H20=H20a AND T4=T4c AND RSI=RSI3`
- Raw: n=147  W=39/L=108  WR=26.5%
- Sharpen: sharpest is H60=H60c (19/108 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF60 neutral

### L06.  `H20=H20e AND T1=T1c AND RSI=RSI5`
- Raw: n=142  W=38/L=104  WR=26.8%
- Sharpen: sharpest is BBP=BBP4 (58/104 of losers there)
- **Sharp: n=66  W=8/L=58  WR=12.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when upper third

### L07.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=142  W=38/L=104  WR=26.8%
- Sharpen: sharpest is BBP=BBP4 (58/104 of losers there)
- **Sharp: n=66  W=8/L=58  WR=12.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when upper third

### L08.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=142  W=38/L=104  WR=26.8%
- Sharpen: sharpest is BBP=BBP4 (58/104 of losers there)
- **Sharp: n=66  W=8/L=58  WR=12.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when upper third

### L09.  `H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=139  W=54/L=85  WR=38.8%
- Sharpen: sharpest is T1=T1c (58/85 of losers there)
- **Sharp: n=78  W=20/L=58  WR=25.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when 1h trend AGAINST trade

### L10.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=134  W=51/L=83  WR=38.1%
- Sharpen: sharpest is RSI=RSI5 (58/83 of losers there)
- **Sharp: n=66  W=8/L=58  WR=12.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when RSI 60-70 strong

### L11.  `H20=H20a AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=131  W=49/L=82  WR=37.4%
- Sharpen: sharpest is H60=H60a (40/82 of losers there)
- **Sharp: n=47  W=7/L=40  WR=14.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when HTF60 aligned WITH trade

### L12.  `T1=T1a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=130  W=42/L=88  WR=32.3%
- Sharpen: sharpest is T4=T4c (51/88 of losers there)
- **Sharp: n=60  W=9/L=51  WR=15.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L13.  `H20=H20e AND T4=T4c AND RSI=RSI5`
- Raw: n=128  W=31/L=97  WR=24.2%
- Sharpen: sharpest is H60=H60d (32/97 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 mildly against

### L14.  `T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=128  W=31/L=97  WR=24.2%
- Sharpen: sharpest is H60=H60d (32/97 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 mildly against

### L15.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=128  W=31/L=97  WR=24.2%
- Sharpen: sharpest is H60=H60d (32/97 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 mildly against

### L16.  `T1=T1a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=126  W=23/L=103  WR=18.3%
- Sharpen: sharpest is BBP=BBP4 (34/103 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when upper third

### L17.  `H20=H20e AND T1=T1c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=125  W=49/L=76  WR=39.2%
- Sharpen: sharpest is RSI=RSI5 (53/76 of losers there)
- **Sharp: n=61  W=8/L=53  WR=13.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 60-70 strong

### L18.  `H20=H20a AND RSI=RSI4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=124  W=39/L=85  WR=31.5%
- Sharpen: sharpest is H60=H60a (43/85 of losers there)
- **Sharp: n=48  W=5/L=43  WR=10.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when HTF60 aligned WITH trade

### L19.  `H20=H20a AND T4=T4c AND direction_exec=short`
- Raw: n=121  W=39/L=82  WR=32.2%
- Sharpen: sharpest is session_bucket=ny_open (28/82 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L20.  `H20=H20a AND H60=H60a AND session_bucket=london_open`
- Raw: n=120  W=33/L=87  WR=27.5%
- Sharpen: sharpest is T4=T4c (44/87 of losers there)
- **Sharp: n=47  W=3/L=44  WR=6.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london_open  •  ONLY when 4h trend AGAINST trade

### L21.  `T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=119  W=28/L=91  WR=23.5%
- Sharpen: sharpest is H60=H60d (32/91 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 mildly against

### L22.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=119  W=28/L=91  WR=23.5%
- Sharpen: sharpest is H60=H60d (32/91 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 mildly against

### L23.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=119  W=28/L=91  WR=23.5%
- Sharpen: sharpest is H60=H60d (32/91 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 mildly against

### L24.  `H20=H20e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=119  W=34/L=85  WR=28.6%
- Sharpen: sharpest is BBP=BBP4 (36/85 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when upper third

### L25.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=119  W=34/L=85  WR=28.6%
- Sharpen: sharpest is BBP=BBP4 (36/85 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when upper third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(50/37) | H20a(36/48) |
| H60 | H60d(17/11) | H60b(10/18) |
| T1 | — | — |
| T4 | T4a(55/44) | T4c(45/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
