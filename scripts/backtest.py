"""Score the last N closed windows. Writes results/backtest_windows.csv and refreshes summary.md."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import markets, report, runner  # noqa: E402

BT = "results/backtest_windows.csv"


def main():
    cfg = runner.load_config()
    wins = markets.closed_windows(cfg["backtest_windows"])
    rows, samples = {}, {}
    for i, ws in enumerate(wins):
        row, sample = runner.score_window(ws, cfg)
        rows[ws] = row
        if sample:
            samples[ws] = sample
        if i % 50 == 0:
            print(f"{i}/{len(wins)} scored", flush=True)
    report.rebuild(rows, cfg)
    report.save(BT, rows)
    paper = report.load("results/windows.csv")
    report.rebuild(paper, cfg)
    spot = runner.spot_text(rows, samples, cfg)
    verdict = report.write_summary("results/summary.md", cfg, rows, paper, [runner.SOURCE], spot)
    m = report.metrics(rows, cfg)
    total = m["scored"] + m["excluded"]
    print(f"verdict={verdict} scored={m['scored']}/{total} fills={m['fills']} hit={m['hit_rate']:.3f} "
          f"profit={m['profit']:.2f}")
    if total and m["scored"] / total < 0.95:
        print("WARNING: fewer than 95% of windows scored", m["reasons"])


if __name__ == "__main__":
    main()
