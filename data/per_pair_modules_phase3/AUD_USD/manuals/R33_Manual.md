# AUD_USD — R33 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,018**  (W=1,939 / L=1,079)  -  WR: **64.2%**

## Session distribution

- asia: n=746  W=497/L=249  WR=66.6%
- london_open: n=656  W=432/L=224  WR=65.9%
- ny_open: n=416  W=269/L=147  WR=64.7%
- ny_mid: n=368  W=233/L=135  WR=63.3%
- london: n=344  W=205/L=139  WR=59.6%
- ny_close: n=291  W=177/L=114  WR=60.8%
- asia_late: n=161  W=103/L=58  WR=64.0%
- off_hours: n=36  W=23/L=13  WR=63.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=221  W=190/L=31  WR=86.0%
- Refine: exclude H60=H60e drops 23/31 losers (74%)
- **Final: n=127  W=119/L=8  WR=93.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when HTF60 strongly against

### W02.  `H20=H20a AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=129  W=117/L=12  WR=90.7%
- Refine: exclude ZS=ZS1 drops 6/12 losers (50%)
- **Final: n=105  W=99/L=6  WR=94.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W03.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=127  W=119/L=8  WR=93.7%
- Refine: exclude BBP=BBP0 drops 4/8 losers (50%)
- **Final: n=107  W=103/L=4  WR=96.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when deep below lower band

### W04.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude H20=H20e drops 12/17 losers (71%)
- **Final: n=72  W=67/L=5  WR=93.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF20 strongly against

