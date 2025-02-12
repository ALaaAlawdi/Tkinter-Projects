import tkinter as tk
from tkinter import ttk

class AddTaskPage(tk.Frame):
    def __init__(self, master, controller=None):  # Controller is optional initially
        super().__init__(master)
        self.controller = controller

    def create_widgets(self):  # Create widgets *after* controller is assigned
        title_label = ttk.Label(self, text="العنوان:")
        title_label.grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = ttk.Entry(self)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        description_label = ttk.Label(self, text="الوصف:")
        description_label.grid(row=1, column=0, padx=5, pady=5)
        self.description_entry = ttk.Entry(self)
        self.description_entry.grid(row=1, column=1, padx=5, pady=5)

        add_button = ttk.Button(self, text="إضافة", command=lambda: self.controller.add_task()) # lambda is here
        add_button.grid(row=2, column=0, columnspan=2, pady=10)

        back_button = ttk.Button(self, text="العودة", command=lambda: self.controller.show_main_page()) # lambda is here
        back_button.grid(row=3, column=0, columnspan=2, pady=5)

    def get_task_data(self):
        return (self.title_entry.get(), self.description_entry.get())

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)