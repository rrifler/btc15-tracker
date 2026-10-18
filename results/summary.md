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
- Windows scored: 1696; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.0% of scored windows had a fill (132 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 151/339 = 44.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-18T14:00Z (market 5818541, result down)
Scored: p1 up filled at 117s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4799999846, 6s@0.48, 8s@0.48, 8s@0.47, 8s@0.47, 8s@0.47, 11s@0.5, 14s@0.51, 15s@0.54, 15s@0.54, 15s@0.5358333333, 17s@0.54 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 12s@0.5099999984, 12s@0.5211488075, 12s@0.52, 14s@0.5199999406, 14s@0.52, 15s@0.47, 15s@0.469999991, 15s@0.4899999968, 15s@0.4899999824, 18s@0.4699999988, 18s@0.47, 20s@0.4699999988 ...

### 2026-10-18T14:30Z (market 5818740, result down)
Scored: p1 up filled at 26s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 20s@0.25, 21s@0.25, 21s@0.25, 26s@0.22, 27s@0.1818181818, 29s@0.17, 29s@0.1699999983, 29s@0.1799999981, 30s@0.18, 30s@0.1772223077, 32s@0.1899999962, 32s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.565, 0s@0.55, 2s@0.59, 2s@0.58, 3s@0.6199999046, 3s@0.6199999587, 5s@0.62, 5s@0.6199999903, 8s@0.66, 8s@0.66, 11s@0.709999976, 12s@0.71 ...

### 2026-10-18T15:00Z (market 5819808, result up)
Scored: p1 down filled at 41s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5199997957, 3s@0.48, 3s@0.5099998215, 3s@0.49, 3s@0.48, 5s@0.53, 5s@0.529999783, 5s@0.5216237992, 6s@0.5299999229, 8s@0.5415, 8s@0.533009, 8s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.45, 2s@0.5199999843, 2s@0.5, 2s@0.5, 3s@0.5099428287, 3s@0.53, 3s@0.52, 41s@0.249991349, 48s@0.2299999517, 51s@0.22, 56s@0.2199999984, 56s@0.2199999984 ...

### 2026-10-18T15:30Z (market 5821350, result down)
Scored: p1 up filled at 38s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 38s@0.21, 41s@0.22, 41s@0.22, 41s@0.21, 41s@0.22, 48s@0.1699999887, 48s@0.18, 48s@0.2099999695, 51s@0.13, 54s@0.14, 57s@0.14, 57s@0.1499999966 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.59, 3s@0.5899999725, 5s@0.5999999902, 5s@0.6236094601, 5s@0.609999783, 6s@0.6999999616, 12s@0.7199999527, 12s@0.72, 12s@0.71, 14s@0.7299999903, 33s@0.74, 35s@0.75 ...

### 2026-10-18T17:00Z (market 5825844, result up)
Scored: p1 down filled at 45s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5299999868, 6s@0.52, 8s@0.59, 8s@0.58, 8s@0.584, 12s@0.6, 12s@0.67, 23s@0.69, 23s@0.6899999508, 23s@0.68, 27s@0.71, 27s@0.71 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4951889, 6s@0.47, 6s@0.5, 45s@0.24, 47s@0.24, 48s@0.23, 56s@0.2299999517, 57s@0.2170403563, 65s@0.21, 66s@0.2099999983, 66s@0.2099999895, 66s@0.2099999895 ...


_Updated 2026-10-18 19:29Z_
