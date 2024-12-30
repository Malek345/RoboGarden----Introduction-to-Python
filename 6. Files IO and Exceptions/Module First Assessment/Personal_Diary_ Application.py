import os
from datetime import datetime

DIARY_FILE = r"\RoboGarden -- Introduction to Python\6. Files IO and Exceptions\Module First Assessment\diary.txt"

def add_entry(entry, add_timestamp=True):
    """
    Add a new diary entry to the file.
    """
    try:
        with open(DIARY_FILE, "a") as file:
            if add_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{timestamp} - {entry}\n")
            else:
                file.write(f"{entry}\n")
        print("Entry added successfully.")
    except PermissionError:
        print("Error: Permission denied. Unable to write to the diary file.")

def view_entries():
    """
    View all previous diary entries.
    """
    try:
        if os.path.exists(DIARY_FILE):
            with open(DIARY_FILE, "r") as file:
                content = file.read()
                print("\nPrevious Diary Entries:")
                print("-" * 40)
                print(content)
        else:
            print("No diary entries found.")
    except PermissionError:
        print("Error: Permission denied. Unable to read the diary file.")

def main():
    while True:
        print("\nPersonal Diary")
        print("1. Add a New Entry")
        print("2. View Previous Entries")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            entry = input("Write your entry: ")
            add_timestamp = input("Add a timestamp? (yes/no): ").strip().lower() == "yes"
            add_entry(entry, add_timestamp)
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Exiting the diary. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
