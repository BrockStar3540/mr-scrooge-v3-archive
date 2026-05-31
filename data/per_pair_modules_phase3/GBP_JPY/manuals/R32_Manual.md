# GBP_JPY — R32 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,160**  (W=1,838 / L=1,322)  -  WR: **58.2%**

## Session distribution

- asia: n=710  W=449/L=261  WR=63.2%
- london_open: n=632  W=359/L=273  WR=56.8%
- ny_open: n=458  W=266/L=192  WR=58.1%
- london: n=383  W=237/L=146  WR=61.9%
- asia_late: n=362  W=196/L=166  WR=54.1%
- ny_mid: n=288  W=159/L=129  WR=55.2%
- ny_close: n=269  W=145/L=124  WR=53.9%
- off_hours: n=58  W=27/L=31  WR=46.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=125  W=109/L=16  WR=87.2%
- Refine: exclude T4=T4c drops 16/16 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=asia  •  AVOID when 4h trend AGAINST trade

### W02.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=125  W=109/L=16  WR=87.2%
- Refine: exclude T4=T4c drops 16/16 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; session=asia  •  AVOID when 4h trend AGAINST trade

### W03.  `H60=H60e AND T1=T1a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=125  W=109/L=16  WR=87.2%
- Refine: exclude T4=T4c drops 16/16 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when 4h trend AGAINST trade

### W04.  `H60=H60e AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=125  W=109/L=16  WR=87.2%
- Refine: exclude T4=T4c drops 16/16 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 30-40 weak; session=asia  •  AVOID when 4h trend AGAINST trade

### W05.  `T1=T1a AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude strategy_id=BR2_vcb_short drops 5/14 losers (36%)
- **Final: n=93  W=84/L=9  WR=90.3%**
- **Dir: ?**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=london_open  •  AVOID when strategy=BR2_vcb_short

### W06.  `T1=T1a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude strategy_id=BR2_vcb_short drops 5/14 losers (36%)
- **Final: n=93  W=84/L=9  WR=90.3%**
- **Dir: ?**  •  1h trend WITH trade; lower third; zscore -2 to -1 oversold; session=london_open  •  AVOID when strategy=BR2_vcb_short

### W07.  `T1=T1a AND ZS=ZS2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=100  W=86/L=14  WR=86.0%
- Refine: exclude strategy_id=BR2_vcb_short drops 5/14 losers (36%)
- **Final: n=91  W=82/L=9  WR=90.1%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=london_open  •  AVOID when strategy=BR2_vcb_short

### W08.  `H20=H20e AND T1=T1a AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude strategy_id=BR2_vcb_short drops 5/14 losers (36%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold; session=london_open  •  AVOID when strategy=BR2_vcb_short

### W09.  `H60=H60e AND T1=T1a AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude strategy_id=BR2_vcb_short drops 5/14 losers (36%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold; session=london_open  •  AVOID when strategy=BR2_vcb_short

