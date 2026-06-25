"""NumPy basics examples.

Run: python3 numpy_basics.py
"""
import numpy as np


def main() -> None:
    a = np.array([1, 2, 3])
    print("Array a:", a)
    b = np.arange(6).reshape(2, 3)
    print("Array b:\n", b)
    print("b.shape:", b.shape)
    print("b.dtype:", b.dtype)
    print("Mean across axis=1:", b.mean(axis=1))


if __name__ == "__main__":
    main()
