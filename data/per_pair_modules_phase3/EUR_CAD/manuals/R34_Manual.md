# EUR_CAD — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,521**  (W=1,556 / L=965)  -  WR: **61.7%**

## Session distribution

- ny_mid: n=631  W=374/L=257  WR=59.3%
- ny_open: n=626  W=387/L=239  WR=61.8%
- london_open: n=585  W=373/L=212  WR=63.8%
- london: n=440  W=270/L=170  WR=61.4%
- asia: n=102  W=60/L=42  WR=58.8%
- asia_late: n=97  W=65/L=32  WR=67.0%
- ny_close: n=28  W=18/L=10  WR=64.3%
- off_hours: n=12  W=9/L=3  WR=75.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20c AND H60=H60a AND RSI=RSI3`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude BBP=BBP2 drops 8/17 losers (47%)
- **Final: n=91  W=82/L=9  WR=90.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when lower third

### W02.  `H20=H20c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude BBP=BBP2 drops 8/17 losers (47%)
- **Final: n=91  W=82/L=9  WR=90.1%**
- **Dir: SHORT**  •  HTF20 neutral; RSI 40-50 lower neutral  •  AVOID when lower third

### W03.  `H20=H20c AND H60=H60a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude BBP=BBP2 drops 8/17 losers (47%)
- **Final: n=91  W=82/L=9  WR=90.1%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when lower third

