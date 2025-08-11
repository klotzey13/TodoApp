class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True
        print(f"Task '{self.description}' marked as completed.")

    
