"""Solution for Problem 3 — Missing values and filtering (pandas)."""
import pandas as pd


def process(df: pd.DataFrame) -> pd.DataFrame:
    if "score" in df.columns:
        df["score"] = df["score"].astype(float)
        mean_score = df["score"].mean()
        df["score"] = df["score"].fillna(mean_score)
    res = df[df["age"] >= 18].sort_values("score", ascending=False)
    return res.reset_index(drop=True)


def main() -> None:
    data = {"name": ["A", "B", "C"], "age": [17, 20, 22], "score": [80, None, 90]}
    df = pd.DataFrame(data)
    print("Input:\n", df)
    print("Processed:\n", process(df))


if __name__ == "__main__":
    main()
