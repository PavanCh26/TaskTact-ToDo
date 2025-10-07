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
    """Add a new task with due date validation."""
    task_name = input("Enter task name: ").strip()
    if not task_name:
        print("Task cannot be empty!")
        return

    due_date = input("Enter due date (YYYY-MM-DD or leave blank): ").strip()
    if due_date:
        try:
            due = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
            today = datetime.date.today()
            if due < today:
                print("⚠️  Due date cannot be before today! Please enter a valid future date.")
                return
        except ValueError:
            print("⚠️  Invalid date format. Please use YYYY-MM-DD.")
            return
    else:
        due_date = "No due date"

    task = {
        "task": task_name,
        "due": due_date,
        "done": False,
        "created": str(datetime.date.today())
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task '{task_name}' added successfully!")

def view_tasks(tasks):
    """View all tasks with their status."""
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "Done" if t["done"] else "Pending"
        print(f"{i}. {t['task']} (Due: {t['due']}) - {status}")

def update_task(tasks):
    """Edit or update a task's name or due date."""
    if not tasks:
        print("No tasks available to update.")
        return
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to update: ")) - 1
        if 0 <= num < len(tasks):
            new_name = input("Enter new task name (leave blank to keep same): ").strip()
            new_due = input("Enter new due date (YYYY-MM-DD or leave blank to keep same): ").strip()
            if new_name:
                tasks[num]["task"] = new_name
            if new_due:
                try:
                    due = datetime.datetime.strptime(new_due, "%Y-%m-%d").date()
                    today = datetime.date.today()
                    if due < today:
                        print("⚠️  Due date cannot be before today! Keeping old date.")
                    else:
                        tasks[num]["due"] = new_due
                except ValueError:
                    print("⚠️  Invalid date format. Keeping old date.")
            save_tasks(tasks)
            print("📝 Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_done(tasks):
    """Mark or unmark a task as done."""
    if not tasks:
        print("No tasks available.")
        return
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark/unmark as done: ")) - 1
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
    if not tasks:
        print("No tasks available.")
        return
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)
            save_tasks(tasks)
            print(f"🗑️  Deleted '{removed['task']}' successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def export_tasks(tasks):
    """Export all tasks to a JSON file."""
    if not tasks:
        print("No tasks to export.")
        return
    export_file = "TaskTact_Export.json"
    with open(export_file, "w") as f:
        json.dump(tasks, f, indent=4)
    print(f"📦 Tasks exported successfully to '{export_file}'.")

# ---------- Main Menu ----------
def main():
    tasks = load_tasks()
    while True:
        print("\n--- TaskTact – Intelligent To-Do Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark/Unmark Done")
        print("5. Delete Task")
        print("6. Export Tasks to JSON")
        print("7. Exit")

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
            export_tasks(tasks)
        elif choice == "7":
            print("👋 Goodbye! Stay productive.")
            break
        else:
            print("Invalid choice, please try again.")

# ---------- Run ----------
if __name__ == "__main__":
    main()
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a specific task."""
    if not tasks:
        print("No tasks available.")
        return
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)
            save_tasks(tasks)
            print(f"🗑️  Deleted '{removed['task']}' successfully.")
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
        print("4. Mark/Unmark Done")
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
            print("👋 Goodbye! Stay productive.")
            break
        else:
            print("Invalid choice, please try again.")

# ---------- Run ----------
if __name__ == "__main__":
    main()# ---------- Main Menu ----------
def main():
    tasks = load_tasks()
    while True:
        print("\n--- TaskTact – Intelligent To-Do Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark/Unmark Done")
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
