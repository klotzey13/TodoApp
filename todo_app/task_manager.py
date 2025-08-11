from typing import List
from todo_app.task import Task

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []
        
    def add_task(self):
        task_description = input("Enter task description: ")
        self.tasks.append(Task(task_description))
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for i,t in enumerate(self.tasks):
                print(f"{i+1}. {"[X]" if t.completed else '[ ]'} {t.description}")

    def mark_completed(self):
        self.view_tasks()
        task_index = int(input("Enter the task number to mark as completed: "))
        
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index-1].mark_completed()
        else:
            print("Invalid task number.")

    def delete_task(self):
        self.view_tasks()
        if not self.tasks:
            return # No tasks to delete

        try:
            task_number_str = input("Enter the task number to delete: ")
            task_index = int(task_number_str) - 1
            
            if 0 <= task_index < len(self.tasks):
                removed_task = self.tasks.pop(task_index)
                print(f"Task '{removed_task.description}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")