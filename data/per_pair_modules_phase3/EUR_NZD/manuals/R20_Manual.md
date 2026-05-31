# EUR_NZD — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,863**  (W=2,157 / L=1,706)  -  WR: **55.8%**

## Session distribution

- asia: n=1285  W=723/L=562  WR=56.3%
- ny_mid: n=852  W=450/L=402  WR=52.8%
- ny_close: n=485  W=288/L=197  WR=59.4%
- ny_open: n=457  W=263/L=194  WR=57.5%
- london_open: n=418  W=225/L=193  WR=53.8%
- off_hours: n=240  W=134/L=106  WR=55.8%
- london: n=125  W=74/L=51  WR=59.2%
- asia_late: n=1  W=0/L=1  WR=0.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude BBP=BBP5 drops 9/13 losers (69%)
- **Final: n=89  W=85/L=4  WR=95.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_open  •  AVOID when just touched upper band

### W02.  `T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude BBP=BBP5 drops 9/13 losers (69%)
- **Final: n=89  W=85/L=4  WR=95.5%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_open  •  AVOID when just touched upper band

### W03.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude BBP=BBP5 drops 9/13 losers (69%)
- **Final: n=89  W=85/L=4  WR=95.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when just touched upper band

### W04.  `T4=T4a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude H60=H60a drops 11/12 losers (92%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=ny_open  •  AVOID when HTF60 aligned WITH trade

### W05.  `H20=H20c AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude BBP=BBP2 drops 6/12 losers (50%)
- **Final: n=81  W=75/L=6  WR=92.6%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when lower third

