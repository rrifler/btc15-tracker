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
- Windows scored: 573; excluded: 0
- Fill rate: 17.3% of scored windows had a fill (0 too small)
- Fills that reached 45c: 43 of 99 = 43.4% (95% range 34.1% to 53.3%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-11.80 (balance $8.20 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 43/99 = 43.4%; touch 48/109 = 44.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-06T23:15Z (market 5347261, result down)
Scored: p1 up filled at 119s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5, 5s@0.5, 5s@0.5, 5s@0.5, 13s@0.5, 13s@0.5, 29s@0.47, 34s@0.469999906, 35s@0.4899999824, 35s@0.47, 41s@0.4899999824, 43s@0.4899998383 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.51, 2s@0.5002836903, 4s@0.5099998215, 5s@0.5099998215, 5s@0.51, 7s@0.5099999905, 10s@0.5099999781, 16s@0.51, 16s@0.51, 25s@0.52, 26s@0.53, 26s@0.5299999354 ...

### 2026-10-07T01:00Z (market 5354549, result down)
Scored: p1 up filled at 68s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.469999906, 5s@0.45, 5s@0.45, 8s@0.45, 68s@0.22, 68s@0.21, 68s@0.21, 68s@0.21, 68s@0.21, 68s@0.21, 68s@0.21, 68s@0.21 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5299998463, 8s@0.53, 9s@0.52, 12s@0.5199999555, 14s@0.56, 15s@0.58, 15s@0.5799999162, 15s@0.57, 17s@0.6199998512, 17s@0.62, 17s@0.6199999803, 17s@0.62 ...

### 2026-10-07T01:30Z (market 5355696, result up)
Scored: p1 down filled at 110s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5505123173, 3s@0.5699999886, 3s@0.5699999886, 5s@0.5399999568, 5s@0.5399999568, 5s@0.539999986, 6s@0.5399999771, 6s@0.5399999828, 6s@0.5399999568, 6s@0.5399999542, 6s@0.54, 8s@0.5399999771 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.46, 5s@0.469999906, 5s@0.469999906, 5s@0.47, 5s@0.47, 6s@0.47, 6s@0.47, 8s@0.47, 8s@0.47, 12s@0.48, 12s@0.48, 12s@0.47 ...

### 2026-10-07T02:00Z (market 5355934, result down)
Scored: p1 up filled at 6s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.24, 6s@0.24, 6s@0.2399999808, 6s@0.25, 8s@0.2299999914, 8s@0.23, 8s@0.23, 8s@0.2399999808, 8s@0.23, 8s@0.2399999808, 8s@0.2299999517, 8s@0.2299999517 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.649999987, 2s@0.64, 2s@0.64, 2s@0.63, 2s@0.63, 2s@0.63, 2s@0.62, 2s@0.6299999933, 3s@0.7312934, 3s@0.7299999563, 3s@0.7392008626, 3s@0.719999977 ...


_Updated 2026-10-07 02:24Z_
