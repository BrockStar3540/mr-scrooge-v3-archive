# GBP_AUD — R27 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **5,036**  (W=3,100 / L=1,936)  -  WR: **61.6%**

## Session distribution

- asia: n=2715  W=1697/L=1018  WR=62.5%
- ny_close: n=717  W=431/L=286  WR=60.1%
- asia_late: n=364  W=233/L=131  WR=64.0%
- off_hours: n=327  W=168/L=159  WR=51.4%
- london: n=289  W=174/L=115  WR=60.2%
- london_open: n=283  W=192/L=91  WR=67.8%
- ny_open: n=218  W=133/L=85  WR=61.0%
- ny_mid: n=123  W=72/L=51  WR=58.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20c AND H60=H60e AND RSI=RSI4`
- Raw: n=108  W=93/L=15  WR=86.1%
- Refine: exclude ZS=ZS6 drops 7/15 losers (47%)
- **Final: n=101  W=93/L=8  WR=92.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; RSI 50-60 upper neutral  •  AVOID when zscore >+3 extreme

### W02.  `H20=H20c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=108  W=93/L=15  WR=86.1%
- Refine: exclude ZS=ZS6 drops 7/15 losers (47%)
- **Final: n=101  W=93/L=8  WR=92.1%**
- **Dir: LONG**  •  HTF20 neutral; RSI 50-60 upper neutral  •  AVOID when zscore >+3 extreme

### W03.  `H20=H20c AND H60=H60e AND RSI=RSI4 AND direction_exec=long`
- Raw: n=108  W=93/L=15  WR=86.1%
- Refine: exclude ZS=ZS6 drops 7/15 losers (47%)
- **Final: n=101  W=93/L=8  WR=92.1%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 strongly against; RSI 50-60 upper neutral  •  AVOID when zscore >+3 extreme

