class Task:
    def __init__(self, description, status="Incomplete"):
        self.description = description
        self.status = status


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. [{task.status}] {task.description}")

    def mark_complete(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].status = "Complete"
            print("Task marked as complete.")
        else:
            print("Invalid task index.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.status},{task.description}\n")

    def load_from_file(self, filename):
        self.tasks = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    status, description = line.strip().split(',', 1)
                    self.add_task(Task(description, status))
        except FileNotFoundError:
            pass


def main():
    todo_list = ToDoList()
    todo_list.load_from_file("todo.txt")

    while True:
        print("\n=== To-Do List ===")
        todo_list.display_tasks()

        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
    
            todo_list.add_task(Task(description))
        elif choice == "2":
            task_index = int(input("Enter task index to mark as complete: "))
            todo_list.mark_complete(task_index)
        elif choice == "3":
            todo_list.save_to_file("todo.txt")
            print("To-Do List saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()