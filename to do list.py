tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added:", task)

# Function to display the current tasks in the list
def show_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks in the list.")

# Main program loop
while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task_name = input("Enter the task: ")
        add_task(task_name)
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select again.")