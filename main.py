from todo_app.task_manager import TaskManager


task_manager = TaskManager()

while True:
    print("-------------------------------")
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("Type exit to exit task manager")
    
    choice = input("Enter your choice: ")
    print("-------------------------------")
    

    if choice == '1':
        task_manager.add_task()
    elif choice == '2':
        task_manager.view_tasks()
    elif choice == '3':
        task_manager.mark_completed()
    elif choice == '4':
        task_manager.delete_task()
    elif choice.lower() == "exit":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
    




