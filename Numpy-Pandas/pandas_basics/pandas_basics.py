"""Pandas basics examples.

Run: python3 pandas_basics.py
"""
import pandas as pd


def main() -> None:
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 22],
        "score": [85.0, 92.5, 78.0],
    })
    print("DataFrame:\n", df)
    print("\nInfo:\n")
    print(df.info())
    print("\nDescribe:\n", df.describe())
    print("\nSelect names where age > 23:\n", df[df["age"] > 23]["name"].tolist())


if __name__ == "__main__":
    main()
