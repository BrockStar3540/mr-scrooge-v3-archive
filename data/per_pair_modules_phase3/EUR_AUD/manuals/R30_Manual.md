# EUR_AUD — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,344**  (W=2,601 / L=1,743)  -  WR: **59.9%**

## Session distribution

- ny_mid: n=1411  W=837/L=574  WR=59.3%
- asia: n=1006  W=592/L=414  WR=58.8%
- london_open: n=986  W=617/L=369  WR=62.6%
- ny_close: n=293  W=173/L=120  WR=59.0%
- ny_open: n=272  W=160/L=112  WR=58.8%
- london: n=246  W=147/L=99  WR=59.8%
- asia_late: n=109  W=63/L=46  WR=57.8%
- off_hours: n=21  W=12/L=9  WR=57.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND ZS=ZS3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=136  W=117/L=19  WR=86.0%
- Refine: exclude H60=H60c drops 5/19 losers (26%)
- **Final: n=129  W=115/L=14  WR=89.1%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -1 to +1 neutral; session=london_open  •  AVOID when HTF60 neutral

### W02.  `H60=H60a AND T4=T4a AND ZS=ZS3 AND session_bucket=london_open`
- Raw: n=124  W=111/L=13  WR=89.5%
- Refine: exclude T1=T1c drops 4/13 losers (31%)
- **Final: n=118  W=109/L=9  WR=92.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral; session=london_open  •  AVOID when 1h trend AGAINST trade

### W03.  `H60=H60a AND T1=T1a AND ZS=ZS3 AND session_bucket=london_open`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude T4=T4c drops 8/17 losers (47%)
- **Final: n=106  W=97/L=9  WR=91.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -1 to +1 neutral; session=london_open  •  AVOID when 4h trend AGAINST trade

### W04.  `H20=H20a AND T4=T4a AND ZS=ZS3 AND session_bucket=london_open`
- Raw: n=109  W=93/L=16  WR=85.3%
- Refine: exclude H60=H60c drops 3/16 losers (19%)
- **Final: n=106  W=93/L=13  WR=87.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral; session=london_open  •  AVOID when HTF60 neutral

### W05.  `BBP=BBP3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude RSI=RSI3 drops 13/14 losers (93%)
- **Final: n=32  W=31/L=1  WR=96.9%**
- **Dir: SHORT**  •  middle of band; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W06.  `BBP=BBP3 AND ZS=ZS3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude RSI=RSI3 drops 13/14 losers (93%)
- **Final: n=32  W=31/L=1  WR=96.9%**
- **Dir: SHORT**  •  middle of band; zscore -1 to +1 neutral; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W07.  `RSI=RSI3 AND strategy_id=TF2_pullback_EMA20_long AND direction_exec=short`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude ZS=ZS5 drops 7/14 losers (50%)
- **Final: n=76  W=69/L=7  WR=90.8%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; strategy=TF2_pullback_EMA20_long  •  AVOID when zscore +2 to +3 deep overbought

### W08.  `H60=H60a AND BBP=BBP3 AND session_bucket=london_open`
- Raw: n=100  W=89/L=11  WR=89.0%
- Refine: exclude T1=T1c drops 4/11 losers (36%)
- **Final: n=89  W=82/L=7  WR=92.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; middle of band; session=london_open  •  AVOID when 1h trend AGAINST trade

### W09.  `H60=H60a AND BBP=BBP3 AND ZS=ZS3 AND session_bucket=london_open`
- Raw: n=100  W=89/L=11  WR=89.0%
- Refine: exclude T1=T1c drops 4/11 losers (36%)
- **Final: n=89  W=82/L=7  WR=92.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; middle of band; zscore -1 to +1 neutral; session=london_open  •  AVOID when 1h trend AGAINST trade

### W10.  `H60=H60a AND BBP=BBP3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=100  W=89/L=11  WR=89.0%
- Refine: exclude T1=T1c drops 4/11 losers (36%)
- **Final: n=89  W=82/L=7  WR=92.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; middle of band; session=london_open  •  AVOID when 1h trend AGAINST trade

