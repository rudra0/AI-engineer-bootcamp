"""Solution for Problem 4 — Group and aggregate (pandas)."""
import pandas as pd


def aggregate_by_category(df: pd.DataFrame) -> pd.DataFrame:
    grouped = df.groupby("category").agg(total_amount=("amount", "sum"), avg_amount=("amount", "mean"))
    return grouped.sort_values("total_amount", ascending=False).reset_index()


def main() -> None:
    df = pd.DataFrame({
        "user_id": [1, 2, 1, 3],
        "category": ["food", "travel", "food", "travel"],
        "amount": [10, 20, 5, 15],
    })
    print("Input:\n", df)
    print("Aggregated:\n", aggregate_by_category(df))


if __name__ == "__main__":
    main()
