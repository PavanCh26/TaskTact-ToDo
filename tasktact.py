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

def mark_done(tasks):
    """Mark a task as done."""
    if not tasks:
        print("No tasks to mark.")
        return
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            save_tasks(tasks)
            print(f"'{tasks[num]['task']}' marked as done!")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

def delete_task(tasks):
    """Delete a specific task."""
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)
            save_tasks(tasks)
            print(f"🗑️ Deleted '{removed['task']}'")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

# ---------- Main Menu ----------
def main():
    tasks = load_tasks()
    while True:
        print("\n--- TaskTact – Intelligent To-Do Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye! Stay productive.")
            break
        else:
            print("Invalid choice, try again.")

# ---------- Run ----------
if __name__ == "__main__":
    main()
