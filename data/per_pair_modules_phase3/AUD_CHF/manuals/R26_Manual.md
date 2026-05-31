# AUD_CHF — R26 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **800**  (W=522 / L=278)  -  WR: **65.2%**

## Session distribution

- asia: n=298  W=198/L=100  WR=66.4%
- ny_close: n=137  W=90/L=47  WR=65.7%
- ny_mid: n=113  W=65/L=48  WR=57.5%
- ny_open: n=90  W=58/L=32  WR=64.4%
- london_open: n=69  W=48/L=21  WR=69.6%
- off_hours: n=48  W=32/L=16  WR=66.7%
- london: n=33  W=22/L=11  WR=66.7%
- asia_late: n=12  W=9/L=3  WR=75.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=150  W=128/L=22  WR=85.3%
- Refine: exclude BBP=BBP0 drops 11/22 losers (50%)
- **Final: n=131  W=120/L=11  WR=91.6%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak  •  AVOID when deep below lower band

### W02.  `T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=147  W=127/L=20  WR=86.4%
- Refine: exclude BBP=BBP0 drops 11/20 losers (55%)
- **Final: n=128  W=119/L=9  WR=93.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when deep below lower band

### W03.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=147  W=127/L=20  WR=86.4%
- Refine: exclude BBP=BBP0 drops 11/20 losers (55%)
- **Final: n=128  W=119/L=9  WR=93.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when deep below lower band

### W04.  `H60=H60e AND T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=138  W=118/L=20  WR=85.5%
- Refine: exclude BBP=BBP0 drops 11/20 losers (55%)
- **Final: n=123  W=114/L=9  WR=92.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when deep below lower band

### W05.  `H20=H20e AND T4=T4a AND RSI=RSI2`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude BBP=BBP0 drops 10/19 losers (53%)
- **Final: n=109  W=100/L=9  WR=91.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when deep below lower band

### W06.  `H20=H20e AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude BBP=BBP0 drops 10/19 losers (53%)
- **Final: n=109  W=100/L=9  WR=91.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when deep below lower band

### W07.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=124  W=107/L=17  WR=86.3%
- Refine: exclude BBP=BBP0 drops 10/17 losers (59%)
- **Final: n=106  W=99/L=7  WR=93.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when deep below lower band

### W08.  `T4=T4a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude ZS=ZS3 drops 5/17 losers (29%)
- **Final: n=108  W=96/L=12  WR=88.9%**
- **Dir: SHORT**  •  4h trend WITH trade; lower third  •  AVOID when zscore -1 to +1 neutral

### W09.  `H60=H60e AND T4=T4a AND BBP=BBP2`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude ZS=ZS3 drops 5/17 losers (29%)
- **Final: n=105  W=93/L=12  WR=88.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third  •  AVOID when zscore -1 to +1 neutral

### W10.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude ZS=ZS3 drops 5/17 losers (29%)
- **Final: n=105  W=93/L=12  WR=88.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; lower third  •  AVOID when zscore -1 to +1 neutral

### W11.  `T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude RSI=RSI3 drops 5/15 losers (33%)
- **Final: n=104  W=94/L=10  WR=90.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when RSI 40-50 lower neutral

### W12.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude RSI=RSI3 drops 5/15 losers (33%)
- **Final: n=104  W=94/L=10  WR=90.4%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when RSI 40-50 lower neutral

### W13.  `H60=H60e AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=110  W=95/L=15  WR=86.4%
- Refine: exclude RSI=RSI3 drops 5/15 losers (33%)
- **Final: n=101  W=91/L=10  WR=90.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when RSI 40-50 lower neutral

