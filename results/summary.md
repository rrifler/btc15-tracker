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
- Windows scored: 413; excluded: 0
- Fill rate: 17.2% of scored windows had a fill (0 too small)
- Fills that reached 45c: 33 of 71 = 46.5% (95% range 35.4% to 58.0%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-7.95 (balance $12.05 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 33/71 = 46.5%; touch 37/76 = 48.7%. The verdict uses strict.

## Spot-checked windows

### 2026-10-05T06:00Z (market 5269338, result up)
Scored: p1 down filled at 100s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5, 7s@0.53, 7s@0.51, 8s@0.55, 14s@0.5, 14s@0.5499999966, 16s@0.5, 16s@0.5299998463, 25s@0.54, 26s@0.58, 28s@0.5199999451, 28s@0.52 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5, 7s@0.49, 14s@0.46, 16s@0.49, 17s@0.5, 23s@0.47, 26s@0.48, 29s@0.4899999824, 38s@0.48, 100s@0.21, 100s@0.21, 104s@0.19 ...

### 2026-10-05T06:45Z (market 5269696, result up)
Scored: p1 down filled at 103s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.49, 10s@0.5, 10s@0.49, 61s@0.5499999738, 61s@0.54, 61s@0.52, 61s@0.51, 67s@0.55, 67s@0.55, 70s@0.5899999895, 70s@0.59, 71s@0.61 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5199999792, 11s@0.5099999863, 26s@0.5099999516, 35s@0.51, 37s@0.5099999776, 43s@0.5099998215, 64s@0.46, 89s@0.45, 89s@0.45, 89s@0.4599999197, 94s@0.45, 103s@0.23 ...

### 2026-10-05T08:45Z (market 5273127, result down)
Scored: p1 up filled at 62s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.45, 4s@0.45, 4s@0.47, 4s@0.47, 62s@0.2299999517, 62s@0.2399999808, 62s@0.24, 62s@0.1899999842, 64s@0.21, 64s@0.202679558, 64s@0.2199999966, 64s@0.19 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5399999833, 4s@0.56, 4s@0.54509684, 5s@0.58, 10s@0.62, 11s@0.6199999958, 14s@0.62, 14s@0.62, 14s@0.62, 16s@0.63, 17s@0.64, 17s@0.64 ...

### 2026-10-05T09:15Z (market 5274221, result down)
Scored: p1 up filled at 80s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5, 2s@0.49, 4s@0.4899999944, 4s@0.4599997976, 4s@0.487804878, 5s@0.461568, 5s@0.46, 5s@0.4599997976, 5s@0.459999988, 5s@0.46, 7s@0.4699999918, 7s@0.47 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.55, 4s@0.51, 5s@0.549999945, 5s@0.5418, 5s@0.549999945, 7s@0.5399999568, 8s@0.5399999568, 8s@0.5399999568, 8s@0.54, 8s@0.5399999821, 11s@0.54, 11s@0.54 ...


_Updated 2026-10-05 10:27Z_
