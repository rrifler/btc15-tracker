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
- Windows scored: 1270; excluded: 0
- Fill rate: 17.4% of scored windows had a fill (47 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 113/246 = 45.9%. The verdict uses strict.

## Spot-checked windows

### 2026-10-14T02:15Z (market 5639540, result down)
Scored: p1 up filled at 82s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 82s@0.23, 86s@0.24, 103s@0.25, 103s@0.23, 103s@0.24, 154s@0.45, 158s@0.4599999387, 161s@0.46, 166s@0.48, 175s@0.45, 218s@0.5, 227s@0.55 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.5, 2s@0.5, 2s@0.5, 4s@0.59, 4s@0.5899999458, 4s@0.5899998496, 4s@0.59, 4s@0.59, 5s@0.59, 7s@0.6, 7s@0.59, 10s@0.59 ...

### 2026-10-14T02:45Z (market 5639875, result up)
Scored: p1 down filled at 74s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5899999705, 4s@0.59, 4s@0.5899998496, 4s@0.5899999458, 13s@0.58, 14s@0.61, 14s@0.6099999322, 14s@0.59, 19s@0.65, 19s@0.64, 26s@0.6632048641, 26s@0.65 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.45, 74s@0.24, 77s@0.22, 77s@0.229999994, 79s@0.23, 83s@0.19, 83s@0.19, 83s@0.1899999962, 83s@0.19, 83s@0.19, 83s@0.19, 86s@0.1929752778 ...

### 2026-10-14T03:30Z (market 5640109, result up)
Scored: p1 down filled at 44s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5, 2s@0.49281375, 2s@0.5, 2s@0.47, 4s@0.5, 4s@0.5, 4s@0.5, 4s@0.5, 5s@0.54, 5s@0.51, 5s@0.5099999946, 5s@0.509999966 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.53, 2s@0.5099999971, 2s@0.5099999516, 2s@0.51, 2s@0.5099998215, 2s@0.51, 2s@0.51, 2s@0.5099999909, 4s@0.5099999949, 5s@0.4699999944, 5s@0.4699999641, 5s@0.469999981 ...

### 2026-10-14T04:15Z (market 5641145, result up)
Scored: p1 up filled at 107s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.45, 7s@0.4899999984, 7s@0.48, 8s@0.4899999884, 13s@0.45, 13s@0.45, 17s@0.45, 107s@0.23, 113s@0.25, 113s@0.25, 113s@0.25, 113s@0.2444424063 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5599999955, 10s@0.53, 13s@0.56, 14s@0.56, 25s@0.61, 25s@0.6099998383, 25s@0.5912307529, 25s@0.58, 25s@0.58, 29s@0.629999937, 32s@0.63, 43s@0.66 ...

### 2026-10-14T04:30Z (market 5641653, result down)
Scored: p1 down filled at 83s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5199999792, 5s@0.5099999972, 7s@0.5099999442, 17s@0.57, 17s@0.5699999673, 17s@0.53, 19s@0.6099999984, 19s@0.61, 19s@0.58, 19s@0.6099999913, 19s@0.5799999348, 19s@0.58 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.4899998383, 5s@0.5, 5s@0.4919323101, 5s@0.5, 5s@0.5, 7s@0.5, 7s@0.5, 83s@0.2199999998, 86s@0.1899999962, 91s@0.1899999962, 92s@0.2, 92s@0.2 ...


_Updated 2026-10-14 08:38Z_
