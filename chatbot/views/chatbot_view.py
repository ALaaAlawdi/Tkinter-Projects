import tkinter as tk
from tkinter import ttk

class ChatbotView(tk.Frame):
    def __init__(self, master, controller=None):  # Controller is optional initially
        super().__init__(master)
        self.controller = controller

    def create_widgets(self):  # Create widgets *after* controller is assigned
        self.chat_log = tk.Text(self, width=50, height=10)
        self.chat_log.pack(pady=10)

        self.user_input = ttk.Entry(self, width=40)
        self.user_input.pack(pady=5)

        send_button = ttk.Button(self, text="Send", command=lambda: self.controller.send_message()) # Corrected
        send_button.pack()

    def display_message(self, message, sender="Bot"):
        self.chat_log.insert(tk.END, f"{sender}: {message}\n")
        self.chat_log.see(tk.END)  # Scroll to the bottom

    def get_user_input(self):
        return self.user_input.get()

    def clear_user_input(self):
        self.user_input.delete(0, tk.END)