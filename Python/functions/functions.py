def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Negative numbers are not allowed")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main() -> None:
    print(greet("Learner"))
    values = [10, 20, 30, 40]
    print("Values:", values)
    print("Average:", calculate_average(values))
    print("5! =", factorial(5))


if __name__ == "__main__":
    main()
