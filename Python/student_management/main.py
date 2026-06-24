import json
from pathlib import Path


class Student:
    def __init__(self, student_id: int, name: str, marks: float):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def to_dict(self) -> dict:
        return {
            "student_id": self.student_id,
            "name": self.name,
            "marks": self.marks,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        return cls(
            student_id=int(data.get("student_id", data.get("id", 0))),
            name=str(data.get("name", "")),
            marks=float(data.get("marks", 0.0)),
        )


class StudentManager:
    def __init__(self, data_file: Path):
        self.data_file = data_file
        self.students: list[Student] = []
        self.load_data()

    def add_student(self, student: Student) -> None:
        if self.search_student(student.student_id) is not None:
            print(f"Student ID {student.student_id} already exists.")
            return
        self.students.append(student)
        print(f"Student {student.name} added.")

    def view_students(self) -> None:
        if not self.students:
            print("No students available.")
            return
        print("\nStudent records:")
        for student in self.students:
            print(f"- ID: {student.student_id}, Name: {student.name}, Marks: {student.marks}")

    def search_student(self, student_id: int):
        return next((student for student in self.students if student.student_id == student_id), None)

    def delete_student(self, student_id: int) -> None:
        student = self.search_student(student_id)
        if student is None:
            print("Student not found.")
            return
        self.students.remove(student)
        print(f"Student {student.name} deleted.")

    def save_data(self) -> None:
        try:
            self.data_file.write_text(json.dumps([student.to_dict() for student in self.students], indent=2))
            print(f"Student data saved to {self.data_file.name}.")
        except OSError as exc:
            print(f"Error saving data: {exc}")

    def load_data(self) -> None:
        if not self.data_file.exists():
            self.students = []
            return
        try:
            raw_text = self.data_file.read_text()
            if not raw_text.strip():
                self.students = []
                return
            data = json.loads(raw_text)
            self.students = [Student.from_dict(item) for item in data]
            print(f"Loaded {len(self.students)} student(s) from {self.data_file.name}.")
        except (json.JSONDecodeError, OSError, TypeError, ValueError) as exc:
            print(f"Error loading data: {exc}")
            self.students = []


def read_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        if raw == "":
            print("Input cannot be empty. Please enter a number.")
            continue
        try:
            return int(raw)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def read_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        if raw == "":
            print("Input cannot be empty. Please enter a number.")
            continue
        try:
            return float(raw)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main() -> None:
    data_file = Path(__file__).resolve().parent / "students.json"
    manager = StudentManager(data_file)

    while True:
        print("\n===== MENU =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Save")
        print("6. Exit")

        choice = input("Enter Choice: ").strip()
        if choice == "1":
            student_id = read_int("ID: ")
            name = input("Name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            marks = read_float("Marks: ")
            manager.add_student(Student(student_id, name, marks))

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            student_id = read_int("Enter ID: ")
            student = manager.search_student(student_id)
            if student is None:
                print("Student not found.")
            else:
                print(f"Found: ID: {student.student_id}, Name: {student.name}, Marks: {student.marks}")

        elif choice == "4":
            student_id = read_int("Enter ID: ")
            manager.delete_student(student_id)

        elif choice == "5":
            manager.save_data()

        elif choice == "6":
            manager.save_data()
            print("Goodbye")
            break

        else:
            print("Invalid choice. Please select a valid menu option.")


if __name__ == "__main__":
    main()
