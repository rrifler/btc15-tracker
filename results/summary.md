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
- Windows scored: 525; excluded: 0
- Fill rate: 17.1% of scored windows had a fill (0 too small)
- Fills that reached 45c: 38 of 90 = 42.2% (95% range 32.5% to 52.5%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-11.80 (balance $8.20 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 38/90 = 42.2%; touch 43/99 = 43.4%. The verdict uses strict.

## Spot-checked windows

### 2026-10-06T08:00Z (market 5318206, result up)
Scored: p1 down filled at 109s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.4899998383, 4s@0.47, 4s@0.455, 6s@0.528280592, 6s@0.5066248802, 9s@0.5699999214, 10s@0.57, 12s@0.5799999848, 13s@0.58, 15s@0.58, 15s@0.58, 16s@0.59 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5588235245, 3s@0.57, 4s@0.52, 4s@0.5199999792, 4s@0.54, 6s@0.49, 6s@0.52, 6s@0.49, 40s@0.47, 109s@0.25, 109s@0.24, 115s@0.25 ...

### 2026-10-06T09:15Z (market 5319270, result down)
Scored: p1 down filled at 117s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5099999776, 4s@0.52, 7s@0.52, 19s@0.5199999792, 19s@0.52, 19s@0.5199999792, 22s@0.54, 22s@0.5379166667, 24s@0.6199998512, 24s@0.6082376632, 24s@0.62, 25s@0.6199999958 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5, 1s@0.5, 1s@0.5, 4s@0.4799998464, 4s@0.49, 4s@0.4899999584, 6s@0.48, 6s@0.49, 10s@0.4899999824, 18s@0.4899999824, 22s@0.4899999824, 117s@0.2199999998 ...

### 2026-10-06T11:15Z (market 5320544, result up)
Scored: p1 down filled at 45s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 37s@0.48, 37s@0.48, 37s@0.48, 43s@0.5025, 45s@0.75, 45s@0.751616341, 45s@0.75, 45s@0.75, 45s@0.75, 45s@0.75, 45s@0.7399999703, 45s@0.739999997 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.57, 0s@0.5781531532, 3s@0.56, 4s@0.5699999886, 4s@0.5799999768, 4s@0.57, 4s@0.58, 4s@0.58, 6s@0.5699999886, 6s@0.5699999886, 7s@0.57, 7s@0.57 ...


_Updated 2026-10-06 14:26Z_
