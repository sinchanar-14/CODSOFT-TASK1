tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        for idx, task in enumerate(tasks):
            status = "✓" if task["done"] else "✗"
            print(f"{idx + 1}. [{status}] {task['task']}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added.")

def mark_done():
    view_tasks()
    try:
        task_no = int(input("Enter the number of the task to mark as done: "))
        tasks[task_no - 1]["done"] = True
        print("Task marked as done.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter the number of the task to delete: "))
        tasks.pop(task_no - 1)
        print("Task deleted.")
    except (ValueError, IndexError):
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