### W11.  `T1=T1a AND strategy_id=TF2_pullback_EMA20_long AND direction_exec=short`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude ZS=ZS5 drops 6/14 losers (43%)
- **Final: n=72  W=64/L=8  WR=88.9%**
- **Dir: SHORT**  •  1h trend WITH trade; strategy=TF2_pullback_EMA20_long  •  AVOID when zscore +2 to +3 deep overbought

### W12.  `T4=T4a AND BBP=BBP3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude H60=H60c drops 3/10 losers (30%)
- **Final: n=89  W=82/L=7  WR=92.1%**
- **Dir: SHORT**  •  4h trend WITH trade; middle of band; session=london_open  •  AVOID when HTF60 neutral

### W13.  `T1=T1a AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=91  W=79/L=12  WR=86.8%
- Refine: exclude H60=H60a drops 12/12 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when HTF60 aligned WITH trade

### W14.  `T1=T1a AND BBP=BBP3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=90  W=80/L=10  WR=88.9%
- Refine: exclude RSI=RSI3 drops 10/10 losers (100%)
- **Final: n=27  W=27/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; middle of band; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W15.  `T1=T1a AND RSI=RSI3 AND strategy_id=TF2_pullback_EMA20_long AND direction_exec=short`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude ZS=ZS5 drops 6/12 losers (50%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; strategy=TF2_pullback_EMA20_long  •  AVOID when zscore +2 to +3 deep overbought

### W16.  `H60=H60a AND T4=T4a AND BBP=BBP3 AND session_bucket=london_open`
- Raw: n=85  W=78/L=7  WR=91.8%
- Refine: exclude strategy_id=alpha_pullback_v2 drops 2/7 losers (29%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; middle of band; session=london_open  •  AVOID when strategy=alpha_pullback_v2

### W17.  `H60=H60a AND T1=T1a AND BBP=BBP3 AND session_bucket=london_open`
- Raw: n=83  W=76/L=7  WR=91.6%
- Refine: exclude RSI=RSI3 drops 7/7 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; middle of band; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W18.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude H60=H60b drops 6/11 losers (55%)
- **Final: n=60  W=55/L=5  WR=91.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when HTF60 slightly aligned

### W19.  `T4=T4a AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude H60=H60b drops 6/11 losers (55%)
- **Final: n=60  W=55/L=5  WR=91.7%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when HTF60 slightly aligned

### W20.  `T4=T4a AND RSI=RSI3 AND strategy_id=TF2_pullback_EMA20_long AND direction_exec=short`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude ZS=ZS5 drops 5/10 losers (50%)
- **Final: n=56  W=51/L=5  WR=91.1%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; strategy=TF2_pullback_EMA20_long  •  AVOID when zscore +2 to +3 deep overbought

### W21.  `H20=H20a AND H60=H60a AND BBP=BBP3 AND session_bucket=london_open`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude T4=T4c drops 4/10 losers (40%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; middle of band; session=london_open  •  AVOID when 4h trend AGAINST trade

### W22.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude BBP=BBP0 drops 4/9 losers (44%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W23.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude BBP=BBP0 drops 4/9 losers (44%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W24.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude BBP=BBP0 drops 4/9 losers (44%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W25.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude BBP=BBP0 drops 4/9 losers (44%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=275  W=107/L=168  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=275  W=107/L=168  WR=38.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third

### L02.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=269  W=107/L=162  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=269  W=107/L=162  WR=39.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third

### L03.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=234  W=93/L=141  WR=39.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=234  W=93/L=141  WR=39.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third

### L04.  `H20=H20e AND T1=T1c AND RSI=RSI2`
- Raw: n=231  W=92/L=139  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=231  W=92/L=139  WR=39.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak

### L05.  `H20=H20e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=231  W=92/L=139  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=231  W=92/L=139  WR=39.8%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak

### L06.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=231  W=92/L=139  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=231  W=92/L=139  WR=39.8%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak

### L07.  `T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=229  W=82/L=147  WR=35.8%
- Sharpen: sharpest is session_bucket=ny_mid (46/147 of losers there)
- **Sharp: n=59  W=13/L=46  WR=22.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L08.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=229  W=82/L=147  WR=35.8%
- Sharpen: sharpest is session_bucket=ny_mid (46/147 of losers there)
- **Sharp: n=59  W=13/L=46  WR=22.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L09.  `T1=T1c AND T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=223  W=82/L=141  WR=36.8%
- Sharpen: sharpest is session_bucket=ny_mid (46/141 of losers there)
- **Sharp: n=59  W=13/L=46  WR=22.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L10.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=198  W=72/L=126  WR=36.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=198  W=72/L=126  WR=36.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third

### L11.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=194  W=70/L=124  WR=36.1%
- Sharpen: sharpest is session_bucket=ny_mid (43/124 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L12.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=169  W=60/L=109  WR=35.5%
- Sharpen: sharpest is session_bucket=ny_mid (34/109 of losers there)
- **Sharp: n=43  W=9/L=34  WR=20.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L13.  `H20=H20a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=152  W=60/L=92  WR=39.5%
- Sharpen: sharpest is RSI=RSI3 (64/92 of losers there)
- **Sharp: n=86  W=22/L=64  WR=25.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L14.  `H20=H20a AND T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=152  W=60/L=92  WR=39.5%
- Sharpen: sharpest is RSI=RSI3 (64/92 of losers there)
- **Sharp: n=86  W=22/L=64  WR=25.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L15.  `T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=140  W=51/L=89  WR=36.4%
- Sharpen: sharpest is H60=H60e (89/89 of losers there)
- **Sharp: n=130  W=41/L=89  WR=31.5%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L16.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=140  W=51/L=89  WR=36.4%
- Sharpen: sharpest is H60=H60e (89/89 of losers there)
- **Sharp: n=130  W=41/L=89  WR=31.5%**
- **Dir: LONG**  •  deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L17.  `T1=T1c AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=140  W=51/L=89  WR=36.4%
- Sharpen: sharpest is H60=H60e (89/89 of losers there)
- **Sharp: n=130  W=41/L=89  WR=31.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L18.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=135  W=52/L=83  WR=38.5%
- Sharpen: sharpest is session_bucket=asia (42/83 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L19.  `H20=H20e AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=135  W=52/L=83  WR=38.5%
- Sharpen: sharpest is session_bucket=asia (42/83 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L20.  `H60=H60e AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=130  W=41/L=89  WR=31.5%
- Sharpen: sharpest is H20=H20e (61/89 of losers there)
- **Sharp: n=76  W=15/L=61  WR=19.7%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L21.  `H60=H60e AND T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=130  W=41/L=89  WR=31.5%
- Sharpen: sharpest is H20=H20e (61/89 of losers there)
- **Sharp: n=76  W=15/L=61  WR=19.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L22.  `H60=H60e AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=130  W=41/L=89  WR=31.5%
- Sharpen: sharpest is H20=H20e (61/89 of losers there)
- **Sharp: n=76  W=15/L=61  WR=19.7%**
- **Dir: LONG**  •  HTF60 strongly against; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L23.  `H20=H20a AND H60=H60e AND session_bucket=ny_mid`
- Raw: n=122  W=42/L=80  WR=34.4%
- Sharpen: sharpest is RSI=RSI3 (64/80 of losers there)
- **Sharp: n=78  W=14/L=64  WR=17.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L24.  `H20=H20a AND H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=122  W=42/L=80  WR=34.4%
- Sharpen: sharpest is RSI=RSI3 (64/80 of losers there)
- **Sharp: n=78  W=14/L=64  WR=17.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L25.  `H20=H20a AND H60=H60e AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=122  W=42/L=80  WR=34.4%
- Sharpen: sharpest is RSI=RSI3 (64/80 of losers there)
- **Sharp: n=78  W=14/L=64  WR=17.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(51/39) | H60e(38/51) |
| T1 | T1a(57/42) | T1c(41/57) |
| T4 | T4a(54/47) | T4c(46/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(57/44) | long(43/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
