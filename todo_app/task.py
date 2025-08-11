from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class Task(BaseModel):
    """Represents a task with a unique ID, description, and completion status."""
    id: UUID = Field(default_factory=uuid4)
    description: str
    completed: bool = False

class TaskCreate(BaseModel):
    """A model for creating a new task, which only requires a description."""
    description: str
