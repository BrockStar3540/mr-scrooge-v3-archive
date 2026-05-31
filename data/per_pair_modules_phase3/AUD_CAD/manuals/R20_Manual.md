# AUD_CAD — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,930**  (W=1,248 / L=682)  -  WR: **64.7%**

## Session distribution

- asia: n=924  W=602/L=322  WR=65.2%
- ny_close: n=314  W=208/L=106  WR=66.2%
- ny_open: n=218  W=135/L=83  WR=61.9%
- london_open: n=180  W=112/L=68  WR=62.2%
- london: n=110  W=66/L=44  WR=60.0%
- asia_late: n=84  W=58/L=26  WR=69.0%
- off_hours: n=61  W=41/L=20  WR=67.2%
- ny_mid: n=39  W=26/L=13  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=126  W=110/L=16  WR=87.3%
- Refine: exclude ZS=ZS6 drops 4/16 losers (25%)
- **Final: n=122  W=110/L=12  WR=90.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore >+3 extreme

### W02.  `H20=H20e AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=111  W=97/L=14  WR=87.4%
- Refine: exclude T1=T1b drops 6/14 losers (43%)
- **Final: n=90  W=82/L=8  WR=91.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when 1h trend flat

### W03.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=111  W=97/L=14  WR=87.4%
- Refine: exclude T1=T1b drops 6/14 losers (43%)
- **Final: n=90  W=82/L=8  WR=91.1%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when 1h trend flat

### W04.  `H20=H20b AND direction_exec=long AND session_bucket=asia`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude ZS=ZS3 drops 7/16 losers (44%)
- **Final: n=90  W=81/L=9  WR=90.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; session=asia  •  AVOID when zscore -1 to +1 neutral

### W05.  `H20=H20b AND T4=T4c AND direction_exec=long`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude RSI=RSI2 drops 5/15 losers (33%)
- **Final: n=89  W=79/L=10  WR=88.8%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend AGAINST trade  •  AVOID when RSI 30-40 weak

### W06.  `H60=H60a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=99  W=88/L=11  WR=88.9%
- Refine: exclude T1=T1b drops 6/11 losers (55%)
- **Final: n=78  W=73/L=5  WR=93.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend flat

### W07.  `RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=99  W=88/L=11  WR=88.9%
- Refine: exclude T1=T1b drops 6/11 losers (55%)
- **Final: n=78  W=73/L=5  WR=93.6%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend flat

### W08.  `H60=H60a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=99  W=88/L=11  WR=88.9%
- Refine: exclude T1=T1b drops 6/11 losers (55%)
- **Final: n=78  W=73/L=5  WR=93.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend flat

### W09.  `H20=H20b AND H60=H60a AND T4=T4c`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude BBP=BBP2 drops 5/14 losers (36%)
- **Final: n=84  W=75/L=9  WR=89.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when lower third

### W10.  `H20=H20b AND H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude BBP=BBP2 drops 5/14 losers (36%)
- **Final: n=84  W=75/L=9  WR=89.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when lower third

### W11.  `H20=H20a AND H60=H60e AND RSI=RSI2`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude session_bucket=asia drops 7/8 losers (88%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 30-40 weak  •  AVOID when session=asia

### W12.  `H20=H20a AND T1=T1a AND RSI=RSI2`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude session_bucket=asia drops 7/8 losers (88%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when session=asia

### W13.  `H20=H20a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude session_bucket=asia drops 7/8 losers (88%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak  •  AVOID when session=asia

### W14.  `H20=H20a AND H60=H60e AND T1=T1a AND RSI=RSI2`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude session_bucket=asia drops 7/8 losers (88%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when session=asia

### W15.  `H20=H20a AND H60=H60e AND RSI=RSI2 AND direction_exec=short`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude session_bucket=asia drops 7/8 losers (88%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 30-40 weak  •  AVOID when session=asia

### W16.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude RSI=RSI2 drops 4/8 losers (50%)
- **Final: n=76  W=72/L=4  WR=94.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 30-40 weak

### W17.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude session_bucket=asia drops 7/8 losers (88%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when session=asia

### W18.  `H20=H20b AND T4=T4c AND session_bucket=asia`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude RSI=RSI2 drops 5/11 losers (45%)
- **Final: n=63  W=57/L=6  WR=90.5%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 30-40 weak

### W19.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP2`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude session_bucket=asia_late drops 3/11 losers (27%)
- **Final: n=77  W=69/L=8  WR=89.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; lower third  •  AVOID when session=asia_late

### W20.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude session_bucket=asia_late drops 3/11 losers (27%)
- **Final: n=77  W=69/L=8  WR=89.6%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third  •  AVOID when session=asia_late

### W21.  `H20=H20b AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude RSI=RSI2 drops 5/11 losers (45%)
- **Final: n=63  W=57/L=6  WR=90.5%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 30-40 weak

