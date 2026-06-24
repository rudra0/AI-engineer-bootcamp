def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def main() -> None:
    print("Factorial of 5:", factorial(5))
    print("Fibonacci sequence:")
    print([fibonacci(i) for i in range(8)])


if __name__ == "__main__":
    main()
