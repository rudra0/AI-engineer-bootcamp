numbers = list(range(1, 11))

squares = [x * x for x in numbers]
filtered = [x for x in numbers if x % 2 == 0]
word_lengths = {word: len(word) for word in ["python", "learn", "code"]}
unique_chars = {char for char in "python"}


def main() -> None:
    print("Numbers:", numbers)
    print("Squares:", squares)
    print("Even numbers:", filtered)
    print("Word lengths:", word_lengths)
    print("Unique chars:", unique_chars)


if __name__ == "__main__":
    main()
