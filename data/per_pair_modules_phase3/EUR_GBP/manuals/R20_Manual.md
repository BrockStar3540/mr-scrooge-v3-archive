# EUR_GBP — R20 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,141**  (W=764 / L=377)  -  WR: **67.0%**

## Session distribution

- ny_close: n=313  W=213/L=100  WR=68.1%
- asia: n=284  W=180/L=104  WR=63.4%
- ny_open: n=174  W=118/L=56  WR=67.8%
- london_open: n=164  W=106/L=58  WR=64.6%
- london: n=78  W=60/L=18  WR=76.9%
- off_hours: n=58  W=34/L=24  WR=58.6%
- ny_mid: n=38  W=27/L=11  WR=71.1%
- asia_late: n=32  W=26/L=6  WR=81.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=143  W=123/L=20  WR=86.0%
- Refine: exclude strategy_id=charlie_compression_breakout drops 7/20 losers (35%)
- **Final: n=127  W=114/L=13  WR=89.8%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  AVOID when strategy=charlie_compression_breakout

### W02.  `H60=H60a AND T4=T4c AND RSI=RSI2`
- Raw: n=141  W=124/L=17  WR=87.9%
- Refine: exclude session_bucket=asia drops 12/17 losers (71%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when session=asia

### W03.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=127  W=112/L=15  WR=88.2%
- Refine: exclude strategy_id=charlie_compression_breakout drops 6/15 losers (40%)
- **Final: n=113  W=104/L=9  WR=92.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  AVOID when strategy=charlie_compression_breakout

### W04.  `T4=T4c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=127  W=112/L=15  WR=88.2%
- Refine: exclude strategy_id=charlie_compression_breakout drops 6/15 losers (40%)
- **Final: n=113  W=104/L=9  WR=92.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  AVOID when strategy=charlie_compression_breakout

### W05.  `H60=H60a AND T1=T1c AND direction_exec=long`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude H20=H20a drops 7/18 losers (39%)
- **Final: n=101  W=90/L=11  WR=89.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when HTF20 aligned WITH trade

### W06.  `H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=118  W=102/L=16  WR=86.4%
- Refine: exclude session_bucket=asia drops 11/16 losers (69%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=asia

### W07.  `H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=118  W=102/L=16  WR=86.4%
- Refine: exclude session_bucket=asia drops 11/16 losers (69%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when session=asia

### W08.  `H60=H60a AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=118  W=102/L=16  WR=86.4%
- Refine: exclude session_bucket=asia drops 11/16 losers (69%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=asia

### W09.  `H60=H60a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude T4=T4a drops 11/15 losers (73%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W10.  `H60=H60a AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude T4=T4a drops 11/15 losers (73%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W11.  `H20=H20a AND T1=T1c AND direction_exec=long`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude session_bucket=asia drops 9/9 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=asia

### W12.  `H20=H20e AND T4=T4c AND session_bucket=ny_close`
- Raw: n=75  W=68/L=7  WR=90.7%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W13.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=75  W=68/L=7  WR=90.7%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W14.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=75  W=68/L=7  WR=90.7%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W15.  `H20=H20d AND T4=T4c AND ZS=ZS1`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude session_bucket=ny_close drops 5/10 losers (50%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W16.  `H20=H20d AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude session_bucket=ny_close drops 5/10 losers (50%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W17.  `H20=H20d AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude session_bucket=ny_close drops 5/10 losers (50%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W18.  `H20=H20b AND T4=T4c AND RSI=RSI2`
- Raw: n=74  W=68/L=6  WR=91.9%
- Refine: exclude ZS=ZS4 drops 5/6 losers (83%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when zscore +1 to +2 overbought

### W19.  `T4=T4c AND BBP=BBP2 AND session_bucket=ny_close`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude T1=T1a drops 4/10 losers (40%)
- **Final: n=62  W=56/L=6  WR=90.3%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; session=ny_close  •  AVOID when 1h trend WITH trade

### W20.  `T1=T1c AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=london_open drops 5/10 losers (50%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 20-30 oversold  •  AVOID when session=london_open

### W21.  `T4=T4c AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=london_open drops 5/10 losers (50%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 20-30 oversold  •  AVOID when session=london_open

### W22.  `T4=T4c AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude T1=T1a drops 4/10 losers (40%)
- **Final: n=60  W=54/L=6  WR=90.0%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_close  •  AVOID when 1h trend WITH trade

### W23.  `BBP=BBP2 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=london_open drops 5/10 losers (50%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: LONG**  •  lower third; RSI 20-30 oversold  •  AVOID when session=london_open

### W24.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=london_open drops 5/10 losers (50%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; RSI 20-30 oversold  •  AVOID when session=london_open

### W25.  `T1=T1c AND BBP=BBP2 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=london_open drops 5/10 losers (50%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; RSI 20-30 oversold  •  AVOID when session=london_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=84  W=33/L=51  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_close (15/51 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=ny_close

### L02.  `T4=T4a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=76  W=29/L=47  WR=38.2%
- Sharpen: sharpest is session_bucket=ny_close (14/47 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=ny_close

### L03.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_close (10/40 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=ny_close

### L04.  `T4=T4a AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_close (10/40 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=ny_close

### L05.  `T4=T4a AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=60  W=22/L=38  WR=36.7%
- Sharpen: sharpest is session_bucket=ny_close (12/38 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; RSI 30-40 weak  •  ONLY when session=ny_close

### L06.  `T4=T4a AND BBP=BBP1 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=60  W=22/L=38  WR=36.7%
- Sharpen: sharpest is session_bucket=ny_close (12/38 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=ny_close

### L07.  `H20=H20a AND T1=T1a AND session_bucket=asia`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is RSI=RSI1 (19/36 of losers there)
- **Sharp: n=27  W=8/L=19  WR=29.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  ONLY when RSI 20-30 oversold

### L08.  `H20=H20a AND direction_exec=short AND session_bucket=asia`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is RSI=RSI1 (19/36 of losers there)
- **Sharp: n=27  W=8/L=19  WR=29.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=asia  •  ONLY when RSI 20-30 oversold

### L09.  `H20=H20a AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is RSI=RSI1 (19/36 of losers there)
- **Sharp: n=27  W=8/L=19  WR=29.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  ONLY when RSI 20-30 oversold

### L10.  `T1=T1c AND T4=T4a AND RSI=RSI2`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is H20=H20d (22/32 of losers there)
- **Sharp: n=31  W=9/L=22  WR=29.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 mildly against

### L11.  `T4=T4a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is H20=H20d (22/32 of losers there)
- **Sharp: n=31  W=9/L=22  WR=29.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 mildly against

### L12.  `T1=T1c AND T4=T4a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is H20=H20d (22/32 of losers there)
- **Sharp: n=31  W=9/L=22  WR=29.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 mildly against

### L13.  `T1=T1a AND T4=T4a AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is session_bucket=ny_close (8/32 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band; RSI 30-40 weak  •  ONLY when session=ny_close

### L14.  `T4=T4a AND BBP=BBP1 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is session_bucket=ny_close (8/32 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; just touched lower band; RSI 30-40 weak  •  ONLY when session=ny_close

### L15.  `H60=H60b AND T1=T1a AND direction_exec=short`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is H20=H20e (21/32 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 1h trend WITH trade  •  ONLY when HTF20 strongly against

### L16.  `H20=H20d AND T4=T4a AND RSI=RSI2`
- Raw: n=48  W=17/L=31  WR=35.4%
- Sharpen: sharpest is session_bucket=london_open (6/31 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when session=london_open

### L17.  `H20=H20b AND T4=T4a AND ZS=ZS1`
- Raw: n=48  W=19/L=29  WR=39.6%
- Sharpen: sharpest is BBP=BBP1 (20/29 of losers there)
- **Sharp: n=29  W=9/L=20  WR=31.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L18.  `H20=H20b AND T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=48  W=19/L=29  WR=39.6%
- Sharpen: sharpest is BBP=BBP1 (20/29 of losers there)
- **Sharp: n=29  W=9/L=20  WR=31.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L19.  `H20=H20b AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=48  W=19/L=29  WR=39.6%
- Sharpen: sharpest is BBP=BBP1 (20/29 of losers there)
- **Sharp: n=29  W=9/L=20  WR=31.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L20.  `H60=H60a AND T4=T4a AND ZS=ZS1`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is H20=H20a (14/28 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when HTF20 aligned WITH trade

### L21.  `H60=H60a AND T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is H20=H20a (14/28 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when HTF20 aligned WITH trade

### L22.  `H60=H60a AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is H20=H20a (14/28 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when HTF20 aligned WITH trade

### L23.  `H20=H20a AND T4=T4a AND ZS=ZS1`
- Raw: n=43  W=16/L=27  WR=37.2%
- Sharpen: sharpest is H60=H60a (14/27 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L24.  `H20=H20a AND T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=43  W=16/L=27  WR=37.2%
- Sharpen: sharpest is H60=H60a (14/27 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L25.  `H20=H20a AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=43  W=16/L=27  WR=37.2%
- Sharpen: sharpest is H60=H60a (14/27 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(32/25) | H60b(6/12) |
| T1 | T1c(61/41) | T1a(39/59) |
| T4 | T4c(66/35) | T4a(34/65) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(61/40) | short(39/60) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
