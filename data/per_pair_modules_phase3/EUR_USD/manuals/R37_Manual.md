# EUR_USD — R37 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,349**  (W=2,108 / L=1,241)  -  WR: **62.9%**

## Session distribution

- london_open: n=826  W=513/L=313  WR=62.1%
- asia: n=564  W=354/L=210  WR=62.8%
- london: n=526  W=327/L=199  WR=62.2%
- ny_open: n=489  W=302/L=187  WR=61.8%
- ny_close: n=385  W=251/L=134  WR=65.2%
- ny_mid: n=371  W=239/L=132  WR=64.4%
- asia_late: n=177  W=116/L=61  WR=65.5%
- off_hours: n=11  W=6/L=5  WR=54.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=180  W=153/L=27  WR=85.0%
- Refine: exclude H20=H20b drops 10/27 losers (37%)
- **Final: n=167  W=150/L=17  WR=89.8%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W02.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=151  W=132/L=19  WR=87.4%
- Refine: exclude H20=H20b drops 10/19 losers (53%)
- **Final: n=138  W=129/L=9  WR=93.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W03.  `T1=T1a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=146  W=125/L=21  WR=85.6%
- Refine: exclude RSI=RSI3 drops 10/21 losers (48%)
- **Final: n=113  W=102/L=11  WR=90.3%**
- **Dir: ?**  •  1h trend WITH trade; lower third; session=asia  •  AVOID when RSI 40-50 lower neutral

### W04.  `T4=T4a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=143  W=125/L=18  WR=87.4%
- Refine: exclude H60=H60a drops 15/18 losers (83%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: ?**  •  4h trend WITH trade; lower third; session=asia  •  AVOID when HTF60 aligned WITH trade

### W05.  `BBP=BBP2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=143  W=125/L=18  WR=87.4%
- Refine: exclude H60=H60a drops 15/18 losers (83%)
- **Final: n=75  W=72/L=3  WR=96.0%**
- **Dir: SHORT**  •  lower third; session=asia  •  AVOID when HTF60 aligned WITH trade

### W06.  `T1=T1a AND BBP=BBP2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=143  W=125/L=18  WR=87.4%
- Refine: exclude H60=H60a drops 15/18 losers (83%)
- **Final: n=75  W=72/L=3  WR=96.0%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; session=asia  •  AVOID when HTF60 aligned WITH trade

### W07.  `T1=T1a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=141  W=123/L=18  WR=87.2%
- Refine: exclude RSI=RSI3 drops 9/18 losers (50%)
- **Final: n=111  W=102/L=9  WR=91.9%**
- **Dir: ?**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when RSI 40-50 lower neutral

### W08.  `T1=T1a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=141  W=123/L=18  WR=87.2%
- Refine: exclude RSI=RSI3 drops 9/18 losers (50%)
- **Final: n=111  W=102/L=9  WR=91.9%**
- **Dir: ?**  •  1h trend WITH trade; lower third; zscore -2 to -1 oversold; session=asia  •  AVOID when RSI 40-50 lower neutral

### W09.  `ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=138  W=123/L=15  WR=89.1%
- Refine: exclude H60=H60a drops 12/15 losers (80%)
- **Final: n=75  W=72/L=3  WR=96.0%**
- **Dir: SHORT**  •  zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

### W10.  `T1=T1a AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=138  W=123/L=15  WR=89.1%
- Refine: exclude H60=H60a drops 12/15 losers (80%)
- **Final: n=75  W=72/L=3  WR=96.0%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

### W11.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=138  W=123/L=15  WR=89.1%
- Refine: exclude H60=H60a drops 12/15 losers (80%)
- **Final: n=75  W=72/L=3  WR=96.0%**
- **Dir: SHORT**  •  lower third; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

### W12.  `T4=T4a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=137  W=121/L=16  WR=88.3%
- Refine: exclude H60=H60a drops 13/16 losers (81%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: ?**  •  4h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

### W13.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=137  W=121/L=16  WR=88.3%
- Refine: exclude H60=H60a drops 13/16 losers (81%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third; session=asia  •  AVOID when HTF60 aligned WITH trade

### W14.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=137  W=121/L=16  WR=88.3%
- Refine: exclude H60=H60a drops 13/16 losers (81%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: ?**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

### W15.  `T4=T4a AND BBP=BBP2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=137  W=121/L=16  WR=88.3%
- Refine: exclude H60=H60a drops 13/16 losers (81%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: SHORT**  •  4h trend WITH trade; lower third; session=asia  •  AVOID when HTF60 aligned WITH trade

### W16.  `T1=T1a AND T4=T4a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=133  W=119/L=14  WR=89.5%
- Refine: exclude H60=H60a drops 11/14 losers (79%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

### W17.  `T4=T4a AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=133  W=119/L=14  WR=89.5%
- Refine: exclude H60=H60a drops 11/14 losers (79%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

### W18.  `H20=H20a AND T4=T4a AND direction_exec=long`
- Raw: n=117  W=105/L=12  WR=89.7%
- Refine: exclude BBP=BBP5 drops 4/12 losers (33%)
- **Final: n=109  W=101/L=8  WR=92.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade  •  AVOID when just touched upper band

### W19.  `H20=H20a AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=117  W=105/L=12  WR=89.7%
- Refine: exclude BBP=BBP5 drops 4/12 losers (33%)
- **Final: n=109  W=101/L=8  WR=92.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when just touched upper band

### W20.  `T1=T1a AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=101  W=92/L=9  WR=91.1%
- Refine: exclude H60=H60a drops 8/9 losers (89%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 30-40 weak; session=asia  •  AVOID when HTF60 aligned WITH trade

### W21.  `T4=T4a AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=101  W=92/L=9  WR=91.1%
- Refine: exclude H60=H60a drops 8/9 losers (89%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 30-40 weak; session=asia  •  AVOID when HTF60 aligned WITH trade

### W22.  `BBP=BBP2 AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=101  W=92/L=9  WR=91.1%
- Refine: exclude H60=H60a drops 8/9 losers (89%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: SHORT**  •  lower third; RSI 30-40 weak; session=asia  •  AVOID when HTF60 aligned WITH trade

### W23.  `T1=T1a AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=99  W=92/L=7  WR=92.9%
- Refine: exclude H60=H60a drops 6/7 losers (86%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

### W24.  `RSI=RSI2 AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=99  W=92/L=7  WR=92.9%
- Refine: exclude H60=H60a drops 6/7 losers (86%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

### W25.  `T4=T4a AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=98  W=90/L=8  WR=91.8%
- Refine: exclude H60=H60a drops 7/8 losers (88%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=239  W=95/L=144  WR=39.7%
- Sharpen: sharpest is H60=H60a (53/144 of losers there)
- **Sharp: n=68  W=15/L=53  WR=22.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L02.  `T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=228  W=86/L=142  WR=37.7%
- Sharpen: sharpest is H60=H60a (51/142 of losers there)
- **Sharp: n=62  W=11/L=51  WR=17.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L03.  `T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=225  W=86/L=139  WR=38.2%
- Sharpen: sharpest is H60=H60a (51/139 of losers there)
- **Sharp: n=62  W=11/L=51  WR=17.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L04.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=225  W=86/L=139  WR=38.2%
- Sharpen: sharpest is H60=H60a (51/139 of losers there)
- **Sharp: n=62  W=11/L=51  WR=17.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L05.  `T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=174  W=62/L=112  WR=35.6%
- Sharpen: sharpest is H60=H60a (44/112 of losers there)
- **Sharp: n=51  W=7/L=44  WR=13.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when HTF60 aligned WITH trade

### L06.  `T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=169  W=63/L=106  WR=37.3%
- Sharpen: sharpest is ZS=ZS2 (46/106 of losers there)
- **Sharp: n=58  W=12/L=46  WR=20.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when zscore -2 to -1 oversold

### L07.  `RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=169  W=63/L=106  WR=37.3%
- Sharpen: sharpest is ZS=ZS2 (46/106 of losers there)
- **Sharp: n=58  W=12/L=46  WR=20.7%**
- **Dir: LONG**  •  RSI 30-40 weak; session=asia  •  ONLY when zscore -2 to -1 oversold

### L08.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=169  W=63/L=106  WR=37.3%
- Sharpen: sharpest is ZS=ZS2 (46/106 of losers there)
- **Sharp: n=58  W=12/L=46  WR=20.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when zscore -2 to -1 oversold

### L09.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=167  W=62/L=105  WR=37.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=167  W=62/L=105  WR=37.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third; RSI 30-40 weak

### L10.  `H60=H60e AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=165  W=64/L=101  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=165  W=64/L=101  WR=38.8%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; RSI 30-40 weak

### L11.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=159  W=55/L=104  WR=34.6%
- Sharpen: sharpest is H60=H60a (37/104 of losers there)
- **Sharp: n=42  W=5/L=37  WR=11.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when HTF60 aligned WITH trade

### L12.  `T4=T4c AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=159  W=55/L=104  WR=34.6%
- Sharpen: sharpest is H60=H60a (37/104 of losers there)
- **Sharp: n=42  W=5/L=37  WR=11.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when HTF60 aligned WITH trade

### L13.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=157  W=58/L=99  WR=36.9%
- Sharpen: sharpest is H20=H20a (30/99 of losers there)
- **Sharp: n=38  W=8/L=30  WR=21.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when HTF20 aligned WITH trade

### L14.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=149  W=57/L=92  WR=38.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=149  W=57/L=92  WR=38.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold

### L15.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=139  W=54/L=85  WR=38.8%
- Sharpen: sharpest is H20=H20a (26/85 of losers there)
- **Sharp: n=34  W=8/L=26  WR=23.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

### L16.  `T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=136  W=54/L=82  WR=39.7%
- Sharpen: sharpest is RSI=RSI2 (70/82 of losers there)
- **Sharp: n=99  W=29/L=70  WR=29.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 30-40 weak

### L17.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=136  W=54/L=82  WR=39.7%
- Sharpen: sharpest is RSI=RSI2 (70/82 of losers there)
- **Sharp: n=99  W=29/L=70  WR=29.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 30-40 weak

### L18.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=135  W=54/L=81  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=54/L=81  WR=40.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; RSI 30-40 weak

### L19.  `T4=T4c AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=128  W=50/L=78  WR=39.1%
- Sharpen: sharpest is T1=T1c (70/78 of losers there)
- **Sharp: n=99  W=29/L=70  WR=29.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L20.  `H20=H20e AND H60=H60c AND RSI=RSI2`
- Raw: n=128  W=51/L=77  WR=39.8%
- Sharpen: sharpest is T4=T4c (56/77 of losers there)
- **Sharp: n=83  W=27/L=56  WR=32.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 neutral; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L21.  `H20=H20a AND T4=T4c AND session_bucket=asia`
- Raw: n=125  W=49/L=76  WR=39.2%
- Sharpen: sharpest is H60=H60a (40/76 of losers there)
- **Sharp: n=54  W=14/L=40  WR=25.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L22.  `H20=H20a AND H60=H60e AND T4=T4c AND RSI=RSI2`
- Raw: n=122  W=41/L=81  WR=33.6%
- Sharpen: sharpest is session_bucket=ny_mid (18/81 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_mid

### L23.  `H20=H20a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=117  W=43/L=74  WR=36.8%
- Sharpen: sharpest is H60=H60a (38/74 of losers there)
- **Sharp: n=46  W=8/L=38  WR=17.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L24.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=117  W=43/L=74  WR=36.8%
- Sharpen: sharpest is H60=H60a (38/74 of losers there)
- **Sharp: n=46  W=8/L=38  WR=17.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L25.  `T1=T1c AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=113  W=36/L=77  WR=31.9%
- Sharpen: sharpest is BBP=BBP0 (20/77 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_mid  •  ONLY when deep below lower band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(61/40) | T1c(39/60) |
| T4 | T4a(62/39) | T4c(38/61) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(58/43) | long(42/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
