import os

FILE_NAME = "tasks.txt"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return [task.strip() for task in file.readlines()]
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks available.")
    else:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST APP =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        show_tasks(tasks)

    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added successfully!")

    elif choice == "3":
        show_tasks(tasks)

        if tasks:
            try:
                index = int(input("Enter task number to delete: ")) - 1

                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    save_tasks(tasks)
                    print(f"🗑 Deleted: {removed}")
                else:
                    print("❌ Invalid task number.")

            except ValueError:
                print("❌ Please enter a valid number.")

    elif choice == "4":
        print("👋 Exiting To-Do App...")
        break

    else:
        print("❌ Invalid choice.")
