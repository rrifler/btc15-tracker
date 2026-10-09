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
- Windows scored: 793; excluded: 0
- Fill rate: 16.1% of scored windows had a fill (0 too small)
- Fills that reached 45c: 58 of 128 = 45.3% (95% range 37.0% to 53.9%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.30 (balance $7.70 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 58/128 = 45.3%; touch 65/140 = 46.4%. The verdict uses strict.

## Spot-checked windows

### 2026-10-09T04:00Z (market 5422765, result up)
Scored: p1 down filled at 118s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.46, 3s@0.45, 3s@0.45, 3s@0.45, 4s@0.4569761986, 4s@0.47, 10s@0.45, 10s@0.48, 10s@0.45, 10s@0.4799999578, 10s@0.4707692018, 10s@0.45 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5299998463, 3s@0.5599999211, 3s@0.5399999568, 3s@0.5599999955, 3s@0.5599999955, 3s@0.5599999211, 3s@0.559999776, 4s@0.5699999886, 4s@0.54, 4s@0.54, 4s@0.5399999208, 4s@0.5399999705 ...

### 2026-10-09T06:45Z (market 5424777, result down)
Scored: p1 down filled at 67s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.55, 7s@0.5599999686, 7s@0.56, 9s@0.5599999686, 10s@0.549999945, 12s@0.5699999873, 12s@0.5605202572, 12s@0.57, 13s@0.57, 13s@0.5699999886, 16s@0.5899999797, 16s@0.6 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4599997976, 3s@0.4689993314, 3s@0.4710332871, 4s@0.4599997976, 4s@0.46, 4s@0.4602154071, 4s@0.4526724342, 4s@0.46, 6s@0.459999972, 6s@0.46, 6s@0.4599999828, 6s@0.46 ...

### 2026-10-09T09:00Z (market 5426092, result down)
Scored: p1 up filled at 66s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 57s@0.25, 58s@0.25, 66s@0.24, 73s@0.2199999974, 75s@0.2199999974, 76s@0.22, 84s@0.22, 85s@0.22, 87s@0.2017844444, 88s@0.2099999895, 93s@0.2099999895, 93s@0.2099999895 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5699999886, 1s@0.5699999886, 3s@0.5899998466, 3s@0.57, 3s@0.57, 4s@0.63, 4s@0.63, 4s@0.6, 4s@0.59, 4s@0.5899998466, 4s@0.59, 6s@0.64 ...


_Updated 2026-10-09 09:27Z_