### W04.  `BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=117  W=101/L=16  WR=86.3%
- Refine: exclude T4=T4c drops 15/16 losers (94%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: SHORT**  •  deep above upper band; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W05.  `H20=H20c AND H60=H60a AND T4=T4a AND RSI=RSI3`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude ZS=ZS2 drops 7/14 losers (50%)
- **Final: n=79  W=72/L=7  WR=91.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W06.  `H20=H20c AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude ZS=ZS2 drops 7/14 losers (50%)
- **Final: n=79  W=72/L=7  WR=91.1%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W07.  `H60=H60a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude session_bucket=ny_open drops 13/13 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W08.  `H60=H60a AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=89  W=81/L=8  WR=91.0%
- Refine: exclude session_bucket=ny_open drops 8/8 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W09.  `T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude RSI=RSI5 drops 11/12 losers (92%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: SHORT**  •  4h trend WITH trade; deep above upper band  •  AVOID when RSI 60-70 strong

### W10.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=83  W=75/L=8  WR=90.4%
- Refine: exclude session_bucket=asia drops 4/8 losers (50%)
- **Final: n=76  W=72/L=4  WR=94.7%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W11.  `H20=H20a AND T4=T4a AND BBP=BBP6`
- Raw: n=82  W=76/L=6  WR=92.7%
- Refine: exclude session_bucket=ny_open drops 6/6 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when session=ny_open

### W12.  `H20=H20a AND T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=77  W=76/L=1  WR=98.7%
- Refine: no further refinement
- **Final: n=77  W=76/L=1  WR=98.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band

### W13.  `H60=H60a AND T4=T4a AND BBP=BBP6`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude T1=T1b drops 5/9 losers (56%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when 1h trend flat

### W14.  `H60=H60a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=76  W=67/L=9  WR=88.2%
- Refine: exclude session_bucket=london_open drops 5/9 losers (56%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W15.  `BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=76  W=67/L=9  WR=88.2%
- Refine: exclude session_bucket=london_open drops 5/9 losers (56%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: SHORT**  •  deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W16.  `H60=H60a AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=76  W=67/L=9  WR=88.2%
- Refine: exclude session_bucket=london_open drops 5/9 losers (56%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W17.  `H20=H20a AND H60=H60a AND T4=T4a AND BBP=BBP6`
- Raw: n=74  W=68/L=6  WR=91.9%
- Refine: exclude T1=T1b drops 5/6 losers (83%)
- **Final: n=69  W=68/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when 1h trend flat

### W18.  `H60=H60a AND T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=72  W=68/L=4  WR=94.4%
- Refine: exclude H20=H20c drops 3/4 losers (75%)
- **Final: n=69  W=68/L=1  WR=98.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when HTF20 neutral

### W19.  `H60=H60a AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude session_bucket=london_open drops 5/9 losers (56%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W20.  `BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude session_bucket=london_open drops 5/9 losers (56%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: SHORT**  •  deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W21.  `H20=H20a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=64  W=58/L=6  WR=90.6%
- Refine: exclude T1=T1b drops 5/6 losers (83%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when 1h trend flat

### W22.  `H20=H20a AND T4=T4a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=64  W=58/L=6  WR=90.6%
- Refine: exclude T1=T1b drops 5/6 losers (83%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when 1h trend flat

### W23.  `H20=H20a AND T1=T1c AND T4=T4a AND ZS=ZS5`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude BBP=BBP5 drops 8/9 losers (89%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W24.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude session_bucket=ny_open drops 9/9 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W25.  `T1=T1a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude session_bucket=ny_open drops 9/9 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=138  W=40/L=98  WR=29.0%
- Sharpen: sharpest is H60=H60b (28/98 of losers there)
- **Sharp: n=29  W=1/L=28  WR=3.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF60 slightly aligned

### L02.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=132  W=42/L=90  WR=31.8%
- Sharpen: sharpest is session_bucket=ny_mid (27/90 of losers there)
- **Sharp: n=33  W=6/L=27  WR=18.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_mid

### L03.  `T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=111  W=42/L=69  WR=37.8%
- Sharpen: sharpest is T4=T4c (47/69 of losers there)
- **Sharp: n=57  W=10/L=47  WR=17.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L04.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=93  W=29/L=64  WR=31.2%
- Sharpen: sharpest is BBP=BBP6 (36/64 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L05.  `H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=93  W=30/L=63  WR=32.3%
- Sharpen: sharpest is T4=T4c (47/63 of losers there)
- **Sharp: n=57  W=10/L=47  WR=17.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L06.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=93  W=30/L=63  WR=32.3%
- Sharpen: sharpest is T4=T4c (47/63 of losers there)
- **Sharp: n=57  W=10/L=47  WR=17.5%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L07.  `T4=T4c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is H60=H60b (28/56 of losers there)
- **Sharp: n=29  W=1/L=28  WR=3.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF60 slightly aligned

### L08.  `T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is T4=T4a (25/55 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: LONG**  •  1h trend WITH trade; session=london  •  ONLY when 4h trend WITH trade

### L09.  `H60=H60e AND T1=T1c AND RSI=RSI2`
- Raw: n=88  W=24/L=64  WR=27.3%
- Sharpen: sharpest is BBP=BBP2 (23/64 of losers there)
- **Sharp: n=26  W=3/L=23  WR=11.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when lower third

### L10.  `H60=H60e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=88  W=24/L=64  WR=27.3%
- Sharpen: sharpest is BBP=BBP2 (23/64 of losers there)
- **Sharp: n=26  W=3/L=23  WR=11.5%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak  •  ONLY when lower third

### L11.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=88  W=24/L=64  WR=27.3%
- Sharpen: sharpest is BBP=BBP2 (23/64 of losers there)
- **Sharp: n=26  W=3/L=23  WR=11.5%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when lower third

### L12.  `H60=H60e AND BBP=BBP6 AND direction_exec=long`
- Raw: n=88  W=28/L=60  WR=31.8%
- Sharpen: sharpest is RSI=RSI4 (46/60 of losers there)
- **Sharp: n=46  W=0/L=46  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L13.  `H20=H20c AND T4=T4c AND ZS=ZS1`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: sharpest is T1=T1c (45/53 of losers there)
- **Sharp: n=67  W=22/L=45  WR=32.8%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L14.  `H60=H60e AND T4=T4c AND BBP=BBP0`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (14/51 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band  •  ONLY when session=ny_open

### L15.  `T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (14/51 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band  •  ONLY when session=ny_open

### L16.  `H60=H60e AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (14/51 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band  •  ONLY when session=ny_open

### L17.  `T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=84  W=32/L=52  WR=38.1%
- Sharpen: sharpest is session_bucket=ny_open (14/52 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band  •  ONLY when session=ny_open

### L18.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=84  W=32/L=52  WR=38.1%
- Sharpen: sharpest is ZS=ZS2 (48/52 of losers there)
- **Sharp: n=70  W=22/L=48  WR=31.4%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L19.  `H20=H20e AND ZS=ZS2 AND direction_exec=long`
- Raw: n=82  W=28/L=54  WR=34.1%
- Sharpen: sharpest is session_bucket=london_open (22/54 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: LONG**  •  HTF20 strongly against; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L20.  `H20=H20e AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=82  W=28/L=54  WR=34.1%
- Sharpen: sharpest is session_bucket=london_open (22/54 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: LONG**  •  HTF20 strongly against; lower third; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L21.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=81  W=30/L=51  WR=37.0%
- Sharpen: sharpest is H60=H60b (28/51 of losers there)
- **Sharp: n=29  W=1/L=28  WR=3.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF60 slightly aligned

### L22.  `H60=H60e AND T1=T1c AND BBP=BBP0`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (14/48 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep below lower band  •  ONLY when session=ny_open

### L23.  `H60=H60e AND T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (14/48 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; deep below lower band  •  ONLY when session=ny_open

### L24.  `H20=H20e AND T1=T1c AND ZS=ZS2`
- Raw: n=78  W=28/L=50  WR=35.9%
- Sharpen: sharpest is RSI=RSI2 (14/50 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L25.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=78  W=28/L=50  WR=35.9%
- Sharpen: sharpest is RSI=RSI2 (14/50 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(44/35) | H60e(37/45) |
| T1 | T1a(52/46) | T1c(46/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(55/43) | long(45/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
