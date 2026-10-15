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
- Windows scored: 1358; excluded: 0
- Fill rate: 17.5% of scored windows had a fill (64 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 121/264 = 45.8%. The verdict uses strict.

## Spot-checked windows

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

### 2026-10-15T04:30Z (market 5678672, result up)
Scored: p1 down filled at 40s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.6, 4s@0.61, 4s@0.61, 5s@0.62, 5s@0.62, 7s@0.62, 11s@0.64, 11s@0.62, 11s@0.63, 11s@0.62, 19s@0.6799999889, 22s@0.68 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 40s@0.24, 40s@0.2399999923, 43s@0.2399999984, 58s@0.25, 64s@0.2299999993, 65s@0.22, 65s@0.22, 85s@0.17, 86s@0.1814079464, 91s@0.1899999951, 91s@0.1799999856, 94s@0.21 ...

### 2026-10-15T06:15Z (market 5680257, result up)
Scored: p1 down filled at 58s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.57, 4s@0.6, 5s@0.58, 8s@0.58, 10s@0.59999988, 13s@0.61, 20s@0.59999988, 22s@0.6, 23s@0.6, 23s@0.6, 29s@0.65, 31s@0.6699999823 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 58s@0.2299999898, 61s@0.24, 61s@0.2399999808, 61s@0.23, 65s@0.2466666667, 67s@0.24, 68s@0.25, 70s@0.25, 70s@0.25, 70s@0.25, 71s@0.2399999972, 130s@0.24 ...


_Updated 2026-10-15 06:44Z_
