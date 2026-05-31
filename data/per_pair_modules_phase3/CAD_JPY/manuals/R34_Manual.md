# CAD_JPY — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,914**  (W=1,145 / L=769)  -  WR: **59.8%**

## Session distribution

- ny_mid: n=698  W=432/L=266  WR=61.9%
- asia: n=561  W=326/L=235  WR=58.1%
- ny_open: n=238  W=134/L=104  WR=56.3%
- london_open: n=232  W=144/L=88  WR=62.1%
- asia_late: n=78  W=50/L=28  WR=64.1%
- ny_close: n=68  W=33/L=35  WR=48.5%
- london: n=30  W=20/L=10  WR=66.7%
- off_hours: n=9  W=6/L=3  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=139  W=128/L=11  WR=92.1%
- Refine: exclude H60=H60d drops 5/11 losers (45%)
- **Final: n=134  W=128/L=6  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF60 mildly against

### W02.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=139  W=128/L=11  WR=92.1%
- Refine: exclude H60=H60d drops 5/11 losers (45%)
- **Final: n=134  W=128/L=6  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF60 mildly against

### W03.  `T1=T1c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=128  W=111/L=17  WR=86.7%
- Refine: exclude session_bucket=asia drops 8/17 losers (47%)
- **Final: n=102  W=93/L=9  WR=91.2%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=asia

### W04.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=128  W=111/L=17  WR=86.7%
- Refine: exclude session_bucket=asia drops 8/17 losers (47%)
- **Final: n=102  W=93/L=9  WR=91.2%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=asia

### W05.  `H60=H60a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=126  W=108/L=18  WR=85.7%
- Refine: exclude BBP=BBP2 drops 9/18 losers (50%)
- **Final: n=98  W=89/L=9  WR=90.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=london_open  •  AVOID when lower third

### W06.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=117  W=106/L=11  WR=90.6%
- Refine: exclude H60=H60d drops 5/11 losers (45%)
- **Final: n=112  W=106/L=6  WR=94.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF60 mildly against

### W07.  `T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=95  W=86/L=9  WR=90.5%
- Refine: exclude BBP=BBP2 drops 9/9 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=london_open  •  AVOID when lower third

### W08.  `H60=H60a AND T1=T1c AND session_bucket=london_open`
- Raw: n=91  W=82/L=9  WR=90.1%
- Refine: exclude BBP=BBP2 drops 9/9 losers (100%)
- **Final: n=63  W=63/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when lower third

### W09.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=91  W=82/L=9  WR=90.1%
- Refine: exclude BBP=BBP2 drops 9/9 losers (100%)
- **Final: n=63  W=63/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when lower third

### W10.  `H20=H20a AND T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=91  W=80/L=11  WR=87.9%
- Refine: exclude H60=H60d drops 5/11 losers (45%)
- **Final: n=82  W=76/L=6  WR=92.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when HTF60 mildly against

### W11.  `H20=H20a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude H60=H60d drops 11/13 losers (85%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; lower third  •  AVOID when HTF60 mildly against

### W12.  `H20=H20a AND T4=T4a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude H60=H60d drops 11/13 losers (85%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third  •  AVOID when HTF60 mildly against

