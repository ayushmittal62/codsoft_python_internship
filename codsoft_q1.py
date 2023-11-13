# to do list 
# without using json
class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.status = "Incomplete"

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"{self.name} (Due: {self.due_date}) [Status: {self.status}]"


def main():
    tasks = []

    while True:
        # Display tasks
        
        print("To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

        # Display menu options
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            due_date = input("Enter due date: ")
            tasks.append(Task(name, due_date))
        elif choice == "2":
            task_idx = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= task_idx < len(tasks):
                tasks[task_idx].mark_complete()
            else:
                print("Invalid task number.")
        elif choice == "3":
            task_idx = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_idx < len(tasks):
                del tasks[task_idx]
            else:
                print("Invalid task number.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
