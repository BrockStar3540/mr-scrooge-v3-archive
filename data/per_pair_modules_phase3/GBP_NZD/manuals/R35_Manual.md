# GBP_NZD — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,372**  (W=2,524 / L=1,848)  -  WR: **57.7%**

## Session distribution

- asia: n=1272  W=735/L=537  WR=57.8%
- ny_mid: n=1181  W=673/L=508  WR=57.0%
- london_open: n=884  W=524/L=360  WR=59.3%
- ny_open: n=279  W=164/L=115  WR=58.8%
- london: n=233  W=137/L=96  WR=58.8%
- ny_close: n=199  W=108/L=91  WR=54.3%
- asia_late: n=191  W=110/L=81  WR=57.6%
- off_hours: n=133  W=73/L=60  WR=54.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=195  W=169/L=26  WR=86.7%
- Refine: exclude BBP=BBP4 drops 20/26 losers (77%)
- **Final: n=103  W=97/L=6  WR=94.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when upper third

### W02.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=179  W=153/L=26  WR=85.5%
- Refine: exclude BBP=BBP4 drops 20/26 losers (77%)
- **Final: n=101  W=95/L=6  WR=94.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when upper third

### W03.  `H20=H20a AND H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=175  W=149/L=26  WR=85.1%
- Refine: exclude BBP=BBP4 drops 20/26 losers (77%)
- **Final: n=102  W=96/L=6  WR=94.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when upper third

### W04.  `BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=166  W=142/L=24  WR=85.5%
- Refine: exclude H60=H60e drops 9/24 losers (38%)
- **Final: n=157  W=142/L=15  WR=90.4%**
- **Dir: SHORT**  •  deep above upper band; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W05.  `T1=T1c AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=164  W=140/L=24  WR=85.4%
- Refine: exclude H60=H60e drops 9/24 losers (38%)
- **Final: n=155  W=140/L=15  WR=90.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W06.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI4`
- Raw: n=140  W=119/L=21  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 6/21 losers (29%)
- **Final: n=122  W=107/L=15  WR=87.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W07.  `H60=H60a AND T1=T1c AND session_bucket=london`
- Raw: n=117  W=102/L=15  WR=87.2%
- Refine: exclude H20=H20d drops 12/15 losers (80%)
- **Final: n=93  W=90/L=3  WR=96.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london  •  AVOID when HTF20 mildly against

### W08.  `T1=T1c AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=117  W=102/L=15  WR=87.2%
- Refine: exclude H20=H20d drops 6/15 losers (40%)
- **Final: n=105  W=96/L=9  WR=91.4%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; session=asia  •  AVOID when HTF20 mildly against

### W09.  `BBP=BBP6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=117  W=102/L=15  WR=87.2%
- Refine: exclude H20=H20d drops 6/15 losers (40%)
- **Final: n=105  W=96/L=9  WR=91.4%**
- **Dir: SHORT**  •  deep above upper band; session=asia  •  AVOID when HTF20 mildly against

### W10.  `T1=T1c AND BBP=BBP6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=117  W=102/L=15  WR=87.2%
- Refine: exclude H20=H20d drops 6/15 losers (40%)
- **Final: n=105  W=96/L=9  WR=91.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; session=asia  •  AVOID when HTF20 mildly against

