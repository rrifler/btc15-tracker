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
- Windows scored: 1532; excluded: 1 (trades_truncated: 1)
- Fill rate: 17.5% of scored windows had a fill (94 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 135/298 = 45.3%. The verdict uses strict.

## Spot-checked windows

### 2026-10-16T22:30Z (market 5763282, result up)
Scored: p1 down filled at 72s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.56, 6s@0.559999776, 9s@0.4699999493, 11s@0.4899999809, 11s@0.47, 11s@0.4699999493, 12s@0.5, 12s@0.4899999183, 14s@0.5, 14s@0.5, 14s@0.5, 14s@0.5 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.45, 8s@0.49, 8s@0.4899999984, 8s@0.45, 8s@0.45, 9s@0.5399999568, 11s@0.539999986, 14s@0.5199999955, 20s@0.49, 23s@0.49, 23s@0.47, 69s@0.25 ...

### 2026-10-17T00:30Z (market 5764977, result down)
Scored: p1 down filled at 24s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5217319455, 2s@0.585, 2s@0.57, 5s@0.64, 8s@0.6662962963, 9s@0.7, 18s@0.7, 20s@0.7199998443, 21s@0.75, 21s@0.75, 23s@0.77, 26s@0.77 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 24s@0.2422503443, 27s@0.219999999, 29s@0.2299999993, 30s@0.229999998, 39s@0.209999993, 54s@0.2, 54s@0.2, 54s@0.2, 54s@0.2, 56s@0.2099999895, 57s@0.21, 57s@0.2099999895 ...

### 2026-10-17T02:00Z (market 5765523, result up)
Scored: p1 down filled at 119s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.52, 2s@0.55, 2s@0.55, 2s@0.55, 3s@0.5699998137, 3s@0.57, 3s@0.56, 3s@0.568, 5s@0.6, 5s@0.6, 5s@0.6, 5s@0.593997599 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 26s@0.45, 33s@0.45, 44s@0.45, 45s@0.4699999944, 45s@0.4616975643, 51s@0.4699999944, 51s@0.469999998, 114s@0.25, 119s@0.2113257805, 122s@0.2299999986, 122s@0.2223841044, 122s@0.2299999993 ...


_Updated 2026-10-17 02:34Z_
