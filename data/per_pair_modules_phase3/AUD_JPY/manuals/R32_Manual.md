# AUD_JPY — R32 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,252**  (W=2,004 / L=1,248)  -  WR: **61.6%**

## Session distribution

- asia: n=1445  W=881/L=564  WR=61.0%
- ny_close: n=639  W=389/L=250  WR=60.9%
- off_hours: n=269  W=173/L=96  WR=64.3%
- ny_open: n=239  W=153/L=86  WR=64.0%
- london: n=216  W=145/L=71  WR=67.1%
- london_open: n=204  W=119/L=85  WR=58.3%
- asia_late: n=161  W=100/L=61  WR=62.1%
- ny_mid: n=79  W=44/L=35  WR=55.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1a AND ZS=ZS2`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude session_bucket=london_open drops 8/14 losers (57%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W02.  `T1=T1a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude session_bucket=london_open drops 8/14 losers (57%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: LONG**  •  1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W03.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude session_bucket=london_open drops 8/14 losers (57%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W04.  `H60=H60a AND T1=T1a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude session_bucket=london_open drops 8/14 losers (57%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W05.  `T1=T1a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude session_bucket=london_open drops 8/14 losers (57%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: LONG**  •  1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W06.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude session_bucket=london_open drops 11/15 losers (73%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W07.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude session_bucket=london_open drops 11/15 losers (73%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: LONG**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W08.  `T1=T1a AND T4=T4a AND session_bucket=london`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude ZS=ZS0 drops 7/14 losers (50%)
- **Final: n=82  W=75/L=7  WR=91.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london  •  AVOID when zscore <-3 extreme

### W09.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=london`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude ZS=ZS0 drops 7/13 losers (54%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=london  •  AVOID when zscore <-3 extreme

### W10.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=london`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude ZS=ZS0 drops 7/13 losers (54%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=london  •  AVOID when zscore <-3 extreme

### W11.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude session_bucket=london_open drops 8/12 losers (67%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W12.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude session_bucket=london_open drops 8/12 losers (67%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W13.  `H20=H20e AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude T4=T4c drops 11/13 losers (85%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W14.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=asia`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude ZS=ZS3 drops 7/11 losers (64%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W15.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude ZS=ZS3 drops 7/11 losers (64%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W16.  `H60=H60e AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude session_bucket=asia drops 8/11 losers (73%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; RSI 30-40 weak  •  AVOID when session=asia

### W17.  `T1=T1a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude session_bucket=asia drops 8/11 losers (73%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 30-40 weak  •  AVOID when session=asia

### W18.  `BBP=BBP0 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude session_bucket=asia drops 8/11 losers (73%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: SHORT**  •  deep below lower band; RSI 30-40 weak  •  AVOID when session=asia

### W19.  `H60=H60e AND T1=T1a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude session_bucket=asia drops 8/11 losers (73%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; deep below lower band; RSI 30-40 weak  •  AVOID when session=asia

### W20.  `H60=H60e AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude session_bucket=asia drops 8/11 losers (73%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: SHORT**  •  HTF60 strongly against; deep below lower band; RSI 30-40 weak  •  AVOID when session=asia

### W21.  `T1=T1a AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude session_bucket=asia drops 8/11 losers (73%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; RSI 30-40 weak  •  AVOID when session=asia

### W22.  `H60=H60a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude session_bucket=ny_close drops 4/10 losers (40%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W23.  `H20=H20a AND H60=H60a AND session_bucket=asia_late`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude ZS=ZS3 drops 7/10 losers (70%)
- **Final: n=60  W=57/L=3  WR=95.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia_late  •  AVOID when zscore -1 to +1 neutral

### W24.  `H20=H20a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude ZS=ZS3 drops 7/10 losers (70%)
- **Final: n=60  W=57/L=3  WR=95.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=asia_late  •  AVOID when zscore -1 to +1 neutral

### W25.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude ZS=ZS3 drops 7/10 losers (70%)
- **Final: n=60  W=57/L=3  WR=95.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia_late  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=214  W=75/L=139  WR=35.0%
- Sharpen: sharpest is ZS=ZS2 (52/139 of losers there)
- **Sharp: n=60  W=8/L=52  WR=13.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when zscore -2 to -1 oversold

### L02.  `H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=190  W=68/L=122  WR=35.8%
- Sharpen: sharpest is ZS=ZS2 (47/122 of losers there)
- **Sharp: n=52  W=5/L=47  WR=9.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when zscore -2 to -1 oversold

### L03.  `T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=190  W=68/L=122  WR=35.8%
- Sharpen: sharpest is ZS=ZS2 (47/122 of losers there)
- **Sharp: n=52  W=5/L=47  WR=9.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when zscore -2 to -1 oversold

### L04.  `H60=H60e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=190  W=68/L=122  WR=35.8%
- Sharpen: sharpest is ZS=ZS2 (47/122 of losers there)
- **Sharp: n=52  W=5/L=47  WR=9.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when zscore -2 to -1 oversold

### L05.  `H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=187  W=67/L=120  WR=35.8%
- Sharpen: sharpest is ZS=ZS2 (48/120 of losers there)
- **Sharp: n=56  W=8/L=48  WR=14.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L06.  `T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=187  W=67/L=120  WR=35.8%
- Sharpen: sharpest is ZS=ZS2 (48/120 of losers there)
- **Sharp: n=56  W=8/L=48  WR=14.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L07.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=187  W=67/L=120  WR=35.8%
- Sharpen: sharpest is ZS=ZS2 (48/120 of losers there)
- **Sharp: n=56  W=8/L=48  WR=14.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L08.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=165  W=62/L=103  WR=37.6%
- Sharpen: sharpest is ZS=ZS2 (43/103 of losers there)
- **Sharp: n=48  W=5/L=43  WR=10.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L09.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=165  W=62/L=103  WR=37.6%
- Sharpen: sharpest is ZS=ZS2 (43/103 of losers there)
- **Sharp: n=48  W=5/L=43  WR=10.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L10.  `H20=H20e AND H60=H60e AND T1=T1c`
- Raw: n=121  W=35/L=86  WR=28.9%
- Sharpen: sharpest is BBP=BBP2 (31/86 of losers there)
- **Sharp: n=35  W=4/L=31  WR=11.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when lower third

### L11.  `H20=H20e AND T1=T1c AND direction_exec=short`
- Raw: n=121  W=35/L=86  WR=28.9%
- Sharpen: sharpest is BBP=BBP2 (31/86 of losers there)
- **Sharp: n=35  W=4/L=31  WR=11.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade  •  ONLY when lower third

### L12.  `H20=H20e AND H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=121  W=35/L=86  WR=28.9%
- Sharpen: sharpest is BBP=BBP2 (31/86 of losers there)
- **Sharp: n=35  W=4/L=31  WR=11.4%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when lower third

### L13.  `H60=H60e AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=120  W=47/L=73  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (58/73 of losers there)
- **Sharp: n=79  W=21/L=58  WR=26.6%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L14.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=120  W=47/L=73  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (58/73 of losers there)
- **Sharp: n=79  W=21/L=58  WR=26.6%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L15.  `H60=H60e AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=120  W=47/L=73  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (58/73 of losers there)
- **Sharp: n=79  W=21/L=58  WR=26.6%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L16.  `H60=H60e AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=119  W=45/L=74  WR=37.8%
- Sharpen: sharpest is H20=H20a (20/74 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L17.  `BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=119  W=45/L=74  WR=37.8%
- Sharpen: sharpest is H20=H20a (20/74 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  deep below lower band; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L18.  `H60=H60e AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=119  W=45/L=74  WR=37.8%
- Sharpen: sharpest is H20=H20a (20/74 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  HTF60 strongly against; deep below lower band; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L19.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=103  W=29/L=74  WR=28.2%
- Sharpen: sharpest is BBP=BBP2 (27/74 of losers there)
- **Sharp: n=31  W=4/L=27  WR=12.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when lower third

### L20.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=103  W=29/L=74  WR=28.2%
- Sharpen: sharpest is BBP=BBP2 (27/74 of losers there)
- **Sharp: n=31  W=4/L=27  WR=12.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when lower third

### L21.  `H20=H20e AND T1=T1c AND T4=T4a`
- Raw: n=97  W=28/L=69  WR=28.9%
- Sharpen: sharpest is BBP=BBP2 (26/69 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when lower third

### L22.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=97  W=28/L=69  WR=28.9%
- Sharpen: sharpest is BBP=BBP2 (26/69 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when lower third

### L23.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=97  W=28/L=69  WR=28.9%
- Sharpen: sharpest is BBP=BBP2 (26/69 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when lower third

### L24.  `H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=94  W=37/L=57  WR=39.4%
- Sharpen: sharpest is H20=H20e (33/57 of losers there)
- **Sharp: n=47  W=14/L=33  WR=29.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when HTF20 strongly against

### L25.  `T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=94  W=37/L=57  WR=39.4%
- Sharpen: sharpest is H20=H20e (33/57 of losers there)
- **Sharp: n=47  W=14/L=33  WR=29.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=asia  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(55/44) | T1c(44/56) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
