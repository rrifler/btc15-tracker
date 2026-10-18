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
- Windows scored: 1676; excluded: 1 (trades_truncated: 1)
- Fill rate: 17.7% of scored windows had a fill (123 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 147/329 = 44.7%. The verdict uses strict.

## Spot-checked windows

### 2026-10-18T08:45Z (market 5800119, result up)
Scored: p1 up filled at 59s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 48s@0.25, 59s@0.24, 60s@0.24, 62s@0.24, 62s@0.24, 62s@0.24, 74s@0.2321552586, 80s@0.24, 80s@0.24, 87s@0.25, 93s@0.22, 96s@0.22 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5799998446, 9s@0.58, 17s@0.59, 17s@0.58, 23s@0.6599999976, 23s@0.64, 23s@0.64, 24s@0.719001379, 24s@0.6963195147, 24s@0.71, 24s@0.6899999741, 26s@0.72 ...

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


_Updated 2026-10-18 14:31Z_
