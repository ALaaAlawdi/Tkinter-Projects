import tkinter as tk
from models.chatbot_model import ChatbotModel
from views.chatbot_view import ChatbotView
from controllers.chatbot_controller import ChatbotController

root = tk.Tk()
root.title("Simple Chatbot")

model = ChatbotModel()
view = ChatbotView(root)  # No controller initially

controller = ChatbotController(model, view)
view.controller = controller  # Assign the controller *before* creating widgets

view.create_widgets()  # Call create_widgets *after* controller is assigned

view.pack()
root.mainloop()