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
- Windows scored: 1889; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.8% of scored windows had a fill (181 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 176/391 = 45.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-20T13:45Z (market 5923798, result up)
Scored: p1 down filled at 63s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.469999906, 6s@0.48, 14s@0.46, 17s@0.47, 17s@0.46, 17s@0.4977990085, 17s@0.47, 17s@0.4599999968, 17s@0.4599999968, 17s@0.46, 17s@0.4699999736, 17s@0.46 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5399999568, 6s@0.54, 6s@0.54, 6s@0.5399999353, 9s@0.5499999974, 12s@0.5499999807, 17s@0.5499999926, 63s@0.24, 63s@0.24, 63s@0.24, 65s@0.2399999923, 65s@0.24 ...

### 2026-10-20T14:00Z (market 5924627, result up)
Scored: p1 down filled at 101s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.509999956, 3s@0.5299998463, 5s@0.5099999863, 5s@0.54, 6s@0.51, 8s@0.48, 8s@0.48, 8s@0.48, 8s@0.48, 8s@0.48, 8s@0.48, 8s@0.48 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.48, 3s@0.47, 3s@0.48, 3s@0.4799999616, 3s@0.4799999598, 3s@0.47, 3s@0.47, 3s@0.47, 5s@0.5, 5s@0.48572, 5s@0.5, 5s@0.4710416667 ...

### 2026-10-20T15:00Z (market 5927247, result down)
Scored: p1 up filled at 101s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.45, 6s@0.45, 101s@0.23, 101s@0.2299999985, 102s@0.229999994, 108s@0.2199999931, 110s@0.2199999959, 110s@0.2199999959, 110s@0.2199999841, 113s@0.23, 113s@0.23, 119s@0.219999978 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5699998454, 3s@0.5799999768, 9s@0.5599999642, 9s@0.5699999886, 9s@0.56, 11s@0.56, 14s@0.6, 14s@0.58, 15s@0.59999988, 18s@0.61, 18s@0.6, 18s@0.6 ...

### 2026-10-20T15:15Z (market 5928237, result up)
Scored: p1 down filled at 95s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.62, 8s@0.57, 8s@0.57, 14s@0.5299999325, 14s@0.5299998463, 15s@0.53, 15s@0.53, 15s@0.53, 17s@0.5099999334, 17s@0.51, 17s@0.5099999672, 17s@0.5099999334 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 9s@0.45, 9s@0.47, 9s@0.45, 9s@0.45, 11s@0.469999998, 11s@0.47, 11s@0.4699999962, 11s@0.4699999944, 11s@0.4675996159, 12s@0.47, 14s@0.48, 14s@0.48 ...

### 2026-10-20T15:45Z (market 5928627, result up)
Scored: p1 up filled at 38s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 36s@0.25, 36s@0.25, 36s@0.25, 38s@0.24, 38s@0.24, 45s@0.2399999808, 47s@0.25, 47s@0.25, 47s@0.24, 126s@0.25, 137s@0.24, 243s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.6099998373, 3s@0.6099997255, 5s@0.6099998597, 6s@0.61, 9s@0.6, 9s@0.61, 11s@0.61, 12s@0.65, 14s@0.65, 14s@0.65, 18s@0.6799999921, 18s@0.68 ...


_Updated 2026-10-20 19:38Z_
