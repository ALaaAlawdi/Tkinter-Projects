class ChatbotModel:
    def __init__(self):
        self.responses = {  # Basic responses (you can expand this)
            "hello": "Hi there!",
            "how are you": "I'm doing well, thank you.",
            "bye": "Goodbye!",
            "help": "I can answer simple questions. Try 'hello', 'how are you', or 'bye'."
        }

    def get_response(self, user_input):
        user_input = user_input.lower()  # Make input case-insensitive
        if user_input in self.responses:
            return self.responses[user_input]
        else:
            return "I don't understand that yet. Try 'help'."