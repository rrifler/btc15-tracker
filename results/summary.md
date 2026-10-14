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
- Windows scored: 1254; excluded: 0
- Fill rate: 17.5% of scored windows had a fill (45 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 111/244 = 45.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-13T23:00Z (market 5637570, result down)
Scored: p1 up filled at 99s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.45, 99s@0.2421422222, 99s@0.21069, 99s@0.23207, 100s@0.1899999962, 100s@0.18, 102s@0.17, 102s@0.17, 102s@0.18, 102s@0.17, 102s@0.17, 103s@0.1799999999 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.48, 4s@0.4799999616, 7s@0.5899999458, 7s@0.5718333333, 7s@0.5899998496, 7s@0.5825, 9s@0.5899999705, 19s@0.58, 22s@0.5872917238, 24s@0.6, 28s@0.59, 36s@0.61 ...

### 2026-10-14T00:00Z (market 5638420, result up)
Scored: p1 down filled at 99s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.549999945, 7s@0.6238461538, 7s@0.6199999885, 7s@0.6199999651, 7s@0.5795454545, 7s@0.6199998784, 7s@0.6199999449, 7s@0.6199999885, 7s@0.62, 9s@0.65, 9s@0.65, 9s@0.65 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.45, 6s@0.45, 73s@0.25, 81s@0.25, 84s@0.25, 84s@0.25, 99s@0.2199999974, 127s@0.21, 130s@0.24, 130s@0.23, 130s@0.24, 130s@0.24 ...

### 2026-10-14T00:15Z (market 5638505, result up)
Scored: p1 down filled at 63s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.53, 3s@0.57, 3s@0.5599999756, 4s@0.604, 15s@0.6499999409, 15s@0.64, 16s@0.66, 16s@0.65, 16s@0.6499999618, 22s@0.6199999471, 27s@0.61, 28s@0.62 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 63s@0.2299999782, 64s@0.19, 64s@0.1899999994, 66s@0.21, 66s@0.2, 66s@0.21, 67s@0.2099999923, 72s@0.21, 130s@0.25, 132s@0.25, 136s@0.2, 136s@0.2099999895 ...

### 2026-10-14T02:00Z (market 5639458, result up)
Scored: p1 down filled at 106s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 16s@0.45, 16s@0.46, 34s@0.5, 47s@0.52, 50s@0.57, 50s@0.57, 55s@0.61, 61s@0.61, 68s@0.64, 71s@0.68, 77s@0.6831373388, 79s@0.7099999803 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.52, 4s@0.5499999549, 4s@0.5499998382, 4s@0.575, 4s@0.52, 7s@0.59, 8s@0.5899999435, 16s@0.55, 22s@0.5699999886, 22s@0.5699999886, 23s@0.5799999768, 23s@0.5739164642 ...

### 2026-10-14T02:15Z (market 5639540, result down)
Scored: p1 up filled at 82s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 82s@0.23, 86s@0.24, 103s@0.25, 103s@0.23, 103s@0.24, 154s@0.45, 158s@0.4599999387, 161s@0.46, 166s@0.48, 175s@0.45, 218s@0.5, 227s@0.55 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.5, 2s@0.5, 2s@0.5, 4s@0.59, 4s@0.5899999458, 4s@0.5899998496, 4s@0.59, 4s@0.59, 5s@0.59, 7s@0.6, 7s@0.59, 10s@0.59 ...


_Updated 2026-10-14 04:38Z_
