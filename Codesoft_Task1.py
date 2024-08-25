# <------------------------------------To-do list ---------------------------------->

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Added task: "{task}"')

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Removed task: "{removed_task}"')
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in your to-do list.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def clear_tasks(self):
        self.tasks.clear()
        print("Cleared all tasks.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. View all tasks")
        print("4. Clear all tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                todo_list.remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            todo_list.clear_tasks()
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid number.")

if __name__ == "__main__":
    main()
