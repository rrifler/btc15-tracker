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
- Windows scored: 1621; excluded: 1 (trades_truncated: 1)
- Fill rate: 17.6% of scored windows had a fill (112 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 141/316 = 44.6%. The verdict uses strict.

## Spot-checked windows

### 2026-10-17T19:30Z (market 5785866, result up)
Scored: p1 down filled at 72s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5, 3s@0.5, 3s@0.51, 3s@0.51, 5s@0.55, 5s@0.52, 5s@0.531, 5s@0.51, 6s@0.5499999815, 8s@0.6, 8s@0.6, 17s@0.63 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 5s@0.5, 5s@0.5, 5s@0.5, 72s@0.2399999808, 77s@0.2399999984, 80s@0.2399999931, 81s@0.2439833701, 83s@0.25, 83s@0.25, 83s@0.25, 84s@0.25 ...

### 2026-10-17T20:00Z (market 5786489, result up)
Scored: p1 down filled at 29s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.46, 8s@0.4799999882, 11s@0.5, 17s@0.48, 17s@0.48, 23s@0.4899999796, 24s@0.5647354645, 24s@0.649999985, 24s@0.6524034262, 24s@0.6499999937, 24s@0.6499999953, 24s@0.6461988245 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5728395024, 3s@0.559999776, 8s@0.5, 9s@0.5099999137, 29s@0.24, 29s@0.24, 29s@0.23, 30s@0.22, 30s@0.21, 30s@0.2199999827, 32s@0.2, 32s@0.2 ...

### 2026-10-17T21:30Z (market 5788406, result down)
Scored: p1 up filled at 105s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 15s@0.459999992, 15s@0.45, 15s@0.45, 17s@0.4599999793, 17s@0.46, 18s@0.45, 20s@0.4699999944, 20s@0.47, 26s@0.51, 26s@0.5, 29s@0.51, 30s@0.5503761538 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.55, 2s@0.59, 2s@0.575, 2s@0.56, 3s@0.68, 3s@0.68, 3s@0.68, 3s@0.64, 3s@0.64, 3s@0.64, 3s@0.64, 5s@0.69 ...

### 2026-10-17T21:45Z (market 5788524, result up)
Scored: p1 down filled at 29s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.59, 2s@0.58, 3s@0.61, 3s@0.5999998938, 5s@0.629999995, 5s@0.65, 5s@0.64, 5s@0.64, 6s@0.6799998912, 6s@0.6799999401, 8s@0.68, 8s@0.6799999518 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 29s@0.24, 32s@0.25, 32s@0.25, 33s@0.2299999834, 36s@0.19, 36s@0.2, 39s@0.1699999983, 41s@0.17, 41s@0.1699999945, 41s@0.1699999887, 42s@0.1699999983, 47s@0.1699999887 ...

### 2026-10-17T22:00Z (market 5789685, result up)
Scored: p1 down filled at 29s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.56, 3s@0.59, 3s@0.59, 6s@0.64, 8s@0.61, 8s@0.61, 8s@0.61, 9s@0.64, 12s@0.6799999861, 12s@0.66, 12s@0.6599999892, 17s@0.7099999732 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 29s@0.25, 29s@0.24, 29s@0.24, 29s@0.24, 29s@0.2, 29s@0.2, 29s@0.2, 42s@0.2299999517, 44s@0.2, 47s@0.19, 48s@0.2016992679, 48s@0.1899999992 ...


_Updated 2026-10-18 00:46Z_
