# GBP_JPY — R26 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **5,630**  (W=3,512 / L=2,118)  -  WR: **62.4%**

## Session distribution

- asia: n=3166  W=2008/L=1158  WR=63.4%
- ny_close: n=990  W=608/L=382  WR=61.4%
- asia_late: n=410  W=257/L=153  WR=62.7%
- off_hours: n=337  W=195/L=142  WR=57.9%
- london: n=277  W=161/L=116  WR=58.1%
- ny_open: n=192  W=120/L=72  WR=62.5%
- ny_mid: n=138  W=80/L=58  WR=58.0%
- london_open: n=120  W=83/L=37  WR=69.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `RSI=RSI4 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=214  W=182/L=32  WR=85.0%
- Refine: exclude session_bucket=off_hours drops 7/32 losers (22%)
- **Final: n=199  W=174/L=25  WR=87.4%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=off_hours

### W02.  `H20=H20d AND T1=T1c AND session_bucket=asia`
- Raw: n=156  W=138/L=18  WR=88.5%
- Refine: exclude H60=H60e drops 18/18 losers (100%)
- **Final: n=83  W=83/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; session=asia  •  AVOID when HTF60 strongly against

### W03.  `RSI=RSI4 AND ZS=ZS3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=153  W=133/L=20  WR=86.9%
- Refine: no further refinement
- **Final: n=153  W=133/L=20  WR=86.9%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -1 to +1 neutral; session=asia

### W04.  `H60=H60a AND RSI=RSI4 AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=150  W=130/L=20  WR=86.7%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 5/20 losers (25%)
- **Final: n=132  W=117/L=15  WR=88.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W05.  `H20=H20d AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=133  W=115/L=18  WR=86.5%
- Refine: exclude H60=H60e drops 18/18 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend AGAINST trade; session=asia  •  AVOID when HTF60 strongly against

### W06.  `BBP=BBP3 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=127  W=110/L=17  WR=86.6%
- Refine: exclude session_bucket=off_hours drops 5/17 losers (29%)
- **Final: n=122  W=110/L=12  WR=90.2%**
- **Dir: LONG**  •  middle of band; RSI 50-60 upper neutral  •  AVOID when session=off_hours

### W07.  `BBP=BBP3 AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=127  W=110/L=17  WR=86.6%
- Refine: exclude session_bucket=off_hours drops 5/17 losers (29%)
- **Final: n=122  W=110/L=12  WR=90.2%**
- **Dir: LONG**  •  middle of band; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=off_hours

### W08.  `H60=H60a AND BBP=BBP3 AND RSI=RSI4`
- Raw: n=125  W=108/L=17  WR=86.4%
- Refine: exclude session_bucket=off_hours drops 5/17 losers (29%)
- **Final: n=120  W=108/L=12  WR=90.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; middle of band; RSI 50-60 upper neutral  •  AVOID when session=off_hours

### W09.  `H60=H60a AND BBP=BBP3 AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=125  W=108/L=17  WR=86.4%
- Refine: exclude session_bucket=off_hours drops 5/17 losers (29%)
- **Final: n=120  W=108/L=12  WR=90.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; middle of band; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=off_hours

### W10.  `H60=H60a AND BBP=BBP3 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=125  W=108/L=17  WR=86.4%
- Refine: exclude session_bucket=off_hours drops 5/17 losers (29%)
- **Final: n=120  W=108/L=12  WR=90.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; middle of band; RSI 50-60 upper neutral  •  AVOID when session=off_hours

