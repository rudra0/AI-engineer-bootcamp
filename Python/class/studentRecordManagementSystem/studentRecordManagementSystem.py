# Student Record Management System using classes

class Student:
    def __init__(self, name: str, age: int, grade: str):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, age={self.age}, grade={self.grade!r})"


class StudentRecordManagementSystem:
    def __init__(self):
        self.students: list[Student] = []

    def add_student(self, name: str, age: int, grade: str) -> None:
        student = Student(name, age, grade)
        self.students.append(student)

    def display_students(self) -> None:
        if not self.students:
            print("No students available.")
            return
        print("Student records:")
        for student in self.students:
            print(f"- {student.name}, Age: {student.age}, Grade: {student.grade}")

    def find_student(self, name: str):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None


def run_example() -> None:
    system = StudentRecordManagementSystem()
    system.add_student("Alice", 20, "A")
    system.add_student("Bob", 22, "B")
    system.add_student("Charlie", 19, "A+")

    system.display_students()

    print("\nSearching for Bob...")
    found = system.find_student("Bob")
    if found:
        print(f"Found: {found.name}, Grade: {found.grade}")
    else:
        print("Student not found.")


if __name__ == "__main__":
    run_example()
