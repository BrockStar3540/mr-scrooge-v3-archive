# EUR_USD — R39 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,132**  (W=1,992 / L=1,140)  -  WR: **63.6%**

## Session distribution

- london_open: n=718  W=453/L=265  WR=63.1%
- ny_open: n=575  W=365/L=210  WR=63.5%
- london: n=466  W=293/L=173  WR=62.9%
- ny_close: n=398  W=249/L=149  WR=62.6%
- ny_mid: n=380  W=244/L=136  WR=64.2%
- asia: n=377  W=253/L=124  WR=67.1%
- asia_late: n=196  W=121/L=75  WR=61.7%
- off_hours: n=22  W=14/L=8  WR=63.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=135  W=116/L=19  WR=85.9%
- Refine: exclude session_bucket=ny_close drops 7/19 losers (37%)
- **Final: n=116  W=104/L=12  WR=89.7%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; RSI 40-50 lower neutral  •  AVOID when session=ny_close

### W02.  `T4=T4a AND BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=135  W=116/L=19  WR=85.9%
- Refine: exclude session_bucket=ny_close drops 7/19 losers (37%)
- **Final: n=116  W=104/L=12  WR=89.7%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W03.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=122  W=108/L=14  WR=88.5%
- Refine: exclude direction_exec=short drops 11/14 losers (79%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when short

### W04.  `H60=H60d AND T4=T4a AND RSI=RSI3`
- Raw: n=105  W=95/L=10  WR=90.5%
- Refine: exclude session_bucket=asia drops 5/10 losers (50%)
- **Final: n=98  W=93/L=5  WR=94.9%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=asia

### W05.  `T1=T1c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude H60=H60a drops 9/13 losers (69%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W06.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude BBP=BBP5 drops 5/10 losers (50%)
- **Final: n=85  W=80/L=5  WR=94.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when just touched upper band

### W07.  `T1=T1a AND T4=T4a AND BBP=BBP1`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude session_bucket=ny_close drops 4/13 losers (31%)
- **Final: n=78  W=69/L=9  WR=88.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band  •  AVOID when session=ny_close

### W08.  `T1=T1a AND T4=T4a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude session_bucket=ny_close drops 4/13 losers (31%)
- **Final: n=78  W=69/L=9  WR=88.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W09.  `T4=T4a AND BBP=BBP1 AND direction_exec=long`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=ny_close drops 5/13 losers (38%)
- **Final: n=83  W=75/L=8  WR=90.4%**
- **Dir: LONG**  •  4h trend WITH trade; just touched lower band  •  AVOID when session=ny_close

### W10.  `T4=T4a AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=ny_close drops 5/13 losers (38%)
- **Final: n=83  W=75/L=8  WR=90.4%**
- **Dir: LONG**  •  4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W11.  `H60=H60c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=85  W=79/L=6  WR=92.9%
- Refine: exclude BBP=BBP1 drops 3/6 losers (50%)
- **Final: n=82  W=79/L=3  WR=96.3%**
- **Dir: SHORT**  •  HTF60 neutral; RSI 50-60 upper neutral  •  AVOID when just touched lower band

### W12.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude session_bucket=london_open drops 6/8 losers (75%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W13.  `H60=H60a AND direction_exec=short AND session_bucket=asia`
- Raw: n=83  W=73/L=10  WR=88.0%
- Refine: exclude T1=T1a drops 9/10 losers (90%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=asia  •  AVOID when 1h trend WITH trade

### W14.  `H20=H20a AND H60=H60c AND RSI=RSI4`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude direction_exec=long drops 5/11 losers (45%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; RSI 50-60 upper neutral  •  AVOID when long

### W15.  `H60=H60a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude BBP=BBP0 drops 10/11 losers (91%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 30-40 weak  •  AVOID when deep below lower band

### W16.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude H60=H60a drops 9/11 losers (82%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF60 aligned WITH trade

### W17.  `T1=T1c AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=79  W=71/L=8  WR=89.9%
- Refine: exclude session_bucket=london_open drops 6/8 losers (75%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W18.  `H60=H60a AND T1=T1a AND RSI=RSI2`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude BBP=BBP0 drops 10/10 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when deep below lower band

### W19.  `H60=H60a AND T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude BBP=BBP0 drops 10/10 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when deep below lower band

### W20.  `H60=H60a AND T4=T4a AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude H20=H20e drops 4/7 losers (57%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; just touched lower band; RSI 40-50 lower neutral  •  AVOID when HTF20 strongly against

### W21.  `H20=H20a AND T4=T4a AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude session_bucket=ny_close drops 7/9 losers (78%)
- **Final: n=66  W=64/L=2  WR=97.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched lower band; RSI 40-50 lower neutral  •  AVOID when session=ny_close

### W22.  `H20=H20e AND T4=T4a AND ZS=ZS1`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude H60=H60d drops 4/11 losers (36%)
- **Final: n=66  W=59/L=7  WR=89.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 mildly against

### W23.  `H60=H60d AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=76  W=67/L=9  WR=88.2%
- Refine: exclude session_bucket=asia drops 5/9 losers (56%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=asia

### W24.  `T1=T1a AND T4=T4a AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude session_bucket=ny_close drops 4/10 losers (40%)
- **Final: n=59  W=53/L=6  WR=89.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band; RSI 40-50 lower neutral  •  AVOID when session=ny_close

### W25.  `T4=T4a AND RSI=RSI3 AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude direction_exec=short drops 11/11 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold; session=london_open  •  AVOID when short

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=213  W=79/L=134  WR=37.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=213  W=79/L=134  WR=37.1%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral

### L02.  `H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=173  W=66/L=107  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=173  W=66/L=107  WR=38.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral

### L03.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=142  W=53/L=89  WR=37.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=142  W=53/L=89  WR=37.3%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral

### L04.  `H20=H20e AND H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=52/L=78  WR=40.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade

### L05.  `H20=H20a AND H60=H60e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=117  W=45/L=72  WR=38.5%
- Sharpen: sharpest is BBP=BBP0 (14/72 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 40-50 lower neutral  •  ONLY when deep below lower band

### L06.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=117  W=46/L=71  WR=39.3%
- Sharpen: sharpest is BBP=BBP0 (13/71 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when deep below lower band

### L07.  `H60=H60e AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=99  W=35/L=64  WR=35.4%
- Sharpen: sharpest is BBP=BBP1 (13/64 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when just touched lower band

### L08.  `T4=T4c AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=96  W=33/L=63  WR=34.4%
- Sharpen: sharpest is H20=H20e (37/63 of losers there)
- **Sharp: n=47  W=10/L=37  WR=21.3%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched lower band; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L09.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=96  W=33/L=63  WR=34.4%
- Sharpen: sharpest is ZS=ZS2 (16/63 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L10.  `T4=T4c AND BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=96  W=33/L=63  WR=34.4%
- Sharpen: sharpest is H20=H20e (37/63 of losers there)
- **Sharp: n=47  W=10/L=37  WR=21.3%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L11.  `H60=H60e AND T4=T4c AND ZS=ZS1`
- Raw: n=86  W=31/L=55  WR=36.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=86  W=31/L=55  WR=36.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold

### L12.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI4`
- Raw: n=84  W=33/L=51  WR=39.3%
- Sharpen: sharpest is session_bucket=london (9/51 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=london

### L13.  `H20=H20e AND H60=H60c AND direction_exec=long`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is T1=T1a (24/50 of losers there)
- **Sharp: n=29  W=5/L=24  WR=17.2%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 neutral  •  ONLY when 1h trend WITH trade

### L14.  `H60=H60e AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is BBP=BBP0 (10/47 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=ny_open  •  ONLY when deep below lower band

### L15.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=73  W=26/L=47  WR=35.6%
- Sharpen: sharpest is H20=H20e (30/47 of losers there)
- **Sharp: n=42  W=12/L=30  WR=28.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L16.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=72  W=25/L=47  WR=34.7%
- Sharpen: sharpest is T4=T4c (18/47 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L17.  `H20=H20e AND T4=T4c AND BBP=BBP1`
- Raw: n=71  W=24/L=47  WR=33.8%
- Sharpen: sharpest is RSI=RSI3 (37/47 of losers there)
- **Sharp: n=47  W=10/L=37  WR=21.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched lower band  •  ONLY when RSI 40-50 lower neutral

### L18.  `H20=H20e AND T4=T4c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=71  W=24/L=47  WR=33.8%
- Sharpen: sharpest is RSI=RSI3 (37/47 of losers there)
- **Sharp: n=47  W=10/L=37  WR=21.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 40-50 lower neutral

### L19.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=71  W=26/L=45  WR=36.6%
- Sharpen: sharpest is session_bucket=ny_close (14/45 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_close

### L20.  `T1=T1c AND T4=T4c AND BBP=BBP1`
- Raw: n=70  W=27/L=43  WR=38.6%
- Sharpen: sharpest is session_bucket=london_open (16/43 of losers there)
- **Sharp: n=20  W=4/L=16  WR=20.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band  •  ONLY when session=london_open

### L21.  `T1=T1c AND T4=T4c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=70  W=27/L=43  WR=38.6%
- Sharpen: sharpest is session_bucket=london_open (16/43 of losers there)
- **Sharp: n=20  W=4/L=16  WR=20.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L22.  `T4=T4c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is T1=T1a (18/42 of losers there)
- **Sharp: n=24  W=6/L=18  WR=25.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; session=london_open  •  ONLY when 1h trend WITH trade

### L23.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=68  W=25/L=43  WR=36.8%
- Sharpen: sharpest is T1=T1c (17/43 of losers there)
- **Sharp: n=23  W=6/L=17  WR=26.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L24.  `H60=H60e AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=68  W=26/L=42  WR=38.2%
- Sharpen: sharpest is session_bucket=ny_close (13/42 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=ny_close

### L25.  `T4=T4c AND BBP=BBP1 AND direction_exec=short`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is H20=H20e (26/41 of losers there)
- **Sharp: n=34  W=8/L=26  WR=23.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; just touched lower band  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(41/34) | H60e(31/39) |
| T1 | — | — |
| T4 | T4a(55/46) | T4c(45/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/46) | long(47/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
