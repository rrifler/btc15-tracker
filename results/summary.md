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
- Windows scored: 1712; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.1% of scored windows had a fill (136 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 154/343 = 44.9%. The verdict uses strict.

## Spot-checked windows

### 2026-10-18T17:00Z (market 5825844, result up)
Scored: p1 down filled at 45s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5299999868, 6s@0.52, 8s@0.59, 8s@0.58, 8s@0.584, 12s@0.6, 12s@0.67, 23s@0.69, 23s@0.6899999508, 23s@0.68, 27s@0.71, 27s@0.71 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4951889, 6s@0.47, 6s@0.5, 45s@0.24, 47s@0.24, 48s@0.23, 56s@0.2299999517, 57s@0.2170403563, 65s@0.21, 66s@0.2099999983, 66s@0.2099999895, 66s@0.2099999895 ...

### 2026-10-18T17:30Z (market 5827343, result down)
Scored: p1 up filled at 50s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 9s@0.4899999968, 14s@0.49, 18s@0.47, 50s@0.2399999778, 50s@0.25, 53s@0.2351020408, 123s@0.2399999852, 125s@0.22, 125s@0.22, 128s@0.22, 132s@0.25, 132s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.52, 5s@0.52, 12s@0.51, 15s@0.5199999792, 21s@0.56, 21s@0.55, 23s@0.56, 23s@0.6099999536, 27s@0.58, 27s@0.629999937, 29s@0.66, 29s@0.6280769231 ...

### 2026-10-18T18:15Z (market 5830503, result down)
Scored: p1 up filled at 56s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 17s@0.47, 17s@0.4599999462, 17s@0.47, 17s@0.47, 17s@0.4599999462, 17s@0.4599999462, 17s@0.45, 17s@0.47, 18s@0.4899998748, 18s@0.48, 21s@0.4599999962, 56s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4899999824, 3s@0.5, 5s@0.5, 5s@0.5, 5s@0.49, 6s@0.61, 8s@0.61, 8s@0.63, 9s@0.6199998654, 9s@0.6199998654, 9s@0.619999876, 12s@0.57 ...

### 2026-10-18T18:30Z (market 5831324, result down)
Scored: p1 up filled at 75s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4799998464, 66s@0.25, 66s@0.25, 75s@0.24, 81s@0.24, 83s@0.25, 107s@0.25, 107s@0.24, 107s@0.25, 107s@0.25, 111s@0.25, 111s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5, 2s@0.5, 3s@0.52, 3s@0.5, 3s@0.5299999748, 3s@0.53, 3s@0.5, 5s@0.58, 5s@0.58, 5s@0.58, 6s@0.61, 6s@0.61 ...

### 2026-10-18T18:45Z (market 5831531, result up)
Scored: p1 down filled at 29s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.62, 2s@0.62, 3s@0.6599997888, 5s@0.69, 5s@0.682, 5s@0.6744, 9s@0.69, 12s@0.6899999795, 14s@0.7061474959, 14s@0.7, 15s@0.7444415034, 15s@0.72 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 29s@0.25, 29s@0.2399999808, 29s@0.2399999911, 35s@0.25, 39s@0.25, 44s@0.25, 60s@0.18, 60s@0.18, 60s@0.18, 62s@0.18, 66s@0.2, 66s@0.19 ...


_Updated 2026-10-18 23:29Z_
