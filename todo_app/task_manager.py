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
