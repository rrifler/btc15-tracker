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
- Windows scored: 1193; excluded: 0
- Fill rate: 17.3% of scored windows had a fill (32 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 104/228 = 45.6%. The verdict uses strict.

## Spot-checked windows

### 2026-10-13T07:15Z (market 5600040, result down)
Scored: p1 down filled at 100s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.48, 8s@0.5, 16s@0.5, 32s@0.4899998383, 38s@0.5699999774, 38s@0.54, 38s@0.53, 38s@0.5299999607, 38s@0.5, 38s@0.519999946, 38s@0.5, 38s@0.5199999567 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 16s@0.5099999995, 28s@0.51, 35s@0.5199998734, 40s@0.4544674, 50s@0.45, 59s@0.45, 100s@0.21, 103s@0.19, 104s@0.2123306233, 121s@0.25, 124s@0.2, 127s@0.2 ...

### 2026-10-13T07:30Z (market 5600212, result up)
Scored: p1 down filled at 50s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.6199999449, 4s@0.6199999324, 4s@0.6199999449, 7s@0.62, 10s@0.62, 11s@0.64, 11s@0.62, 23s@0.659999995, 23s@0.6999999813, 25s@0.73, 25s@0.7199999611, 25s@0.7199999611 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 50s@0.2299999969, 53s@0.2199999993, 64s@0.21, 65s@0.2, 74s@0.2, 76s@0.2, 89s@0.2, 97s@0.14, 98s@0.14, 100s@0.14, 103s@0.12, 104s@0.11 ...

### 2026-10-13T07:45Z (market 5600333, result up)
Scored: p1 down filled at 89s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5, 5s@0.48, 7s@0.56, 7s@0.48, 10s@0.5599999538, 25s@0.61, 25s@0.59, 25s@0.5899999546, 25s@0.5899999546, 25s@0.5899999546, 25s@0.58, 26s@0.6599999985 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5299998463, 7s@0.45, 7s@0.45, 8s@0.45, 14s@0.46, 16s@0.49, 16s@0.4599999269, 16s@0.46, 25s@0.46, 89s@0.25, 89s@0.2409638554, 91s@0.25 ...

### 2026-10-13T08:15Z (market 5600822, result down)
Scored: p1 up filled at 56s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.53, 4s@0.5499999807, 7s@0.5560896575, 13s@0.47, 13s@0.47, 13s@0.47, 14s@0.45, 14s@0.45, 14s@0.46, 14s@0.46, 16s@0.45, 16s@0.45 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.46, 2s@0.4599997976, 4s@0.46, 4s@0.4599999034, 4s@0.4599997976, 5s@0.46, 5s@0.46, 5s@0.46, 5s@0.46, 5s@0.4599999861, 5s@0.46, 7s@0.45 ...

### 2026-10-13T08:45Z (market 5600988, result down)
Scored: p1 up filled at 91s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.49, 8s@0.49, 13s@0.5799999882, 13s@0.5799998766, 13s@0.54, 13s@0.49, 16s@0.5812807825, 91s@0.23, 94s@0.25, 94s@0.2460371615, 94s@0.24, 148s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.49, 7s@0.48, 8s@0.5199999176, 8s@0.51, 28s@0.47, 28s@0.49, 28s@0.48, 32s@0.57, 34s@0.6, 50s@0.6099998495, 50s@0.6099998495, 50s@0.6099998495 ...


_Updated 2026-10-13 13:33Z_
