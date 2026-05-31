# GBP_NZD — R25 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **6,043**  (W=3,473 / L=2,570)  -  WR: **57.5%**

## Session distribution

- asia: n=2507  W=1462/L=1045  WR=58.3%
- ny_mid: n=857  W=462/L=395  WR=53.9%
- london_open: n=696  W=402/L=294  WR=57.8%
- ny_close: n=644  W=384/L=260  WR=59.6%
- off_hours: n=426  W=225/L=201  WR=52.8%
- ny_open: n=406  W=250/L=156  WR=61.6%
- london: n=390  W=222/L=168  WR=56.9%
- asia_late: n=117  W=66/L=51  WR=56.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T1=T1a AND session_bucket=ny_open`
- Raw: n=106  W=97/L=9  WR=91.5%
- Refine: exclude T4=T4c drops 6/9 losers (67%)
- **Final: n=84  W=81/L=3  WR=96.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W02.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=ny_close`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude RSI=RSI4 drops 14/14 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=ny_close  •  AVOID when RSI 50-60 upper neutral

### W03.  `H60=H60a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=94  W=86/L=8  WR=91.5%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W04.  `H60=H60a AND T4=T4a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=94  W=86/L=8  WR=91.5%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W05.  `H60=H60a AND RSI=RSI4 AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=94  W=86/L=8  WR=91.5%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W06.  `H60=H60a AND ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=94  W=86/L=8  WR=91.5%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W07.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=94  W=86/L=8  WR=91.5%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W08.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=94  W=86/L=8  WR=91.5%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W09.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=84  W=81/L=3  WR=96.4%
- Refine: exclude BBP=BBP4 drops 2/3 losers (67%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when upper third

### W10.  `H20=H20e AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=84  W=81/L=3  WR=96.4%
- Refine: exclude BBP=BBP4 drops 2/3 losers (67%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when upper third

### W11.  `T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude session_bucket=asia drops 10/10 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W12.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude session_bucket=asia drops 10/10 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: LONG**  •  deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W13.  `T4=T4a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude session_bucket=asia drops 10/10 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W14.  `H20=H20e AND H60=H60e AND BBP=BBP5 AND session_bucket=asia`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude RSI=RSI4 drops 11/11 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched upper band; session=asia  •  AVOID when RSI 50-60 upper neutral

### W15.  `H20=H20a AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude T4=T4c drops 12/12 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W16.  `T1=T1a AND BBP=BBP2 AND session_bucket=ny_close`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; lower third; session=ny_close  •  AVOID when RSI 50-60 upper neutral

### W17.  `T4=T4c AND BBP=BBP2 AND session_bucket=ny_close`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude H60=H60a drops 7/11 losers (64%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; session=ny_close  •  AVOID when HTF60 aligned WITH trade

### W18.  `H60=H60a AND BBP=BBP5 AND session_bucket=ny_mid`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched upper band; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W19.  `H60=H60a AND T4=T4a AND BBP=BBP5 AND session_bucket=ny_mid`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; just touched upper band; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W20.  `H60=H60a AND BBP=BBP5 AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched upper band; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W21.  `H60=H60a AND BBP=BBP5 AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W22.  `H60=H60a AND BBP=BBP5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; just touched upper band; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W23.  `T4=T4a AND BBP=BBP5 AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W24.  `BBP=BBP5 AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: LONG**  •  just touched upper band; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W25.  `T1=T1a AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude RSI=RSI4 drops 7/7 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=ny_close  •  AVOID when RSI 50-60 upper neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=283  W=103/L=180  WR=36.4%
- Sharpen: sharpest is T1=T1c (114/180 of losers there)
- **Sharp: n=156  W=42/L=114  WR=26.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L02.  `RSI=RSI4 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=255  W=101/L=154  WR=39.6%
- Sharpen: sharpest is T4=T4a (63/154 of losers there)
- **Sharp: n=78  W=15/L=63  WR=19.2%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L03.  `BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=255  W=101/L=154  WR=39.6%
- Sharpen: sharpest is T4=T4a (63/154 of losers there)
- **Sharp: n=78  W=15/L=63  WR=19.2%**
- **Dir: SHORT**  •  lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L04.  `T1=T1c AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=239  W=92/L=147  WR=38.5%
- Sharpen: sharpest is H60=H60a (108/147 of losers there)
- **Sharp: n=142  W=34/L=108  WR=23.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; lower third; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L05.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=238  W=87/L=151  WR=36.6%
- Sharpen: sharpest is H60=H60e (105/151 of losers there)
- **Sharp: n=144  W=39/L=105  WR=27.1%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L06.  `BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=238  W=87/L=151  WR=36.6%
- Sharpen: sharpest is H60=H60e (105/151 of losers there)
- **Sharp: n=144  W=39/L=105  WR=27.1%**
- **Dir: LONG**  •  lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L07.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=238  W=87/L=151  WR=36.6%
- Sharpen: sharpest is H60=H60e (105/151 of losers there)
- **Sharp: n=144  W=39/L=105  WR=27.1%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L08.  `T1=T1c AND T4=T4a AND BBP=BBP2`
- Raw: n=234  W=82/L=152  WR=35.0%
- Sharpen: sharpest is direction_exec=short (61/152 of losers there)
- **Sharp: n=81  W=20/L=61  WR=24.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third  •  ONLY when short

### L09.  `H60=H60a AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=228  W=86/L=142  WR=37.7%
- Sharpen: sharpest is T1=T1c (87/142 of losers there)
- **Sharp: n=116  W=29/L=87  WR=25.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

### L10.  `H60=H60a AND BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=228  W=86/L=142  WR=37.7%
- Sharpen: sharpest is T1=T1c (87/142 of losers there)
- **Sharp: n=116  W=29/L=87  WR=25.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

### L11.  `H60=H60a AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=219  W=67/L=152  WR=30.6%
- Sharpen: sharpest is T1=T1c (108/152 of losers there)
- **Sharp: n=142  W=34/L=108  WR=23.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; lower third; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L12.  `T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=218  W=84/L=134  WR=38.5%
- Sharpen: sharpest is ZS=ZS5 (38/134 of losers there)
- **Sharp: n=46  W=8/L=38  WR=17.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_close  •  ONLY when zscore +2 to +3 deep overbought

### L13.  `T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=214  W=79/L=135  WR=36.9%
- Sharpen: sharpest is H60=H60e (91/135 of losers there)
- **Sharp: n=129  W=38/L=91  WR=29.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L14.  `RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=214  W=79/L=135  WR=36.9%
- Sharpen: sharpest is H60=H60e (91/135 of losers there)
- **Sharp: n=129  W=38/L=91  WR=29.5%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L15.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=214  W=79/L=135  WR=36.9%
- Sharpen: sharpest is H60=H60e (91/135 of losers there)
- **Sharp: n=129  W=38/L=91  WR=29.5%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L16.  `T4=T4a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=214  W=79/L=135  WR=36.9%
- Sharpen: sharpest is H60=H60e (91/135 of losers there)
- **Sharp: n=129  W=38/L=91  WR=29.5%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L17.  `BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=214  W=79/L=135  WR=36.9%
- Sharpen: sharpest is H60=H60e (91/135 of losers there)
- **Sharp: n=129  W=38/L=91  WR=29.5%**
- **Dir: LONG**  •  lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L18.  `H60=H60e AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=205  W=80/L=125  WR=39.0%
- Sharpen: sharpest is ZS=ZS5 (61/125 of losers there)
- **Sharp: n=61  W=0/L=61  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L19.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=205  W=80/L=125  WR=39.0%
- Sharpen: sharpest is ZS=ZS5 (61/125 of losers there)
- **Sharp: n=61  W=0/L=61  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L20.  `H60=H60e AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=205  W=80/L=125  WR=39.0%
- Sharpen: sharpest is ZS=ZS5 (61/125 of losers there)
- **Sharp: n=61  W=0/L=61  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L21.  `H60=H60a AND T1=T1c AND session_bucket=ny_close`
- Raw: n=205  W=82/L=123  WR=40.0%
- Sharpen: sharpest is ZS=ZS2 (31/123 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  ONLY when zscore -2 to -1 oversold

### L22.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=197  W=78/L=119  WR=39.6%
- Sharpen: sharpest is H60=H60a (44/119 of losers there)
- **Sharp: n=51  W=7/L=44  WR=13.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third; session=asia  •  ONLY when HTF60 aligned WITH trade

### L23.  `T1=T1c AND T4=T4a AND ZS=ZS2`
- Raw: n=196  W=67/L=129  WR=34.2%
- Sharpen: sharpest is direction_exec=short (51/129 of losers there)
- **Sharp: n=66  W=15/L=51  WR=22.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when short

### L24.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=196  W=67/L=129  WR=34.2%
- Sharpen: sharpest is direction_exec=short (51/129 of losers there)
- **Sharp: n=66  W=15/L=51  WR=22.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when short

### L25.  `H60=H60a AND T4=T4a AND BBP=BBP2`
- Raw: n=195  W=71/L=124  WR=36.4%
- Sharpen: sharpest is direction_exec=short (76/124 of losers there)
- **Sharp: n=96  W=20/L=76  WR=20.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third  •  ONLY when short

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
