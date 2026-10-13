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
- Windows scored: 1177; excluded: 0
- Fill rate: 17.2% of scored windows had a fill (28 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 100/222 = 45.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-13T03:00Z (market 5593086, result down)
Scored: p1 up filled at 62s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 57s@0.25, 59s@0.25, 62s@0.2389380497, 62s@0.22, 62s@0.22, 63s@0.24, 63s@0.2399999693, 65s@0.23, 65s@0.24, 66s@0.19, 68s@0.22, 68s@0.2299999693 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5904761905, 0s@0.58, 0s@0.57, 2s@0.6, 5s@0.6558641166, 5s@0.6373366065, 6s@0.67, 8s@0.68, 8s@0.6734125995, 8s@0.67, 11s@0.6599999957, 17s@0.68 ...

### 2026-10-13T03:30Z (market 5593380, result up)
Scored: p1 down filled at 84s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.52, 9s@0.53, 9s@0.5199999843, 9s@0.52, 9s@0.5199999843, 20s@0.46, 21s@0.469999906, 24s@0.48, 26s@0.51, 26s@0.51, 26s@0.51, 29s@0.49 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.4599999965, 6s@0.489999992, 6s@0.46, 6s@0.459999988, 8s@0.49, 8s@0.5, 9s@0.4699999944, 9s@0.47, 9s@0.47, 9s@0.48, 9s@0.5107076838, 12s@0.48 ...

### 2026-10-13T04:30Z (market 5595363, result up)
Scored: p1 down filled at 102s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.4899999968, 2s@0.49, 5s@0.4995916799, 6s@0.4699999944, 8s@0.4699999962, 9s@0.48, 9s@0.4799999687, 14s@0.5, 14s@0.4831034483, 15s@0.52, 15s@0.55, 15s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.539999967, 5s@0.5399999473, 5s@0.52, 5s@0.5199999927, 5s@0.5199999995, 6s@0.53, 6s@0.5297925311, 8s@0.53, 11s@0.5199999985, 15s@0.45, 15s@0.5099999975, 23s@0.4699999796 ...

### 2026-10-13T06:30Z (market 5599430, result up)
Scored: p1 up filled at 101s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.46, 8s@0.47, 8s@0.47, 8s@0.47, 8s@0.47, 19s@0.48, 19s@0.46, 22s@0.5, 22s@0.5, 29s@0.51, 41s@0.51, 53s@0.51 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.5399999482, 7s@0.5399999327, 19s@0.5299999399, 20s@0.5099999949, 28s@0.49, 35s@0.5, 40s@0.4990761271, 52s@0.49, 56s@0.48, 62s@0.5, 64s@0.505, 64s@0.5599999756 ...

### 2026-10-13T07:15Z (market 5600040, result down)
Scored: p1 down filled at 100s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.48, 8s@0.5, 16s@0.5, 32s@0.4899998383, 38s@0.5699999774, 38s@0.54, 38s@0.53, 38s@0.5299999607, 38s@0.5, 38s@0.519999946, 38s@0.5, 38s@0.5199999567 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 16s@0.5099999995, 28s@0.51, 35s@0.5199998734, 40s@0.4544674, 50s@0.45, 59s@0.45, 100s@0.21, 103s@0.19, 104s@0.2123306233, 121s@0.25, 124s@0.2, 127s@0.2 ...


_Updated 2026-10-13 09:28Z_
