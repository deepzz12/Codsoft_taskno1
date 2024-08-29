def display_tasks():
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour to-do list:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Function to add a task to the list
def add_task():
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added to your to-do list.")

# Function to remove a task from the list
def remove_task():
    display_tasks()
    if tasks:
        task_num = int(input("\nEnter the number of the task you want to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed from your to-do list.")
        else:
            print("Invalid task number.")

# Function to show the menu
def show_menu():
print("\nTo-Do List Menu:")
    print("1. Display tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

# Main loop
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
