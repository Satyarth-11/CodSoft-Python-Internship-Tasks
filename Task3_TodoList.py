# Task 3: Simple To-Do List App

tasks = []

def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == '2':
        print("\nYour Tasks:")
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks yet.")

    elif choice == '3':
        task_num = int(input("Enter task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")

    elif choice == '4':
        print("Exiting To-Do List.")
        break

    else:
        print("Invalid input.")
