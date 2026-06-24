from pathlib import Path

FILE_PATH = Path("sample_data.txt")


def write_sample_data() -> None:
    lines = [
        "Python file I/O example\n",
        "This file was written by a Python script.\n",
        "File I/O helps you save and read data.\n",
    ]
    FILE_PATH.write_text("".join(lines))


def read_sample_data() -> list[str]:
    return FILE_PATH.read_text().splitlines()


def main() -> None:
    write_sample_data()
    print(f"Wrote sample file: {FILE_PATH.name}")
    print("Contents:")
    for line in read_sample_data():
        print("-", line)


if __name__ == "__main__":
    main()
