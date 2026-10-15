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
- Windows scored: 1386; excluded: 0
- Fill rate: 17.5% of scored windows had a fill (68 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 125/269 = 46.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-15T09:15Z (market 5682102, result down)
Scored: p1 up filled at 70s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 13s@0.5, 70s@0.2361111111, 70s@0.229999994, 77s@0.2199999885, 79s@0.2099999997, 80s@0.21, 83s@0.2099999983, 86s@0.2099999895, 89s@0.21, 92s@0.2099999895, 94s@0.23, 95s@0.2347594724 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.4612365056, 5s@0.4595404588, 8s@0.4799998464, 8s@0.4699999962, 10s@0.4899998383, 10s@0.4799999585, 10s@0.47, 16s@0.5103042184, 17s@0.546, 22s@0.55, 28s@0.59, 28s@0.5699999886 ...

### 2026-10-15T10:30Z (market 5682562, result down)
Scored: p1 down filled at 88s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.579999997, 7s@0.58, 10s@0.5799999768, 13s@0.58, 16s@0.6, 16s@0.59, 19s@0.645, 19s@0.6, 26s@0.6499999409, 29s@0.64, 31s@0.62, 32s@0.61 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 82s@0.25, 88s@0.2, 91s@0.2, 94s@0.19375, 97s@0.2, 98s@0.2, 98s@0.2, 101s@0.2, 101s@0.2, 106s@0.2, 134s@0.19, 134s@0.2 ...

### 2026-10-15T11:00Z (market 5682868, result down)
Scored: p1 up filled at 103s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.46, 1s@0.46, 4s@0.47, 4s@0.47, 4s@0.47, 4s@0.47, 13s@0.48, 15s@0.45, 16s@0.4599999953, 46s@0.49, 49s@0.4599998269, 55s@0.45 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.54, 6s@0.5, 12s@0.52, 12s@0.5299998463, 13s@0.5499999774, 16s@0.55, 18s@0.55, 18s@0.55, 18s@0.55, 18s@0.55, 24s@0.6, 24s@0.5999999625 ...

### 2026-10-15T12:30Z (market 5685285, result down)
Scored: p1 up filled at 7s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5133333333, 4s@0.51, 4s@0.51, 5s@0.52, 7s@0.23, 7s@0.2246666667, 7s@0.2469045617, 7s@0.25, 8s@0.2375, 8s@0.23, 8s@0.2215799604, 8s@0.23 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5, 4s@0.52, 4s@0.5199999792, 4s@0.54, 4s@0.5228848465, 4s@0.4912195122, 5s@0.59, 5s@0.79, 5s@0.54, 5s@0.69, 5s@0.6586946015, 5s@0.59 ...


_Updated 2026-10-15 13:46Z_