### W11.  `H20=H20e AND T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=119  W=108/L=11  WR=90.8%
- Refine: exclude H60=H60e drops 11/11 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W12.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude session_bucket=asia drops 11/14 losers (79%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W13.  `H60=H60e AND T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=105  W=92/L=13  WR=87.6%
- Refine: exclude session_bucket=asia drops 9/13 losers (69%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W14.  `H20=H20e AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude RSI=RSI3 drops 11/15 losers (73%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W15.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude RSI=RSI3 drops 11/15 losers (73%)
- **Final: n=68  W=64/L=4  WR=94.1%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W16.  `T4=T4a AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude H20=H20a drops 13/14 losers (93%)
- **Final: n=32  W=31/L=1  WR=96.9%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when HTF20 aligned WITH trade

### W17.  `T4=T4a AND BBP=BBP0 AND ZS=ZS0`
- Raw: n=98  W=87/L=11  WR=88.8%
- Refine: exclude T1=T1a drops 10/11 losers (91%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; zscore <-3 extreme  •  AVOID when 1h trend WITH trade

### W18.  `H20=H20d AND RSI=RSI4 AND direction_exec=long`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude session_bucket=london drops 13/14 losers (93%)
- **Final: n=84  W=83/L=1  WR=98.8%**
- **Dir: LONG**  •  HTF20 mildly against; RSI 50-60 upper neutral  •  AVOID when session=london

### W19.  `H60=H60a AND BBP=BBP3 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=96  W=87/L=9  WR=90.6%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 4/9 losers (44%)
- **Final: n=85  W=80/L=5  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; middle of band; RSI 50-60 upper neutral; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W20.  `BBP=BBP3 AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=96  W=87/L=9  WR=90.6%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 4/9 losers (44%)
- **Final: n=85  W=80/L=5  WR=94.1%**
- **Dir: LONG**  •  middle of band; RSI 50-60 upper neutral; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W21.  `H20=H20e AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude RSI=RSI3 drops 10/14 losers (71%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W22.  `H20=H20e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude RSI=RSI3 drops 10/14 losers (71%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W23.  `H60=H60e AND T4=T4a AND session_bucket=london`
- Raw: n=95  W=88/L=7  WR=92.6%
- Refine: exclude BBP=BBP2 drops 6/7 losers (86%)
- **Final: n=68  W=67/L=1  WR=98.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=london  •  AVOID when lower third

### W24.  `T4=T4a AND direction_exec=short AND session_bucket=london`
- Raw: n=95  W=88/L=7  WR=92.6%
- Refine: exclude BBP=BBP2 drops 6/7 losers (86%)
- **Final: n=68  W=67/L=1  WR=98.5%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london  •  AVOID when lower third

### W25.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=london`
- Raw: n=95  W=88/L=7  WR=92.6%
- Refine: exclude BBP=BBP2 drops 6/7 losers (86%)
- **Final: n=68  W=67/L=1  WR=98.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=london  •  AVOID when lower third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60e AND RSI=RSI4`
- Raw: n=226  W=89/L=137  WR=39.4%
- Sharpen: sharpest is T4=T4a (49/137 of losers there)
- **Sharp: n=55  W=6/L=49  WR=10.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L02.  `H20=H20a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=226  W=89/L=137  WR=39.4%
- Sharpen: sharpest is T4=T4a (49/137 of losers there)
- **Sharp: n=55  W=6/L=49  WR=10.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L03.  `H20=H20a AND H60=H60e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=226  W=89/L=137  WR=39.4%
- Sharpen: sharpest is T4=T4a (49/137 of losers there)
- **Sharp: n=55  W=6/L=49  WR=10.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L04.  `H20=H20e AND T4=T4c AND ZS=ZS1`
- Raw: n=194  W=77/L=117  WR=39.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=194  W=77/L=117  WR=39.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold

### L05.  `T1=T1a AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=183  W=70/L=113  WR=38.3%
- Sharpen: sharpest is T4=T4a (66/113 of losers there)
- **Sharp: n=73  W=7/L=66  WR=9.6%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L06.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS1`
- Raw: n=181  W=70/L=111  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=181  W=70/L=111  WR=38.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold

### L07.  `H20=H20e AND T1=T1a AND T4=T4c AND ZS=ZS1`
- Raw: n=175  W=69/L=106  WR=39.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=175  W=69/L=106  WR=39.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold

### L08.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=171  W=64/L=107  WR=37.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=171  W=64/L=107  WR=37.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold

### L09.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=169  W=66/L=103  WR=39.1%
- Sharpen: sharpest is T4=T4a (66/103 of losers there)
- **Sharp: n=73  W=7/L=66  WR=9.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L10.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=155  W=59/L=96  WR=38.1%
- Sharpen: sharpest is BBP=BBP5 (52/96 of losers there)
- **Sharp: n=69  W=17/L=52  WR=24.6%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=asia  •  ONLY when just touched upper band

### L11.  `H20=H20b AND T1=T1a AND direction_exec=short`
- Raw: n=152  W=48/L=104  WR=31.6%
- Sharpen: sharpest is RSI=RSI4 (46/104 of losers there)
- **Sharp: n=55  W=9/L=46  WR=16.4%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L12.  `H20=H20a AND H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=135  W=51/L=84  WR=37.8%
- Sharpen: sharpest is T4=T4a (43/84 of losers there)
- **Sharp: n=45  W=2/L=43  WR=4.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L13.  `H20=H20a AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=135  W=51/L=84  WR=37.8%
- Sharpen: sharpest is T4=T4a (43/84 of losers there)
- **Sharp: n=45  W=2/L=43  WR=4.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L14.  `H60=H60e AND T4=T4c AND BBP=BBP0`
- Raw: n=127  W=48/L=79  WR=37.8%
- Sharpen: sharpest is ZS=ZS0 (33/79 of losers there)
- **Sharp: n=34  W=1/L=33  WR=2.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L15.  `H60=H60e AND T4=T4c AND BBP=BBP0 AND direction_exec=short`
- Raw: n=127  W=48/L=79  WR=37.8%
- Sharpen: sharpest is ZS=ZS0 (33/79 of losers there)
- **Sharp: n=34  W=1/L=33  WR=2.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L16.  `H20=H20b AND T1=T1a AND session_bucket=asia`
- Raw: n=125  W=39/L=86  WR=31.2%
- Sharpen: sharpest is ZS=ZS2 (28/86 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; session=asia  •  ONLY when zscore -2 to -1 oversold

### L17.  `H60=H60e AND T4=T4c AND BBP=BBP1`
- Raw: n=120  W=46/L=74  WR=38.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=120  W=46/L=74  WR=38.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; just touched lower band

### L18.  `T4=T4c AND BBP=BBP1 AND direction_exec=short`
- Raw: n=120  W=46/L=74  WR=38.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=120  W=46/L=74  WR=38.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; just touched lower band

### L19.  `H60=H60e AND T4=T4c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=120  W=46/L=74  WR=38.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=120  W=46/L=74  WR=38.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold

### L20.  `H60=H60e AND T4=T4c AND BBP=BBP1 AND direction_exec=short`
- Raw: n=120  W=46/L=74  WR=38.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=120  W=46/L=74  WR=38.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; just touched lower band

### L21.  `T4=T4c AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=120  W=46/L=74  WR=38.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=120  W=46/L=74  WR=38.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold

### L22.  `H20=H20e AND T4=T4c AND BBP=BBP1`
- Raw: n=116  W=43/L=73  WR=37.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=116  W=43/L=73  WR=37.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched lower band

### L23.  `H20=H20e AND T4=T4c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=116  W=43/L=73  WR=37.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=116  W=43/L=73  WR=37.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold

### L24.  `H60=H60a AND direction_exec=long AND session_bucket=london`
- Raw: n=113  W=33/L=80  WR=29.2%
- Sharpen: sharpest is T4=T4c (55/80 of losers there)
- **Sharp: n=58  W=3/L=55  WR=5.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=london  •  ONLY when 4h trend AGAINST trade

### L25.  `H20=H20e AND T4=T4c AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=112  W=39/L=73  WR=34.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=112  W=39/L=73  WR=34.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched lower band; RSI 40-50 lower neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(55/46) | T4c(45/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
