import tkinter as tk
from models.note import Note
from views.main_window import MainWindow
from controllers.note_controller import NoteController
from utils.file_manager import FileManager

root = MainWindow()  # No initial controller needed
controller = NoteController(root)  # Pass the view directly
root.controller = controller  # Assign controller *before* creating widgets
root.create_widgets()  # Create widgets *after* controller is assigned

root.mainloop()