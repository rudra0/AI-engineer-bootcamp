"""Pandas groupby and aggregation examples.

Run: python3 pandas_groupby.py
"""
import pandas as pd


def main() -> None:
    df = pd.DataFrame({
        "city": ["A", "B", "A", "B", "A"],
        "score": [10, 20, 30, 40, 50],
        "people": [1, 2, 1, 3, 2],
    })
    print("DataFrame:\n", df)
    agg = df.groupby("city")["score"].agg(["sum", "mean", "count"])
    print("\nAggregated:\n", agg)

    # groupby multiple columns and custom aggregation
    multi = df.groupby("city").agg(total_score=("score", "sum"), avg_people=("people", "mean"))
    print("\nMulti-agg:\n", multi)


if __name__ == "__main__":
    main()
