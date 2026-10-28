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
- Windows scored: 2658; excluded: 2 (trades_truncated: 2)
- Fill rate: 19.2% of scored windows had a fill (337 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 263/568 = 46.3%. The verdict uses strict.

## Spot-checked windows

### 2026-10-28T15:30Z (market 6301049, result down)
Scored: p1 up filled at 73s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 73s@0.2199999974, 76s@0.1899999962, 79s@0.1699999983, 83s@0.149999997, 83s@0.16, 88s@0.1499999925, 88s@0.15, 88s@0.15, 91s@0.12, 94s@0.11, 94s@0.11, 95s@0.109999989 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.59999988, 5s@0.63, 7s@0.6299998362, 10s@0.629999952, 10s@0.629999997, 19s@0.63, 28s@0.63, 47s@0.6499999511, 47s@0.6499999264, 47s@0.6799999819, 47s@0.65, 47s@0.65 ...

### 2026-10-28T16:00Z (market 6304473, result up)
Scored: p1 down filled at 80s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.5499999904, 5s@0.5099998215, 8s@0.5199999792, 10s@0.520727406, 13s@0.5299999797, 19s@0.53, 31s@0.54, 32s@0.6346153846, 32s@0.5799999768, 32s@0.54, 32s@0.5631067546, 34s@0.65 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5, 5s@0.5, 5s@0.5, 5s@0.5, 10s@0.4799999616, 19s@0.48, 23s@0.5, 23s@0.4958333333, 80s@0.2399999896, 82s@0.2399999901, 83s@0.2399999981, 85s@0.2466666667 ...

### 2026-10-28T17:00Z (market 6311765, result down)
Scored: p1 up filled at 61s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 61s@0.22, 65s@0.23, 92s@0.24, 101s@0.22, 101s@0.23, 103s@0.24, 103s@0.24, 103s@0.24, 109s@0.25, 109s@0.219999987, 116s@0.21, 119s@0.2299999782 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5699999436, 4s@0.6, 4s@0.62, 5s@0.67, 5s@0.65, 5s@0.65, 7s@0.66, 7s@0.67, 8s@0.68, 8s@0.67, 16s@0.6599999992, 16s@0.66 ...

### 2026-10-28T18:45Z (market 6318030, result down)
Scored: p1 up filled at 43s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 43s@0.2, 43s@0.2, 43s@0.2, 46s@0.2, 50s@0.2, 62s@0.21, 62s@0.2099999914, 64s@0.209999997, 64s@0.209999997, 67s@0.1979057592, 67s@0.2, 68s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.61, 4s@0.6099999736, 4s@0.6199998512, 4s@0.6199999749, 5s@0.61, 5s@0.6099999365, 8s@0.615, 8s@0.61, 13s@0.62, 14s@0.63, 14s@0.6502940689, 17s@0.64 ...

### 2026-10-28T20:00Z (market 6322959, result down)
Scored: p1 down filled at 68s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5501754077, 4s@0.55, 4s@0.56, 5s@0.5899999725, 5s@0.6, 8s@0.6, 8s@0.6, 8s@0.598, 8s@0.59, 11s@0.6, 13s@0.599999976, 13s@0.5999999754 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4599999387, 68s@0.2425, 70s@0.25, 74s@0.24, 80s@0.2, 80s@0.2, 82s@0.21, 82s@0.2, 83s@0.21543, 85s@0.25, 85s@0.23, 86s@0.25 ...


_Updated 2026-10-28 21:38Z_
