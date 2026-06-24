class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return f"{self.name} makes a sound."


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says woof!"


class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says meow!"


def main() -> None:
    animals = [Dog("Buddy"), Cat("Whiskers")]
    for animal in animals:
        print(animal.speak())


if __name__ == "__main__":
    main()
