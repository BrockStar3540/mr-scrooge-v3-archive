# EUR_GBP — R32 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **918**  (W=590 / L=328)  -  WR: **64.3%**

## Session distribution

- ny_mid: n=340  W=209/L=131  WR=61.5%
- london_open: n=211  W=141/L=70  WR=66.8%
- ny_open: n=166  W=106/L=60  WR=63.9%
- london: n=98  W=65/L=33  WR=66.3%
- ny_close: n=56  W=39/L=17  WR=69.6%
- off_hours: n=22  W=14/L=8  WR=63.6%
- asia: n=17  W=10/L=7  WR=58.8%
- asia_late: n=8  W=6/L=2  WR=75.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60d AND T1=T1c AND T4=T4c`
- Raw: n=62  W=56/L=6  WR=90.3%
- Refine: exclude BBP=BBP2 drops 4/6 losers (67%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when lower third

### W02.  `H60=H60d AND T4=T4c AND direction_exec=long`
- Raw: n=62  W=56/L=6  WR=90.3%
- Refine: exclude BBP=BBP2 drops 4/6 losers (67%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: LONG**  •  HTF60 mildly against; 4h trend AGAINST trade  •  AVOID when lower third

### W03.  `H60=H60d AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=62  W=56/L=6  WR=90.3%
- Refine: exclude BBP=BBP2 drops 4/6 losers (67%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when lower third

### W04.  `H20=H20a AND T1=T1c AND T4=T4c`
- Raw: n=59  W=51/L=8  WR=86.4%
- Refine: exclude H60=H60a drops 6/8 losers (75%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when HTF60 aligned WITH trade

### W05.  `H20=H20a AND T4=T4c AND direction_exec=long`
- Raw: n=59  W=51/L=8  WR=86.4%
- Refine: exclude H60=H60a drops 6/8 losers (75%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when HTF60 aligned WITH trade

### W06.  `H20=H20a AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=59  W=51/L=8  WR=86.4%
- Refine: exclude H60=H60a drops 6/8 losers (75%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when HTF60 aligned WITH trade

### W07.  `H60=H60e AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude H20=H20d drops 4/7 losers (57%)
- **Final: n=38  W=35/L=3  WR=92.1%**
- **Dir: ?**  •  HTF60 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 mildly against

### W08.  `H20=H20a AND T4=T4c AND RSI=RSI2`
- Raw: n=55  W=47/L=8  WR=85.5%
- Refine: exclude T1=T1c drops 8/8 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when 1h trend AGAINST trade

### W09.  `H60=H60e AND T1=T1c AND BBP=BBP1`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude H20=H20d drops 4/6 losers (67%)
- **Final: n=30  W=28/L=2  WR=93.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched lower band  •  AVOID when HTF20 mildly against

### W10.  `H60=H60e AND T4=T4c AND BBP=BBP1`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude H20=H20d drops 4/6 losers (67%)
- **Final: n=30  W=28/L=2  WR=93.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; just touched lower band  •  AVOID when HTF20 mildly against

### W11.  `H60=H60e AND BBP=BBP1 AND direction_exec=long`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude H20=H20d drops 4/6 losers (67%)
- **Final: n=30  W=28/L=2  WR=93.3%**
- **Dir: LONG**  •  HTF60 strongly against; just touched lower band  •  AVOID when HTF20 mildly against

### W12.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP1`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude H20=H20d drops 4/6 losers (67%)
- **Final: n=30  W=28/L=2  WR=93.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band  •  AVOID when HTF20 mildly against

### W13.  `H60=H60e AND T1=T1c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude H20=H20d drops 4/6 losers (67%)
- **Final: n=30  W=28/L=2  WR=93.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 mildly against

### W14.  `H60=H60e AND T1=T1c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude H20=H20d drops 4/6 losers (67%)
- **Final: n=30  W=28/L=2  WR=93.3%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched lower band  •  AVOID when HTF20 mildly against

### W15.  `H60=H60e AND T4=T4c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude H20=H20d drops 4/6 losers (67%)
- **Final: n=30  W=28/L=2  WR=93.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 mildly against

### W16.  `H60=H60e AND T4=T4c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude H20=H20d drops 4/6 losers (67%)
- **Final: n=30  W=28/L=2  WR=93.3%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; just touched lower band  •  AVOID when HTF20 mildly against

### W17.  `H60=H60e AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude H20=H20d drops 4/6 losers (67%)
- **Final: n=30  W=28/L=2  WR=93.3%**
- **Dir: LONG**  •  HTF60 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 mildly against

### W18.  `H20=H20e AND T1=T1c AND BBP=BBP0`
- Raw: n=46  W=42/L=4  WR=91.3%
- Refine: exclude session_bucket=ny_close drops 2/4 losers (50%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_close

### W19.  `H20=H20e AND T4=T4c AND BBP=BBP0`
- Raw: n=46  W=42/L=4  WR=91.3%
- Refine: exclude session_bucket=ny_close drops 2/4 losers (50%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_close

### W20.  `H20=H20e AND BBP=BBP0 AND direction_exec=long`
- Raw: n=46  W=42/L=4  WR=91.3%
- Refine: exclude session_bucket=ny_close drops 2/4 losers (50%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: LONG**  •  HTF20 strongly against; deep below lower band  •  AVOID when session=ny_close

### W21.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=46  W=42/L=4  WR=91.3%
- Refine: exclude session_bucket=ny_close drops 2/4 losers (50%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_close

### W22.  `H20=H20e AND T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=46  W=42/L=4  WR=91.3%
- Refine: exclude session_bucket=ny_close drops 2/4 losers (50%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_close

### W23.  `H20=H20e AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=46  W=42/L=4  WR=91.3%
- Refine: exclude session_bucket=ny_close drops 2/4 losers (50%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_close

### W24.  `H60=H60a AND T1=T1a AND T4=T4a AND ZS=ZS3`
- Raw: n=45  W=40/L=5  WR=88.9%
- Refine: exclude strategy_id=TF2_pullback_EMA20_short drops 2/5 losers (40%)
- **Final: n=35  W=32/L=3  WR=91.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when strategy=TF2_pullback_EMA20_short

### W25.  `H60=H60a AND T4=T4a AND ZS=ZS3 AND direction_exec=short`
- Raw: n=45  W=40/L=5  WR=88.9%
- Refine: exclude strategy_id=TF2_pullback_EMA20_short drops 2/5 losers (40%)
- **Final: n=35  W=32/L=3  WR=91.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when strategy=TF2_pullback_EMA20_short

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1a AND direction_exec=short`
- Raw: n=51  W=18/L=33  WR=35.3%
- Sharpen: sharpest is session_bucket=ny_mid (20/33 of losers there)
- **Sharp: n=21  W=1/L=20  WR=4.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade  •  ONLY when session=ny_mid

### L02.  `T4=T4a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=48  W=17/L=31  WR=35.4%
- Sharpen: sharpest is H60=H60a (20/31 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L03.  `H60=H60a AND T1=T1a AND ZS=ZS1`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is BBP=BBP1 (20/30 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L04.  `H60=H60a AND T4=T4a AND ZS=ZS1`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is BBP=BBP1 (20/30 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L05.  `H60=H60a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is BBP=BBP1 (20/30 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L06.  `H60=H60a AND T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is BBP=BBP1 (20/30 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L07.  `H60=H60a AND T1=T1a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is BBP=BBP1 (20/30 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L08.  `H60=H60a AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is BBP=BBP1 (20/30 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L09.  `T1=T1a AND T4=T4a AND BBP=BBP1`
- Raw: n=47  W=17/L=30  WR=36.2%
- Sharpen: sharpest is H60=H60a (20/30 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band  •  ONLY when HTF60 aligned WITH trade

### L10.  `T1=T1a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=47  W=17/L=30  WR=36.2%
- Sharpen: sharpest is H60=H60a (20/30 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  1h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L11.  `T1=T1a AND BBP=BBP1 AND direction_exec=short`
- Raw: n=47  W=17/L=30  WR=36.2%
- Sharpen: sharpest is H60=H60a (20/30 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  1h trend WITH trade; just touched lower band  •  ONLY when HTF60 aligned WITH trade

### L12.  `T4=T4a AND BBP=BBP1 AND direction_exec=short`
- Raw: n=47  W=17/L=30  WR=36.2%
- Sharpen: sharpest is H60=H60a (20/30 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  4h trend WITH trade; just touched lower band  •  ONLY when HTF60 aligned WITH trade

### L13.  `BBP=BBP1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=47  W=17/L=30  WR=36.2%
- Sharpen: sharpest is H60=H60a (20/30 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L14.  `T1=T1a AND T4=T4a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=47  W=17/L=30  WR=36.2%
- Sharpen: sharpest is H60=H60a (20/30 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L15.  `T1=T1a AND T4=T4a AND BBP=BBP1 AND direction_exec=short`
- Raw: n=47  W=17/L=30  WR=36.2%
- Sharpen: sharpest is H60=H60a (20/30 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band  •  ONLY when HTF60 aligned WITH trade

### L16.  `T1=T1a AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=47  W=17/L=30  WR=36.2%
- Sharpen: sharpest is H60=H60a (20/30 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  1h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L17.  `T4=T4a AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=47  W=17/L=30  WR=36.2%
- Sharpen: sharpest is H60=H60a (20/30 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L18.  `H20=H20d AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is RSI=RSI2 (14/27 of losers there)
- **Sharp: n=19  W=5/L=14  WR=26.3%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 30-40 weak

### L19.  `H20=H20d AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is RSI=RSI2 (14/27 of losers there)
- **Sharp: n=19  W=5/L=14  WR=26.3%**
- **Dir: LONG**  •  HTF20 mildly against; session=ny_mid  •  ONLY when RSI 30-40 weak

### L20.  `H20=H20d AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is RSI=RSI2 (14/27 of losers there)
- **Sharp: n=19  W=5/L=14  WR=26.3%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 30-40 weak

### L21.  `H20=H20a AND T1=T1a AND session_bucket=london_open`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is ZS=ZS1 (12/24 of losers there)
- **Sharp: n=16  W=4/L=12  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L22.  `H20=H20a AND T4=T4a AND session_bucket=london_open`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is ZS=ZS1 (12/24 of losers there)
- **Sharp: n=16  W=4/L=12  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L23.  `H20=H20a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is ZS=ZS1 (12/24 of losers there)
- **Sharp: n=16  W=4/L=12  WR=25.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L24.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is ZS=ZS1 (12/24 of losers there)
- **Sharp: n=16  W=4/L=12  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L25.  `H20=H20a AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is ZS=ZS1 (12/24 of losers there)
- **Sharp: n=16  W=4/L=12  WR=25.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(18/11), H20a(32/25) | H20d(13/24) |
| H60 | H60d(9/4) | H60a(31/37) |
| T1 | — | — |
| T4 | T4c(58/50) | T4a(42/50) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
