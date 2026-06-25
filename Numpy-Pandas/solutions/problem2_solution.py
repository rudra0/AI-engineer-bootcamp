"""Solution for Problem 2 — Moving average."""
import numpy as np


def moving_average(arr: np.ndarray, k: int) -> np.ndarray:
    arr = np.asarray(arr, dtype=float)
    if k <= 0:
        raise ValueError("k must be > 0")
    out = np.full(arr.shape, np.nan)
    if k > len(arr):
        return out
    cumsum = np.cumsum(arr, dtype=float)
    out[k - 1 :] = (cumsum[k - 1 :] - np.concatenate(([0.0], cumsum[:-k]))) / k
    return out


def main() -> None:
    example = np.array([1, 2, 3, 4, 5])
    print("Input:", example)
    print("k=3 moving average:", moving_average(example, 3))


if __name__ == "__main__":
    main()
