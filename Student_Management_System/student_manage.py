class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = {}

    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def show_result(self):
        print(f"\n👨‍🎓 Name: {self.name}")
        print(f"🆔 Roll Number: {self.roll_number}")
        if not self.marks:
            print("📄 No marks available.")
            return
        total = 0
        print("📊 Marks:")
        for subject, mark in self.marks.items():
            print(f"  - {subject}: {mark}")
            total += mark
        print(f"🔢 Total Marks: {total}")
        print(f"📈 Percentage: {total / len(self.marks):.2f}%")


class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, name, roll_number):
        if roll_number in self.students:
            print("⚠️ Student already exists!")
        else:
            self.students[roll_number] = Student(name, roll_number)
            print("✅ Student added successfully!")

    def add_student_marks(self, roll_number, subject, marks):
        student = self.students.get(roll_number)
        if student:
            student.add_marks(subject, marks)
            print("✅ Marks added successfully!")
        else:
            print("❌ Student not found!")

    def show_student_result(self, roll_number):
        student = self.students.get(roll_number)
        if student:
            student.show_result()
        else:
            print("❌ Student not found!")


if __name__ == "__main__":
    manager = StudentManager()

    while True:
        print("\n========== STUDENT RESULT SYSTEM ==========")
        print("1. Add New Student")
        print("2. Add Marks to Student")
        print("3. Show Student Result")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            roll = input("Enter roll number: ")
            manager.add_student(name, roll)

        elif choice == "2":
            roll = input("Enter student roll number: ")
            subject = input("Enter subject: ")
            marks = int(input("Enter marks: "))
            manager.add_student_marks(roll, subject, marks)

        elif choice == "3":
            roll = input("Enter student roll number: ")
            manager.show_student_result(roll)

        elif choice == "4":
            print("👋 Exiting... Bye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

