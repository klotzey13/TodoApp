# Python To-Do App Project Plan

This document outlines the development phases, key Python concepts, and actionable steps for building a To-Do application in Python. This project serves as a foundational step for familiarizing myself with Python before diving into Machine Learning and AI.

---

## Project Goal

A functional To-Do list application where users can add, view, mark as complete, and delete tasks.

---

## **Phase 1: Core Functionality (Command-Line)**

**Objective:** Get comfortable with basic Python syntax, data structures, and file I/O.

### Python Concepts to Focus On:

* **Variables:** Storing task descriptions, statuses.
* **Data Types:** Strings (task names), Booleans (completed/not completed).
* **Lists:** To store multiple To-Do items.
* **Functions:** To encapsulate actions (add, view, complete, delete).
* **Conditional Statements (`if`/`elif`/`else`):** For user input handling.
* **Loops (`while`/`for`):** For displaying tasks and the main application loop.
* **File I/O (`open()`, `read()`, `write()`, `close()`, `with open(...) as f:`):** For data persistence.

### Actionable Steps:

#### Setup
* [done] Create a new project folder `python-todo-app`.
* [done ] Initialize a Git repository in `python-todo-app` (e.g., `git init`).
* [done] Create a virtual environment `venv` in the project folder (e.g., `python -m venv venv`).
* [done] Activate the virtual environment (e.g., `source venv/bin/activate` on Linux/macOS, or `.\venv\Scripts\activate` on Windows PowerShell).
* [done] Create `main.py` (or `todo_app.py`) file for your application code.
* [done] Add this `PLAN.md` file to the project folder.
* [done] Make initial Git commit: "Project setup and plan."

#### Core - Add Task Feature
* [done] Define an empty list `tasks` at the top of `main.py` to hold your To-Do items.
* [done] Create a function `add_task()` that takes no arguments.
* [ ] Inside `add_task()`, use `input()` to get a task description from the user.
* [ ] Append the new task description (as a string) to the `tasks` list.
* [ ] Add a temporary call to `add_task()` in the main part of the script for testing.
* [ ] Test `add_task()` by running the script.
* [ ] Make Git commit: "Implemented basic add_task function."

#### Core - View Tasks Feature
* [ ] Create a function `view_tasks()`.
* [ ] Inside `view_tasks()`, loop through the `tasks` list.
* [ ] For each task, print it with an index number (e.g., "1. Buy groceries").
* [ ] Update the main application loop (or add a temporary call) to allow calling `view_tasks()`.
* [ ] Test `view_tasks()` after adding a few tasks.
* [ ] Make Git commit: "Added view_tasks functionality."

#### Core - Mark Task Complete Feature
* [ ] Decide on a simple way to represent "completed" status for each task (e.g., store tasks as `[description, is_completed_boolean]` pairs in the list, or prefix with `[X]` when viewing).
* [ ] Create a function `mark_task_complete()`.
* [ ] Prompt the user for the number of the task to mark complete.
* [ ] Validate the input (is it a number? is it within range?).
* [ ] Update the status of the selected task in the `tasks` list.
* [ ] Update `view_tasks()` to display the completed status clearly (e.g., `[X] Task`, `[ ] Task`).
* [ ] Make Git commit: "Implemented mark_task_complete functionality."

#### Core - Delete Task Feature
* [ ] Create a function `delete_task()`.
* [ ] Prompt the user for the number of the task to delete.
* [ ] Validate the input.
* [ ] Remove the selected task from the `tasks` list (be careful with list indexing after deletion).
* [ ] Make Git commit: "Added delete_task functionality."

#### Core - Main Application Loop
* [ ] Implement a `while True` loop that continuously presents options to the user (e.g., `(a)dd, (v)iew, (m)ark complete, (d)elete, (q)uit`).
* [ ] Use `input()` to get user choices.
* [ ] Use `if`/`elif`/`else` to call the appropriate functions based on user input.
* [ ] Add a way to break the loop when the user chooses to quit.
* [ ] Make Git commit: "Created main application loop."

