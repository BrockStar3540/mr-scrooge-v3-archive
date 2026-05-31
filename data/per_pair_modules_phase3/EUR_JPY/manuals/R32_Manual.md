# EUR_JPY — R32 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **4,544**  (W=2,649 / L=1,895)  -  WR: **58.3%**

## Session distribution

- asia: n=1274  W=748/L=526  WR=58.7%
- ny_mid: n=896  W=518/L=378  WR=57.8%
- ny_close: n=695  W=404/L=291  WR=58.1%
- london_open: n=466  W=285/L=181  WR=61.2%
- ny_open: n=442  W=254/L=188  WR=57.5%
- london: n=396  W=239/L=157  WR=60.4%
- asia_late: n=200  W=105/L=95  WR=52.5%
- off_hours: n=175  W=96/L=79  WR=54.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60a AND session_bucket=london`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude ZS=ZS4 drops 6/9 losers (67%)
- **Final: n=80  W=77/L=3  WR=96.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=london  •  AVOID when zscore +1 to +2 overbought

### W02.  `H60=H60a AND T4=T4c AND session_bucket=london`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude ZS=ZS4 drops 6/9 losers (67%)
- **Final: n=80  W=77/L=3  WR=96.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when zscore +1 to +2 overbought

### W03.  `H20=H20e AND H60=H60a AND T4=T4c AND session_bucket=london`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude ZS=ZS4 drops 6/9 losers (67%)
- **Final: n=80  W=77/L=3  WR=96.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when zscore +1 to +2 overbought

### W04.  `H20=H20e AND H60=H60a AND direction_exec=long AND session_bucket=london`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude ZS=ZS4 drops 6/9 losers (67%)
- **Final: n=80  W=77/L=3  WR=96.2%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=london  •  AVOID when zscore +1 to +2 overbought

### W05.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=london`
- Raw: n=108  W=99/L=9  WR=91.7%
- Refine: exclude ZS=ZS4 drops 6/9 losers (67%)
- **Final: n=80  W=77/L=3  WR=96.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when zscore +1 to +2 overbought

### W06.  `H20=H20d AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=100  W=90/L=10  WR=90.0%
- Refine: exclude session_bucket=ny_open drops 10/10 losers (100%)
- **Final: n=76  W=76/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=ny_open

### W07.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude H20=H20a drops 10/13 losers (77%)
- **Final: n=42  W=39/L=3  WR=92.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 aligned WITH trade

### W08.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude RSI=RSI3 drops 8/11 losers (73%)
- **Final: n=70  W=67/L=3  WR=95.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london  •  AVOID when RSI 40-50 lower neutral

### W09.  `H20=H20e AND H60=H60a AND T1=T1a AND session_bucket=london`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude RSI=RSI3 drops 5/8 losers (62%)
- **Final: n=70  W=67/L=3  WR=95.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; session=london  •  AVOID when RSI 40-50 lower neutral

### W10.  `H60=H60a AND T1=T1a AND T4=T4c AND session_bucket=london`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude RSI=RSI3 drops 5/8 losers (62%)
- **Final: n=70  W=67/L=3  WR=95.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when RSI 40-50 lower neutral

### W11.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude H60=H60e drops 9/9 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral; session=ny_close  •  AVOID when HTF60 strongly against

### W12.  `H20=H20d AND T4=T4a AND BBP=BBP2`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude session_bucket=ny_open drops 4/9 losers (44%)
- **Final: n=78  W=73/L=5  WR=93.6%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; lower third  •  AVOID when session=ny_open

### W13.  `H60=H60b AND T1=T1c AND RSI=RSI4`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude H20=H20a drops 10/10 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W14.  `H60=H60b AND T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude H20=H20a drops 10/10 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W15.  `H60=H60b AND T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude H20=H20a drops 10/10 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 slightly aligned; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W16.  `H60=H60b AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude H20=H20a drops 10/10 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 aligned WITH trade

### W17.  `T4=T4a AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=78  W=71/L=7  WR=91.0%
- Refine: exclude H60=H60e drops 7/7 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=ny_close  •  AVOID when HTF60 strongly against

