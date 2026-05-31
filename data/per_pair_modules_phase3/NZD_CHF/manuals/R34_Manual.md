# NZD_CHF — R34 Manual

## Regime centroid (locked factors)

- **BB = BB0**  (very narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **960**  (W=586 / L=374)  -  WR: **61.0%**

## Session distribution

- asia: n=301  W=192/L=109  WR=63.8%
- ny_close: n=230  W=134/L=96  WR=58.3%
- london: n=97  W=62/L=35  WR=63.9%
- london_open: n=82  W=42/L=40  WR=51.2%
- ny_open: n=73  W=43/L=30  WR=58.9%
- off_hours: n=65  W=38/L=27  WR=58.5%
- asia_late: n=64  W=43/L=21  WR=67.2%
- ny_mid: n=48  W=32/L=16  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60c AND T4=T4c AND direction_exec=long`
- Raw: n=53  W=50/L=3  WR=94.3%
- Refine: exclude H20=H20e drops 2/3 losers (67%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend AGAINST trade  •  AVOID when HTF20 strongly against

### W02.  `H60=H60c AND T4=T4c AND RSI=RSI4`
- Raw: n=51  W=50/L=1  WR=98.0%
- Refine: no further refinement
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; RSI 50-60 upper neutral

### W03.  `H20=H20b AND T1=T1c AND T4=T4c`
- Raw: n=45  W=42/L=3  WR=93.3%
- Refine: exclude session_bucket=asia drops 2/3 losers (67%)
- **Final: n=25  W=24/L=1  WR=96.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=asia

### W04.  `H20=H20b AND T4=T4c AND direction_exec=short`
- Raw: n=44  W=42/L=2  WR=95.5%
- Refine: exclude T1=T1c drops 2/2 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend AGAINST trade  •  AVOID when 1h trend AGAINST trade

### W05.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=44  W=39/L=5  WR=88.6%
- Refine: exclude session_bucket=london_open drops 2/5 losers (40%)
- **Final: n=42  W=39/L=3  WR=92.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W06.  `T1=T1c AND ZS=ZS3 AND direction_exec=short`
- Raw: n=42  W=36/L=6  WR=85.7%
- Refine: exclude T4=T4a drops 4/6 losers (67%)
- **Final: n=27  W=25/L=2  WR=92.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when 4h trend WITH trade

### W07.  `H60=H60c AND T1=T1a AND RSI=RSI4`
- Raw: n=40  W=34/L=6  WR=85.0%
- Refine: exclude T4=T4a drops 6/6 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 neutral; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when 4h trend WITH trade

### W08.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=38  W=33/L=5  WR=86.8%
- Refine: exclude H60=H60d drops 3/5 losers (60%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 mildly against

### W09.  `T1=T1c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=37  W=32/L=5  WR=86.5%
- Refine: exclude direction_exec=short drops 3/5 losers (60%)
- **Final: n=29  W=27/L=2  WR=93.1%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; session=asia  •  AVOID when short

### W10.  `BBP=BBP2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=37  W=32/L=5  WR=86.5%
- Refine: exclude H60=H60e drops 4/5 losers (80%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: LONG**  •  lower third; session=asia  •  AVOID when HTF60 strongly against

### W11.  `H60=H60c AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=36  W=35/L=1  WR=97.2%
- Refine: no further refinement
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend WITH trade; 4h trend AGAINST trade

### W12.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=36  W=34/L=2  WR=94.4%
- Refine: exclude session_bucket=asia_late drops 2/2 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=asia_late

### W13.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=36  W=34/L=2  WR=94.4%
- Refine: exclude session_bucket=asia_late drops 2/2 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong  •  AVOID when session=asia_late

### W14.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=36  W=34/L=2  WR=94.4%
- Refine: exclude session_bucket=asia_late drops 2/2 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=asia_late

### W15.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=36  W=32/L=4  WR=88.9%
- Refine: exclude RSI=RSI4 drops 4/4 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when RSI 50-60 upper neutral

### W16.  `H20=H20e AND BBP=BBP2 AND direction_exec=long`
- Raw: n=36  W=31/L=5  WR=86.1%
- Refine: exclude session_bucket=ny_close drops 3/5 losers (60%)
- **Final: n=28  W=26/L=2  WR=92.9%**
- **Dir: LONG**  •  HTF20 strongly against; lower third  •  AVOID when session=ny_close

### W17.  `H20=H20a AND H60=H60c AND T4=T4c`
- Raw: n=35  W=30/L=5  WR=85.7%
- Refine: exclude session_bucket=asia drops 4/5 losers (80%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; 4h trend AGAINST trade  •  AVOID when session=asia

### W18.  `T1=T1c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=35  W=30/L=5  WR=85.7%
- Refine: exclude direction_exec=short drops 3/5 losers (60%)
- **Final: n=27  W=25/L=2  WR=92.6%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  AVOID when short

### W19.  `ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=35  W=30/L=5  WR=85.7%
- Refine: exclude H60=H60e drops 4/5 losers (80%)
- **Final: n=25  W=24/L=1  WR=96.0%**
- **Dir: LONG**  •  zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 strongly against

### W20.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=35  W=30/L=5  WR=85.7%
- Refine: exclude direction_exec=short drops 3/5 losers (60%)
- **Final: n=27  W=25/L=2  WR=92.6%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=asia  •  AVOID when short

### W21.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=35  W=30/L=5  WR=85.7%
- Refine: exclude H60=H60e drops 4/5 losers (80%)
- **Final: n=25  W=24/L=1  WR=96.0%**
- **Dir: LONG**  •  lower third; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 strongly against

### W22.  `H60=H60a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=34  W=30/L=4  WR=88.2%
- Refine: exclude H20=H20a drops 2/4 losers (50%)
- **Final: n=25  W=23/L=2  WR=92.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W23.  `H20=H20e AND ZS=ZS2 AND direction_exec=long`
- Raw: n=34  W=29/L=5  WR=85.3%
- Refine: exclude session_bucket=ny_close drops 3/5 losers (60%)
- **Final: n=26  W=24/L=2  WR=92.3%**
- **Dir: LONG**  •  HTF20 strongly against; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W24.  `H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=34  W=29/L=5  WR=85.3%
- Refine: exclude direction_exec=short drops 5/5 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when short

### W25.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=34  W=29/L=5  WR=85.3%
- Refine: exclude T1=T1c drops 5/5 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third  •  AVOID when 1h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T1=T1a AND direction_exec=short`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is RSI=RSI2 (13/44 of losers there)
- **Sharp: n=16  W=3/L=13  WR=18.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  ONLY when RSI 30-40 weak

### L02.  `T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is H20=H20a (20/40 of losers there)
- **Sharp: n=25  W=5/L=20  WR=20.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_close  •  ONLY when HTF20 aligned WITH trade

### L03.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=53  W=19/L=34  WR=35.8%
- Sharpen: sharpest is H60=H60e (12/34 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF60 strongly against

### L04.  `H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is T1=T1a (22/29 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade  •  ONLY when 1h trend WITH trade

### L05.  `H60=H60e AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=45  W=16/L=29  WR=35.6%
- Sharpen: sharpest is BBP=BBP4 (10/29 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_close  •  ONLY when upper third

### L06.  `H60=H60e AND T1=T1a AND direction_exec=short`
- Raw: n=45  W=17/L=28  WR=37.8%
- Sharpen: sharpest is T4=T4a (22/28 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade  •  ONLY when 4h trend WITH trade

### L07.  `H20=H20a AND H60=H60a AND T1=T1a`
- Raw: n=44  W=13/L=31  WR=29.5%
- Sharpen: sharpest is session_bucket=london (5/31 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when session=london

### L08.  `H20=H20a AND T4=T4a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=42  W=16/L=26  WR=38.1%
- Sharpen: sharpest is session_bucket=ny_close (8/26 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; upper third  •  ONLY when session=ny_close

### L09.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=41  W=13/L=28  WR=31.7%
- Sharpen: sharpest is H60=H60c (9/28 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when HTF60 neutral

### L10.  `H20=H20a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=39  W=10/L=29  WR=25.6%
- Sharpen: sharpest is ZS=ZS4 (9/29 of losers there)
- **Sharp: n=10  W=1/L=9  WR=10.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_close  •  ONLY when zscore +1 to +2 overbought

### L11.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=39  W=13/L=26  WR=33.3%
- Sharpen: sharpest is H60=H60e (9/26 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; lower third  •  ONLY when HTF60 strongly against

### L12.  `T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=39  W=15/L=24  WR=38.5%
- Sharpen: sharpest is H60=H60c (7/24 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 neutral

### L13.  `T1=T1a AND T4=T4a AND ZS=ZS3`
- Raw: n=38  W=11/L=27  WR=28.9%
- Sharpen: sharpest is H60=H60e (11/27 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when HTF60 strongly against

### L14.  `H20=H20a AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=37  W=11/L=26  WR=29.7%
- Sharpen: sharpest is direction_exec=long (7/26 of losers there)
- **Sharp: n=8  W=1/L=7  WR=12.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when long

### L15.  `H60=H60a AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=37  W=14/L=23  WR=37.8%
- Sharpen: sharpest is H20=H20a (7/23 of losers there)
- **Sharp: n=8  W=1/L=7  WR=12.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF20 aligned WITH trade

### L16.  `H20=H20d AND T1=T1a AND T4=T4a`
- Raw: n=36  W=9/L=27  WR=25.0%
- Sharpen: sharpest is RSI=RSI4 (10/27 of losers there)
- **Sharp: n=11  W=1/L=10  WR=9.1%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L17.  `H20=H20a AND T1=T1a AND BBP=BBP2`
- Raw: n=36  W=13/L=23  WR=36.1%
- Sharpen: sharpest is direction_exec=short (16/23 of losers there)
- **Sharp: n=21  W=5/L=16  WR=23.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third  •  ONLY when short

### L18.  `T1=T1a AND T4=T4a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=36  W=13/L=23  WR=36.1%
- Sharpen: sharpest is H20=H20a (14/23 of losers there)
- **Sharp: n=17  W=3/L=14  WR=17.6%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

### L19.  `H60=H60c AND T4=T4a AND direction_exec=short`
- Raw: n=35  W=9/L=26  WR=25.7%
- Sharpen: sharpest is RSI=RSI4 (11/26 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF60 neutral; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L20.  `H20=H20a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=35  W=14/L=21  WR=40.0%
- Sharpen: sharpest is direction_exec=short (16/21 of losers there)
- **Sharp: n=23  W=7/L=16  WR=30.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when short

### L21.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=35  W=14/L=21  WR=40.0%
- Sharpen: sharpest is direction_exec=short (16/21 of losers there)
- **Sharp: n=23  W=7/L=16  WR=30.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when short

### L22.  `H20=H20a AND H60=H60e AND RSI=RSI3`
- Raw: n=34  W=13/L=21  WR=38.2%
- Sharpen: sharpest is direction_exec=short (9/21 of losers there)
- **Sharp: n=11  W=2/L=9  WR=18.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 40-50 lower neutral  •  ONLY when short

### L23.  `H20=H20a AND T1=T1a AND session_bucket=ny_close`
- Raw: n=33  W=8/L=25  WR=24.2%
- Sharpen: sharpest is RSI=RSI6 (5/25 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_close  •  ONLY when RSI 70-80 overbought

### L24.  `T1=T1a AND T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=33  W=11/L=22  WR=33.3%
- Sharpen: sharpest is H60=H60c (7/22 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 neutral

### L25.  `H20=H20a AND T1=T1a AND ZS=ZS2`
- Raw: n=32  W=12/L=20  WR=37.5%
- Sharpen: sharpest is direction_exec=short (15/20 of losers there)
- **Sharp: n=20  W=5/L=15  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when short

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(19/11) | H20a(29/36) |
| H60 | — | — |
| T1 | T1c(53/44) | T1a(47/56) |
| T4 | T4c(57/39) | T4a(43/61) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
