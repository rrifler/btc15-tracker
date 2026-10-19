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
- Windows scored: 1717; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.1% of scored windows had a fill (136 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 154/343 = 44.9%. The verdict uses strict.

## Spot-checked windows

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

### 2026-10-18T19:00Z (market 5832497, result down)
Scored: p1 up filled at 99s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.46, 5s@0.46, 9s@0.4599999879, 14s@0.46, 15s@0.4599997976, 17s@0.47, 18s@0.4736229508, 18s@0.469999999, 24s@0.4599997976, 99s@0.2424023155, 131s@0.23, 134s@0.23 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.55, 5s@0.55, 6s@0.55, 6s@0.55, 12s@0.5499999828, 30s@0.55, 30s@0.5499999763, 32s@0.6, 32s@0.6, 32s@0.56, 33s@0.6, 33s@0.6099998764 ...

### 2026-10-18T20:00Z (market 5834721, result down)
Scored: p1 down filled at 78s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4599999034, 3s@0.45, 5s@0.5, 5s@0.49, 5s@0.49, 5s@0.478125, 6s@0.4799998464, 6s@0.48, 6s@0.5, 6s@0.4899999342, 8s@0.4899999491, 8s@0.49 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5599999955, 3s@0.55, 5s@0.51, 6s@0.54, 6s@0.5499999865, 6s@0.53, 6s@0.5599998682, 6s@0.52, 11s@0.52, 12s@0.5203635607, 20s@0.5199999447, 21s@0.54 ...


_Updated 2026-10-19 00:46Z_
