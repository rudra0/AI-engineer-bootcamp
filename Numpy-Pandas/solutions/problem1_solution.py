"""Solution for Problem 1 — Normalize array."""
import numpy as np


def normalize(arr: np.ndarray) -> np.ndarray:
    arr = np.asarray(arr, dtype=float)
    mn = arr.min()
    mx = arr.max()
    if np.isclose(mn, mx):
        return np.zeros_like(arr)
    return (arr - mn) / (mx - mn)


def main() -> None:
    example = np.array([10, 20, 30])
    print("Input:", example)
    print("Normalized:", normalize(example))


if __name__ == "__main__":
    main()
