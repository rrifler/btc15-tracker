"""Re-score windows closed in the last lookback_hours. Idempotent: rows replace by window start."""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import markets, report, runner  # noqa: E402

PAPER = "results/windows.csv"
START = "results/paper_start.txt"


def paper_start():
    """Paper run begins at the first window after the first run of this job. Stored so it never moves."""
    if os.path.exists(START):
        with open(START) as f:
            return int(f.read().strip())
    ws = markets.window_floor(time.time()) + 900
    os.makedirs("results", exist_ok=True)
    with open(START, "w") as f:
        f.write(str(ws))
    return ws


def main():
    cfg = runner.load_config()
    start = paper_start()
    rows = report.load(PAPER)
    samples = {}
    for ws in markets.windows_since(cfg["lookback_hours"]):
        if ws < start:
            continue
        row, sample = runner.score_window(ws, cfg)
        rows[ws] = row
        if sample:
            samples[ws] = sample
    report.rebuild(rows, cfg)
    report.save(PAPER, rows)
    bt = report.load("results/backtest_windows.csv")
    report.rebuild(bt, cfg)
    report.write_summary("results/summary.md", cfg, bt, rows, [runner.SOURCE],
                         runner.spot_text(rows, samples, cfg))
    if rows:
        m = report.metrics(rows, cfg)
        print(f"paper windows: {len(rows)} fills={m['fills']} profit={m['profit']:.2f}")
    else:
        print("paper windows: 0 (first window starts later)")


if __name__ == "__main__":
    main()
