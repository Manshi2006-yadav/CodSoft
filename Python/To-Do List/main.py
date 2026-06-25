from assets.task_manager import *

while True:

    print("\n TO-DO LIST ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        task_name = input("Enter task: ")

        add_task(task_name)

        print("Task added successfully.")

    elif choice == "2":

        tasks = view_tasks()

        if len(tasks) == 0:
            print("No tasks available.")

        else:

            print("\nYour Tasks:\n")

            for index, task in enumerate(tasks, start=1):

                status = "Completed" if task["completed"] else "Pending"

                print(
                    f"{index}. {task['task']} - [{status}]"
                )

    elif choice == "3":

        tasks = view_tasks()

        if len(tasks) == 0:
            print("No tasks available.")

        else:

            try:
                task_num = int(
                    input("Enter task number: ")
                )

                if mark_completed(task_num - 1):
                    print("Task marked as completed.")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":

        tasks = view_tasks()

        if len(tasks) == 0:
            print("No tasks available.")

        else:

            try:
                task_num = int(
                    input("Enter task number to delete: ")
                )

                if delete_task(task_num - 1):
                    print("Task deleted successfully.")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":

        print("Exiting To-Do List...")
        break

    else:

        print("Invalid choice.")