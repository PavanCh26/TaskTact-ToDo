import json
import datetime

FILE = "tasks.json"

# ---------- File Handling ----------
def load_tasks():
    """Load tasks from JSON file."""
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# ---------- Task Operations ----------
def add_task(tasks):
    """Add a new task with optional due date."""
    task_name = input("Enter task name: ").strip()
    if not task_name:
        print("Task cannot be empty!")
        return

    due_date = input("Enter due date (YYYY-MM-DD or leave blank): ").strip()
    task = {
        "task": task_name,
        "due": due_date if due_date else "No due date",
        "done": False,
        "created": str(datetime.date.today())
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task_name}' added successfully!")

def view_tasks(tasks):
    """View all tasks with status."""
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "Done" if t["done"] else "Pending"
        print(f"{i}. {t['task']} (Due: {t['due']}) - {status}")

def update_task(tasks):
    """Update an existing task."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to update: ")) - 1
        if 0 <= num < len(tasks):
            new_name = input("Enter new task name (leave blank to keep same): ").strip()
            new_due = input("Enter new due date (YYYY-MM-DD or leave blank to keep same): ").strip()
            if new_name:
                tasks[num]["task"] = new_name
            if new_due:
                tasks[num]["due"] = new_due
            save_tasks(tasks)
            print(f"Task '{tasks[num]['task']}' updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_done(tasks):
    """Mark or unmark a task as done."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to toggle done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = not tasks[num]["done"]
            save_tasks(tasks)
            state = "Done" if tasks[num]["done"] else "Pending"
            print(f"Task '{tasks[num]['task']}' marked as {state}.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a specific task."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)
            save_tasks(tasks)
            print(f"Deleted '{removed['task']}' successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# ---------- Main Menu ----------
def main():
    tasks = load_tasks()
    while True:
        print("\n--- TaskTact – Intelligent To-Do Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark / Unmark Done")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye! Stay productive.")
            break
        else:
            print("Invalid choice, please try again.")

# ---------- Run ----------
if __name__ == "__main__":
    main()