### W11.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=115  W=101/L=14  WR=87.8%
- Refine: exclude T1=T1a drops 8/14 losers (57%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when 1h trend WITH trade

### W12.  `H60=H60a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=113  W=104/L=9  WR=92.0%
- Refine: exclude session_bucket=asia drops 9/9 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=asia

### W13.  `H60=H60e AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=108  W=94/L=14  WR=87.0%
- Refine: exclude T1=T1a drops 8/14 losers (57%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when 1h trend WITH trade

### W14.  `H60=H60a AND BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=106  W=97/L=9  WR=91.5%
- Refine: exclude session_bucket=asia drops 9/9 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W15.  `T1=T1c AND RSI=RSI4 AND session_bucket=london`
- Raw: n=105  W=91/L=14  WR=86.7%
- Refine: exclude BBP=BBP2 drops 7/14 losers (50%)
- **Final: n=92  W=85/L=7  WR=92.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=london  •  AVOID when lower third

### W16.  `T4=T4a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H60=H60b drops 4/14 losers (29%)
- **Final: n=95  W=85/L=10  WR=89.5%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF60 slightly aligned

### W17.  `H20=H20a AND H60=H60e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude ZS=ZS4 drops 8/12 losers (67%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 60-70 strong; session=asia  •  AVOID when zscore +1 to +2 overbought

### W18.  `H60=H60a AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=95  W=86/L=9  WR=90.5%
- Refine: exclude H20=H20e drops 9/9 losers (100%)
- **Final: n=43  W=43/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W19.  `H60=H60a AND T1=T1c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=93  W=84/L=9  WR=90.3%
- Refine: exclude H20=H20e drops 9/9 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W20.  `T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=91  W=80/L=11  WR=87.9%
- Refine: exclude BBP=BBP2 drops 7/11 losers (64%)
- **Final: n=80  W=76/L=4  WR=95.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london  •  AVOID when lower third

### W21.  `H20=H20a AND T4=T4c AND BBP=BBP2`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude session_bucket=ny_mid drops 10/11 losers (91%)
- **Final: n=68  W=67/L=1  WR=98.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when session=ny_mid

### W22.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=87  W=81/L=6  WR=93.1%
- Refine: exclude ZS=ZS4 drops 6/6 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore +1 to +2 overbought

### W23.  `H20=H20a AND H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude RSI=RSI4 drops 8/8 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W24.  `H20=H20a AND T4=T4c AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude session_bucket=ny_mid drops 8/9 losers (89%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W25.  `H60=H60a AND RSI=RSI4 AND session_bucket=london`
- Raw: n=84  W=81/L=3  WR=96.4%
- Refine: exclude ZS=ZS3 drops 3/3 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=410  W=157/L=253  WR=38.3%
- Sharpen: sharpest is H60=H60a (112/253 of losers there)
- **Sharp: n=149  W=37/L=112  WR=24.8%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=asia  •  ONLY when HTF60 aligned WITH trade

### L02.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=332  W=118/L=214  WR=35.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=332  W=118/L=214  WR=35.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral

### L03.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=324  W=123/L=201  WR=38.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=324  W=123/L=201  WR=38.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia

### L04.  `H20=H20e AND direction_exec=long AND session_bucket=asia`
- Raw: n=285  W=78/L=207  WR=27.4%
- Sharpen: sharpest is ZS=ZS5 (44/207 of losers there)
- **Sharp: n=44  W=0/L=44  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L05.  `T1=T1a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=283  W=111/L=172  WR=39.2%
- Sharpen: sharpest is H20=H20a (87/172 of losers there)
- **Sharp: n=124  W=37/L=87  WR=29.8%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 aligned WITH trade

### L06.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=257  W=97/L=160  WR=37.7%
- Sharpen: sharpest is H20=H20e (59/160 of losers there)
- **Sharp: n=71  W=12/L=59  WR=16.9%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 strongly against

### L07.  `H20=H20e AND T1=T1a AND session_bucket=asia`
- Raw: n=249  W=65/L=184  WR=26.1%
- Sharpen: sharpest is T4=T4a (60/184 of losers there)
- **Sharp: n=66  W=6/L=60  WR=9.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=asia  •  ONLY when 4h trend WITH trade

### L08.  `H20=H20e AND H60=H60e AND direction_exec=long`
- Raw: n=249  W=92/L=157  WR=36.9%
- Sharpen: sharpest is T4=T4c (99/157 of losers there)
- **Sharp: n=137  W=38/L=99  WR=27.7%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against  •  ONLY when 4h trend AGAINST trade

### L09.  `H20=H20e AND H60=H60a AND T1=T1a AND RSI=RSI4`
- Raw: n=246  W=95/L=151  WR=38.6%
- Sharpen: sharpest is BBP=BBP2 (38/151 of losers there)
- **Sharp: n=41  W=3/L=38  WR=7.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when lower third

### L10.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=230  W=71/L=159  WR=30.9%
- Sharpen: sharpest is H60=H60a (74/159 of losers there)
- **Sharp: n=96  W=22/L=74  WR=22.9%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L11.  `H20=H20e AND H60=H60e AND T1=T1a AND direction_exec=long`
- Raw: n=230  W=90/L=140  WR=39.1%
- Sharpen: sharpest is T4=T4c (90/140 of losers there)
- **Sharp: n=127  W=37/L=90  WR=29.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade  •  ONLY when 4h trend AGAINST trade

### L12.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=226  W=87/L=139  WR=38.5%
- Sharpen: sharpest is H20=H20a (87/139 of losers there)
- **Sharp: n=119  W=32/L=87  WR=26.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF20 aligned WITH trade

### L13.  `H20=H20e AND T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=222  W=64/L=158  WR=28.8%
- Sharpen: sharpest is T4=T4a (56/158 of losers there)
- **Sharp: n=62  W=6/L=56  WR=9.7%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; session=asia  •  ONLY when 4h trend WITH trade

### L14.  `H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=219  W=70/L=149  WR=32.0%
- Sharpen: sharpest is RSI=RSI4 (112/149 of losers there)
- **Sharp: n=149  W=37/L=112  WR=24.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L15.  `H20=H20e AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=211  W=63/L=148  WR=29.9%
- Sharpen: sharpest is T4=T4a (59/148 of losers there)
- **Sharp: n=71  W=12/L=59  WR=16.9%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L16.  `T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=209  W=82/L=127  WR=39.2%
- Sharpen: sharpest is H60=H60a (97/127 of losers there)
- **Sharp: n=129  W=32/L=97  WR=24.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L17.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=206  W=79/L=127  WR=38.3%
- Sharpen: sharpest is ZS=ZS3 (42/127 of losers there)
- **Sharp: n=52  W=10/L=42  WR=19.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L18.  `H60=H60a AND T1=T1a AND session_bucket=asia`
- Raw: n=204  W=71/L=133  WR=34.8%
- Sharpen: sharpest is T4=T4c (113/133 of losers there)
- **Sharp: n=146  W=33/L=113  WR=22.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  ONLY when 4h trend AGAINST trade

### L19.  `T4=T4a AND BBP=BBP3 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=199  W=78/L=121  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_mid (33/121 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: LONG**  •  4h trend WITH trade; middle of band; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L20.  `H20=H20a AND T4=T4a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=195  W=72/L=123  WR=36.9%
- Sharpen: sharpest is T1=T1a (101/123 of losers there)
- **Sharp: n=145  W=44/L=101  WR=30.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when 1h trend WITH trade

### L21.  `H20=H20a AND T1=T1a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=191  W=74/L=117  WR=38.7%
- Sharpen: sharpest is T4=T4a (101/117 of losers there)
- **Sharp: n=145  W=44/L=101  WR=30.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when 4h trend WITH trade

### L22.  `H20=H20e AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=190  W=75/L=115  WR=39.5%
- Sharpen: sharpest is direction_exec=long (62/115 of losers there)
- **Sharp: n=83  W=21/L=62  WR=25.3%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  ONLY when long

### L23.  `H20=H20e AND BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=190  W=75/L=115  WR=39.5%
- Sharpen: sharpest is direction_exec=long (62/115 of losers there)
- **Sharp: n=83  W=21/L=62  WR=25.3%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  ONLY when long

### L24.  `H20=H20a AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=185  W=74/L=111  WR=40.0%
- Sharpen: sharpest is T1=T1a (92/111 of losers there)
- **Sharp: n=136  W=44/L=92  WR=32.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when 1h trend WITH trade

### L25.  `H20=H20e AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=183  W=59/L=124  WR=32.2%
- Sharpen: sharpest is H60=H60a (105/124 of losers there)
- **Sharp: n=137  W=32/L=105  WR=23.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(46/38) | H20e(38/47) |
| H60 | — | — |
| T1 | T1c(58/46) | T1a(42/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(57/47) | long(43/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
