import tkinter as tk
from tkinter import ttk

class MainPage(tk.Frame):
    def __init__(self, master, controller=None):
        super().__init__(master)
        self.controller = controller

    def create_widgets(self):
        self.task_listbox = tk.Listbox(self, width=50)
        self.task_listbox.pack(pady=10)

        # Use lambda for dynamic command creation:
        add_button = ttk.Button(self, text="إضافة مهمة", command=lambda: self.controller.show_add_task_page())
        add_button.pack()

        complete_button = ttk.Button(self, text="إكمال مهمة", command=lambda: self.controller.complete_selected_task())
        complete_button.pack()

    def update_task_list(self, tasks):
        self.task_listbox.delete(0, tk.END)
        for task in tasks:
            self.task_listbox.insert(tk.END, str(task))