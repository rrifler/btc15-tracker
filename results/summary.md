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
- Windows scored: 2699; excluded: 2 (trades_truncated: 2)
- Fill rate: 19.2% of scored windows had a fill (344 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 268/576 = 46.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-29T03:15Z (market 6330319, result down)
Scored: p1 down filled at 32s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.59, 2s@0.59, 2s@0.5868, 2s@0.61, 4s@0.5999999815, 4s@0.6099999831, 4s@0.5999999815, 4s@0.5999999815, 4s@0.6, 5s@0.6099999713, 7s@0.61, 8s@0.6664994584 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 32s@0.22, 32s@0.2199999974, 40s@0.2299999517, 40s@0.2277227696, 56s@0.2299999983, 59s@0.2299999782, 59s@0.229999987, 65s@0.24, 65s@0.21, 119s@0.47, 119s@0.47, 121s@0.47 ...

### 2026-10-29T04:45Z (market 6332174, result up)
Scored: p1 down filled at 112s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.45, 2s@0.45, 5s@0.4599999563, 5s@0.4599999034, 16s@0.4699999953, 16s@0.45, 17s@0.46, 35s@0.4899999953, 35s@0.45, 37s@0.5073432519, 37s@0.48, 37s@0.49 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.55, 5s@0.55, 5s@0.57, 5s@0.57, 5s@0.5645549383, 5s@0.5706642857, 5s@0.57, 5s@0.56, 8s@0.5777598566, 17s@0.5399999857, 17s@0.5399999972, 19s@0.54 ...

### 2026-10-29T07:30Z (market 6336009, result up)
Scored: p1 down filled at 115s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.5299998463, 10s@0.5, 10s@0.5099999442, 16s@0.4799999846, 17s@0.51, 19s@0.5089117108, 19s@0.5099999215, 19s@0.51, 28s@0.4799999616, 29s@0.48, 29s@0.4799998464, 29s@0.46 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.4799998464, 5s@0.4799999985, 7s@0.48, 8s@0.48, 10s@0.5, 10s@0.5, 10s@0.5113982487, 10s@0.5099999454, 10s@0.5, 10s@0.5, 10s@0.5, 10s@0.4879166667 ...

### 2026-10-29T08:00Z (market 6336542, result up)
Scored: p1 down filled at 85s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.45, 8s@0.45, 10s@0.4690618748, 11s@0.54, 11s@0.5, 13s@0.52, 13s@0.55, 13s@0.55, 19s@0.5699999886, 19s@0.5699999214, 20s@0.57, 22s@0.6099999869 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5599999642, 2s@0.5414876508, 5s@0.56, 7s@0.559999776, 11s@0.48, 11s@0.5099999397, 13s@0.49, 13s@0.48, 85s@0.239999989, 86s@0.2399999923, 86s@0.2399999981, 89s@0.25 ...


_Updated 2026-10-29 08:23Z_
