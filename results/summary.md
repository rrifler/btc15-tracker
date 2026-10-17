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
- Windows scored: 1573; excluded: 1 (trades_truncated: 1)
- Fill rate: 17.4% of scored windows had a fill (100 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 137/304 = 45.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-17T07:30Z (market 5769569, result up)
Scored: p1 down filled at 45s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.5399999978, 9s@0.5399999568, 14s@0.5799999567, 14s@0.58, 14s@0.54, 14s@0.54, 14s@0.54, 15s@0.58, 17s@0.57, 23s@0.549999945, 23s@0.5499999505, 27s@0.56 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4699999556, 3s@0.46, 3s@0.4599997976, 3s@0.47, 5s@0.4699999796, 5s@0.469999906, 5s@0.47, 5s@0.47, 5s@0.47, 5s@0.47, 6s@0.47, 6s@0.47 ...

### 2026-10-17T10:00Z (market 5771268, result down)
Scored: p1 up filled at 29s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 29s@0.2299999517, 30s@0.2299999989, 33s@0.22, 38s@0.2, 44s@0.2, 45s@0.2, 48s@0.1899999962, 48s@0.16, 53s@0.16, 56s@0.16, 60s@0.17, 60s@0.17 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6510034308, 3s@0.6865945455, 3s@0.68, 3s@0.68, 3s@0.68, 3s@0.69, 3s@0.69, 3s@0.69, 3s@0.6799999788, 5s@0.675652967, 5s@0.69, 5s@0.69 ...

### 2026-10-17T11:00Z (market 5772340, result up)
Scored: p1 down filled at 110s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5399999568, 3s@0.5337075833, 3s@0.5286782998, 5s@0.56, 8s@0.6099999488, 8s@0.58, 12s@0.61, 12s@0.61, 17s@0.63, 24s@0.63, 27s@0.63, 32s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 56s@0.25, 56s@0.25, 110s@0.21, 111s@0.21, 111s@0.21, 113s@0.21, 113s@0.22, 113s@0.22, 117s@0.219999978, 126s@0.2, 134s@0.2, 141s@0.2 ...


_Updated 2026-10-17 12:37Z_
