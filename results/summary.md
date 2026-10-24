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
- Windows scored: 2248; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.9% of scored windows had a fill (251 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 218/471 = 46.3%. The verdict uses strict.

## Spot-checked windows

### 2026-10-24T07:30Z (market 6076242, result up)
Scored: p1 up filled at 80s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 80s@0.25, 80s@0.24, 242s@0.49, 242s@0.4799999846, 242s@0.4699999467, 242s@0.4599999938, 242s@0.45, 243s@0.5, 243s@0.5, 243s@0.5, 243s@0.5, 243s@0.48 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.57, 3s@0.5699999478, 6s@0.57, 6s@0.56, 8s@0.57, 9s@0.5699999886, 21s@0.65, 21s@0.65, 21s@0.6499999665, 21s@0.6199999575, 21s@0.6099999913, 21s@0.61 ...

### 2026-10-24T08:00Z (market 6076659, result up)
Scored: p1 down filled at 87s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 9s@0.5799999768, 14s@0.58, 17s@0.5699999795, 18s@0.559999776, 23s@0.62, 36s@0.64, 36s@0.64, 39s@0.6487533275, 39s@0.6599999504, 42s@0.6768957551, 42s@0.6799999523, 42s@0.6699999163 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 59s@0.25, 59s@0.25, 63s@0.25, 65s@0.25, 66s@0.25, 87s@0.24, 89s@0.24, 90s@0.25, 90s@0.25, 123s@0.24, 125s@0.24, 128s@0.24 ...

### 2026-10-24T09:00Z (market 6077400, result down)
Scored: p1 up filled at 111s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 9s@0.4599999879, 9s@0.4599999944, 17s@0.4599999034, 18s@0.46, 30s@0.4799999939, 57s@0.45, 60s@0.4599999034, 63s@0.45, 107s@0.25, 108s@0.25, 111s@0.2375, 116s@0.24 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 41s@0.53, 41s@0.53, 45s@0.559999776, 72s@0.56612, 80s@0.6899999894, 80s@0.6899999616, 80s@0.6899999846, 80s@0.6899999491, 80s@0.7, 80s@0.6899999508, 80s@0.58, 81s@0.67 ...


_Updated 2026-10-24 13:34Z_
