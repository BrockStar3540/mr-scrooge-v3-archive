# EUR_CHF — R27 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,444**  (W=944 / L=500)  -  WR: **65.4%**

## Session distribution

- ny_close: n=478  W=311/L=167  WR=65.1%
- asia: n=417  W=274/L=143  WR=65.7%
- london_open: n=137  W=92/L=45  WR=67.2%
- london: n=135  W=86/L=49  WR=63.7%
- ny_open: n=103  W=70/L=33  WR=68.0%
- off_hours: n=91  W=62/L=29  WR=68.1%
- ny_mid: n=61  W=36/L=25  WR=59.0%
- asia_late: n=22  W=13/L=9  WR=59.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1c AND direction_exec=short`
- Raw: n=205  W=180/L=25  WR=87.8%
- Refine: exclude session_bucket=ny_mid drops 9/25 losers (36%)
- **Final: n=182  W=166/L=16  WR=91.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=ny_mid

### W02.  `H20=H20a AND H60=H60a AND T1=T1c`
- Raw: n=187  W=170/L=17  WR=90.9%
- Refine: exclude session_bucket=ny_mid drops 9/17 losers (53%)
- **Final: n=164  W=156/L=8  WR=95.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=ny_mid

### W03.  `H20=H20a AND H60=H60a AND direction_exec=short`
- Raw: n=187  W=170/L=17  WR=90.9%
- Refine: exclude session_bucket=ny_mid drops 9/17 losers (53%)
- **Final: n=164  W=156/L=8  WR=95.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade  •  AVOID when session=ny_mid

### W04.  `H20=H20a AND H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=187  W=170/L=17  WR=90.9%
- Refine: exclude session_bucket=ny_mid drops 9/17 losers (53%)
- **Final: n=164  W=156/L=8  WR=95.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=ny_mid

### W05.  `H20=H20a AND T1=T1c AND RSI=RSI5`
- Raw: n=184  W=160/L=24  WR=87.0%
- Refine: exclude session_bucket=ny_mid drops 9/24 losers (38%)
- **Final: n=165  W=150/L=15  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W06.  `H20=H20a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=184  W=160/L=24  WR=87.0%
- Refine: exclude session_bucket=ny_mid drops 9/24 losers (38%)
- **Final: n=165  W=150/L=15  WR=90.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W07.  `H20=H20a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=184  W=160/L=24  WR=87.0%
- Refine: exclude session_bucket=ny_mid drops 9/24 losers (38%)
- **Final: n=165  W=150/L=15  WR=90.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W08.  `H20=H20a AND H60=H60a AND RSI=RSI5`
- Raw: n=168  W=150/L=18  WR=89.3%
- Refine: exclude session_bucket=ny_mid drops 9/18 losers (50%)
- **Final: n=149  W=140/L=9  WR=94.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W09.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI5`
- Raw: n=166  W=150/L=16  WR=90.4%
- Refine: exclude session_bucket=ny_mid drops 9/16 losers (56%)
- **Final: n=147  W=140/L=7  WR=95.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W10.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=166  W=150/L=16  WR=90.4%
- Refine: exclude session_bucket=ny_mid drops 9/16 losers (56%)
- **Final: n=147  W=140/L=7  WR=95.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W11.  `H20=H20a AND T1=T1c AND T4=T4c`
- Raw: n=143  W=124/L=19  WR=86.7%
- Refine: exclude session_bucket=ny_mid drops 9/19 losers (47%)
- **Final: n=120  W=110/L=10  WR=91.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_mid

### W12.  `H20=H20a AND T4=T4c AND direction_exec=short`
- Raw: n=143  W=124/L=19  WR=86.7%
- Refine: exclude session_bucket=ny_mid drops 9/19 losers (47%)
- **Final: n=120  W=110/L=10  WR=91.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_mid

### W13.  `H20=H20a AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=143  W=124/L=19  WR=86.7%
- Refine: exclude session_bucket=ny_mid drops 9/19 losers (47%)
- **Final: n=120  W=110/L=10  WR=91.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_mid