### W05.  `T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=113  W=99/L=14  WR=87.6%
- Refine: exclude T1=T1a drops 11/14 losers (79%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=asia  •  AVOID when 1h trend WITH trade

### W06.  `T1=T1a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=111  W=97/L=14  WR=87.4%
- Refine: exclude H60=H60a drops 11/14 losers (79%)
- **Final: n=77  W=74/L=3  WR=96.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when HTF60 aligned WITH trade

### W07.  `H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=107  W=96/L=11  WR=89.7%
- Refine: exclude T1=T1c drops 10/11 losers (91%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W08.  `T4=T4a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=102  W=90/L=12  WR=88.2%
- Refine: exclude T1=T1a drops 9/12 losers (75%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: ?**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when 1h trend WITH trade

### W09.  `T4=T4a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=102  W=90/L=12  WR=88.2%
- Refine: exclude T1=T1a drops 9/12 losers (75%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: ?**  •  4h trend WITH trade; upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when 1h trend WITH trade

### W10.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude H60=H60e drops 11/13 losers (85%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF60 strongly against

### W11.  `H60=H60a AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=99  W=91/L=8  WR=91.9%
- Refine: exclude BBP=BBP0 drops 4/8 losers (50%)
- **Final: n=93  W=89/L=4  WR=95.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when deep below lower band

### W12.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=99  W=88/L=11  WR=88.9%
- Refine: exclude T1=T1c drops 10/11 losers (91%)
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W13.  `T1=T1a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=99  W=86/L=13  WR=86.9%
- Refine: exclude T4=T4a drops 10/13 losers (77%)
- **Final: n=55  W=52/L=3  WR=94.5%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when 4h trend WITH trade

### W14.  `H60=H60e AND T1=T1a AND direction_exec=long`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude RSI=RSI4 drops 10/14 losers (71%)
- **Final: n=46  W=42/L=4  WR=91.3%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W15.  `T4=T4a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude T1=T1c drops 13/13 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W16.  `H20=H20a AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=86  W=78/L=8  WR=90.7%
- Refine: exclude H60=H60a drops 8/8 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF60 aligned WITH trade

### W17.  `T1=T1a AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=86  W=77/L=9  WR=89.5%
- Refine: exclude T4=T4a drops 9/9 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when 4h trend WITH trade

### W18.  `T4=T4a AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=85  W=75/L=10  WR=88.2%
- Refine: exclude H20=H20d drops 2/10 losers (20%)
- **Final: n=82  W=74/L=8  WR=90.2%**
- **Dir: ?**  •  4h trend WITH trade; zscore -1 to +1 neutral; session=asia  •  AVOID when HTF20 mildly against

### W19.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude T1=T1c drops 10/11 losers (91%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W20.  `H20=H20e AND T1=T1a AND T4=T4c AND BBP=BBP6`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude direction_exec=short drops 11/11 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; deep above upper band  •  AVOID when short

### W21.  `T4=T4a AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=83  W=75/L=8  WR=90.4%
- Refine: exclude H60=H60a drops 8/8 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF60 aligned WITH trade

### W22.  `H20=H20a AND T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude T1=T1a drops 9/9 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; upper third; session=asia  •  AVOID when 1h trend WITH trade

### W23.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=82  W=76/L=6  WR=92.7%
- Refine: exclude H20=H20c drops 3/6 losers (50%)
- **Final: n=78  W=75/L=3  WR=96.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 neutral

### W24.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=82  W=75/L=7  WR=91.5%
- Refine: exclude BBP=BBP1 drops 2/7 losers (29%)
- **Final: n=80  W=75/L=5  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when just touched lower band

### W25.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude BBP=BBP5 drops 8/8 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when just touched upper band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=104  W=41/L=63  WR=39.4%
- Sharpen: sharpest is H20=H20a (10/63 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L02.  `T1=T1c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is H60=H60a (51/62 of losers there)
- **Sharp: n=65  W=14/L=51  WR=21.5%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L03.  `H20=H20a AND H60=H60a AND session_bucket=london`
- Raw: n=99  W=35/L=64  WR=35.4%
- Sharpen: sharpest is T1=T1c (44/64 of losers there)
- **Sharp: n=55  W=11/L=44  WR=20.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london  •  ONLY when 1h trend AGAINST trade

### L04.  `H60=H60a AND T1=T1c AND BBP=BBP0`
- Raw: n=98  W=33/L=65  WR=33.7%
- Sharpen: sharpest is RSI=RSI3 (51/65 of losers there)
- **Sharp: n=65  W=14/L=51  WR=21.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band  •  ONLY when RSI 40-50 lower neutral

### L05.  `H60=H60a AND T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=98  W=33/L=65  WR=33.7%
- Sharpen: sharpest is RSI=RSI3 (51/65 of losers there)
- **Sharp: n=65  W=14/L=51  WR=21.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band  •  ONLY when RSI 40-50 lower neutral

### L06.  `H20=H20a AND direction_exec=long AND session_bucket=london`
- Raw: n=97  W=34/L=63  WR=35.1%
- Sharpen: sharpest is T1=T1c (44/63 of losers there)
- **Sharp: n=55  W=11/L=44  WR=20.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london  •  ONLY when 1h trend AGAINST trade

### L07.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=london`
- Raw: n=95  W=33/L=62  WR=34.7%
- Sharpen: sharpest is T1=T1c (44/62 of losers there)
- **Sharp: n=55  W=11/L=44  WR=20.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london  •  ONLY when 1h trend AGAINST trade

### L08.  `H20=H20a AND H60=H60a AND T1=T1c AND BBP=BBP0`
- Raw: n=83  W=31/L=52  WR=37.3%
- Sharpen: sharpest is RSI=RSI3 (38/52 of losers there)
- **Sharp: n=52  W=14/L=38  WR=26.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band  •  ONLY when RSI 40-50 lower neutral

### L09.  `H60=H60a AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is T1=T1c (32/50 of losers there)
- **Sharp: n=46  W=14/L=32  WR=30.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L10.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=81  W=23/L=58  WR=28.4%
- Sharpen: sharpest is RSI=RSI4 (26/58 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L11.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=81  W=30/L=51  WR=37.0%
- Sharpen: sharpest is H60=H60e (26/51 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF60 strongly against

### L12.  `H20=H20a AND T4=T4a AND BBP=BBP6`
- Raw: n=80  W=29/L=51  WR=36.2%
- Sharpen: sharpest is T1=T1c (37/51 of losers there)
- **Sharp: n=43  W=6/L=37  WR=14.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when 1h trend AGAINST trade

### L13.  `T1=T1c AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=79  W=28/L=51  WR=35.4%
- Sharpen: sharpest is H60=H60a (51/51 of losers there)
- **Sharp: n=65  W=14/L=51  WR=21.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L14.  `H60=H60a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=75  W=28/L=47  WR=37.3%
- Sharpen: sharpest is RSI=RSI3 (27/47 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  ONLY when RSI 40-50 lower neutral

### L15.  `H60=H60a AND T1=T1c AND session_bucket=ny_close`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is BBP=BBP0 (14/45 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  ONLY when deep below lower band

### L16.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is session_bucket=london_open (9/45 of losers there)
- **Sharp: n=10  W=1/L=9  WR=10.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=london_open

### L17.  `T1=T1c AND direction_exec=long AND session_bucket=london`
- Raw: n=73  W=25/L=48  WR=34.2%
- Sharpen: sharpest is H20=H20a (44/48 of losers there)
- **Sharp: n=55  W=11/L=44  WR=20.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=london  •  ONLY when HTF20 aligned WITH trade

### L18.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=73  W=26/L=47  WR=35.6%
- Sharpen: sharpest is session_bucket=asia (20/47 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=asia

### L19.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=72  W=26/L=46  WR=36.1%
- Sharpen: sharpest is session_bucket=asia (11/46 of losers there)
- **Sharp: n=13  W=2/L=11  WR=15.4%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=asia

### L20.  `T4=T4c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is T1=T1a (22/44 of losers there)
- **Sharp: n=30  W=8/L=22  WR=26.7%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  ONLY when 1h trend WITH trade

### L21.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is RSI=RSI3 (26/44 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  ONLY when RSI 40-50 lower neutral

### L22.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is T1=T1a (22/44 of losers there)
- **Sharp: n=30  W=8/L=22  WR=26.7%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when 1h trend WITH trade

### L23.  `T1=T1c AND T4=T4a AND session_bucket=ny_open`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is H60=H60a (28/43 of losers there)
- **Sharp: n=31  W=3/L=28  WR=9.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_open  •  ONLY when HTF60 aligned WITH trade

### L24.  `T4=T4c AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is RSI=RSI3 (24/42 of losers there)
- **Sharp: n=33  W=9/L=24  WR=27.3%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -1 to +1 neutral; session=asia  •  ONLY when RSI 40-50 lower neutral

### L25.  `H20=H20e AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=69  W=25/L=44  WR=36.2%
- Sharpen: sharpest is RSI=RSI3 (20/44 of losers there)
- **Sharp: n=21  W=1/L=20  WR=4.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 40-50 lower neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(48/43) | H60a(42/49) |
| T1 | — | — |
| T4 | — | T4c(47/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
