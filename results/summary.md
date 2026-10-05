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
- Windows scored: 377; excluded: 0
- Fill rate: 17.2% of scored windows had a fill (0 too small)
- Fills that reached 45c: 32 of 65 = 49.2% (95% range 37.5% to 61.1%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-5.85 (balance $14.15 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 32/65 = 49.2%; touch 36/70 = 51.4%. The verdict uses strict.

## Spot-checked windows

### 2026-10-04T19:30Z (market 5247174, result down)
Scored: p1 down filled at 119s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.47, 1s@0.4699999691, 2s@0.4899999654, 2s@0.4899999654, 2s@0.47, 2s@0.4777874485, 2s@0.47, 2s@0.46, 2s@0.469999998, 2s@0.47, 4s@0.49, 4s@0.49 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.52, 4s@0.5199999792, 4s@0.5199999792, 5s@0.52, 5s@0.5199999792, 5s@0.5199999792, 5s@0.5199999792, 5s@0.52, 7s@0.5199999792, 7s@0.52, 7s@0.52, 7s@0.52 ...

### 2026-10-04T22:00Z (market 5255728, result up)
Scored: p1 down filled at 28s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5899999797, 2s@0.5899999934, 2s@0.59, 4s@0.6199999676, 4s@0.5701282917, 4s@0.6032885906, 5s@0.62, 5s@0.6199999778, 5s@0.62, 7s@0.6599999291, 7s@0.65, 7s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 28s@0.23, 29s@0.22, 31s@0.2, 31s@0.2, 32s@0.21, 32s@0.2, 32s@0.2, 34s@0.2, 34s@0.2299999992, 35s@0.22, 35s@0.2292520305, 38s@0.2 ...

### 2026-10-04T22:15Z (market 5255913, result down)
Scored: p1 down filled at 82s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4634622166, 4s@0.45, 5s@0.45, 5s@0.45, 5s@0.45, 5s@0.45, 7s@0.45, 7s@0.45, 8s@0.45, 10s@0.45, 10s@0.45, 13s@0.45 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5599999851, 4s@0.56, 4s@0.56, 4s@0.5558823366, 4s@0.5499999995, 4s@0.5399999568, 5s@0.5599999955, 5s@0.5599999642, 5s@0.559999776, 5s@0.56, 7s@0.5599999804, 7s@0.56 ...

### 2026-10-05T00:00Z (market 5262302, result down)
Scored: p1 up filled at 71s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 26s@0.45, 71s@0.24, 71s@0.2361904762, 71s@0.2299999854, 73s@0.2399999981, 73s@0.24, 73s@0.24, 73s@0.23, 73s@0.2399999931, 73s@0.2464025232, 73s@0.24, 85s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.49, 2s@0.560338951, 4s@0.58, 4s@0.55, 4s@0.5479166667, 5s@0.603468, 5s@0.6, 5s@0.59999988, 5s@0.6, 5s@0.5899999841, 5s@0.59, 7s@0.6099999488 ...

### 2026-10-05T01:00Z (market 5262755, result down)
Scored: p1 up filled at 94s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 94s@0.2099999983, 94s@0.2199999974, 97s@0.17, 98s@0.16, 98s@0.1623342174, 106s@0.16, 109s@0.17, 118s@0.1945945946, 119s@0.2099999895, 133s@0.1799999948, 146s@0.18, 146s@0.17 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5699999886, 5s@0.6099998597, 5s@0.6099998597, 5s@0.61, 5s@0.57, 5s@0.609999986, 7s@0.62, 7s@0.64, 7s@0.64, 7s@0.63, 7s@0.6299998362, 7s@0.61 ...


_Updated 2026-10-05 01:24Z_
