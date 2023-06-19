
tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index+1}. {task}")

def remove_task():
    view_tasks()
    if len(tasks) == 0:
        return

    choice = input("Enter the task number to remove: ")
    try:
        choice = int(choice)
        if choice > 0 and choice <= len(tasks):
            task = tasks.pop(choice - 1)
            print(f"Task '{task}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
    