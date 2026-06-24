def even_numbers(limit: int):
    for n in range(0, limit + 1, 2):
        yield n


def main() -> None:
    print("Even numbers generator:")
    for value in even_numbers(10):
        print(value, end=" ")
    print()


if __name__ == "__main__":
    main()
