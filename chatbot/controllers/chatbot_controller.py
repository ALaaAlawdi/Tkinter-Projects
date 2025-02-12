class ChatbotController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def send_message(self):
        user_input = self.view.get_user_input()
        self.view.display_message(user_input, "You")  # Display user message

        bot_response = self.model.get_response(user_input)
        self.view.display_message(bot_response)  # Display bot response

        self.view.clear_user_input()  # Clear the input field