### W06.  `H20=H20a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=81  W=75/L=6  WR=92.6%
- Refine: exclude ZS=ZS3 drops 5/6 losers (83%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W07.  `H20=H20a AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=81  W=75/L=6  WR=92.6%
- Refine: exclude ZS=ZS3 drops 5/6 losers (83%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; upper third; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W08.  `H20=H20a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude H60=H60a drops 8/9 losers (89%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when HTF60 aligned WITH trade

### W09.  `H20=H20a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=77  W=73/L=4  WR=94.8%
- Refine: exclude BBP=BBP5 drops 4/4 losers (100%)
- **Final: n=65  W=65/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when just touched upper band

### W10.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=77  W=73/L=4  WR=94.8%
- Refine: exclude BBP=BBP5 drops 4/4 losers (100%)
- **Final: n=65  W=65/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when just touched upper band

### W11.  `H20=H20e AND T4=T4a AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude BBP=BBP3 drops 8/11 losers (73%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=asia  •  AVOID when middle of band

### W12.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude BBP=BBP3 drops 8/11 losers (73%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when middle of band

### W13.  `H20=H20e AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude BBP=BBP3 drops 8/11 losers (73%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when middle of band

### W14.  `H20=H20e AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude BBP=BBP3 drops 8/11 losers (73%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; session=asia  •  AVOID when middle of band

### W15.  `T4=T4a AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=74  W=67/L=7  WR=90.5%
- Refine: exclude H60=H60a drops 6/7 losers (86%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF60 aligned WITH trade

### W16.  `T4=T4a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=74  W=67/L=7  WR=90.5%
- Refine: exclude H60=H60a drops 6/7 losers (86%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  4h trend WITH trade; upper third; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF60 aligned WITH trade

### W17.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude H20=H20e drops 5/11 losers (45%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W18.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude H60=H60a drops 9/9 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral; session=ny_open  •  AVOID when HTF60 aligned WITH trade

### W19.  `H20=H20a AND H60=H60e AND session_bucket=ny_open`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude T1=T1c drops 9/9 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W20.  `H60=H60e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude T1=T1c drops 9/9 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W21.  `H20=H20a AND H60=H60e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude T1=T1c drops 9/9 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W22.  `H20=H20a AND H60=H60e AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude T1=T1c drops 9/9 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W23.  `H60=H60e AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude T1=T1c drops 9/9 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W24.  `T4=T4a AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude session_bucket=ny_mid drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W25.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude RSI=RSI3 drops 4/9 losers (44%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI 40-50 lower neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=368  W=138/L=230  WR=37.5%
- Sharpen: sharpest is T4=T4c (128/230 of losers there)
- **Sharp: n=162  W=34/L=128  WR=21.0%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

### L02.  `T4=T4c AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=352  W=125/L=227  WR=35.5%
- Sharpen: sharpest is H60=H60a (110/227 of losers there)
- **Sharp: n=123  W=13/L=110  WR=10.6%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF60 aligned WITH trade

### L03.  `H60=H60a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=338  W=122/L=216  WR=36.1%
- Sharpen: sharpest is T4=T4c (110/216 of losers there)
- **Sharp: n=123  W=13/L=110  WR=10.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

### L04.  `H60=H60a AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=329  W=117/L=212  WR=35.6%
- Sharpen: sharpest is T4=T4c (110/212 of losers there)
- **Sharp: n=123  W=13/L=110  WR=10.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

### L05.  `H20=H20e AND T4=T4c AND ZS=ZS3`
- Raw: n=308  W=109/L=199  WR=35.4%
- Sharpen: sharpest is T1=T1a (110/199 of losers there)
- **Sharp: n=142  W=32/L=110  WR=22.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when 1h trend WITH trade

### L06.  `T1=T1a AND T4=T4c AND BBP=BBP4`
- Raw: n=290  W=114/L=176  WR=39.3%
- Sharpen: sharpest is ZS=ZS3 (52/176 of losers there)
- **Sharp: n=63  W=11/L=52  WR=17.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third  •  ONLY when zscore -1 to +1 neutral

### L07.  `T1=T1a AND T4=T4c AND ZS=ZS3`
- Raw: n=287  W=110/L=177  WR=38.3%
- Sharpen: sharpest is H20=H20e (110/177 of losers there)
- **Sharp: n=142  W=32/L=110  WR=22.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when HTF20 strongly against

### L08.  `H20=H20e AND H60=H60a AND RSI=RSI4`
- Raw: n=281  W=107/L=174  WR=38.1%
- Sharpen: sharpest is ZS=ZS3 (88/174 of losers there)
- **Sharp: n=105  W=17/L=88  WR=16.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L09.  `H60=H60e AND T4=T4c AND BBP=BBP4`
- Raw: n=279  W=110/L=169  WR=39.4%
- Sharpen: sharpest is H20=H20e (93/169 of losers there)
- **Sharp: n=130  W=37/L=93  WR=28.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third  •  ONLY when HTF20 strongly against

### L10.  `H60=H60e AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=269  W=106/L=163  WR=39.4%
- Sharpen: sharpest is direction_exec=long (146/163 of losers there)
- **Sharp: n=221  W=75/L=146  WR=33.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when long

### L11.  `T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=268  W=102/L=166  WR=38.1%
- Sharpen: sharpest is H20=H20e (93/166 of losers there)
- **Sharp: n=128  W=35/L=93  WR=27.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third  •  ONLY when HTF20 strongly against

### L12.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=268  W=102/L=166  WR=38.1%
- Sharpen: sharpest is H20=H20e (93/166 of losers there)
- **Sharp: n=128  W=35/L=93  WR=27.3%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third  •  ONLY when HTF20 strongly against

### L13.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=268  W=104/L=164  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=268  W=104/L=164  WR=38.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia

### L14.  `H20=H20e AND H60=H60a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=263  W=99/L=164  WR=37.6%
- Sharpen: sharpest is ZS=ZS3 (84/164 of losers there)
- **Sharp: n=98  W=14/L=84  WR=14.3%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L15.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=261  W=94/L=167  WR=36.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=261  W=94/L=167  WR=36.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=asia

### L16.  `H20=H20e AND H60=H60a AND T4=T4c AND RSI=RSI4`
- Raw: n=255  W=97/L=158  WR=38.0%
- Sharpen: sharpest is ZS=ZS3 (84/158 of losers there)
- **Sharp: n=96  W=12/L=84  WR=12.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L17.  `H20=H20e AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=248  W=82/L=166  WR=33.1%
- Sharpen: sharpest is H60=H60a (88/166 of losers there)
- **Sharp: n=105  W=17/L=88  WR=16.2%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF60 aligned WITH trade

### L18.  `H60=H60a AND BBP=BBP3 AND RSI=RSI4`
- Raw: n=245  W=97/L=148  WR=39.6%
- Sharpen: sharpest is T4=T4c (73/148 of losers there)
- **Sharp: n=78  W=5/L=73  WR=6.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; middle of band; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L19.  `H60=H60a AND BBP=BBP3 AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=245  W=97/L=148  WR=39.6%
- Sharpen: sharpest is T4=T4c (73/148 of losers there)
- **Sharp: n=78  W=5/L=73  WR=6.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; middle of band; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

### L20.  `H60=H60a AND BBP=BBP3 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=240  W=92/L=148  WR=38.3%
- Sharpen: sharpest is T4=T4c (73/148 of losers there)
- **Sharp: n=78  W=5/L=73  WR=6.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; middle of band; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L21.  `T4=T4c AND BBP=BBP3 AND RSI=RSI4`
- Raw: n=238  W=83/L=155  WR=34.9%
- Sharpen: sharpest is H60=H60a (73/155 of losers there)
- **Sharp: n=78  W=5/L=73  WR=6.4%**
- **Dir: ?**  •  4h trend AGAINST trade; middle of band; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L22.  `T4=T4c AND BBP=BBP3 AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=238  W=83/L=155  WR=34.9%
- Sharpen: sharpest is H60=H60a (73/155 of losers there)
- **Sharp: n=78  W=5/L=73  WR=6.4%**
- **Dir: ?**  •  4h trend AGAINST trade; middle of band; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF60 aligned WITH trade

### L23.  `H20=H20e AND ZS=ZS3 AND direction_exec=long`
- Raw: n=226  W=85/L=141  WR=37.6%
- Sharpen: sharpest is T1=T1a (98/141 of losers there)
- **Sharp: n=143  W=45/L=98  WR=31.5%**
- **Dir: LONG**  •  HTF20 strongly against; zscore -1 to +1 neutral  •  ONLY when 1h trend WITH trade

### L24.  `RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=223  W=82/L=141  WR=36.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=223  W=82/L=141  WR=36.8%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -1 to +1 neutral

### L25.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=222  W=88/L=134  WR=39.6%
- Sharpen: sharpest is T4=T4c (57/134 of losers there)
- **Sharp: n=69  W=12/L=57  WR=17.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(38/29) | H20e(29/37) |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(58/44) | T4c(42/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
