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
- Windows scored: 637; excluded: 0
- Fill rate: 16.5% of scored windows had a fill (0 too small)
- Fills that reached 45c: 45 of 105 = 42.9% (95% range 33.8% to 52.4%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.40 (balance $7.60 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 45/105 = 42.9%; touch 51/115 = 44.3%. The verdict uses strict.

## Spot-checked windows

### 2026-10-07T12:00Z (market 5373370, result down)
Scored: p1 up filled at 86s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.4899999584, 5s@0.4899998383, 8s@0.4899999824, 16s@0.46, 19s@0.5499999214, 19s@0.52, 26s@0.5665703726, 31s@0.5599999955, 34s@0.45, 86s@0.2199999895, 89s@0.21, 89s@0.21 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.52, 4s@0.51, 11s@0.52, 20s@0.46, 29s@0.45, 34s@0.5599999686, 34s@0.5199999377, 34s@0.4933399112, 34s@0.4899999183, 34s@0.4899998787, 34s@0.4899999183, 37s@0.5999999806 ...

### 2026-10-07T13:45Z (market 5374842, result up)
Scored: p1 up filled at 119s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5313100869, 2s@0.5199999718, 4s@0.5199999692, 4s@0.52, 4s@0.5299998463, 4s@0.5299999625, 4s@0.53, 4s@0.5299999868, 4s@0.53, 4s@0.5388158674, 4s@0.54, 5s@0.49 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.45, 2s@0.48, 2s@0.47, 2s@0.46, 2s@0.47, 2s@0.4595840086, 2s@0.45, 2s@0.45, 2s@0.45, 2s@0.45, 4s@0.4899998383, 4s@0.4899999322 ...

### 2026-10-07T15:30Z (market 5377101, result up)
Scored: p1 down filled at 80s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.55, 4s@0.549999945, 5s@0.546, 5s@0.549999945, 10s@0.5499999966, 13s@0.55, 16s@0.57, 16s@0.5699999886, 16s@0.55, 16s@0.55, 17s@0.58, 20s@0.5933333333 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.4599999387, 5s@0.46, 5s@0.4599999814, 5s@0.46, 11s@0.4599999819, 13s@0.4599999387, 80s@0.229999994, 82s@0.2099999969, 86s@0.2099999895, 91s@0.2, 95s@0.1899999842, 97s@0.1926284928 ...


_Updated 2026-10-07 18:29Z_
