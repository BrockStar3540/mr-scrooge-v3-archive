# CHF_JPY — R31 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,722**  (W=2,251 / L=1,471)  -  WR: **60.5%**

## Session distribution

- asia: n=1283  W=795/L=488  WR=62.0%
- ny_mid: n=783  W=479/L=304  WR=61.2%
- london_open: n=473  W=276/L=197  WR=58.4%
- ny_close: n=391  W=234/L=157  WR=59.8%
- london: n=253  W=160/L=93  WR=63.2%
- ny_open: n=252  W=156/L=96  WR=61.9%
- off_hours: n=155  W=72/L=83  WR=46.5%
- asia_late: n=132  W=79/L=53  WR=59.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=155  W=135/L=20  WR=87.1%
- Refine: exclude T1=T1a drops 14/20 losers (70%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: LONG**  •  deep below lower band; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W02.  `H60=H60a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude H20=H20d drops 6/21 losers (29%)
- **Final: n=133  W=118/L=15  WR=88.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band  •  AVOID when HTF20 mildly against

### W03.  `H60=H60a AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=141  W=121/L=20  WR=85.8%
- Refine: exclude H20=H20d drops 6/20 losers (30%)
- **Final: n=132  W=118/L=14  WR=89.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when HTF20 mildly against

### W04.  `T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=138  W=123/L=15  WR=89.1%
- Refine: exclude ZS=ZS1 drops 15/15 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band  •  AVOID when zscore -3 to -2 deep oversold

### W05.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=137  W=123/L=14  WR=89.8%
- Refine: exclude ZS=ZS1 drops 14/14 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when zscore -3 to -2 deep oversold

### W06.  `H60=H60a AND T4=T4c AND BBP=BBP0`
- Raw: n=124  W=109/L=15  WR=87.9%
- Refine: exclude ZS=ZS1 drops 15/15 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when zscore -3 to -2 deep oversold

### W07.  `H60=H60a AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=124  W=109/L=15  WR=87.9%
- Refine: exclude ZS=ZS1 drops 15/15 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when zscore -3 to -2 deep oversold

### W08.  `H60=H60a AND T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=123  W=109/L=14  WR=88.6%
- Refine: exclude ZS=ZS1 drops 14/14 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when zscore -3 to -2 deep oversold

### W09.  `H20=H20a AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude session_bucket=asia drops 5/13 losers (38%)
- **Final: n=89  W=81/L=8  WR=91.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W10.  `T1=T1a AND BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=95  W=84/L=11  WR=88.4%
- Refine: exclude session_bucket=ny_close drops 4/11 losers (36%)
- **Final: n=91  W=84/L=7  WR=92.3%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W11.  `H60=H60a AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude H20=H20e drops 8/14 losers (57%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W12.  `BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude H20=H20e drops 8/14 losers (57%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: LONG**  •  deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W13.  `T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=87  W=80/L=7  WR=92.0%
- Refine: exclude session_bucket=ny_mid drops 6/7 losers (86%)
- **Final: n=65  W=64/L=1  WR=98.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_mid

### W14.  `T1=T1c AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=86  W=80/L=6  WR=93.0%
- Refine: exclude session_bucket=ny_mid drops 6/6 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W15.  `H20=H20a AND H60=H60a AND BBP=BBP0`
- Raw: n=85  W=78/L=7  WR=91.8%
- Refine: exclude session_bucket=ny_mid drops 6/7 losers (86%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band  •  AVOID when session=ny_mid

### W16.  `H20=H20a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=85  W=78/L=7  WR=91.8%
- Refine: exclude session_bucket=ny_mid drops 6/7 losers (86%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep below lower band  •  AVOID when session=ny_mid

### W17.  `H20=H20a AND H60=H60a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=85  W=78/L=7  WR=91.8%
- Refine: exclude session_bucket=ny_mid drops 6/7 losers (86%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band  •  AVOID when session=ny_mid

### W18.  `H20=H20a AND H60=H60a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=84  W=78/L=6  WR=92.9%
- Refine: exclude session_bucket=ny_mid drops 6/6 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W19.  `H20=H20a AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=84  W=78/L=6  WR=92.9%
- Refine: exclude session_bucket=ny_mid drops 6/6 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W20.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude T1=T1c drops 6/10 losers (60%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=asia  •  AVOID when 1h trend AGAINST trade

### W21.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=78  W=71/L=7  WR=91.0%
- Refine: exclude session_bucket=ny_mid drops 6/7 losers (86%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_mid

### W22.  `H20=H20a AND T4=T4c AND BBP=BBP0`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude session_bucket=ny_mid drops 6/7 losers (86%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_mid

### W23.  `H20=H20a AND H60=H60a AND T4=T4c AND BBP=BBP0`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude session_bucket=ny_mid drops 6/7 losers (86%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_mid

### W24.  `H20=H20a AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude session_bucket=ny_mid drops 6/7 losers (86%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_mid

### W25.  `H20=H20a AND T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=75  W=69/L=6  WR=92.0%
- Refine: exclude session_bucket=ny_mid drops 6/6 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=154  W=61/L=93  WR=39.6%
- Sharpen: sharpest is T1=T1c (66/93 of losers there)
- **Sharp: n=97  W=31/L=66  WR=32.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend AGAINST trade

### L02.  `RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=154  W=61/L=93  WR=39.6%
- Sharpen: sharpest is T1=T1c (66/93 of losers there)
- **Sharp: n=97  W=31/L=66  WR=32.0%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend AGAINST trade

### L03.  `H60=H60e AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=154  W=61/L=93  WR=39.6%
- Sharpen: sharpest is T1=T1c (66/93 of losers there)
- **Sharp: n=97  W=31/L=66  WR=32.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend AGAINST trade

### L04.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=123  W=44/L=79  WR=35.8%
- Sharpen: sharpest is session_bucket=asia (37/79 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L05.  `H20=H20e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=122  W=45/L=77  WR=36.9%
- Sharpen: sharpest is T1=T1c (50/77 of losers there)
- **Sharp: n=65  W=15/L=50  WR=23.1%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend AGAINST trade

### L06.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=122  W=45/L=77  WR=36.9%
- Sharpen: sharpest is T1=T1c (50/77 of losers there)
- **Sharp: n=65  W=15/L=50  WR=23.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend AGAINST trade

### L07.  `H20=H20e AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=122  W=45/L=77  WR=36.9%
- Sharpen: sharpest is T1=T1c (50/77 of losers there)
- **Sharp: n=65  W=15/L=50  WR=23.1%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend AGAINST trade

### L08.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=121  W=45/L=76  WR=37.2%
- Sharpen: sharpest is ZS=ZS5 (37/76 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `T4=T4a AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=121  W=45/L=76  WR=37.2%
- Sharpen: sharpest is ZS=ZS5 (37/76 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L10.  `H20=H20e AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=120  W=42/L=78  WR=35.0%
- Sharpen: sharpest is session_bucket=asia (27/78 of losers there)
- **Sharp: n=34  W=7/L=27  WR=20.6%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; RSI 50-60 upper neutral  •  ONLY when session=asia

### L11.  `H20=H20e AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=120  W=42/L=78  WR=35.0%
- Sharpen: sharpest is session_bucket=asia (27/78 of losers there)
- **Sharp: n=34  W=7/L=27  WR=20.6%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L12.  `H60=H60e AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=120  W=48/L=72  WR=40.0%
- Sharpen: sharpest is H20=H20e (51/72 of losers there)
- **Sharp: n=72  W=21/L=51  WR=29.2%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L13.  `H60=H60e AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=120  W=48/L=72  WR=40.0%
- Sharpen: sharpest is H20=H20e (51/72 of losers there)
- **Sharp: n=72  W=21/L=51  WR=29.2%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L14.  `H60=H60e AND BBP=BBP5 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=120  W=48/L=72  WR=40.0%
- Sharpen: sharpest is H20=H20e (51/72 of losers there)
- **Sharp: n=72  W=21/L=51  WR=29.2%**
- **Dir: SHORT**  •  HTF60 strongly against; just touched upper band; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L15.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=115  W=35/L=80  WR=30.4%
- Sharpen: sharpest is H20=H20c (17/80 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF20 neutral

### L16.  `H20=H20e AND H60=H60a AND T4=T4c AND RSI=RSI3`
- Raw: n=115  W=46/L=69  WR=40.0%
- Sharpen: sharpest is ZS=ZS2 (24/69 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L17.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=115  W=46/L=69  WR=40.0%
- Sharpen: sharpest is ZS=ZS2 (24/69 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L18.  `T1=T1c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=106  W=37/L=69  WR=34.9%
- Sharpen: sharpest is ZS=ZS5 (63/69 of losers there)
- **Sharp: n=88  W=25/L=63  WR=28.4%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L19.  `H60=H60e AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=99  W=29/L=70  WR=29.3%
- Sharpen: sharpest is direction_exec=short (70/70 of losers there)
- **Sharp: n=85  W=15/L=70  WR=17.6%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; RSI 40-50 lower neutral  •  ONLY when short

### L20.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=97  W=31/L=66  WR=32.0%
- Sharpen: sharpest is ZS=ZS5 (33/66 of losers there)
- **Sharp: n=39  W=6/L=33  WR=15.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L21.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=97  W=31/L=66  WR=32.0%
- Sharpen: sharpest is ZS=ZS5 (33/66 of losers there)
- **Sharp: n=39  W=6/L=33  WR=15.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L22.  `H20=H20e AND H60=H60e AND T1=T1a AND ZS=ZS1`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is session_bucket=london_open (15/59 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L23.  `H20=H20e AND T1=T1a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is session_bucket=london_open (15/59 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L24.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=96  W=35/L=61  WR=36.5%
- Sharpen: sharpest is BBP=BBP6 (23/61 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L25.  `H60=H60a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=95  W=35/L=60  WR=36.8%
- Sharpen: sharpest is T4=T4c (23/60 of losers there)
- **Sharp: n=29  W=6/L=23  WR=20.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; session=ny_mid  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(44/35) | H20e(35/43) |
| H60 | H60a(51/44) | H60e(43/49) |
| T1 | — | — |
| T4 | T4c(54/48) | T4a(46/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/46) | short(45/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
