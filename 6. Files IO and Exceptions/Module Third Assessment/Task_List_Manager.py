import os

TASK_FILE = r"D:\RoboGarden -- Introduction to Python\6. Files IO and Exceptions\Module Third Assessment\tasks.txt"

def load_tasks():
    """
    Load tasks from the file and return them as a list.
    """
    try:
        if not os.path.exists(TASK_FILE):
            return []  # Return an empty list if the file doesn't exist
        with open(TASK_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []

def save_tasks(tasks):
    """
    Save the list of tasks to the file.
    """
    try:
        with open(TASK_FILE, "w") as file:
            for task in tasks:
                file.write(f"{task}\n")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def add_task(tasks):
    """
    Add a new task to the list.
    """
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")

def remove_task(tasks):
    """
    Remove a task from the list.
    """
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove (0 to cancel): "))
        if task_num == 0:
            print("Task removal canceled.")
            return
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def view_tasks(tasks):
    """
    View the current list of tasks.
    """
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nCurrent Task List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\nTask List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Exiting the Task List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
