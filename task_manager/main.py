import tkinter as tk
from database.database_manager import DatabaseManager
from views.main_page import MainPage
from views.add_task_page import AddTaskPage
from controllers.task_controller import TaskController


root = tk.Tk()
root.title("مدير المهام")

database_manager = DatabaseManager()

main_page = MainPage(root)
add_task_page = AddTaskPage(root)

task_controller = TaskController(database_manager, main_page, add_task_page)

main_page.controller = task_controller
add_task_page.controller = task_controller  # Assign controller to add_task_page

main_page.create_widgets()  # Create widgets *after* controller assignment
add_task_page.create_widgets()  # Create widgets *after* controller assignment

task_controller.load_tasks()
main_page.pack()

root.mainloop()
database_manager.close()