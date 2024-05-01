tasks = []

def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added to your to-do list.")

def mark_task_completed():
    task_number = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_number <= len(tasks):
        completed_task = tasks.pop(task_number - 1)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task number.")

def remove_task():
    task_number = int(input("Enter the task number to remove: "))
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' removed from your to-do list.")
    else:
        print("Invalid task number.")

def quit_app():
    print("Thank you for using the To-Do List. Goodbye!")
    exit()

menu_options = {
    '1': display_tasks,
    '2': add_task,
    '3': mark_task_completed,
    '4': remove_task,
    '5': quit_app
}

while True:
    print("\nTo-Do List Menu:")
    print("1. Display To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Completed")
    print("4. Remove a Task")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice in menu_options:
        menu_options[choice]()
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