### W10.  `T1=T1a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=91  W=79/L=12  WR=86.8%
- Refine: exclude T4=T4c drops 10/12 losers (83%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when 4h trend AGAINST trade

### W11.  `T1=T1a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=91  W=79/L=12  WR=86.8%
- Refine: exclude T4=T4c drops 10/12 losers (83%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  1h trend WITH trade; lower third; zscore -2 to -1 oversold; session=asia  •  AVOID when 4h trend AGAINST trade

### W12.  `H20=H20a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude H60=H60e drops 4/12 losers (33%)
- **Final: n=76  W=68/L=8  WR=89.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; session=ny_open  •  AVOID when HTF60 strongly against

### W13.  `H20=H20e AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude T4=T4c drops 10/12 losers (83%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF20 strongly against; zscore -2 to -1 oversold; session=asia  •  AVOID when 4h trend AGAINST trade

### W14.  `H20=H20e AND T1=T1a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude T4=T4c drops 10/12 losers (83%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when 4h trend AGAINST trade

### W15.  `H20=H20e AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude T4=T4c drops 10/12 losers (83%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF20 strongly against; lower third; zscore -2 to -1 oversold; session=asia  •  AVOID when 4h trend AGAINST trade

### W16.  `H20=H20e AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude T4=T4c drops 10/12 losers (83%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore -2 to -1 oversold; session=asia  •  AVOID when 4h trend AGAINST trade

### W17.  `T1=T1a AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude T4=T4c drops 10/12 losers (83%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when 4h trend AGAINST trade

### W18.  `H20=H20e AND H60=H60e AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude T4=T4c drops 9/11 losers (82%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore -2 to -1 oversold; session=asia  •  AVOID when 4h trend AGAINST trade

### W19.  `H60=H60e AND T1=T1a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude T4=T4c drops 9/11 losers (82%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when 4h trend AGAINST trade

### W20.  `H20=H20a AND H60=H60a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=76  W=68/L=8  WR=89.5%
- Refine: exclude RSI=RSI2 drops 8/8 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third; session=ny_open  •  AVOID when RSI 30-40 weak

### W21.  `H20=H20a AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=76  W=68/L=8  WR=89.5%
- Refine: exclude RSI=RSI2 drops 8/8 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; lower third; session=ny_open  •  AVOID when RSI 30-40 weak

### W22.  `BBP=BBP1 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude session_bucket=asia drops 7/9 losers (78%)
- **Final: n=66  W=64/L=2  WR=97.0%**
- **Dir: LONG**  •  just touched lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W23.  `BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude session_bucket=asia drops 7/9 losers (78%)
- **Final: n=66  W=64/L=2  WR=97.0%**
- **Dir: LONG**  •  just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W24.  `H20=H20a AND T1=T1c AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude RSI=RSI2 drops 8/8 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; lower third; session=ny_open  •  AVOID when RSI 30-40 weak

### W25.  `H20=H20e AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude strategy_id=BR2_vcb_short drops 2/8 losers (25%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 30-40 weak; session=london_open  •  AVOID when strategy=BR2_vcb_short

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=502  W=197/L=305  WR=39.2%
- Sharpen: sharpest is session_bucket=london_open (105/305 of losers there)
- **Sharp: n=141  W=36/L=105  WR=25.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when session=london_open

### L02.  `H20=H20a AND T1=T1c AND RSI=RSI2`
- Raw: n=495  W=195/L=300  WR=39.4%
- Sharpen: sharpest is session_bucket=london_open (105/300 of losers there)
- **Sharp: n=141  W=36/L=105  WR=25.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L03.  `H20=H20a AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=495  W=195/L=300  WR=39.4%
- Sharpen: sharpest is session_bucket=london_open (105/300 of losers there)
- **Sharp: n=141  W=36/L=105  WR=25.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L04.  `H20=H20a AND H60=H60a AND RSI=RSI2`
- Raw: n=490  W=192/L=298  WR=39.2%
- Sharpen: sharpest is session_bucket=london_open (105/298 of losers there)
- **Sharp: n=141  W=36/L=105  WR=25.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when session=london_open

### L05.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=490  W=192/L=298  WR=39.2%
- Sharpen: sharpest is session_bucket=london_open (105/298 of losers there)
- **Sharp: n=141  W=36/L=105  WR=25.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when session=london_open

### L06.  `H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=475  W=176/L=299  WR=37.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=475  W=176/L=299  WR=37.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak

### L07.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=475  W=176/L=299  WR=37.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=475  W=176/L=299  WR=37.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak

### L08.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=463  W=171/L=292  WR=36.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=463  W=171/L=292  WR=36.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak

### L09.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=241  W=93/L=148  WR=38.6%
- Sharpen: sharpest is session_bucket=asia (37/148 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L10.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=241  W=93/L=148  WR=38.6%
- Sharpen: sharpest is session_bucket=asia (37/148 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L11.  `H60=H60a AND T4=T4a AND RSI=RSI2`
- Raw: n=234  W=83/L=151  WR=35.5%
- Sharpen: sharpest is BBP=BBP1 (56/151 of losers there)
- **Sharp: n=70  W=14/L=56  WR=20.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when just touched lower band

### L12.  `H60=H60a AND T1=T1c AND T4=T4a AND RSI=RSI2`
- Raw: n=234  W=83/L=151  WR=35.5%
- Sharpen: sharpest is BBP=BBP1 (56/151 of losers there)
- **Sharp: n=70  W=14/L=56  WR=20.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when just touched lower band

### L13.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=234  W=83/L=151  WR=35.5%
- Sharpen: sharpest is BBP=BBP1 (56/151 of losers there)
- **Sharp: n=70  W=14/L=56  WR=20.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when just touched lower band

### L14.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI2`
- Raw: n=222  W=78/L=144  WR=35.1%
- Sharpen: sharpest is BBP=BBP1 (56/144 of losers there)
- **Sharp: n=70  W=14/L=56  WR=20.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when just touched lower band

### L15.  `H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=209  W=76/L=133  WR=36.4%
- Sharpen: sharpest is T1=T1a (109/133 of losers there)
- **Sharp: n=155  W=46/L=109  WR=29.7%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_open  •  ONLY when 1h trend WITH trade

### L16.  `H60=H60a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=208  W=74/L=134  WR=35.6%
- Sharpen: sharpest is T4=T4a (78/134 of losers there)
- **Sharp: n=107  W=29/L=78  WR=27.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L17.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=208  W=74/L=134  WR=35.6%
- Sharpen: sharpest is T4=T4a (78/134 of losers there)
- **Sharp: n=107  W=29/L=78  WR=27.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L18.  `H60=H60a AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=208  W=74/L=134  WR=35.6%
- Sharpen: sharpest is T4=T4a (78/134 of losers there)
- **Sharp: n=107  W=29/L=78  WR=27.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L19.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=200  W=70/L=130  WR=35.0%
- Sharpen: sharpest is T4=T4a (78/130 of losers there)
- **Sharp: n=107  W=29/L=78  WR=27.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L20.  `H20=H20e AND H60=H60e AND session_bucket=ny_open`
- Raw: n=184  W=70/L=114  WR=38.0%
- Sharpen: sharpest is T1=T1a (90/114 of losers there)
- **Sharp: n=130  W=40/L=90  WR=30.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when 1h trend WITH trade

### L21.  `H20=H20e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=184  W=70/L=114  WR=38.0%
- Sharpen: sharpest is T1=T1a (90/114 of losers there)
- **Sharp: n=130  W=40/L=90  WR=30.8%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_open  •  ONLY when 1h trend WITH trade

### L22.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=184  W=70/L=114  WR=38.0%
- Sharpen: sharpest is T1=T1a (90/114 of losers there)
- **Sharp: n=130  W=40/L=90  WR=30.8%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when 1h trend WITH trade

### L23.  `T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=178  W=60/L=118  WR=33.7%
- Sharpen: sharpest is session_bucket=london_open (44/118 of losers there)
- **Sharp: n=51  W=7/L=44  WR=13.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band  •  ONLY when session=london_open

### L24.  `T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=175  W=60/L=115  WR=34.3%
- Sharpen: sharpest is session_bucket=london_open (35/115 of losers there)
- **Sharp: n=42  W=7/L=35  WR=16.7%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L25.  `H20=H20a AND H60=H60a AND BBP=BBP0`
- Raw: n=159  W=57/L=102  WR=35.8%
- Sharpen: sharpest is T1=T1c (102/102 of losers there)
- **Sharp: n=141  W=39/L=102  WR=27.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band  •  ONLY when 1h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(47/41) | — |
| H60 | — | — |
| T1 | T1a(53/46) | T1c(47/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
