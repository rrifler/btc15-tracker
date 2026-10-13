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
- Windows scored: 1197; excluded: 0
- Fill rate: 17.2% of scored windows had a fill (32 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 104/228 = 45.6%. The verdict uses strict.

## Spot-checked windows

### 2026-10-13T08:15Z (market 5600822, result down)
Scored: p1 up filled at 56s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.53, 4s@0.5499999807, 7s@0.5560896575, 13s@0.47, 13s@0.47, 13s@0.47, 14s@0.45, 14s@0.45, 14s@0.46, 14s@0.46, 16s@0.45, 16s@0.45 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.46, 2s@0.4599997976, 4s@0.46, 4s@0.4599999034, 4s@0.4599997976, 5s@0.46, 5s@0.46, 5s@0.46, 5s@0.46, 5s@0.4599999861, 5s@0.46, 7s@0.45 ...

### 2026-10-13T08:45Z (market 5600988, result down)
Scored: p1 up filled at 91s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.49, 8s@0.49, 13s@0.5799999882, 13s@0.5799998766, 13s@0.54, 13s@0.49, 16s@0.5812807825, 91s@0.23, 94s@0.25, 94s@0.2460371615, 94s@0.24, 148s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.49, 7s@0.48, 8s@0.5199999176, 8s@0.51, 28s@0.47, 28s@0.49, 28s@0.48, 32s@0.57, 34s@0.6, 50s@0.6099998495, 50s@0.6099998495, 50s@0.6099998495 ...

### 2026-10-13T09:00Z (market 5601365, result down)
Scored: p1 up filled at 52s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5, 4s@0.5, 5s@0.459999979, 5s@0.5, 7s@0.45, 52s@0.21, 55s@0.23, 55s@0.21, 55s@0.21, 56s@0.22, 58s@0.24, 58s@0.24 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5, 4s@0.5099999933, 5s@0.51, 5s@0.51, 8s@0.56, 10s@0.5899999458, 10s@0.5810152122, 11s@0.5899998836, 11s@0.6, 13s@0.61, 13s@0.6, 14s@0.63 ...

### 2026-10-13T09:45Z (market 5601534, result down)
Scored: p1 up filled at 61s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 61s@0.2, 62s@0.2, 62s@0.2, 67s@0.21, 67s@0.19, 67s@0.18, 67s@0.23, 67s@0.23, 67s@0.22, 67s@0.2, 67s@0.18, 68s@0.2399999981 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.55, 2s@0.58, 2s@0.56, 2s@0.57, 7s@0.64, 10s@0.64, 10s@0.64, 11s@0.64, 11s@0.64, 13s@0.69, 13s@0.69, 13s@0.6899999561 ...

### 2026-10-13T10:15Z (market 5601961, result down)
Scored: p1 up filled at 86s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.45, 11s@0.46, 13s@0.47, 14s@0.47, 14s@0.47, 17s@0.47, 17s@0.47, 17s@0.47, 19s@0.5, 19s@0.49, 31s@0.45, 31s@0.45 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.549999956, 1s@0.5559968193, 2s@0.6, 2s@0.5899999725, 2s@0.59, 2s@0.5776892342, 4s@0.5499999898, 4s@0.5957499312, 8s@0.55, 11s@0.5399999568, 13s@0.54, 26s@0.51 ...


_Updated 2026-10-13 14:29Z_
