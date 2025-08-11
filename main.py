from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, status
from typing import List
from uuid import UUID

from todo_app.task_manager import TaskManager
from todo_app.task import Task, TaskCreate

task_manager = TaskManager("tasks.json")

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manages application startup and shutdown events.
    On shutdown, it saves the current tasks to a file.
    """
    # Code before the yield runs on startup. Nothing to do here for now.
    yield
    # Code after the yield runs on shutdown.
    task_manager.save_tasks()
    print("Tasks have been saved.")

app = FastAPI(title="To-Do List API", lifespan=lifespan)

@app.get("/tasks", response_model=List[Task], tags=["Tasks"])
def get_all_tasks():
    """Retrieve all tasks."""
    return task_manager.get_all_tasks()

@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED, tags=["Tasks"])
def create_task(task_data: TaskCreate):
    """Create a new task."""
    return task_manager.add_task(task_data)

@app.put("/tasks/{task_id}/complete", response_model=Task, tags=["Tasks"])
def mark_task_as_completed(task_id: UUID):
    """Mark a specific task as completed."""
    task = task_manager.mark_completed(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Tasks"])
def delete_task(task_id: UUID):
    """Delete a specific task."""
    success = task_manager.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}