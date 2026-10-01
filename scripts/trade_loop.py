"""Run the trader for up to 5h50m. Dry run unless env LIVE_TRADING is exactly "true"."""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import pm_us, runner  # noqa: E402
from src.trader import Halt, Trader  # noqa: E402

RUN_SECONDS = 5 * 3600 + 50 * 60


def main():
    cfg = runner.load_config()
    live = os.environ.get("LIVE_TRADING", "").strip().lower() == "true"
    if live:
        client = pm_us.LiveClient()
    else:
        client = pm_us.DryRunClient(balance=cfg["bankroll_start"])
    print(f"mode={client.mode}", flush=True)
    trader = Trader(client, cfg)
    try:
        trader.run(until=time.time() + RUN_SECONDS)
    except Halt as e:
        print(f"HALTED: {e}", flush=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
