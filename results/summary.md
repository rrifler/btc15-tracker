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
- Windows scored: 589; excluded: 0
- Fill rate: 17.0% of scored windows had a fill (0 too small)
- Fills that reached 45c: 43 of 100 = 43.0% (95% range 33.7% to 52.8%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.05 (balance $7.95 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 43/100 = 43.0%; touch 49/110 = 44.5%. The verdict uses strict.

## Spot-checked windows

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

### 2026-10-07T02:45Z (market 5360930, result up)
Scored: p1 down filled at 84s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5399999568, 5s@0.5299999783, 5s@0.53, 5s@0.53, 5s@0.53, 6s@0.5299999883, 6s@0.5299999797, 6s@0.5299998463, 8s@0.54, 8s@0.53, 8s@0.54, 8s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.47, 3s@0.47, 3s@0.469999906, 5s@0.4799998464, 5s@0.4799998464, 6s@0.48, 74s@0.25, 78s@0.25, 84s@0.24, 159s@0.45, 332s@0.2399999981, 360s@0.2099999988 ...


_Updated 2026-10-07 06:29Z_
