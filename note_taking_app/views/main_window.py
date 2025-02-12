import tkinter as tk
from tkinter import ttk, messagebox

class MainWindow(tk.Tk):
    def __init__(self, controller=None):  # Controller is optional initially
        super().__init__()
        self.controller = controller
        self.title("Simple Note Taking App")

    def create_widgets(self):  # Call this *after* controller is assigned
        # Note Listbox
        self.note_listbox = tk.Listbox(self, width=40, height=10)
        self.note_listbox.pack(pady=10, padx=10)

        # Use lambda with event argument to delay method call
        self.note_listbox.bind("<Double-Button-1>", lambda event: self.controller.open_note(event))  # Corrected

        # Buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=5, padx=10)

        add_button = ttk.Button(button_frame, text="Add Note", command=self.controller.add_note)
        add_button.grid(row=0, column=0, padx=5)

        delete_button = ttk.Button(button_frame, text="Delete Note", command=self.controller.delete_note)
        delete_button.grid(row=0, column=1, padx=5)

    def update_note_list(self, notes):
        self.note_listbox.delete(0, tk.END)
        for note in notes:
            self.note_listbox.insert(tk.END, note)

    def show_note_content(self, title, content):
        NoteWindow(self, title, content, self.controller)

    def show_message(self, message):
      messagebox.showinfo("Info", message)