### W18.  `H60=H60e AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: no further refinement
- **Final: n=78  W=67/L=11  WR=85.9%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 50-60 upper neutral; session=asia

### W19.  `H20=H20d AND T4=T4a AND ZS=ZS2`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude session_bucket=ny_open drops 4/9 losers (44%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W20.  `H20=H20d AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude session_bucket=ny_open drops 4/9 losers (44%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W21.  `H20=H20d AND T1=T1c AND T4=T4a AND session_bucket=ny_close`
- Raw: n=71  W=67/L=4  WR=94.4%
- Refine: exclude BBP=BBP4 drops 4/4 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  AVOID when upper third

### W22.  `H60=H60a AND RSI=RSI4 AND session_bucket=london`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/3 losers (67%)
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london  •  AVOID when strategy=delta_tag_and_go_v2

### W23.  `H20=H20e AND H60=H60a AND RSI=RSI4 AND session_bucket=london`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/3 losers (67%)
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london  •  AVOID when strategy=delta_tag_and_go_v2

### W24.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND session_bucket=london`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/3 losers (67%)
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; session=london  •  AVOID when strategy=delta_tag_and_go_v2

### W25.  `H60=H60a AND T4=T4c AND RSI=RSI4 AND session_bucket=london`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/3 losers (67%)
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london  •  AVOID when strategy=delta_tag_and_go_v2

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=170  W=66/L=104  WR=38.8%
- Sharpen: sharpest is BBP=BBP0 (31/104 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when deep below lower band

### L02.  `H20=H20e AND T1=T1a AND RSI=RSI3`
- Raw: n=161  W=55/L=106  WR=34.2%
- Sharpen: sharpest is H60=H60c (46/106 of losers there)
- **Sharp: n=54  W=8/L=46  WR=14.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 neutral

### L03.  `T4=T4a AND direction_exec=short AND session_bucket=london`
- Raw: n=141  W=56/L=85  WR=39.7%
- Sharpen: sharpest is H60=H60e (64/85 of losers there)
- **Sharp: n=87  W=23/L=64  WR=26.4%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london  •  ONLY when HTF60 strongly against

### L04.  `T4=T4c AND BBP=BBP3 AND direction_exec=short`
- Raw: n=139  W=54/L=85  WR=38.8%
- Sharpen: sharpest is session_bucket=london_open (19/85 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; middle of band  •  ONLY when session=london_open

### L05.  `T4=T4c AND BBP=BBP3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=139  W=54/L=85  WR=38.8%
- Sharpen: sharpest is session_bucket=london_open (19/85 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; middle of band; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L06.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=129  W=47/L=82  WR=36.4%
- Sharpen: sharpest is H60=H60c (46/82 of losers there)
- **Sharp: n=54  W=8/L=46  WR=14.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF60 neutral

### L07.  `H60=H60d AND T4=T4a AND direction_exec=short`
- Raw: n=126  W=45/L=81  WR=35.7%
- Sharpen: sharpest is T1=T1a (72/81 of losers there)
- **Sharp: n=90  W=18/L=72  WR=20.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend WITH trade  •  ONLY when 1h trend WITH trade

### L08.  `H60=H60d AND RSI=RSI4 AND direction_exec=short`
- Raw: n=124  W=47/L=77  WR=37.9%
- Sharpen: sharpest is T1=T1a (43/77 of losers there)
- **Sharp: n=52  W=9/L=43  WR=17.3%**
- **Dir: SHORT**  •  HTF60 mildly against; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L09.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=119  W=47/L=72  WR=39.5%
- Sharpen: sharpest is H60=H60c (24/72 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when HTF60 neutral

### L10.  `H60=H60e AND direction_exec=short AND session_bucket=london`
- Raw: n=117  W=42/L=75  WR=35.9%
- Sharpen: sharpest is H20=H20a (64/75 of losers there)
- **Sharp: n=87  W=23/L=64  WR=26.4%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london  •  ONLY when HTF20 aligned WITH trade

### L11.  `H60=H60d AND T4=T4a AND session_bucket=asia`
- Raw: n=116  W=45/L=71  WR=38.8%
- Sharpen: sharpest is T1=T1a (62/71 of losers there)
- **Sharp: n=80  W=18/L=62  WR=22.5%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend WITH trade; session=asia  •  ONLY when 1h trend WITH trade

### L12.  `H60=H60d AND direction_exec=short AND session_bucket=asia`
- Raw: n=116  W=45/L=71  WR=38.8%
- Sharpen: sharpest is T1=T1a (62/71 of losers there)
- **Sharp: n=80  W=18/L=62  WR=22.5%**
- **Dir: SHORT**  •  HTF60 mildly against; session=asia  •  ONLY when 1h trend WITH trade

### L13.  `H60=H60d AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=116  W=45/L=71  WR=38.8%
- Sharpen: sharpest is T1=T1a (62/71 of losers there)
- **Sharp: n=80  W=18/L=62  WR=22.5%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend WITH trade; session=asia  •  ONLY when 1h trend WITH trade

### L14.  `H60=H60d AND T1=T1a AND direction_exec=short`
- Raw: n=111  W=26/L=85  WR=23.4%
- Sharpen: sharpest is ZS=ZS4 (30/85 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend WITH trade  •  ONLY when zscore +1 to +2 overbought

### L15.  `T1=T1a AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=111  W=33/L=78  WR=29.7%
- Sharpen: sharpest is H20=H20e (38/78 of losers there)
- **Sharp: n=43  W=5/L=38  WR=11.6%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when HTF20 strongly against

### L16.  `H20=H20a AND T4=T4c AND direction_exec=short`
- Raw: n=111  W=42/L=69  WR=37.8%
- Sharpen: sharpest is session_bucket=london_open (14/69 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=london_open

### L17.  `H20=H20a AND H60=H60e AND RSI=RSI4`
- Raw: n=107  W=37/L=70  WR=34.6%
- Sharpen: sharpest is session_bucket=london (44/70 of losers there)
- **Sharp: n=56  W=12/L=44  WR=21.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when session=london

### L18.  `H20=H20a AND H60=H60e AND T1=T1c AND RSI=RSI4`
- Raw: n=107  W=37/L=70  WR=34.6%
- Sharpen: sharpest is session_bucket=london (44/70 of losers there)
- **Sharp: n=56  W=12/L=44  WR=21.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=london

### L19.  `H20=H20a AND H60=H60e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=107  W=37/L=70  WR=34.6%
- Sharpen: sharpest is session_bucket=london (44/70 of losers there)
- **Sharp: n=56  W=12/L=44  WR=21.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when session=london

### L20.  `H20=H20e AND T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=103  W=30/L=73  WR=29.1%
- Sharpen: sharpest is H60=H60c (46/73 of losers there)
- **Sharp: n=54  W=8/L=46  WR=14.8%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 neutral

### L21.  `H60=H60d AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is T1=T1a (30/62 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: ?**  •  HTF60 mildly against; upper third; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L22.  `H60=H60e AND T4=T4c AND BBP=BBP3 AND direction_exec=short`
- Raw: n=102  W=39/L=63  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=102  W=39/L=63  WR=38.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; middle of band

### L23.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=98  W=37/L=61  WR=37.8%
- Sharpen: sharpest is H20=H20d (35/61 of losers there)
- **Sharp: n=39  W=4/L=35  WR=10.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF20 mildly against

### L24.  `H20=H20e AND T1=T1a AND BBP=BBP2`
- Raw: n=97  W=30/L=67  WR=30.9%
- Sharpen: sharpest is session_bucket=ny_mid (37/67 of losers there)
- **Sharp: n=48  W=11/L=37  WR=22.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third  •  ONLY when session=ny_mid

### L25.  `H20=H20a AND H60=H60e AND T4=T4a AND RSI=RSI4`
- Raw: n=97  W=33/L=64  WR=34.0%
- Sharpen: sharpest is session_bucket=london (44/64 of losers there)
- **Sharp: n=56  W=12/L=44  WR=21.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=london

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1c(53/47) | T1a(47/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
