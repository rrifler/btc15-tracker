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
- Windows scored: 865; excluded: 0
- Fill rate: 16.8% of scored windows had a fill (0 too small)
- Fills that reached 45c: 68 of 145 = 46.9% (95% range 39.0% to 55.0%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.05 (balance $7.95 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 68/145 = 46.9%; touch 75/158 = 47.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-09T22:15Z (market 5444396, result up)
Scored: p1 down filled at 100s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5399999568, 4s@0.5399999568, 5s@0.5599999946, 11s@0.56, 11s@0.56, 13s@0.6099999615, 13s@0.61, 13s@0.61, 13s@0.6099999581, 13s@0.559999776, 14s@0.6099999801, 14s@0.6099998597 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.46, 4s@0.47, 5s@0.47, 86s@0.25, 100s@0.17, 106s@0.18, 125s@0.1799999964, 131s@0.1799999856, 137s@0.17, 137s@0.17, 137s@0.17, 139s@0.17 ...

### 2026-10-09T22:30Z (market 5444802, result up)
Scored: p1 down filled at 97s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 26s@0.52, 44s@0.52, 44s@0.5199999502, 55s@0.5199999956, 56s@0.52, 73s@0.6001612368, 73s@0.59, 73s@0.59, 73s@0.54, 74s@0.6254562439, 74s@0.6099999488, 74s@0.62 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.48, 2s@0.49, 5s@0.4939280702, 13s@0.4599997976, 34s@0.49, 97s@0.22, 101s@0.2299999987, 103s@0.23, 121s@0.219999978, 133s@0.19, 134s@0.19, 134s@0.19 ...


_Updated 2026-10-10 03:35Z_
