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
- Windows scored: 29; excluded: 0
- Fill rate: 20.7% of scored windows had a fill (0 too small)
- Fills that reached 45c: 3 of 6 = 50.0% (95% range 18.8% to 81.2%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-0.80 (balance $19.20 from $20)
- Longest losing streak: 2
- Strict vs touch: strict 3/6 = 50.0%; touch 3/6 = 50.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-01T02:30Z (market 5145460, result down)
Scored: p1 down filled at 42s, exit hit 1; p2 none. Profit p1 0.6.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5699999479, 3s@0.57, 5s@0.599999988, 6s@0.6, 9s@0.65, 9s@0.65, 9s@0.6499999888, 11s@0.66, 12s@0.69, 12s@0.68, 12s@0.68, 15s@0.7 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 42s@0.22, 48s@0.23, 156s@0.2399999808, 159s@0.2423220153, 162s@0.24, 170s@0.22, 174s@0.2199999941, 200s@0.25, 201s@0.25, 201s@0.25, 201s@0.25, 201s@0.25 ...

### 2026-10-01T03:30Z (market 5146492, result up)
Scored: p1 up filled at 111s, exit hit 1; p2 none. Profit p1 0.8.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.4899999873, 111s@0.23, 114s@0.2299999517, 117s@0.23, 120s@0.23, 128s@0.23, 128s@0.25, 189s@0.45, 191s@0.45, 195s@0.45, 228s@0.5, 228s@0.49 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4957142857, 3s@0.54, 3s@0.52, 5s@0.5899999966, 5s@0.5899999841, 5s@0.5899999288, 6s@0.58, 9s@0.59, 11s@0.6, 29s@0.5799999768, 36s@0.58, 42s@0.5799999768 ...

### 2026-10-01T04:45Z (market 5148040, result up)
Scored: p1 down filled at 84s, exit hit 0; p2 none. Profit p1 -1.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5399999568, 6s@0.54, 6s@0.5399999568, 8s@0.57, 11s@0.559999972, 11s@0.559999776, 14s@0.5599999839, 18s@0.52, 24s@0.5299999607, 30s@0.5306537063, 36s@0.559999776, 36s@0.55 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.46, 3s@0.4599997976, 3s@0.5043263256, 3s@0.4835866325, 3s@0.46, 3s@0.4599997976, 3s@0.49, 3s@0.4897551212, 3s@0.4899999984, 3s@0.49, 3s@0.47, 5s@0.466640491 ...

### 2026-10-01T07:30Z (market 5150289, result up)
Scored: p1 down filled at 107s, exit hit 0; p2 none. Profit p1 -1.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5399999887, 3s@0.54, 3s@0.5494505495, 5s@0.5399998361, 5s@0.5399999568, 5s@0.5099998215, 5s@0.5399999568, 5s@0.53, 5s@0.5299999868, 5s@0.52, 5s@0.5154545455, 5s@0.5299998463 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.48, 5s@0.4855, 5s@0.47, 5s@0.4925, 6s@0.47, 6s@0.47, 6s@0.4699999962, 6s@0.4699999962, 6s@0.47, 6s@0.469999906, 8s@0.4699999691, 8s@0.4899998863 ...


_Updated 2026-10-01 08:27Z_