### W04.  `H20=H20d AND T1=T1a AND T4=T4c`
- Raw: n=88  W=78/L=10  WR=88.6%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W05.  `H60=H60a AND T4=T4c AND BBP=BBP0`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=asia_late drops 5/12 losers (42%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=asia_late

### W06.  `T4=T4c AND BBP=BBP0 AND direction_exec=short`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=asia_late drops 5/12 losers (42%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep below lower band  •  AVOID when session=asia_late

### W07.  `H60=H60a AND T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=asia_late drops 5/12 losers (42%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia_late

### W08.  `H60=H60a AND T4=T4c AND BBP=BBP0 AND direction_exec=short`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=asia_late drops 5/12 losers (42%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=asia_late

### W09.  `T4=T4c AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=asia_late drops 5/12 losers (42%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia_late

### W10.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 3/9 losers (33%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when strategy=delta_tag_and_go_v2

### W11.  `T1=T1c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 3/9 losers (33%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when strategy=delta_tag_and_go_v2

### W12.  `H60=H60a AND T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude session_bucket=asia_late drops 5/9 losers (56%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W13.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude session_bucket=asia_late drops 5/9 losers (56%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W14.  `H60=H60a AND T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude H20=H20e drops 6/10 losers (60%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W15.  `T1=T1c AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude H20=H20e drops 6/10 losers (60%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W16.  `H20=H20a AND RSI=RSI4 AND session_bucket=asia_late`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude T1=T1c drops 5/7 losers (71%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia_late  •  AVOID when 1h trend AGAINST trade

### W17.  `H20=H20d AND T4=T4a AND RSI=RSI4`
- Raw: n=63  W=59/L=4  WR=93.7%
- Refine: exclude BBP=BBP1 drops 2/4 losers (50%)
- **Final: n=61  W=59/L=2  WR=96.7%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when just touched lower band

### W18.  `H60=H60e AND RSI=RSI4 AND session_bucket=london`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS3 drops 5/9 losers (56%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=london  •  AVOID when zscore -1 to +1 neutral

### W19.  `RSI=RSI4 AND direction_exec=long AND session_bucket=london`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS3 drops 5/9 losers (56%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=london  •  AVOID when zscore -1 to +1 neutral

### W20.  `H60=H60e AND RSI=RSI4 AND direction_exec=long AND session_bucket=london`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS3 drops 5/9 losers (56%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=london  •  AVOID when zscore -1 to +1 neutral

### W21.  `H20=H20a AND H60=H60e AND BBP=BBP2`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude RSI=RSI2 drops 2/4 losers (50%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; lower third  •  AVOID when RSI 30-40 weak

### W22.  `H20=H20a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude RSI=RSI2 drops 2/4 losers (50%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; lower third  •  AVOID when RSI 30-40 weak

### W23.  `H20=H20a AND H60=H60e AND BBP=BBP2 AND direction_exec=long`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude RSI=RSI2 drops 2/4 losers (50%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; lower third  •  AVOID when RSI 30-40 weak

### W24.  `H20=H20d AND H60=H60a AND T4=T4c`
- Raw: n=59  W=53/L=6  WR=89.8%
- Refine: exclude RSI=RSI4 drops 6/6 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W25.  `H20=H20d AND T4=T4c AND direction_exec=short`
- Raw: n=59  W=53/L=6  WR=89.8%
- Refine: exclude RSI=RSI4 drops 6/6 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND BBP=BBP0 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=138  W=50/L=88  WR=36.2%
- Sharpen: sharpest is T4=T4a (35/88 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; zscore -3 to -2 deep oversold; session=asia  •  ONLY when 4h trend WITH trade

### L02.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=138  W=50/L=88  WR=36.2%
- Sharpen: sharpest is T4=T4a (35/88 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: LONG**  •  deep below lower band; zscore -3 to -2 deep oversold; session=asia  •  ONLY when 4h trend WITH trade

### L03.  `H20=H20c AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=116  W=46/L=70  WR=39.7%
- Sharpen: sharpest is BBP=BBP0 (25/70 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when deep below lower band

### L04.  `H20=H20c AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=116  W=46/L=70  WR=39.7%
- Sharpen: sharpest is BBP=BBP0 (25/70 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when deep below lower band

### L05.  `H60=H60a AND T1=T1a AND session_bucket=off_hours`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is ZS=ZS1 (25/67 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=off_hours  •  ONLY when zscore -3 to -2 deep oversold

### L06.  `T1=T1a AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is ZS=ZS1 (25/67 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; session=off_hours  •  ONLY when zscore -3 to -2 deep oversold

### L07.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is ZS=ZS1 (25/67 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=off_hours  •  ONLY when zscore -3 to -2 deep oversold

### L08.  `H20=H20c AND H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is BBP=BBP0 (21/57 of losers there)
- **Sharp: n=27  W=6/L=21  WR=22.2%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  ONLY when deep below lower band

### L09.  `H20=H20c AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is BBP=BBP0 (21/57 of losers there)
- **Sharp: n=27  W=6/L=21  WR=22.2%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend WITH trade; session=asia  •  ONLY when deep below lower band

### L10.  `T1=T1a AND RSI=RSI3 AND session_bucket=off_hours`
- Raw: n=90  W=25/L=65  WR=27.8%
- Sharpen: sharpest is ZS=ZS1 (20/65 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=off_hours  •  ONLY when zscore -3 to -2 deep oversold

### L11.  `H20=H20c AND H60=H60a AND RSI=RSI4`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is ZS=ZS5 (19/55 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L12.  `H20=H20c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is ZS=ZS5 (19/55 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L13.  `H20=H20c AND H60=H60a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is ZS=ZS5 (19/55 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L14.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND session_bucket=off_hours`
- Raw: n=82  W=25/L=57  WR=30.5%
- Sharpen: sharpest is ZS=ZS1 (20/57 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; session=off_hours  •  ONLY when zscore -3 to -2 deep oversold

### L15.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=82  W=25/L=57  WR=30.5%
- Sharpen: sharpest is ZS=ZS1 (20/57 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=off_hours  •  ONLY when zscore -3 to -2 deep oversold

### L16.  `H60=H60a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=82  W=32/L=50  WR=39.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_close

### L17.  `T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=82  W=32/L=50  WR=39.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_close

### L18.  `H60=H60a AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=82  W=32/L=50  WR=39.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_close

### L19.  `T1=T1c AND T4=T4a AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=79  W=31/L=48  WR=39.2%
- Sharpen: sharpest is H60=H60e (26/48 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; deep below lower band; session=asia  •  ONLY when HTF60 strongly against

### L20.  `H20=H20b AND T4=T4c AND BBP=BBP4`
- Raw: n=78  W=30/L=48  WR=38.5%
- Sharpen: sharpest is RSI=RSI4 (17/48 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; upper third  •  ONLY when RSI 50-60 upper neutral

### L21.  `T1=T1a AND T4=T4c AND session_bucket=off_hours`
- Raw: n=69  W=20/L=49  WR=29.0%
- Sharpen: sharpest is H20=H20b (22/49 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=off_hours  •  ONLY when HTF20 slightly aligned

### L22.  `T4=T4c AND BBP=BBP4 AND ZS=ZS3`
- Raw: n=69  W=23/L=46  WR=33.3%
- Sharpen: sharpest is H20=H20e (20/46 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; zscore -1 to +1 neutral  •  ONLY when HTF20 strongly against

### L23.  `H20=H20d AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is ZS=ZS2 (14/42 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -2 to -1 oversold

### L24.  `H20=H20d AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is ZS=ZS2 (14/42 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -2 to -1 oversold

### L25.  `H20=H20d AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is ZS=ZS2 (14/42 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -2 to -1 oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
