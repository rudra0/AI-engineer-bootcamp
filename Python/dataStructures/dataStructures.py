def list_example() -> None:
    fruits = ["apple", "banana", "orange"]
    fruits.append("mango")
    print("List example:", fruits)


def tuple_example() -> None:
    coordinates = (10, 20)
    print("Tuple example:", coordinates)


def set_example() -> None:
    unique_numbers = {1, 2, 2, 3, 3, 4}
    print("Set example:", unique_numbers)


def dict_example() -> None:
    inventory = {"apple": 10, "banana": 5, "orange": 8}
    inventory["mango"] = 2
    print("Dict example:", inventory)
    print("Bananas in stock:", inventory["banana"])


def main() -> None:
    list_example()
    tuple_example()
    set_example()
    dict_example()


if __name__ == "__main__":
    main()
