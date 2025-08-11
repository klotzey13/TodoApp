import json
from typing import List
from uuid import UUID
from .task import Task, TaskCreate

class TaskManager:
    def __init__(self, filepath='tasks.json'):
        self.filepath = filepath
        self.tasks: List[Task] = []
        self.load_tasks()

    def get_all_tasks(self) -> List[Task]:
        return self.tasks

    def get_task_by_id(self, task_id: UUID) -> Task | None:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def add_task(self, task_data: TaskCreate) -> Task:
        new_task = Task(description=task_data.description)
        self.tasks.append(new_task)
        self.save_tasks() # Save after modification
        return new_task

    def mark_completed(self, task_id: UUID) -> Task | None:
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = True
            self.save_tasks() # Save after modification
        return task

    def update_task(self, task_id: UUID, updated_task: Task) -> Task | None:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks[i] = updated_task
                self.save_tasks() # Save after modification
                return updated_task
        return None

    def delete_task(self, task_id: UUID) -> bool:
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks() # Save after modification
            return True
        return False

    def save_tasks(self):
        """Saves the current list of tasks to the JSON file."""
        if not self.tasks:
            print("No tasks to save.")
            return
        try:
            with open(self.filepath, 'w') as f:
                json_data = [task.model_dump() for task in self.tasks]
                json.dump(json_data, f, indent=4)
        except IOError as e:
            print(f"Error saving tasks to {self.filepath}: {e}")

    def load_tasks(self):
        """Loads tasks from the JSON file when the application starts."""
        try:
            with open(self.filepath, 'r') as f:
                tasks_data = json.load(f)
                # Recreate Task objects from the loaded data
                self.tasks = [Task(**data) for data in tasks_data]
        except FileNotFoundError:
            pass
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading or parsing {self.filepath}: {e}. Starting with an empty list.")
