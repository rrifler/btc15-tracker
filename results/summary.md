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
- Windows scored: 1680; excluded: 1 (trades_truncated: 1)
- Fill rate: 17.8% of scored windows had a fill (125 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 147/331 = 44.4%. The verdict uses strict.

## Spot-checked windows

### 2026-10-18T11:00Z (market 5804485, result up)
Scored: p1 up filled at 107s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.4719531972, 21s@0.51, 23s@0.5199999928, 27s@0.48, 105s@0.25, 107s@0.2303333333, 107s@0.25, 113s@0.21, 113s@0.21, 113s@0.21, 122s@0.17, 123s@0.16 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5454958333, 15s@0.52, 17s@0.5299999697, 23s@0.49, 29s@0.52, 30s@0.55, 32s@0.59, 32s@0.559999962, 32s@0.56, 32s@0.5899999288, 36s@0.59, 39s@0.5745516559 ...

### 2026-10-18T12:30Z (market 5807858, result down)
Scored: p1 up filled at 87s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.49, 12s@0.4899999824, 12s@0.49, 30s@0.48, 30s@0.4899999809, 30s@0.48, 87s@0.24, 87s@0.24, 89s@0.25, 162s@0.23, 164s@0.25, 164s@0.23 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.53, 5s@0.53, 5s@0.52, 12s@0.5199999961, 35s@0.59, 35s@0.59, 35s@0.5399999773, 35s@0.58, 35s@0.54, 36s@0.61, 36s@0.6001612368, 36s@0.592 ...

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


_Updated 2026-10-18 15:31Z_