### W22.  `H20=H20b AND T1=T1c AND T4=T4c`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude BBP=BBP4 drops 3/12 losers (25%)
- **Final: n=77  W=68/L=9  WR=88.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when upper third

### W23.  `H20=H20b AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude BBP=BBP4 drops 3/12 losers (25%)
- **Final: n=77  W=68/L=9  WR=88.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when upper third

### W24.  `H20=H20b AND H60=H60a AND RSI=RSI3`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude ZS=ZS4 drops 6/10 losers (60%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore +1 to +2 overbought

### W25.  `H20=H20b AND RSI=RSI3 AND direction_exec=long`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude ZS=ZS4 drops 6/10 losers (60%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 40-50 lower neutral  •  AVOID when zscore +1 to +2 overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=79  W=25/L=54  WR=31.6%
- Sharpen: sharpest is T1=T1a (46/54 of losers there)
- **Sharp: n=61  W=15/L=46  WR=24.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; session=asia  •  ONLY when 1h trend WITH trade

### L02.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=79  W=25/L=54  WR=31.6%
- Sharpen: sharpest is T1=T1a (46/54 of losers there)
- **Sharp: n=61  W=15/L=46  WR=24.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  ONLY when 1h trend WITH trade

### L03.  `H60=H60e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=77  W=18/L=59  WR=23.4%
- Sharpen: sharpest is T1=T1a (33/59 of losers there)
- **Sharp: n=37  W=4/L=33  WR=10.8%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L04.  `H20=H20a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is BBP=BBP2 (20/43 of losers there)
- **Sharp: n=27  W=7/L=20  WR=25.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=ny_open  •  ONLY when lower third

### L05.  `H60=H60a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is BBP=BBP2 (22/45 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_open  •  ONLY when lower third

### L06.  `T1=T1c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is BBP=BBP2 (22/45 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when lower third

### L07.  `RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is BBP=BBP2 (22/45 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: LONG**  •  RSI 30-40 weak; session=ny_open  •  ONLY when lower third

### L08.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is BBP=BBP2 (22/45 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when lower third

### L09.  `H60=H60a AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is BBP=BBP2 (22/45 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_open  •  ONLY when lower third

### L10.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is BBP=BBP2 (22/45 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when lower third

### L11.  `H60=H60e AND T4=T4a AND RSI=RSI4`
- Raw: n=68  W=18/L=50  WR=26.5%
- Sharpen: sharpest is T1=T1a (24/50 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L12.  `T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=68  W=18/L=50  WR=26.5%
- Sharpen: sharpest is T1=T1a (24/50 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L13.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=68  W=18/L=50  WR=26.5%
- Sharpen: sharpest is T1=T1a (24/50 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L14.  `H20=H20e AND H60=H60a AND RSI=RSI2`
- Raw: n=67  W=20/L=47  WR=29.9%
- Sharpen: sharpest is T4=T4a (20/47 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L15.  `H20=H20e AND T1=T1c AND RSI=RSI2`
- Raw: n=67  W=20/L=47  WR=29.9%
- Sharpen: sharpest is T4=T4a (20/47 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L16.  `H20=H20e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=67  W=20/L=47  WR=29.9%
- Sharpen: sharpest is T4=T4a (20/47 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L17.  `H20=H20e AND H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=67  W=20/L=47  WR=29.9%
- Sharpen: sharpest is T4=T4a (20/47 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L18.  `H20=H20e AND H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=67  W=20/L=47  WR=29.9%
- Sharpen: sharpest is T4=T4a (20/47 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L19.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=67  W=20/L=47  WR=29.9%
- Sharpen: sharpest is T4=T4a (20/47 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L20.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=67  W=24/L=43  WR=35.8%
- Sharpen: sharpest is BBP=BBP2 (20/43 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_open  •  ONLY when lower third

### L21.  `H20=H20a AND T1=T1c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=67  W=24/L=43  WR=35.8%
- Sharpen: sharpest is BBP=BBP2 (20/43 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when lower third

### L22.  `H20=H20a AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=67  W=24/L=43  WR=35.8%
- Sharpen: sharpest is BBP=BBP2 (20/43 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=ny_open  •  ONLY when lower third

### L23.  `T1=T1a AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is RSI=RSI4 (21/40 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 50-60 upper neutral

### L24.  `H60=H60e AND T1=T1a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=63  W=23/L=40  WR=36.5%
- Sharpen: sharpest is RSI=RSI4 (21/40 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 50-60 upper neutral

### L25.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=61  W=15/L=46  WR=24.6%
- Sharpen: sharpest is BBP=BBP4 (21/46 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when upper third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(14/7) | — |
| H60 | — | — |
| T1 | T1a(52/45) | T1c(46/53) |
| T4 | T4c(53/47) | T4a(47/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
