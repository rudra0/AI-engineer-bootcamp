"""Solution for Problem 5 — Join and compute metric (pandas)."""
import pandas as pd


def user_transaction_share(users: pd.DataFrame, tx: pd.DataFrame) -> pd.DataFrame:
    merged = tx.merge(users, on="user_id", how="left")
    totals = merged.groupby(["user_id", "name"]).agg(user_total=("amount", "sum")).reset_index()
    global_total = totals["user_total"].sum()
    totals["share"] = totals["user_total"] / global_total
    return totals.sort_values("user_total", ascending=False).reset_index(drop=True)


def main() -> None:
    users = pd.DataFrame({"user_id": [1, 2], "name": ["Alice", "Bob"]})
    tx = pd.DataFrame({"user_id": [1, 2, 1], "amount": [100, 50, 25]})
    print("Users:\n", users)
    print("Transactions:\n", tx)
    print("Result:\n", user_transaction_share(users, tx))


if __name__ == "__main__":
    main()
