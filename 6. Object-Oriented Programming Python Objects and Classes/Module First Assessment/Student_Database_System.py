class Student:
    """
    Class to represent a student with attributes and methods.
    """
    def __init__(self, name, age, grades=None):
        self.name = name
        self.age = age
        self.grades = grades if grades is not None else []

    def display_info(self):
        """
        Method to display student information.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def calculate_average(self):
        """
        Method to calculate the average grade.
        """
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


class StudentDatabase:
    """
    Class to manage a database of students.
    """
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grades):
        """
        Method to add a new student to the database.
        """
        student = Student(name, age, grades)
        self.students.append(student)

    def display_all_students(self):
        """
        Method to display information about all students.
        """
        if not self.students:
            print("No students in the database.")
            return
        for student in self.students:
            student.display_info()
            print(f"Average Grade: {student.calculate_average():.2f}")
            print("-" * 30)


def main():
    # Create the database
    db = StudentDatabase()

    # Add students to the database
    db.add_student("Alice", 20, [90, 85, 88])
    db.add_student("Bob", 22, [75, 80, 72])
    db.add_student("Charlie", 19, [95, 98, 92])

    # Display all students
    print("Student Database:")
    db.display_all_students()


main()
