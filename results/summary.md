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
- Windows scored: 1346; excluded: 0
- Fill rate: 17.5% of scored windows had a fill (62 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 121/262 = 46.2%. The verdict uses strict.

## Spot-checked windows

### 2026-10-14T21:45Z (market 5673877, result down)
Scored: p1 down filled at 34s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.6, 6s@0.6, 6s@0.6, 9s@0.6, 13s@0.5799999768, 18s@0.5799999768, 19s@0.57, 22s@0.62, 22s@0.619999991, 22s@0.6199999865, 22s@0.6199998327, 22s@0.6199999853 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 34s@0.2399999977, 34s@0.24, 63s@0.23, 67s@0.2399999923, 69s@0.2099999923, 75s@0.2, 76s@0.21, 90s@0.21, 94s@0.2099999989, 96s@0.2099999895, 103s@0.1799999999, 106s@0.1799999856 ...

### 2026-10-14T23:30Z (market 5674735, result up)
Scored: p1 up filled at 66s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 66s@0.2399999923, 66s@0.24, 73s@0.25, 73s@0.25, 73s@0.24, 145s@0.45, 147s@0.47, 147s@0.469999998, 148s@0.4799999687, 148s@0.4702040509, 295s@0.45, 295s@0.46 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.59, 7s@0.6, 7s@0.5999999803, 7s@0.5899999725, 9s@0.6150399717, 10s@0.66, 10s@0.66, 12s@0.6599999448, 16s@0.6899999685, 16s@0.6599999448, 16s@0.66, 18s@0.7 ...

### 2026-10-15T01:00Z (market 5676394, result up)
Scored: p1 down filled at 50s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.57, 4s@0.5973301495, 4s@0.65, 4s@0.6, 4s@0.589999991, 5s@0.65, 5s@0.65, 7s@0.6499999992, 7s@0.65, 7s@0.65, 7s@0.6499999854, 8s@0.65 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 50s@0.2299999986, 50s@0.2299999983, 52s@0.2199999934, 55s@0.1799999856, 55s@0.18, 59s@0.169999981, 62s@0.1368078165, 62s@0.12, 64s@0.12, 65s@0.1303685265, 65s@0.13, 65s@0.1299999942 ...

### 2026-10-15T01:30Z (market 5676597, result up)
Scored: p1 down filled at 41s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.56, 7s@0.56, 8s@0.56, 10s@0.55, 11s@0.59, 11s@0.58, 13s@0.6199999823, 13s@0.6117771844, 13s@0.63, 13s@0.62, 14s@0.61, 14s@0.61 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.4599999387, 10s@0.45, 38s@0.25, 41s@0.2399999981, 43s@0.24, 44s@0.229999994, 44s@0.2399999808, 46s@0.2299999693, 46s@0.23, 46s@0.2299999517, 47s@0.2359931146, 50s@0.2199999885 ...

### 2026-10-15T03:00Z (market 5677620, result down)
Scored: p1 up filled at 92s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5, 5s@0.5, 5s@0.5, 7s@0.5023498316, 7s@0.5, 91s@0.25, 92s@0.24, 94s@0.23, 94s@0.23, 95s@0.23, 95s@0.23, 103s@0.2199999966 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.51, 5s@0.5099999857, 5s@0.51, 5s@0.509999901, 7s@0.517322346, 7s@0.51, 10s@0.5299998463, 11s@0.54, 23s@0.5599999642, 29s@0.5899998466, 31s@0.59, 35s@0.61 ...


_Updated 2026-10-15 03:35Z_
