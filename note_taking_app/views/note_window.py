import tkinter as tk
from tkinter import ttk

class NoteWindow(tk.Toplevel):  # Toplevel for a separate window
    def __init__(self, master, title, content, controller):
        super().__init__(master)
        self.title(title)
        self.controller = controller
        self.note_title = title # Store the title
        self._create_widgets(content)

    def _create_widgets(self, content):
        title_label = ttk.Label(self, text="Title:")
        title_label.pack(pady=(10, 0), padx=10, anchor=tk.W) # Left align

        self.title_entry = ttk.Entry(self)
        self.title_entry.insert(0, self.note_title) # Insert the title
        self.title_entry.pack(pady=5, padx=10, fill=tk.X)

        content_label = ttk.Label(self, text="Content:")
        content_label.pack(pady=(10, 0), padx=10, anchor=tk.W)

        self.content_text = tk.Text(self, wrap=tk.WORD, height=10)
        self.content_text.insert(tk.END, content)
        self.content_text.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

        save_button = ttk.Button(self, text="Save", command=self.controller.save_note)
        save_button.pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.on_close) # Handle window close event

    def on_close(self):
        self.controller.close_note(self.note_title) # Pass the title to the controller
        self.destroy()

    def get_note_data(self):
        return self.title_entry.get(), self.content_text.get("1.0", tk.END).strip()