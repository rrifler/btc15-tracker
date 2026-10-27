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
- Windows scored: 2556; excluded: 2 (trades_truncated: 2)
- Fill rate: 19.1% of scored windows had a fill (315 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 255/545 = 46.8%. The verdict uses strict.

## Spot-checked windows

### 2026-10-27T12:15Z (market 6248576, result up)
Scored: p1 down filled at 30s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5672849795, 2s@0.56, 3s@0.6099999662, 3s@0.57, 5s@0.61, 5s@0.6099999831, 8s@0.65, 8s@0.66, 14s@0.71, 14s@0.7, 17s@0.72, 20s@0.73 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 30s@0.22, 35s@0.2, 41s@0.1899999918, 41s@0.1899999947, 41s@0.19, 42s@0.19, 42s@0.19, 44s@0.2, 47s@0.2, 47s@0.2, 47s@0.2, 48s@0.2 ...

### 2026-10-27T14:00Z (market 6252426, result up)
Scored: p1 up filled at 84s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.533130122, 3s@0.5299998463, 6s@0.5027368421, 27s@0.4599999387, 84s@0.24, 84s@0.2399999868, 86s@0.25, 89s@0.239999999, 93s@0.25, 96s@0.22, 99s@0.2199999941, 99s@0.21 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.505, 5s@0.48, 6s@0.56, 8s@0.59, 17s@0.5299999607, 17s@0.53, 18s@0.5799999574, 20s@0.59, 21s@0.5599999328, 27s@0.5299999763, 27s@0.5399999568, 30s@0.55 ...

### 2026-10-27T14:15Z (market 6252547, result up)
Scored: p1 up filled at 114s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 18s@0.45, 21s@0.469999906, 23s@0.469999906, 24s@0.4799998464, 24s@0.48, 24s@0.48, 24s@0.47, 32s@0.4799999687, 32s@0.48, 41s@0.47, 45s@0.4599999387, 47s@0.46 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.57, 6s@0.5699999467, 12s@0.549999945, 15s@0.5503685504, 15s@0.5499999214, 15s@0.55, 27s@0.5299999961, 29s@0.5299999587, 41s@0.54, 41s@0.54, 41s@0.5299999792, 41s@0.53 ...

### 2026-10-27T15:00Z (market 6253986, result down)
Scored: p1 down filled at 62s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.4599999687, 2s@0.4599999669, 6s@0.5274626866, 8s@0.54, 11s@0.5399999568, 18s@0.53, 18s@0.5299999607, 21s@0.5399999568, 23s@0.6024481592, 23s@0.6199999575, 23s@0.6299999454, 23s@0.6147117206 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5199999792, 3s@0.5199999438, 9s@0.4699999944, 17s@0.4699999944, 18s@0.47, 18s@0.48, 18s@0.4799999694, 41s@0.25, 41s@0.25, 42s@0.25, 42s@0.25, 42s@0.25 ...

### 2026-10-27T15:15Z (market 6254768, result up)
Scored: p1 down filled at 119s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 12s@0.49, 12s@0.4899999824, 24s@0.5, 26s@0.5, 41s@0.4799998464, 45s@0.4699999944, 48s@0.46, 50s@0.47, 71s@0.509999914, 83s@0.5399999955, 83s@0.53, 83s@0.52 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 3s@0.5, 5s@0.5, 11s@0.5, 17s@0.5099998215, 24s@0.5099999516, 29s@0.51, 38s@0.5299999868, 53s@0.5399999568, 71s@0.5, 74s@0.5, 74s@0.5 ...


_Updated 2026-10-27 18:46Z_
