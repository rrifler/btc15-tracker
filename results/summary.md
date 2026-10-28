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
- Windows scored: 2638; excluded: 2 (trades_truncated: 2)
- Fill rate: 19.2% of scored windows had a fill (333 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 261/564 = 46.3%. The verdict uses strict.

## Spot-checked windows

### 2026-10-28T10:15Z (market 6295202, result up)
Scored: p1 down filled at 91s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5599998952, 5s@0.56, 13s@0.5599999961, 14s@0.6099999488, 14s@0.6099999968, 14s@0.5599999686, 14s@0.56, 14s@0.59, 14s@0.58, 14s@0.56, 14s@0.56, 14s@0.5599999923 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 49s@0.457951651, 49s@0.45, 50s@0.48, 52s@0.47, 55s@0.4799999939, 58s@0.486959707, 58s@0.4799999947, 58s@0.47, 58s@0.4799999616, 59s@0.5, 91s@0.2316786205, 91s@0.2399999923 ...

### 2026-10-28T13:45Z (market 6299264, result down)
Scored: p1 up filled at 107s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 14s@0.49, 14s@0.49, 14s@0.49, 19s@0.45, 28s@0.45, 107s@0.2, 107s@0.2, 112s@0.2, 116s@0.17, 116s@0.1622222222, 116s@0.18, 116s@0.16 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.53, 10s@0.52, 16s@0.52, 19s@0.5599999328, 19s@0.55, 20s@0.56, 32s@0.52, 49s@0.6001612368, 62s@0.64, 62s@0.6199998878, 65s@0.66, 65s@0.66 ...

### 2026-10-28T14:15Z (market 6299807, result down)
Scored: p1 up filled at 118s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.4599997976, 13s@0.4599999986, 14s@0.46, 14s@0.46, 14s@0.46, 19s@0.5, 19s@0.5, 19s@0.51, 23s@0.51, 28s@0.46, 94s@0.25, 94s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.5268389544, 5s@0.55, 17s@0.5099998215, 19s@0.47, 20s@0.469999906, 32s@0.55, 34s@0.55, 37s@0.57, 40s@0.6, 40s@0.58, 44s@0.62, 46s@0.62 ...

### 2026-10-28T15:00Z (market 6300794, result up)
Scored: p1 down filled at 40s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.5499999861, 2s@0.5499999214, 4s@0.55, 4s@0.55, 4s@0.5899999381, 5s@0.6199999449, 5s@0.59, 13s@0.64, 14s@0.66, 19s@0.66, 20s@0.69, 20s@0.6899999808 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 40s@0.23, 41s@0.2399999808, 43s@0.25, 43s@0.24, 44s@0.25, 44s@0.25, 46s@0.24, 49s@0.25, 71s@0.25, 74s@0.25, 76s@0.24, 79s@0.25 ...

### 2026-10-28T15:30Z (market 6301049, result down)
Scored: p1 up filled at 73s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 73s@0.2199999974, 76s@0.1899999962, 79s@0.1699999983, 83s@0.149999997, 83s@0.16, 88s@0.1499999925, 88s@0.15, 88s@0.15, 91s@0.12, 94s@0.11, 94s@0.11, 95s@0.109999989 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.59999988, 5s@0.63, 7s@0.6299998362, 10s@0.629999952, 10s@0.629999997, 19s@0.63, 28s@0.63, 47s@0.6499999511, 47s@0.6499999264, 47s@0.6799999819, 47s@0.65, 47s@0.65 ...


_Updated 2026-10-28 16:35Z_
