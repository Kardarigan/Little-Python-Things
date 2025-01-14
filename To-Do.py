tasks = []

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Mark a task as done")
    print("5. Delete all tasks")
    print("6. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added successfully!")

def view_tasks():
    if tasks:
        for i in range(len(tasks)):
            status = "✅" if tasks[i]["done"] else "❌"
            print(f"{i + 1}. {tasks[i]['task']} [{status}]")
    else:
        print("No tasks in the to-do list.")

def delete_task():
    if not tasks:
        print("No tasks to delete.")
    else:
        view_tasks()
        task_num = int(input("Enter the task number to delete: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' deleted successfully!")
        else:
            print("Invalid task number.")

def mark_task_done():
    if not tasks:
        print("No tasks to mark as done.")
    else:
        view_tasks()
        task_num = int(input("Enter the task number to mark as done: "))
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            print(f"Task '{tasks[task_num - 1]['task']}' marked as done!")
        else:
            print("Invalid task number.")

def delete_all_tasks():
    global tasks
    tasks = []
    print("All tasks have been deleted!")

while True:
    display_menu()
    choice = input("Choose an option (1-6): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        mark_task_done()
    elif choice == '5':
        delete_all_tasks()
    elif choice == '6':
        print("Exiting the to-do list application. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")