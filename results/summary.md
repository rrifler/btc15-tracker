# BTC 15-min strategy tracker: FAIL

Data source: INTL_PROXY. INTL_PROXY means trades from the international exchange, used because the US gateway publishes no public trade history.
Real money needs PASS in both the backtest and the live paper run, with the live hit rate within 8 points of the backtest.

## Backtest

- Verdict: **FAIL**
- Windows scored: 700; excluded: 0
- Fill rate: 16.9% of scored windows had a fill (0 too small)
- Fills that reached 45c: 52 of 118 = 44.1% (95% range 35.4% to 53.1%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.35 (balance $7.65 from $20)
- Longest losing streak: 9
- Strict vs touch: strict 52/118 = 44.1%; touch 67/136 = 49.3%. The verdict uses strict.

## Live paper run

- Verdict: **FAIL**
- Windows scored: 2916; excluded: 4 (trades_truncated: 2, no_trades: 2)
- Fill rate: 19.2% of scored windows had a fill (385 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 287/624 = 46.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-31T11:15Z (market 6416854, result up)
Scored: p1 down filled at 114s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5172463768, 4s@0.53, 6s@0.53, 13s@0.5335135135, 13s@0.5199999843, 13s@0.5299999998, 13s@0.52, 13s@0.5199999843, 15s@0.53, 39s@0.5299999868, 55s@0.5299999868, 58s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.4799999939, 10s@0.4899999781, 10s@0.4899999183, 27s@0.48, 28s@0.48, 37s@0.47, 45s@0.49, 49s@0.4799999687, 49s@0.4799999875, 112s@0.25, 114s@0.2199999909, 117s@0.2199999921 ...

### 2026-10-31T14:30Z (market 6422314, result up)
Scored: p1 down filled at 118s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5299999868, 6s@0.53, 10s@0.5299999399, 13s@0.53, 21s@0.5399999568, 22s@0.539999986, 40s@0.5499999297, 55s@0.55, 64s@0.6999999296, 64s@0.6699999196, 64s@0.67, 66s@0.7 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.4799998464, 13s@0.4799999616, 34s@0.469999906, 40s@0.4599999034, 51s@0.4599999087, 118s@0.2299999517, 118s@0.2299999517, 118s@0.22, 118s@0.22, 120s@0.23, 120s@0.2299999979, 121s@0.25 ...


_Updated 2026-10-31 17:40Z_
