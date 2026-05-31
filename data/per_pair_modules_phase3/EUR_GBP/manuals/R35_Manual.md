# EUR_GBP — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **895**  (W=564 / L=331)  -  WR: **63.0%**

## Session distribution

- ny_mid: n=370  W=238/L=132  WR=64.3%
- ny_close: n=217  W=135/L=82  WR=62.2%
- ny_open: n=159  W=100/L=59  WR=62.9%
- london: n=92  W=59/L=33  WR=64.1%
- london_open: n=47  W=24/L=23  WR=51.1%
- off_hours: n=10  W=8/L=2  WR=80.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=137  W=119/L=18  WR=86.9%
- Refine: no further refinement
- **Final: n=137  W=119/L=18  WR=86.9%**
- **Dir: ?**  •  4h trend WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold

### W02.  `T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=133  W=114/L=19  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 10/19 losers (53%)
- **Final: n=101  W=92/L=9  WR=91.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W03.  `T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=133  W=114/L=19  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 10/19 losers (53%)
- **Final: n=101  W=92/L=9  WR=91.1%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W04.  `T1=T1a AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=133  W=114/L=19  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 10/19 losers (53%)
- **Final: n=101  W=92/L=9  WR=91.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W05.  `H20=H20a AND T4=T4a AND ZS=ZS1`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude session_bucket=ny_close drops 10/18 losers (56%)
- **Final: n=100  W=92/L=8  WR=92.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W06.  `H20=H20a AND T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude session_bucket=ny_close drops 10/18 losers (56%)
- **Final: n=100  W=92/L=8  WR=92.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W07.  `H20=H20a AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude session_bucket=ny_close drops 10/18 losers (56%)
- **Final: n=100  W=92/L=8  WR=92.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W08.  `T4=T4a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude H60=H60d drops 4/15 losers (27%)
- **Final: n=100  W=89/L=11  WR=89.0%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF60 mildly against

### W09.  `T1=T1a AND T4=T4a AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude BBP=BBP1 drops 9/12 losers (75%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W10.  `T4=T4a AND RSI=RSI1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude BBP=BBP1 drops 9/12 losers (75%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W11.  `H60=H60b AND T4=T4a AND RSI=RSI1`
- Raw: n=96  W=88/L=8  WR=91.7%
- Refine: exclude session_bucket=ny_open drops 4/8 losers (50%)
- **Final: n=88  W=84/L=4  WR=95.5%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_open

### W12.  `T4=T4a AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=91  W=80/L=11  WR=87.9%
- Refine: exclude H60=H60d drops 4/11 losers (36%)
- **Final: n=87  W=80/L=7  WR=92.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when HTF60 mildly against

### W13.  `H20=H20a AND T4=T4a AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude BBP=BBP1 drops 8/11 losers (73%)
- **Final: n=44  W=41/L=3  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W14.  `H60=H60b AND T1=T1a AND T4=T4a`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude session_bucket=ny_open drops 4/10 losers (40%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W15.  `H60=H60b AND T4=T4a AND direction_exec=short`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude session_bucket=ny_open drops 4/10 losers (40%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 4h trend WITH trade  •  AVOID when session=ny_open

### W16.  `H60=H60b AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude session_bucket=ny_open drops 4/10 losers (40%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W17.  `H20=H20a AND H60=H60b AND T1=T1a`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude session_bucket=ny_open drops 4/6 losers (67%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 1h trend WITH trade  •  AVOID when session=ny_open

### W18.  `H20=H20a AND H60=H60b AND T4=T4a`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude session_bucket=ny_open drops 4/6 losers (67%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 4h trend WITH trade  •  AVOID when session=ny_open

### W19.  `H20=H20a AND H60=H60b AND direction_exec=short`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude session_bucket=ny_open drops 4/6 losers (67%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 slightly aligned  •  AVOID when session=ny_open

### W20.  `H20=H20a AND H60=H60b AND T1=T1a AND T4=T4a`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude session_bucket=ny_open drops 4/6 losers (67%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W21.  `H20=H20a AND H60=H60b AND T1=T1a AND direction_exec=short`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude session_bucket=ny_open drops 4/6 losers (67%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 1h trend WITH trade  •  AVOID when session=ny_open

### W22.  `H20=H20a AND H60=H60b AND T4=T4a AND direction_exec=short`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude session_bucket=ny_open drops 4/6 losers (67%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 4h trend WITH trade  •  AVOID when session=ny_open

### W23.  `H60=H60b AND T1=T1a AND RSI=RSI1`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude H20=H20e drops 6/11 losers (55%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; RSI 20-30 oversold  •  AVOID when HTF20 strongly against

### W24.  `H60=H60b AND RSI=RSI1 AND direction_exec=short`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude H20=H20e drops 6/11 losers (55%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: SHORT**  •  HTF60 slightly aligned; RSI 20-30 oversold  •  AVOID when HTF20 strongly against

### W25.  `H60=H60b AND T1=T1a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude H20=H20e drops 6/11 losers (55%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 1h trend WITH trade; RSI 20-30 oversold  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60d AND T1=T1c AND direction_exec=long`
- Raw: n=99  W=37/L=62  WR=37.4%
- Sharpen: sharpest is H20=H20e (39/62 of losers there)
- **Sharp: n=51  W=12/L=39  WR=23.5%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when HTF20 strongly against

### L02.  `H20=H20e AND T4=T4c AND ZS=ZS1`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is RSI=RSI0 (13/59 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI<20 extreme oversold

### L03.  `H60=H60d AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=95  W=30/L=65  WR=31.6%
- Sharpen: sharpest is session_bucket=ny_mid (19/65 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: ?**  •  HTF60 mildly against; lower third; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

### L04.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=95  W=38/L=57  WR=40.0%
- Sharpen: sharpest is RSI=RSI0 (13/57 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI<20 extreme oversold

### L05.  `H20=H20e AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=95  W=38/L=57  WR=40.0%
- Sharpen: sharpest is RSI=RSI0 (13/57 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI<20 extreme oversold

### L06.  `H60=H60d AND T1=T1c AND BBP=BBP2`
- Raw: n=78  W=26/L=52  WR=33.3%
- Sharpen: sharpest is H20=H20e (32/52 of losers there)
- **Sharp: n=42  W=10/L=32  WR=23.8%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; lower third  •  ONLY when HTF20 strongly against

### L07.  `H60=H60d AND BBP=BBP2 AND direction_exec=long`
- Raw: n=78  W=26/L=52  WR=33.3%
- Sharpen: sharpest is H20=H20e (32/52 of losers there)
- **Sharp: n=42  W=10/L=32  WR=23.8%**
- **Dir: LONG**  •  HTF60 mildly against; lower third  •  ONLY when HTF20 strongly against

### L08.  `H60=H60d AND T1=T1c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=78  W=26/L=52  WR=33.3%
- Sharpen: sharpest is H20=H20e (32/52 of losers there)
- **Sharp: n=42  W=10/L=32  WR=23.8%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade; lower third  •  ONLY when HTF20 strongly against

### L09.  `H60=H60d AND T1=T1c AND ZS=ZS2`
- Raw: n=75  W=25/L=50  WR=33.3%
- Sharpen: sharpest is H20=H20e (30/50 of losers there)
- **Sharp: n=39  W=9/L=30  WR=23.1%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L10.  `H60=H60d AND ZS=ZS2 AND direction_exec=long`
- Raw: n=75  W=25/L=50  WR=33.3%
- Sharpen: sharpest is H20=H20e (30/50 of losers there)
- **Sharp: n=39  W=9/L=30  WR=23.1%**
- **Dir: LONG**  •  HTF60 mildly against; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L11.  `H60=H60d AND T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=75  W=25/L=50  WR=33.3%
- Sharpen: sharpest is H20=H20e (30/50 of losers there)
- **Sharp: n=39  W=9/L=30  WR=23.1%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L12.  `H60=H60d AND T1=T1c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=75  W=25/L=50  WR=33.3%
- Sharpen: sharpest is H20=H20e (30/50 of losers there)
- **Sharp: n=39  W=9/L=30  WR=23.1%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L13.  `H60=H60d AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=75  W=25/L=50  WR=33.3%
- Sharpen: sharpest is H20=H20e (30/50 of losers there)
- **Sharp: n=39  W=9/L=30  WR=23.1%**
- **Dir: LONG**  •  HTF60 mildly against; lower third; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L14.  `T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is T4=T4c (38/44 of losers there)
- **Sharp: n=52  W=14/L=38  WR=26.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band  •  ONLY when 4h trend AGAINST trade

### L15.  `T4=T4c AND BBP=BBP0 AND RSI=RSI1`
- Raw: n=69  W=23/L=46  WR=33.3%
- Sharpen: sharpest is H60=H60b (12/46 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 20-30 oversold  •  ONLY when HTF60 slightly aligned

### L16.  `T1=T1c AND BBP=BBP0 AND RSI=RSI1`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is T4=T4c (35/41 of losers there)
- **Sharp: n=49  W=14/L=35  WR=28.6%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; RSI 20-30 oversold  •  ONLY when 4h trend AGAINST trade

### L17.  `BBP=BBP0 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is T4=T4c (35/41 of losers there)
- **Sharp: n=49  W=14/L=35  WR=28.6%**
- **Dir: LONG**  •  deep below lower band; RSI 20-30 oversold  •  ONLY when 4h trend AGAINST trade

### L18.  `T1=T1c AND BBP=BBP0 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is T4=T4c (35/41 of losers there)
- **Sharp: n=49  W=14/L=35  WR=28.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; RSI 20-30 oversold  •  ONLY when 4h trend AGAINST trade

### L19.  `H60=H60d AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=65  W=21/L=44  WR=32.3%
- Sharpen: sharpest is session_bucket=ny_mid (16/44 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF60 mildly against; lower third; RSI 20-30 oversold  •  ONLY when session=ny_mid

### L20.  `T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=65  W=26/L=39  WR=40.0%
- Sharpen: sharpest is H60=H60b (22/39 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when HTF60 slightly aligned

### L21.  `T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=64  W=23/L=41  WR=35.9%
- Sharpen: sharpest is session_bucket=london_open (11/41 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L22.  `H60=H60d AND T4=T4c AND RSI=RSI1`
- Raw: n=61  W=15/L=46  WR=24.6%
- Sharpen: sharpest is session_bucket=london (22/46 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=london

### L23.  `T4=T4c AND BBP=BBP0 AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=61  W=23/L=38  WR=37.7%
- Sharpen: sharpest is session_bucket=london_open (11/38 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L24.  `H60=H60d AND T1=T1c AND T4=T4c`
- Raw: n=60  W=19/L=41  WR=31.7%
- Sharpen: sharpest is H20=H20e (39/41 of losers there)
- **Sharp: n=51  W=12/L=39  WR=23.5%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when HTF20 strongly against

### L25.  `H60=H60d AND T4=T4c AND direction_exec=long`
- Raw: n=60  W=19/L=41  WR=31.7%
- Sharpen: sharpest is H20=H20e (39/41 of losers there)
- **Sharp: n=51  W=12/L=39  WR=23.5%**
- **Dir: LONG**  •  HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(51/31) | H20e(33/53) |
| H60 | H60b(28/14) | H60d(12/27) |
| T1 | T1a(60/38) | T1c(40/62) |
| T4 | T4a(63/38) | T4c(37/62) |
| BBP | BBP1(22/17) | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(60/38) | long(40/62) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
