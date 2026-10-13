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
- Windows scored: 1165; excluded: 0
- Fill rate: 16.7% of scored windows had a fill (21 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 97/215 = 45.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-13T00:45Z (market 5591686, result down)
Scored: p1 up filled at 111s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 104s@0.25, 111s@0.23, 113s@0.24, 117s@0.23, 117s@0.23, 119s@0.2399999923, 120s@0.25, 125s@0.22, 125s@0.23, 126s@0.2299999914, 128s@0.2299999993, 132s@0.1899999962 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6, 0s@0.6100569527, 3s@0.56, 3s@0.5599999869, 5s@0.66, 5s@0.65, 5s@0.62, 8s@0.6599999969, 8s@0.6710476653, 8s@0.6599999448, 8s@0.6599999921, 8s@0.66 ...

### 2026-10-13T01:15Z (market 5592257, result up)
Scored: p1 down filled at 89s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5299999754, 8s@0.54, 8s@0.53, 8s@0.53, 8s@0.54, 11s@0.53, 17s@0.52, 18s@0.49, 20s@0.51, 20s@0.51, 24s@0.553, 24s@0.56 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.48, 6s@0.47, 8s@0.4599999817, 8s@0.47, 12s@0.4699999899, 14s@0.48, 14s@0.47, 14s@0.47, 15s@0.47, 17s@0.5, 18s@0.5, 18s@0.5199999792 ...

### 2026-10-13T03:00Z (market 5593086, result down)
Scored: p1 up filled at 62s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 57s@0.25, 59s@0.25, 62s@0.2389380497, 62s@0.22, 62s@0.22, 63s@0.24, 63s@0.2399999693, 65s@0.23, 65s@0.24, 66s@0.19, 68s@0.22, 68s@0.2299999693 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5904761905, 0s@0.58, 0s@0.57, 2s@0.6, 5s@0.6558641166, 5s@0.6373366065, 6s@0.67, 8s@0.68, 8s@0.6734125995, 8s@0.67, 11s@0.6599999957, 17s@0.68 ...

### 2026-10-13T03:30Z (market 5593380, result up)
Scored: p1 down filled at 84s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.52, 9s@0.53, 9s@0.5199999843, 9s@0.52, 9s@0.5199999843, 20s@0.46, 21s@0.469999906, 24s@0.48, 26s@0.51, 26s@0.51, 26s@0.51, 29s@0.49 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.4599999965, 6s@0.489999992, 6s@0.46, 6s@0.459999988, 8s@0.49, 8s@0.5, 9s@0.4699999944, 9s@0.47, 9s@0.47, 9s@0.48, 9s@0.5107076838, 12s@0.48 ...

### 2026-10-13T04:30Z (market 5595363, result up)
Scored: p1 down filled at 102s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.4899999968, 2s@0.49, 5s@0.4995916799, 6s@0.4699999944, 8s@0.4699999962, 9s@0.48, 9s@0.4799999687, 14s@0.5, 14s@0.4831034483, 15s@0.52, 15s@0.55, 15s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.539999967, 5s@0.5399999473, 5s@0.52, 5s@0.5199999927, 5s@0.5199999995, 6s@0.53, 6s@0.5297925311, 8s@0.53, 11s@0.5199999985, 15s@0.45, 15s@0.5099999975, 23s@0.4699999796 ...


_Updated 2026-10-13 06:34Z_
