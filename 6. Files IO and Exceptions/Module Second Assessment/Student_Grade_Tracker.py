import os

GRADE_FILE = r"D:\RoboGarden -- Introduction to Python\6. Files IO and Exceptions\Module Second Assessment\grades.txt"

def input_grades():
    """
    Input grades for subjects and store them in a file.
    """
    grades = {}
    try:
        while True:
            subject = input("Enter the subject name (or type 'done' to finish): ").strip()
            if subject.lower() == "done":
                break
            grade = input(f"Enter the grade for {subject}: ").strip()
            if not grade.replace(".", "", 1).isdigit():  # Validate numeric input
                print("Invalid grade. Please enter a numeric value.")
                continue
            grades[subject] = float(grade)
        save_grades_to_file(grades)
    except Exception as e:
        print(f"An error occurred: {e}")

def save_grades_to_file(grades):
    """
    Save grades to a file for persistent storage.
    """
    try:
        with open(GRADE_FILE, "a") as file:
            for subject, grade in grades.items():
                file.write(f"{subject}:{grade}\n")
        print("Grades have been saved.")
    except PermissionError:
        print("Error: Permission denied. Unable to write to the grades file.")
    except Exception as e:
        print(f"An unexpected error occurred while saving grades: {e}")

def read_grades():
    """
    Read grades from the file and return them as a dictionary.
    """
    if not os.path.exists(GRADE_FILE):
        print("No grades found. Please input grades first.")
        return {}

    try:
        grades = {}
        with open(GRADE_FILE, "r") as file:
            for line in file:
                subject, grade = line.strip().split(":")
                grades[subject] = float(grade)
        return grades
    except ValueError:
        print("Error: Invalid data in the grades file.")
        return {}
    except PermissionError:
        print("Error: Permission denied. Unable to read the grades file.")
        return {}

def calculate_average(grades):
    """
    Calculate and display the average grade.
    """
    if not grades:
        print("No grades available to calculate the average.")
        return
    average = sum(grades.values()) / len(grades)
    print(f"The average grade is: {average:.2f}")

def main():
    while True:
        print("\nGrade Tracking System")
        print("1. Input Grades")
        print("2. View Grades and Calculate Average")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            input_grades()
        elif choice == "2":
            grades = read_grades()
            if grades:
                print("\nGrades:")
                for subject, grade in grades.items():
                    print(f"{subject}: {grade:.2f}")
                calculate_average(grades)
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
