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
- Windows scored: 2417; excluded: 2 (trades_truncated: 2)
- Fill rate: 19.2% of scored windows had a fill (290 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 238/514 = 46.3%. The verdict uses strict.

## Spot-checked windows

### 2026-10-26T03:00Z (market 6170231, result up)
Scored: p1 down filled at 98s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.559999776, 3s@0.5399999568, 6s@0.51, 6s@0.48, 9s@0.5399999568, 9s@0.54, 9s@0.54, 11s@0.575, 12s@0.5799999768, 14s@0.57, 17s@0.5799999768, 29s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.45, 3s@0.47, 3s@0.47, 5s@0.6299999573, 5s@0.6299999573, 5s@0.6299999573, 5s@0.53, 5s@0.51, 5s@0.5257960633, 5s@0.53, 5s@0.52, 5s@0.49 ...

### 2026-10-26T04:15Z (market 6173122, result down)
Scored: p1 down filled at 48s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4799999346, 5s@0.49, 6s@0.51, 6s@0.51, 9s@0.5199999843, 12s@0.5299998463, 18s@0.53, 20s@0.55, 20s@0.55, 30s@0.54, 32s@0.56, 32s@0.5399999948 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5099999687, 6s@0.4899999561, 6s@0.51, 8s@0.5, 9s@0.4899999824, 9s@0.49, 11s@0.4899999984, 11s@0.4899999584, 12s@0.48, 12s@0.5, 23s@0.469999906, 48s@0.2399999923 ...

### 2026-10-26T04:30Z (market 6173578, result up)
Scored: p1 down filled at 84s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.65, 0s@0.6337820076, 2s@0.6777995939, 3s@0.64, 9s@0.63, 9s@0.63, 9s@0.63, 29s@0.6199998512, 51s@0.66, 51s@0.66, 57s@0.67, 57s@0.67 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 84s@0.22, 84s@0.22, 90s@0.2099999983, 90s@0.22, 96s@0.1899999896, 98s@0.21, 110s@0.2299999782, 120s@0.25, 122s@0.2399999808, 128s@0.1899999962, 131s@0.1799999856, 135s@0.1499999925 ...

### 2026-10-26T06:15Z (market 6179907, result down)
Scored: p1 down filled at 66s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 15s@0.45, 17s@0.46, 21s@0.4599997976, 23s@0.46, 26s@0.5033333333, 27s@0.56, 30s@0.6, 30s@0.59, 30s@0.56, 33s@0.649999805, 35s@0.65, 35s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.57, 3s@0.54, 6s@0.61, 11s@0.5599999732, 20s@0.549999945, 21s@0.55, 24s@0.5299999868, 24s@0.54, 62s@0.25, 66s@0.229999994, 66s@0.2299999517, 68s@0.2299999993 ...

### 2026-10-26T07:00Z (market 6181094, result down)
Scored: p1 down filled at 51s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.48, 8s@0.56, 8s@0.5599999131, 8s@0.56, 8s@0.5599999131, 18s@0.45, 21s@0.55, 21s@0.51, 23s@0.51, 30s@0.6099999488, 33s@0.62, 33s@0.61 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.52, 3s@0.5199999792, 5s@0.51, 6s@0.4599999669, 6s@0.4899999944, 6s@0.4899999944, 6s@0.4899999824, 6s@0.4899999944, 6s@0.4899999944, 6s@0.4899999944, 6s@0.4899999944, 6s@0.4899999944 ...


_Updated 2026-10-26 07:54Z_