### W13.  `T1=T1c AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=84  W=75/L=9  WR=89.3%
- Refine: exclude session_bucket=asia drops 7/9 losers (78%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=asia

### W14.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude ZS=ZS4 drops 6/12 losers (50%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W15.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=82  W=76/L=6  WR=92.7%
- Refine: exclude H60=H60d drops 3/6 losers (50%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when HTF60 mildly against

### W16.  `H20=H20a AND T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude H60=H60d drops 5/8 losers (62%)
- **Final: n=77  W=74/L=3  WR=96.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF60 mildly against

### W17.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=79  W=73/L=6  WR=92.4%
- Refine: exclude H60=H60d drops 3/6 losers (50%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when HTF60 mildly against

### W18.  `T1=T1c AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=79  W=73/L=6  WR=92.4%
- Refine: exclude H60=H60d drops 3/6 losers (50%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when HTF60 mildly against

### W19.  `H60=H60a AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=79  W=71/L=8  WR=89.9%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; middle of band; RSI 40-50 lower neutral  •  AVOID when HTF20 aligned WITH trade

### W20.  `H60=H60a AND BBP=BBP3 AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=79  W=71/L=8  WR=89.9%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; middle of band; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W21.  `H60=H60a AND BBP=BBP3 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=79  W=71/L=8  WR=89.9%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; middle of band; RSI 40-50 lower neutral  •  AVOID when HTF20 aligned WITH trade

### W22.  `H60=H60a AND T1=T1c AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; middle of band; RSI 40-50 lower neutral  •  AVOID when HTF20 aligned WITH trade

### W23.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude H20=H20e drops 5/9 losers (56%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W24.  `H20=H20a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=76  W=72/L=4  WR=94.7%
- Refine: exclude session_bucket=asia drops 3/4 losers (75%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=asia

### W25.  `H20=H20a AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=76  W=70/L=6  WR=92.1%
- Refine: exclude H60=H60d drops 3/6 losers (50%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when HTF60 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1a AND RSI=RSI3`
- Raw: n=278  W=100/L=178  WR=36.0%
- Sharpen: sharpest is ZS=ZS2 (74/178 of losers there)
- **Sharp: n=99  W=25/L=74  WR=25.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L02.  `T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=178  W=59/L=119  WR=33.1%
- Sharpen: sharpest is session_bucket=london_open (21/119 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L03.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=150  W=45/L=105  WR=30.0%
- Sharpen: sharpest is direction_exec=long (54/105 of losers there)
- **Sharp: n=70  W=16/L=54  WR=22.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when long

### L04.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=149  W=58/L=91  WR=38.9%
- Sharpen: sharpest is H20=H20e (91/91 of losers there)
- **Sharp: n=126  W=35/L=91  WR=27.8%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L05.  `H20=H20e AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=141  W=42/L=99  WR=29.8%
- Sharpen: sharpest is H60=H60a (30/99 of losers there)
- **Sharp: n=34  W=4/L=30  WR=11.8%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L06.  `H20=H20e AND T1=T1a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=139  W=52/L=87  WR=37.4%
- Sharpen: sharpest is BBP=BBP2 (47/87 of losers there)
- **Sharp: n=57  W=10/L=47  WR=17.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when lower third

### L07.  `H20=H20e AND T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=126  W=35/L=91  WR=27.8%
- Sharpen: sharpest is session_bucket=ny_mid (47/91 of losers there)
- **Sharp: n=57  W=10/L=47  WR=17.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L08.  `H20=H20e AND T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=121  W=46/L=75  WR=38.0%
- Sharpen: sharpest is direction_exec=long (40/75 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when long

### L09.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=121  W=47/L=74  WR=38.8%
- Sharpen: sharpest is H20=H20e (74/74 of losers there)
- **Sharp: n=99  W=25/L=74  WR=25.3%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L10.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=121  W=47/L=74  WR=38.8%
- Sharpen: sharpest is H20=H20e (74/74 of losers there)
- **Sharp: n=99  W=25/L=74  WR=25.3%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L11.  `H60=H60d AND T1=T1a AND T4=T4a`
- Raw: n=115  W=43/L=72  WR=37.4%
- Sharpen: sharpest is BBP=BBP1 (18/72 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when just touched lower band

### L12.  `H60=H60d AND T1=T1a AND direction_exec=short`
- Raw: n=115  W=43/L=72  WR=37.4%
- Sharpen: sharpest is BBP=BBP1 (18/72 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend WITH trade  •  ONLY when just touched lower band

### L13.  `H60=H60d AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=115  W=43/L=72  WR=37.4%
- Sharpen: sharpest is BBP=BBP1 (18/72 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when just touched lower band

### L14.  `H20=H20e AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=113  W=43/L=70  WR=38.1%
- Sharpen: sharpest is H60=H60b (23/70 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when HTF60 slightly aligned

### L15.  `H20=H20e AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=110  W=30/L=80  WR=27.3%
- Sharpen: sharpest is H60=H60a (30/80 of losers there)
- **Sharp: n=34  W=4/L=30  WR=11.8%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 aligned WITH trade

### L16.  `H20=H20e AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=110  W=30/L=80  WR=27.3%
- Sharpen: sharpest is H60=H60a (30/80 of losers there)
- **Sharp: n=34  W=4/L=30  WR=11.8%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 aligned WITH trade

### L17.  `H20=H20e AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=103  W=40/L=63  WR=38.8%
- Sharpen: sharpest is RSI=RSI3 (47/63 of losers there)
- **Sharp: n=60  W=13/L=47  WR=21.7%**
- **Dir: ?**  •  HTF20 strongly against; lower third; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L18.  `H20=H20e AND T1=T1a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=100  W=37/L=63  WR=37.0%
- Sharpen: sharpest is RSI=RSI3 (47/63 of losers there)
- **Sharp: n=57  W=10/L=47  WR=17.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L19.  `H20=H20e AND T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=99  W=25/L=74  WR=25.3%
- Sharpen: sharpest is H60=H60a (25/74 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 aligned WITH trade

### L20.  `H20=H20e AND T4=T4a AND ZS=ZS2`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is RSI=RSI3 (33/61 of losers there)
- **Sharp: n=43  W=10/L=33  WR=23.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L21.  `H20=H20e AND T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is RSI=RSI3 (33/61 of losers there)
- **Sharp: n=43  W=10/L=33  WR=23.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L22.  `H20=H20e AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is RSI=RSI3 (33/61 of losers there)
- **Sharp: n=43  W=10/L=33  WR=23.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L23.  `H20=H20e AND T4=T4a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is RSI=RSI3 (33/61 of losers there)
- **Sharp: n=43  W=10/L=33  WR=23.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L24.  `H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=96  W=31/L=65  WR=32.3%
- Sharpen: sharpest is RSI=RSI3 (32/65 of losers there)
- **Sharp: n=40  W=8/L=32  WR=20.0%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london_open  •  ONLY when RSI 40-50 lower neutral

### L25.  `T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=95  W=32/L=63  WR=33.7%
- Sharpen: sharpest is H20=H20e (54/63 of losers there)
- **Sharp: n=70  W=16/L=54  WR=22.9%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(51/42) | H20e(42/51) |
| H60 | — | — |
| T1 | T1c(56/44) | T1a(44/56) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
