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

- Verdict: **NOT ENOUGH DATA**
- Windows scored: 566; excluded: 0
- Fill rate: 17.0% of scored windows had a fill (0 too small)
- Fills that reached 45c: 42 of 96 = 43.8% (95% range 34.3% to 53.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-11.50 (balance $8.50 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 42/96 = 43.8%; touch 47/106 = 44.3%. The verdict uses strict.

## Spot-checked windows

### 2026-10-06T19:30Z (market 5340101, result up)
Scored: p1 down filled at 108s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.51, 3s@0.5099999946, 3s@0.5, 3s@0.49, 3s@0.4899999984, 3s@0.49, 5s@0.52, 5s@0.5199999792, 5s@0.549999945, 5s@0.549999945, 5s@0.5, 6s@0.55128 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5099997829, 2s@0.5099997829, 3s@0.51, 5s@0.46, 5s@0.49, 5s@0.49, 5s@0.49, 6s@0.46, 6s@0.46, 108s@0.2199999984, 108s@0.23, 108s@0.23 ...

### 2026-10-06T19:45Z (market 5340173, result up)
Scored: p1 down filled at 77s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.47, 5s@0.47, 5s@0.469999906, 5s@0.469999906, 5s@0.47, 5s@0.47, 6s@0.5, 6s@0.5, 6s@0.48, 6s@0.47, 8s@0.589999995, 8s@0.5299999607 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.53, 3s@0.539999987, 77s@0.23, 78s@0.229999994, 78s@0.2299999914, 84s@0.2299999517, 84s@0.2299999517, 84s@0.2299999517, 86s@0.2299999937, 93s@0.22, 101s@0.2299999517, 116s@0.2 ...

### 2026-10-06T23:15Z (market 5347261, result down)
Scored: p1 up filled at 119s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5, 5s@0.5, 5s@0.5, 5s@0.5, 13s@0.5, 13s@0.5, 29s@0.47, 34s@0.469999906, 35s@0.4899999824, 35s@0.47, 41s@0.4899999824, 43s@0.4899998383 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.51, 2s@0.5002836903, 4s@0.5099998215, 5s@0.5099998215, 5s@0.51, 7s@0.5099999905, 10s@0.5099999781, 16s@0.51, 16s@0.51, 25s@0.52, 26s@0.53, 26s@0.5299999354 ...


_Updated 2026-10-07 00:35Z_
