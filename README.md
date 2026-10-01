# btc15-tracker

Tests the Polymarket 15-minute BTC "25c to 45c" strategy on real data. No money moves until you turn it on.

- `results/summary.md` is the report. Read it in the GitHub app.
- Backtest: run the `backtest` workflow once. Paper tracking runs hourly on its own.
- `trader` workflow is a dry run unless the repo variable `LIVE_TRADING` is `true`.
- Keys: only as GitHub secrets `PM_KEY_ID` and `PM_SECRET`. Never paste them anywhere else.

Data source for the backtest and paper run is the international exchange (`INTL_PROXY`), because the US
gateway publishes no public trade history.