### W14.  `T4=T4a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=108  W=96/L=12  WR=88.9%
- Refine: exclude RSI=RSI3 drops 3/12 losers (25%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W15.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=108  W=96/L=12  WR=88.9%
- Refine: exclude RSI=RSI3 drops 3/12 losers (25%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: SHORT**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W16.  `T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=105  W=94/L=11  WR=89.5%
- Refine: exclude RSI=RSI3 drops 3/11 losers (27%)
- **Final: n=98  W=90/L=8  WR=91.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W17.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=105  W=94/L=11  WR=89.5%
- Refine: exclude RSI=RSI3 drops 3/11 losers (27%)
- **Final: n=98  W=90/L=8  WR=91.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W18.  `T1=T1a AND T4=T4a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=105  W=94/L=11  WR=89.5%
- Refine: exclude RSI=RSI3 drops 3/11 losers (27%)
- **Final: n=98  W=90/L=8  WR=91.8%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W19.  `H60=H60e AND T4=T4a AND ZS=ZS2`
- Raw: n=105  W=93/L=12  WR=88.6%
- Refine: exclude RSI=RSI3 drops 3/12 losers (25%)
- **Final: n=96  W=87/L=9  WR=90.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W20.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=105  W=93/L=12  WR=88.6%
- Refine: exclude RSI=RSI3 drops 3/12 losers (25%)
- **Final: n=96  W=87/L=9  WR=90.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W21.  `H60=H60e AND T4=T4a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=105  W=93/L=12  WR=88.6%
- Refine: exclude RSI=RSI3 drops 3/12 losers (25%)
- **Final: n=96  W=87/L=9  WR=90.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W22.  `H60=H60e AND T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=102  W=91/L=11  WR=89.2%
- Refine: exclude RSI=RSI3 drops 3/11 losers (27%)
- **Final: n=95  W=87/L=8  WR=91.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W23.  `H20=H20e AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude RSI=RSI3 drops 5/15 losers (33%)
- **Final: n=92  W=82/L=10  WR=89.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when RSI 40-50 lower neutral

### W24.  `H20=H20e AND T4=T4a AND ZS=ZS2`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude RSI=RSI3 drops 3/12 losers (25%)
- **Final: n=87  W=78/L=9  WR=89.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W25.  `H20=H20e AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude RSI=RSI3 drops 3/12 losers (25%)
- **Final: n=87  W=78/L=9  WR=89.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=74  W=28/L=46  WR=37.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=74  W=28/L=46  WR=37.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third

### L02.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=74  W=28/L=46  WR=37.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=74  W=28/L=46  WR=37.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third

### L03.  `H60=H60a AND T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=73  W=28/L=45  WR=38.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; lower third

### L04.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=70  W=27/L=43  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=70  W=27/L=43  WR=38.6%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak

### L05.  `T4=T4c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=68  W=25/L=43  WR=36.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=68  W=25/L=43  WR=36.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -2 to -1 oversold

### L06.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=68  W=25/L=43  WR=36.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=68  W=25/L=43  WR=36.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold

### L07.  `H60=H60a AND T4=T4c AND ZS=ZS2`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=67  W=25/L=42  WR=37.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold

### L08.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=67  W=25/L=42  WR=37.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold

### L09.  `H60=H60a AND T4=T4c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=67  W=25/L=42  WR=37.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold

### L10.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=67  W=26/L=41  WR=38.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak

### L11.  `T1=T1c AND T4=T4c AND ZS=ZS2`
- Raw: n=66  W=23/L=43  WR=34.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=66  W=23/L=43  WR=34.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold

### L12.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=66  W=23/L=43  WR=34.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=66  W=23/L=43  WR=34.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold

### L13.  `T1=T1c AND T4=T4c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=66  W=23/L=43  WR=34.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=66  W=23/L=43  WR=34.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold

### L14.  `H60=H60a AND T1=T1c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=66  W=26/L=40  WR=39.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third; RSI 30-40 weak

### L15.  `H60=H60a AND T1=T1c AND T4=T4c AND ZS=ZS2`
- Raw: n=65  W=23/L=42  WR=35.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=65  W=23/L=42  WR=35.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold

### L16.  `H20=H20a AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=65  W=24/L=41  WR=36.9%
- Sharpen: sharpest is RSI=RSI1 (19/41 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L17.  `H20=H20a AND T4=T4c AND ZS=ZS2`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=61  W=24/L=37  WR=39.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold

### L18.  `H20=H20a AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=61  W=24/L=37  WR=39.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold

### L19.  `H20=H20a AND T4=T4c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=61  W=24/L=37  WR=39.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold

### L20.  `H20=H20a AND H60=H60a AND T4=T4c AND ZS=ZS2`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=60  W=24/L=36  WR=40.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold

### L21.  `H20=H20a AND T1=T1c AND T4=T4c AND ZS=ZS2`
- Raw: n=59  W=22/L=37  WR=37.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=59  W=22/L=37  WR=37.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold

### L22.  `H20=H20a AND T1=T1c AND T4=T4c AND BBP=BBP1`
- Raw: n=53  W=20/L=33  WR=37.7%
- Sharpen: sharpest is RSI=RSI1 (16/33 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L23.  `T4=T4c AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=47  W=16/L=31  WR=34.0%
- Sharpen: sharpest is H20=H20a (19/31 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when HTF20 aligned WITH trade

### L24.  `H60=H60a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=41  W=10/L=31  WR=24.4%
- Sharpen: sharpest is RSI=RSI1 (12/31 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when RSI 20-30 oversold

### L25.  `T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=41  W=10/L=31  WR=24.4%
- Sharpen: sharpest is RSI=RSI1 (12/31 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when RSI 20-30 oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(52/34) | H20a(36/55) |
| H60 | H60e(57/37) | H60a(40/62) |
| T1 | T1a(59/38) | T1c(41/62) |
| T4 | T4a(60/40) | T4c(39/58) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(59/37) | long(41/63) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
