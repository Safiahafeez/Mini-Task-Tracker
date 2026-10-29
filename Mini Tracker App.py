# mini_task_tracker.py

import json

# JSON file for storing tasks
TASKS_FILE = "tasks.json"


# Load saved tasks from the JSON file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Invalid JSON file. Starting with an empty task list.")
        return []


# Save tasks to the JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


# Add a new task
def add_task(tasks):
    title = input("Task title: ").strip()

    if title == "":
        print("Task title cannot be empty.")
        return

    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")


# Display all tasks
def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    for number, task in enumerate(tasks, start=1):
        if task["done"]:
            status = "Done"
        else:
            status = "Pending"

        print(f"{number}. {task['title']} [{status}]")


# Get and validate a task number
def get_task_number(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return None

    try:
        number = int(input("Task number: "))
    except ValueError:
        print("Invalid task number. Please enter a number.")
        return None

    if number < 1 or number > len(tasks):
        print("Invalid task number. Please select an existing task.")
        return None

    return number - 1


# Mark a task as completed
def complete_task(tasks):
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    index = get_task_number(tasks)

    if index is None:
        return

    tasks[index]["done"] = True
    save_tasks(tasks)
    print("Task completed.")


# Delete a task
def delete_task(tasks):
    view_tasks(tasks)

    if len(tasks) == 0:
        return

    index = get_task_number(tasks)

    if index is None:
        return

    tasks.pop(index)
    save_tasks(tasks)
    print("Task deleted.")


# Display the menu until the user chooses Exit
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TASK TRACKER ---")
        print("1. Add")
        print("2. View")
        print("3. Complete")
        print("4. Delete")
        print("5. Exit")

        choice = input("Choice: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break

        else:
            print("Invalid menu choice. Please enter 1, 2, 3, 4, or 5.")


# Run the program
if __name__ == "__main__":
    main()