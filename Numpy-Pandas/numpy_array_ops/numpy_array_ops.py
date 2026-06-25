"""NumPy array operations examples.

Run: python3 numpy_array_ops.py
"""
import numpy as np


def main() -> None:
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("a + b:", a + b)
    print("a * 2:", a * 2)
    print("dot(a, b):", np.dot(a, b))

    # Broadcasting example
    c = np.arange(6).reshape(2, 3)
    print("c:\n", c)
    print("c + a (broadcasted):\n", c + a)

    # Reductions and stacking
    print("Sum axis=0:", c.sum(axis=0))
    print("vstack:\n", np.vstack([a, a]))


if __name__ == "__main__":
    main()
