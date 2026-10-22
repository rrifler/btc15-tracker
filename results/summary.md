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
- Windows scored: 2085; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.7% of scored windows had a fill (216 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 198/432 = 45.8%. The verdict uses strict.

## Spot-checked windows

### 2026-10-22T16:30Z (market 6016119, result down)
Scored: p1 up filled at 101s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5799999768, 3s@0.549999945, 29s@0.45, 29s@0.45, 30s@0.4599999653, 93s@0.25, 96s@0.25, 101s@0.23, 116s@0.2099999983, 122s@0.1814278948, 144s@0.15, 150s@0.1699999983 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 3s@0.4599999968, 3s@0.4599999968, 3s@0.46, 3s@0.4599999921, 3s@0.46, 3s@0.4599999968, 3s@0.46, 3s@0.4599999968, 3s@0.45, 5s@0.5099999516, 5s@0.5099999137 ...

### 2026-10-22T17:15Z (market 6017730, result up)
Scored: p1 down filled at 119s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5461766658, 5s@0.5399999568, 6s@0.5499999406, 6s@0.5499999518, 8s@0.55, 9s@0.55, 9s@0.5699999886, 9s@0.55, 11s@0.59999988, 15s@0.63, 15s@0.62, 15s@0.62 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4599997976, 72s@0.4599999928, 119s@0.219999978, 123s@0.21, 126s@0.2099999895, 141s@0.1499999933, 143s@0.14, 146s@0.1499999925, 146s@0.14, 147s@0.1499999933, 147s@0.1499999925, 150s@0.1699999933 ...

### 2026-10-22T20:15Z (market 6025903, result down)
Scored: p1 up filled at 66s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.4799998464, 66s@0.2399999852, 75s@0.25, 75s@0.25, 162s@0.25, 185s@0.2, 200s@0.2, 216s@0.16, 218s@0.16, 219s@0.16, 224s@0.16, 227s@0.18 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.4974602312, 0s@0.51, 2s@0.51, 2s@0.51, 3s@0.5199998891, 3s@0.52, 3s@0.51, 3s@0.52, 5s@0.54, 5s@0.52, 6s@0.57, 6s@0.5699999886 ...


_Updated 2026-10-22 20:35Z_