### W14.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=139  W=120/L=19  WR=86.3%
- Refine: exclude session_bucket=ny_mid drops 9/19 losers (47%)
- **Final: n=120  W=110/L=10  WR=91.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W15.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=139  W=120/L=19  WR=86.3%
- Refine: exclude session_bucket=ny_mid drops 9/19 losers (47%)
- **Final: n=120  W=110/L=10  WR=91.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W16.  `T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=133  W=114/L=19  WR=85.7%
- Refine: exclude H20=H20d drops 10/19 losers (53%)
- **Final: n=110  W=101/L=9  WR=91.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 mildly against

### W17.  `H20=H20a AND H60=H60a AND T4=T4c`
- Raw: n=125  W=114/L=11  WR=91.2%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=102  W=100/L=2  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_mid

### W18.  `H20=H20a AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=125  W=114/L=11  WR=91.2%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=102  W=100/L=2  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_mid

### W19.  `H20=H20a AND H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=125  W=114/L=11  WR=91.2%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=102  W=100/L=2  WR=98.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_mid

### W20.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=121  W=110/L=11  WR=90.9%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=102  W=100/L=2  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W21.  `T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude H20=H20d drops 10/17 losers (59%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 mildly against

### W22.  `T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude H20=H20d drops 10/17 losers (59%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 mildly against

### W23.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude H20=H20d drops 10/17 losers (59%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 mildly against

### W24.  `H60=H60a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 4/17 losers (24%)
- **Final: n=109  W=96/L=13  WR=88.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when strategy=charlie_pullback_continuation_v2

### W25.  `H60=H60a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=109  W=94/L=15  WR=86.2%
- Refine: exclude session_bucket=off_hours drops 4/15 losers (27%)
- **Final: n=105  W=94/L=11  WR=89.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=off_hours

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1a AND direction_exec=long`
- Raw: n=139  W=42/L=97  WR=30.2%
- Sharpen: sharpest is ZS=ZS4 (39/97 of losers there)
- **Sharp: n=48  W=9/L=39  WR=18.8%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade  •  ONLY when zscore +1 to +2 overbought

### L02.  `H20=H20e AND T1=T1a AND RSI=RSI5`
- Raw: n=127  W=42/L=85  WR=33.1%
- Sharpen: sharpest is ZS=ZS4 (37/85 of losers there)
- **Sharp: n=46  W=9/L=37  WR=19.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +1 to +2 overbought

### L03.  `H20=H20e AND RSI=RSI5 AND direction_exec=long`
- Raw: n=127  W=42/L=85  WR=33.1%
- Sharpen: sharpest is ZS=ZS4 (37/85 of losers there)
- **Sharp: n=46  W=9/L=37  WR=19.6%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 60-70 strong  •  ONLY when zscore +1 to +2 overbought

### L04.  `H20=H20e AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=127  W=42/L=85  WR=33.1%
- Sharpen: sharpest is ZS=ZS4 (37/85 of losers there)
- **Sharp: n=46  W=9/L=37  WR=19.6%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +1 to +2 overbought

### L05.  `H20=H20e AND H60=H60e AND T1=T1a`
- Raw: n=121  W=33/L=88  WR=27.3%
- Sharpen: sharpest is ZS=ZS4 (39/88 of losers there)
- **Sharp: n=48  W=9/L=39  WR=18.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade  •  ONLY when zscore +1 to +2 overbought

### L06.  `H20=H20e AND H60=H60e AND direction_exec=long`
- Raw: n=121  W=33/L=88  WR=27.3%
- Sharpen: sharpest is ZS=ZS4 (39/88 of losers there)
- **Sharp: n=48  W=9/L=39  WR=18.8%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against  •  ONLY when zscore +1 to +2 overbought

### L07.  `H20=H20e AND H60=H60e AND T1=T1a AND direction_exec=long`
- Raw: n=121  W=33/L=88  WR=27.3%
- Sharpen: sharpest is ZS=ZS4 (39/88 of losers there)
- **Sharp: n=48  W=9/L=39  WR=18.8%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade  •  ONLY when zscore +1 to +2 overbought

