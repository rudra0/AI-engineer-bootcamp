class NegativeNumberError(ValueError):
    pass


def safe_divide(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return 0.0


def parse_positive_int(value: str) -> int:
    try:
        number = int(value)
    except ValueError:
        raise ValueError("Input must be a whole number")
    if number < 0:
        raise NegativeNumberError("Value must be positive")
    return number


def main() -> None:
    values = ["5", "0", "abc", "-3"]
    for text in values:
        try:
            number = parse_positive_int(text)
            result = safe_divide(10, number)
            print(f"10 / {number} = {result}")
        except NegativeNumberError as exc:
            print("NegativeNumberError:", exc)
        except ValueError as exc:
            print("ValueError:", exc)


if __name__ == "__main__":
    main()