#### Persistence - Basic File I/O
* [ ] Create a function `load_tasks()` that reads tasks from a text file (e.g., `tasks.txt`).
* [ ] When loading, decide how to parse tasks and their status from each line.
* [ ] Call `load_tasks()` at the beginning of the program to populate the `tasks` list.
* [ ] Create a function `save_tasks()` that writes the current `tasks` list to `tasks.txt`.
* [ ] Call `save_tasks()` just before the program exits (e.g., when 'q' is chosen).
* [ ] Handle `FileNotFoundError` in `load_tasks()` (start with an empty list if file doesn't exist).
* [ ] Make Git commit: "Added basic file I/O for persistence."

---

## **Phase 2: Enhancements & Best Practices**

**Objective:** Improve user experience, code organization, and robustness.

### Python Concepts to Focus On:

* **Error Handling (`try`/`except`):** For robust input validation and file operations.
* **Classes and Objects (OOP):** Define a `Task` class for better data encapsulation.
* **Modules and Packages:** Organize code into separate `.py` files.
* **JSON Module (`import json`):** For structured data persistence.
* **Virtual Environments:** Reinforce their usage (already set up, but understand why).

### Actionable Steps:

#### Robust Error Handling
* [ ] Implement `try-except` blocks around `input()` where numerical input is expected, catching `ValueError`.
* [ ] Implement `try-except` blocks for index out of range errors when selecting tasks.
* [ ] Refine `load_tasks()` to robustly handle `FileNotFoundError` and potentially corrupted file data.
* [ ] Make Git commit: "Implemented basic error handling for user input and file loading."

#### Object-Oriented Design (OOP)
* [ ] Create a new file `task.py`.
* [ ] Define a `Task` class in `task.py` with attributes: `description` (string) and `completed` (boolean, default `False`).
* [ ] Add an `__init__` method to the `Task` class.
* [ ] Add a `__str__` method to the `Task` class for pretty printing of tasks.
* [ ] Modify `add_task()` to create `Task` objects instead of just strings.
* [ ] Modify `view_tasks()` to work with `Task` objects and display their `description` and `completed` status.
* [ ] Modify `mark_task_complete()` and `delete_task()` to operate on `Task` objects.
* [ ] Update `main.py` to import the `Task` class from `task.py`.
* [ ] Make Git commit: "Refactored with Task class for OOP."

#### JSON-based Persistence
* [ ] Modify `save_tasks()`:
    * Iterate through the `tasks` list (which now contains `Task` objects).
    * Convert each `Task` object into a dictionary (e.g., `{'description': '...', 'completed': True}`).
    * Use `json.dump()` to write the list of dictionaries to `tasks.json`.
* [ ] Modify `load_tasks()`:
    * Use `json.load()` to read the list of dictionaries from `tasks.json`.
    * Iterate through the loaded dictionaries and reconstruct `Task` objects.
* [ ] Test loading and saving thoroughly to ensure data integrity.
* [ ] Make Git commit: "Switched persistence to JSON format."

#### Code Modularization
* [ ] Create a new file `task_manager.py`.
* [ ] Move all core To-Do list manipulation functions (`add_task`, `view_tasks`, `mark_task_complete`, `delete_task`, `load_tasks`, `save_tasks`) into `task_manager.py`.
* [ ] Update `main.py` to import functions from `task_manager.py`.
* [ ] Ensure all necessary imports are handled correctly in `task_manager.py` (e.g., `from task import Task`, `import json`).
* [ ] Make Git commit: "Modularized code into task_manager.py."

---

## **Phase 3: Optional GUI (Graphical User Interface)**

**Objective:** Move beyond the command line to a more user-friendly interface.

### Python Concepts to Focus On:

* **GUI Frameworks:** Tkinter (built-in) recommended for simplicity.
* **Event Handling:** Responding to button clicks, text input, etc.

### Actionable Steps (Choose one GUI framework, Tkinter is suggested):

#### Tkinter - Basic Window
* [ ] Install Tkinter if not already available (usually built-in).
* [ ] Create a new file `gui_app.py`.
* [ ] Create a basic Tkinter window with a title.
* [ ] Run `gui_app.py` to ensure the window appears.
* [ ] Make Git commit: "Created basic Tkinter window."

#### Tkinter - Add Task GUI
* [ ] Add a `Label` for "New Task:".
* [ ] Add an `Entry` widget for user input of new task descriptions.
* [ ] Add a `Button` labeled "Add Task".
* [ ] Link the button's `command` to a function that calls your `add_task()` logic (from `task_manager.py`).
* [ ] Make Git commit: "Implemented add task GUI elements."

#### Tkinter - Display Tasks GUI
* [ ] Add a `Listbox` or `Text` widget to display current tasks.
* [ ] Create a function to refresh the display in the GUI whenever tasks are added, completed, or deleted.
* [ ] Update `view_tasks()` in `task_manager.py` (or create a new GUI-specific view function) to format tasks for the GUI display.
* [ ] Make Git commit: "Added task display to GUI."

#### Tkinter - Mark/Delete GUI
* [ ] Add buttons or context menus for "Mark Complete" and "Delete" actions.
* [ ] Connect these GUI elements to your existing `mark_task_complete()` and `delete_task()` logic.
* [ ] Ensure the GUI display updates after these actions.
* [ ] Make Git commit: "Added mark complete and delete functionality to GUI."

#### Tkinter - Connect Persistence
* [ ] Call `load_tasks()` when the GUI application starts.
* [ ] Call `save_tasks()` when the GUI application closes (e.g., using `window.protocol("WM_DELETE_WINDOW", save_and_quit_function)`).
* [ ] Make Git commit: "Integrated persistence with GUI."

---

## **Key Python Things to Learn (As You Build)**

* **Python Standard Library:** Actively explore modules like `json`, `os`, `sys`, `datetime`.
* **Package Management with `pip`:** Understand `pip install`, `pip uninstall`, `pip freeze > requirements.txt`.
* **Virtual Environments (`venv`):** Understand their purpose and consistent use.
* **Debugging:** Learn how to use your IDE's debugger (breakpoints, stepping, inspecting variables).
* **Basic Git/Version Control:** `git init`, `git add`, `git commit`, `git status`, `git log`.
* **Code Style (PEP 8):** Strive for readable, consistent code.
* **Docstrings and Comments:** Document your functions, classes, and complex logic.

---

## **Progress Tracking**

Use the checkboxes `[ ]` within this Markdown file to mark completed tasks as `[x]`.
Regularly commit your progress to Git with clear, descriptive messages.

---