### L08.  `H20=H20e AND H60=H60e AND RSI=RSI5`
- Raw: n=113  W=37/L=76  WR=32.7%
- Sharpen: sharpest is ZS=ZS4 (37/76 of losers there)
- **Sharp: n=48  W=11/L=37  WR=22.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when zscore +1 to +2 overbought

### L09.  `H20=H20e AND H60=H60e AND T1=T1a AND RSI=RSI5`
- Raw: n=109  W=33/L=76  WR=30.3%
- Sharpen: sharpest is ZS=ZS4 (37/76 of losers there)
- **Sharp: n=46  W=9/L=37  WR=19.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +1 to +2 overbought

### L10.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND direction_exec=long`
- Raw: n=109  W=33/L=76  WR=30.3%
- Sharpen: sharpest is ZS=ZS4 (37/76 of losers there)
- **Sharp: n=46  W=9/L=37  WR=19.6%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when zscore +1 to +2 overbought

### L11.  `H20=H20e AND T4=T4a AND RSI=RSI5`
- Raw: n=104  W=39/L=65  WR=37.5%
- Sharpen: sharpest is H60=H60e (56/65 of losers there)
- **Sharp: n=78  W=22/L=56  WR=28.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L12.  `H20=H20e AND T1=T1a AND T4=T4a`
- Raw: n=99  W=31/L=68  WR=31.3%
- Sharpen: sharpest is BBP=BBP5 (19/68 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when just touched upper band

### L13.  `H20=H20e AND T4=T4a AND direction_exec=long`
- Raw: n=99  W=31/L=68  WR=31.3%
- Sharpen: sharpest is BBP=BBP5 (19/68 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade  •  ONLY when just touched upper band

### L14.  `H20=H20e AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=99  W=31/L=68  WR=31.3%
- Sharpen: sharpest is BBP=BBP5 (19/68 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when just touched upper band

### L15.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=96  W=31/L=65  WR=32.3%
- Sharpen: sharpest is BBP=BBP5 (19/65 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when just touched upper band

### L16.  `H20=H20e AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=96  W=31/L=65  WR=32.3%
- Sharpen: sharpest is BBP=BBP5 (19/65 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when just touched upper band

### L17.  `H60=H60e AND T1=T1a AND ZS=ZS5`
- Raw: n=92  W=36/L=56  WR=39.1%
- Sharpen: sharpest is H20=H20e (23/56 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L18.  `H60=H60e AND ZS=ZS5 AND direction_exec=long`
- Raw: n=92  W=36/L=56  WR=39.1%
- Sharpen: sharpest is H20=H20e (23/56 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L19.  `T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=92  W=36/L=56  WR=39.1%
- Sharpen: sharpest is session_bucket=asia (37/56 of losers there)
- **Sharp: n=51  W=14/L=37  WR=27.5%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L20.  `H60=H60e AND T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=92  W=36/L=56  WR=39.1%
- Sharpen: sharpest is H20=H20e (23/56 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L21.  `H60=H60e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=83  W=29/L=54  WR=34.9%
- Sharpen: sharpest is H20=H20c (20/54 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=asia  •  ONLY when HTF20 neutral

### L22.  `H20=H20e AND H60=H60e AND T4=T4a`
- Raw: n=81  W=22/L=59  WR=27.2%
- Sharpen: sharpest is BBP=BBP5 (17/59 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when just touched upper band

### L23.  `H20=H20e AND H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=81  W=22/L=59  WR=27.2%
- Sharpen: sharpest is BBP=BBP5 (17/59 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when just touched upper band

### L24.  `H20=H20e AND H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=81  W=22/L=59  WR=27.2%
- Sharpen: sharpest is BBP=BBP5 (17/59 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when just touched upper band

### L25.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=78  W=22/L=56  WR=28.2%
- Sharpen: sharpest is BBP=BBP5 (17/56 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when just touched upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(36/24) | H20e(28/39) |
| H60 | H60a(54/25) | H60e(23/51) |
| T1 | T1c(65/42) | T1a(35/58) |
| T4 | T4c(58/49) | T4a(42/51) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(65/42) | long(35/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
